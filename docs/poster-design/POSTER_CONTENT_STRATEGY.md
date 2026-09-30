# Chiến lược nội dung poster

## Đối tượng người xem

### Chính

- Hội đồng, giảng viên và nhà nghiên cứu ở nhiều chuyên ngành, không mặc định biết đồ thị tri thức hay kiến trúc tác tử.
- Người xem đi ngang trong phiên poster, dành 10 giây để quyết định có dừng lại và khoảng 1–3 phút nếu quan tâm.

### Phụ

- Cán bộ học vụ quan tâm khả năng truy nguyên và cập nhật dữ liệu.
- Sinh viên/người làm sản phẩm muốn xem hành vi hỏi đáp và thử bản minh họa.

Mức kiến thức giả định: hiểu khái niệm LLM/chatbot, nhưng không yêu cầu biết RDF, named graph, BM25 hay SHACL. Mọi thuật ngữ kỹ thuật giữ lại phải được giải thích bằng vai trò, không bằng định nghĩa hàn lâm.

## Mục tiêu truyền thông

Sau một phút, người xem phải có thể nói lại:

> Hệ thống không dùng LLM như nơi nhớ quy định. LLM chuyển cách hỏi thành từ khóa và diễn đạt; BM25 tìm mục trong chỉ mục, rồi hệ thống đọc hồ sơ dữ kiện kèm nguồn đã khai báo từ đồ thị tri thức để trả lời hoặc nói rõ khi dữ liệu thiếu.

Sau ba phút, người xem phải hiểu thêm phạm vi bộ đánh giá, bốn kết quả chính và ba giới hạn lớn nhất.

Mục tiêu **không** phải chứng minh sản phẩm đã sẵn sàng triển khai toàn trường, so sánh hơn–thua với RAG, hoặc trình bày đầy đủ mọi lớp và công nghệ.

## Ba thông điệp bắt buộc phải nhớ

### Thông điệp số 1 — Bài toán

> **Câu hỏi học vụ có nhiều cách nói, còn câu trả lời cần truy được về đúng căn cứ.**

Lý do chọn:

- nối nhu cầu của sinh viên với yêu cầu học thuật về nguồn;
- giải thích vì sao chỉ để LLM trả lời trôi chảy là chưa đủ;
- ngắn hơn việc liệt kê từng loại quy chế, biểu mẫu và phòng ban.

### Thông điệp số 2 — Ý tưởng/kiến trúc

> **Trong thiết kế này, LLM hiểu và diễn đạt; đồ thị tri thức cung cấp dữ kiện, với cơ chế truy nguyên cho dữ kiện có gắn nguồn.**

Lý do chọn:

- là điểm phân vai quan trọng nhất của công trình;
- ngăn người xem hiểu nhầm đây là chatbot “hỏi thẳng LLM” hoặc RAG dựa trên véc-tơ thông thường;
- dẫn tự nhiên tới hình trung tâm: câu hỏi → từ khóa → BM25 → đọc đồ thị → trả lời.

### Thông điệp số 3 — Kết quả/giá trị

> **Trên bộ đánh giá cố định, chuỗi truy xuất–trả lời cho kết quả khả thi; 19/19 tình huống được thiết kế cần từ chối được mô hình chấm là từ chối.**

Lý do chọn:

- nói được cả năng lực trả lời lẫn giá trị của việc không tự điền khoảng trống;
- dùng đúng phạm vi tệp thực nghiệm, không suy rộng ra thực tế;
- mở đường để người xem đọc tiếp 48/49, hai thước đo 55/58 và 52/58, cùng trung vị 2,0 giây.

## Câu chuyện ngắn nhất của poster

1. **Vấn đề:** nguồn học vụ nhiều dạng, cách hỏi nhiều cách, câu trả lời cần căn cứ.
2. **Lựa chọn thiết kế:** tách vai trò diễn đạt của LLM khỏi kho dữ kiện.
3. **Cơ chế:** LLM tạo từ khóa; BM25 tìm mục; hệ thống đọc lại hồ sơ dữ kiện kèm nguồn đã khai báo; LLM trả lời.
4. **Kiểm soát:** khi thiếu dữ kiện, LLM được hướng dẫn nêu giới hạn; khi cập nhật, hệ thống kiểm yêu cầu khai báo nguồn rồi kiểm cấu trúc bằng SHACL.
5. **Bằng chứng:** bốn cụm số liệu có mẫu số.
6. **Kết luận có điều kiện:** khả thi trên phần dữ liệu đã biểu diễn; còn cần mở rộng, đánh giá độc lập và đối chứng.

