"""Minimal Lightning chat-completions streaming client."""

from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator, Sequence
from dataclasses import dataclass
import json
import logging
from typing import Any

import httpx


logger = logging.getLogger(__name__)


class LightningProtocolError(RuntimeError):
    """The upstream stream did not follow the advertised SSE protocol."""


@dataclass(frozen=True)
class ToolCallDelta:
    index: int
    call_id: str = ""
    name: str = ""
    arguments: str = ""
    extra_content: dict[str, Any] | None = None


@dataclass(frozen=True)
class ChatDelta:
    content: str = ""
    tool_calls: tuple[ToolCallDelta, ...] = ()
    finish_reason: str | None = None


class LightningClient:
    def __init__(
        self,
        http: httpx.AsyncClient,
        *,
        model: str,
        reasoning_effort: str | None = None,
        fallback_model: str | None = None,
    ) -> None:
        self._http = http
        self._model = model
        self._reasoning_effort = reasoning_effort
        self._fallback_model = fallback_model

    async def stream(
        self,
        *,
        messages: Sequence[dict[str, Any]],
        tools: Sequence[dict[str, Any]],
    ) -> AsyncIterator[ChatDelta]:
        body = {
            "model": self._model,
            "messages": list(messages),
            "tools": list(tools),
            "tool_choice": "auto",
            "stream": True,
        }
        if self._reasoning_effort is not None:
            body["reasoning_effort"] = self._reasoning_effort
        attempt = 0
        while True:
            emitted = False
            try:
                async for delta in self._stream_once(body):
                    emitted = True
                    yield delta
                return
            except (httpx.TransportError, httpx.HTTPStatusError) as exc:
                status = (
                    exc.response.status_code
                    if isinstance(exc, httpx.HTTPStatusError)
                    else None
                )
                retryable = isinstance(exc, httpx.TransportError) or (
                    status in {408, 409, 429}
                    or (status is not None and status >= 500)
                )
                # Gemini's documented client behaviour uses up to four attempts
                # for HTTP capacity/rate errors. Network failures only get two;
                # otherwise a 90-second read timeout could take many minutes.
                max_attempts = 2 if isinstance(exc, httpx.TransportError) else 4
                if not emitted and retryable and attempt + 1 < max_attempts:
                    await asyncio.sleep(2.0**attempt)
                    attempt += 1
                    continue
                if (
                    not emitted
                    and status == 503
                    and self._fallback_model
                    and self._fallback_model != body["model"]
                ):
                    fallback_body = {**body, "model": self._fallback_model}
                    logger.warning(
                        "model unavailable after retries; using fallback model=%s",
                        self._fallback_model,
                    )
                    async for delta in self._stream_once(fallback_body):
                        yield delta
                    return
                raise

    async def _stream_once(
        self, body: dict[str, Any]
    ) -> AsyncIterator[ChatDelta]:
        async with self._http.stream(
            "POST", "chat/completions", json=body
        ) as response:
            response.raise_for_status()
            completed = False
            finished = False
            async for line in response.aiter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[6:]
                if data == "[DONE]":
                    completed = True
                    break
                payload = json.loads(data)
                choices = payload.get("choices", [])
                if not choices:
                    continue
                choice = choices[0]
                delta = choice.get("delta") or {}
                content = delta.get("content")
                if not isinstance(content, str):
                    content = ""
                # OpenAI and Lightning include ``index`` on each streamed tool-call
                # fragment. Gemini's OpenAI-compatible endpoint currently omits it,
                # while preserving the calls' array order. Use that position as the
                # protocol index so the agent can reconstruct both variants.
                tool_calls = tuple(
                    ToolCallDelta(
                        index=tool_call.get("index", position),
                        call_id=tool_call.get("id") or "",
                        name=(tool_call.get("function") or {}).get("name") or "",
                        arguments=(tool_call.get("function") or {}).get("arguments")
                        or "",
                        extra_content=(
                            tool_call.get("extra_content")
                            if isinstance(tool_call.get("extra_content"), dict)
                            else None
                        ),
                    )
                    for position, tool_call in enumerate(
                        delta.get("tool_calls") or ()
                    )
                )
                finish_reason = choice.get("finish_reason")
                if finish_reason is not None:
                    finished = True
                if content or tool_calls or finish_reason:
                    yield ChatDelta(
                        content=content,
                        tool_calls=tool_calls,
                        finish_reason=finish_reason,
                    )
            # OpenAI/Lightning terminate with ``data: [DONE]``. Gemini may
            # instead close the SSE response immediately after a choice with a
            # finish reason. Both are complete; a stream with neither remains
            # truncated and must not be accepted.
            if not completed and not finished:
                raise LightningProtocolError("Lightning stream ended without [DONE]")
