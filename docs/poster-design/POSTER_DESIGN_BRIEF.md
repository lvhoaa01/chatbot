# Đặc tả thiết kế poster 80 × 130 cm

## Định hướng chung

Poster cần tạo cảm giác **học thuật, có căn cứ, hiện đại và dễ đọc khi in**. Điểm thu hút không phải hiệu ứng “AI” mà là sự phân vai rõ: LLM hiểu/diễn đạt, BM25 truy xuất và đồ thị tri thức cung cấp dữ kiện cùng cơ chế truy nguyên nguồn.

Không dùng nền tối toàn trang, chuyển màu mạnh, neon, khung thiết bị, đổ bóng dày hoặc mạng nút trang trí không mang nghĩa.

## Ba phong cách thị giác

### Phong cách A — Học thuật sáng với điểm nhấn đồ thị — khuyên dùng

**Cảm giác:** tin cậy, sạch, có cấu trúc; hiện đại vừa đủ để nói về AI nhưng vẫn giống một poster nghiên cứu.

**Bảng màu:**

| Vai trò | HEX | Cách dùng |
|---|---|---|
| Nền giấy | `#F7F9FC` | nền toàn trang |
| Bề mặt | `#FFFFFF` | ô nội dung, vùng ảnh chụp |
| Chữ chính/xanh đậm | `#17324D` | tiêu đề, số lớn, đường chính |
| Chữ thân | `#243447` | thân bài |
| Đồ thị/xanh ngọc | `#0F766E` | nút đồ thị tri thức, nhấn truy nguyên |
| Xanh ngọc nhạt | `#DDF4F1` | nền nút/ô đồ thị tri thức |
| LLM/xanh lam | `#2457A6` | nút LLM, liên kết và từ khóa |
| Xanh lam nhạt | `#EAF2FF` | nền nút câu hỏi/LLM |
| Nguồn/hổ phách | `#C47A12` | viền, biểu tượng và mảng nhấn lớn về nguồn/phạm vi |
| Chữ hổ phách đậm | `#8A5200` | tiêu đề và chữ nhỏ trên nền sáng |
| Hổ phách nhạt | `#FFF4D6` | nền ô nhấn nguồn/giới hạn |
| Thành công | `#16803D` | nhánh “có căn cứ”, dùng ít |
| Viền trung tính | `#CBD5E1` | đường phân vùng nhẹ |

Tỷ lệ màu: khoảng 70% nền/trắng, 20% xanh đậm–xanh ngọc, tối đa 10% xanh lam/hổ phách/xanh lá. Không tô cả bốn ô số liệu bằng bốn màu bão hòa.

**Phông chữ có trên Canva:**

- Tiêu đề: **Montserrat ExtraBold/Bold**.
- Thân bài: **Open Sans Regular/Semibold**.
- Số liệu: Montserrat Bold, dùng chữ số có độ rộng bằng nhau nếu phông hỗ trợ.
- Phông dự phòng khi lỗi dấu: **Noto Sans** cho toàn poster.

**Biểu tượng:** dạng nét bo nhẹ, nét đều 1,5–2 pt ở kích thước in; chọn một bộ duy nhất. Các hình cần có: hội thoại, kính lúp, ba nút nối nhau, văn bản, dấu trích dẫn/liên kết và bảng kiểm cấu trúc. Biểu tượng bảng kiểm chỉ nói về dữ liệu trước khi ghi, không đại diện cho việc xác minh câu trả lời.

**Ô nội dung:** nền trắng, viền `#CBD5E1` **0,8 pt**, bo góc **0,4 cm**, không đổ bóng hoặc chỉ đổ bóng rất nhẹ với độ đục 5%.

**Màu nhấn:** xanh ngọc chỉ ra nơi chứa dữ kiện; xanh lam cho hành động của LLM; hổ phách luôn mang nghĩa nguồn/phạm vi cần chú ý. Không dùng `#C47A12` cho chữ nhỏ; dùng `#8A5200` thay thế.

**Sơ đồ:** đường xanh đậm/xám, mũi tên rõ; nút đồ thị lớn hơn nút khác khoảng 15–20%; nhánh nguồn màu hổ phách đi vào nút đồ thị.