## Xếp hạng nội dung

### BẮT BUỘC CÓ

- Tên đề tài chính thức, mã `SV2025-13-61`, tác giả, giảng viên hướng dẫn và đơn vị.
- Một câu chốt lớn thể hiện phân vai LLM–đồ thị tri thức.
- Bài toán trong tối đa 3 ý ngắn.
- Hình trung tâm mô tả đúng luồng hỏi đáp và nhánh nguồn chính thức/cập nhật.
- Một ô nhấn về truy nguyên: dữ kiện → vị trí trong văn bản → nguồn.
- Bốn cụm kết quả được khóa ở phần “Số liệu được chọn”.
- Một câu ghi rõ bộ toàn quy trình có 85 tình huống và chỉ là một lượt chạy trên phần dữ liệu đã biểu diễn.
- Ba giới hạn: độ phủ dữ liệu; phụ thuộc từ vựng/từ khóa; đánh giá một lượt/cùng mô hình chấm/chưa có đối chứng RAG.
- Kết luận ngắn, QR/liên hệ và nguồn nền tảng tối giản.

### NÊN CÓ NẾU CÒN KHÔNG GIAN

- Hai vùng cắt ảnh chụp minh họa “đang tra cứu bằng các cách gọi” và “trả lời kèm nguồn”.
- Một ô nhấn nhỏ về cập nhật: biểu mẫu kiểm yêu cầu nguồn, toàn đồ thị kiểm SHACL, rồi dựng lại chỉ mục; không cần ảnh chụp quản trị ở phương án chính.
- Một dòng mô tả ba nhóm câu hỏi của bộ đánh giá: 66 có dữ kiện, 11 ngoài phạm vi, 8 khoảng trống.
- Một câu hướng phát triển: mở rộng dữ liệu, đánh giá nhiều lượt/người chấm độc lập, so sánh RAG.
- Ba tài liệu nền tảng nhỏ ở chân trang.

### KHÔNG NÊN ĐƯA LÊN POSTER

- Tên file, đường dẫn thư mục, tên hàm/class/biến, JSON key, biến môi trường.
- Đoạn mã, câu lệnh chạy, cấu trúc gói và danh sách khung phần mềm.
- Công thức BM25, tham số `k1`, `b`, 20 dòng mỗi từ khóa và chi tiết cộng điểm.
- API, SSE, proxy, hàng đợi, timeout và giới hạn lịch sử hội thoại.
- Bản đồ toàn bộ lớp của đồ thị tri thức, IRI/namespace và ví dụ TriG nguyên văn.
- Tất cả trạng thái vận hành UI như server waking, queued, warning, offline.
- Ảnh chụp quản trị đầy đủ, ảnh toàn màn hình có chữ quá nhỏ.
- Danh sách toàn bộ 85 câu, bảng kết quả từng câu, nhật ký hoặc đầu ra kiểm thử.
- Con số 204 từ báo cáo thu thập; đó không phải số dữ kiện trong môi trường vận hành.
- “153 kiểm thử đạt” như thành tích nghiên cứu; kiểm thử chỉ xác nhận phần triển khai.
- Tổng quan công trình liên quan dài hoặc danh sách tài liệu tham khảo đầy đủ.
- Tuyên bố tốt hơn RAG/truy xuất ngữ nghĩa, dễ dùng, giảm tải, triển khai toàn trường hoặc loại bỏ bịa đặt.

## Ngân sách chữ

Mục tiêu: **520 từ, cho phép 460–600 từ nhìn thấy trên poster**, tính cả nhãn/chú thích nhưng không tính tên tác giả. Trần cứng 650 từ. Nếu vượt, cắt nội dung chứ không hạ thân bài dưới 24 pt ở kích thước in thật.

| Khối | Ngân sách |
|---|---:|
| Tên đề tài + mã + nhận diện | 35–55 từ |
| Câu chốt/thông điệp chính | 12–20 từ |
| Bài toán + mục tiêu | 50–65 từ |
| Nhãn/chú thích hình trung tâm | 95–125 từ |
| Đóng góp/truy nguyên/cập nhật | 55–75 từ |
| Số liệu + mẫu số + ghi chú phạm vi | 120–140 từ |
| Chú thích ảnh chụp | 15–30 từ |
| Kết luận + giới hạn + hướng phát triển | 75–95 từ |
| QR/liên hệ + 3 tài liệu nền tảng | 25–40 từ |

Các khoảng trên là ngân sách theo vai trò nội dung, không phải các cực đại để cộng dồn. Bản chữ chốt hiện có 549 từ không tính ba dòng tác giả; phần hình trung tâm và dải số liệu dài hơn các khối khác vì phải giữ nhãn nhánh, mẫu số và giới hạn diễn giải.

