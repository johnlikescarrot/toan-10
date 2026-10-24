# Đề cương ôn tập Giữa học kì I – Toán 10 (Kết nối tri thức)

Tài liệu ôn tập **42 trang** được biên soạn từ ma trận và bảng đặc tả đề kiểm tra
trong tệp `MA TRẬN TOÁN 10 - GIỮA KÌ I.docx` (Tổ Toán – Tin, Trường THPT Hà Huy Tập,
năm học 2026 – 2027).

➡️ **Sản phẩm chính: [`DE_CUONG_ON_TAP_TOAN_10_GK1.pdf`](DE_CUONG_ON_TAP_TOAN_10_GK1.pdf)**

## Nội dung tài liệu

| Phần | Nội dung | Trang |
|------|----------|-------|
| — | Bìa, mục lục có liên kết + bookmark PDF | 1 – 2 |
| Mở đầu | Hướng dẫn sử dụng, cấu trúc đề, phân bổ điểm, chiến lược 90 phút, lộ trình 7 ngày | 3 – 6 |
| **A** | Tóm tắt lý thuyết trọng tâm 4 chương (định nghĩa, tính chất, công thức, lỗi thường gặp) | 6 – 17 |
| **B** | 17 dạng toán thường gặp: phương pháp + ví dụ mẫu có lời giải + bảng tra nhanh | 18 – 26 |
| **C** | Đề luyện tập số 1 (12 TN + 2 đúng–sai + 4 trả lời ngắn + 3 tự luận) + phiếu trả lời | 27 – 30 |
| **D** | Đáp án nhanh và lời giải chi tiết 100% câu hỏi, kèm thang điểm từng bước | 31 – 35 |
| **E** | Phụ lục: ma trận & đặc tả **nguyên văn**, sổ tay công thức, kĩ năng máy tính, checklist | 36 – 42 |

## Về nguồn gốc đề bài

Tệp `.docx` gốc **chỉ chứa ma trận và bảng đặc tả** (mô tả số câu, mức độ, dạng câu cho
từng đơn vị kiến thức) — **không kèm nội dung câu hỏi cụ thể**. Vì vậy tài liệu này:

1. Tái hiện **nguyên văn** ma trận và đặc tả ở Phần E để đối chiếu;
2. Biên soạn **Đề luyện tập số 1** bám chính xác từng ô của ma trận
   (đúng số câu, đúng mức độ NB – TH – VD – VDC, đúng hình thức câu mà đặc tả yêu cầu);
3. Cung cấp lời giải chi tiết cho **toàn bộ** câu hỏi của đề luyện.

## Cấu trúc mã nguồn

```
assets/fonts/          DejaVu Sans (đã subset, phủ đủ tiếng Việt + ký hiệu toán)
tools/
  pdfkit.py            Đăng ký font, bảng màu, style, flowable tuỳ biến (banner, callout, bảng)
  figures.py           Hình vẽ vector: biểu đồ Ven, trục số, nửa mặt phẳng, miền nghiệm, tam giác
  build_pdf.py         Khung tài liệu: bìa, mục lục, header/footer, bookmark
  content_front.py     Phần mở đầu
  content_theory.py    Phần A – lý thuyết
  content_methods.py   Phần B – 17 dạng toán
  content_exam.py      Phần C – đề luyện + phiếu trả lời
  content_answers.py   Phần D – đáp án, lời giải
  content_appendix.py  Phần E – phụ lục
```

## Dựng lại PDF

Yêu cầu Python ≥ 3.9 và ReportLab (không cần LaTeX, không cần font hệ thống).

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python tools/build_pdf.py            # -> DE_CUONG_ON_TAP_TOAN_10_GK1.pdf
.venv/bin/python tools/build_pdf.py out.pdf    # hoặc chỉ định đường dẫn
```

Font DejaVu Sans được nhúng sẵn trong `assets/fonts/`, đã subset để giữ đủ dấu tiếng Việt
(ă â đ ê ô ơ ư và toàn bộ thanh điệu), các ký hiệu toán (∈ ∉ ⊂ ⊃ ∪ ∩ ∅ ℝ ℕ ℤ ℚ ∀ ∃ ⇒ ⇔ ≤ ≥ ≠ √ ∞ °)
và các ký tự trang trí, nhờ đó PDF hiển thị đúng trên mọi máy đọc.

## Đặc điểm kỹ thuật của PDF

- Khổ A4, 42 trang, vector hoàn toàn (chữ và hình đều sắc nét khi phóng to).
- **98 liên kết** trong mục lục (bấm để nhảy tới mục) và **49 bookmark** điều hướng.
- Metadata đầy đủ (tiêu đề, tác giả, chủ đề).
- Toàn bộ công thức được trình bày bằng ký hiệu Unicode chuẩn trong font nhúng — có thể
  sao chép/tìm kiếm văn bản trong PDF.
