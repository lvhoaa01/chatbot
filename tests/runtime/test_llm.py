from __future__ import annotations

import asyncio
import json

import httpx
import pytest

from ontchatbot.runtime.llm import (
    ChatDelta,
    LightningClient,
    LightningProtocolError,
    ToolCallDelta,
)


def test_stream_reconstructs_the_lightning_tool_call_protocol() -> None:
    """Dropping a streamed argument fragment would make valid tool JSON invalid."""

    stream = """data: {"choices":[{"index":0,"delta":{"role":"assistant"},"finish_reason":null}]}\n\n
data: {"choices":[{"index":0,"delta":{"tool_calls":[{"index":0,"id":"call-1","type":"function","function":{"name":"lookup_academic_information","arguments":"{\\\"key"}}]},"finish_reason":null}]}\n\n
data: {"choices":[{"index":0,"delta":{"tool_calls":[{"index":0,"type":"","function":{"arguments":"words\\\":[\\\"học phí\\\"]}"}}]},"finish_reason":null}]}\n\n
data: {"choices":[{"index":0,"delta":{},"finish_reason":"tool_calls"}]}\n\n
data: [DONE]\n\n"""

    def respond(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/api/v1/chat/completions"
        return httpx.Response(
            200,
            headers={"Content-Type": "text/event-stream"},
            content=stream.encode(),
        )

    async def run() -> list[ChatDelta]:
        async with httpx.AsyncClient(
            base_url="https://lightning.test/api/v1/",
            transport=httpx.MockTransport(respond),
        ) as http:
            client = LightningClient(http, model="gemma")
            return [
                delta
                async for delta in client.stream(
                    messages=[{"role": "user", "content": "học phí"}],
                    tools=[{"type": "function", "function": {"name": "lookup"}}],
                )
            ]

    deltas = asyncio.run(run())

    assert deltas == [
        ChatDelta(
            tool_calls=(
                ToolCallDelta(
                    index=0,
                    call_id="call-1",
                    name="lookup_academic_information",
                    arguments='{"key',
                ),
            )
        ),
        ChatDelta(
            tool_calls=(
                ToolCallDelta(
                    index=0,
                    arguments='words":["học phí"]}',
                ),
            )
        ),
        ChatDelta(finish_reason="tool_calls"),
    ]


def test_stream_accepts_gemini_tool_calls_without_an_index() -> None:
    """Gemini keeps call order but omits OpenAI's optional streaming index."""

    stream = """data: {"choices":[{"delta":{"tool_calls":[{"id":"call-1","type":"function","function":{"name":"lookup_academic_information","arguments":"{\\"keywords\\":[\\"học phí\\"]}"},"extra_content":{"google":{"thought_signature":"signed"}}}]},"finish_reason":null}]}

data: {"choices":[{"delta":{},"finish_reason":"tool_calls"}]}

data: [DONE]

"""

    def respond(_request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            headers={"Content-Type": "text/event-stream"},
            content=stream.encode(),
        )

    async def run() -> list[ChatDelta]:
        async with httpx.AsyncClient(
            base_url="https://gemini.test/v1beta/openai/",
            transport=httpx.MockTransport(respond),
        ) as http:
            return [
                item
                async for item in LightningClient(http, model="gemini").stream(
                    messages=[], tools=[]
                )
            ]

    assert asyncio.run(run()) == [
        ChatDelta(
            tool_calls=(
                ToolCallDelta(
                    index=0,
                    call_id="call-1",
                    name="lookup_academic_information",
                    arguments='{"keywords":["học phí"]}',
                    extra_content={"google": {"thought_signature": "signed"}},
                ),
            )
        ),
        ChatDelta(finish_reason="tool_calls"),
    ]


def test_stream_sends_the_minimal_openai_compatible_request() -> None:
    seen: dict = {}

    def respond(request: httpx.Request) -> httpx.Response:
        seen.update(json.loads(request.content))
        return httpx.Response(
            200,
            headers={"Content-Type": "text/event-stream"},
            content=b'data: {"choices":[{"delta":{"content":"Xin chao"},"finish_reason":"stop"}]}\n\ndata: [DONE]\n\n',
        )

    messages = [{"role": "user", "content": "xin chào"}]
    tools = [{"type": "function", "function": {"name": "lookup"}}]

    async def run() -> list[ChatDelta]:
        async with httpx.AsyncClient(
            base_url="https://lightning.test/api/v1/",
            transport=httpx.MockTransport(respond),
        ) as http:
            return [
                item
                async for item in LightningClient(http, model="gemma").stream(
                    messages=messages, tools=tools
                )
            ]

    assert asyncio.run(run()) == [
        ChatDelta(content="Xin chao", finish_reason="stop")
    ]
    assert seen == {
        "model": "gemma",
        "messages": messages,
        "tools": tools,
        "tool_choice": "auto",
        "stream": True,
    }


def test_stream_sends_configured_reasoning_effort() -> None:
    seen: dict = {}

    def respond(request: httpx.Request) -> httpx.Response:
        seen.update(json.loads(request.content))
        return httpx.Response(
            200,
            headers={"Content-Type": "text/event-stream"},
            content=b'data: {"choices":[{"delta":{"content":"ok"},"finish_reason":"stop"}]}\n\n',
        )

    async def run() -> None:
        async with httpx.AsyncClient(
            base_url="https://gemini.test/v1beta/openai/",
            transport=httpx.MockTransport(respond),
        ) as http:
            async for _ in LightningClient(
                http,
                model="gemini-3.8-flash",
                reasoning_effort="low",
            ).stream(messages=[], tools=[]):
                pass

    asyncio.run(run())

    assert seen["reasoning_effort"] == "low"


def test_stream_rejects_a_truncated_response() -> None:
    def respond(_request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            headers={"Content-Type": "text/event-stream"},
            content=b'data: {"choices":[{"delta":{"content":"dang do"},"finish_reason":null}]}\n\n',
        )

    async def run() -> None:
        async with httpx.AsyncClient(
            base_url="https://lightning.test/api/v1/",
            transport=httpx.MockTransport(respond),
        ) as http:
            async for _ in LightningClient(http, model="gemma").stream(
                messages=[], tools=[]
            ):
                pass

    with pytest.raises(LightningProtocolError, match="DONE"):
        asyncio.run(run())


def test_stream_accepts_a_final_finish_reason_without_done() -> None:
    def respond(_request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            headers={"Content-Type": "text/event-stream"},
            content=b'data: {"choices":[{"delta":{"content":"xong"},"finish_reason":"stop"}]}\n\n',
        )

    async def run() -> list[ChatDelta]:
        async with httpx.AsyncClient(
            base_url="https://gemini.test/v1beta/openai/",
            transport=httpx.MockTransport(respond),
        ) as http:
            return [
                item
                async for item in LightningClient(http, model="gemini").stream(
                    messages=[], tools=[]
                )
            ]

    assert asyncio.run(run()) == [ChatDelta(content="xong", finish_reason="stop")]


def test_stream_retries_one_connection_failure_before_any_event(monkeypatch) -> None:
    attempts = 0
    sleeps = []

    async def sleep(delay: float) -> None:
        sleeps.append(delay)

    monkeypatch.setattr("ontchatbot.runtime.llm.asyncio.sleep", sleep)

    def respond(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            raise httpx.ConnectError("temporary", request=request)
        return httpx.Response(
            200,
            headers={"Content-Type": "text/event-stream"},
            content=b'data: {"choices":[{"delta":{"content":"ok"},"finish_reason":"stop"}]}\n\ndata: [DONE]\n\n',
        )

    async def run() -> list[ChatDelta]:
        async with httpx.AsyncClient(
            base_url="https://lightning.test/api/v1/",
            transport=httpx.MockTransport(respond),
        ) as http:
            return [
                item
                async for item in LightningClient(http, model="gemma").stream(
                    messages=[], tools=[]
                )
            ]

    assert asyncio.run(run()) == [ChatDelta(content="ok", finish_reason="stop")]
    assert attempts == 2
    assert sleeps == [1.0]


def test_stream_retries_one_retryable_http_failure_before_any_event(monkeypatch) -> None:
    attempts = 0
    sleeps = []

    async def sleep(delay: float) -> None:
        sleeps.append(delay)

    monkeypatch.setattr("ontchatbot.runtime.llm.asyncio.sleep", sleep)

    def respond(_request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            return httpx.Response(503, text="temporarily unavailable")
        return httpx.Response(
            200,
            headers={"Content-Type": "text/event-stream"},
            content=b'data: {"choices":[{"delta":{"content":"ok"},"finish_reason":"stop"}]}\n\ndata: [DONE]\n\n',
        )

    async def run() -> list[ChatDelta]:
        async with httpx.AsyncClient(
            base_url="https://lightning.test/api/v1/",
            transport=httpx.MockTransport(respond),
        ) as http:
            return [
                item
                async for item in LightningClient(http, model="gemma").stream(
                    messages=[], tools=[]
                )
            ]

    assert asyncio.run(run()) == [ChatDelta(content="ok", finish_reason="stop")]
    assert attempts == 2
    assert sleeps == [1.0]


def test_stream_falls_back_after_exponential_retries_of_503(monkeypatch) -> None:
    models = []
    sleeps = []

    async def sleep(delay: float) -> None:
        sleeps.append(delay)

    monkeypatch.setattr("ontchatbot.runtime.llm.asyncio.sleep", sleep)

    def respond(request: httpx.Request) -> httpx.Response:
        model = json.loads(request.content)["model"]
        models.append(model)
        if model == "gemini-3.8-flash":
            return httpx.Response(503, text="high demand")
        return httpx.Response(
            200,
            headers={"Content-Type": "text/event-stream"},
            content=b'data: {"choices":[{"delta":{"content":"ok"},"finish_reason":"stop"}]}\n\n',
        )

    async def run() -> list[ChatDelta]:
        async with httpx.AsyncClient(
            base_url="https://gemini.test/v1beta/openai/",
            transport=httpx.MockTransport(respond),
        ) as http:
            return [
                item
                async for item in LightningClient(
                    http,
                    model="gemini-3.8-flash",
                    reasoning_effort="low",
                    fallback_model="gemini-3.5-flash-lite",
                ).stream(messages=[], tools=[])
            ]

    assert asyncio.run(run()) == [ChatDelta(content="ok", finish_reason="stop")]
    assert models == ["gemini-3.8-flash"] * 4 + ["gemini-3.5-flash-lite"]
    assert sleeps == [1.0, 2.0, 4.0]