**Số liệu:** số xanh đậm rất lớn; nhãn một–hai dòng; phạm vi bằng chữ xám ngay dưới. Ô `55/58 | 52/58` chia thành hai nửa có nhãn riêng, không dùng mũi tên hay biểu tượng huy chương.

**Mức phù hợp:** **5/5**.

---

### Phong cách B — Đồ thị dữ liệu hiện đại

**Cảm giác:** công nghệ, có nhịp và giàu kết nối; phù hợp nếu muốn đồ thị tri thức trở thành ngôn ngữ hình ảnh rõ hơn.

**Bảng màu:**

| Vai trò | HEX |
|---|---|
| Nền | `#F8FAFC` |
| Chữ | `#111827` |
| Chàm | `#4338CA` |
| Xanh ngọc | `#0F766E` |
| Lục lam | `#087F8C` |
| Hổ phách | `#D97706` |
| Nền chàm nhạt | `#EEF2FF` |
| Nền xanh ngọc nhạt | `#ECFDF5` |
| Viền | `#94A3B8` |

**Phông chữ có trên Canva:**

- Tiêu đề: **Montserrat ExtraBold**.
- Thân bài: **Lato Regular/Medium**.

**Biểu tượng:** hình học tối giản, góc tròn; nút tròn + đường nối làm họa tiết lặp lại, nhưng mỗi nút trang trí phải ăn theo lưới, không phủ nền ngẫu nhiên.

**Ô nội dung:** bo góc 0,55–0,7 cm, nền pha màu rất nhạt, viền không quá 0,6 pt; không dùng hiệu ứng kính mờ.

**Màu nhấn:** chàm cho LLM, xanh ngọc cho đồ thị tri thức, lục lam cho truy xuất, hổ phách cho nguồn/giới hạn.

**Sơ đồ:** nút–cạnh rõ, có số bước; đường nối dùng góc 90° hoặc cong nhẹ đồng nhất.

**Số liệu:** số lớn đi cùng một thanh tiến độ mảnh có điểm kết thúc; không dùng biểu đồ vòng hoặc đồng hồ vì dễ làm người xem hiểu là độ chính xác phổ quát.

**Mức phù hợp:** **4,5/5**. Hiện đại hơn phong cách A nhưng dễ trượt sang đồ họa thông tin công nghệ nếu thêm quá nhiều họa tiết nút.

---

### Phong cách C — Biên tập học thuật trang trọng

**Cảm giác:** tạp chí nghiên cứu, chững chạc, ít “sản phẩm”; phù hợp bối cảnh hội đồng chính thức.

**Bảng màu:**

| Vai trò | HEX |
|---|---|
| Nền ấm | `#FBFAF7` |
| Xanh lam đậm | `#183153` |
| Đỏ rượu điểm nhấn | `#8A2D3B` |
| Vàng đồng | `#B68B2C` |
| Xanh xám | `#567568` |
| Chữ thân | `#292D32` |
| Viền ấm | `#D8D3C8` |

Đây là bảng màu đề xuất trung tính, **không được coi là màu thương hiệu NTU**. Nếu hội thảo cung cấp hướng dẫn nhận diện, thay đỏ/vàng bằng màu chính thức sau khi kiểm độ tương phản.

**Phông chữ có trên Canva:**

- Tiêu đề: **Merriweather Bold**.
- Thân bài: **Lato Regular/Semibold**.

**Biểu tượng:** dạng nét thẳng, ít bo; ưu tiên ký hiệu văn bản, sơ đồ và trích dẫn hơn biểu tượng AI.

**Ô nội dung:** góc vuông hoặc bo góc 0,15 cm, dùng đường phân cách mảnh; không đổ bóng.

**Màu nhấn:** đỏ rượu chỉ dùng cho câu chốt/số liệu chính; vàng đồng cho nguồn; xanh đậm giữ vai trò cấu trúc.

**Sơ đồ:** gần phong cách hình minh họa biên tập, nhãn trái, đường mảnh, chú thích đánh số.

**Số liệu:** số lớn bằng Merriweather, phần giải thích Lato; dùng đường kẻ trên/dưới thay ô kín.

**Mức phù hợp:** **4/5**. Học thuật mạnh nhưng kém trực quan hơn với chủ đề hệ thống AI và khó xử lý tên đề tài rất dài.

## Phong cách được chọn

