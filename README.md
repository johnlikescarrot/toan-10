# Đề cương ôn tập Toán 10 – Giữa học kì I

## Tệp hoàn chỉnh

**[DE-CUONG-ON-TAP-TOAN-10-GIUA-KI-1-2026-2027.pdf](DE-CUONG-ON-TAP-TOAN-10-GIUA-KI-1-2026-2027.pdf)**

Tài liệu tiếng Việt bám sát ma trận Trường THPT Hà Huy Tập và chương trình Toán 10 **Kết nối tri thức với cuộc sống**, gồm:

- phân tích cấu trúc đề, lộ trình ôn 7 ngày và chiến lược làm bài 90 phút;
- lý thuyết, ví dụ từng bước và bài luyện có đáp án cho cả bốn mạch kiến thức;
- phiếu công thức tra cứu nhanh;
- đề luyện tập đủ 12 câu nhiều phương án, 2 câu đúng–sai, 4 câu trả lời ngắn và 3 câu tự luận;
- đáp án, lời giải chi tiết, thang điểm gợi ý và bảng đối chiếu toàn bộ bảng đặc tả;
- mục lục, bookmark PDF, liên kết nguồn và font tiếng Việt nhúng.

> **Lưu ý về nguồn:** DOCX đầu vào chỉ chứa ma trận và bảng đặc tả, không chứa đề thi hoàn chỉnh hay đáp án chính thức. Vì vậy, đề trong tài liệu được ghi rõ là **đề luyện tập mới bám ma trận**, không phải đề gốc của nhà trường.

## Cấu trúc mã nguồn

- `guide/content.py`: phần hướng dẫn và lý thuyết theo chương.
- `guide/assessment.py`: phiếu công thức và đề luyện tập.
- `guide/solutions.py`: đáp án, lời giải và phụ lục đối chiếu.
- `guide/pdfguide.py`: kiểu trang, bảng, sơ đồ và bộ dựng PDF.
- `guide/mathjax_renderer.cjs`: kết xuất công thức TeX bằng MathJax.
- `guide/build.py`: tạo PDF hoàn chỉnh.
- `guide/validate.py`: kiểm tra số câu, đáp số, nội dung bắt buộc, font, metadata, giới hạn trang và tạo ảnh tổng duyệt.

## Dựng và kiểm tra lại

Yêu cầu: Python 3.11+, Node.js 18+, và font DejaVu Sans (thường có sẵn trên Linux).

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
npm ci
.venv/bin/python guide/build.py
.venv/bin/python guide/validate.py
```

PDF được ghi ở thư mục gốc. Các tệp trung gian và ảnh tổng duyệt được ghi trong `build/guide/`, không đưa vào Git.
