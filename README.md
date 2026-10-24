# Đề cương ôn tập giữa học kì I – Toán 10 (Kết nối tri thức)

Tài liệu ôn tập được biên soạn từ văn bản **“MA TRẬN ĐỀ KIỂM TRA GIỮA KÌ I NĂM HỌC 2026–2027 – MÔN TOÁN, LỚP 10”**
của Tổ Toán – Tin, Trường THPT Hà Huy Tập.

## Sản phẩm

| Tệp | Mô tả |
|---|---|
| [`De-cuong-on-tap-Giua-ki-I-Toan-10-KNTT.pdf`](De-cuong-on-tap-Giua-ki-I-Toan-10-KNTT.pdf) | **Đề cương hoàn chỉnh – 29 trang A4**, có mục lục, dấu trang (bookmark), hình minh hoạ |
| [`MA TRẬN TOÁN 10 - GIỮA KÌ I.docx`](MA%20TR%E1%BA%ACN%20TO%C3%81N%2010%20-%20GI%E1%BB%AEA%20K%C3%8C%20I.docx) | Văn bản gốc của nhà trường (ma trận + bảng đặc tả) |
| [`src/`](src/) | Mã nguồn Python (ReportLab) dựng lại toàn bộ PDF |
| [`assets/`](assets/) | Font (Noto Sans, DejaVu Sans) và hình minh hoạ |

## Nội dung PDF

1. **Mở đầu** – tài liệu được xây dựng thế nào, cách dùng, nguồn.
2. **Phần I – Kiến thức trọng tâm** (tr. 4–16), bám theo SGK *Kết nối tri thức với cuộc sống*:
   - Chương I. Mệnh đề và tập hợp (Bài 1, Bài 2)
   - Chương II. Bất phương trình và hệ bất phương trình bậc nhất hai ẩn (Bài 3, Bài 4)
   - Chương III. Hệ thức lượng trong tam giác (Bài 5, Bài 6)
   - Chương IV. Vectơ (Bài 7 → Bài 11)
   
   Mỗi mục gồm: định nghĩa → công thức → phương pháp giải → ví dụ mẫu có lời giải → hộp “ghi nhớ / lỗi thường gặp”.
3. **Phần II – Đề thi tham khảo 24 câu** (tr. 17–19) đúng cấu trúc ma trận:
   12 câu TN chọn đáp án (3,0 đ) · 2 câu TN đúng–sai (2,0 đ) · 4 câu TN trả lời ngắn (2,0 đ) · 3 câu tự luận (3,0 đ).
4. **Phần III – Đáp án và lời giải chi tiết cả 24 câu** (tr. 20–24), kèm phân tích phương án nhiễu, thang điểm và lỗi thường gặp.
5. **Phần IV – Ma trận, đặc tả và kế hoạch ôn tập** (tr. 25–29): hình thức đề, ma trận theo nội dung,
   bảng đặc tả tóm tắt, bảng đối chiếu đề ↔ ma trận, kế hoạch ôn 7 ngày, chiến lược làm bài 90 phút,
   trang công thức cần nhớ, bảng tra cứu mục ↔ bài SGK.

## Lưu ý về nguồn đề

Tệp `.docx` gốc là **ma trận đề + bảng đặc tả + mô tả 3 câu tự luận**, **không kèm nội dung câu hỏi**.
Vì vậy Phần II là **đề tham khảo được biên soạn lại** phân bố đúng từng đơn vị kiến thức, đúng mức độ nhận thức
và đúng số điểm trong ma trận, kèm đáp án – lời giải đầy đủ cho cả 24 câu. Khi có đề gốc, chỉ cần thay Phần II;
phần lí thuyết và cách giải vẫn dùng được vì bám đúng đặc tả.

## Dựng lại PDF

```bash
cd src
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python figures.py && python build.py
```

Chi tiết về mã nguồn: xem [`src/README.md`](src/README.md).
