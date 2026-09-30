# Sổ cái bằng chứng cho poster

## Cách đọc

- **Cao:** được xác nhận trực tiếp bằng mã nguồn/dữ liệu máy đọc được và có kiểm thử hoặc tệp thực nghiệm tương ứng.
- **Trung bình:** mô tả đúng ý đồ thiết kế hoặc quan sát của một lượt chạy, nhưng phụ thuộc chỉ dẫn, người biên soạn hay mô hình chấm.
- **Thấp/chưa đủ:** thiếu phép đo hoặc có nguồn mâu thuẫn; không dùng làm tuyên bố trên poster.
- “Được đưa lên poster” luôn đi kèm đúng câu chữ và giới hạn ghi trong bảng; không được rút gọn làm thay đổi phạm vi.

## Tuyên bố về bài toán và phương pháp

| Tuyên bố dự kiến | Bằng chứng trong kho mã nguồn | Mức chắc chắn | Được đưa lên poster? | Giới hạn/câu chữ bắt buộc |
|---|---|---|---|---|
| Thông tin học vụ được tổng hợp từ nhiều loại nguồn; sinh viên hỏi bằng cách nói đời thường | `README.md:28-46`; tập nguồn trong `references/`; trường `register` trong `resources/end-to-end/questions.json` | Trung bình | **Có**, làm bối cảnh | Không định lượng mức “phân tán” hoặc mức khó nếu chưa có khảo sát người dùng |
| Người dùng nhập câu hỏi ở giao diện web; giao diện gửi câu hỏi cùng lịch sử gần đây tới dịch vụ và nhận trạng thái/câu trả lời phát dần | `webui/script.js:290-305,350-406`; nhận `message`/`history` ở `src/ontchatbot/runtime/api.py:400-407`; phát sự kiện ở `src/ontchatbot/runtime/api.py:269-283` | Cao | **Chỉ đưa hành vi giao diện**, không đưa giao thức | Poster có thể nói “gửi câu hỏi và xem tiến trình tra cứu”; không cần nêu API, SSE, hàng đợi hay giới hạn lịch sử |
| LLM hiểu câu hỏi, quyết định tra cứu, tạo cụm từ khóa và diễn đạt câu trả lời | `src/ontchatbot/runtime/agent.py:41-78,143-215,293-323`; `src/ontchatbot/runtime/llm.py:43-49`; từ khóa thực tế trong `resources/end-to-end/results.json` | Cao | **Có** | Không nói LLM tự xác minh dữ kiện hay tự lưu quy định |
| Dữ kiện học vụ phục vụ câu trả lời được lấy từ đồ thị tri thức, thay vì coi LLM là kho quy định | Lời hướng dẫn môi trường vận hành ở `src/ontchatbot/runtime/agent.py:293-317`; công cụ chuyển kết quả ontology ở `src/ontchatbot/runtime/lookup.py:66-92`; mô tả thiết kế `README.md:3-11` | Cao cho **thiết kế**, không phải bảo đảm tuyệt đối | **Có, có điều kiện** | Viết “LLM được dùng để hiểu và diễn đạt; dữ kiện học vụ được lấy từ đồ thị tri thức”. Không viết “LLM không thể dùng kiến thức riêng” hoặc “mọi câu luôn tra cứu” |
| Hệ thống hiện hành dùng truy xuất từ vựng BM25, không phải RAG dựa trên véc-tơ/truy xuất ngữ nghĩa | `src/ontchatbot/search/index.py:23-60`; các phụ thuộc trong `pyproject.toml`; chưa có kho véc-tơ/mô hình nhúng trong mã tìm kiếm | Cao | **Có**, khi mô tả phương pháp | Không biến thành tuyên bố so sánh chất lượng; dự án chưa đối chứng RAG (`README.md:774-776`) |
| Kho tri thức là RDF/TriG; ontology là bản biểu diễn có cấu trúc, còn văn bản chính thức là căn cứ có thẩm quyền | `resources/ontology/ontology.trig:1-4`; nơi nạp TriG `src/ontchatbot/search/ontology.py:42-49`; `README.md:154-158` | Cao | **Có** | Không gọi ontology là bản sao đầy đủ của mọi quy định |
| Dữ kiện có thể mang địa chỉ tới đúng vị trí của nguồn | Ví dụ thật: metadata nguồn `resources/ontology/ontology.trig:719-725`, địa chỉ `resources/ontology/ontology.trig:1470-1472`, phát biểu trong named graph `resources/ontology/ontology.trig:3003-3012`; dựng citation/URL tại `src/ontchatbot/search/profile.py:69-92` | Cao | **Có** | Viết “dữ kiện cần nguồn được gắn vị trí và văn bản”; không viết “mọi dữ kiện đều có trích dẫn” vì phát biểu ngoài named graph cho `citation: null` |
| Bộ tìm kiếm dựng chỉ mục từ nhãn/tên gọi khác và thuộc tính/quan hệ của ontology | `src/ontchatbot/search/builder.py:10-18,24-47`; nhãn và SKOS altLabel `src/ontchatbot/search/ontology.py:123-129` | Cao | **Có**, nhưng nên giản lược | Poster chính chỉ cần “BM25 xếp hạng các mục từ chỉ mục sinh từ ontology” |
| Mỗi từ khóa lấy tối đa 20 dòng; điểm mục là tổng điểm tốt nhất theo từng từ khóa; sau đó lấy k mục đầu | `src/ontchatbot/search/index.py:50-60`; `src/ontchatbot/search/engine.py:57-82,104-131` | Cao | **Chỉ nên có nếu còn chỗ** | “3 mục đầu” chỉ đúng với cấu hình mặc định và thực nghiệm (`src/ontchatbot/cli/serve.py:69-72`; `resources/end-to-end/run-info.json`) |
| Sau khi xếp hạng, hệ thống quay lại ontology đọc toàn bộ hồ sơ của mục, gồm phát biểu đi và phát biểu trỏ vào, rồi gom theo nguồn | `src/ontchatbot/search/engine.py:126-131`; `src/ontchatbot/search/profile.py:95-112` | Cao | **Có** | Đây là khác biệt cần thể hiện trong hình trung tâm; không nói BM25 trực tiếp sinh câu trả lời |
| SHACL mô tả cấu trúc dữ liệu và kiểm toàn đồ thị trước khi ghi | `resources/ontology/shapes.ttl:8-39`; đọc khuôn dạng để dựng biểu mẫu `src/ontchatbot/admin/schema.py:69-125`; kiểm pySHACL `src/ontchatbot/admin/store.py:321-355`; kiểm thử `tests/search/test_shapes.py:27-34` | Cao | **Có**, ở vai trò phụ | Thiếu nguồn được kiểm bằng quy tắc riêng ở `src/ontchatbot/admin/store.py:284-296`; không viết “SHACL xác minh câu trả lời” hay “SHACL tự xác định nguồn đúng pháp lý” |
| Biểu mẫu quản trị và kiểm dữ liệu cùng dựa trên một lược đồ; bản hợp lệ được ghi rồi bộ tìm kiếm dựng lại | `src/ontchatbot/admin/schema.py:1-5,69-125`; `src/ontchatbot/admin/store.py:210-236,321-329`; lệnh nạp lại `src/ontchatbot/cli/serve.py:122-139` | Cao | **Có nếu còn chỗ** | Viết “cập nhật có kiểm soát, không cần huấn luyện lại”. Bản triển khai dựa trên tệp chưa bền vững và chưa có phân quyền/lịch sử (`README.md:771-773`) |
| Ngoài phạm vi, không khớp và thiếu dữ kiện được xử lý thành ba nhánh khác nhau | Lời hướng dẫn `src/ontchatbot/runtime/agent.py:65-78,303-320`; dữ liệu trả về khi không khớp `src/ontchatbot/runtime/lookup.py:28-36,66-72` | Trung bình | **Có, có điều kiện** | Đây là hành vi **được hướng dẫn cho mô hình**, không có bộ phân loại/bộ kiểm tất định. Dùng “được hướng dẫn từ chối/nói rõ giới hạn” |
| Khi không từ khóa nào khớp, mô hình được hướng dẫn thử lại tối đa một lần bằng cách gọi khác; nếu vẫn không có thì dừng và nói không tìm thấy | `src/ontchatbot/runtime/agent.py:65-78`; payload `not_found` tại `src/ontchatbot/runtime/lookup.py:28-36,66-72` | Trung bình | **Có**, như chú thích nhánh | Đây là chỉ dẫn cho mô hình, không phải bộ đếm thử lại tất định độc lập; không nói hệ thống luôn thực hiện đúng nhánh |
| Giao diện đi qua “Đang suy nghĩ” → “Đang tra cứu” kèm cụm từ → “Đang viết câu trả lời” → phát dần văn bản | `webui/script.js:300-321,350-370`; sự kiện từ `src/ontchatbot/runtime/api.py:269-283` | Cao | **Có**, qua ảnh chụp | Nguồn hiện là Markdown/URL do LLM giữ lại trong văn bản, không phải thẻ trích dẫn có cấu trúc được ràng buộc bằng dữ liệu |
| Từ chối trên giao diện là nội dung trả lời thông thường, không phải trạng thái/thẻ từ chối có cấu trúc | Trợ lý phát trực tiếp `text_delta`/`completed` ở `src/ontchatbot/runtime/agent.py:153-170`; giao diện xử lý chung tại `webui/script.js:350-370` | Cao | Có thể nêu khi giải thích ảnh | Không suy ra có bộ phân loại từ chối trong giao diện hoặc API |
| Ontology hoặc SHACL kiểm lại câu trả lời sau khi LLM sinh | Tác tử phát trực tiếp văn bản/sự kiện hoàn tất tại `src/ontchatbot/runtime/agent.py:153-170`; API chuyển tiếp ở `src/ontchatbot/runtime/api.py:269-287` | Cao rằng tuyên bố này **sai** | **Không** | Chỉ có kiểm tra ngoại tuyến trong bộ đánh giá; tuyệt đối không gọi ontology là “lớp xác minh đầu ra” |

