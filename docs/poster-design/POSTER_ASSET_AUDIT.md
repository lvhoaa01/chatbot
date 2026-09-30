# Kiểm toán tài sản hình ảnh cho poster

## Kết luận nhanh

Kho mã nguồn có một bộ ảnh chụp giao diện phù hợp về nội dung và bảy sơ đồ có cả PNG lẫn SVG. Chất lượng in của ảnh chụp cần được kiểm lại hoặc chụp lại ở mật độ điểm ảnh cao. **Không sơ đồ hiện có nào nên được dùng nguyên làm hình trung tâm**: chúng được tạo để giải thích phần triển khai trong README, có nhiều thuật ngữ và chi tiết nhỏ hơn mức một poster hội thảo cần.

Phương án tái sử dụng tốt nhất:

1. dùng hai ảnh giao diện thật, cắt sát hành vi sau khi kiểm chất lượng in;
2. dựng lại hình trung tâm ở mức khái niệm từ bằng chứng của các sơ đồ hiện có;
3. ưu tiên SVG khi cần lấy lại một thành phần véc-tơ;
4. tạo ô số liệu mới trong Canva từ số liệu đã xác minh, không chụp bảng trong README.

## Cách kiểm toán

- Rà toàn bộ kho mã nguồn theo định dạng PNG, SVG, PDF, ICO, HTML/CSS và nguồn Mermaid.
- Đọc kích thước ảnh điểm trực tiếp từ tệp.
- Kiểm tra trực quan từng ảnh trong `docs/images/` ở độ phân giải gốc.
- Đối chiếu ảnh giao diện với trạng thái được triển khai trong `webui/`.

Các PNG sơ đồ là 2× bản SVG tương ứng, rộng 2440 px và khai báo 96 ppi. Các ảnh chụp rộng 1920 px. Ppi nhúng không quyết định chất lượng cuối cùng; số điểm ảnh và kích thước đặt trên poster mới là điều cần kiểm. Nếu trải ảnh gốc trên cột rộng khoảng 42,6 cm, 1920 px chỉ tương đương khoảng 114 ppi; cần khoảng 2518 px cho 150 ppi và 3357 px cho 200 ppi, trước khi tính phần bị mất do cắt. Riêng vùng cắt gợi ý của ảnh “đang tra cứu” chỉ khoảng 1610 × 205 px: ở 300 ppi, nó tương ứng khoảng 13,6 × 1,7 cm. Vì vậy **không trải vùng cắt hiện tại trên khối rộng 7 cột**. Trước khi dựng, nên chụp lại đúng giao diện thật ở mật độ 2×/3× hoặc bỏ ảnh nếu bản in thử không đạt; không nội suy để giả độ nét.

## Sơ đồ hiện có

Mỗi hàng dưới đây áp dụng cho cả PNG trong `docs/images/` và SVG cùng tên trong `docs/diagrams/`, trừ khi ghi khác.

