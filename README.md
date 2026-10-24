# Đề cương ôn tập Giữa học kì I — Toán 10 (Kết nối tri thức) — NH 2026–2027

Đề cương được biên soạn **bám sát trực tiếp** tệp `MA TRẬN TOÁN 10 - GIỮA KÌ I.docx` (ma trận + bảng đặc tả của Tổ Toán - Tin, Trường THPT Hà Huy Tập).

## 📄 Sản phẩm chính

**[`DE-CUONG-ON-TAP-TOAN-10-GIUA-KI-I-2026-2027.pdf`](DE-CUONG-ON-TAP-TOAN-10-GIUA-KI-I-2026-2027.pdf)** — 38 trang, khổ A4, tiếng Việt.

## Nội dung tài liệu

| Phần | Nội dung |
| --- | --- |
| Mục lục | Có liên kết nhảy tới từng mục (bookmark PDF) |
| **1** | Thông tin kì thi, cấu trúc đề, **ma trận** và **bảng đặc tả** được lược dịch và diễn giải; phân tích "học gì để trúng ma trận" |
| **2** | Tóm tắt lí thuyết trọng tâm 4 chương + 11 dạng toán mẫu có lời giải (mệnh đề, tập hợp, bất phương trình & hệ bất phương trình bậc nhất hai ẩn, giá trị lượng giác, hệ thức lượng, khái niệm vectơ) |
| **3** | **Đề kiểm tra minh họa** đúng ma trận: 12 câu TN + 2 câu Đúng–Sai (8 ý) + 4 câu trả lời ngắn + 3 câu tự luận + phiếu trả lời |
| **4** | **Đáp án và lời giải chi tiết 100 % câu hỏi** (21 câu / 27 ý), thang điểm từng ý, bảng đối chiếu đề ↔ ma trận |
| **5** | 17 lỗi sai thường gặp, phân bổ 90 phút trong phòng thi, kế hoạch ôn 7 ngày, checklist tự đánh giá |
| Phụ lục A | Trang công thức "bỏ túi" |
| Phụ lục B | 10 câu tự luyện nhanh kèm đáp án |

## Lưu ý về nguồn đề

Tệp gốc là **ma trận – bảng đặc tả** (chưa chứa nội dung câu hỏi). Vì vậy Phần 3 là **đề minh họa được biên soạn trùng khớp từng câu với bảng đặc tả** (đúng mã câu, đơn vị kiến thức, mức độ NB/TH/VD/VDC, số điểm), và Phần 4 giải chi tiết toàn bộ đề đó.

## Cấu trúc mã nguồn

```
nguon/
├── build.py            # render PDF bằng ReportLab (DejaVu, hỗ trợ tiếng Việt)
└── content/*.txt       # nội dung tài liệu (markup rút gọn: #H2, #B, #TABLE, #M ...)
```

Kết xuất lại PDF:

```bash
pip install reportlab
python3 nguon/build.py DE-CUONG-ON-TAP-TOAN-10-GIUA-KI-I-2026-2027.pdf
```
