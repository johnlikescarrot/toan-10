# Đề cương ôn tập Giữa học kì I – Toán 10 (Kết nối tri thức)

Tài liệu ôn tập 38 trang, biên soạn bám sát **Ma trận đề** và **Bảng đặc tả** kiểm tra
Giữa kì I năm học 2026–2027 của Tổ Toán – Tin, Trường THPT Hà Huy Tập
(tệp nguồn: `MA TRẬN TOÁN 10 - GIỮA KÌ I.docx`).

## Sản phẩm

| Tệp | Nội dung |
|---|---|
| `de-cuong-on-tap-giua-ki-1-toan-10.pdf` | **Bản PDF hoàn chỉnh** (38 trang, khổ A4) |
| `src/` | Mã nguồn dựng PDF bằng ReportLab |
| `assets/fonts/` | Font DejaVu Sans (hỗ trợ đầy đủ tiếng Việt và kí hiệu toán) |

## Cấu trúc tài liệu

- **Bìa + Lời nói đầu + Mục lục** (có bookmark PDF, số trang tự động)
- **Phần A** – Phân tích đề: cấu trúc 4 phần, ma trận điểm rút gọn, bảng đặc tả ↔ câu hỏi,
  chiến lược 90 phút, kế hoạch ôn 7 ngày, 10 lỗi mất điểm.
- **Phần B** – Lý thuyết trọng tâm và **12 dạng toán** (Chương I–IV): mỗi dạng có quy trình,
  ví dụ mẫu giải chi tiết, lỗi thường gặp; kèm **B.5 – Bảng công thức cần nhớ**.
- **Phần C** – **ĐỀ MẪU** đúng ma trận: 12 TN lựa chọn + 2 Đúng–Sai (4 ý/câu) + 4 trả lời ngắn
  + 3 tự luận (10 điểm, 90 phút).
- **Phần D** – **Đáp án và lời giải chi tiết toàn bộ 27 câu**, thang điểm tự luận, nhận xét sau khi chấm.
- **Phần E** – Đáp số 22 bài tự luyện.
- **Phần F** – Phụ lục: bảng ma trận ↔ đáp án, checklist kĩ năng, lưu ý phòng thi, nguồn tài liệu.

## Dựng lại PDF

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python src/build.py                 # -> de-cuong-on-tap-giua-ki-1-toan-10.pdf
```

`build.py` chạy hai lượt: lượt đầu đếm số trang, lượt sau dựng bản chính thức để mục lục và
chân trang ("Trang n/N") chính xác.
