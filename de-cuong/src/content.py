# -*- coding: utf-8 -*-
"""
content.py -- Toan bo noi dung de cuong on tap Toan 10 (giua ki I, 2026-2027).
Noi dung duoc viet bang "mini-markup" do pdfkit.py hien thi thanh PDF.
"""

# ---------------------------------------------------------------------------
COVER_LINES = [
    "SỞ GIÁO DỤC VÀ ĐÀO TẠO",
    "TRƯỜNG THPT HÀ HUY TẬP – TỔ TOÁN – TIN",
]

INTRO = """
# LỜI NÓI ĐẦU & CÁCH DÙNG TÀI LIỆU

**Đề cương ôn tập kiểm tra giữa học kì I – môn Toán lớp 10 – năm học 2026–2027** được biên
soạn bám sát **Ma trận đề kiểm tra giữa kì I** của Tổ Toán–Tin, Trường THPT Hà Huy Tập và chương
trình **Toán 10 – bộ sách Kết nối tri thức với cuộc sống** (bộ sách dùng chung toàn quốc từ năm
học 2026–2027).

> **Nguồn tài liệu gốc**
> Tệp `MA TRẬN TOÁN 10 - GIỮA KÌ I.docx` — *Ma trận đề kiểm tra giữa kì I năm học 2026-2027,
> môn: Toán, lớp 10, thời gian làm bài 90 phút*. Tệp gồm ba phần: (I) Mục tiêu, (II) Hình thức,
> (III) Ma trận chi tiết và Bảng đặc tả. Theo siêu dữ liệu của tệp, tài liệu được tạo ngày
> 17/10/2026.

! **Một lưu ý quan trọng về phạm vi**
> Tệp nguồn là **ma trận + bảng đặc tả**: tài liệu mô tả *cấu trúc đề, số câu, mức độ nhận thức
> và yêu cầu cần đạt của từng câu* — nhưng **không chứa đề bài cụ thể** (không có câu hỏi, không
> có đáp án).
> Vì vậy, **Phần 3** của đề cương này là một **đề kiểm tra minh họa được biên soạn mới, bám sát
> 100% ma trận gốc**: đúng số câu (12 trắc nghiệm nhiều phương án + 2 câu đúng/sai gồm 8 ý + 4 câu
> trả lời ngắn + 3 câu tự luận), đúng mức độ nhận thức, đúng đơn vị kiến thức và đúng nội dung mà
> bảng đặc tả đã mô tả cho từng câu (Câu 1→Câu 12; Câu 1a–1d; Câu 2a–2d; Câu 1→Câu 4 trả lời ngắn;
> Câu 1→Câu 3 tự luận).
> **Phần 4** là **đáp án và lời giải chi tiết cho toàn bộ 27 lệnh hỏi** của đề minh họa đó, kèm
> hướng dẫn chấm tự luận.

## Tài liệu gồm những gì

- **Phần 1 — Phân tích ma trận.** Cấu trúc đề, ma trận chi tiết, bảng đặc tả từng câu, tỉ trọng
  điểm theo chương và chiến lược làm bài trong 90 phút.
- **Phần 2 — Kiến thức trọng tâm.** Lý thuyết cô đọng theo đúng 4 chương trong phạm vi kiểm tra,
  kèm công thức, ví dụ minh họa có lời giải và các "bẫy" mất điểm.
- **Phần 3 — Đề kiểm tra minh họa.** Đề hoàn chỉnh, đúng khuôn dạng 4 phần của đề kiểm tra mới.
- **Phần 4 — Đáp án và lời giải chi tiết.** Bảng đáp án nhanh + lời giải từng câu + hướng dẫn chấm.
- **Phần 5 — Ngân hàng bài tập tự luyện.** 12 bài theo 4 chương, có đáp án.
- **Phần 6 — Phụ lục.** Bảng công thức tóm tắt, bảng giá trị lượng giác đặc biệt, hướng dẫn bấm
  máy tính cầm tay, phiếu tự đánh giá và danh mục nguồn tham khảo.

## Ba cách dùng đề cương này

1. **Ôn cấp tốc (2–3 buổi):** đọc Phần 1 để biết trọng số điểm → học Phần 2 → làm Phần 3 → đối
   chiếu Phần 4.
2. **Ôn theo chuyên đề:** mỗi buổi một chương ở Phần 2, làm ngay các bài tương ứng ở Phần 5.
3. **Luyện đề:** in riêng Phần 3, bấm giờ 90 phút, rồi tự chấm bằng Phần 4 theo đúng thang điểm
   (kể cả quy tắc cho điểm câu đúng/sai).

> **Quy ước trình bày**
> Các công thức đặt trong khung xám. Các hộp **xanh dương** là ghi chú lý thuyết, hộp **xanh lá**
> là ví dụ có lời giải, hộp **vàng** là mẹo làm bài, hộp **đỏ** là lỗi sai thường gặp.
> Kí hiệu vectơ được viết có mũi tên ở trên, ví dụ vectơ AB; kí hiệu độ dài vectơ viết trong
> hai dấu gạch đứng.
"""

