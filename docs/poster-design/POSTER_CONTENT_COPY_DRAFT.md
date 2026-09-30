# Bản nháp nội dung chữ dành cho poster

> Đây là thư viện câu chữ và một bản lắp ghép đề xuất, không phải poster cuối. Các phương án thay thế không được đặt đồng thời; chọn một để giữ ngân sách chữ.

## 1. Khối nhận diện

### Nhãn nhỏ phía trên

> NGHIÊN CỨU KHOA HỌC SINH VIÊN · MÃ ĐỀ TÀI SV2025-13-61

### Tên đề tài chính thức

> XÂY DỰNG HỆ THỐNG HỎI ĐÁP TỰ ĐỘNG VỀ QUY TRÌNH HỌC VỤ CHO SINH VIÊN TRƯỜNG ĐẠI HỌC NHA TRANG DỰA TRÊN ONTOLOGY VÀ MÔ HÌNH NGÔN NGỮ

Gợi ý ngắt dòng, không đổi chữ:

> XÂY DỰNG HỆ THỐNG HỎI ĐÁP TỰ ĐỘNG<br>
> VỀ QUY TRÌNH HỌC VỤ CHO SINH VIÊN<br>
> TRƯỜNG ĐẠI HỌC NHA TRANG<br>
> DỰA TRÊN ONTOLOGY VÀ MÔ HÌNH NGÔN NGỮ

### Tác giả/đơn vị — chỗ trống bắt buộc thay

> [HỌ TÊN TÁC GIẢ] · [LỚP/KHOA/VIỆN]<br>
> Giảng viên hướng dẫn: [HỌ TÊN] · [ĐƠN VỊ]<br>
> [THƯ ĐIỆN TỬ LIÊN HỆ]

Không tự suy ra tên tác giả từ Git identity.

## 2. Câu chốt — chọn 1

### Phương án A — khuyên dùng

> **LLM hiểu và diễn đạt; đồ thị tri thức cung cấp dữ kiện có cơ chế truy nguyên.**

### Phương án B — nhấn trải nghiệm

> **Từ câu hỏi đời thường đến câu trả lời có thể truy nguyên.**

### Phương án C — nhấn quy trình

> **Tìm mục liên quan, đọc hồ sơ dữ kiện, nêu rõ khoảng trống.**

## 3. Bài toán

### Tiêu đề khối

> **Từ nhiều cách hỏi đến một câu trả lời có căn cứ**

### Nội dung khuyên dùng

- Nguồn học vụ gồm quy chế, quyết định, biểu mẫu và trang đơn vị.
- Câu hỏi có thể dùng cách nói đời thường, viết tắt hoặc thiếu dấu.
- Câu trả lời cần nêu được căn cứ và giới hạn khi dữ liệu chưa đủ.

### Câu mục tiêu

> Xây dựng và đánh giá một quy trình hỏi đáp tách phần hiểu–diễn đạt khỏi kho dữ kiện học vụ có truy nguyên nguồn.

### Phương án ngắn hơn nếu thiếu chỗ

> Mục tiêu: trả lời câu hỏi tự nhiên bằng dữ kiện học vụ có cơ chế truy nguyên, đồng thời không tự điền phần dữ liệu còn thiếu.

## 4. Hình trung tâm

### Tiêu đề

> **LLM hiểu và diễn đạt; đồ thị tri thức cung cấp dữ kiện**

### Nhãn trên luồng hỏi đáp

1. **Câu hỏi tự nhiên**
   “Em muốn xin nghỉ học”
2. **LLM hiểu ý và quyết định có cần tra cứu**
3. **Khi cần: LLM tạo cụm tra cứu**
   “nghỉ học tạm thời” · “bảo lưu kết quả học tập”
4. **BM25 chọn 3 mục liên quan**
5. **Đọc đủ hồ sơ dữ kiện**
   từ đồ thị tri thức RDF/TriG
6. **LLM được hướng dẫn diễn đạt và đánh giá mức đủ căn cứ**

### Hai nhánh kết quả

- **Có căn cứ:** trả lời từ dữ kiện đã tra; giữ nguồn khi hồ sơ có khai báo.
- **Thiếu chi tiết:** được hướng dẫn nêu giới hạn của dữ liệu hiện có.
- **Ngoài phạm vi:** được hướng dẫn từ chối mà không cần tra cứu.
- **Không tìm thấy:** được hướng dẫn thử lại tối đa một lần bằng cách diễn đạt khác; nếu vẫn không có, nêu giới hạn dữ liệu.

