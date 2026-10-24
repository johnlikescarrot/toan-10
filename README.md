# Ôn tập Toán 10 — Giữa học kì I, năm học 2026–2027

## Tải tài liệu

**[Đề cương PDF — 28 trang](tai-lieu/De-cuong-Toan-10-Giua-HKI-2026-2027.pdf)**

Bám ma trận trong tệp **[MA TRẬN TOÁN 10 - GIỮA KÌ I.docx](MA%20TRẬN%20TOÁN%2010%20-%20GIỮA%20KÌ%20I.docx)**, ghi tên Trường THPT Hà Huy Tập, Tổ Toán–Tin. Phạm vi tương ứng **Bài 1–7, Toán 10 tập một, Kết nối tri thức với cuộc sống**.

> **Không có đề thi hoặc đáp án gốc trong tệp Word.** Các dòng “Câu…” trong bảng đặc tả mô tả yêu cầu kiến thức, không phải câu hỏi có dữ kiện. Tài liệu này cung cấp đề minh họa tự biên soạn có lời giải đầy đủ, **không nhận là đề thi chính thức 2026–2027**, không cam kết dự đoán đề thật. Muốn cung cấp toàn bộ câu hỏi/đáp án đề gốc cần có chính đề đó.

## Nội dung PDF

- Phân tích cấu trúc 90 phút, thang điểm và các điểm chưa thống nhất trong nguồn.
- Lý thuyết, công thức, quy trình giải và ví dụ mẫu: mệnh đề; tập hợp; bất phương trình và hệ bất phương trình bậc nhất hai ẩn; lượng giác và hệ thức lượng trong tam giác; khái niệm vectơ.
- **5 hình minh họa** tự vẽ: Ven, trục số, vectơ, miền nghiệm và tam giác đo đạc.
- **28 bài luyện**, tất cả có lời giải.
- **1 đề minh họa đủ 12 câu lựa chọn + 2 câu đúng–sai (8 ý) + 4 câu trả lời ngắn + 3 câu tự luận**, đáp án và lời giải cho mọi câu/ý, gợi ý chấm tự luận.
- Bảng đối chiếu **27 vị trí câu/ý** với đặc tả; hướng dẫn tự chấm đúng thang điểm phi tuyến của phần đúng–sai; lộ trình 7 buổi.
- Nguồn tham khảo có liên kết và giới hạn sử dụng, tra cứu ngày 24/10/2026.

Phân biệt cách đếm: đề có **21 câu lớn**; riêng trắc nghiệm được bảng ma trận đếm thành **24 đơn vị** (12 lựa chọn + 8 ý đúng–sai + 4 trả lời ngắn). Cộng 3 tự luận thành 27 vị trí đối chiếu. Không mở rộng sang các phép toán hay tọa độ vectơ.

## Tệp và kiểm chứng

| Đường dẫn | Mục đích |
|---|---|
| `tai-lieu/de-cuong.typ` | Nguồn biên soạn, chỉnh sửa được; công thức toán dạng văn bản |
| `tai-lieu/hinh/*.svg` | Hình minh họa dạng vectơ, không có tài nguyên web phụ thuộc |
| `kiem-chung/trich-xuat-docx.md` | Bản trích văn bản/ô bảng và SHA-256 tệp đầu vào |
| `kiem-chung/ghi-chu-bien-soan.md` | Cách xử lý ma trận, nhật kí nguồn, phạm vi kiểm tra |
| `kiem-chung/bao-cao-pdf.json` | Số trang, font nhúng, kiểm tra văn bản và giới hạn mép giấy |
| `scripts/check_math.py` | 10 nhóm kiểm thử cấu trúc, toán học, thang điểm và tối ưu |

Tệp Word ban đầu được giữ nguyên. Việc trích xuất không OCR các ảnh WMF và không khôi phục toàn bộ định dạng ô gộp; bản trích xuất là công cụ đối chiếu, không thay thế bản gốc.

## Tái tạo PDF

Yêu cầu Python 3.11+, font **DejaVu Serif / DejaVu Sans** (Debian/Ubuntu: gói `fonts-dejavu-core`). Typst qua gói Python có sẵn font toán New Computer Modern. Cài phụ thuộc từ PyPI, sau đó quá trình build không cần mạng.

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/extract_docx.py
.venv/bin/python scripts/draw_figures.py
.venv/bin/python scripts/check_math.py
.venv/bin/python scripts/build_pdf.py
.venv/bin/python scripts/check_pdf.py --render
```

`--render` là tùy chọn: tạo ảnh từng trang trong `kiem-chung/render/` để rà soát, thư mục này không đưa vào Git. Có thể bỏ tùy chọn để chỉ kiểm tra PDF. **Kiểm thử tự động không thay thế việc đọc lại lời giải và kiểm tra bố cục bằng mắt.**