# ---------------------------------------------------------------------------
PART1 = """
# PHẦN 1. PHÂN TÍCH MA TRẬN VÀ CẤU TRÚC ĐỀ

## 1.1. Phạm vi kiến thức

Theo mục *I. Mục tiêu* của ma trận gốc, đề kiểm tra **các kiến thức đại số và hình học đến hết
giữa học kì I lớp 10**, gồm 4 chương:

| Chương | Tên chương (theo SGK Kết nối tri thức) | Bài học tương ứng |
|---|---|---|
| Chương 1 | Mệnh đề và tập hợp | Bài 1. Mệnh đề; Bài 2. Tập hợp và các phép toán trên tập hợp |
| Chương 2 | Bất phương trình và hệ bất phương trình bậc nhất hai ẩn | Bài 3. Bất phương trình bậc nhất hai ẩn; Bài 4. Hệ bất phương trình bậc nhất hai ẩn |
| Chương 3 | Hệ thức lượng trong tam giác | Bài 5. Giá trị lượng giác của một góc từ 0° đến 180°; Bài 6. Hệ thức lượng trong tam giác |
| Chương 4 | Vectơ | Bài 7. Các khái niệm mở đầu (ma trận ghi là "Khái niệm vectơ") |

Ma trận gốc cũng nêu rõ các **kĩ năng** cần thành thạo: nhận biết và xét tính đúng/sai của mệnh
đề; phủ định của mệnh đề chứa kí hiệu "với mọi" và "tồn tại"; điều kiện cần – đủ; các phép toán
trên tập hợp; biểu diễn miền nghiệm của bất phương trình và hệ bất phương trình bậc nhất hai ẩn;
giá trị lượng giác của góc từ 0° đến 180°; định lí sin, định lí côsin, công thức diện tích tam
giác và giải tam giác; các khái niệm về vectơ, độ dài vectơ, hai vectơ cùng phương – cùng hướng –
bằng nhau – đối nhau, vectơ-không.

## 1.2. Cấu trúc đề kiểm tra và cách tính điểm

| Phần | Số câu | Điểm | Ghi chú |
|---|---|---|---|
| I. Trắc nghiệm nhiều phương án lựa chọn | 12 câu | 3,0 | Mỗi câu 0,25 điểm; chọn 1 phương án đúng |
| II. Trắc nghiệm đúng – sai | 2 câu (8 ý) | 2,0 | Mỗi câu 4 ý a, b, c, d |
| III. Trắc nghiệm trả lời ngắn | 4 câu | 2,0 | Mỗi câu 0,5 điểm |
| IV. Tự luận | 3 câu | 3,0 | Mỗi câu 1,0 điểm |
| **Tổng** | **24 lệnh hỏi TN + 3 câu TL** | **10,0** | **Thời gian làm bài: 90 phút** |

! **Quy tắc cho điểm câu đúng – sai (rất dễ mất điểm oan)**
> Trong **mỗi câu** đúng/sai, điểm được tính theo **số ý trả lời đúng**:
> đúng **1 ý = 0,1 điểm**; đúng **2 ý = 0,25 điểm**; đúng **3 ý = 0,5 điểm**; đúng **cả 4 ý = 1,0
> điểm**. Sai ý nào không bị trừ điểm của ý khác, nhưng **chỉ khi đúng cả 4 ý mới được trọn 1,0
> điểm**. Vì thế: ý nào chưa chắc chắn vẫn nên chọn, nhưng phải ưu tiên thời gian cho các ý đã
> nắm vững.


## 1.3. Ma trận chi tiết (trích từ tệp nguồn)

Kí hiệu: **NB** = nhận biết, **TH** = thông hiểu, **VD** = vận dụng, **VDC** = vận dụng cao.
Mỗi ô ghi "số câu" theo từng loại câu hỏi.

| Đơn vị kiến thức | Chọn PA (NB-TH-VD) | Đúng-sai (NB-TH-VD) | TL ngắn (NB-TH-VD) | Tự luận (TH-VD-VDC) | Số câu TN | Số câu TL | Điểm TN | Điểm TL |
|---|---|---|---|---|---|---|---|---|
| 1.1. Mệnh đề | 2 / – / – | – / – / – | – / – / – | – / – / – | 2 | – | 0,50 | – |
| 1.2. Tập hợp | 1 / – / – | 1 / 1 / – | – / 1 / – | – / – / – | 4 | – | 1,25 | – |
| 1.3. Các phép toán trên tập hợp | 1 / – / – | – / 1 / 1 | – / – / 1 | 1 / – / – | 4 | 1 | 1,25 | 1,0 |
| 2.1. Bất phương trình bậc nhất hai ẩn | 1 / – / – | 1 / 2 / 1 | – / – / – | – / – / – | 5 | – | 1,25 | – |
| 2.2. Hệ bất phương trình bậc nhất hai ẩn | 1 / – / – | – / – / – | – / – / – | – / – / 1 | 1 | 1 | 0,25 | 1,0 |
| 3.1. Giá trị lượng giác của góc 0°–180° | 1 / 1 / – | – / – / – | – / – / 1 | – / – / – | 3 | – | 1,00 | – |
| 3.2. Hệ thức lượng trong tam giác | 1 / 1 / – | – / – / – | – / 1 / – | – / 1 / – | 3 | 1 | 1,00 | 1,0 |
| 4.1. Khái niệm vectơ | 1 / 1 / – | – / – / – | – / – / – | – / – / – | 2 | – | 0,50 | – |
| **Tổng** | **9 / 3 / 0** | **2 / 4 / 2** | **0 / 2 / 2** | **1 / 1 / 1** | **24** | **3** | **7,00** | **3,00** |

## 1.4. Tỉ trọng điểm theo chương

| Chương | Điểm TN | Điểm TL | Tổng điểm | Tỉ lệ |
|---|---|---|---|---|
| Chương 1. Mệnh đề và tập hợp | 3,00 | 1,0 | **4,00** | 40% |
| Chương 2. Bất phương trình và hệ BPT bậc nhất hai ẩn | 1,50 | 1,0 | **2,50** | 25% |
| Chương 3. Hệ thức lượng trong tam giác | 2,00 | 1,0 | **3,00** | 30% |
| Chương 4. Vectơ | 0,50 | – | **0,50** | 5% |
| **Tổng** | **7,00** | **3,00** | **10,00** | 100% |

~ **Kết luận để phân bổ thời gian ôn**
> Chương 1 (Mệnh đề – Tập hợp) chiếm **40%**, Chương 3 (Hệ thức lượng) **30%**, Chương 2 (Bất
> phương trình) **25%**, Chương 4 (Vectơ) chỉ **5%**. Hãy dành thời gian tương ứng: khoảng
> 35% công sức cho Chương 1, 30% cho Chương 3, 25% cho Chương 2 và 10% cho Chương 4.
> Chương 4 chỉ thi 2 câu nhận biết/thông hiểu nên **không được bỏ**, nhưng cũng **không cần đào
> sâu** — chỉ cần nắm chắc định nghĩa và cách xét hai vectơ bằng nhau.


## 1.5. Bảng đặc tả: mỗi câu hỏi kiểm tra điều gì

Đây là bản "đặt hàng" của người ra đề. Ôn đúng các ô này là ôn trúng đề.

| Câu | Đơn vị kiến thức | Mức độ | Yêu cầu cần đạt (theo bảng đặc tả gốc) |
|---|---|---|---|
| Câu 1 (TN) | 1.1 Mệnh đề | NB | Biết thế nào là một mệnh đề, mệnh đề phủ định, mệnh đề chứa biến |
| Câu 2 (TN) | 1.1 Mệnh đề | NB | Biết ý nghĩa kí hiệu phổ biến (với mọi) và kí hiệu tồn tại |
| Câu 3 (TN) | 1.2 Tập hợp | NB | Cho tập hợp bằng cách liệt kê phần tử hoặc chỉ ra tính chất đặc trưng |
| Câu 4 (TN) | 1.3 Phép toán tập hợp | NB | Dùng biểu đồ Ven để biểu diễn giao, hợp của hai tập hợp |
| Câu 5 (TN) | 2.1 BPT bậc nhất hai ẩn | NB | Nhận biết được bất phương trình bậc nhất hai ẩn |
| Câu 6 (TN) | 2.2 Hệ BPT bậc nhất hai ẩn | NB | Nhận biết được hệ bất phương trình bậc nhất hai ẩn |
| Câu 7 (TN) | 3.1 Giá trị lượng giác | NB | Nhận biết GTLG của góc 0°–180°; hệ thức giữa hai góc phụ nhau, bù nhau |
| Câu 8 (TN) | 3.1 Giá trị lượng giác | TH | Tính GTLG của một góc khi biết một trong bốn GTLG của nó |
| Câu 9 (TN) | 3.2 Hệ thức lượng | NB | Nhận biết định lí côsin, định lí sin, công thức tính diện tích tam giác |
| Câu 10 (TN) | 3.2 Hệ thức lượng | TH | Dùng định lí côsin, định lí sin, công thức diện tích để tính cạnh, góc, diện tích |
| Câu 11 (TN) | 4.1 Vectơ | NB | Biết khái niệm vectơ, vectơ-không, độ dài, cùng phương, cùng hướng, bằng nhau |
| Câu 12 (TN) | 4.1 Vectơ | TH | Hiểu đặc điểm các vectơ; chứng minh hai vectơ bằng nhau (trường hợp đơn giản) |
| Câu 1a (ĐS) | 1.2 Tập hợp | NB | Dùng đúng kí hiệu thuộc, tập con; dùng đúng kí hiệu khoảng, đoạn, nửa khoảng |
| Câu 1b (ĐS) | 1.2 Tập hợp | TH | Biểu diễn được các khoảng, đoạn trên trục số |
| Câu 1c (ĐS) | 1.3 Phép toán tập hợp | TH | Thực hiện phép giao, hợp, phần bù của một tập con |
| Câu 1d (ĐS) | 1.3 Phép toán tập hợp | VD | Vận dụng các phép toán tập hợp vào tình huống có yêu cầu cao hơn |
| Câu 2a (ĐS) | 2.1 BPT bậc nhất hai ẩn | NB | Nhận biết nghiệm và miền nghiệm của BPT bậc nhất hai ẩn trên mặt phẳng tọa độ |
| Câu 2b, 2c (ĐS) | 2.1 BPT bậc nhất hai ẩn | TH | Mô tả được miền nghiệm của BPT bậc nhất hai ẩn trên mặt phẳng tọa độ |
| Câu 2d (ĐS) | 2.1 BPT bậc nhất hai ẩn | VD | Chuyển điều kiện của bài toán thực tế về dạng BPT bậc nhất hai ẩn |
| Câu 3 (TLN) | 3.1 Giá trị lượng giác | VD | Cho biết một GTLG, tính giá trị của một biểu thức |
| Câu 4 (TLN) | 3.2 Hệ thức lượng | TH | Dùng hệ thức lượng để tính cạnh, góc, diện tích; ứng dụng thực tiễn đơn giản |
| Câu 1 (TLN) | 1.2 Tập hợp | TH | Tìm số tập hợp con của một tập hợp |
| Câu 2 (TLN) | 1.3 Phép toán tập hợp | VD | Bài toán thực tế về các phép toán tập hợp (sơ đồ Ven) |
| Câu 1 (TL) | 1.3 Phép toán tập hợp | TH | Thực hiện phép giao, hợp, phần bù của một tập con (1,0 điểm) |
| Câu 2 (TL) | 3.2 Hệ thức lượng | VD | Giải bài toán có nội dung thực tiễn bằng hệ thức lượng trong tam giác (1,0 điểm) |
| Câu 3 (TL) | 2.2 Hệ BPT bậc nhất hai ẩn | VDC | Mô tả miền nghiệm của hệ BPT; tìm phương án tối ưu của bài toán thực tế (1,0 điểm) |

## 1.6. Ba câu tự luận được mô tả như thế nào

Ma trận gốc có riêng một mục *Mô tả cụ thể mức độ câu tự luận*:

- **Câu 1** (mức độ 2 – thông hiểu, 1,0 điểm): *Thực hiện được các phép toán giao của hai tập
  hợp, hợp của hai tập hợp, phần bù của một tập con.*
- **Câu 2** (mức độ 2 – thông hiểu, 1,0 điểm): *Vận dụng hệ thức lượng trong tam giác vào việc
  giải một số bài toán có nội dung thực tiễn (mức đơn giản).*
- **Câu 3** (mức độ 3 – vận dụng, 1,0 điểm): *Vận dụng được kiến thức về hệ bất phương trình bậc
  nhất hai ẩn vào giải quyết bài toán thực tiễn.*

> Trong ma trận, câu tự luận về hệ bất phương trình được xếp vào cột **vận dụng cao (VDC)** — đây
> là câu "chốt điểm 9, 10" của đề. Muốn lấy trọn 1,0 điểm phải trình bày đủ ba bước: **đặt ẩn và
> nêu điều kiện → lập hệ bất phương trình → tìm giá trị lớn nhất của biểu thức tại các đỉnh của
> miền nghiệm và kết luận**.

## 1.7. Chiến lược làm bài trong 90 phút

| Mốc thời gian | Việc cần làm | Điểm có thể đạt |
|---|---|---|
| 0 – 5 phút | Đọc lướt toàn đề, đánh dấu câu quen thuộc; ghi nháp các dữ kiện quan trọng | – |
| 5 – 25 phút | Phần I: 12 câu trắc nghiệm (khoảng 1,5 phút/câu). Câu nào quá 2 phút thì đánh dấu bỏ qua | 3,0 |
| 25 – 45 phút | Phần II: 2 câu đúng – sai (8 ý). Làm chắc từng ý, ghi rõ Đúng/Sai vào phiếu | 2,0 |
| 45 – 58 phút | Phần III: 4 câu trả lời ngắn. Chỉ điền kết quả cuối, nhớ làm tròn đúng yêu cầu | 2,0 |
| 58 – 85 phút | Phần IV: 3 câu tự luận. Ưu tiên Câu 1 (tập hợp) vì dễ ăn điểm nhất, rồi Câu 3 (hệ BPT), cuối cùng Câu 2 (thực tiễn) | 3,0 |
| 85 – 90 phút | Rà lại phiếu trả lời, kiểm tra đã tô/ghi đủ 24 lệnh hỏi chưa | – |

~ **Mẹo quản lí thời gian**
> - Trắc nghiệm **không trừ điểm khi sai**, nên tuyệt đối không bỏ trống: hết giờ phải tô đủ 12 câu.
> - Phần trả lời ngắn thường yêu cầu **làm tròn** (hàng phần mười, phần trăm) — đọc kĩ đề, sai quy
>   tắc làm tròn là mất điểm dù phép tính đúng.
> - Tự luận: **viết công thức trước, thay số sau**. Nếu bí, vẫn viết được công thức và được điểm
>   từng bước theo hướng dẫn chấm.

! **Những lỗi mất điểm kinh điển**
> 1. Quên rằng **0 thuộc tập số tự nhiên**; nhầm tập rỗng với tập {0}.
> 2. Khi lấy **phần bù** của khoảng/đoạn: quên "đổi loại móc" — phần bù của [a; b] là
>    (−∞; a) hợp (b; +∞), **không** phải (−∞; a] hợp [b; +∞).
> 3. Biểu diễn miền nghiệm: quên xét **dấu của hệ số b** khi kết luận "nửa mặt phẳng phía trên hay
>    phía dưới"; quên ghi **kể cả biên** hay **không kể biên**.
> 4. Nhầm dấu GTLG của **góc tù**: sin dương nhưng cos, tan, cot đều **âm**.
> 5. Áp định lí côsin nhưng **nhầm cạnh đối diện** góc đang xét.
> 6. Vectơ: quên rằng **vectơ-không cùng phương, cùng hướng với mọi vectơ**; nhầm "cùng phương"
>    với "cùng hướng".
"""

# ---------------------------------------------------------------------------
PART2_CH1 = """
# PHẦN 2. KIẾN THỨC TRỌNG TÂM

> Phần này bám theo 4 chương trong phạm vi kiểm tra. Mỗi đơn vị kiến thức gồm: **lý thuyết cô
> đọng → công thức cần nhớ → ví dụ minh họa có lời giải → bẫy mất điểm**.

## Chương 1. MỆNH ĐỀ VÀ TẬP HỢP

### 1.1. Mệnh đề (Bài 1)

> **Khái niệm**
> - **Mệnh đề** là một khẳng định **hoặc đúng, hoặc sai**, không thể vừa đúng vừa sai. Câu hỏi,
>   câu cảm thán, câu mệnh lệnh **không phải** mệnh đề.
> - **Mệnh đề chứa biến** là câu chứa biến mà khi thay biến bằng giá trị cụ thể thì trở thành một
>   mệnh đề (đúng hoặc sai). Ví dụ "x > 5" là mệnh đề chứa biến.
> - **Mệnh đề phủ định** của mệnh đề P, kí hiệu là P phủ định (viết P có gạch ngang trên đầu),
>   có tính đúng/sai **ngược** với P.

> **Mệnh đề kéo theo, mệnh đề đảo, mệnh đề tương đương**
> - **P kéo theo Q** (viết "nếu P thì Q", kí hiệu P ⇒ Q) chỉ **sai khi P đúng và Q sai**.
> - **Mệnh đề đảo** của P ⇒ Q là Q ⇒ P. Mệnh đề đảo **không nhất thiết** đúng khi mệnh đề ban đầu
>   đúng.
> - Khi cả P ⇒ Q và Q ⇒ P đều đúng, ta có **mệnh đề tương đương** P ⇔ Q, đọc là "P khi và chỉ khi
>   Q", "P là điều kiện cần và đủ của Q".
> - P là **điều kiện đủ** của Q nếu P ⇒ Q; P là **điều kiện cần** của Q nếu Q ⇒ P.

= P ⇒ Q chỉ sai khi P đúng và Q sai     |     P ⇔ Q đúng khi P và Q cùng tính đúng/sai

> **Kí hiệu "với mọi" và "tồn tại" — và cách phủ định**
> - Kí hiệu ∀ đọc là "với mọi"; kí hiệu ∃ đọc là "tồn tại" (có ít nhất một).
> - **Quy tắc phủ định: đổi kí hiệu, phủ định vị ngữ.**

= Phủ định của "∀x ∈ X, P(x)"  là  "∃x ∈ X, P(x) sai"
= Phủ định của "∃x ∈ X, P(x)"  là  "∀x ∈ X, P(x) sai"

Bảng ghi nhớ cách phủ định các quan hệ:

| Mệnh đề | Phủ định |
|---|---|
| a = b | a ≠ b |
| a > b | a ≤ b |
| a ≥ b | a < b |
| a < b | a ≥ b |
| a ≤ b | a > b |

~ **Ví dụ 1** (dạng Câu 2 trong đề)
> Phủ định của mệnh đề "∀x ∈ ℝ, x² + 1 > 0" là: đổi ∀ thành ∃, đổi "> 0" thành "≤ 0", ta được
> **"∃x ∈ ℝ, x² + 1 ≤ 0"**. Chú ý phủ định của ">" là "≤" chứ **không phải** "<".

! **Bẫy mất điểm**
> - "x² ≥ 1 với mọi x ∈ ℝ" là mệnh đề **sai** (chọn x = 0), nên mệnh đề phủ định của nó **đúng**.
>   Học sinh hay nhầm: xét tính đúng/sai của mệnh đề phủ định chứ không phải của mệnh đề gốc.
> - Phủ định của "mọi số nguyên tố đều lẻ" là "**tồn tại** một số nguyên tố **không** lẻ" — phải
>   chỉ ra được số 2.

### 1.2. Tập hợp (Bài 2)

> **Hai cách xác định tập hợp**
> 1. **Liệt kê các phần tử**: A = {1; 2; 3}.
> 2. **Chỉ ra tính chất đặc trưng**: A = {x ∈ ℤ | −2 ≤ x < 3}.
> Kí hiệu: x ∈ A (x thuộc A); x ∉ A (x không thuộc A); A ⊂ B (A là tập con của B); A = B khi
> A ⊂ B và B ⊂ A; ∅ là **tập rỗng** (không có phần tử nào).

> **Các tập hợp số thường dùng**
> ℕ* ⊂ ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ, trong đó ℕ* là tập số tự nhiên khác 0, ℕ là tập số tự nhiên (có cả số 0),
> ℤ là tập số nguyên, ℚ là tập số hữu tỉ, ℝ là tập số thực.

> **Khoảng, đoạn, nửa khoảng** (với a < b)

| Kí hiệu | Ý nghĩa | Biểu diễn trên trục số |
|---|---|---|
| (a; b) | a < x < b | khoanh tròn cả a và b |
| [a; b] | a ≤ x ≤ b | tô đậm cả a và b |
| (a; b] | a < x ≤ b | khoanh tròn a, tô đậm b |
| [a; b) | a ≤ x < b | tô đậm a, khoanh tròn b |
| (a; +∞) | x > a | khoanh tròn a, mũi tên sang phải |
| [a; +∞) | x ≥ a | tô đậm a, mũi tên sang phải |
| (−∞; b) | x < b | mũi tên từ trái, khoanh tròn b |
| (−∞; b] | x ≤ b | mũi tên từ trái, tô đậm b |
| (−∞; +∞) | ℝ | cả trục số |

~ **Quy tắc nhớ móc – ngoặc**
> **Ngoặc tròn ( )** ứng với dấu **<** hoặc **>** — đầu mút **không** thuộc tập hợp, vẽ **khoanh
> tròn**. **Ngoặc vuông [ ]** ứng với dấu **≤** hoặc **≥** — đầu mút **có** thuộc tập hợp, vẽ **tô
> đậm**. Vô cực **luôn** đi với ngoặc tròn.

@@hinh:trucso@@
*Hình 1. Biểu diễn A = (−3; 4] (màu xanh dương) và B = [0; +∞) (màu xanh rêu) trên trục số.*

> **Số tập hợp con**
> Một tập hợp có **n** phần tử thì có **2ⁿ** tập hợp con (kể cả tập rỗng và chính nó).

~ **Ví dụ 2** (dạng Câu 1 – trả lời ngắn)
> Cho A = {x ∈ ℤ | x² − 5x + 6 = 0} ∪ {0; 1; 2; 3}. Giải x² − 5x + 6 = 0 được x = 2 và x = 3, suy
> ra tập thứ nhất là {2; 3}. Hợp với {0; 1; 2; 3} ta được A = {0; 1; 2; 3} — có **4 phần tử**.
> Vậy số tập hợp con của A là **2⁴ = 16**.

! **Bẫy mất điểm**
> - Liệt kê tập {x ∈ ℕ | x < 6} phải có **số 0**: {0; 1; 2; 3; 4; 5} — 6 phần tử, không phải 5.
> - Tập {x ∈ ℤ | x² + 1 = 0} là **tập rỗng ∅**, khác với tập {0}.
> - Hai phần tử trùng nhau chỉ viết **một lần**: {1; 2; 2; 3} = {1; 2; 3}.

### 1.3. Các phép toán trên tập hợp (Bài 2)

| Phép toán | Kí hiệu | Định nghĩa |
|---|---|---|
| Giao | A ∩ B | x ∈ A **và** x ∈ B |
| Hợp | A ∪ B | x ∈ A **hoặc** x ∈ B |
| Hiệu | A \\ B | x ∈ A **và** x ∉ B |
| Phần bù của A trong E | E \\ A, hay phần bù của A | x ∈ E **và** x ∉ A |

@@hinh:venn@@
*Hình 2. Biểu đồ Ven: phần tô đậm ở giữa (hình "thấu kính") là giao A ∩ B; toàn bộ hai hình tròn
là hợp A ∪ B.*

= |A ∪ B| = |A| + |B| − |A ∩ B|        (công thức bao hàm – loại trừ)

~ **Ví dụ 3** (dạng Câu 2 – trả lời ngắn)
> Lớp 10A có 40 học sinh; 25 bạn thích bóng đá, 20 bạn thích cầu lông, 12 bạn thích **cả hai**
> môn. Số bạn thích **ít nhất một** môn là 25 + 20 − 12 = 33. Vậy số bạn **không thích môn nào**
> là 40 − 33 = **7** bạn.

~ **Ví dụ 4** (dạng Câu 1 – tự luận)
> Cho A = [−4; 3) và B = (1; 6]. Khi đó:
> - A ∩ B = **(1; 3)** — lấy phần chung, đầu trái theo tập "chặt" hơn, đầu phải cũng vậy.
> - A ∪ B = **[−4; 6]** — gộp lại, đầu nào "rộng" hơn thì giữ.
> - Phần bù của A trong ℝ là **(−∞; −4) ∪ [3; +∞)** — đổi loại móc ở cả hai đầu mút.

! **Bẫy mất điểm**
> - A \\ B **khác** B \\ A. Ví dụ {1;2;3} \\ {2;3;4} = {1}, còn {2;3;4} \\ {1;2;3} = {4}.
> - Khi giao hai khoảng, đầu mút thuộc cả hai tập mới thuộc giao: [0; 5] ∩ (0; 4] = **(0; 4]**.
> - Phần bù của (a; b) là (−∞; **a]** hợp **[b**; +∞): phải **đổi** loại móc.
"""

