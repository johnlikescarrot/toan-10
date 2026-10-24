# Ghi chú biên soạn và kiểm chứng

Ngày biên soạn: **24/10/2026**.

## 1. Kết luận về nguồn đầu vào

- Tệp Word ghi Trường THPT Hà Huy Tập, Tổ Toán–Tin; giữa học kì I năm học 2026–2027, Toán 10, 90 phút.
- Nội dung gồm mục tiêu, hình thức, ma trận, mô tả tự luận và đặc tả. **Không có đề thi hoặc đáp án gốc**.
- Các đoạn “Câu 1”, “Câu 2…” là vị trí câu trong đặc tả; không đủ dữ kiện để khôi phục câu hỏi thật.
- Tệp có bốn ảnh WMF và công thức OMML. Trình trích xuất nối văn bản OMML, không OCR WMF, không giữ bố cục công thức hoặc toàn bộ cấu trúc ô gộp. Vì vậy PDF diễn giải độc lập các ký hiệu theo kiến thức chuẩn, không coi bản trích là bản sao trình bày của Word.
- Giữ nguyên tệp gốc; SHA-256 được ghi trong bản trích xuất.

## 2. Quyết định xử lý ma trận

1. Ưu tiên cấu trúc phần hình thức: 12 lựa chọn (3 điểm), 2 đúng–sai (2 điểm), 4 trả lời ngắn (2 điểm), 3 tự luận (3 điểm).
2. Đúng–sai: số ý trả lời đúng trong một câu lần lượt 0/1/2/3/4 cho 0/0,10/0,25/0,50/1,00 điểm. Không gán 0,25 điểm cố định mỗi ý.
3. “24” trắc nghiệm hiểu là 12 lựa chọn + 8 ý đúng–sai + 4 trả lời ngắn. Đề có 21 câu lớn, bảng đối chiếu có 27 vị trí nếu tách 8 ý đúng–sai.
4. Đặc tả hệ thức lượng có ô số lượng nhận biết không khớp các câu được liệt kê. Theo bảng ma trận chính, dùng câu I.9 nhận biết và I.10 thông hiểu.
5. Tự luận câu 2 mô tả MĐ2, nhưng bảng ma trận/đặc tả có chỗ vận dụng. Giữ bài thực tiễn hệ thức lượng đơn giản, ghi chú khác biệt, không tự khẳng định nguồn thống nhất.
6. Vectơ chỉ đến khái niệm mở đầu, không thêm phép cộng, nhân, tọa độ, tích vô hướng vào đề minh họa.
7. Các mức độ được đối chiếu theo loại nhiệm vụ. Không khẳng định độ khó thực nghiệm hoặc khẳng định số điểm tuyến tính cho từng nhánh nội dung đúng–sai.
8. Đề minh họa tự biên soạn, có nhãn rõ ở bìa, trang đề và chân trang. Một số dạng và cấu trúc lặp lại để ôn tập, nhưng các câu số liệu tổng hợp III.3, III.4, IV.3 dùng dữ liệu khác các ví dụ/bài luyện đã giải.

## 3. Nhật kí nghiên cứu

Tra cứu web ngày 24/10/2026; không nhập câu hỏi có sẵn từ các nguồn tham khảo vào đề minh họa.

| Nguồn | URL | Sử dụng / giới hạn |
|---|---|---|
| HEID — giới thiệu SGK | https://heid.vn/product/sgk-toan-lop-10-tap-1-ket-noi-tri-thuc/ | Xác nhận tiêu đề, NXB GDVN, nhóm tác giả, năm 2022. Phần thông tin phụ của trang có trường lớp/bộ sách bị lẫn, không sử dụng. |
| TOANMATH — mục lục SGK | https://toanmath.com/2022/01/sach-giao-khoa-toan-10-tap-1-ket-noi-tri-thuc-voi-cuoc-song.html | Đối chiếu Bài 1–7, thứ tự các chương. Không dùng lời giới thiệu về chính sách toàn quốc làm căn cứ. |
| Loigiaihay — mục 1 Bài 1 | https://loigiaihay.com/giai-muc-1-trang-6-7-sgk-toan-10-tap-1-ket-noi-tri-thuc-a105281.html | Kết quả tra cứu giải thích mệnh đề, câu hỏi và tính đúng–sai. Dùng để đối chiếu định nghĩa, không chép ví dụ. |
| VietJack — Bài 6 | https://vietjack.com/toan-10-kn/ly-thuyet-bai-6-he-thuc-luong-trong-tam-giac.jsp | Kết quả tra cứu có định lí sin/côsin, diện tích. Bản văn bản bị mất một số căn/phân số; khôi phục theo công thức chuẩn và kiểm tra đại số, không sao chép lỗi hiển thị. |
| VietJack — Bài 7 | https://vietjack.com/toan-10-kn/ly-thuyet-bai-7-cac-khai-niem-mo-dau.jsp | Đã đọc phần định nghĩa, vectơ bằng nhau và quy ước vectơ-không cùng phương/cùng hướng với mọi vectơ. |

Nguồn chính để xác định cấu trúc kiểm tra vẫn là DOCX người dùng cung cấp. Các trang bài giải là nguồn đối chiếu thứ cấp, không được gọi là quy định chính thức của nhà trường/Bộ.

## 4. Kiểm chứng thực hiện

- `scripts/check_math.py`: 10 nhóm kiểm thử bao gồm cấu trúc đủ 12/2/4/3, đủ 8 ý đúng–sai, đủ 28 bài có lời giải; phép toán tập hợp; giá trị lượng giác; diện tích và khoảng cách; tìm đỉnh miền nghiệm bằng giao từng cặp đường và lọc toàn hệ; so sánh tối ưu liên tục với vét cạn nguyên; thang điểm đúng–sai.
- Đề minh họa có đáp án nhanh: I = C B A D C B A D C A B D; II.1 = Đ S Đ Đ; II.2 = Đ Đ S S; III = 31, 10, 11, 48. IV.2 = 66,9 m. IV.3 = 4 sản phẩm I, 4 sản phẩm II, lãi 3,6 triệu đồng.
- Bài tự luận có gợi ý phân điểm 1 điểm/câu, ghi rõ là hướng dẫn tự chấm, không phải đáp án chính thức.
- `scripts/check_pdf.py`: kiểm tra số trang, văn bản chọn được, ký tự lỗi cơ bản, font nhúng, liên kết và chữ vượt mép giấy. Không tự động phát hiện được mọi lỗi toán, mọi chồng lấn hay cắt chữ trong SVG.
- Rà soát trực quan các trang đại diện: bìa, mục lục, bất phương trình, bảng công thức tam giác, hình minh họa, đề thi, lời giải và bảng đối chiếu. Sửa một lỗi căn thức do cú pháp Typst và một nhãn SVG vượt khung trong quá trình rà soát.
- Các hình SVG do script tự vẽ, có nội dung đại số đi kèm; không phụ thuộc hình ảnh có bản quyền từ web.

## 5. Giới hạn còn lại

Không thể đáp ứng theo nghĩa đen “tất cả câu hỏi và đáp án của đề thi thật 2026–2027” khi không có đề gốc. Sản phẩm cung cấp đầy đủ mọi vị trí được mô tả trong ma trận và lời giải cho **toàn bộ câu hỏi tự biên soạn**. Không đánh tráo hai phạm vi này.