Chọn **Phong cách A — Học thuật sáng với điểm nhấn đồ thị**. Nó hỗ trợ tốt nhất phương án “Dòng chảy có căn cứ”, giữ độ tin cậy khi in và cho phép phân biệt vai trò bằng màu mà không biến poster thành giao diện sản phẩm.

## Hệ phân cấp thị giác

| Cấp | Thành phần | Cỡ khởi điểm ở 80 × 130 cm | Kiểu |
|---|---|---:|---|
| 1 | Tên đề tài | 58–68 pt | Montserrat ExtraBold, xanh đậm, giãn dòng 1,05–1,12 |
| 1 | Câu chốt | 40–46 pt | Montserrat Bold, xanh ngọc/xanh đậm |
| 1 | Số liệu chính | 56–72 pt | Montserrat Bold, xanh đậm |
| 2 | Tiêu đề hình trung tâm/khối | 31–36 pt | Montserrat Bold, xanh đậm |
| 2 | Nhãn bước trong hình | 25–29 pt | Open Sans Semibold |
| 3 | Thân bài | 25–29 pt | Open Sans Regular, giãn dòng 1,2–1,3 |
| 3 | Nhãn số liệu | 23–26 pt | Open Sans Semibold |
| 4 | Chú thích/phạm vi | 20–23 pt | Open Sans Regular |
| 4 | Tài liệu/URL | 18–20 pt | Open Sans Regular |

Quy tắc:

- Chỉ tối đa ba độ đậm chính: Regular, Semibold, Bold/ExtraBold.
- Thân bài căn trái; chỉ tên đề tài, câu chốt hoặc số liệu được căn giữa khi cần.
- Không dùng toàn chữ hoa cho câu chốt/tiêu đề khối. Tên đề tài chính thức có thể giữ chữ hoa theo hồ sơ, nhưng phải ngắt 3–4 dòng và tăng giãn dòng đủ để dấu tiếng Việt không va nhau.
- Không gạch chân; liên kết chỉ cần màu + QR/URL rõ.
- Một dòng thân bài lý tưởng 45–65 ký tự; khối không quá 6 dòng liên tục.

## Lưới và kích thước

### Trang thiết kế

- Kích thước: **80 × 130 cm**, dọc.
- Lề an toàn nội dung: **3,2 cm** bốn cạnh.
- Vùng làm việc: **73,6 × 123,6 cm**.
- Vùng tràn lề: theo yêu cầu nhà in; chỉ nền/mảng màu được tràn, không đưa chữ/logo/QR ra ngoài lề an toàn.

### Lưới ngang

- **12 cột**, khoảng cách cột **0,7 cm**.
- Chiều rộng mỗi cột xấp xỉ **5,49 cm**.
- Vùng tiêu đề, câu chốt, hình trung tâm: trải đủ 12 cột.
- Bốn ô số liệu: mỗi ô trải 3 cột.
- Khối ảnh chụp/đóng góp: 7 cột / 5 cột.
- Chân trang dùng hai tầng: tầng trên là kết luận 8 cột + QR/liên hệ 4 cột; tầng dưới là một dòng tài liệu nền tảng trải 12 cột.

Nếu Canva không có công cụ tạo lưới tự động, dùng đường căn thủ công; không căn bằng mắt.

### Nhịp dọc cho phương án khuyên dùng

| Vùng | Tọa độ dọc gần đúng | Chiều cao |
|---|---:|---:|
| Lề an toàn trên | 0–3,2 cm | 3,2 cm |
| Tiêu đề/nhận diện | 3,2–21,2 cm | 18 cm |
| Khoảng cách | 21,2–22,4 cm | 1,2 cm |
| Câu chốt + bài toán | 22,4–32,4 cm | 10 cm |
| Khoảng cách | 32,4–33,6 cm | 1,2 cm |
| Hình trung tâm | 33,6–67,6 cm | 34 cm |
| Khoảng cách | 67,6–68,8 cm | 1,2 cm |
| Dải kết quả | 68,8–88,8 cm | 20 cm |
| Khoảng cách | 88,8–90,0 cm | 1,2 cm |
| Ảnh chụp + đóng góp/giới hạn | 90,0–114,0 cm | 24 cm |
| Khoảng cách | 114,0–115,2 cm | 1,2 cm |
| Kết luận + tài liệu + QR | 115,2–126,8 cm | 11,6 cm |
| Lề an toàn dưới | 126,8–130 cm | 3,2 cm |