# ---------------------------------------------------------------------------
PART2_CH2 = """
## Chương 2. BẤT PHƯƠNG TRÌNH VÀ HỆ BẤT PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN

### 2.1. Bất phương trình bậc nhất hai ẩn (Bài 3)

> **Định nghĩa**
> Bất phương trình bậc nhất hai ẩn x, y có dạng tổng quát
> **ax + by ≤ c** (hoặc ax + by ≥ c, ax + by < c, ax + by > c),
> trong đó a, b, c là các số đã cho, **a và b không đồng thời bằng 0**.

> **Nghiệm và miền nghiệm**
> - Mỗi cặp số (x₀; y₀) làm cho bất phương trình đúng gọi là một **nghiệm**.
> - Tập hợp các điểm có tọa độ là nghiệm gọi là **miền nghiệm**. Miền nghiệm của bất phương trình
>   bậc nhất hai ẩn là **một nửa mặt phẳng** bờ là đường thẳng d: ax + by = c.

> **Quy trình biểu diễn miền nghiệm (4 bước — học thuộc lòng)**
> 1. Vẽ đường thẳng **d: ax + by = c**.
> 2. Lấy một **điểm thử** M(x₀; y₀) **không thuộc d** (ưu tiên O(0; 0) nếu O không nằm trên d).
> 3. Thay tọa độ M vào bất phương trình: nếu **đúng** thì nửa mặt phẳng **chứa M** là miền nghiệm;
>    nếu **sai** thì miền nghiệm là nửa mặt phẳng **không chứa M**.
> 4. **Gạch bỏ** nửa mặt phẳng không phải miền nghiệm. Dấu **≤** hoặc **≥** thì **kể cả biên** (vẽ
>    nét liền); dấu **<** hoặc **>** thì **không kể biên** (vẽ nét đứt).

@@hinh:nua_mp@@
*Hình 3. Miền nghiệm của bất phương trình 3x + 2y ≤ 12: nửa mặt phẳng bờ là đường thẳng
3x + 2y = 12 chứa điểm O(0; 0), kể cả biên. Đường thẳng cắt Ox tại A(4; 0) và cắt Oy tại B(0; 6).*

~ **Ví dụ 5** (dạng Câu 2a, 2b trong đề)
> Xét bất phương trình 3x + 2y ≤ 12.
> - Cặp (2; 3): 3·2 + 2·3 = 12 ≤ 12 — **đúng**, vậy (2; 3) là một nghiệm.
> - Cặp (3; 1): 3·3 + 2·1 = 11 ≤ 12 — **đúng**, vậy (3; 1) **thuộc** miền nghiệm.
> - Điểm O(0; 0): 0 ≤ 12 đúng, nên miền nghiệm là nửa mặt phẳng chứa O.

### 2.2. Hệ bất phương trình bậc nhất hai ẩn (Bài 4)

> **Định nghĩa và miền nghiệm**
> Hệ bất phương trình bậc nhất hai ẩn gồm một số bất phương trình bậc nhất hai ẩn. **Nghiệm của hệ**
> là nghiệm chung của tất cả các bất phương trình trong hệ. **Miền nghiệm của hệ** là **giao** các
> miền nghiệm của từng bất phương trình — thường là một **miền đa giác** (có thể kể cả biên).

> **Bài toán tìm giá trị lớn nhất / nhỏ nhất**
> Cho biểu thức **F(x; y) = ax + by**. Trên một **miền đa giác lồi** (kể cả biên), F đạt giá trị
> lớn nhất và nhỏ nhất **tại một trong các đỉnh** của miền. Quy trình:
> 1. Vẽ miền nghiệm, xác định **các đỉnh** (giải hệ phương trình của hai đường thẳng cắt nhau).
> 2. Tính giá trị của F **tại từng đỉnh**.
> 3. So sánh: giá trị lớn nhất là kết quả, giá trị nhỏ nhất là kết quả.

@@hinh:mien_he@@
*Hình 4. Miền nghiệm của hệ { x ≥ 0; y ≥ 0; 4x + 3y ≤ 48; 2x + 3y ≤ 36 } là tứ giác có bốn đỉnh
O(0; 0), (12; 0), (6; 8), (0; 12). Đây chính là bài toán tự luận Câu 3.*

~ **Ví dụ 6** (bài toán tối ưu — đúng dạng Câu 3 tự luận)
> Tìm giá trị lớn nhất của F = 3x + 2y trên miền nghiệm của hệ
> { x ≥ 0; y ≥ 0; x + y ≤ 6; 2x + y ≤ 8 }.
> Bốn đỉnh của miền: O(0; 0), A(4; 0) (từ 2x + y = 8 và y = 0), B(2; 4) (giao của x + y = 6 và
> 2x + y = 8), C(0; 6) (từ x + y = 6 và x = 0).
> F(O) = 0; F(A) = 12; F(B) = 3·2 + 2·4 = **14**; F(C) = 12.
> Vậy **giá trị lớn nhất là 14, đạt tại (x; y) = (2; 4)**.

> **Quy trình giải bài toán thực tiễn bằng hệ bất phương trình (5 bước)**
> 1. **Chọn ẩn**: gọi x, y là số lượng cần tìm, **nêu rõ đơn vị** và **điều kiện** (thường là
>    x ≥ 0, y ≥ 0; nếu là số sản phẩm thì x, y nguyên).
> 2. **Biểu diễn các đại lượng** khác theo x, y.
> 3. **Lập hệ bất phương trình** từ các ràng buộc của đề bài (nguyên liệu, thời gian, vốn...).
> 4. **Lập biểu thức cần tối ưu** F(x; y) (tiền lãi, chi phí...).
> 5. **Tìm các đỉnh của miền nghiệm**, tính F tại từng đỉnh, so sánh và **kết luận theo câu hỏi
>    của đề** (sản xuất bao nhiêu mỗi loại, giá trị lớn nhất là bao nhiêu).

! **Bẫy mất điểm**
> - Quên điều kiện **x ≥ 0, y ≥ 0** khi ẩn là số lượng — miền nghiệm sẽ sai hoàn toàn.
> - Nhầm chiều bất phương trình khi chuyển điều kiện thực tế: "tối đa 48 giờ" là **≤ 48**, "ít nhất
>   10 tấn" là **≥ 10**.
> - Chỉ tìm giao của hai đường thẳng mà **quên các đỉnh nằm trên trục tọa độ** (O, giao với Ox,
>   giao với Oy).
> - Kết luận thiếu: phải nói rõ **tại đỉnh nào** thì F đạt giá trị lớn nhất.
"""