### Nhánh xây dựng tri thức phía dưới

> **Nguồn học vụ chính thức → biên soạn → đồ thị tri thức có cơ chế gắn nguồn**

> Khi cập nhật: kiểm yêu cầu nguồn và cấu trúc SHACL trước khi ghi.

### Hai nhãn phân vai

- Gắn cạnh LLM: **Hiểu cách hỏi · chọn từ khóa · diễn đạt**
- Gắn cạnh đồ thị: **Lưu dữ kiện · quan hệ · vị trí nguồn khi được khai báo**

### Chú thích hình trung tâm

> BM25 chỉ chọn mục. Sau xếp hạng, hệ thống quay lại đồ thị để đọc đầy đủ hồ sơ dữ kiện, kèm phần nguồn đã khai báo của từng mục.

## 5. Truy nguyên và cập nhật

### Tiêu đề khối

> **Dữ kiện không đứng một mình**

### Nội dung

> Mỗi dữ kiện cần nguồn được nối với vị trí cụ thể trong văn bản và đường dẫn tới nguồn. Khi quy định đổi, người biên soạn có thể cập nhật dữ liệu mà không huấn luyện lại LLM.

### Sơ đồ nhỏ ba nhãn

> **Dữ kiện** → **Khoản/mục/trang** → **Nguồn học vụ chính thức**

### Ô nhấn về cập nhật

> **Biểu mẫu theo lược đồ**
> Kiểm yêu cầu khai báo nguồn → kiểm cấu trúc bằng SHACL → ghi dữ liệu → dựng lại chỉ mục

Không viết “SHACL xác minh nguồn” hoặc “SHACL kiểm câu trả lời”.

## 6. Đóng góp — chọn tối đa 3 ý ngắn

### Tiêu đề khối

> **Ba đóng góp của cách tiếp cận**

- **Kho tri thức có cấu trúc:** dữ kiện học vụ được tổ chức trong RDF/TriG.
- **Tra cứu rồi đọc đầy đủ:** BM25 chọn mục; đồ thị trả hồ sơ dữ kiện.
- **Quản trị có kiểm tra:** kiểm yêu cầu khai báo nguồn và SHACL trước khi ghi.

Phương án thay ý thứ ba nếu muốn nhấn truy nguyên:

- **Truy nguyên theo dữ kiện:** nối dữ kiện cần nguồn với vị trí trong văn bản.

## 7. Kết quả

### Tiêu đề khối

> **Bằng chứng trên bộ đánh giá cố định**

### Ô số liệu 1 — truy xuất riêng

> **TRUY XUẤT RIÊNG · 49 CÂU ĐƯỢC CHẤM · TỪ KHÓA CỐ ĐỊNH**
> **48/49**
> câu đưa đúng mục vào 3 kết quả đầu
> *Cụm tra cứu lấy từ một lượt trợ lý rồi cố định; 43/49 đứng đầu.*

### Nhãn chung phía trên ô 2–4

> **TOÀN QUY TRÌNH · 85 TÌNH HUỐNG · MỘT LƯỢT**

### Ô số liệu 2 — hai thước đo toàn quy trình

> **55/58** đúng mục  |  **52/58** [a] được mô hình chấm đúng
> *58 câu có nhãn mục cần tra để đối chiếu.*

### Ô số liệu 3 — từ chối

> **19/19** [a]
> tình huống cần từ chối được mô hình chấm là từ chối
> *11 ngoài phạm vi + 8 khoảng trống dữ liệu.*

### Ô số liệu 4 — thời gian

> **2,0 giây**
> trung vị toàn lượt, 85 tình huống
> *Phân vị 95 là 2,9 giây; gồm LLM qua mạng.*

### Ghi chú phương pháp bắt buộc dưới cụm toàn quy trình

> [a] Cùng mô hình làm trợ lý và chấm; 4/85 phán quyết của bộ chấm được đánh dấu cần đọc lại. Mỗi câu chạy độc lập, lấy ba kết quả đầu. Kết quả chỉ áp dụng cho phần dữ liệu đã biểu diễn.

