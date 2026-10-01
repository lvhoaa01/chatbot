# 01 — Hiện trạng và hợp đồng phải giữ

## 1. Hiện trạng thực tế của workspace

Luồng hiện tại là:

```text
TriG ontology
→ sinh các dòng chữ từ label/property/relation
→ BM25 local
→ hồ sơ của entity, gom facts theo nguồn
→ JSON lookup
→ LLM chọn tool/từ khóa và diễn đạt
→ SSE / CLI / Web UI
```

Ontology đang làm hai việc cùng lúc:

1. kho nội dung được biên soạn thủ công;
2. cấu trúc provenance để gom fact theo nguồn.

Nhưng retrieval online không chạy suy luận ontology hay SPARQL phức tạp. Nó biến label
và property thành văn bản rồi xếp hạng bằng BM25. Đây là lý do có thể thay lớp lưu trữ
tri thức mà vẫn giữ phần lớn runtime.

Các số liệu mốc đang có trong repository:

| Hạng mục | Mốc hiện tại |
|---|---:|
| Python tests được pytest thu thập | 158 |
| Kết quả chạy ngày 2026-10-01 | 156 pass, 2 fail do thiếu hai file `.github` |
| Bộ retrieval được chấm | 49 câu |
| Retrieval có đáp án đúng trong top 3 | 48/49 |
| Retrieval có đáp án đúng ở hạng 1 | 43/49 |
| Bộ end-to-end | 85 câu |
| Cơ cấu end-to-end | 66 có dữ kiện, 11 ngoài phạm vi, 8 thiếu dữ liệu |
| File nguồn trong `references/` | 8 PDF, 18 Markdown, 2 TXT, 1 HTML |
| PDF có Markdown cùng tên | 8/8 |

Số liệu retrieval/end-to-end được lấy từ `resources/end-to-end/` và README hiện tại.
Đây là mốc so sánh, không phải chứng nhận chất lượng trên mọi câu hỏi thực tế. Baseline
chưa hoàn toàn xanh: ngoài hai pytest fail, CLI search dạng text đang gọi API profile
cũ và web dependency chưa được cài. Các lỗi này được đưa vào G0 của roadmap thay vì bị
che bởi đợt refactor.

## 2. Điều “mọi case hiện tại vẫn chạy” có nghĩa gì?

Cần tách ba lớp:

### 2.1 Giữ test lịch sử cho đến khi có replacement được review

Sau khi G0 làm baseline xanh và cho đến commit mapping/replacement được review:

- 158 Python tests lịch sử vẫn chạy trên legacy job;
- proxy và browser tests của `webui` vẫn xanh;
- CLI smoke hoàn thành thành công ở cả text và JSON paths;
- ontology backend vẫn tồn tại để rollback và đối chiếu.

Không được xóa test đang đỏ để làm pipeline mới “đạt”.

### 2.2 Giữ hành vi, không giả lập implementation cũ mãi mãi

Một số test đang kiểm chi tiết riêng của ontology:

- SHACL và citation bag;
- đọc/ghi TriG trong admin;
- index row sinh từ datatype/object property;
- image build chỉ copy ontology resources;
- source fidelity giữa bảng trong ontology và bản Markdown.

Document backend không cần giả làm RDF chỉ để qua các test này. Cách migration đúng là:

1. giữ các test đó chạy với legacy backend;
2. thêm test document backend kiểm cùng invariant ở dạng mới;
3. chỉ đổi hoặc retire test ontology trong một commit riêng, sau khi có bảng ánh xạ
   `test cũ → invariant → test thay thế` và được review;
4. sau mốc đó invariant tương đương phải xanh và ledger vẫn lưu dấu test lịch sử,
   nhưng tên/count 158 không bắt buộc tồn tại vĩnh viễn.

Do đó, “parity” là **không mất hành vi người dùng và invariant dữ liệu**, không phải
ép kiến trúc mới giữ tên class/file của kiến trúc cũ vĩnh viễn.

### 2.3 Giữ bộ câu hỏi đánh giá

- giữ cả 57 retrieval scenarios: 49 ca legacy-scored được ánh xạ từ `node_dung` sang
  gold evidence, còn 8 ca trước đây bị loại phải có expected evidence/outcome mới;
- 85 câu end-to-end vẫn phải chạy được với backend mới.
- Live evaluation dùng LLM qua API được giữ như một phép đo có điều kiện, nhưng test
  bắt buộc trong CI/dev phải chạy offline bằng client giả hoặc replay fixture.