Các tọa độ là điểm xuất phát. Có thể chuyển tối đa 2 cm giữa hai vùng kề nhau, nhưng không làm hình trung tâm thấp hơn 30 cm hoặc dải kết quả thấp hơn 18 cm.

### Khoảng cách và khoảng đệm

- Đơn vị nhịp cơ sở: **0,6 cm**.
- Khoảng giữa hai khối lớn: 1,2–1,8 cm.
- Khoảng đệm ô: 1,0–1,3 cm.
- Khoảng tiêu đề–thân bài: 0,6–0,9 cm.
- Khoảng giữa các ý: 0,35–0,55 cm.
- Khoảng số lớn–nhãn: 0,3–0,5 cm.

## Vùng tiêu đề và nhận diện

- Logo trường ở góc trên trái hoặc phải, tối đa cao 5–6 cm; không tự dựng lại logo.
- Nhãn `NGHIÊN CỨU KHOA HỌC SINH VIÊN · SV2025-13-61` nhỏ nhưng tương phản.
- Tên đề tài chiếm khoảng 11–13 cm cao, ngắt theo cụm nghĩa.
- Tác giả/đơn vị một đến hai dòng ở đáy vùng tiêu đề.
- Không thêm ảnh nền, biểu tượng AI hoặc họa tiết sau tên đề tài.

## Hình trung tâm

Nguồn nội dung: `poster-diagrams/hero-workflow.mmd`. Mermaid là bản đồ ngữ nghĩa; **không chụp bản kết xuất mặc định rồi đặt nguyên lên Canva**.

### Cách dựng lại trên Canva

- Giữ 5 chặng xử lý và một đầu ra trên nhánh cần tra cứu: câu hỏi → LLM hiểu ý/quyết định → BM25 chọn mục → đồ thị đọc dữ kiện → LLM diễn đạt → trả lời hoặc nêu giới hạn.
- Xếp luồng theo lưới 3 × 3 để vừa tỷ lệ hình: bước 1–3 đọc trái → phải ở hàng trên; bước 4 hạ xuống cột phải; bước 5–6 tiếp tục ở hàng dưới theo hướng phải → trái. Hai nhánh giới hạn nằm ở hàng giữa; nguồn đi lên bước 4 từ góc phải dưới.
- Ghi rõ “khi cần tra cứu” trên đường vào BM25; vẽ nhánh ngoài phạm vi bằng nhãn “được hướng dẫn từ chối”, không như một bộ phân loại tất định.
- Có thể dùng một đường nét đứt cho trường hợp không tìm thấy và thử lại bằng cách diễn đạt khác; không biến nó thành vòng lặp nổi bật.
- Đặt nút đồ thị làm trọng tâm thị giác, lớn hơn các nút khác 15–20% và tô xanh ngọc nhạt.
- Đưa “Nguồn học vụ chính thức” vào nút đồ thị bằng một nhánh màu hổ phách từ góc phải dưới, nhãn “biên soạn · kiểm yêu cầu khai báo nguồn · kiểm cấu trúc bằng SHACL”.
- Sau LLM diễn đạt, tách hai kết quả bằng hai hình/nhãn: “trả lời từ dữ kiện đã tra; có thể nêu nguồn đã khai báo” và “nêu giới hạn dữ liệu”; ghi rõ đây là hành vi mô hình được hướng dẫn.
- Dùng số bước 1–6 để trợ giúp luồng; nhánh nguồn và hai nhánh giới hạn không đánh số vì không thuộc đường đi chính đầy đủ dữ kiện.
- Đường nối 1,4–1,8 pt, đầu mũi tên rõ; tránh đường chéo cắt nhau.
- Nhãn nút tối thiểu 24 pt; không vượt hai dòng/nút.

### Ngôn ngữ màu/hình

- Câu hỏi: bong bóng hội thoại nền xanh lam nhạt.
- LLM: hình chữ nhật bo, viền xanh lam.
- BM25: hình kính lúp hoặc danh sách xếp hạng, nền xám sáng.
- Đồ thị: hình trụ/khung nút, viền xanh ngọc dày hơn.
- Nguồn: biểu tượng văn bản, màu hổ phách.
- Trả lời: bong bóng xanh lá nhạt.
- Giới hạn: bong bóng hổ phách nhạt, không dùng đỏ lỗi.