# ---------------------------------------------------------------------------
PART2_CH3 = """
## Chương 3. HỆ THỨC LƯỢNG TRONG TAM GIÁC

### 3.1. Giá trị lượng giác của một góc từ 0° đến 180° (Bài 5)

> **Nửa đường tròn đơn vị**
> Trong mặt phẳng tọa độ Oxy, nửa đường tròn tâm O, bán kính R = 1, nằm phía trên trục hoành gọi là
> **nửa đường tròn đơn vị**. Với mỗi góc α (0° ≤ α ≤ 180°), xác định **duy nhất** điểm M trên nửa
> đường tròn sao cho góc MOx = α. Nếu M có tọa độ (x₀; y₀) thì:

= sin α = y₀      cos α = x₀      tan α = y₀/x₀ (x₀ ≠ 0)      cot α = x₀/y₀ (y₀ ≠ 0)

@@hinh:duong_tron@@
*Hình 5. Nửa đường tròn đơn vị. Với góc α, điểm M(cos α; sin α) cho ta đồng thời cả bốn giá trị
lượng giác. Vì M luôn nằm phía trên trục hoành nên sin α luôn không âm.*

> **Bảng giá trị lượng giác của các góc đặc biệt**

| Góc α | 0° | 30° | 45° | 60° | 90° | 120° | 135° | 150° | 180° |
|---|---|---|---|---|---|---|---|---|---|
| sin α | 0 | 1/2 | √2/2 | √3/2 | 1 | √3/2 | √2/2 | 1/2 | 0 |
| cos α | 1 | √3/2 | √2/2 | 1/2 | 0 | −1/2 | −√2/2 | −√3/2 | −1 |
| tan α | 0 | √3/3 | 1 | √3 | không xác định | −√3 | −1 | −√3/3 | 0 |
| cot α | không xác định | √3 | 1 | √3/3 | 0 | −√3/3 | −1 | −√3 | không xác định |

> **Dấu của các giá trị lượng giác**

| Loại góc | sin α | cos α | tan α | cot α |
|---|---|---|---|---|
| α nhọn (0° < α < 90°) | + | + | + | + |
| α = 90° | + | 0 | không xác định | 0 |
| α tù (90° < α < 180°) | + | − | − | − |

> **Quan hệ giữa hai góc bù nhau** (α và 180° − α)

= sin(180° − α) = sin α        cos(180° − α) = −cos α
= tan(180° − α) = −tan α       cot(180° − α) = −cot α

> **Các hệ thức cơ bản** (điều kiện để biểu thức có nghĩa)

= sin²α + cos²α = 1
= tan α = sin α / cos α  (α ≠ 90°)          cot α = cos α / sin α  (α ≠ 0° và α ≠ 180°)
= tan α · cot α = 1                          1 + tan²α = 1/cos²α       1 + cot²α = 1/sin²α

> **Hai góc phụ nhau** (α + β = 90°): sin α = cos β; cos α = sin β; tan α = cot β; cot α = tan β.

~ **Ví dụ 7** (dạng Câu 8 trong đề)
> Cho 90° < α < 180° và sin α = 3/5. Từ sin²α + cos²α = 1 suy ra cos²α = 1 − 9/25 = 16/25, nên
> cos α = ±4/5. Vì α là **góc tù** nên cos α < 0, vậy **cos α = −4/5**.
> Từ đó tan α = sin α / cos α = −3/4 và cot α = −4/3.

~ **Ví dụ 8** (dạng Câu 3 – trả lời ngắn)
> Cho 90° < α < 180° và tan α = −2. Tính P = (2 sin α − 3 cos α) / (sin α + cos α).
> Từ 1 + tan²α = 1/cos²α suy ra cos²α = 1/5. Vì α tù nên cos α = −1/√5, và
> sin α = tan α · cos α = 2/√5. Thay vào:
> P = (2·2/√5 + 3/√5) / (2/√5 − 1/√5) = (7/√5) / (1/√5) = **7**.
> **Cách nhanh hơn**: chia cả tử và mẫu cho cos α ta được P = (2 tan α − 3)/(tan α + 1) =
> (−4 − 3)/(−2 + 1) = **7**.

! **Bẫy mất điểm**
> - Quên **xét dấu** khi khai căn: biết sin α thì có **hai** giá trị của cos α; phải dựa vào việc α
>   nhọn hay tù để chọn dấu.
> - tan 90° và cot 0°, cot 180° **không xác định** — không được viết bằng 0.
> - sin(180° − α) = sin α nhưng cos(180° − α) = **−**cos α: dấu trừ rất dễ quên.

### 3.2. Hệ thức lượng trong tam giác (Bài 6)

> **Định lí côsin.** Với tam giác ABC có BC = a, CA = b, AB = c:

= a² = b² + c² − 2bc·cos A      b² = a² + c² − 2ac·cos B      c² = a² + b² − 2ab·cos C
= cos A = (b² + c² − a²) / (2bc)     (và tương tự cho cos B, cos C)

> **Định lí sin.** Với R là bán kính đường tròn ngoại tiếp tam giác ABC:

= a / sin A = b / sin B = c / sin C = 2R

> **Công thức tính diện tích tam giác** (p = (a + b + c)/2 là nửa chu vi, r và R là bán kính đường
> tròn nội tiếp và ngoại tiếp, hₐ là đường cao ứng với cạnh a)

= S = (1/2)·a·hₐ = (1/2)·b·c·sin A = (1/2)·c·a·sin B = (1/2)·a·b·sin C
= S = a·b·c / (4R)      S = p·r      S = √(p(p − a)(p − b)(p − c))   (công thức Hê-rông)

> **Công thức đường trung tuyến** (mₐ, m_b, m_c là độ dài các đường trung tuyến ứng với a, b, c)

= mₐ² = (2b² + 2c² − a²)/4      m_b² = (2a² + 2c² − b²)/4      m_c² = (2a² + 2b² − c²)/4

> **Hệ quả — tam giác vuông.** Nếu A = 90° thì cos A = 0, định lí côsin trở thành định lí
> Pi-ta-go: a² = b² + c². Ngược lại, a² < b² + c² thì A nhọn; a² > b² + c² thì A tù.

> **Giải tam giác** là tìm các cạnh và các góc chưa biết khi biết một số yếu tố. Thứ tự nên dùng:
> 1. Biết **hai cạnh và góc xen giữa** → dùng **định lí côsin** tìm cạnh thứ ba.
> 2. Biết **một cạnh và hai góc** → góc thứ ba bằng 180° trừ hai góc kia, rồi dùng **định lí sin**.
> 3. Biết **ba cạnh** → dùng cos A = (b² + c² − a²)/(2bc) để tìm các góc.
> Luôn kiểm tra **tổng ba góc bằng 180°** và **tổng hai cạnh lớn hơn cạnh còn lại**.

~ **Ví dụ 9** (định lí côsin — dạng Câu 10)
> Tam giác ABC có b = 5, c = 8, góc A = 60°. Ta có
> a² = 25 + 64 − 2·5·8·cos 60° = 89 − 80·(1/2) = 89 − 40 = 49, suy ra **a = 7**.
> Đường trung tuyến ứng với cạnh a: mₐ² = (2·25 + 2·64 − 49)/4 = 129/4, nên mₐ = √129/2 ≈ 5,68.

~ **Ví dụ 10** (định lí sin)
> Tam giác ABC có a = 6 và góc A = 60°. Bán kính đường tròn ngoại tiếp:
> 2R = a / sin A = 6 / (√3/2) = 4√3, suy ra **R = 2√3**.

~ **Ví dụ 11** (công thức Hê-rông)
> Tam giác có a = 13, b = 14, c = 15. Nửa chu vi p = 21.
> S = √(21·8·7·6) = √7056 = **84**. Bán kính đường tròn nội tiếp r = S/p = 84/21 = **4**.
> Bán kính đường tròn ngoại tiếp R = abc/(4S) = (13·14·15)/(4·84) = 2730/336 = **65/8 = 8,125**.

> **Ứng dụng thực tế — hai mô hình kinh điển**
> **Mô hình 1 (đo chiều cao khi đứng được dưới chân vật).** Đứng cách chân vật một khoảng d, đo
> góc nâng α. Chiều cao h = d·tan α (bỏ qua chiều cao của dụng cụ đo).
> **Mô hình 2 (không đến được chân vật — có vật cản).** Chọn hai điểm A, B thẳng hàng với chân vật
> C (B nằm giữa A và C), biết AB, đo hai góc nâng α tại A và β tại B.
> - Trong tam giác ABD (D là đỉnh vật): góc ADB = 180° − α − (180° − β) = **β − α**.
> - Định lí sin: BD / sin α = AB / sin(β − α), suy ra BD = AB·sin α / sin(β − α).
> - Chiều cao **h = CD = BD·sin β**.
> - Công thức gọn (dùng cot): **h = AB / (cot α − cot β)**.

@@hinh:do_thap@@
*Hình 6. Mô hình đo chiều cao ngọn tháp khi không thể đến gần chân tháp. Biết AB = 24 m,
góc nâng tại A là 35°, tại B là 50°. Góc ADB = 50° − 35° = 15°.*

~ **Ví dụ 12** (dạng Câu 2 – tự luận)
> Với AB = 24 m, α = 35°, β = 50°: góc ADB = 15°.
> BD = 24·sin 35° / sin 15° ≈ 24·0,5736 / 0,2588 ≈ 53,187 m.
> Chiều cao tháp h = CD = BD·sin 50° ≈ 53,187·0,7660 ≈ **40,7 m**.
> Kiểm tra bằng công thức cot: h = 24 / (cot 35° − cot 50°) = 24 / (1,4281 − 0,8391) ≈ 40,7 m. ✓

! **Bẫy mất điểm**
> - Định lí côsin: **a là cạnh đối diện góc A**. Nhầm thứ tự a, b, c là sai toàn bộ.
> - Định lí sin cho **a/sin A = 2R**, không phải R. Rất nhiều học sinh quên hệ số 2.
> - Máy tính cầm tay phải ở **chế độ độ (D)**, không phải ra-đi-an (R).
> - Bài toán thực tế phải **kết luận kèm đơn vị** và **làm tròn theo yêu cầu**.
"""

# ---------------------------------------------------------------------------
PART2_CH4 = """
## Chương 4. VECTƠ

### 4.1. Các khái niệm mở đầu (Bài 7)

> **Vectơ là gì**
> **Vectơ** là một đoạn thẳng **có hướng**, tức là đã chỉ rõ điểm đầu và điểm cuối. Kí hiệu vectơ
> có điểm đầu A, điểm cuối B là vectơ AB (mũi tên từ A đến B). Vectơ còn được kí hiệu bằng một chữ
> thường có mũi tên, ví dụ vectơ a.
> **Độ dài** của vectơ AB là khoảng cách giữa A và B, kí hiệu |vectơ AB|. Vectơ có độ dài bằng 1 gọi
> là **vectơ đơn vị**.

> **Vectơ-không**
> Vectơ có điểm đầu **trùng** điểm cuối gọi là **vectơ-không**, kí hiệu là vectơ 0. Vectơ-không có
> độ dài bằng 0, **cùng phương và cùng hướng với mọi vectơ**. Quy ước: vectơ AA = vectơ BB = vectơ 0.

> **Giá của vectơ — hai vectơ cùng phương**
> Đường thẳng đi qua điểm đầu và điểm cuối của một vectơ gọi là **giá** của vectơ đó.
> Hai vectơ **cùng phương** nếu giá của chúng **song song hoặc trùng nhau**.
> Hai vectơ cùng phương thì hoặc **cùng hướng**, hoặc **ngược hướng**.

> **Hai vectơ bằng nhau, đối nhau**

= Vectơ a = vectơ b  ⇔  cùng hướng  và  cùng độ dài
= Vectơ đối của vectơ a là vectơ −a:  ngược hướng với a và có cùng độ dài với a
= |vectơ a| = |vectơ −a| ;  vectơ a + (−vectơ a) = vectơ 0

! **Điều kiện để hai vectơ bằng nhau — rất hay bị hỏi**
> Hai vectơ bằng nhau **không phụ thuộc vị trí**: chúng có thể nằm ở hai chỗ khác nhau trên hình
> vẽ. Chỉ cần **cùng hướng** (giá song song hoặc trùng nhau, hai mũi tên chỉ cùng chiều) và **cùng
> độ dài**. Vì thế trong hình bình hành ABCD (các đỉnh theo thứ tự A, B, C, D):
> **vectơ AB = vectơ DC** và **vectơ AD = vectơ BC**; còn **vectơ AD = −vectơ CB**.

@@hinh:vecto@@
*Hình 7. Hình bình hành ABCD tâm O. Hai vectơ màu xanh dương (AB và DC) bằng nhau. Hai vectơ màu
đỏ (AD và CB) ngược hướng và cùng độ dài, nên là hai vectơ đối nhau.*

> **Các tính chất và hệ thức vectơ cơ bản cần nhớ**

| Tình huống | Hệ thức |
|---|---|
| M là trung điểm của AB | vectơ MA + vectơ MB = vectơ 0; độ dài MA = độ dài MB |
| M là trung điểm của AB, O bất kì | vectơ OA + vectơ OB = 2·vectơ OM |
| G là trọng tâm tam giác ABC | vectơ GA + vectơ GB + vectơ GC = vectơ 0 |
| G là trọng tâm, O bất kì | vectơ OA + vectơ OB + vectơ OC = 3·vectơ OG |
| Quy tắc ba điểm | vectơ AB + vectơ BC = vectơ AC |
| Quy tắc hình bình hành | vectơ AB + vectơ AD = vectơ AC (ABCD là hình bình hành) |
| Vectơ-không | vectơ a + vectơ 0 = vectơ a; vectơ a − vectơ a = vectơ 0 |

~ **Ví dụ 13** (dạng Câu 11, 12 trong đề)
> Cho hình bình hành ABCD tâm O. Xét bốn khẳng định:
> (A) vectơ AB = vectơ DC — **đúng** (cùng hướng, cùng độ dài).
> (B) vectơ OA = vectơ CO — **đúng**: O là trung điểm AC nên OA và CO cùng hướng (hướng C đến A)
> và cùng độ dài (bằng nửa AC).
> (C) vectơ AD = vectơ CB — **sai**: trong hình bình hành vectơ AD = vectơ BC, còn vectơ CB ngược
> hướng với vectơ AD. Đúng ra là vectơ AD = −vectơ CB.
> (D) |vectơ AB| = |vectơ CD| — **đúng** (hai cạnh đối của hình bình hành bằng nhau).

~ **Ví dụ 14** (chứng minh hai vectơ bằng nhau)
> Cho tam giác ABC, M và N lần lượt là trung điểm của AB và AC. Vì MN là **đường trung bình** của
> tam giác nên MN song song với BC và MN = BC/2. Hai vectơ MN và BC **cùng hướng**, nhưng độ dài
> khác nhau nên **không bằng nhau**. Ta chỉ có: vectơ MN = (1/2)·vectơ BC.
> Ngược lại, nếu I là trung điểm của BC thì **vectơ MI = vectơ NC** — kiểm tra: MI song song và
> cùng hướng với AC, độ dài MI = AC/2 = NC. ✓

! **Bẫy mất điểm**
> - Nhầm **cùng phương** với **cùng hướng**: hai vectơ cùng phương có thể **ngược hướng** nhau.
> - Quên **vectơ-không cùng phương và cùng hướng với mọi vectơ** — đây là một câu nhận biết kinh điển.
> - Hai vectơ bằng nhau **không cần chung điểm đầu**. Đừng chỉ nhìn vào hình vẽ để kết luận.
> - Đếm số vectơ: với n điểm phân biệt, số vectơ khác vectơ-không có điểm đầu và điểm cuối là các
>   điểm đó là **n(n − 1)**. Với tam giác (3 đỉnh) là 3·2 = **6 vectơ**.
"""

