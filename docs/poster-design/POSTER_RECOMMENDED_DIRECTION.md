# PHƯƠNG ÁN POSTER ĐƯỢC KHUYÊN DÙNG

> **Đây là wireframe, không phải poster cuối.** Tệp này là đặc tả định hướng kèm sơ đồ khung.

## 1. Quyết định thiết kế

Chọn phương án **“Dòng chảy có căn cứ”** kết hợp phong cách **“Học thuật sáng – điểm nhấn đồ thị tri thức”**.

Poster dùng nền sáng, tiêu đề xanh lam đậm, các nút và đường nối màu xanh ngọc cho phần dữ liệu, xanh lam cho vai trò của LLM, vàng hổ phách cho nguồn và các lưu ý giới hạn. Bố cục là những dải ngang rõ ràng trên khổ dọc 80 × 130 cm; hình trung tâm chiếm diện tích lớn nhất. Các khối không được đóng trong quá nhiều hộp có viền nặng.

Ấn tượng cần đạt được là: **một công trình nghiên cứu có quy trình có căn cứ và phạm vi đánh giá rõ**, hiện đại nhưng không mang dáng dấp quảng cáo sản phẩm.

## 2. Câu chuyện khoa học được giữ lại

Poster chỉ kể một câu chuyện:

1. Câu hỏi học vụ có nhiều cách diễn đạt, nhưng câu trả lời cần dựa trên dữ kiện và nguồn chính thức.
2. Với câu cần tra cứu, LLM hiểu câu hỏi và tạo cụm từ; BM25 tìm các mục liên quan; đồ thị tri thức cung cấp hồ sơ dữ kiện kèm nguồn đã khai báo; LLM diễn đạt câu trả lời.
3. Trên bộ đánh giá cố định, quy trình này truy xuất đúng mục trong phần lớn trường hợp; 19/19 tình huống đã thiết kế là ngoài phạm vi hoặc thiếu dữ kiện được mô hình chấm là từ chối.

Những phần không phục vụ trực tiếp ba ý trên được loại khỏi bề mặt chính.

## 3. Điểm bắt đầu và đường đi của mắt

Người xem bắt đầu ở phần trên cùng với tên đề tài, rồi đi theo trục dọc:

1. **Tên đề tài và câu chốt**: nhận ra ngay bài toán và sự phân vai giữa LLM với đồ thị tri thức.
2. **Bài toán**: hiểu vì sao chỉ tạo một chatbot là chưa đủ.
3. **Hình trung tâm**: đọc quy trình từ câu hỏi đến câu trả lời có căn cứ.
4. **Dải kết quả**: nhìn thấy bốn cụm số liệu lớn mà không cần đọc đoạn văn.
5. **Bằng chứng hành vi, đóng góp và giới hạn**: xem hệ thống thực sự tra cứu, trả lời và chỉ nguồn như thế nào, đồng thời đọc đúng phạm vi của bằng chứng.
6. **Kết luận và QR**: chốt giá trị nghiên cứu và biết nơi xem thêm.

Không dùng mũi tên buộc người xem phải nhảy qua lại giữa ba cột. Trục đọc chính luôn từ trên xuống; trong hình trung tâm, người xem theo số 1–3 từ trái sang phải rồi 4–6 từ phải sang trái.

## 4. Bản đồ trang 80 × 130 cm

Lề an toàn: 3,2 cm mỗi cạnh. Chiều rộng nội dung hữu dụng: 73,6 cm. Dùng lưới 12 cột, khoảng cách giữa hai cột 0,7 cm.

