# Ghi chú nghiên cứu thiết kế poster hội thảo

## Phạm vi và ràng buộc đã giữ cố định

- Sản phẩm đích là poster nghiên cứu khổ dọc **80 × 130 cm**, dựng trên Canva.
- Poster dùng **100% tiếng Việt**, ngoại trừ các tên chuẩn cần giữ để nhận diện như RDF, TriG, SHACL, BM25 và LLM.
- Mục tiêu đọc là ba tầng: nhận ra chủ đề trong 10 giây, hiểu ý tưởng và kết quả chính trong 1 phút, hiểu bằng chứng và giới hạn trong 3 phút.
- Các tài liệu bên ngoài chỉ cung cấp nguyên tắc truyền thông và in ấn. Nội dung khoa học vẫn phải được chứng minh bằng kho mã nguồn.

## Điều học được từ các poster/tài liệu tham khảo bên ngoài

### 1. Poster là một lộ trình thị giác, không phải “bài báo treo tường”

MIT AeroAstro Communication Lab khuyên cắt tiếp nếu người xem chưa nắm được kết luận chính sau 30–60 giây; chi tiết phương pháp nên hiểu được trong khoảng hai phút.[1] MIT NSE Communication Lab cũng đặt “một thông điệp chính” và luồng trình bày làm hai tiêu chí trung tâm.[2]

Áp dụng cho đề tài:

- giữ một câu chuyện duy nhất: **câu hỏi đời thường → tra cứu đồ thị tri thức → trả lời từ dữ kiện hoặc nêu giới hạn dữ liệu**;
- không tái hiện cấu trúc chương của báo cáo;
- không dùng danh sách công nghệ làm nội dung chính;
- thiết kế để poster vẫn tự giải thích khi tác giả không đứng bên cạnh.

### 2. Hình trung tâm phải làm phần việc nặng nhất

Các hướng dẫn của MIT ưu tiên hình hơn chữ và xem một hình lớn ở trung tâm là cách hiệu quả để truyền thông điệp chính.[1][2][3] Với đề tài này, hình phù hợp nhất không phải ảnh giao diện mà là sơ đồ khái niệm cho thấy vai trò tách biệt của LLM, BM25 và đồ thị tri thức có cơ chế truy nguyên nguồn.

Áp dụng:

- hình trung tâm chiếm khoảng 24–28% diện tích toàn poster;
- dùng 5 chặng xử lý và 1 đầu ra lớn, không dùng tên lớp, hàm, khóa JSON hay gói phần mềm;
- làm nổi bật **đồ thị tri thức có truy nguyên nguồn**, không làm LLM thành “bộ não chứa quy định”;
- dùng màu và hình dạng đồng thời để phân biệt nguồn, xử lý và kết quả, tránh mã hóa chỉ bằng màu.[1]

### 3. Tiêu đề khối phải nói ra kết luận

MIT CEE Communication Lab khuyên dùng tiêu đề khối dạng mệnh đề có nghĩa thay vì nhãn chung như “Phương pháp” hay “Kết quả”; ý ngắn dưới khoảng 15 từ dễ quét hơn đoạn văn.[3]

Áp dụng:

- dùng “LLM hiểu và diễn đạt; đồ thị cung cấp dữ kiện” thay cho “Kiến trúc”;
- dùng “Đúng mục trong 3 kết quả đầu ở 48/49 câu” thay cho “Kết quả truy xuất”;
- dùng “Khi thiếu căn cứ, hệ thống được hướng dẫn nói rõ giới hạn” thay cho “Cơ chế dự phòng”.

### 4. Khoảng trắng và nhóm nội dung dẫn mắt tốt hơn viền nặng

MIT NSE khuyên nhóm nội dung bằng khoảng trắng và màu nền, tránh viền đậm quanh mọi panel vì chúng cạnh tranh với nội dung.[2] Hướng dẫn của University of Rochester cũng yêu cầu chừa nhiều khoảng trắng, căn thẳng hàng và giữ phong cách chữ nhất quán.[5]

Áp dụng:

- nền sáng, ô nội dung rất nhạt, viền mảnh;
- một khoảng trống rõ giữa hình trung tâm, dải số liệu và phần bằng chứng;
- không phủ kín trang bằng các hộp cùng trọng lượng;
- dành khoảng 15–20% diện tích cho khoảng trắng, khoảng cách cột và vùng thở bên trong.

### 5. Chữ phải được kiểm ở khoảng cách thật

MIT CEE đề xuất tiêu đề lớn hơn 44 pt và thân bài khoảng 28 pt trở lên; Rochester xem 24 pt là mức tối thiểu thường dùng khi đọc ở khoảng 1,8 m.[3][5] Đây là mốc tham khảo, không phải công thức tuyệt đối cho mọi máy in.