# ---------------------------------------------------------------------------
PART3 = """
# PHẦN 3. ĐỀ KIỂM TRA MINH HỌA

> **ĐỀ KIỂM TRA ĐÁNH GIÁ GIỮA HỌC KÌ I — NĂM HỌC 2026–2027**
> Môn: **TOÁN** – Lớp: **10** – Thời gian làm bài: **90 phút** (không kể thời gian phát đề)
> Đề gồm 4 phần, 24 lệnh hỏi trắc nghiệm và 3 câu tự luận. Đề được biên soạn bám sát 100% ma trận
> và bảng đặc tả của Tổ Toán–Tin.

## PHẦN I. CÂU TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN (12 câu – 3,0 điểm)

*Thí sinh trả lời từ Câu 1 đến Câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án đúng.*

**Câu 1.** *(NB – 1.1 Mệnh đề)* Trong các câu sau, câu nào là một mệnh đề?
- **A.** x + 2 = 5.
- **B.** Hà Nội là thủ đô của nước Cộng hòa Xã hội Chủ nghĩa Việt Nam.
- **C.** Bây giờ là mấy giờ?
- **D.** Chúc các em làm bài thật tốt!

**Câu 2.** *(NB – 1.1 Mệnh đề)* Mệnh đề phủ định của mệnh đề "∀x ∈ ℝ, x² + 1 > 0" là
- **A.** "∃x ∈ ℝ, x² + 1 ≤ 0".
- **B.** "∀x ∈ ℝ, x² + 1 ≤ 0".
- **C.** "∃x ∈ ℝ, x² + 1 < 0".
- **D.** "∃x ∈ ℝ, x² + 1 > 0".

**Câu 3.** *(NB – 1.2 Tập hợp)* Viết tập hợp A = {x ∈ ℤ | −2 ≤ x < 3} bằng cách liệt kê các phần
tử, ta được
- **A.** A = {−2; −1; 0; 1; 2; 3}.
- **B.** A = {−2; −1; 0; 1; 2}.
- **C.** A = {−1; 0; 1; 2}.
- **D.** A = {−2; −1; 0; 1; 2; 3; 4; ...}.

**Câu 4.** *(NB – 1.3 Phép toán tập hợp)* Cho sơ đồ Ven biểu diễn hai tập hợp A và B như hình bên,
trong đó phần được tô đậm là phần nằm trong cả hai hình tròn. Phần tô đậm biểu diễn tập hợp nào
sau đây?
- **A.** A ∪ B.
- **B.** A ∩ B.
- **C.** A \\ B.
- **D.** B \\ A.

@@hinh:venn@@
*Hình của Câu 4.*

**Câu 5.** *(NB – 2.1 Bất phương trình bậc nhất hai ẩn)* Bất phương trình nào sau đây là bất phương
trình bậc nhất hai ẩn?
- **A.** x² + y ≤ 3.
- **B.** 2x − 3y > 5.
- **C.** x + y² ≥ 1.
- **D.** 3x + 2 > 0.

**Câu 6.** *(NB – 2.2 Hệ bất phương trình bậc nhất hai ẩn)* Hệ bất phương trình nào sau đây là hệ
bất phương trình bậc nhất hai ẩn?
- **A.** { x + y ≤ 2 ; 2x − y ≥ 1 }
- **B.** { x² + y ≤ 2 ; x ≥ 0 }
- **C.** { xy ≥ 1 ; x + y ≤ 4 }
- **D.** { x² ≤ 4 ; y > 1 }

**Câu 7.** *(NB – 3.1 Giá trị lượng giác)* Với mọi góc α thỏa mãn 0° ≤ α ≤ 180°, đẳng thức nào sau
đây **đúng**?
- **A.** sin(180° − α) = −sin α.
- **B.** cos(180° − α) = cos α.
- **C.** sin(180° − α) = sin α.
- **D.** tan(180° − α) = tan α.

**Câu 8.** *(TH – 3.1 Giá trị lượng giác)* Cho góc α thỏa mãn 90° < α < 180° và sin α = 3/5. Giá trị
của cos α bằng
- **A.** 4/5.
- **B.** −4/5.
- **C.** 3/4.
- **D.** −3/4.

**Câu 9.** *(NB – 3.2 Hệ thức lượng trong tam giác)* Cho tam giác ABC có BC = a, CA = b, AB = c và
R là bán kính đường tròn ngoại tiếp tam giác. Đẳng thức nào sau đây đúng?
- **A.** a / sin A = R.
- **B.** a / sin A = 2R.
- **C.** a / sin A = R/2.
- **D.** a·sin A = 2R.

**Câu 10.** *(TH – 3.2 Hệ thức lượng trong tam giác)* Cho tam giác ABC có AB = 8 cm, AC = 5 cm và
góc A = 60°. Diện tích của tam giác ABC bằng
- **A.** 10√3 cm².
- **B.** 20√3 cm².
- **C.** 10 cm².
- **D.** 20 cm².

**Câu 11.** *(NB – 4.1 Vectơ)* Cho hình bình hành ABCD (các đỉnh theo thứ tự A, B, C, D). Khẳng
định nào sau đây đúng?
- **A.** vectơ AB = vectơ DC.
- **B.** vectơ AB = vectơ CD.
- **C.** vectơ AB = vectơ BC.
- **D.** vectơ AB = vectơ CB.

**Câu 12.** *(TH – 4.1 Vectơ)* Cho hình bình hành ABCD có tâm O. Trong các khẳng định sau, khẳng
định nào **sai**?
- **A.** vectơ AB = vectơ DC.
- **B.** vectơ OA = vectơ CO.
- **C.** vectơ AD = vectơ CB.
- **D.** |vectơ AB| = |vectơ CD|.

## PHẦN II. CÂU TRẮC NGHIỆM ĐÚNG – SAI (2 câu – 2,0 điểm)

*Thí sinh trả lời từ Câu 1 đến Câu 2. Ở mỗi câu, thí sinh chọn Đúng hoặc Sai cho mỗi ý a), b), c),
d). Điểm mỗi câu: đúng 1 ý = 0,1; đúng 2 ý = 0,25; đúng 3 ý = 0,5; đúng 4 ý = 1,0.*

**Câu 1.** *(1.2 – 1.3 Tập hợp và các phép toán trên tập hợp)* Cho hai tập hợp
A = (−3; 4] và B = [0; +∞).
- **a)** Số 4 là một phần tử của tập A và số −3 **không** là phần tử của tập A.
- **b)** Trên trục số, tập A được biểu diễn bởi phần tô đậm từ −3 đến 4, trong đó điểm −3 được
  khoanh tròn còn điểm 4 được tô đậm.
- **c)** A ∩ B = (0; 4].
- **d)** Tập hợp (A \\ B) ∩ ℤ có đúng 2 phần tử.

**Câu 2.** *(2.1 Bất phương trình bậc nhất hai ẩn)* Trong mặt phẳng tọa độ Oxy, xét bất phương
trình 3x + 2y ≤ 12  (*)  và hệ bất phương trình
(S): { 3x + 2y ≤ 12 ; x ≥ 0 ; y ≥ 0 }.
- **a)** Cặp số (2; 3) là một nghiệm của (*) và điểm (3; 1) **không** thuộc miền nghiệm của (*).
- **b)** Miền nghiệm của (*) là nửa mặt phẳng bờ là đường thẳng d: 3x + 2y = 12, chứa điểm
  O(0; 0), kể cả các điểm nằm trên d.
- **c)** Miền nghiệm của hệ (S) là tam giác OAB với A(4; 0), B(0; 6), kể cả ba cạnh của tam giác.
- **d)** Một phân xưởng có tối đa 12 kg nguyên liệu. Biết mỗi sản phẩm loại I cần 3 kg và mỗi sản
  phẩm loại II cần 2 kg nguyên liệu. Nếu x, y lần lượt là số sản phẩm loại I và loại II được sản
  xuất thì điều kiện về nguyên liệu là 3x + 2y ≥ 12.

## PHẦN III. CÂU TRẮC NGHIỆM TRẢ LỜI NGẮN (4 câu – 2,0 điểm)

*Thí sinh trả lời từ Câu 1 đến Câu 4. Mỗi câu 0,5 điểm.*

**Câu 1.** *(TH – 1.2 Tập hợp)* Cho tập hợp A = {x ∈ ℤ | x² − 5x + 6 = 0} ∪ {0; 1; 2; 3}. Số tập
hợp con của A bằng bao nhiêu?

**Câu 2.** *(VD – 1.3 Các phép toán trên tập hợp)* Lớp 10A có 40 học sinh. Trong đó có 25 bạn
thích môn Bóng đá, 20 bạn thích môn Cầu lông và 12 bạn thích **cả hai** môn. Hỏi lớp 10A có bao
nhiêu bạn **không thích** cả hai môn trên?

**Câu 3.** *(VD – 3.1 Giá trị lượng giác)* Cho góc α thỏa mãn 90° < α < 180° và tan α = −2. Tính giá
trị của biểu thức P = (2 sin α − 3 cos α) / (sin α + cos α).

**Câu 4.** *(TH – 3.2 Hệ thức lượng trong tam giác)* Một người đứng cách chân một cột cờ 20 m và
nhìn thấy đỉnh cột cờ với góc nâng 55°. Bỏ qua chiều cao của người quan sát và dụng cụ đo, hãy
tính chiều cao của cột cờ (đơn vị mét), **làm tròn kết quả đến hàng phần mười**.

## PHẦN IV. TỰ LUẬN (3 câu – 3,0 điểm)

**Câu 1.** *(1,0 điểm – 1.3 Các phép toán trên tập hợp)* Cho hai tập hợp
A = {x ∈ ℝ | −4 ≤ x < 3} và B = (1; 6].
a) Viết tập A dưới dạng khoảng hoặc đoạn và biểu diễn A, B trên trục số.
b) Tìm A ∩ B và A ∪ B.
c) Tìm phần bù của A trong tập số thực ℝ.

**Câu 2.** *(1,0 điểm – 3.2 Hệ thức lượng trong tam giác)* Để đo chiều cao CD của một ngọn tháp
(C là chân tháp, D là đỉnh tháp), người ta chọn hai điểm A, B trên mặt đất sao cho ba điểm A, B, C
thẳng hàng và B nằm giữa A và C, biết AB = 24 m. Tại A và B, người ta đo được góc nâng tới đỉnh
tháp lần lượt là 35° và 50°. Tính chiều cao của ngọn tháp, **làm tròn kết quả đến hàng phần mười**
(đơn vị mét). Bỏ qua chiều cao của dụng cụ đo.

@@hinh:do_thap@@
*Hình minh họa Câu 2 tự luận.*

**Câu 3.** *(1,0 điểm – 2.2 Hệ bất phương trình bậc nhất hai ẩn)* Một xưởng mộc sản xuất hai loại
bàn: bàn loại I và bàn loại II. Để sản xuất một chiếc bàn loại I cần 4 giờ công và 2 m² gỗ; để sản
xuất một chiếc bàn loại II cần 3 giờ công và 3 m² gỗ. Mỗi ngày, xưởng có tối đa 48 giờ công và
36 m² gỗ. Tiền lãi thu được khi bán một chiếc bàn loại I là 500 nghìn đồng, một chiếc bàn loại II
là 400 nghìn đồng. Hỏi mỗi ngày xưởng cần sản xuất bao nhiêu chiếc bàn mỗi loại để **tổng tiền lãi
lớn nhất**? Tính giá trị lớn nhất đó.
"""