| Vùng | Tọa độ dọc gợi ý | Chiều cao | Tỷ lệ gần đúng | Nội dung |
|---|---:|---:|---:|---|
| Nhận diện và tiêu đề | 3,2–21,2 cm | 18 cm | 14% | Logo, đơn vị, tên đề tài, tác giả, mã đề tài |
| Câu chốt và bài toán | 22,4–32,4 cm | 10 cm | 8% | Câu chốt lớn, một câu vấn đề và ba ý ngắn |
| Hình trung tâm | 33,6–67,6 cm | 34 cm | 26% | Quy trình “câu hỏi → hiểu ý → truy xuất → đọc dữ kiện → trả lời” và nhánh nguồn chính thức |
| Kết quả nổi bật | 68,8–88,8 cm | 20 cm | 15% | Bốn ô số liệu, dòng chú thích phạm vi |
| Bằng chứng và đóng góp | 90–114 cm | 24 cm | 18% | Hai ảnh chụp hành vi ở trái; ba đóng góp và giới hạn ở phải |
| Kết luận, QR, tài liệu | 115,2–126,8 cm | 11,6 cm | 9% | Kết luận, QR, liên hệ, 3 tài liệu nền tảng |
| Khoảng trắng và khe phân cách | Phân bố toàn trang | khoảng 12 cm | 10% | Tạo nhịp thở, phân tách cấp thông tin |

Tổng tỷ lệ chỉ mang tính định hướng; tọa độ và chiều cao là cơ sở thực tế để dựng trên Canva.

```text
┌──────────────────────────────────────────────────────────┐
│ LOGO/ĐƠN VỊ       TÊN ĐỀ TÀI                    MÃ ĐỀ TÀI │
│                TÁC GIẢ · HƯỚNG DẪN · ĐƠN VỊ              │
├──────────────────────────────────────────────────────────┤
│ CÂU CHỐT: LLM hiểu/diễn đạt; đồ thị cung cấp dữ kiện     │
│ BÀI TOÁN: nhiều cách hỏi · cần đúng dữ kiện · cần nguồn  │
├──────────────────────────────────────────────────────────┤
│                                                          │
│       HÌNH TRUNG TÂM — DÒNG CHẢY CÓ CĂN CỨ               │
│  Câu hỏi → LLM → BM25 → Đồ thị tri thức → LLM → Trả lời │
│                   ↑                                      │
│         Nguồn chính thức + kiểm tra dữ liệu               │
│                                                          │
├──────────────────────────────────────────────────────────┤
│  TRUY XUẤT RIÊNG │          TOÀN QUY TRÌNH · 85 TÌNH HUỐNG│
│   48/49       55/58 | 52/58       19/19        2,0 giây  │
├───────────────────────────────┬──────────────────────────┤
│ ẢNH 1: đang tra cứu           │ 03 ĐÓNG GÓP              │
│ ẢNH 2: trả lời + nguồn        │ TRUY NGUYÊN NGUỒN        │
│ Chú thích hành vi             │ GIỚI HẠN NGHIÊN CỨU      │
├───────────────────────────────┴──────────────────────────┤
│ KẾT LUẬN                QR · LIÊN HỆ · TÀI LIỆU NỀN TẢNG │
└──────────────────────────────────────────────────────────┘
```

## 5. Nội dung chính xác của từng vùng

### 5.1. Vùng nhận diện và tiêu đề

- Logo Trường Đại học Nha Trang ở góc trái, chỉ dùng tệp chính thức do nhóm cung cấp.
- Tên đề tài giữ nguyên nội dung chính thức, chia tối đa bốn dòng.
- Mã đề tài `SV2025-13-61` đặt nhỏ ở góc phải.
- Tác giả, giảng viên hướng dẫn và đơn vị đặt dưới tiêu đề, không cạnh tranh thị giác với tên đề tài.
Tên đề tài cho biết chủ đề; câu chốt ở dải kế tiếp mới là thứ người xem cần nhớ sau 10 giây.

### 5.2. Khối câu chốt và bài toán

Câu chốt đặt ở đầu dải trên một nền xanh rất nhạt:

> **LLM hiểu và diễn đạt; đồ thị tri thức cung cấp dữ kiện có cơ chế truy nguyên.**

Tiêu đề khối:

> **Từ nhiều cách hỏi đến một câu trả lời có căn cứ**

Nội dung:

- Nguồn học vụ gồm quy chế, quyết định, biểu mẫu và trang đơn vị.
- Câu hỏi có thể dùng cách nói đời thường, viết tắt hoặc thiếu dấu.
- Câu trả lời cần nêu căn cứ và giới hạn khi dữ liệu chưa đủ.

Không thêm tổng quan dài về chatbot, chuyển đổi số hoặc lịch sử LLM.

### 5.3. Hình trung tâm

Dùng sơ đồ mới trong `poster-diagrams/hero-workflow.mmd`, vẽ lại bằng các phần tử véc-tơ trên Canva nếu cần đồng bộ kiểu chữ.

Để vừa dải hình có tỷ lệ ngang khoảng 2,2:1, xếp luồng theo lưới 3 × 3: bước 1–3 từ trái sang phải ở hàng trên; bước 4 hạ xuống cột phải; bước 5–6 tiếp tục ở hàng dưới theo hướng phải sang trái. Hai nhánh giới hạn nằm ở hàng giữa; nguồn đi lên bước 4 từ góc phải dưới. Số thứ tự làm rõ đường đọc, nhưng không biến mỗi ghi chú thành một hộp phần mềm.

Nhánh tra cứu chính gồm sáu điểm:

1. **Câu hỏi tự nhiên**
2. **LLM hiểu ý, quyết định có cần tra cứu và tạo cụm từ khi cần**
3. **BM25 chọn ba mục liên quan nhất**
4. **Đồ thị tri thức trả hồ sơ dữ kiện kèm nguồn đã khai báo**
5. **LLM diễn đạt và được hướng dẫn đánh giá mức đủ căn cứ**
6. **Trả lời từ dữ kiện đã tra, có thể nêu nguồn đã khai báo; hoặc nêu giới hạn dữ liệu**

Nhãn “khi cần tra cứu” phải xuất hiện trên đường từ LLM đến BM25. Nhánh ngoài phạm vi dẫn tới “được hướng dẫn từ chối”; trường hợp không tìm thấy, mô hình được hướng dẫn thử lại **tối đa một lần** bằng cách diễn đạt khác. Những nhánh này thể hiện hành vi theo chỉ dẫn cho mô hình, không được vẽ như bộ kiểm tất định.

Một nhánh phụ đi từ **nguồn chính thức** đến **đồ thị tri thức**, với hai nhãn ngắn: “kiểm yêu cầu khai báo nguồn” và “kiểm cấu trúc bằng SHACL”. Nhánh này cho thấy dữ liệu được xây dựng và kiểm tra, nhưng không lấn át quy trình hỏi đáp.

Phía dưới sơ đồ đặt một câu phân vai:

> Trong thiết kế này, LLM không được dùng làm kho lưu tri thức học vụ; dữ kiện được tra từ đồ thị và đưa vào ngữ cảnh trả lời.

Không mô tả sơ đồ bằng tên tệp, lớp, hàm, khóa JSON hay gói phần mềm.

### 5.4. Dải kết quả

Bốn ô số liệu có cùng chiều cao và cùng độ rộng ba cột. Ô thứ hai chia đôi bên trong để thể hiện hai phép đo riêng; cỡ số có thể nhỏ hơn ba ô còn lại nhưng không dưới 44 pt.

Tạo hai nhãn phạm vi ngay phía trên: **“Truy xuất riêng · 49 câu được chấm · từ khóa cố định”** trên ô 1; **“Toàn quy trình · 85 tình huống · một lượt”** trải trên các ô 2–4.