Quy tắc biên tập:

- mỗi ý ngắn thường không quá 15 từ;
- mỗi khối tối đa 3–4 ý;
- không có đoạn thân bài dài hơn 45 từ;
- dùng phân số trước, phần trăm sau hoặc bỏ phần trăm nếu không đủ chỗ;
- mọi số liệu phải có danh từ nói rõ nó đo gì.

## Số liệu được chọn: 4 cụm, 5 con số

### 1. Đánh giá truy xuất riêng — 48/49

- **Con số:** 48/49 câu (98,0%) đưa đúng mục vào 3 kết quả đầu; 43/49 đứng đầu.
- **Mẫu số:** 49 câu được chấm trong bộ 57 câu; 8 câu ngoài mô hình truy xuất mục bị loại.
- **Phạm vi:** BM25 với từ khóa đã được lấy từ một lượt trợ lý và cố định.
- **Điều cần hiểu:** bộ tìm kiếm có khả năng đưa mục cần tra vào tập ứng viên nhỏ.
- **Nguy cơ hiểu sai:** không phải độ chính xác câu trả lời và không đo tạo từ khóa ở câu mới.
- **Cách trình bày:** số lớn `48/49` + nhãn `đưa đúng mục vào 3 kết quả đầu`; `43 đứng đầu` ở chú thích nhỏ, không thành ô riêng.

### 2. Hai thước đo toàn quy trình — 55/58 và 52/58

- **Con số:** 55/58 câu truy xuất đúng mục cần tìm; 52/58 câu trả lời được mô hình chấm đúng.
- **Mẫu số:** 58 câu có dữ kiện và nhãn mục cần tra để đối chiếu.
- **Phạm vi:** tác tử thật, lấy ba kết quả đầu, một lượt độc lập cho mỗi câu.
- **Điều cần hiểu:** truy xuất mục cần tra và chất lượng câu trả lời là hai phép đo khác nhau trên cùng 58 câu.
- **Nguy cơ hiểu sai:** 52/58 do mô hình chấm, cùng mô hình với trợ lý; không phải chấm người độc lập.
- **Cách trình bày:** một ô chia đôi `55/58 đúng mục | 52/58 [a] câu trả lời đúng`; không dùng mũi tên vì hai tập trường hợp không lồng hoàn toàn. Dấu `[a]` dẫn tới ghi chú phương pháp chấm.

### 3. Từ chối — 19/19

- **Con số:** 11/11 câu ngoài phạm vi + 8/8 câu hỏi vào khoảng trống được mô hình chấm là từ chối.
- **Mẫu số:** 19 tình huống cố định cần từ chối.
- **Phạm vi:** cùng một lượt đánh giá 85 câu.
- **Điều cần hiểu:** từ chối là hành vi có chủ đích, không phải lỗi giao diện.
- **Nguy cơ hiểu sai:** không suy rộng thành “từ chối sai bằng 0 trong thực tế”.
- **Cách trình bày:** `19/19 [a]` + nhãn `được mô hình chấm là từ chối`.

### 4. Thời gian — trung vị 2,0 giây

- **Con số:** trung vị 2,0 giây; phân vị 95 là 2,9 giây; dài nhất 21,9 giây.
- **Mẫu số:** 85 lượt tuần tự, mỗi lượt độc lập.
- **Phạm vi:** toàn lượt, gồm LLM qua mạng; 78 lượt có tra cứu.
- **Điều cần hiểu:** phần lớn thời gian nằm ở LLM/mạng, không phải tra đồ thị.
- **Nguy cơ hiểu sai:** không phải cam kết mức dịch vụ; giá trị dài nhất vẫn phải có trong tài liệu chi tiết.
- **Cách trình bày:** ô nhỏ `2,0 giây` + nhãn `trung vị toàn lượt, 85 tình huống`; phân vị 95 đặt trong chú thích chung.

### Phân nhóm phạm vi bắt buộc trong dải số liệu

- Trên ô `48/49`: **“Truy xuất riêng · 49 câu được chấm · từ khóa cố định”**.
- Trên cụm ba ô còn lại: **“Toàn quy trình · 85 tình huống · một lượt”**.
- Chú thích `[a]`: **“Cùng mô hình làm trợ lý và chấm; 4/85 phán quyết của bộ chấm được đánh dấu cần đọc lại.”**
- Ghi chú cuối cụm: **“Kết quả không đại diện cho mọi câu hỏi thực tế.”**

