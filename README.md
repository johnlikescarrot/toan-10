# Đề cương ôn tập Toán 10 – Giữa học kỳ I (năm học 2026-2027)

Tài liệu ôn tập toàn diện cho môn Toán lớp 10, bám sát chương trình **“Kết nối tri thức”**
(tập 1: Bài 1 → Bài 7) và được xây dựng từ tài liệu gốc
**[`MA TRẬN TOÁN 10 - GIỮA KÌ I.docx`](MA%20TRẬN%20TOÁN%2010%20-%20GIỮA%20KÌ%20I.docx)**
(ma trận + bảng đặc tả đề kiểm tra giữa học kỳ I năm học 2026-2027).

## Sản phẩm

📄 **[`DE CUONG ON TAP TOAN 10 - GIUA KY I 2026-2027.pdf`](DE%20CUONG%20ON%20TAP%20TOAN%2010%20-%20GIUA%20KY%20I%202026-2027.pdf)** — 37 trang, định dạng PDF, có mục lục tự động,
đầu trang/chân trang đánh số trang và các bảng trình bày trên khổ A4 dọc lẫn A4 ngang.

### Cấu trúc tài liệu

| Phần | Nội dung |
|------|----------|
| **A** | Thông tin chung; cấu trúc đề; **ma trận** và **bảng đặc tả** (nguyên bản từ tài liệu nguồn); bảng đối chiếu 21 câu hỏi với đơn vị kiến thức; ghi chú về các điểm chưa thống nhất trong ma trận gốc; lộ trình ôn tập 8 tuần; phương pháp ôn tập |
| **B** | Kiến thức nền tảng và dạng bài theo từng chương (mục tiêu → lý thuyết → công thức → **ví dụ mẫu có lời giải** → lỗi thường gặp → bài tập tự luyện kèm đáp án) cho Chương 1–4 |
| **C** | **Đề kiểm tra giữa học kỳ I 2026-2027: đầy đủ 21 câu hỏi** (12 câu trắc nghiệm chọn phương án, 2 câu trắc nghiệm đúng sai, 4 câu trả lời ngắn, 3 câu tự luận) – 90 phút – 10,0 điểm |
| **D** | **Đáp án chi tiết cho toàn bộ 21 câu**, kèm hướng dẫn chấm điểm các câu tự luận |
| **E** | Phụ lục: bảng công thức cần nhớ, bảng đáp án nhanh, phiếu tự đánh giá 16 mục, gợi ý sử dụng, tài liệu tham khảo |

### Đối chiếu với tài liệu nguồn

* Ma trận (19 cột) và bảng đặc tả được trích **nguyên vẹn** từ file `.docx` (Phần A.3 và A.4).
* Mỗi câu hỏi trong Phần C đều được đối chiếu với bảng đặc tả theo bảng tại A.5.
* Các kí hiệu đặc biệt trong tài liệu gốc (ký hiệu phổ biến `∀`, ký hiệu tồn tại `∃`, ký hiệu vô
  cùng `∞` trong cách ghi khoảng) được giữ nguyên khi trích dẫn.

## Dựng lại PDF từ mã nguồn

Mã nguồn nằm trong thư mục `tools/`:

| Tệp | Vai trò |
|-----|---------|
| `tools/build_de_cuong.py` | Tệp chạy chính: dựng bìa, mục lục và ghép các phần nội dung, xuất PDF. |
| `tools/dung_pdf.py` | Bộ công cụ trình bày: font DejaVu, style, khung tiêu đề/chân trang, hộp ghi chú, bảng, mục lục tự động. |
| `tools/noi_dung_phan_a.py` | Nội dung Phần A. |
| `tools/noi_dung_phan_b.py` | Nội dung Phần B (4 chương). |
| `tools/noi_dung_phan_cde.py` | Nội dung Phần C, D, E. |

Yêu cầu môi trường:

```bash
pip install reportlab          # dựng PDF
# Font: bộ DejaVu (Sans/Serif/Mono + Oblique/Italic) của hệ đối
```

Dựng lại:

```bash
python3 tools/build_de_cuong.py
```

Tệp PDF kết quả sẽ được ghi đè tại thư mục gốc với tên
`DE CUONG ON TAP TOAN 10 - GIUA KY I 2026-2027.pdf`.

## Cấu trúc thư mục

```
.
├── DE CUONG ON TAP TOAN 10 - GIUA KY I 2026-2027.pdf   # sản phẩm chính
├── MA TRẬN TOÁN 10 - GIỮA KÌ I.docx                   # tài liệu nguồn (ma trận + bảng đặc tả)
├── README.md
└── tools/                                             # mã nguồn dựng PDF
```

## Đơn vị phụ trách

Tổ Toán – Tin, Trường THPT Hà Huy Tập.