| Ô | Số lớn | Nhãn | Chú thích/phạm vi |
|---|---|---|---|
| 1 | **48/49** | câu đưa đúng mục vào ba kết quả đầu | Cụm tra cứu lấy từ một lượt trợ lý rồi được cố định; 43/49 đứng đầu nếu còn chỗ |
| 2 | **55/58** và **52/58 [a]** | đúng mục; câu trả lời được mô hình chấm đúng | Hai thước đo riêng trên cùng 58 câu có nhãn mục cần tra; trình bày song song, không nối bằng mũi tên |
| 3 | **19/19 [a]** | tình huống cần từ chối được mô hình chấm là từ chối | 11 ngoài phạm vi + 8 thiếu dữ kiện |
| 4 | **2,0 giây** | trung vị thời gian hoàn tất toàn lượt | 85 câu; phân vị 95 là 2,9 giây |

Ghi chú `[a]` đặt ngay dưới cụm toàn quy trình, không đẩy xuống chú thích cuối trang:

> [a] Bộ chấm dùng cùng mô hình với hệ thống; 4/85 phán quyết của bộ chấm được đánh dấu cần xem lại. Kết quả không đại diện cho mọi câu hỏi thực tế.

Ưu tiên hiển thị phân số thay vì chỉ phần trăm để người xem luôn thấy mẫu số.

### 5.5. Bằng chứng hành vi

Nửa trái của vùng hỗ trợ dùng tối đa hai ảnh chụp, với điều kiện chụp lại đúng giao diện thật ở mật độ 2×/3× hoặc vượt kiểm tra nét ở tỷ lệ in. Nếu ảnh trải gần hết cột rộng khoảng 42,6 cm, cần tối thiểu khoảng 2.518 px ở 150 ppi và nên đạt 3.357 px ở 200 ppi. Hai ảnh hiện có rộng 1.920 px, chỉ khoảng 114 ppi trước khi cắt, nên không được mặc định là đủ cho bản in:

1. **Đang tra cứu**: cắt vào câu hỏi và trạng thái tra cứu có cụm từ tìm kiếm.
2. **Trả lời có căn cứ**: ghép hai vùng cắt từ cùng màn hình — nội dung trả lời và phần nguồn — trong một khung thống nhất.

Chú thích chung:

> Giao diện cho thấy quá trình tra cứu và câu trả lời có đường dẫn nguồn; đây là minh họa hành vi, không phải bằng chứng định lượng.

Không dùng ảnh toàn màn hình trình duyệt nếu chữ trong đó nhỏ hơn phần thân bài. Nếu ảnh hiện tại không đủ nét, bỏ khối ảnh và mở rộng phần đóng góp/giới hạn; không nội suy hoặc dựng ảnh giả. Không thêm ảnh màn hình từ chối hoặc quản trị vào phương án chính; chúng làm loãng câu chuyện và lặp lại thông tin đã có trong sơ đồ, số liệu và khối đóng góp.

### 5.6. Đóng góp và giới hạn

Nửa phải của vùng hỗ trợ có ba đóng góp, mỗi đóng góp một biểu tượng nét mảnh và tối đa hai dòng:

- **Kho tri thức có cấu trúc:** dữ kiện học vụ được tổ chức trong RDF/TriG và liên kết với nguồn khi có khai báo.
- **Tra cứu rồi đọc đầy đủ:** BM25 dùng để chọn mục; câu trả lời nhận lại hồ sơ dữ kiện đầy đủ từ đồ thị.
- **Quy trình quản trị có kiểm tra:** dữ liệu được kiểm tra trước khi ghi và nạp lại vào hệ thống.

Ngay dưới ba đóng góp, đặt một dải truy nguyên nhỏ, chỉ ba nhãn:

> **Dữ kiện → Khoản/mục/trang → Nguồn học vụ chính thức**

Chú thích một dòng: “Áp dụng cho dữ kiện có khai báo nguồn; không hàm ý mọi dữ kiện đều đã có trích dẫn.”

Tiếp theo là khối giới hạn nền vàng rất nhạt:

- Dữ liệu mới phủ một phần phạm vi học vụ; chất lượng phụ thuộc độ phủ và độ đúng của đồ thị tri thức.
- BM25 phụ thuộc từ vựng trong chỉ mục và cụm từ do LLM tạo.
- Đánh giá mới có một lượt, dùng cùng mô hình cho trợ lý và bộ chấm; chưa đối chứng RAG trên cùng bộ câu hỏi.

