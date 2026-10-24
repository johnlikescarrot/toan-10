# Toán 10 — Đề cương giữa học kì I

## Tài liệu chính

**[Tải/đọc PDF: Đề cương ôn tập Toán 10 — Giữa học kì I, 2026–2027](de-cuong/DE-CUONG-TOAN-10-GIUA-KI-I-2026-2027.pdf)**

Đề cương bám sát `MA TRẬN TOÁN 10 - GIỮA KÌ I.docx` và chương trình *Kết nối tri thức với cuộc sống*, gồm:

- Bốn chuyên đề: mệnh đề–tập hợp; BPT/hệ BPT bậc nhất hai ẩn; hệ thức lượng trong tam giác; khái niệm vectơ.
- Lý thuyết, ví dụ từng bước, lỗi thường gặp, luyện nhanh có đáp án và bảng công thức.
- Đề ôn 90 phút: 12 câu chọn phương án, 2 câu đúng–sai (8 ý), 4 câu trả lời ngắn và 3 câu tự luận.
- Đáp án, lời giải chi tiết, thang điểm và phụ lục đối chiếu 27/27 câu/ý với ma trận.

> **Giới hạn nguồn:** DOCX được cung cấp chỉ có ma trận và bảng đặc tả, không có đề thi hoàn chỉnh hoặc đáp án chính thức. Vì vậy đề trong PDF là **đề ôn biên soạn mới bám sát từng vị trí đặc tả**, không phải nguyên văn đề thi chính thức. Xem [`PHAN-TICH-MA-TRAN.md`](PHAN-TICH-MA-TRAN.md) để biết chi tiết.

## Tái tạo PDF

Yêu cầu Python 3.10+ và font DejaVu Sans tại `/usr/share/fonts/truetype/dejavu` (script cũng dùng font toán đi kèm Typst).

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r scripts/requirements.txt
.venv/bin/python scripts/build_review.py
.venv/bin/python scripts/verify_pdf.py
```

Để tạo thêm ảnh contact sheet phục vụ rà soát trực quan:

```bash
.venv/bin/python scripts/verify_pdf.py --render
```

Build chạy hoàn toàn ngoại tuyến sau khi cài gói: bảy hình SVG được tạo từ mã nguồn, không tải hình ảnh/font/gói Typst bên ngoài. Các kết quả số quan trọng của đề cũng được kiểm tra bằng `assert` trước khi biên dịch.

## Cấu trúc thư mục

- `de-cuong/main.typ`: thiết lập tài liệu, bìa, hướng dẫn và mục lục.
- `de-cuong/01-ly-thuyet.typ`: bốn chuyên đề và công thức ôn nhanh.
- `de-cuong/02-de-on.typ`: đề ôn đủ bốn phần.
- `de-cuong/03-dap-an.typ`: đáp án, lời giải và thang điểm.
- `de-cuong/04-doi-chieu.typ`: phụ lục bao phủ, nội dung đặc tả và nguồn.
- `de-cuong/style.typ`: kiểu hiển thị dùng chung.
- `scripts/build_review.py`: tạo SVG, kiểm tra kết quả số và biên dịch PDF.
- `scripts/verify_pdf.py`: kiểm tra cấu trúc, text layer, font, liên kết và số lượng câu.
- `PHAN-TICH-MA-TRAN.md`: kết quả phân tích tệp nguồn và quyết định biên soạn.

Các SVG và ảnh kiểm tra là sản phẩm build nên được bỏ qua trong Git; PDF cuối cùng được lưu trong repository để đọc trực tiếp.