### Phương án ghi chú ngắn hơn

> *Toàn quy trình: 85 tình huống cố định, một lượt chạy. Cùng mô hình làm trợ lý và chấm; 4/85 phán quyết cần đọc lại. Không đại diện cho mọi câu hỏi thực tế.*

## 8. Ảnh chụp giao diện

### Ảnh chụp 1 — đang tra cứu

> **Từ cách hỏi đời thường đến cụm tra cứu**
> LLM tạo các cách gọi gần với ngôn ngữ học vụ; giao diện cho người xem thấy các cụm đã dùng.

### Ảnh chụp 2 — câu trả lời

> **Từ dữ kiện đến câu trả lời có căn cứ**
> Câu trả lời giữ liên kết biểu mẫu và chỉ ra văn bản làm nguồn.

### Ảnh chụp thay thế — từ chối

> **Không đủ dữ kiện thì nói rõ giới hạn**
> Hệ thống không biến mức học phí riêng của một ngành thành một con số chung khi dữ liệu chưa có.

## 9. Kết luận

### Bản khuyên dùng

> Kết quả ban đầu cho thấy chuỗi **LLM → công cụ tra cứu → đồ thị tri thức** khả thi trên phần nội dung đã biểu diễn. Giá trị của thiết kế không chỉ nằm ở việc trả lời, mà còn ở cơ chế truy nguyên cho dữ kiện có gắn nguồn và khả năng nêu rõ khi chưa đủ dữ kiện.

### Bản ngắn

> Cách tiếp cận khả thi trên bộ thử nghiệm hiện có: trả lời từ dữ kiện trong đồ thị, hỗ trợ truy nguyên khi có nguồn khai báo và nêu giới hạn khi dữ liệu thiếu.

## 10. Giới hạn và hướng phát triển

### Tiêu đề khối

> **Kết quả cần được đọc cùng giới hạn**

### Ba bullet giới hạn — khuyên dùng

- Dữ liệu mới phủ một phần phạm vi học vụ dự kiến.
- BM25 phụ thuộc từ vựng và từ khóa do LLM tạo.
- Đánh giá mới có một lượt; cùng mô hình làm trợ lý và chấm.

### Dòng bắt buộc nếu còn chỗ

> Chưa có đối chứng RAG hoặc truy xuất ngữ nghĩa trên cùng bộ câu hỏi.

### Hướng phát triển

> Mở rộng độ phủ; thu câu hỏi thật; chạy nhiều lượt với người chấm độc lập; so sánh RAG trên cùng bộ đánh giá.

## 11. QR và liên hệ

### QR chính — khuyên dùng

> **Quét để thử hệ thống**
> `ontchatbot.vercel.app`

### Dòng phụ

> Tài liệu dự án và mã nguồn: `github.com/vpthinh19/ontology-chatbot`

Trước khi in, tạo QR từ đúng URL đầy đủ `https://ontchatbot.vercel.app/`, quét thử bằng ít nhất hai điện thoại và giữ URL chữ bên dưới.

## 12. Tài liệu nền tảng ở chân poster

> Robertson & Zaragoza (2009) · W3C, *RDF 1.1 TriG* (2014) · W3C, *SHACL* (2017)
> Danh mục đầy đủ và tệp thực nghiệm: xem tài liệu dự án trong kho mã nguồn; chỉ ghi “báo cáo đầy đủ” khi nhóm cung cấp liên kết thật.

## 13. Bản chữ chốt để dán lên Canva

Khối dưới đây là bản lắp ghép thực sự, không phải danh sách chọn. Nó có **549 từ nhìn thấy**, đếm theo khoảng trắng và không tính ba dòng tác giả; tính cả chỗ trống tác giả là 569 từ. Con số này nằm trong ngân sách 460–600 từ. Khi thay chỗ trống bằng tên thật, kiểm lại nhưng không co thân bài dưới 24 pt.