| Asset | Kích thước PNG / SVG | Nội dung | Chất lượng và vấn đề | Xử lý cho poster |
|---|---|---|---|---|
| `tong-quan` | 2440 × 1400 px / viewBox 1220 × 700 | Hai luồng: trả lời câu hỏi và xây dựng/cập nhật tri thức | Logic đúng nhưng có bảy khối triển khai, hai vùng nét đứt, chữ “API + Agent”, “Search engine”, “tool”; hướng ngang dài không hợp khổ dọc | **Thiết kế lại.** Dùng làm bằng chứng để tạo hình trung tâm 5 chặng xử lý và một đầu ra bằng tiếng Việt, không dùng ảnh nguyên |
| `luong-mot-luot-hoi` | 2440 × 1280 / 1220 × 640 | Sơ đồ tuần tự một lượt hỏi | Thể hiện đúng thứ tự nhưng có năm làn và các chi tiết API, JSON, SSE; tỷ lệ rất ngang | **Thiết kế lại**, không cắt; lấy ý “LLM gọi tra cứu rồi nhận dữ kiện” |
| `hinh-dang-du-lieu` | 2440 × 1760 / 1220 × 880 | Dạng dữ liệu ở sáu bước | Chứa JSON, tên công cụ, khóa dữ liệu và giao thức; chính xác nhưng trái nguyên tắc “trình bày nghiên cứu, không trình bày kho mã nguồn” | **Không dùng** |
| `tui-trich-dan` | 2440 × 1280 / 1220 × 640 | Đồ thị định danh nối phát biểu với địa chỉ và nguồn | Giải thích điểm mới về truy nguyên nguồn nhưng dùng IRI, thuộc tính và ký hiệu mã; quá dày nếu thu nhỏ | **Thiết kế lại** thành một ô nhấn đơn giản: “Dữ kiện → vị trí trong văn bản → nguồn chính thức” |
| `tu-ontology-den-chi-muc` | 2440 × 1580 / 1220 × 790 | Ba loại dòng chỉ mục sinh từ đồ thị tri thức | Hữu ích cho báo cáo kỹ thuật, nhưng đầy mã định danh và JSON | **Không dùng** trên poster chính; có thể để trong báo cáo qua QR |
| `thuat-toan-tim-kiem` | 2440 × 1520 / 1220 × 760 | Cách lấy dòng tốt nhất mỗi từ khóa rồi cộng điểm mục | Có nhiều con số và dòng nhỏ; cần nhiều thời gian giải thích | **Không dùng nguyên.** Nếu hội đồng hỏi sâu, tác giả giải thích miệng; poster chỉ ghi “BM25 xếp hạng, lấy 3 mục đầu” |
| `ban-do-loai` | 2440 × 1360 / 1220 × 680 | Các lớp tri thức và quan hệ chính | Sơ đồ đẹp, véc-tơ tốt, nhưng trả lời “đồ thị có gì” thay vì ba câu hỏi chính của poster | **Không dùng**; chỉ cân nhắc ở tài liệu phụ |

### Đánh giá nguồn SVG

- Ưu điểm: véc-tơ, tỷ lệ rõ, bộ phông có Noto Sans; có thể nhập vào Canva hoặc dùng làm tham chiếu khi vẽ lại.
- Hạn chế: đây là SVG viết tay, không phải Mermaid; màu chủ yếu trắng–xám–đen và đường viền nặng, chưa theo palette poster.
- Kết luận: **không sửa các SVG báo cáo để ép thành poster**. Dùng Mermaid mới làm nguồn khái niệm, rồi dựng lại bằng hình cơ bản/biểu tượng trong Canva.

## Ảnh chụp giao diện hỏi đáp

| Asset | Kích thước | Hành vi được minh họa | Đánh giá | Xử lý |
|---|---:|---|---|---|
| `docs/images/giao-dien-dang-tra-cuu.png` | 1920 × 1290 | Câu “em muốn xin nghỉ học” được chuyển thành ba cụm tra cứu | **Rất phù hợp về nội dung, chưa đủ chắc chắn về chất lượng in lớn**; phần lớn ảnh là nền trống | Cắt vùng trên, khoảng x=150–1760, y=45–250; ưu tiên chụp lại ở mật độ 2×/3× trước khi dùng như dải ngang |
| `docs/images/giao-dien-tra-loi.png` | 1920 × 1707 | Câu trả lời thủ tục nghỉ học, liên kết tải mẫu và dòng nguồn | **Phù hợp có điều kiện**: minh họa câu trả lời có căn cứ, nhưng toàn ảnh chứa quá nhiều chữ để đọc khi thu nhỏ | Dùng **hai cửa sổ cắt từ cùng ảnh**: (a) câu hỏi + mở đầu trả lời; (b) dòng nguồn ở cuối. Ghi rõ đây là hai vùng phóng to, không sửa nội dung |
| `docs/images/giao-dien-tu-choi.png` | 1920 × 1290 | Hỏi học phí cụ thể theo ngành; hệ thống nói dữ liệu hiện có không chứa chi tiết | Hành vi rất có giá trị và câu ngắn, nhưng là nhánh phụ so với câu trả lời có nguồn | **Dự phòng.** Cắt vùng x=170–1770, y=45–245. Chỉ dùng nếu còn chỗ hoặc thay ảnh trả lời khi muốn nhấn mạnh từ chối |

### Hai ảnh chụp được chọn có điều kiện