Tên mô hình `lightning-ai/gemma-4-31B-it` có thể chuyển xuống QR/báo cáo nếu không đủ chỗ, nhưng hai nhãn phạm vi, “một lượt” và “mô hình chấm” phải còn trên poster.

## Ảnh chụp được chọn

1. `docs/images/giao-dien-dang-tra-cuu.png`, cắt lấy câu hỏi và dòng từ khóa.
2. `docs/images/giao-dien-tra-loi.png`, dùng hai cửa sổ cắt từ cùng ảnh để thấy mở đầu trả lời và dòng nguồn.

Không chọn ảnh chụp từ chối trong phương án chính vì số liệu 19/19 và ô nhấn về nhánh từ chối đã kể hành vi đó. `giao-dien-tu-choi.png` là lựa chọn thay thế nếu bỏ khối cập nhật SHACL.

## Mức chi tiết kỹ thuật

### Thuật ngữ giữ lại

- **LLM:** hiểu cách hỏi, tạo từ khóa, diễn đạt.
- **BM25:** xếp hạng mục theo mức khớp từ khóa.
- **RDF/TriG:** cách biểu diễn đồ thị tri thức và nhóm dữ kiện theo nguồn.
- **SHACL:** kiểm cấu trúc dữ liệu khi cập nhật.

### Chỉ nói bằng ngôn ngữ chức năng

- “đồ thị tri thức” thay cho mô tả quad/named graph trong nội dung chính;
- “đọc lại hồ sơ dữ kiện kèm nguồn đã khai báo” thay cho thuật ngữ cài đặt về việc dựng hồ sơ;
- “công cụ tra cứu” thay cho tên hàm;
- dùng “môi trường vận hành”, không dùng từ tiếng Anh tương ứng;
- “cơ chế dự phòng” chỉ dùng nếu thật sự cần, ưu tiên mô tả hành vi cụ thể.

### Không đưa dù đúng kỹ thuật

RDFS, SKOS, API, JSON và SSE chỉ xuất hiện nếu hội đồng hỏi miệng; poster không cần chúng để hiểu đóng góp. SPARQL và OWL không được dùng như nhãn trang trí vì bộ tìm kiếm hiện hành không dựa trên suy luận OWL/SPARQL.

## QR và tài liệu tham khảo

### QR

Khuyên dùng một QR dẫn tới bản dùng thử thật:

- URL hiện có trong kho mã nguồn và đã phản hồi HTTP 200 ngày 15/09/2026: `https://ontchatbot.vercel.app/`
- Chú thích: **“Quét để thử hệ thống”**
- In URL ngắn ngay dưới QR để còn đường dự phòng.

Kho mã nguồn thật `https://github.com/vpthinh19/ontology-chatbot` có thể in thành một dòng nhỏ “Tài liệu dự án và mã nguồn”. Kho hiện chưa có một tệp báo cáo nghiên cứu đầy đủ được xác định rõ, nên chỉ dùng nhãn “Báo cáo đầy đủ” sau khi nhóm cung cấp URL thật. Trước khi in, người dùng phải kiểm lại mọi URL.

### Tài liệu tham khảo trên poster

Dùng cả hai tầng:

- 3 tài liệu nền tảng rất ngắn ở chân trang: BM25 (Robertson & Zaragoza, 2009), RDF 1.1 TriG (W3C, 2014), SHACL (W3C, 2017);
- QR/kho mã nguồn dẫn tới tài liệu dự án và danh mục đầy đủ; báo cáo đầy đủ chỉ thêm khi có liên kết thật.

Lựa chọn này giữ tính học thuật mà không chiếm một cột cho references.

## Tiêu chí tự kiểm nội dung

### Bài kiểm tra 10 giây

- Đọc được tên đề tài và câu chốt LLM–đồ thị.
- Nhìn hình trung tâm nhận ra luồng câu hỏi → tra cứu → câu trả lời có căn cứ.
- Một số liệu lớn đủ kéo mắt nhưng không lấn tiêu đề.

### Bài kiểm tra 1 phút

- Nói lại được vai trò của LLM, BM25 và đồ thị.
- Nhìn thấy 48/49, 55/58, 52/58 và 19/19 cùng mẫu số.
- Biết hệ thống nói giới hạn khi thiếu dữ kiện.

### Bài kiểm tra 3 phút

- Hiểu truy nguyên nguồn và cập nhật có kiểm soát.
- Hiểu đây là bản thử nghiệm trên phần dữ liệu đã biểu diễn.
- Nhớ các giới hạn về độ phủ, từ vựng và thiết kế đánh giá.