## Claim và metric thực nghiệm

| Metric/claim | Dữ liệu gốc và phép tính | Mức chắc chắn | Được đưa lên poster? | Người xem nên hiểu / nguy cơ hiểu sai |
|---|---|---|---|---|
| Bộ kiểm truy xuất có 57 câu, 49 câu được chấm | `resources/end-to-end/retrieval.json`; quy tắc loại 8 câu ở `README.md:532-557`; script `resources/end-to-end/check_retrieval.py:34-57` | Cao | Có trong chú thích metric | 8 câu bị loại gồm câu hỏi nguyên văn điều khoản và câu nhắm tới tầng nguồn; không được gọi bộ chấm là 57 câu |
| **48/49 (98,0%)**: mục đúng nằm trong 3 kết quả đầu | Artefact `resources/end-to-end/retrieval.json`; tái chạy `uv run python resources/end-to-end/check_retrieval.py`; tổng hợp `README.md:639-650` | Cao | **Có — metric chính** | Đo riêng search với từ khóa đã cố định từ một lượt trợ lý; không đo khả năng tạo từ khóa ở câu mới và không phải 98% độ chính xác câu trả lời |
| **43/49 (87,8%)**: mục đúng đứng hạng 1 | Cùng artefact/script; `README.md:641-646` | Cao | Có nếu cần metric phụ | Không cần đưa đồng thời nếu làm dải metric quá dày; hit@3 quan trọng hơn vì runtime dùng top-3 |
| Bộ đánh giá toàn quy trình có **85 câu**: 66 có dữ kiện, 11 ngoài phạm vi, 8 hỏi vào khoảng trống | `resources/end-to-end/questions.json`; kết quả từng lượt `resources/end-to-end/results.json`; cấu hình `resources/end-to-end/run-info.json`; `README.md:559-599` | Cao | **Có** trong chú thích chung | Lượt chạy ngày 13/09/2026, tuần tự, mỗi câu độc lập, dùng `lightning-ai/gemma-4-31B-it`, lấy 3 mục đầu, tối đa 4 bước |
| **64/66 (97,0%)** câu có dữ kiện đã gọi công cụ trước khi trả lời | `resources/end-to-end/results.json`; tính tại `resources/end-to-end/score.py:24-31`; `README.md:654-662` | Cao | Không ưu tiên | Chỉ chứng minh có gọi, không chứng minh gọi đúng; đồng thời bác bỏ claim “luôn gọi công cụ” |
| **55/58 (94,8%)** câu có nhãn mục cần tra đã lấy đúng mục trong quy trình thật | `resources/end-to-end/results.json`; `resources/end-to-end/score.py:9-10,24-30`; `README.md:656-660` | Cao | **Có — số liệu quy trình** | Chỉ đo đúng đối tượng truy xuất; chưa chấm diễn đạt câu trả lời. 8/66 câu có dữ kiện không có nhãn mục để đối chiếu |
| **54/58 (93,1%)** vừa lấy đúng mục vừa qua phép dò bám dữ liệu | `resources/end-to-end/results.json`; `resources/end-to-end/score.py:28-30`; `README.md:660-661` | Cao cho đúng phép dò | Không chọn làm số chính | “Bám dữ liệu” ở đây chỉ dò chuỗi số từ hai chữ số và chữ viết tắt, không hiểu quan hệ; không được gọi là độ chính xác thực tế |
| **52/58 (89,7%)** câu có mục cần tra được mô hình chấm ở mức đúng | Đối chiếu phán quyết `resources/end-to-end/quality.json` với nhóm và mục cần tra trong `resources/end-to-end/results.json`; phân bố `README.md:664-676`; tiêu chí tại `resources/end-to-end/score_quality.py:43-105`; thiết lập chấm được mô tả tại `README.md:769-770` | Trung bình | **Có — số liệu chất lượng, phải kèm nhãn “mô hình chấm”** | Một lượt chạy; README ghi cùng mô hình vừa làm trợ lý vừa chấm, nhưng `quality.json` không tự lưu định danh mô hình chấm để kiểm độc lập. Có 4/85 phán quyết toàn bộ bị đánh dấu đáng ngờ. Không gọi là độ chính xác khách quan |
| **51/58** câu vừa lấy đúng mục cần tra vừa được mô hình chấm đúng | Đối chiếu theo `id` giữa `resources/end-to-end/results.json` và `resources/end-to-end/quality.json`: 51 giao nhau; 1 câu được chấm đúng dù không lấy nút đích; 4 câu lấy đúng nút nhưng bị chấm thiếu/từ chối | Cao cho phép đếm, trung bình cho ý nghĩa chất lượng | Không cần làm số chính | Chứng minh `55/58` và `52/58` không phải hai tầng lồng nhau; **không nối chúng bằng mũi tên nhân quả** trên poster |
| **53/66 (80,3%)** mọi câu nhóm có dữ kiện được mô hình chấm đúng | Cùng artefact; `README.md:666-670` | Trung bình | Có trong chú thích hoặc báo cáo, không cần headline | Mẫu số gồm 8 câu nguyên văn điều khoản/hỏi văn bản nguồn không có nhãn mục truy xuất phù hợp; số chính 52/58 dễ giải thích hơn nếu ghi đúng phạm vi |
| **19/19** tình huống cần từ chối được mô hình chấm là từ chối | Đối chiếu `resources/end-to-end/quality.json` với nhóm chuẩn trong `resources/end-to-end/results.json`: 11/11 ngoài phạm vi + 8/8 khoảng trống; `README.md:671-676,729-733` | Trung bình | **Có — số liệu chính** | Chỉ đúng trên 19 tình huống cố định. Không suy rộng thành “không bao giờ trả lời sai” hay tỷ lệ ngoài thực tế |
| **0/85** lượt có lỗi chạy | `resources/end-to-end/results.json`; `resources/end-to-end/score.py:42-46`; `README.md:661-662` | Cao cho lượt chạy này | Không ưu tiên | Không có lỗi kỹ thuật không đồng nghĩa câu trả lời đúng |
| **2,0 giây** trung vị toàn lượt; phân vị 95 là 2,9 giây; dài nhất 21,9 giây | Trường `giay` trong `resources/end-to-end/results.json`; phép tính `resources/end-to-end/score.py:48-60`; `README.md:678-689` | Cao cho môi trường/lượt chạy này | **Có — số liệu phụ** | 85 lượt tuần tự, gồm LLM qua mạng; không phải cam kết mức dịch vụ. Nên ghi cả mẫu số 85 và giữ giá trị dài nhất trong phần giải thích |
| Tra cứu nội bộ trung vị 3,2 ms, phân vị 95 là 6,9 ms trên 78 lần gọi | Trường `ms_cong_cu` trong `resources/end-to-end/results.json`; `resources/end-to-end/score.py:58-60`; `README.md:682-689` | Cao | Có nếu còn chỗ | Đo tìm + đọc hồ sơ + ghi JSON, không gồm LLM/mạng. Không đặt cạnh 2,0 giây nếu không giải thích hai phạm vi |
| Nạp TriG/dựng chỉ mục khoảng 45 ms; search riêng trung vị 0,41 ms, p95 0,68 ms | `README.md:496-501`; không có snapshot benchmark riêng ngoài tài liệu | Trung bình | Không chọn | Dễ nhầm với latency đầu-cuối và phụ thuộc máy; 3,2 ms trong pipeline là artefact gần hơn với hành vi thật |
| Toàn bộ test repository hiện qua | Phiên kiểm tra 14/09/2026: sau khi cài extra `inference`, `uv run pytest -q` cho **153 passed, 2 warnings**; test nằm trong `tests/` | Cao cho commit hiện tại | Không dùng làm metric poster | Đây là kiểm chứng kỹ thuật, không đo chất lượng hỏi đáp với người dùng |