# ---------------------------------------------------------------------------
PART4 = """
# PHẦN 4. ĐÁP ÁN VÀ LỜI GIẢI CHI TIẾT

## 4.1. Bảng đáp án nhanh

**Phần I – Trắc nghiệm nhiều phương án lựa chọn**

| Câu | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Đáp án | B | A | B | B | B | A | C | B | B | A | A | C |

**Phần II – Trắc nghiệm đúng – sai**

| Câu | Ý a | Ý b | Ý c | Ý d | Số ý đúng | Điểm |
|---|---|---|---|---|---|---|
| Câu 1 | Đúng | Đúng | **Sai** | Đúng | 3 | 0,50 |
| Câu 2 | **Sai** | Đúng | Đúng | **Sai** | 2 | 0,25 |

**Phần III – Trắc nghiệm trả lời ngắn**

| Câu | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Đáp án | 16 | 7 | 7 | 28,6 |

**Phần IV – Tự luận:** Câu 1 → A ∩ B = (1; 3), A ∪ B = [−4; 6], phần bù của A là
(−∞; −4) ∪ [3; +∞). Câu 2 → khoảng 40,7 m. Câu 3 → 6 bàn loại I và 8 bàn loại II, tiền lãi lớn nhất
6 200 000 đồng.

## 4.2. Lời giải chi tiết Phần I

**Câu 1 – Đáp án B.** Một mệnh đề phải là khẳng định xác định được tính đúng/sai. Phương án A chứa
biến x nên là **mệnh đề chứa biến**, chưa phải mệnh đề. Phương án C là câu hỏi, D là câu cảm thán —
đều không xác định được đúng/sai. Phương án B là một khẳng định đúng, vậy B là mệnh đề.

**Câu 2 – Đáp án A.** Quy tắc: đổi kí hiệu ∀ thành ∃, đồng thời phủ định vị ngữ. Phủ định của
"x² + 1 > 0" là "x² + 1 ≤ 0". Vậy mệnh đề phủ định là "∃x ∈ ℝ, x² + 1 ≤ 0".
Phương án C sai vì phủ định của ">" là "≤" chứ không phải "<". Phương án B sai vì vẫn giữ ∀.

**Câu 3 – Đáp án B.** Các số nguyên x thỏa −2 ≤ x < 3 là −2, −1, 0, 1, 2 (chú ý −2 **thuộc** tập
hợp vì có dấu "=", còn 3 **không** thuộc vì là dấu "<"). Vậy A = {−2; −1; 0; 1; 2} — 5 phần tử.

**Câu 4 – Đáp án B.** Phần tô đậm nằm trong **cả hai** hình tròn, tức là tập các phần tử vừa thuộc
A vừa thuộc B — đó chính là **giao** A ∩ B. Phần gồm toàn bộ hai hình tròn mới là hợp A ∪ B; phần
thuộc A nhưng không thuộc B là hiệu A \\ B.

**Câu 5 – Đáp án B.** Bất phương trình bậc nhất hai ẩn có dạng ax + by ≤ c (hoặc ≥, <, >) với a, b
không đồng thời bằng 0 và **số mũ của x, y đều bằng 1**.
- A sai vì x² có bậc 2. C sai vì y² có bậc 2. D sai vì **chỉ có một ẩn** x.
- B: 2x − 3y > 5, có a = 2, b = −3, c = 5 — thỏa mãn. ✓

**Câu 6 – Đáp án A.** Hệ bất phương trình bậc nhất hai ẩn là hệ gồm **các** bất phương trình bậc
nhất hai ẩn.
- B sai vì x² + y ≤ 2 có bậc 2. C sai vì xy ≥ 1 có tích hai ẩn (bậc 2). D sai vì x² ≤ 4 có bậc 2.
- A: cả hai bất phương trình x + y ≤ 2 và 2x − y ≥ 1 đều bậc nhất hai ẩn. ✓

**Câu 7 – Đáp án C.** Với hai góc bù nhau: sin(180° − α) = sin α (đúng); cos(180° − α) = −cos α;
tan(180° − α) = −tan α. Vậy chỉ có C đúng.
Kiểm tra nhanh với α = 60°: sin 120° = √3/2 = sin 60° ✓, còn cos 120° = −1/2 ≠ cos 60° = 1/2.

**Câu 8 – Đáp án B.** Từ sin²α + cos²α = 1 suy ra cos²α = 1 − (3/5)² = 1 − 9/25 = 16/25, nên
cos α = 4/5 hoặc cos α = −4/5. Vì 90° < α < 180° (góc tù) nên **cos α < 0**, do đó cos α = **−4/5**.

**Câu 9 – Đáp án B.** Định lí sin: a/sin A = b/sin B = c/sin C = **2R**. Đây là công thức cần nhớ
chính xác — nhiều học sinh quên hệ số 2 và chọn nhầm phương án A.

**Câu 10 – Đáp án A.** Áp dụng S = (1/2)·AB·AC·sin A:
S = (1/2)·8·5·sin 60° = 20·(√3/2) = **10√3** (cm²).
Lưu ý: AB = c = 8, AC = b = 5, và góc A là góc **xen giữa** hai cạnh này.

**Câu 11 – Đáp án A.** Trong hình bình hành ABCD (thứ tự đỉnh A, B, C, D), hai cạnh AB và DC **song
song, bằng nhau và cùng hướng** (mũi tên đều đi từ trái sang phải nếu vẽ theo thứ tự), nên
vectơ AB = vectơ DC.
Vectơ CD ngược hướng với vectơ AB nên vectơ AB = −vectơ CD (B sai). Vectơ BC và vectơ CB không cùng
phương với vectơ AB hoặc ngược hướng (C, D sai).

**Câu 12 – Đáp án C.** Xét từng khẳng định:
- A đúng: vectơ AB = vectơ DC (tính chất hình bình hành).
- B đúng: O là trung điểm của AC nên vectơ OA và vectơ CO cùng hướng (hướng từ C tới A) và cùng độ
  dài (bằng nửa AC), do đó vectơ OA = vectơ CO.
- **C sai**: trong hình bình hành ta có vectơ AD = vectơ BC, còn vectơ CB **ngược hướng** với vectơ
  AD. Đúng ra phải là vectơ AD = −vectơ CB.
- D đúng: AB và CD là hai cạnh đối của hình bình hành nên bằng nhau.

## 4.3. Lời giải chi tiết Phần II

**Câu 1.** A = (−3; 4], B = [0; +∞).
- **a) ĐÚNG.** Tập (−3; 4] gồm các số lớn hơn −3 và nhỏ hơn hoặc bằng 4. Số 4 thuộc A (dấu "=");
  số −3 không thuộc A (dấu "<" ngặt).
- **b) ĐÚNG.** Đầu mút −3 đi với ngoặc tròn nên **khoanh tròn**; đầu mút 4 đi với ngoặc vuông nên
  **tô đậm**.
- **c) SAI.** Giao của hai tập lấy phần chung: A ∩ B gồm các x thỏa x > −3, x ≤ 4, x ≥ 0, tức là
  0 ≤ x ≤ 4. Vậy **A ∩ B = [0; 4]**. Phương án đề bài ghi (0; 4] đã loại mất số 0, trong khi
  0 ∈ A và 0 ∈ B.
- **d) ĐÚNG.** A \\ B = {x | x ∈ A và x ∉ B} = (−3; 4] \\ [0; +∞) = (−3; 0). Các số nguyên thuộc
  (−3; 0) là −2 và −1 — đúng **2 phần tử**.

**Câu 2.** Xét (*) 3x + 2y ≤ 12.
- **a) SAI.** Vế thứ nhất đúng: thay (2; 3) được 3·2 + 2·3 = 12 ≤ 12. Nhưng vế thứ hai sai: thay
  (3; 1) được 3·3 + 2·1 = 11 ≤ 12, nên điểm (3; 1) **có thuộc** miền nghiệm của (*). Một ý sai làm
  cả mệnh đề sai.
- **b) ĐÚNG.** Đường thẳng d: 3x + 2y = 12 là bờ; thay O(0; 0) được 0 ≤ 12 đúng nên miền nghiệm là
  nửa mặt phẳng chứa O. Dấu "≤" nên **kể cả biên**.
- **c) ĐÚNG.** Đường thẳng 3x + 2y = 12 cắt Ox tại A(4; 0) và cắt Oy tại B(0; 6). Kết hợp với
  x ≥ 0, y ≥ 0 ta được miền nghiệm là tam giác OAB **kể cả ba cạnh** (vì tất cả đều là dấu ≤ hoặc ≥).
- **d) SAI.** "Tối đa 12 kg" nghĩa là tổng nguyên liệu **không vượt quá** 12 kg, tức là
  **3x + 2y ≤ 12**. Bất phương trình 3x + 2y ≥ 12 ngược hoàn toàn với điều kiện đề bài.

## 4.4. Lời giải chi tiết Phần III

**Câu 1 – Đáp án: 16.**
Giải x² − 5x + 6 = 0: Δ = 25 − 24 = 1, suy ra x = 2 hoặc x = 3. Vậy tập thứ nhất là {2; 3}.
A = {2; 3} ∪ {0; 1; 2; 3} = {0; 1; 2; 3} — có **4 phần tử**.
Số tập hợp con của một tập có n phần tử là 2ⁿ, nên A có **2⁴ = 16** tập hợp con.

**Câu 2 – Đáp án: 7.**
Gọi F là tập các bạn thích Bóng đá, C là tập các bạn thích Cầu lông.
Số bạn thích **ít nhất một** môn: |F ∪ C| = |F| + |C| − |F ∩ C| = 25 + 20 − 12 = 33.
Số bạn không thích môn nào: 40 − 33 = **7** bạn.

**Câu 3 – Đáp án: 7.**
Vì 90° < α < 180° nên sin α > 0 và cos α < 0.
Từ 1 + tan²α = 1/cos²α suy ra 1/cos²α = 1 + 4 = 5, nên cos²α = 1/5 và cos α = −1/√5.
Khi đó sin α = tan α · cos α = (−2)·(−1/√5) = 2/√5.
P = (2·2/√5 − 3·(−1/√5)) / (2/√5 + (−1/√5)) = (4/√5 + 3/√5) / (1/√5) = (7/√5)·√5 = **7**.
**Cách nhanh:** chia cả tử và mẫu cho cos α (khác 0) ta được
P = (2 tan α − 3)/(tan α + 1) = (2·(−2) − 3)/((−2) + 1) = (−7)/(−1) = **7**.

**Câu 4 – Đáp án: 28,6.**
Gọi h là chiều cao cột cờ, d = 20 m là khoảng cách từ người quan sát đến chân cột, α = 55° là góc
nâng. Tam giác vuông tạo bởi người quan sát, chân cột và đỉnh cột cho ta:
tan 55° = h/20  ⇒  h = 20·tan 55° ≈ 20·1,42815 ≈ 28,5630 (m).
Làm tròn đến hàng phần mười: **h ≈ 28,6 m**.

## 4.5. Lời giải và hướng dẫn chấm Phần IV

### Câu 1 (1,0 điểm)

**a)** A = {x ∈ ℝ | −4 ≤ x < 3} = **[−4; 3)**. (0,25 điểm)
Biểu diễn trên trục số: tô đậm đoạn từ −4 đến 3; **tô đậm** điểm −4 (dấu ≤) và **khoanh tròn**
điểm 3 (dấu <). Tập B = (1; 6]: khoanh tròn điểm 1, tô đậm điểm 6. (0,25 điểm)

**b)** A ∩ B: lấy phần chung của [−4; 3) và (1; 6].
- Đầu trái: cần x ≥ −4 **và** x > 1 ⇒ x > 1 ⇒ đầu trái là **(1**.
- Đầu phải: cần x < 3 **và** x ≤ 6 ⇒ x < 3 ⇒ đầu phải là **3)**.
Vậy **A ∩ B = (1; 3)**. (0,25 điểm)

A ∪ B: gộp hai tập hợp.
- Đầu trái: nhỏ nhất trong hai đầu trái là −4, và −4 ∈ A nên giữ dấu **[−4**.
- Đầu phải: lớn nhất trong hai đầu phải là 6, và 6 ∈ B nên giữ dấu **6]**.
Vậy **A ∪ B = [−4; 6]**. (0,25 điểm)

**c)** Phần bù của A trong ℝ là tập các số thực **không** thuộc [−4; 3), tức là x < −4 hoặc x ≥ 3:
**phần bù của A = (−∞; −4) ∪ [3; +∞)**. (0,25 điểm)

> **Lưu ý khi chấm:** học sinh phải **đổi loại móc** ở cả hai đầu mút khi lấy phần bù. Viết
> (−∞; −4] ∪ [3; +∞) hoặc (−∞; −4) ∪ (3; +∞) đều **không** được điểm ý c.

### Câu 2 (1,0 điểm)

Gọi D là đỉnh tháp, C là chân tháp, nên CD ⊥ mặt đất và CD = h là chiều cao cần tìm. Ba điểm
A, B, C thẳng hàng, B nằm giữa A và C, AB = 24 m. Góc nâng tại A là góc DAC = 35°, tại B là góc
DBC = 50°. (0,25 điểm)

Xét tam giác ABD:
- Góc DAB = 35°.
- Góc ABD và góc DBC kề bù, nên góc ABD = 180° − 50° = 130°.
- Suy ra góc ADB = 180° − 35° − 130° = **15°**. (0,25 điểm)

Áp dụng **định lí sin** trong tam giác ABD:
BD / sin(góc DAB) = AB / sin(góc ADB)
⇒ BD = AB·sin 35° / sin 15° = 24·0,5736 / 0,2588 ≈ **53,187 (m)**. (0,25 điểm)

Xét tam giác vuông BCD (vuông tại C), ta có:
CD = BD·sin(góc DBC) = 53,187·sin 50° ≈ 53,187·0,7660 ≈ 40,74 (m).
Vậy chiều cao ngọn tháp là **h ≈ 40,7 m**. (0,25 điểm)

> **Cách kiểm tra nhanh:** h = AB / (cot 35° − cot 50°) = 24 / (1,42815 − 0,83910) ≈ 40,74 m.
> **Lưu ý khi chấm:** chấp nhận kết quả từ 40,6 m đến 40,8 m do sai số làm tròn trung gian. Nếu học
> sinh quên đổi đơn vị hoặc không làm tròn theo yêu cầu thì trừ 0,25 điểm.

### Câu 3 (1,0 điểm)

**Bước 1 – Đặt ẩn và điều kiện.** Gọi x (chiếc) là số bàn loại I, y (chiếc) là số bàn loại II mà
xưởng sản xuất mỗi ngày. Điều kiện: **x ≥ 0, y ≥ 0, x và y nguyên**. (0,25 điểm)

**Bước 2 – Lập hệ bất phương trình.**
- Về giờ công: 4x + 3y ≤ 48.
- Về gỗ: 2x + 3y ≤ 36.
Hệ bất phương trình: { x ≥ 0 ; y ≥ 0 ; 4x + 3y ≤ 48 ; 2x + 3y ≤ 36 }. (0,25 điểm)

**Bước 3 – Xác định miền nghiệm.** Miền nghiệm là tứ giác lồi có bốn đỉnh:
- O(0; 0).
- Giao của 4x + 3y = 48 với trục Oy... chú ý: trục Ox (y = 0) cho x = 12 → đỉnh **(12; 0)** (thỏa
  2·12 + 0 = 24 ≤ 36).
- Giao của 2x + 3y = 36 với trục Oy (x = 0) cho y = 12 → đỉnh **(0; 12)** (thỏa 0 + 3·12 = 36 ≤ 48).
- Giao của hai đường thẳng 4x + 3y = 48 và 2x + 3y = 36: trừ vế theo vế được 2x = 12 ⇒ x = 6, thay
  vào được 3y = 24 ⇒ y = 8 → đỉnh **(6; 8)**. (0,25 điểm)

**Bước 4 – Tối ưu.** Tiền lãi (nghìn đồng): **F(x; y) = 500x + 400y**.

| Đỉnh | F = 500x + 400y (nghìn đồng) |
|---|---|
| O(0; 0) | 0 |
| (12; 0) | 6 000 |
| (6; 8) | 500·6 + 400·8 = 3 000 + 3 200 = **6 200** |
| (0; 12) | 4 800 |

Vậy F đạt **giá trị lớn nhất là 6 200 nghìn đồng = 6 200 000 đồng** tại đỉnh (6; 8).

**Kết luận:** mỗi ngày xưởng cần sản xuất **6 chiếc bàn loại I và 8 chiếc bàn loại II** thì tổng
tiền lãi lớn nhất, bằng **6 200 000 đồng**. (0,25 điểm)

> **Lưu ý khi chấm:** nếu học sinh chỉ nêu được hệ bất phương trình mà không tìm đỉnh thì cho tối đa
> 0,5 điểm. Nếu tìm đúng đỉnh nhưng kết luận sai giá trị lớn nhất thì cho tối đa 0,75 điểm. Bắt buộc
> phải có **câu kết luận trả lời đúng câu hỏi của đề** (số bàn mỗi loại và số tiền).
"""