Đặt một câu dạng chú thích hình, cỡ 20–23 pt, cạnh hình trung tâm; không biến thành bullet giới hạn thứ tư: “Các nhánh dùng dữ kiện và từ chối là hành vi được hướng dẫn; chưa có bộ kiểm đầu ra tất định.”

Không nói SHACL “xác minh câu trả lời” hoặc “bắt buộc nguồn” vì đó không phải vai trò được triển khai.

### 5.7. Kết luận và chân trang

Kết luận ngắn:

> Cách tiếp cận tách vai trò hiểu–diễn đạt của LLM khỏi kho dữ kiện có cấu trúc, qua đó tạo nền tảng hỏi đáp học vụ có cơ chế truy nguyên ở dữ kiện đã gắn nguồn và được đánh giá theo từng tầng.

QR chính dẫn đến bản dùng thử hiện có và phải có URL chữ bên cạnh để dự phòng khi quét thất bại. Nhãn:

> **Quét để thử hệ thống**

Đặt thêm một liên kết ngắn tới kho mã nguồn với nhãn “Tài liệu dự án và mã nguồn” nếu xác nhận kho được phép công khai. Kho hiện chưa có một tệp báo cáo nghiên cứu đầy đủ được xác định rõ; không dùng nhãn hoặc đường dẫn “Báo cáo đầy đủ” nếu nhóm chưa có nơi công bố.

Chân trang dùng hai tầng: kết luận chiếm 8 cột và QR/liên hệ chiếm 4 cột ở tầng trên; một dòng tài liệu nền tảng trải đủ 12 cột ở tầng dưới. Chỉ giữ `Robertson & Zaragoza (2009) · W3C, RDF 1.1 TriG (2014) · W3C, SHACL (2017)`. Danh mục đầy đủ nằm trong tài liệu dự án hoặc báo cáo khi có liên kết thật.

## 6. Hệ thống thị giác cần khóa

- Nền toàn trang: `#F7F9FC`; khối chính: `#FFFFFF`.
- Chữ và tiêu đề: `#17324D`.
- Đồ thị tri thức và đường dữ liệu: `#0F766E`; nền phụ `#DDF4F1`.
- Vai trò LLM và các bước xử lý: `#2457A6`; nền phụ `#EAF2FF`.
- Viền/biểu tượng về nguồn và giới hạn: `#C47A12`; chữ nhỏ dùng hổ phách đậm `#8A5200`; nền phụ `#FFF4D6`.
- Kết quả tích cực: `#16803D` nhưng chỉ dùng có chọn lọc, không tô xanh mọi số liệu.
- Phông tiêu đề: Montserrat ExtraBold/Bold. Phông nội dung: Open Sans Regular/SemiBold.
- Tiêu đề đề tài: 58–68 pt; câu chốt: 40–46 pt; số liệu: 56–72 pt; tiêu đề khối: 31–36 pt; thân bài: 25–29 pt; chú thích: 20–23 pt.
- Ô nội dung bo góc 0,4 cm, viền `#CBD5E1` 0,8 pt; bóng đổ rất nhẹ hoặc không dùng.
- Biểu tượng nét mảnh, cùng một bộ; không dùng hình 3D, biểu tượng nhiều màu hoặc hiệu ứng neon.

Chi tiết đầy đủ nằm trong `POSTER_DESIGN_BRIEF.md`.

## 7. Những gì chủ động bỏ khỏi poster