## Các tầng đánh giá thực tế

Các phép đo không phải một thang điểm duy nhất. Khi thuyết trình, cần phân biệt năm tầng sau:

1. **Truy xuất riêng:** dùng 49 câu được chấm với từ khóa cố định để đo thứ hạng của đúng mục (`resources/end-to-end/retrieval.json`; `resources/end-to-end/check_retrieval.py:34-57`).
2. **Toàn quy trình:** 85 lượt đo việc gọi công cụ, lấy đúng mục và thời gian hoàn tất (`resources/end-to-end/questions.json`; `resources/end-to-end/results.json`; `resources/end-to-end/score.py:24-60`).
3. **Phép dò tất định:** dò chuỗi số/viết tắt ngoài dữ liệu và các cụm diễn đạt thiếu dữ kiện; đây là chỉ báo hẹp, không hiểu nghĩa của câu trả lời (`resources/end-to-end/run.py:50-116`; `resources/end-to-end/score.py:28-40,63-66`).
4. **Mô hình chấm:** phân loại câu trả lời thành đúng, đúng một phần, từ chối, sai hoặc lạc đề; phải kèm giới hạn cùng mô hình và một lượt (`resources/end-to-end/score_quality.py:43-105`; `README.md:664-676,769-770`).
5. **Kiểm thử phần mềm:** 153 test qua xác nhận hành vi kỹ thuật tại phiên kiểm tra, không thay cho đánh giá chất lượng nghiên cứu (`tests/`).