# ---------------------------------------------------------------------------
PART5 = """
# PHẦN 5. NGÂN HÀNG BÀI TẬP TỰ LUYỆN

> 12 bài tập phủ đủ 4 chương, mức độ tăng dần. Hãy tự làm trước khi xem đáp án ở cuối phần.

## 5.1. Bài tập

**Bài 1** *(Mệnh đề – NB).* Phát biểu mệnh đề phủ định của mệnh đề "∃x ∈ ℝ, x² − 2x + 5 ≤ 0" và xét
tính đúng/sai của mệnh đề phủ định đó.

**Bài 2** *(Mệnh đề – TH).* Xét tính đúng/sai của mệnh đề: "∀x ∈ ℝ, x² ≥ x". Nếu sai, hãy nêu một
giá trị phản ví dụ.

**Bài 3** *(Mệnh đề – TH).* Cho hai mệnh đề P: "x = 2", Q: "x² = 4". Mệnh đề P ⇒ Q đúng hay sai?
Mệnh đề đảo Q ⇒ P đúng hay sai? P là điều kiện cần hay điều kiện đủ của Q?

**Bài 4** *(Tập hợp – NB).* Cho A = {x ∈ ℕ | x < 6} và B = {x ∈ ℤ | −2 ≤ x ≤ 2}. Viết A, B bằng cách
liệt kê rồi tìm A ∩ B, A ∪ B và A \\ B.

**Bài 5** *(Tập hợp – TH).* Tìm các tập hợp sau và biểu diễn trên trục số:
a) [−1; 5) ∩ (2; 7];   b) (−∞; 3) ∪ [1; 6);   c) phần bù của [−2; 4) trong ℝ.

**Bài 6** *(Phép toán tập hợp – VD).* Lớp 10B có 45 học sinh. Có 28 bạn thích môn Toán, 22 bạn thích
môn Lí và 15 bạn thích cả hai môn. Hỏi lớp 10B có bao nhiêu bạn không thích môn nào trong hai môn
trên?

**Bài 7** *(BPT hai ẩn – NB, TH).* Cho bất phương trình 2x − y + 3 ≥ 0.
a) Điểm O(0; 0) có thuộc miền nghiệm không?
b) Mô tả miền nghiệm của bất phương trình đã cho.

**Bài 8** *(Hệ BPT hai ẩn – VDC).* Tìm giá trị lớn nhất và giá trị nhỏ nhất của biểu thức
F = x + 2y trên miền nghiệm của hệ { x ≥ 0 ; y ≥ 0 ; x + y ≤ 5 ; 2x + y ≤ 8 }.

**Bài 9** *(GTLG – TH).* Cho góc α thỏa mãn 90° < α < 180° và cos α = −1/3. Tính sin α, tan α và
cot α.

**Bài 10** *(GTLG – VD).* Tính giá trị của biểu thức M = sin 30°·cos 60° + cos 30°·sin 60°
(không dùng máy tính cầm tay).

**Bài 11** *(Hệ thức lượng – TH).* Tam giác ABC có a = 13, b = 14, c = 15.
a) Tính diện tích tam giác ABC và bán kính đường tròn nội tiếp r.
b) Tính bán kính đường tròn ngoại tiếp R và độ dài đường trung tuyến mₐ.

**Bài 12** *(Hệ thức lượng – VD).* Tam giác ABC có AB = 10, góc A = 75° và góc B = 45°.
a) Tính góc C.   b) Tính độ dài cạnh AC.   c) Tính diện tích tam giác ABC.

**Bài 13** *(Vectơ – NB).* Cho tam giác ABC. Có bao nhiêu vectơ khác vectơ-không có điểm đầu và điểm
cuối là các đỉnh của tam giác ABC? Hãy kể tên.

**Bài 14** *(Vectơ – TH).* Cho tam giác ABC, gọi M là trung điểm của BC.
a) Chứng minh vectơ AB + vectơ AC = 2·vectơ AM.
b) Gọi G là trọng tâm tam giác ABC. Chứng minh vectơ GA + vectơ GB + vectơ GC = vectơ 0.

## 5.2. Đáp án và hướng dẫn ngắn

**Bài 1.** Phủ định: "∀x ∈ ℝ, x² − 2x + 5 > 0". Mệnh đề này **đúng**, vì
x² − 2x + 5 = (x − 1)² + 4 ≥ 4 > 0 với mọi x ∈ ℝ.

**Bài 2.** **Sai.** Phản ví dụ: x = 1/2 thì x² = 1/4 < 1/2 = x.

**Bài 3.** P ⇒ Q **đúng** (x = 2 thì x² = 4). Mệnh đề đảo Q ⇒ P **sai** (x² = 4 còn có nghiệm
x = −2). Vậy P là **điều kiện đủ** của Q (và Q là điều kiện cần của P).

**Bài 4.** A = {0; 1; 2; 3; 4; 5} (chú ý có số 0); B = {−2; −1; 0; 1; 2}.
A ∩ B = {0; 1; 2}. A ∪ B = {−2; −1; 0; 1; 2; 3; 4; 5}. A \\ B = {3; 4; 5}.

**Bài 5.** a) (2; 5). b) (−∞; 6). c) (−∞; −2) ∪ [4; +∞).

**Bài 6.** Số bạn thích ít nhất một môn: 28 + 22 − 15 = 35. Số bạn không thích môn nào:
45 − 35 = **10** bạn.

**Bài 7.** a) Thay O(0; 0): 0 − 0 + 3 = 3 ≥ 0 — đúng, nên O **thuộc** miền nghiệm.
b) Miền nghiệm là nửa mặt phẳng bờ là đường thẳng d: 2x − y + 3 = 0, **chứa** điểm O(0; 0), **kể cả
biên** (vì dấu ≥). Đường thẳng d đi qua (0; 3) và (−3/2; 0).

**Bài 8.** Các đỉnh của miền nghiệm: O(0; 0), A(4; 0), B(3; 2), C(0; 5).
- A là giao của 2x + y = 8 với y = 0; B là giao của x + y = 5 và 2x + y = 8; C là giao của
  x + y = 5 với x = 0.
- F(O) = 0; F(A) = 4; F(B) = 3 + 4 = 7; F(C) = 0 + 10 = 10.
Vậy **giá trị lớn nhất là 10** (tại (0; 5)) và **giá trị nhỏ nhất là 0** (tại (0; 0)).

**Bài 9.** sin²α = 1 − cos²α = 1 − 1/9 = 8/9. Vì α tù nên sin α > 0, suy ra **sin α = 2√2/3**.
tan α = sin α / cos α = (2√2/3)/(−1/3) = **−2√2**. cot α = 1/tan α = **−√2/4** (= −1/(2√2)).

**Bài 10.** M = (1/2)·(1/2) + (√3/2)·(√3/2) = 1/4 + 3/4 = **1**.
(Nhận xét: M = sin(30° + 60°) = sin 90° = 1.)

**Bài 11.** a) Nửa chu vi p = (13 + 14 + 15)/2 = 21.
S = √(21·8·7·6) = √7056 = **84**. r = S/p = 84/21 = **4**.
b) R = abc/(4S) = (13·14·15)/(4·84) = 2730/336 = **65/8 = 8,125**.
mₐ² = (2b² + 2c² − a²)/4 = (2·196 + 2·225 − 169)/4 = (392 + 450 − 169)/4 = 673/4,
nên mₐ = **√673/2 ≈ 12,97**.

**Bài 12.** a) Góc C = 180° − 75° − 45° = **60°**.
b) Định lí sin: AC/sin B = AB/sin C ⇒ AC = 10·sin 45°/sin 60° = 10·(√2/2)/(√3/2) = 10√2/√3 =
**10√6/3 ≈ 8,16**.
c) S = (1/2)·AB·AC·sin A = (1/2)·10·(10√6/3)·sin 75° ≈ (1/2)·10·8,165·0,9659 ≈ **39,43**.

**Bài 13.** Có 3 đỉnh nên số vectơ khác vectơ-không là 3·(3 − 1) = **6 vectơ**:
vectơ AB, vectơ AC, vectơ BA, vectơ BC, vectơ CA, vectơ CB.

**Bài 14.** a) Vì M là trung điểm của BC nên vectơ MB + vectơ MC = vectơ 0. Do đó
vectơ AB + vectơ AC = (vectơ AM + vectơ MB) + (vectơ AM + vectơ MC) =
2·vectơ AM + (vectơ MB + vectơ MC) = 2·vectơ AM + vectơ 0 = **2·vectơ AM**. ■

b) Vì G là trọng tâm tam giác nên G nằm trên trung tuyến AM và AG = (2/3)·AM, suy ra
vectơ AG = (2/3)·vectơ AM, hay vectơ GA = −(2/3)·vectơ AM.
Lại có vectơ GB + vectơ GC = 2·vectơ GM (vì M là trung điểm BC), mà
vectơ GM = −vectơ MG = −(1/3)·vectơ MA = (1/3)·vectơ AM, nên
vectơ GB + vectơ GC = (2/3)·vectơ AM = −vectơ GA.
Vậy vectơ GA + vectơ GB + vectơ GC = −vectơ GA + vectơ GA = **vectơ 0**. ■

~ **Nhận xét về hai bài 13 và 14**
> Đây là hai dạng vectơ duy nhất trong phạm vi kiểm tra: **đếm vectơ** (bài 13) và **dùng hệ thức
> trung điểm – trọng tâm để chứng minh đẳng thức vectơ** (bài 14). Cả hai chỉ ở mức nhận biết –
> thông hiểu, đúng như trọng số 5% của Chương 4 trong ma trận.
"""