- Danh sách công nghệ, cấu trúc mã nguồn, tên lớp, tên hàm và tên khóa dữ liệu.
- Bản đồ lớp đồ thị tri thức đầy đủ và các sơ đồ kiến trúc ngang vốn quá chi tiết để đọc khi in.
- Công thức BM25, tham số tinh chỉnh và bảng kết quả từng câu.
- Màn hình quản trị, lỗi xác thực và toàn bộ quy trình biên tập dữ liệu; chỉ giữ một đóng góp ngắn.
- Ảnh chụp từ chối riêng; số liệu 19/19 và nhánh “nêu giới hạn dữ liệu” đã kể ý này rõ hơn.
- Biểu đồ không có tệp thực nghiệm gốc; không biến các phân số đơn lẻ thành biểu đồ trang trí.
- Tuyên bố về giảm tải cán bộ, độ dễ dùng, loại bỏ ảo giác, triển khai toàn trường hoặc ưu thế so với RAG/truy xuất ngữ nghĩa.
- Danh mục tài liệu tham khảo dài.

Việc bỏ các mục này giúp hình trung tâm, số liệu và bằng chứng hành vi có đủ kích thước để đọc trong 1–3 phút.

## 8. Vì sao đây là phương án phù hợp nhất

So với bố cục chia hai làn, phương án này cho người xem một trục đọc đơn giản hơn và dành nhiều không gian hơn cho kết quả. So với bố cục “câu trả lời ở tâm”, nó diễn đạt rõ trình tự xử lý và ít tạo cảm giác như đồ họa thông tin quảng bá.

Nó phù hợp nhất vì:

- đặt ý tưởng nghiên cứu — sự phân vai giữa LLM, truy xuất và đồ thị tri thức — ở trung tâm;
- cho thấy nguồn chính thức đi vào kho tri thức mà không biến poster thành sơ đồ phần mềm;
- đặt số liệu ngay sau quy trình, đúng lúc người xem cần bằng chứng;
- dùng ảnh chụp như minh họa hành vi, không để giao diện lấn át nghiên cứu;
- có chỗ cho giới hạn ngay cạnh đóng góp, giảm nguy cơ diễn giải quá mức;
- dễ dựng bằng lưới, hình cơ bản và văn bản trên Canva.

Mức khó thực hiện trên Canva: **trung bình**. Phần cần nhiều công nhất là vẽ lại hình trung tâm và cắt ảnh chụp; các vùng còn lại dùng thành phần lặp có thể sao chép.

## 9. Tự phản biện theo ba khoảng thời gian

### Bài kiểm tra 10 giây

Người đứng cách vài mét phải nhận ra được:

- đây là hệ thống hỏi đáp học vụ cho sinh viên Trường Đại học Nha Trang;
- câu chốt “LLM hiểu và diễn đạt; đồ thị tri thức cung cấp dữ kiện có cơ chế truy nguyên”;
- hình trung tâm là dòng đi từ câu hỏi đến câu trả lời có căn cứ;
- ít nhất hai số lớn: 48/49 và 19/19.

Nguy cơ chính là tên đề tài dài lấn câu chốt. Cách xử lý: giới hạn tên đề tài bốn dòng, không làm tên tác giả quá lớn và giữ một dải riêng cho câu chốt.

### Bài kiểm tra 1 phút

Người xem phải đọc được sáu bước trong hình trung tâm, hiểu BM25 chỉ chọn mục còn dữ kiện đầy đủ được đọc từ đồ thị, rồi liên hệ quy trình với bốn cụm số liệu.

Nguy cơ chính là sơ đồ nhiều chữ. Cách xử lý: mỗi nút tối đa hai dòng, chỉ dùng một câu phân vai bên dưới và loại mọi thuật ngữ cài đặt.

### Bài kiểm tra 3 phút

Người xem phải hiểu được đóng góp về dữ liệu có cấu trúc, truy nguyên nguồn, quy trình quản trị có kiểm tra; đồng thời thấy rõ phạm vi đánh giá và các giới hạn.

Nguy cơ chính là số liệu bị hiểu như kết quả phổ quát. Cách xử lý: đặt dòng phạm vi ngay dưới dải số liệu, giữ mẫu số và ghi rõ một lần chạy, bộ chấm bằng mô hình.