1. **Đang tra cứu:** `giao-dien-dang-tra-cuu.png` — chú thích: “LLM chuyển cách hỏi đời thường thành các cụm tra cứu gần với ngôn ngữ học vụ.”
2. **Trả lời có căn cứ:** `giao-dien-tra-loi.png` — chú thích: “Ở lượt minh họa này, câu trả lời giữ liên kết biểu mẫu và chỉ ra văn bản làm căn cứ.”

Hai ảnh này tạo thành câu chuyện tuyến tính “hiểu cách hỏi → trả lời từ dữ kiện có nguồn” nếu được chụp lại hoặc vượt kiểm tra in. Trạng thái từ chối được kể bằng số liệu 19/19 và một ô nhấn chữ; không cần ảnh thứ ba trong phương án khuyên dùng.

### Quy tắc xử lý ảnh chụp

- Không đổi câu hỏi, câu trả lời, từ khóa hay nguồn trong ảnh.
- Không dùng mô hình màn hình điện thoại hoặc laptop; khung thiết bị là trang trí không mang bằng chứng.
- Không bo góc quá lớn; dùng bo góc 0,4 cm và viền `#CBD5E1` 0,8 pt.
- Nền ảnh chụp tối, vì vậy đặt trên ô sáng, chừa viền trắng 0,5–0,7 cm; ô dùng bo góc 0,4 cm và viền `#CBD5E1` 0,8 pt.
- Thêm chú thích bên ngoài ảnh bằng phông poster; không buộc người xem đọc toàn bộ chữ giao diện.
- Nếu dùng hai vùng cắt từ một ảnh, gắn nhãn “Phóng to từ cùng một lượt hỏi” để tránh tạo cảm giác là hai lượt khác nhau.
- Chụp lại từ chính giao diện đang chạy nếu cần tăng độ phân giải; không tái tạo hoặc sửa nội dung câu hỏi, câu trả lời, nguồn hay số liệu.

## Ảnh chụp quản trị

| Asset | Kích thước | Nội dung | Đánh giá | Xử lý |
|---|---:|---|---|---|
| `docs/images/quan-tri-sua-muc.png` | 1920 × 1290 | Biểu mẫu sửa thủ tục với từng phát biểu, nguồn và tọa độ | Chứng minh khả năng biên soạn nhưng rất dày; tên mục và số đếm nhỏ | **Không dùng** trong phương án chính; có thể dùng ở phiên bản poster nhấn mạnh quản trị dữ liệu |
| `docs/images/quan-tri-tu-choi.png` | 1920 × 1290 | Biểu mẫu báo lỗi khi một nội dung chưa chọn nguồn | Thông điệp rõ nhất trong nhóm quản trị; dải lỗi có thể cắt độc lập | **Tùy chọn**: cắt dải lỗi + một dòng biểu mẫu nếu thay cho ô nhấn SHACL; không dùng đồng thời với cả ba ảnh chụp hỏi đáp |

Nếu chọn ảnh chụp quản trị, chú thích phải nói đúng: “Biểu mẫu kiểm yêu cầu khai báo nguồn trước khi lưu; toàn đồ thị tiếp tục được kiểm cấu trúc bằng SHACL.” Không viết “SHACL phát hiện thiếu nguồn” vì yêu cầu nguồn là quy tắc riêng của dự án trước bước kiểm SHACL.

## Văn bản nguồn và tài sản khác