## Mâu thuẫn và điểm cần khóa cách diễn giải

### 1. Nhóm trong `quality.json` có 5 nhãn không khớp

Năm bản ghi trong `quality.json` có trường `nhom` không còn khớp `results.json`: `question-006297`, `question-006275`, `question-006290`, `gap-001`, `gap-007`. Script có cơ chế giữ lại kết quả chấm theo ID khi chạy tiếp (`resources/end-to-end/score_quality.py:206-219`), nhưng lịch sử file hiện có không đủ để kết luận chính xác vì sao năm nhãn nhóm lệch; không nên suy đoán rằng phán quyết của chúng chắc chắn là cache cũ.

- `resources/end-to-end/quality.json` nếu nhóm trực tiếp cho ra phân bố nhóm sai.
- `resources/end-to-end/results.json` được dựng lại từ `resources/end-to-end/questions.json` và là nguồn phù hợp hơn cho **nhóm kỳ vọng** (`resources/end-to-end/run.py:167-185,195-201`).
- `resources/end-to-end/quality.json` vẫn là nguồn cho **phán quyết** `muc`.
- Mọi số liệu chất lượng trong poster phải đối chiếu theo ID: nhóm từ `results.json`, phán quyết từ `quality.json`. Cách này tái tạo đúng 53/66, 11/11 và 8/8 như `README.md`.