## Hệ ô nội dung và ô nhấn

### Ô số liệu

- Bốn ô cùng chiều cao, cùng độ rộng ba cột và đường chân chữ.
- Số lớn ở trên; nhãn dưới; phạm vi nhỏ nhất nhưng không dưới 20 pt.
- Ô `55/58 | 52/58` chia đôi bên trong; dùng cỡ số 44–52 pt nếu cần, không thay đổi độ rộng ô.
- Đặt nhãn `Truy xuất riêng · 49 câu được chấm · từ khóa cố định` trên ô 1; đặt nhãn `Toàn quy trình · 85 tình huống · một lượt` trải trên các ô 2–4.
- Không dùng dấu phần trăm đơn độc. Phân số luôn hiển thị; phần trăm chỉ là phụ.
- Một đường nhấn 0,18–0,25 cm ở mép trên: xanh ngọc cho truy xuất, xanh lam cho kết quả toàn quy trình, hổ phách cho từ chối, xám/xanh đậm cho thời gian.

### Ô nhấn về truy nguyên

- Một dải ba bước: `Dữ kiện → Khoản/mục/trang → Nguồn học vụ chính thức`.
- Dùng biểu tượng + nhãn, không dùng IRI hoặc mã TriG.
- Tô nền hổ phách rất nhạt; đây là thông tin căn cứ, không phải cảnh báo lỗi.

### Ô nhấn về giới hạn

- Không dùng hộp đỏ.
- Tiêu đề hổ phách đậm, nền `#FFF4D6`, tối đa ba ý.
- Đặt gần kết luận/số liệu để người xem đọc kết quả và phạm vi cùng nhau.

## Trình bày số liệu và biểu đồ

Poster không cần bảng điều khiển biểu đồ. Bốn ô số liệu là đủ.

Nếu muốn thêm tín hiệu thị giác cho `48/49`, dùng một thanh 49 ô rất nhỏ với 48 ô xanh ngọc và 1 ô viền, nhưng chỉ khi mỗi ô còn nhìn được và có chú giải. Không dùng:

- biểu đồ vòng/đồng hồ;
- biểu đồ 3D;
- trục không có đơn vị;
- phần trăm làm tròn mà bỏ mẫu số;
- màu xanh lá để ngầm nói “đã hoàn hảo”.

## Xử lý ảnh chụp giao diện

- Dùng tối đa hai ảnh đã chọn trong `POSTER_ASSET_AUDIT.md`, với điều kiện chúng đạt độ nét ở kích thước in.
- Ảnh hiện có chỉ là ứng viên nội dung. Ưu tiên chụp lại đúng giao diện thật ở mật độ 2×/3×; nếu bản in thử không đủ nét, bỏ ảnh thay vì phóng hoặc nội suy.
- Nếu một vùng cắt trải gần hết cột ảnh rộng khoảng 42,6 cm, đặt ngưỡng tối thiểu khoảng **2.518 px ở 150 ppi**, mục tiêu **3.357 px ở 200 ppi**; 300 ppi cần khoảng 5.035 px. Ảnh gốc hiện rộng 1.920 px chỉ đạt khoảng 114 ppi trước khi cắt, nên phải chụp lại ở độ phân giải cao hơn hoặc dùng vùng in hẹp hơn.
- Cắt sát vùng hành vi; không đặt toàn bộ khung trình duyệt.
- Đặt mỗi vùng cắt trên ô trắng với khoảng đệm 0,5–0,7 cm.
- Viền `#CBD5E1`, bo góc 0,35–0,45 cm, không dùng mô hình thiết bị trang trí.
- Chú thích đặt ngoài ảnh bằng Open Sans 20–23 pt.
- Có thể dùng một đường nhấn xanh lam mảnh để trỏ từ câu hỏi đời thường sang các từ khóa.
- Với ảnh trả lời, ghi “Hai vùng phóng to từ cùng một lượt hỏi”; không ghép theo cách khiến người xem tưởng là hai lượt khác nhau.

## QR và liên hệ

