# Đề cương ôn tập Giữa học kì I – Toán 10 (Kết nối tri thức)

Tài liệu ôn tập được biên soạn từ tệp **`MA TRẬN TOÁN 10 - GIỮA KÌ I.docx`** (Tổ Toán – Tin, THPT Hà Huy Tập, năm học 2026 – 2027).

## Sản phẩm

| Tệp | Nội dung |
| --- | --- |
| `DE-CUONG-ON-TAP-TOAN-10-GK1.pdf` | **Bản PDF hoàn chỉnh, 36 trang** – sản phẩm chính |
| `de-cuong/src/parts/*.md` | Nội dung nguồn, chia theo 5 phần |
| `de-cuong/src/md2pdf.py` | Bộ dựng PDF (ReportLab) – không cần LaTeX/pandoc |
| `de-cuong/src/build.py` | Ghép các phần và xuất PDF |
| `de-cuong/source/ma-tran-goc.txt` | Toàn văn tệp ma trận gốc đã trích xuất, để đối chiếu |

## Nội dung PDF

1. **Cấu trúc đề & kế hoạch ôn tập** – hình thức, thang điểm, cách tính điểm phần Đúng – Sai, phân bố câu hỏi theo ma trận, phân bố thời gian trong phòng thi, lộ trình 7 ngày, 5 lỗi mất điểm phổ biến.
2. **Kiến thức trọng tâm 4 chương** – mệnh đề; tập hợp; bất phương trình và hệ bất phương trình bậc nhất hai ẩn; giá trị lượng giác và hệ thức lượng trong tam giác; vectơ. Mỗi mục có định nghĩa, bảng công thức, ví dụ mẫu có lời giải, lỗi thường gặp và hộp “Chốt ý”.
3. **Đề tham khảo 21 câu** – đúng cấu trúc ma trận: 12 trắc nghiệm + 2 Đúng – Sai + 4 trả lời ngắn + 3 tự luận.
4. **Đáp án & lời giải chi tiết** – bảng đáp án nhanh, lời giải từng câu kèm nhận xét và cách kiểm tra chéo.
5. **Bài tập tự luyện & phụ lục** – 15 bài tự luyện có đáp số, bảng công thức, checklist trước thi, mẫu sổ tay lỗi.

Có kèm biểu đồ Ven, hình minh hoạ miền nghiệm bài toán quy hoạch, mục lục tự động và bookmark PDF.

## Ghi chú quan trọng

Tệp ma trận gốc **chỉ có ma trận và bản đặc tả, không kèm nội dung câu hỏi và đáp án**. Vì vậy:

- Toàn bộ mục tiêu, hình thức, thang điểm, ma trận và bản đặc tả (Phần 1, Phần 3) được **chép lại trung thực** từ tệp gốc.
- 21 câu trong Phần 3 là **đề tham khảo do tài liệu biên soạn**, bám đúng đơn vị kiến thức và mức độ nhận thức của từng câu theo bản đặc tả; lời giải ở Phần 4 là lời giải của chính các câu đó. Điều này được nêu rõ ngay trong tài liệu (mục 5.6).

Một điểm chưa nhất quán của tệp gốc cũng đã được ghi chú: dòng “Tổng” của ma trận ghi 24 câu, nhưng 12 + 2 + 4 + 3 = 21 câu, tương ứng đúng 10,0 điểm.

## Dựng lại PDF

```bash
pip install --break-system-packages reportlab matplotlib pymupdf
python3 de-cuong/src/build.py            # -> DE-CUONG-ON-TAP-TOAN-10-GK1.pdf
```

Phông chữ: DejaVu Serif/Sans (có sẵn trong hệ thống Linux) – hỗ trợ đầy đủ tiếng Việt và ký hiệu toán.