### 2. Có 4/85 phán quyết của mô hình chấm bị đánh dấu đáng ngờ

`resources/end-to-end/quality-log.md:1-4` ghi 4 phán quyết đáng ngờ; logic đánh dấu nằm ở `resources/end-to-end/score_quality.py:223-240`. Hai ca “đúng” có chuỗi viết tắt ngoài dữ liệu theo phép dò; hai ca “từ chối” thuộc nhóm có dữ kiện dù đã lấy đúng mục. Vì vậy số liệu 52/58 và 19/19 phải được gọi là **kết quả mô hình chấm trên bộ cố định**, không phải nhãn chuẩn do người chấm độc lập.

### 3. Bộ dò cụm từ và mô hình chấm cho hai kết quả từ chối khác nhau

- Phép dò cố định chỉ nhận ra **7/11** câu ngoài phạm vi vì nó tìm một danh sách cách nói cụ thể (`resources/end-to-end/score.py:33-40`; `README.md:704-706`).
- Mô hình chấm xếp cả **11/11** câu ngoài phạm vi vào mức từ chối (`resources/end-to-end/quality.json`; `README.md:704-706`).
- Hai kết quả đo hai thứ khác nhau. Poster chỉ dùng số **19/19 được mô hình chấm là từ chối**, đồng thời ghi rõ phương pháp chấm; không dùng 7/11 làm headline và không hòa hai phép đo thành một tỷ lệ.

### 4. “Thiếu nguồn bị SHACL từ chối” là diễn giải quá gọn