| Nhóm | Vị trí | Nội dung | Quyết định |
|---|---|---|---|
| PDF | `references/DongHocPhi_VCB_2021.pdf` | Hướng dẫn đóng học phí qua VNPAY–Vietcombank | **Không dùng trực tiếp.** Trang thu nhỏ không đọc được; chỉ thể hiện bằng biểu tượng văn bản trong hình trung tâm |
| PDF | `references/Qd1052.pdf` | Quy chế đào tạo trình độ đại học | **Không dùng trực tiếp**; là bằng chứng nội bộ |
| PDF | `references/Qd1965.pdf` | Sửa đổi, bổ sung phụ lục quy chế đào tạo | **Không dùng trực tiếp**; là bằng chứng nội bộ |
| PDF | `references/Qd317.pdf` | Mức học bổng khuyến khích học tập năm học 2024–2025 | **Không dùng trực tiếp**; là bằng chứng nội bộ |
| PDF | `references/Qd500.pdf` | Quy định soạn thảo, thẩm định và ban hành văn bản quản lý nội bộ | **Không dùng trực tiếp**; là bằng chứng nội bộ |
| PDF | `references/Qd626.pdf` | Quy chế tuyển sinh đại học | **Không dùng trực tiếp**; là bằng chứng nội bộ |
| PDF | `references/Qd729.pdf` | Mức học phí học kỳ I năm học 2025–2026 | **Không dùng trực tiếp**; là bằng chứng nội bộ |
| PDF | `references/Qd753.pdf` | Quy chế đào tạo trình độ đại học | **Không dùng trực tiếp**; là bằng chứng nội bộ |
| HTML | `references/bieumau_url.html` | Mảnh trang lưu danh sách và đường dẫn biểu mẫu học vụ | **Không dùng trực tiếp**; dùng để đối chiếu liên kết biểu mẫu |
| Bản chép Markdown/TXT | `references/*.md`, `references/*.txt` | Nội dung đối chiếu và báo cáo thu thập | **Bằng chứng nội bộ, không phải asset poster** |
| Giao diện web | `webui/index.html`, `webui/style.css`, `webui/script.js` | Giao diện hỏi đáp và trạng thái vận hành | Dùng để xác minh ảnh chụp; **không chỉnh giao diện** chỉ để làm poster |
| Giao diện quản trị | `webui/admin.html`, `webui/admin.css`, `webui/admin.js` | Giao diện biên soạn đồ thị tri thức | Chỉ dùng để xác minh ảnh chụp quản trị |
| Biểu tượng trang | `webui/favicon.ico` | Biểu tượng nhỏ của ứng dụng | **Không dùng như logo đề tài hoặc logo trường** |
| Mermaid mới | `docs/poster-design/poster-diagrams/hero-workflow.mmd` | Nguồn sơ đồ khái niệm cho quy trình hỏi đáp và nhánh xây dựng tri thức | **Dùng làm nguồn để dựng lại** bằng phần tử véc-tơ trên Canva; không coi bản render tự động là poster cuối |

## Tài sản chưa có trong kho mã nguồn

Các mục sau cần người dùng cung cấp hoặc xác nhận trước khi dựng Canva:

- logo chính thức của Trường Đại học Nha Trang ở SVG/PDF/PNG nền trong;
- logo khoa/đơn vị tài trợ nếu hội thảo yêu cầu;
- họ tên tác giả, giảng viên hướng dẫn, đơn vị và email/liên hệ;
- quy định nhận diện thương hiệu hoặc mẫu bắt buộc của hội thảo;
- URL cuối cho QR;
- tệp phông chữ/nhận diện nếu đơn vị yêu cầu phông riêng.

Không có sẵn:

- biểu đồ kết quả;
- biểu đồ thời gian phản hồi;
- ảnh chụp kết quả truy xuất;
- Mermaid source cho các sơ đồ kỹ thuật hiện có; tệp mới chỉ mô tả hình trung tâm ở mức khái niệm;
- QR code;
- ảnh chân dung/ảnh bối cảnh.

Các ô kết quả nên được dựng mới trực tiếp trong Canva từ bốn cụm số liệu đã khóa. Mermaid của hình trung tâm nằm trong `docs/poster-design/poster-diagrams/`; đó là nguồn khái niệm, không phải sản phẩm đồ họa poster cuối.

## Bản đồ sử dụng cuối

| Phân loại | Tài sản |
|---|---|
| Dùng nguyên | Không có tài sản nào nên đặt nguyên, không cắt, vào phương án chính |
| Cắt | `giao-dien-dang-tra-cuu.png`; `giao-dien-tra-loi.png` |
| Chỉnh nhẹ | Hai vùng cắt ảnh chụp: viền, bo góc, chú thích bên ngoài; không đổi nội dung |
| Thiết kế lại | `tong-quan`; ý niệm truy nguyên từ `tui-trich-dan`; các ô số liệu |
| Tùy chọn | `giao-dien-tu-choi.png`; banner của `quan-tri-tu-choi.png` |
| Không dùng trên poster chính | `hinh-dang-du-lieu`; `tu-ontology-den-chi-muc`; `thuat-toan-tim-kiem`; `ban-do-loai`; `quan-tri-sua-muc`; PDF nguồn; favicon |