- Cần giữ nhóm từ chối theo từng `corpus_release_id`. Khi release mới thật sự có dữ kiện
  cho một gap, việc đổi expected outcome phải là scenario change được review, không
  khóa câu đó ở trạng thái từ chối vĩnh viễn.

## 3. Ranh giới tương thích quan trọng nhất

Ranh giới nên ổn định trong giai đoạn đầu là hàm lookup bất đồng bộ:

```text
await lookup(keywords) -> JSON string
```

JSON hiện tại có hình dạng khái quát:

```json
{
  "status": "found",
  "guidance": "...",
  "results": [
    {
      "label": "...",
      "classes": ["..."],
      "matched": ["..."],
      "sources": [
        {
          "citation": "...",
          "url": "...",
          "facts": [
            {"subject": "...", "property": "...", "value": "..."}
          ]
        }
      ]
    }
  ],
  "unmatched": ["..."]
}
```

Document backend cần một `LookupCompatibilityAdapter` dựng đúng shape này. Có thể ánh
xạ tạm thời:

| JSON cũ | Dữ liệu mới |
|---|---|
| `label` | tiêu đề evidence hoặc heading gần nhất |
| `classes` | `document_type`, topic hoặc rỗng |
| `matched` | heading/snippet đã khớp |
| `citation` | citation dựng từ document + locator |
| `url` | canonical source URL, hoặc `null` với nguồn nội bộ có reference hợp lệ |
| `facts[].subject` | tiêu đề evidence |
| `facts[].property` | `nội dung` hoặc nhãn field có cấu trúc |
| `facts[].value` | nguyên văn evidence |

Adapter này là cầu nối tạm thời. Sau khi parity đạt, có thể thiết kế response giàu hơn
theo claim/evidence ID; không nên đổi agent, retriever, UI và API cùng một commit.

## 4. Những phần phải giữ và những phần được thay

| Thành phần | Quyết định giai đoạn đầu | Lý do |
|---|---|---|
| Starlette API, auth, queue, timeout | Giữ | Đã có test hành vi rõ |
| SSE event và Web UI | Giữ | Không liên quan cách lưu tri thức |
| `LightningClient`/OpenAI-compatible stream | Giữ | Đã hỗ trợ Gemini tool-call và retry |
| `AgentLoop` + tool schema | Giữ ở mốc parity | Tránh đổi số lượt LLM đồng thời với kho tri thức |
| Analyzer tiếng Việt hiện tại | Tái sử dụng | Cho phép so sánh công bằng BM25 cũ/mới |
| `bm25s` | Tái sử dụng | Nhẹ, CPU-only, đã có dependency |
| JSON lookup | Giữ qua adapter | Ranh giới testable giữa QA và retrieval |
| Ontology/TriG/SHACL | Legacy backend | Không xóa trước khi backend mới đạt gate |
| Admin ontology | Chưa port ở bước đầu | Không phải điều kiện chứng minh QA parity |
| PDF parser | Track riêng | Không để OCR làm nhiễu phép đo retrieval |

## 5. Hợp đồng dữ liệu mới tối thiểu

### 5.1 Document manifest

```yaml
document_id: qd-1052
document_version_id: qd-1052/2025-07-17
title: Quy chế đào tạo trình độ đại học
source_path: references/Qd1052.md
source_url: https://...
source_hash: sha256:...
document_type: quy_che
issued_at: 2025-07-17
effective_from: null
effective_to: null
applicability_status: unreviewed
scope_mode: unknown
status: published
parser_method: approved_markdown
reviewed_at: 2026-10-01
scope: {}
```

### 5.2 EvidenceUnit

```yaml
evidence_id: qd-1052/2025-07-17/dieu-24/khoan-3
document_id: qd-1052
document_version_id: qd-1052/2025-07-17
section_path: [Điều 24, Khoản 3]
locator:
  page: 18
  article: 24
  clause: 3
title: Nghỉ học tạm thời
content: "... nguyên văn đã duyệt ..."
citation: "Khoản 3 Điều 24 ..."
source_reference: references/Qd1052.pdf
source_url: https://...
content_hash: sha256:...
metadata:
  effective_from: null
  effective_to: null
  applicability_status: reviewed
  scope_mode: restricted
  audience: [sinh_vien_chinh_quy]
  status: published
```

Yêu cầu:

- ID ổn định theo định danh tài liệu và locator, không theo vị trí chunk ngẫu nhiên;
- `document_id` chỉ identity văn bản; `document_version_id` identity một revision cụ thể;
- giữ `content` nguyên văn và `normalized_text` dùng cho search tách biệt;
- mọi `EvidenceUnit` document được publish phải có source revision và locator; record
  legacy chuyển tiếp không trích dẫn được phải là loại riêng và không được hỗ trợ factual
  claim nếu chưa có policy phê duyệt rõ;
