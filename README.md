# Đề cương ôn tập giữa học kì I – Toán 10 (Kết nối tri thức)

Tài liệu ôn thi được biên soạn **bám sát 100% Ma trận và Bảng đặc tả** đề kiểm tra giữa học kì I
môn Toán 10, năm học 2026 – 2027 (Trường THPT Hà Huy Tập – Tổ Toán – Tin).

## 📄 Sản phẩm

| Tệp | Nội dung |
| --- | --- |
| [`DE-CUONG-ON-TAP-TOAN-10-GIUA-KI-1.pdf`](DE-CUONG-ON-TAP-TOAN-10-GIUA-KI-1.pdf) | **Đề cương hoàn chỉnh – 40 trang** (bản chính thức) |
| `MA TRẬN TOÁN 10 - GIỮA KÌ I.docx` | Văn bản gốc của nhà trường (ma trận + bảng đặc tả) |
| `de-cuong/` | Mã nguồn dựng PDF (Python + ReportLab) |

## 🎯 Nội dung đề cương

1. **Hướng dẫn sử dụng & cấu trúc đề** – cấu trúc 4 phần, thang điểm lũy tiến của câu Đúng – Sai,
   bảng phân bố nội dung và mức độ theo ma trận, lộ trình ôn 5 bước, các lỗi mất điểm phổ biến.
2. **Chương I – Mệnh đề và tập hợp** – lý thuyết đầy đủ, 9 dạng toán có ví dụ mẫu, sơ đồ tư duy,
   8 bài tập tự luyện kèm đáp số.
3. **Chương II – Bất phương trình và hệ bất phương trình bậc nhất hai ẩn** – quy tắc 4 bước biểu diễn
   miền nghiệm, quy trình 4 bước giải bài toán tối ưu, ví dụ mẫu đầy đủ có hình vẽ, 4 bài tự luyện.
4. **Chương III – Hệ thức lượng trong tam giác** – bảng giá trị lượng giác của góc đặc biệt,
   hai góc bù/phụ nhau, định lí côsin – sin, 5 công thức diện tích, giải tam giác, ứng dụng thực tiễn,
   7 bài tự luyện.
5. **Chương IV – Vectơ (Bài 7)** – 6 khái niệm mở đầu, 4 dạng toán, 5 bài tự luyện.
6. **Đề tham khảo số 1** – đúng 100% cấu trúc ma trận: 12 TN nhiều lựa chọn + 2 TN đúng–sai +
   4 trả lời ngắn + 3 tự luận, thời gian 90 phút.
7. **Đáp án và lời giải chi tiết** – đáp án nhanh cho cả 21 câu + lời giải từng bước, chỉ rõ bẫy và
   thang điểm gợi ý cho 3 câu tự luận.
8. **Phụ lục** – bảng công thức tổng hợp, 10 lỗi mất điểm, chiến lược làm bài 90 phút,
   phiếu tự đánh giá trước kì thi.

> **Lưu ý về văn bản gốc:** tệp `.docx` của nhà trường là *ma trận đề* kèm *bảng đặc tả* — nó quy định
> kiến thức nào được hỏi, ở mức độ nào, bao nhiêu câu và bao nhiêu điểm, **chứ không chứa câu hỏi cụ thể**.
> Vì vậy đề cương bám đúng 100% các đơn vị kiến thức và mức độ trong ma trận, đồng thời xây dựng
> **Đề tham khảo số 1** trùng khớp hoàn toàn về cấu trúc, số câu và phân bố điểm; toàn bộ 21 câu đều có
> đáp án và lời giải chi tiết.

## 🛠 Dựng lại PDF

Yêu cầu: Python 3.9+ và các gói `reportlab`, `matplotlib`, `pillow`.

```bash
pip install reportlab matplotlib pillow
cd de-cuong
python build.py        # sinh hình minh hoạ + xuất PDF ở thư mục gốc
```

Cấu trúc mã nguồn:

```
de-cuong/
├── build.py         # điểm vào: ghép nội dung và dựng PDF
├── engine.py        # bộ dựng PDF (font, khổ giấy, header/footer, mục lục 2 lượt, các khối nội dung)
├── make_figs.py     # sinh 3 hình minh hoạ (biểu đồ Ven, miền nghiệm, trục số)
├── content1.py      # bìa, mục lục, hướng dẫn, Chương I
├── content2.py      # Chương II, Chương III
├── content3.py      # Chương IV, Đề tham khảo
├── content4.py      # Đáp án, lời giải chi tiết, Phụ lục
└── assets/          # hình PNG + font DejaVu Sans (giấy phép tự do) và STIX
```

Font nhúng: **DejaVu Sans** (bộ kí hiệu toán học đầy đủ: ∈, ⊂, ∪, ∩, ∅, ℝ, ℕ, ℤ, ℚ, ∀, ∃, ≤, ≥, ≠, √, ∠, ⊥, ∞…)
và **STIX General** cho kí hiệu P có gạch ngang trên đầu (mệnh đề phủ định).
