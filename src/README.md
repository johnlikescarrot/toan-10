# Nguồn dựng đề cương (Python + ReportLab)

Thư mục này chứa mã nguồn sinh ra file
`De-cuong-on-tap-Giua-ki-I-Toan-10-KNTT.pdf` ở thư mục gốc của repo.

## Cài đặt

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Dựng PDF

```bash
python figures.py          # sinh hình minh hoạ vào assets/fig/
python build.py            # ghi PDF ra thư mục gốc repo
```

## Cấu trúc

| Tệp | Nội dung |
|---|---|
| `kit.py` | Khung dựng: font, style, thành phần (câu hỏi, lời giải, bảng, hộp ghi nhớ), mục lục, chân trang |
| `c_front.py` | Bìa, mở đầu, mục lục |
| `c_theory1.py` | Phần I – Chương I (mệnh đề, tập hợp) và Chương II (bất phương trình bậc nhất hai ẩn) |
| `c_theory2.py` | Phần I – Chương III (hệ thức lượng) và Chương IV (vectơ) |
| `c_exam.py` | Phần II – đề tham khảo 24 câu (12 TN + 2 ĐS + 4 TLN + 3 TL) |
| `c_solution.py` | Phần III – đáp án và lời giải chi tiết 24 câu |
| `c_back.py` | Phần IV – ma trận, đặc tả, kế hoạch ôn tập, trang công thức |
| `figures.py` | Vẽ hình minh hoạ bằng matplotlib |
| `build.py` | Lắp ráp và xuất PDF |

## Quy ước soạn thảo trong các tệp nội dung

- `$...$` – công thức (in nghiêng); hỗ trợ `^` / `_`, `\\v{AB}` (vectơ), `\\overline{P}`,
  `\\widehat{A}`, và các lệnh LaTeX thông dụng (`\\cup`, `\\cap`, `\\in`, `\\Rightarrow`, `\\sqrt`…).
- `**chữ đậm**`, `<i>`, `<b>`, `<font color=...>` – định dạng trực tiếp.
- Font: Noto Sans (tiếng Việt) + DejaVu Sans (ký hiệu toán) đặt trong `assets/fonts`.