Nếu bản dựng thử không vượt qua một trong ba bài kiểm tra, ưu tiên giảm chữ trong khối đóng góp hoặc chân trang; không thu nhỏ hình trung tâm và số liệu để giữ thêm nội dung.

## 10. Trình tự dựng trên Canva

1. Tạo kích thước tùy chỉnh 80 × 130 cm, bật lề và vùng tràn lề theo yêu cầu nhà in.
2. Dựng lưới 12 cột và các đường dẫn ngang theo tọa độ trong bảng bố cục.
3. Khóa nền, vùng tiêu đề và dải câu chốt.
4. Vẽ hình trung tâm bằng hình cơ bản và đường nối; kiểm tra ở mức thu nhỏ 25%.
5. Tạo một ô số liệu mẫu, sau đó nhân bản để giữ kiểu chữ và khoảng cách nhất quán.
6. Chỉ cắt ảnh từ bản chụp lại đủ nét hoặc tệp gốc đã vượt kiểm tra in; nếu không đạt, bỏ khối ảnh.
7. Đưa nội dung ngắn từ `POSTER_CONTENT_COPY_DRAFT.md` vào từng vùng và kiểm tra tổng lượng chữ.
8. Tạo QR từ liên kết đã được xác nhận, thêm URL chữ và quét thử từ bản in thử.
9. Kiểm tra độ tương phản, lỗi dấu tiếng Việt, tên riêng, mẫu số và chú thích phạm vi.
10. Xuất bản in theo thông số nhà in; xem PDF ở kích thước thật trước khi gửi.

## 11. Người dùng cần chuẩn bị gì trước khi bắt đầu dựng trên Canva?

- [ ] Logo chính thức của Trường Đại học Nha Trang ở định dạng SVG, PDF hoặc PNG nền trong suốt độ phân giải cao.
- [ ] Tên đầy đủ, thứ tự và cách ghi đơn vị của tác giả; tên giảng viên hướng dẫn; thư điện tử hoặc đầu mối liên hệ.
- [ ] Xác nhận lần cuối tên đề tài, mã `SV2025-13-61` và quy tắc nhận diện của trường/khoa.
- [ ] Xác nhận dùng bản dùng thử làm đích QR như phương án khuyên dùng, hoặc thay bằng báo cáo/video/trang tổng hợp đã có URL cuối; không dùng liên kết tạm thời.
- [ ] Xác nhận kho mã nguồn có thể công khai trước khi in liên kết “Tài liệu dự án và mã nguồn”.
- [ ] Tệp ảnh chụp gốc, không nén, và kiểm tra không lộ thông tin cá nhân hoặc dữ liệu không được phép công bố.
- [ ] Chụp lại giao diện thật nếu cần: tối thiểu khoảng 2.518 px cho vùng in rộng 42,6 cm ở 150 ppi, mục tiêu 3.357 px ở 200 ppi; nếu không đạt thì quyết định bỏ ảnh.
- [ ] Chốt phiên bản số liệu. Nếu chạy lại đánh giá, cập nhật đồng thời các phân số, cỡ mẫu, thời gian và chú thích giới hạn.
- [ ] Thông tin xuất file của nhà in: vùng tràn lề, hệ màu, định dạng PDF, loại giấy và khoảng cách an toàn.
- [ ] Kiểm tra Montserrat và Open Sans có sẵn trong tài khoản Canva; nếu thiếu, dùng Noto Sans nhất quán.
- [ ] Quyền sử dụng logo, ảnh chụp và các trích dẫn nguồn trong bối cảnh hội thảo.
- [ ] Một bản in thử thu nhỏ để kiểm tra thứ tự đọc; một đoạn giấy in ở tỷ lệ 100% để kiểm tra cỡ chữ nhỏ nhất.
- [ ] Điện thoại dùng mạng di động để quét thử QR từ khoảng cách thực tế trước khi duyệt in.
