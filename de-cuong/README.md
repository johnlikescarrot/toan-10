# Đề cương ôn tập giữa học kì I — môn Toán lớp 10 — năm học 2026–2027

Đề cương ôn tập toàn diện, biên soạn bám sát **Ma trận đề kiểm tra giữa kì I năm học 2026-2027**
của Tổ Toán–Tin, Trường THPT Hà Huy Tập, và chương trình **Toán 10 – bộ sách Kết nối tri thức với
cuộc sống**.

## Sản phẩm

| Tệp | Nội dung |
|---|---|
| [`De-cuong-on-tap-Toan-10-Giua-ki-I-2026-2027.pdf`](De-cuong-on-tap-Toan-10-Giua-ki-I-2026-2027.pdf) | **Bản PDF hoàn chỉnh** (34 trang, khổ A4) — đây là sản phẩm chính |
| `src/content.py` | Toàn bộ nội dung tài liệu (nguồn duy nhất) |
| `src/pdfkit.py` | Bộ vẽ PDF tiếng Việt (fpdf2 + DejaVu), kèm 7 hình minh họa vẽ bằng vector |
| `src/build.py` | Chương trình sinh PDF (đọc `content.py`, dựng mục lục, canh trang) |
| `src/verify_answers.py` | Kiểm thử lại **toàn bộ kết quả số** bằng Python |
| `src/check_completeness.py` | Đối chiếu đề minh họa với ma trận (số câu, số ý, đáp án) |
| `src/check_pdf.py` | Kiểm tra bản in: tràn lề, chồng chữ, trang trống |

## Cấu trúc tài liệu (6 phần)

1. **Phân tích ma trận** — phạm vi kiến thức, cấu trúc 4 phần của đề, ma trận chi tiết 19 cột, bảng
   đặc tả từng câu, tỉ trọng điểm theo chương, chiến lược làm bài trong 90 phút.
2. **Kiến thức trọng tâm** — lý thuyết cô đọng theo 4 chương, công thức, ví dụ có lời giải, và các
   "bẫy" mất điểm thường gặp.
3. **Đề kiểm tra minh họa** — 12 câu trắc nghiệm + 2 câu đúng/sai (8 ý) + 4 câu trả lời ngắn +
   3 câu tự luận, đúng khuôn dạng đề kiểm tra mới.
4. **Đáp án và lời giải chi tiết** — cho **toàn bộ 27 lệnh hỏi**, kèm hướng dẫn chấm tự luận theo
   thang điểm từng bước.
5. **Ngân hàng bài tập tự luyện** — 14 bài theo 4 chương, có đáp án.
6. **Phụ lục** — bảng công thức một trang, bảng giá trị lượng giác, hướng dẫn bấm máy tính cầm tay,
   phiếu tự đánh giá 24 kỹ năng, nguồn tham khảo, lời kết.

## Về phạm vi của tệp nguồn

Tệp `MA TRẬN TOÁN 10 - GIỮA KÌ I.docx` (ở thư mục gốc kho lưu trữ) là **ma trận + bảng đặc tả**: nó
mô tả *cấu trúc đề, số câu, mức độ nhận thức và yêu cầu cần đạt của từng câu*, nhưng **không chứa đề
bài cụ thể** (không có câu hỏi, không có đáp án). Đề kiểm tra chính thức của kì thi cũng chưa được
công bố công khai tại thời điểm biên soạn.

Vì vậy, đề ở Phần 3 là **đề minh họa được biên soạn mới**, thiết kế **khớp từng ô** với ma trận và
bảng đặc tả gốc — đúng số câu, đúng mức độ nhận thức, đúng đơn vị kiến thức và đúng nội dung mà bảng
đặc tả đã mô tả cho từng câu. Toàn bộ 27 lệnh hỏi đều có đáp án và lời giải chi tiết ở Phần 4.

## Sinh lại PDF

```bash
python3 -m venv .venv
.venv/bin/pip install -r de-cuong/src/requirements.txt \
                     -r de-cuong/src/requirements-dev.txt

# 1. Kiểm tra mọi ký tự đều có glyph trong font
.venv/bin/python de-cuong/src/build.py --check

# 2. Sinh PDF (34 trang)
.venv/bin/python de-cuong/src/build.py

# 3. Chạy ba bộ kiểm tra
python3 de-cuong/src/verify_answers.py        # 39 phép kiểm tra số học
python3 de-cuong/src/check_completeness.py    # 47 phép kiểm tra cấu trúc
.venv/bin/python de-cuong/src/check_pdf.py    # tràn lề / chồng chữ / trang trống
```

Yêu cầu: Python 3.9+, bộ font DejaVu (`/usr/share/fonts/truetype/dejavu`, có sẵn trên hầu hết bản
Linux; trên macOS cài qua `brew install --cask font-dejavu`).

## Đặc điểm kỹ thuật

- **Không phụ thuộc LaTeX, WeasyPrint hay trình duyệt** — chỉ cần `fpdf2` + font DejaVu, nên sinh
  được trong môi trường tối giản.
- **Toán học trình bày bằng ký tự Unicode** (ℝ, ℕ, ∈, ∩, ∪, ∀, ∃, ≤, ≥, √, α, ², ⁵ …) thay vì
  ảnh công thức, nên chữ **tìm kiếm được, sao chép được** và file nhẹ (~215 KB).
- **Mọi khối đều được đo chiều cao trước khi vẽ** (`multi_cell(dry_run=True)`) nên không có chữ tràn
  khung hay chồng lên nhau.
- **7 hình minh họa vẽ bằng vector**: sơ đồ Ven, trục số, nửa mặt phẳng nghiệm, miền nghiệm của hệ
  bất phương trình, tam giác đo chiều cao, hình bình hành vectơ, nửa đường tròn đơn vị.
- **Mục lục tự động** với số trang chính xác (dựng hai lượt đến khi ổn định).
- **Bảng rộng chia cột theo từ dài nhất**, tự giảm cỡ chữ trong giới hạn, không bao giờ ngắt giữa từ.

## Kiểm chứng

| Bộ kiểm tra | Kết quả |
|---|---|
| `verify_answers.py` | 39/39 PASS — mọi kết quả số (diện tích, cạnh, góc, GTLN, số tập con…) |
| `check_completeness.py` | 47/47 PASS — đủ 12+2+4+3 câu, đủ 4 phương án/câu, đủ 4 ý/câu đúng-sai |
| `check_pdf.py` | 34 trang, không tràn lề, không chồng chữ, không trang trống |

Đã kiểm chứng thêm: **sinh lại từ một bản sao sạch** (chỉ `de-cuong/`, môi trường ảo mới) cho ra
đúng số trang với **nội dung từng trang trùng khớp** bản đã phát hành — tài liệu tái lập được từ
mã nguồn.

## Giấy phép

Nội dung biên soạn cho mục đích học tập. Ma trận gốc thuộc Trường THPT Hà Huy Tập.