- UI và README cho thấy lưu dữ liệu thiếu nguồn bị từ chối (`README.md:516-520`).
- Mã nguồn kiểm yêu cầu nguồn bằng quy tắc riêng trước (`src/ontchatbot/admin/store.py:284-296`), sau đó mới chạy pySHACL trên toàn đồ thị (`src/ontchatbot/admin/store.py:321-355`).
- Claim đúng: “Biểu mẫu kiểm yêu cầu nguồn và toàn đồ thị được kiểm theo SHACL trước khi ghi.”

### 5. Thời gian lưu dữ liệu quản trị chưa có artefact đủ tin cậy

`README.md:522-523` nói khoảng nửa giây; chú thích `src/ontchatbot/admin/http.py:3-5` nói thao tác có thể mất 1–2 giây; không có file benchmark. **Không đưa latency quản trị lên poster.**

### 6. `retrieval-baseline.json` không phải baseline phương pháp

Đây là ảnh chụp trạng thái hồi quy để xem câu nào tăng/giảm thứ hạng trong cùng bộ tìm kiếm (`resources/end-to-end/check_retrieval.py:1-11,65-70`). Nó không phải kết quả RAG, truy xuất ngữ nghĩa hay hệ thống đối chứng. Không dùng từ “vượt đường cơ sở” trên poster.

### 7. Con số 204 trong báo cáo thu thập không phải kích thước ontology

`references/ntu_thong_tin_hoc_vu_master_final_2026-09-12.md:457-480` đếm 204 **dòng fact trong các bảng của báo cáo thu thập**, theo quy tắc riêng. Nó không đếm quad, cá thể hay dữ kiện hiện đang được runtime đọc. Không đưa “204 dữ kiện trong ontology” lên poster.

## Claim bị cấm vì vượt bằng chứng

| Không được viết | Lý do |
|---|---|
| “Loại bỏ hallucination” | Không có validator hậu kỳ; 2/85 câu bị heuristic phát hiện số/viết tắt ngoài dữ liệu |
| “Đảm bảo chính xác” / “độ chính xác 100%” | Metric có phạm vi hẹp, một lượt chạy và mô hình tự chấm |
| “Mọi dữ kiện đều có nguồn” | Có dữ kiện ngoài named graph với `citation: null` |
| “Ontology xác minh câu trả lời” | Ontology cung cấp dữ kiện; output LLM không được ontology/SHACL kiểm sau sinh |
| “SHACL bảo đảm đúng nguồn” | SHACL kiểm hình dạng; thẩm quyền/diễn giải nguồn là quyết định biên tập |
| “Ontology tốt hơn RAG” | Chưa có baseline RAG trên cùng bộ câu hỏi |
| “BM25 tốt hơn truy xuất ngữ nghĩa” | Chưa có đối chứng semantic retrieval |
| “Đã triển khai toàn trường” | README gọi đây là nguyên mẫu nghiên cứu (`README.md:3`) |
| “Giảm tải cán bộ” | Chưa có nghiên cứu vận hành hoặc đo tải công việc |
| “Dễ sử dụng” | Chưa có usability study |
| “19/19 nghĩa là từ chối sai bằng 0 trong thực tế” | Chỉ 19 tình huống cố định của một bộ đánh giá |

## Bộ claim được khóa cho phương án khuyên dùng

1. **Bài toán:** Thông tin học vụ có nhiều nguồn và cách gọi; câu trả lời cần vừa dễ hỏi vừa truy được căn cứ.
2. **Ý tưởng:** LLM hiểu và diễn đạt, còn BM25 tra trên đồ thị tri thức RDF/TriG; sau xếp hạng, hệ thống đọc lại đầy đủ dữ kiện theo nguồn.
3. **Quản trị tri thức:** Dữ kiện cần nguồn được gắn vị trí trong văn bản; cập nhật được kiểm cấu trúc trước khi ghi.
4. **Bằng chứng:** 48/49 câu đưa đúng mục vào ba kết quả đầu ở đánh giá truy xuất; trong toàn quy trình, 55/58 lấy đúng mục và 52/58 được mô hình chấm đúng; 19/19 tình huống cần từ chối được mô hình chấm là từ chối; trung vị 2,0 giây trên 85 lượt.
5. **Giới hạn:** Dữ liệu mới phủ một phần phạm vi; search phụ thuộc từ vựng/từ khóa; đánh giá chỉ một lượt, cùng mô hình làm trợ lý và chấm, chưa so với RAG.
