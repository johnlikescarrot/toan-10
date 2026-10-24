# Nguồn nội dung & bộ dựng PDF

- `parts/01_mo_dau.md` – lời nói đầu + cấu trúc đề, kế hoạch ôn tập
- `parts/02_kien_thuc.md` – kiến thức trọng tâm 4 chương
- `parts/03_de_thi.md` – đề tham khảo 21 câu
- `parts/04_dap_an.md` – đáp án và lời giải chi tiết
- `parts/05_tu_luyen.md` – bài tự luyện và phụ lục
- `content.md` – tệp ghép do `build.py` sinh ra
- `md2pdf.py` – bộ dựng PDF trên ReportLab

## Cú pháp nội dung (rút gọn)

```
# số|Tiêu đề chương        -> dải màu + mục lục cấp 1
## 2.3 Tiêu đề mục         -> mục lục cấp 2
### 2.3.1 Tiểu mục         -> mục lục cấp 3 (chỉ khi có số hiệu)
Đoạn văn, **đậm**, *nghiêng*
- gạch đầu dòng (thụt 2 dấu cách = cấp 2)
1. danh sách đánh số
| bảng | cột |
> hộp ghi nhớ   !> hộp lưu ý   +> hộp chốt ý
@opts A. … | B. …   @opts C. … | D. …     (phương án trắc nghiệm 2 cột)
\v{AB}                    -> vectơ AB có mũi tên
[[toc]] [[pagebreak]] [[vennrow]] [[venn:both|nhãn]] [[lpfig|chú thích]]
```

## Dựng lại

```bash
python3 build.py ../..            # hoặc: python3 build.py <đường-dẫn-pdf>
```