```text
Nghiên cứu khoa học sinh viên · SV2025-13-61

XÂY DỰNG HỆ THỐNG HỎI ĐÁP TỰ ĐỘNG VỀ QUY TRÌNH HỌC VỤ CHO SINH VIÊN TRƯỜNG ĐẠI HỌC NHA TRANG DỰA TRÊN ONTOLOGY VÀ MÔ HÌNH NGÔN NGỮ

[HỌ TÊN TÁC GIẢ] · [LỚP/KHOA/VIỆN]
Giảng viên hướng dẫn: [HỌ TÊN] · [ĐƠN VỊ]
[THƯ ĐIỆN TỬ LIÊN HỆ]

LLM hiểu và diễn đạt; đồ thị tri thức cung cấp dữ kiện có cơ chế truy nguyên.

Từ nhiều cách hỏi đến câu trả lời có căn cứ

Nguồn học vụ gồm quy chế, biểu mẫu, trang đơn vị.
Cách hỏi có thể đời thường, viết tắt hoặc thiếu dấu.
Câu trả lời cần dựa trên dữ kiện đã biểu diễn và nêu giới hạn khi dữ liệu thiếu.

LLM hiểu; BM25 tìm mục; đồ thị cung cấp dữ kiện

Câu hỏi → LLM hiểu ý, tạo cụm tra cứu khi cần → BM25 chọn 3 mục → đồ thị trả hồ sơ kèm nguồn đã khai báo → LLM diễn đạt.

Đủ dữ kiện: trả lời từ hồ sơ.
Thiếu chi tiết: nêu giới hạn dữ liệu.
Ngoài phạm vi: từ chối.
Không tìm thấy: thử lại tối đa một lần bằng cách gọi khác; vẫn thiếu thì nêu giới hạn.

Đây là hướng dẫn cho mô hình; chưa có bộ kiểm đầu ra tất định.

Nguồn học vụ chính thức → biên soạn → kiểm yêu cầu khai báo nguồn → SHACL kiểm cấu trúc → đồ thị tri thức.

Ba đóng góp

Kho tri thức có cấu trúc · Tra cứu rồi đọc đầy đủ · Quản trị có kiểm tra

Dữ kiện → Khoản/mục/trang → Nguồn học vụ chính thức
Chỉ áp dụng cho dữ kiện có khai báo nguồn.

Bằng chứng trên bộ đánh giá cố định

Truy xuất riêng · 49 câu được chấm · từ khóa cố định
48/49 đưa đúng mục vào 3 kết quả đầu; 43/49 đứng đầu.
Cụm tra cứu lấy từ một lượt trợ lý rồi được cố định.

Toàn quy trình · 85 tình huống · một lượt
Hai phép đo riêng trên cùng 58 câu có nhãn mục cần tra.
55/58 truy xuất đúng mục.
52/58 [a] câu trả lời được mô hình chấm đúng.
19/19 [a] tình huống cần từ chối được mô hình chấm là từ chối: 11 ngoài phạm vi và 8 khoảng trống dữ liệu.
2,0 giây: trung vị hoàn tất toàn lượt.

[a] Cùng mô hình làm trợ lý và chấm; 4/85 phán quyết cần đọc lại. Kết quả không đại diện mọi câu hỏi thực tế.

Minh họa

Tra cứu: cụm từ gửi tới công cụ.
Trả lời: dữ kiện kèm đường dẫn nguồn.

Kết quả cần đọc cùng giới hạn

Dữ liệu mới phủ một phần phạm vi; chất lượng phụ thuộc đồ thị tri thức.
BM25 phụ thuộc từ vựng và cụm từ do LLM tạo.
Đánh giá mới có một lượt, dùng cùng mô hình cho trợ lý và bộ chấm; chưa đối chứng RAG trên cùng bộ câu hỏi.

Kết luận

Trên bộ thử nghiệm hiện có, cách phân vai LLM–BM25–đồ thị tri thức khả thi trong tra dữ kiện, truy nguyên nguồn đã khai báo và nêu giới hạn.

Quét để thử hệ thống
ontchatbot.vercel.app
Tài liệu dự án và mã nguồn: github.com/vpthinh19/ontology-chatbot

Robertson & Zaragoza (2009) · W3C, RDF 1.1 TriG (2014) · W3C, SHACL (2017)
```

Nếu hai ảnh chụp không đạt độ nét ở kích thước in, xóa cả nhãn “Minh họa” và hai chú thích; dùng diện tích đó để tăng khoảng trắng, không thay bằng ảnh giả. Không bao giờ cắt mẫu số, nhãn “mô hình chấm” hoặc ba giới hạn.