- hash và parser method cho phép biết nội dung sinh từ phiên bản nào;
- file Markdown chỉ trở thành canonical input sau khi được duyệt, không tự động đúng
  chỉ vì có cùng tên với PDF.
- `scope_mode` dùng ba trạng thái tách biệt: `restricted` đi cùng danh sách giá trị,
  `universal` là đã review và áp dụng chung, `unknown` là chưa xác minh và không được
  coi như universal.

## 6. Ingestion khác Question Answering

```text
Document ingestion                         Question answering
------------------                         ------------------
đọc file                                  hiểu câu hỏi
OCR/layout                                tìm evidence
chuẩn hóa heading/bảng                    lọc hiệu lực/phạm vi
gắn locator và metadata                   từ chối khi không đủ dữ kiện
review/publish                            diễn đạt và citation
```

QA chỉ phụ thuộc vào knowledge release đã duyệt. Vì 8 PDF hiện có đều có Markdown cùng
tên, có thể kiểm chứng kiến trúc QA trước bằng các bản Markdown. Điều này không tuyên
bố parser đã giải đúng PDF; chỉ tránh để hai biến số parser và retrieval thay đổi cùng lúc.

Audit ingestion sơ bộ trên workspace ghi nhận 8 PDF với tổng 131 trang. Sáu file
(`Qd1052`, `Qd1965`, `Qd317`, `Qd500`, `Qd729`, `Qd753`) gần như không có native text
đủ dùng; `Qd626` có text layer tốt hơn và `DongHocPhi_VCB_2021` chỉ có một phần. Vì vậy
“dùng PDF” thực tế sẽ kéo theo OCR/layout handling. Tám bản Markdown cùng stem là đầu
vào ứng viên để review, không tự động là bản canonical hay chứng minh fidelity.

Tám cặp PDF/Markdown chỉ đủ cho một experiment ban đầu, không đủ thay toàn bộ ontology.
Các ca hiện tại còn hỏi website, biểu mẫu, ngành/chương trình, chứng chỉ, đơn vị và các
facts đã được curate chỉ còn trong ontology. Trước parity toàn corpus phải:

- ingest mọi nguồn đã duyệt phù hợp trong `references/`;
- ánh xạ mọi target của 57 retrieval scenarios và 85 E2E scenarios sang ít nhất một
  `EvidenceUnit` hoặc `KnowledgeRecord` trung lập;
- one-time export facts chỉ còn trong ontology sang record có provenance;
- báo rõ target chưa có nguồn/evidence, không âm thầm bỏ.

Khi cần parsing mới, dùng tầng tăng dần:

1. text/Markdown/HTML hoặc PDF có text layer;
2. LiteParse + Tesseract trên CPU cho tài liệu thông thường;
3. Docling batch trên CPU cho layout/bảng khó;
4. cloud parser hoặc rà thủ công cho tài liệu ngoại lệ.

LiteParse tự mô tả là chạy local, không cần cloud và có Tesseract; Docling biểu diễn
text, table, picture và reading order. Đây là adapter ingestion tùy loại tài liệu, không
phải dependency trên đường chat. Xem [LiteParse](https://github.com/run-llama/liteparse)
và [Docling document model](https://docling-project.github.io/docling/concepts/docling_document/).

## 7. Các rủi ro hiện hữu phải được đưa vào test

- BM25 hiện chỉ khớp từ vựng và phụ thuộc từ khóa do LLM sinh.
- Không có score threshold; top 3 có thể chỉ gần chữ chứ không đúng ý.
- Prompt hiện tại có giả định “bản hiện hành” và có trường hợp bỏ năm tuyển sinh; điều
  này không an toàn khi thêm nhiều phiên bản văn bản.
- Có citation không đồng nghĩa mọi kết luận của LLM đều được evidence hỗ trợ.
- 85 câu chỉ chạy một lượt; cấu hình hiện có thể dùng cùng biến model cho trả lời và
  chấm, còn judge identity không được ghi riêng trong run artifact. Vì vậy chưa đủ để
  kết luận tổng quát.
- API ngoài có thể 429, 503 hoặc timeout. Google cũng hướng dẫn chỉ retry lỗi tạm thời,
  dùng exponential backoff/jitter và giới hạn số lần retry trong
  [troubleshooting guide](https://ai.google.dev/gemini-api/docs/troubleshooting).

Những rủi ro này là lý do roadmap yêu cầu shadow run, deterministic tests và rollback,
không phải lý do giữ ontology vĩnh viễn.