# ---------------------------------------------------------------------------
PART6 = """
# PHẦN 6. PHỤ LỤC

## 6.1. Bảng công thức tóm tắt một trang

> **CHƯƠNG 1 – MỆNH ĐỀ VÀ TẬP HỢP**
> - P ⇒ Q chỉ sai khi P đúng, Q sai. P ⇔ Q đúng khi P, Q cùng tính đúng/sai.
> - Phủ định: đổi ∀ ↔ ∃ và phủ định vị ngữ; phủ định của ">" là "≤", của "≥" là "<".
> - Tập n phần tử có 2ⁿ tập con. |A ∪ B| = |A| + |B| − |A ∩ B|.
> - A ∩ B: phần chung. A ∪ B: gộp lại. A \\ B: thuộc A, không thuộc B.
> - Phần bù của [a; b] là (−∞; a) ∪ (b; +∞) — **đổi loại móc**.
>
> **CHƯƠNG 2 – BẤT PHƯƠNG TRÌNH VÀ HỆ BPT BẬC NHẤT HAI ẨN**
> - Dạng: ax + by ≤ c (a² + b² ≠ 0). Miền nghiệm là một nửa mặt phẳng bờ d: ax + by = c.
> - Thay điểm thử (thường là O) để chọn nửa mặt phẳng. Dấu ≤, ≥ thì **kể cả biên**.
> - Miền nghiệm của hệ là **giao** các miền nghiệm; thường là một miền đa giác.
> - F = ax + by đạt GTLN/GTNN trên miền đa giác **tại một đỉnh**.
>
> **CHƯƠNG 3 – HỆ THỨC LƯỢNG TRONG TAM GIÁC**
> - sin(180° − α) = sin α; cos(180° − α) = −cos α; tan(180° − α) = −tan α; cot(180° − α) = −cot α.
> - sin²α + cos²α = 1; tan α·cot α = 1; 1 + tan²α = 1/cos²α; 1 + cot²α = 1/sin²α.
> - Góc tù: sin dương; cos, tan, cot **âm**.
> - a² = b² + c² − 2bc·cos A; cos A = (b² + c² − a²)/(2bc).
> - a/sin A = b/sin B = c/sin C = 2R.
> - S = (1/2)bc·sin A = abc/(4R) = p·r = √(p(p−a)(p−b)(p−c)).
> - mₐ² = (2b² + 2c² − a²)/4.
> - Đo chiều cao khi không đến được chân vật: h = AB/(cot α − cot β).
>
> **CHƯƠNG 4 – VECTƠ**
> - Vectơ a = vectơ b ⇔ cùng hướng và cùng độ dài.
> - Vectơ-không có độ dài 0, cùng phương và cùng hướng với **mọi** vectơ.
> - Vectơ AB + vectơ BC = vectơ AC.
> - M trung điểm AB ⇒ vectơ MA + vectơ MB = vectơ 0 và vectơ OA + vectơ OB = 2 vectơ OM.
> - G trọng tâm ⇒ vectơ GA + vectơ GB + vectơ GC = vectơ 0 và vectơ OA + vectơ OB + vectơ OC =
>   3 vectơ OG.

## 6.2. Bảng giá trị lượng giác đặc biệt (bản in để học thuộc)

| α | 0° | 30° | 45° | 60° | 90° | 120° | 135° | 150° | 180° |
|---|---|---|---|---|---|---|---|---|---|
| sin α | 0 | 0,5 | 0,7071 | 0,8660 | 1 | 0,8660 | 0,7071 | 0,5 | 0 |
| cos α | 1 | 0,8660 | 0,7071 | 0,5 | 0 | −0,5 | −0,7071 | −0,8660 | −1 |
| tan α | 0 | 0,5774 | 1 | 1,7321 | KXĐ | −1,7321 | −1 | −0,5774 | 0 |
| cot α | KXĐ | 1,7321 | 1 | 0,5774 | 0 | −0,5774 | −1 | −1,7321 | KXĐ |

~ **Mẹo nhớ bảng sin – cos**
> Giá trị sin của các góc 0°, 30°, 45°, 60°, 90° là căn bậc hai của 0/4, 1/4, 2/4, 3/4, 4/4.
> Cột cos đọc **ngược** cột sin. Các góc tù (120°, 135°, 150°) có sin **giống** góc bù của nó, còn
> cos, tan, cot thì **đổi dấu**.

## 6.3. Hướng dẫn bấm máy tính cầm tay (Casio fx-580VN X / fx-570VN PLUS)

1. **Chuyển sang chế độ độ:** bấm SHIFT → MODE (SETUP) → chọn **2: Degree (D)**. Trên màn hình phải
   hiện chữ **D**. Nếu hiện **R** (ra-đi-an) thì mọi kết quả lượng giác đều sai.
2. **Tính GTLG:** sin, cos, tan bấm trực tiếp, ví dụ sin 55° = 0,8192; tan 55° = 1,4281.
3. **Tìm góc khi biết GTLG:** dùng SHIFT + sin/cos/tan. Ví dụ SHIFT tan(1) = 45°. Với góc tù, dùng
   tính chất: nếu tan α = −2 thì góc nhọn tương ứng là SHIFT tan(2) ≈ 63,43°, suy ra
   α ≈ 180° − 63,43° = 116,57°.
4. **Căn và phân số:** dùng phím √ và phím phân số; kết quả nên để ở **dạng chính xác** khi đề yêu
   cầu viết dưới dạng a√b.
5. **Lưu giá trị trung gian:** dùng phím STO → A, B, C để tránh làm tròn nhiều lần gây sai số.
6. **Kiểm tra nhanh định lí sin/côsin:** nhập vế trái và vế phải rồi dùng phím CALC hoặc so sánh
   bằng dấu "=".

! **Ba lỗi bấm máy phổ biến nhất**
> - Để chế độ **R** thay vì **D**.
> - Nhập sin 55 thành sin(5) rồi gõ thừa số 5.
> - Làm tròn **quá sớm**: hãy giữ đủ chữ số trong các bước trung gian, chỉ làm tròn ở **kết quả
>   cuối cùng** theo yêu cầu của đề.

## 6.4. Phiếu tự đánh giá trước ngày thi

Hãy tự chấm cho mỗi dòng: 0 = chưa biết, 1 = còn lúng túng, 2 = thành thạo. Tổng dưới 24 điểm thì
cần ôn lại Phần 2 của đề cương này.

| STT | Kĩ năng | Chương | Tự chấm |
|---|---|---|---|
| 1 | Nhận biết mệnh đề, mệnh đề chứa biến | 1 | |
| 2 | Phủ định mệnh đề chứa ∀, ∃ | 1 | |
| 3 | Xác định điều kiện cần – đủ | 1 | |
| 4 | Liệt kê tập hợp / viết tính chất đặc trưng | 1 | |
| 5 | Đọc và viết đúng khoảng, đoạn, nửa khoảng | 1 | |
| 6 | Biểu diễn khoảng, đoạn trên trục số | 1 | |
| 7 | Tính giao, hợp, hiệu, phần bù | 1 | |
| 8 | Đếm số tập con, bài toán sơ đồ Ven | 1 | |
| 9 | Nhận biết BPT / hệ BPT bậc nhất hai ẩn | 2 | |
| 10 | Biểu diễn miền nghiệm của BPT | 2 | |
| 11 | Biểu diễn miền nghiệm của hệ BPT | 2 | |
| 12 | Chuyển bài toán thực tế về hệ BPT | 2 | |
| 13 | Tìm GTLN/GTNN của F = ax + by trên miền đa giác | 2 | |
| 14 | Thuộc bảng GTLG đặc biệt và dấu của GTLG | 3 | |
| 15 | Dùng hệ thức sin²α + cos²α = 1 và các hệ thức liên quan | 3 | |
| 16 | Áp dụng định lí côsin | 3 | |
| 17 | Áp dụng định lí sin (chú ý hệ số 2R) | 3 | |
| 18 | Tính diện tích bằng 4 công thức | 3 | |
| 19 | Giải bài toán đo chiều cao / khoảng cách thực tế | 3 | |
| 20 | Nhận biết vectơ, độ dài, giá, cùng phương, cùng hướng | 4 | |
| 21 | Xét hai vectơ bằng nhau / đối nhau | 4 | |
| 22 | Dùng hệ thức trung điểm và trọng tâm | 4 | |
| 23 | Bấm máy tính ở chế độ độ (D) thành thạo | – | |
| 24 | Phân bổ thời gian 90 phút hợp lí | – | |

## 6.5. Nguồn tham khảo và căn cứ biên soạn

1. **Ma trận đề kiểm tra giữa kì I năm học 2026–2027, môn Toán lớp 10** — Trường THPT Hà Huy Tập,
   Tổ Toán–Tin (tệp nguồn `MA TRẬN TOÁN 10 - GIỮA KÌ I.docx`; gồm Mục tiêu, Hình thức, Ma trận chi
   tiết và Bảng đặc tả). **Đây là căn cứ chính** để xác định cấu trúc, số câu, mức độ nhận thức và
   nội dung từng câu hỏi trong Phần 3.
2. **Sách giáo khoa Toán 10, tập 1 — bộ Kết nối tri thức với cuộc sống** (NXB Giáo dục Việt Nam):
   Chương I (Bài 1, 2), Chương II (Bài 3, 4), Chương III (Bài 5, 6), Chương IV (Bài 7). Bộ sách này
   được dùng chung trên toàn quốc từ năm học 2026–2027.
3. **Chương trình giáo dục phổ thông môn Toán** (ban hành kèm Thông tư 32/2018/TT-BGDĐT) — căn cứ
   xác định các yêu cầu cần đạt.

## 6.6. Lời kết

Ba điều đáng nhớ nhất khi bước vào phòng thi:

1. **Đọc kĩ yêu cầu của từng câu** — nhất là phần *trả lời ngắn* (làm tròn đến hàng nào?) và phần
   *đúng – sai* (chấm theo số ý đúng, không trừ điểm ý sai).
2. **Viết công thức trước, thay số sau.** Ở phần tự luận, một công thức đúng vẫn có điểm dù phép
   tính sau đó sai; ngược lại, một đáp án đúng không có công thức rất khó được điểm tối đa.
3. **Không bỏ trống câu nào.** Trắc nghiệm không trừ điểm khi chọn sai, nên trước khi hết giờ hãy
   chắc chắn đã tô đủ cả 12 câu và ghi đủ 4 đáp án trả lời ngắn.

> **Lời nhắn cuối**
> Đề cương này được thiết kế để em **tự học có định hướng**: biết phần nào chiếm nhiều điểm, biết
> mỗi câu trong đề kiểm tra điều gì, và có sẵn đáp án để tự kiểm tra. Hãy làm Phần 3 trong đúng 90
> phút, tự chấm bằng Phần 4, rồi quay lại Phần 2 ở đúng những chỗ mình sai — đó là cách ôn tập hiệu
> quả nhất. Chúc các em làm bài tốt.

---

*Đề cương ôn tập giữa học kì I – môn Toán lớp 10 – năm học 2026–2027. Biên soạn bám sát ma trận đề
kiểm tra của Tổ Toán–Tin, Trường THPT Hà Huy Tập, và chương trình Toán 10 – bộ sách Kết nối tri thức
với cuộc sống.*

> **Ghi chú minh bạch.** Đề kiểm tra chính thức của kì kiểm tra giữa học kì I năm học 2026–2027
> không nằm trong tệp nguồn (tệp nguồn chỉ có ma trận và bảng đặc tả) và cũng chưa được công bố
> công khai tại thời điểm biên soạn đề cương này. Vì vậy Phần 3 là **đề minh họa do đề cương tự
> biên soạn**, được thiết kế **khớp từng ô** với ma trận và bảng đặc tả gốc, chứ không phải là bản
> sao của đề thi thật. Tất cả 27 lệnh hỏi trong Phần 3 đều có đáp án và lời giải chi tiết ở Phần 4,
> và toàn bộ kết quả số đã được kiểm tra lại bằng một tập lệnh kiểm thử tự động
> (`de-cuong/src/verify_answers.py`).
"""

SECTIONS = [INTRO, PART1, PART2_CH1, PART2_CH2, PART2_CH3, PART2_CH4,
            PART3, PART4, PART5, PART6]