Mốc đề xuất cho khổ 80 × 130 cm:

| Vai trò | Cỡ khởi điểm | Ghi chú |
|---|---:|---|
| Tên đề tài chính thức | 58–68 pt | 2–4 dòng, không ép thành một dòng |
| Câu chốt | 38–46 pt | tương phản cao, tối đa 18–22 từ |
| Số liệu lớn | 52–72 pt | phân số luôn đi cùng mẫu số và phạm vi |
| Tiêu đề khối | 30–36 pt | viết như một kết luận ngắn |
| Thân bài | 25–29 pt | không xuống dưới 24 pt ở kích thước in thật |
| Chú thích hình | 20–23 pt | chỉ dùng cho nguồn/phạm vi thiết yếu |
| Chân trang/tài liệu | 18–20 pt | giới hạn ở nội dung thật sự cần giữ |

Các cỡ trên phải được thử bằng bản in thu nhỏ và kiểm lại ở 100% kích thước; không dùng “co chữ tự động” để cứu một khối quá nhiều nội dung.

### 6. Không áp dụng máy móc mẫu “better poster”

Phân tích của MIT Biological Engineering ghi nhận mẫu tối giản cực mạnh giúp thông điệp nổi bật, nhưng cũng có thể đẩy dữ liệu sang các cột quá nhỏ và làm poster giống quảng cáo hơn là lập luận nghiên cứu.[4]

Áp dụng:

- học cách làm nổi thông điệp và giảm chữ;
- không dành hơn nửa trang cho một khẩu hiệu;
- dành diện tích đủ lớn cho sơ đồ phương pháp, mẫu số của số liệu và giới hạn;
- không sao chép nguyên bố cục của bất kỳ poster tham khảo nào.

### 7. Tham khảo poster công nghệ/AI: học cách nhấn, không học giọng quảng cáo

Danh mục poster AI của Yale dành riêng một phiên cho “LLM: phát triển, ứng dụng và đánh giá”, bên cạnh các phiên theo lĩnh vực.[9] Đây không phải một mẫu bố cục, nhưng củng cố lựa chọn xem **đánh giá và phạm vi bằng chứng** là một phần của câu chuyện AI, thay vì chỉ trình diễn giao diện.

Bộ poster công nghệ của MIT CSAIL cho thấy kiểu truyền thông dùng một mệnh đề lớn, ít con số nổi bật và các vùng nội dung tách rõ; poster DynamoFL là một ví dụ của cách đặt thông điệp và các kết quả định lượng ở cấp nhìn nhanh.[10][11] Tuy nhiên, đây là poster giới thiệu công nghệ/startup, không phải chuẩn nội dung khoa học.

Áp dụng có chọn lọc:

- học cách dành ưu tiên thị giác cho một câu chốt và 3–5 số liệu;
- giữ mẫu số, phương pháp chấm và giới hạn ngay cạnh số liệu — không chuyển thành khẩu hiệu thành tích;
- không dùng ngôn ngữ “đột phá”, logo sản phẩm lớn, bảng tính năng hay lời kêu gọi thương mại;
- không sao chép bố cục của ví dụ; chỉ học nhịp **thông điệp → hình → bằng chứng**.

### 8. Canva, phông chữ và chuẩn bị in

Canva cho phép dùng kích thước tùy chỉnh và khóa tỷ lệ; nếu trình biên tập báo vượt giới hạn, Canva hướng dẫn giảm kích thước nhưng giữ nguyên tỷ lệ.[6] Canva cũng phân biệt lề, vùng an toàn, đường xén và vùng tràn lề; nền có thể tràn nhưng chữ/logo phải nằm trong vùng an toàn. Khi xuất in, Canva hướng dẫn dùng PDF dành cho in và có tùy chọn dấu xén + vùng tràn lề.[7]

Các bài hướng dẫn chính thức của Canva minh họa Montserrat, Open Sans, Lato và Merriweather trong hệ mẫu/phối chữ của nền tảng.[12][13] Vì vậy ba phong cách trong gói đặc tả chỉ dùng các họ chữ này; người dựng vẫn phải kiểm lại đúng biến thể chữ có trong tài khoản Canva trước khi khóa thiết kế.

Áp dụng cho poster này:

1. Tạo thiết kế tùy chỉnh **80 cm × 130 cm** ngay từ đầu.
2. Nếu trình biên tập cụ thể không chấp nhận kích thước này, dừng và xác nhận quy trình với nhà in trước khi dựng; đặc tả này không dùng bản nửa cỡ vì mọi cỡ chữ, lề và QR đều đã tính ở 80 × 130 cm.
3. Tạo đường căn thủ công cho lề an toàn 3,2 cm và lưới 12 cột.
4. Bật thước/đường căn, lề và vùng tràn lề in; hỏi nhà in về vùng tràn thực tế vì Canva lưu ý thông số nhà in ngoài Canva có thể khác.[7]
5. Xuất **PDF dành cho in**, kiểm chuyển màu RGB–CMYK và in thử trước khi in khổ thật.[7][8]
6. Canva khuyên ảnh điểm đạt 300 DPI ở kích thước in.[8] Vì vậy ưu tiên SVG cho sơ đồ; ảnh chụp phải cắt sát hành vi cần xem, không kéo toàn màn hình lên quá lớn.

## Quy ước poster khoa học được giữ lại

- Có tên đề tài, tác giả, đơn vị, mã đề tài và thông tin liên hệ.
- Có bài toán, cách tiếp cận, bằng chứng, kết luận và giới hạn.
- Số liệu luôn kèm mẫu số, tập câu hỏi và loại phép chấm.
- Có 2–4 tài liệu nền tảng dạng chữ nhỏ ở chân trang; QR dẫn tới bản dùng thử, còn URL phụ dẫn tới tài liệu dự án hoặc phần giải thích đầy đủ.
- Hình/ảnh chụp có chú thích nói rõ người xem cần nhận ra điều gì.

## Điều không phù hợp với dự án

- Không dùng Pinterest/Behance làm căn cứ cho nội dung khoa học.
- Không dùng phong cách neon/cyberpunk, nền tối toàn trang hay hiệu ứng phát sáng: khó kiểm màu khi in và làm giảm cảm giác học thuật.
- Không dùng sơ đồ kiến trúc hiện có nguyên trạng làm hình trung tâm: đúng về kỹ thuật nhưng có quá nhiều khối và thuật ngữ triển khai.
- Không dùng công thức BM25, cấu trúc JSON, mã nguồn hoặc bản đồ toàn bộ lớp của đồ thị tri thức trên poster chính.
- Không dùng 6–8 ảnh chụp nhỏ; chữ giao diện sẽ không còn đọc được.
- Không dùng tỷ lệ “80% hình, 10% tiêu đề, 10% chữ” như một luật cứng. Đây là lời nhắc ưu tiên hình,[2] còn poster này vẫn cần đủ chỗ cho phạm vi và giới hạn của kết quả.

## Nguồn tham khảo

1. MIT AeroAstro Communication Lab. [Research Posters](https://mitcommlab.mit.edu/aeroastro/commkit/research-posters/). Truy cập 14/09/2026.
2. MIT Nuclear Science and Engineering Communication Lab. [Poster](https://mitcommlab.mit.edu/nse/commkit/poster/). Truy cập 14/09/2026.
3. MIT Civil and Environmental Engineering Communication Lab. [Poster Design](https://mitcommlab.mit.edu/cee/commkit/poster-design/). Truy cập 14/09/2026.
4. MIT Biological Engineering Communication Lab. [Towards an “#evenbetterposter”](https://mitcommlab.mit.edu/be/2023/09/27/toward-an-evenbetterposter-improving-the-betterposter-template/), 27/09/2023.
5. Susan M. Ciurzynski, University of Rochester Medical Center. [Developing & Presenting Posters for Professional Conferences: Take-Away Tips](https://www.urmc.rochester.edu/MediaLibraries/URMCMedia/ctsi/resources/documents/Ciurzynski-s-Take-Away-Tips-for-Posters.pdf), 2016.
6. Canva Help Centre. [Resize designs and size limits](https://www.canva.com/en_gb/help/resize-variantb/). Truy cập 14/09/2026.
7. Canva Help Center. [Use margins, bleed, rulers, and crop marks](https://www.canva.com/help/margins-bleed-crop-marks/). Truy cập 14/09/2026.
8. Canva Help Centre. [Fix an issue with your Canva Print order](https://www.canva.com/en_gb/help/fix-canva-print-order/). Truy cập 14/09/2026.
9. Yale University. [Symposium Posters — AI at Yale](https://ai.yale.edu/symposium-posters). Truy cập 15/09/2026.
10. MIT CSAIL Alliances. [Startup Poster Presentations](https://cap.csail.mit.edu/startup-poster-presentations). Truy cập 15/09/2026.
11. DynamoFL. [Poster presentation PDF, MIT CSAIL Alliances](https://cap.csail.mit.edu/sites/default/files/resource-pdfs/PDF_DynamoFL.pdf). Truy cập 15/09/2026.
12. Canva. [The best Google Font combinations to try](https://www.canva.com/learn/best-google-font-combinations/). Truy cập 15/09/2026.
13. Canva. [Choosing and pairing brand fonts like a pro](https://www.canva.com/learn/best-professional-fonts-use-website/). Truy cập 15/09/2026.