- QR tối thiểu **4,5 × 4,5 cm** ở bản in thật.
- Giữ vùng trắng ít nhất bốn ô mã quanh QR; không đặt QR trên nền pha màu hoặc ảnh.
- Chú thích `Quét để thử hệ thống` 20–22 pt, URL chữ 18–20 pt.
- Đặt góc phải dưới nhưng còn cách mép vùng an toàn ít nhất 0,6 cm.
- Không đặt logo vào giữa QR nếu chưa thử khả năng quét.
- Quét thử trong tệp PDF, bản in thử và dưới ánh sáng hội trường bằng ít nhất hai thiết bị.

## Tài liệu tham khảo

- Một dòng 18–20 pt ở chân poster, tối đa ba tài liệu nền tảng.
- Dùng dấu chấm giữa để tiết kiệm chiều cao.
- Không in URL dài của W3C; QR/kho mã nguồn giữ danh mục đầy đủ.

## Khả năng tiếp cận và in

- Kiểm độ tương phản chữ/nền tối thiểu theo mức thông dụng 4,5:1 cho chữ thân.
- `#C47A12` chỉ dùng cho viền, biểu tượng hoặc chữ rất lớn; chữ chú thích trên nền trắng/`#FFF4D6` dùng `#8A5200` hoặc xanh đậm.
- Không dựa chỉ vào màu: thêm biểu tượng, nhãn và khác biệt hình dạng.
- In thử thang xám: luồng vẫn phải hiểu được khi mất màu.
- Tránh chữ trắng trên xanh ngọc/xanh lam nhạt; chữ xanh đậm trên nền nhạt an toàn hơn.
- Sơ đồ dùng SVG/véc-tơ; ảnh chụp giữ tỷ lệ, không nội suy quá lớn.
- Kiểm lỗi dấu tiếng Việt sau khi đổi phông và sau khi xuất PDF.

## Quy trình dựng trên Canva

1. Tạo thiết kế tùy chỉnh **80 × 130 cm**, không chọn A-series.
2. Đặt nền `#F7F9FC`; bật thước, đường căn, lề và vùng tràn lề in.
3. Tạo đường căn an toàn 3,2 cm; tạo lưới 12 cột, khoảng cách cột 0,7 cm.
4. Tạo trước 8 kiểu chữ: nhãn, tên đề tài, câu chốt, tiêu đề khối, thân bài, số lớn, nhãn số liệu, chú thích.
5. Đặt các hình chữ nhật của sơ đồ khung theo tọa độ dọc; khóa chúng trước khi nhập nội dung.
6. Dựng hình trung tâm bằng hình cơ bản/đường nối theo Mermaid; nhóm từng nút, rồi nhóm toàn hình.
7. Dựng bốn ô số liệu và nhập mẫu số trước; thêm ghi chú phạm vi ngay sau.
8. Nhập ảnh chụp gốc, nhân bản ảnh trả lời để tạo hai vùng cắt; tuyệt đối không sửa chữ trong ảnh.
9. Thêm giới hạn, kết luận, tài liệu; cắt chữ nếu phải giảm dưới cỡ tối thiểu.
10. Tạo QR từ URL thật, thêm URL chữ, thử quét.
11. In một bản thử thu nhỏ để kiểm phân cấp và in các vùng cắt chữ ở 100% để kiểm độ nét.
12. Xuất PDF dành cho in theo yêu cầu nhà in; bật dấu xén/vùng tràn lề chỉ khi nhà in yêu cầu, kiểm lại chuyển màu CMYK và kích thước trang 80 × 130 cm.

## Những lỗi thiết kế cần chặn

- Dùng sơ đồ README nguyên trạng làm hình trung tâm.
- Dùng quá ba màu nhấn trong cùng một vùng.
- Căn giữa đoạn văn hoặc viết tiêu đề khối toàn chữ hoa.
- Hạ thân bài xuống 18–20 pt để nhét thêm nội dung.
- Đặt ghi chú giới hạn quá nhỏ đến mức không đọc được.
- Làm bốn số liệu trông như bốn cam kết không có phạm vi.
- Đặt logo, QR hoặc chữ trong vùng tràn lề/vùng nguy hiểm.
- Dùng ảnh chụp nền tối chiếm cả chiều rộng mà không cắt.
- Thêm nút/đường nối chỉ để “trông giống AI”.
