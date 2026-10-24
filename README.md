# Đề cương ôn tập Giữa học kì I — Toán 10 (Kết nối tri thức)

Tài liệu ôn tập hoàn chỉnh cho bài kiểm tra giữa học kì I năm học **2026–2027**, biên soạn bám sát
file `MA TRẬN TOÁN 10 - GIỮA KÌ I.docx` của Tổ Toán – Tin, Trường THPT Hà Huy Tập.

**Sản phẩm chính:** [`output/De-cuong-on-tap-Toan-10-GK1-KNTT.pdf`](output/De-cuong-on-tap-Toan-10-GK1-KNTT.pdf) — 33 trang, khổ A4, có mục lục và bookmark.

---

## 1. Tài liệu gốc và cách xử lý

File `.docx` gốc **không chứa đề bài**. Nó gồm bốn phần: mục tiêu, hình thức, ma trận phân bố câu hỏi
và bảng đặc tả mức độ nhận thức — tức là chỉ mô tả *yêu cầu* của từng câu (ví dụ "Câu 3: biết cho tập
hợp bằng cách liệt kê…"), chứ không có nội dung số cụ thể.

Vì vậy đề ở Phần 2 của tài liệu được **biên soạn lại đúng theo bảng đặc tả**: mỗi câu giữ nguyên vị trí,
đơn vị kiến thức và mức độ nhận thức mà ma trận quy định. Cấu trúc, thang điểm và độ khó khớp với đề
chính thức; nội dung số là do biên soạn để có sẵn bài luyện. Điều này được nêu rõ ngay trong tài liệu
(mục B.7) để người đọc không nhầm đây là đề đã thi.

## 2. Cấu trúc tài liệu

| Phần | Nội dung | Trang |
|---|---|---|
| Bìa | Nhận diện, phạm vi kiến thức, cách dùng | 1 |
| Mục lục | Có bookmark, nhảy trực tiếp trong PDF | 2 |
| A | Cách dùng đề cương, quy ước kí hiệu, cách tính điểm | 3 |
| B | Cấu trúc đề, ma trận, bản đồ câu hỏi, đối chiếu SGK, phạm vi loại trừ | 4 |
| **I** | Hệ thống lý thuyết 4 chương + ví dụ mẫu + lỗi hay mắc + bài tập tự luyện | 7 |
| **II** | Đề kiểm tra 21 câu, đúng cấu trúc 4 phần, thang điểm 10 | 21 |
| **III** | Đáp án và lời giải chi tiết từng câu, từng ý đúng/sai | 25 |
| **IV** | Bảng đáp án, thang điểm, biểu điểm tự luận, chẩn đoán lỗi, lộ trình 7 ngày, phiếu công thức | 30 |

### Bám ma trận

| Phần | Dạng | Số câu | Điểm |
|---|---|---|---|
| I | Trắc nghiệm chọn phương án | 12 | 3,0 |
| II | Trắc nghiệm đúng – sai (4 ý/câu) | 2 | 2,0 |
| III | Trắc nghiệm trả lời ngắn | 4 | 2,0 |
| IV | Tự luận | 3 | 3,0 |
| | | **21** | **10,0** |

Phân bố theo chương: Chương 1 — 4,00 đ · Chương 2 — 2,50 đ · Chương 3 — 3,00 đ · Chương 4 — 0,50 đ.
Điểm đúng/sai được chia cho từng ý nên được quy về đơn vị kiến thức tương ứng (xem bảng B.2).

## 3. Biên soạn lại PDF

Yêu cầu: Python 3.9+ và font DejaVu Sans (có sẵn trong `fonts-dejavu-core` trên Debian/Ubuntu).

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
cd src && ../.venv/bin/python build.py
```

Kết quả được ghi vào `output/De-cuong-on-tap-Toan-10-GK1-KNTT.pdf`.

Toàn bộ tài liệu dùng **một họ font duy nhất** (DejaVu Sans) vì font này phủ đủ dấu tiếng Việt và các
kí hiệu toán học dùng trong chương trình lớp 10: `∀ ∃ ⇒ ⇔ ∈ ∉ ⊂ ∩ ∪ ∅ ℝ ℕ ℤ ℚ ≤ ≥ √ ∆ α β ≠ ± ≈`.
Nếu đổi sang font không có đủ glyph, dấu tiếng Việt sẽ bị mất.

### Cấu trúc mã nguồn

```
src/
├── design.py        # design system: font, màu, style, bảng, hộp gọi chú ý, khung trang, bìa
├── sec_front.py     # bìa, mục lục, hướng dẫn, cấu trúc đề & ma trận (phần A, B)
├── sec_ch1.py       # Chương 1 – Mệnh đề và tập hợp
├── sec_ch2.py       # Chương 2 – Bất phương trình bậc nhất hai ẩn
├── sec_ch3.py       # Chương 3 – Hệ thức lượng trong tam giác
├── sec_ch4.py       # Chương 4 – Vectơ
├── sec_exam.py      # Đề kiểm tra 21 câu (Phần II)
├── sec_solutions.py # Đáp án và lời giải chi tiết (Phần III)
├── figures.py       # hình vẽ canvas: trục số, biểu đồ Ven, miền nghiệm, tam giác
├── sec_appendix.py  # Tra cứu nhanh, lộ trình ôn tập (Phần IV)
└── build.py         # ghép các phần và xuất PDF
```

## 4. Kiểm tra tính đầy đủ

Đối chiếu với bảng đặc tả, mọi câu được ghi trong ma trận đều có mặt và có lời giải:

- 12 câu trắc nghiệm: câu 1–2 (mệnh đề), 3 (tập hợp), 4 (phép toán tập hợp), 5 (bpt bậc nhất hai ẩn),
  6 (hệ bpt), 7–8 (giá trị lượng giác), 9–10 (hệ thức lượng), 11–12 (vectơ).
- 2 câu đúng/sai × 4 ý = 8 ý, mỗi ý có kết luận Đ/S kèm giải thích.
- 4 câu trả lời ngắn: 15 (số phần tử), 16 (bài toán đếm), 17 (giá trị lượng giác), 18 (diện tích).
- 3 câu tự luận: 19 (giao/hợp/phần bù), 20 (giải tam giác thực tế), 21 (tối ưu hệ bất phương trình).

Không có câu nào trong ma trận bị bỏ sót; mỗi chương còn có thêm 4–9 bài tập tự luyện kèm đáp án.
