#import "template.typ": *

// ============================================================================
// PHẦN C: HỆ THỐNG KIẾN THỨC TRỌNG TÂM, SƠ ĐỒ & BẪY HAY SAI (CHƯƠNG I → IV)
// ============================================================================

= PHẦN C. HỆ THỐNG KIẾN THỨC TRỌNG TÂM, SƠ ĐỒ & BẪY HAY SAI (CHƯƠNG I → IV)

// ----------------------------------------------------------------------------
// CHỦ ĐỀ 1.1: MỆNH ĐỀ (BÀI 1)
// ----------------------------------------------------------------------------
#lesson-header("1.1 (Chương I — Bài 1)", "MỆNH ĐỀ & MỆNH ĐỀ CHỨA BIẾN", "Phần I: Câu 1 (NB), Câu 2 (NB)", "0,50 điểm")

*1. Mệnh đề và Mệnh đề chứa biến (Câu 1 Phần I)*
- *Mệnh đề (mệnh đề lôgic):* Là một câu khẳng định *đúng* hoặc *sai*. Một câu không thể vừa đúng vừa sai (*quy luật cấm mâu thuẫn*), cũng không thể không đúng không sai (*quy luật bài trung*).
  - _Ví dụ mệnh đề đúng:_ “$pi$ là một số vô tỉ”; “Số $17$ là số nguyên tố”; “Phương trình $x^2 + 1 = 0$ vô nghiệm”.
  - _Ví dụ mệnh đề sai:_ “Số $9$ là số nguyên tố”; “$sqrt(2) in QQ$”.
  - *Không phải mệnh đề:* Các câu nghi vấn (`?`), câu cảm thán (`!`), câu cầu khiến/mệnh lệnh (VD: _“Hôm nay trời đẹp quá!”_, _“Bạn đã làm bài tập Toán chưa?”_, _“Các em hãy giữ trật tự!”_).
- *Mệnh đề chứa biến $P(x)$:* Là câu khẳng định chứa biến $x$ (với $x in X$) mà tính đúng/sai chưa xác định được ngay; chỉ khi thay $x$ bằng một giá trị cụ thể $x_0 in X$ thì $P(x_0)$ mới trở thành một mệnh đề xác định.
  - _Ví dụ:_ $P(n)$: “$2n + 1$ chia hết cho $3$” (với $n in NN$). Khi $n = 1 arrow.r.double P(1)$ đúng; khi $n = 2 arrow.r.double P(2)$ sai.
- *Mệnh đề phủ định ($overline(P)$):* Để phủ định mệnh đề $P$, ta thêm (hoặc bớt) từ *“không”* hoặc *“không phải”* trước vị ngữ của $P$. Nếu $P$ đúng thì $overline(P)$ sai; nếu $P$ sai thì $overline(P)$ đúng.

*2. Mệnh đề kéo theo, Mệnh đề đảo, Mệnh đề tương đương & Điều kiện cần – đủ*

#set text(size: 8.8pt)
#table(
  columns: (1.25fr, 1.55fr, 2.4fr),
  stroke: 0.5pt + c-border,
  fill: (x, y) => if y == 0 { rgb("#F1F5F9") } else { white },
  inset: 5pt,
  [*Loại mệnh đề*], [*Kí hiệu & Cách phát biểu*], [*Quy tắc xét tính Đúng / Sai & Ý nghĩa Toán học*],
  [*Mệnh đề kéo theo*], [$P arrow.r.double Q$\ _“Nếu $P$ thì $Q$”_\ _“$P$ suy ra $Q$”_], [• *Chỉ SAI duy nhất* khi *$P$ đúng mà $Q$ sai* ($1 arrow.r.double 0$).\ • Khi định lí $P arrow.r.double Q$ đúng: *$P$ là giả thiết (điều kiện ĐỦ để có $Q$)*; *$Q$ là kết luận (điều kiện CẦN để có $P$)* _(Khẩu quyết: Trước Đủ – Sau Cần)_.],
  [*Mệnh đề đảo*], [$Q arrow.r.double P$\ _(Đảo của $P arrow.r.double Q$)_], [• Mệnh đề $P arrow.r.double Q$ đúng *không có nghĩa* là mệnh đề đảo $Q arrow.r.double P$ cũng đúng!\ _(VD: “Tam giác đều $arrow.r.double$ tam giác cân” đúng, nhưng mệnh đề đảo sai)_.],
  [*Mệnh đề tương đương*], [$P arrow.l.r.double Q$\ _“$P$ khi và chỉ khi $Q$”_], [• Đúng khi cả hai mệnh đề $P arrow.r.double Q$ và $Q arrow.r.double P$ cùng đúng (tức $P, Q$ cùng đúng hoặc cùng sai). Khi đó $P$ là *điều kiện cần và đủ* để có $Q$.],
)
#set text(size: 9.8pt)

*3. Kí hiệu phổ biến ($forall$) và kí hiệu tồn tại ($exists$) — Phủ định mệnh đề có $forall, exists$ (Câu 2 Phần I)*
- *Kí hiệu $forall$ (đọc là “với mọi”):* Mệnh đề “$forall x in X, P(x)$” *đúng* khi *mọi* phần tử $x_0 in X$ đều làm $P(x_0)$ đúng. Muốn chứng minh nó *sai*, chỉ cần chỉ ra *1 phản ví dụ* $x_0 in X$ làm $P(x_0)$ sai.
- *Kí hiệu $exists$ (đọc là “tồn tại” hoặc “có ít nhất một”):* Mệnh đề “$exists x in X, P(x)$” *đúng* khi tìm được *ít nhất 1 giá trị* $x_0 in X$ làm $P(x_0)$ đúng.
- *Quy tắc phủ định mệnh đề chứa $forall, exists$:* Đổi $forall arrow.l.r exists$, giữ nguyên $x in X$, và phủ định $P(x) arrow.r overline(P(x))$:
  $ overline(forall x in X comma P(x)) arrow.l.r.double exists x in X comma overline(P(x)) #h(24pt) "và" #h(24pt) overline(exists x in X comma P(x)) arrow.l.r.double forall x in X comma overline(P(x)) $

#trap-box("3 Bẫy Kinh Điển ở Câu 1 & Câu 2 Phần I (Mục 1.1)", [
  • *Bẫy 1 (Đổi nhầm dấu bất đẳng thức):* Phủ định của $>$ là *$<=$* (không phải $<$!); phủ định của $>=$ là *$<$*; phủ định của $=$ là *$!=$*.\
  • *Bẫy 2 (Đổi nhầm miền $x in X$):* Phủ định của “$forall x in RR, x^2 >= 0$” là “$exists x in RR, x^2 < 0$” (*tuyệt đối không* chọn phương án có $exists x in.not RR$!).\
  • *Bẫy 3 (Phương trình vô nghiệm trên $QQ$ hay $ZZ$):* Mệnh đề “$exists x in QQ, x^2 = 2$” là *SAI* vì $x = plus.minus sqrt(2) in.not QQ$.
])

// ----------------------------------------------------------------------------
// CHỦ ĐỀ 1.2: TẬP HỢP (BÀI 2 - PHẦN 1)
// ----------------------------------------------------------------------------
#lesson-header("1.2 (Chương I — Bài 2a)", "TẬP HỢP, TẬP CON & CÁC TẬP CON CỦA ℝ", "P.I: Câu 3 | P.II: Câu 1a, 1b | P.III: Câu 1 TLN", "1,25 điểm")

*1. Hai cách xác định tập hợp & Quan hệ thuộc ($in$), tập con ($subset$) (Câu 3 P.I & Câu 1a, 1b P.II)*
- *Cách 1 — Liệt kê các phần tử:* Viết các phần tử trong cặp ngoặc nhọn $\{ dots \}$, cách nhau bởi dấu `;` (hoặc `,`), mỗi phần tử chỉ liệt kê *1 lần*, không phân biệt thứ tự.
- *Cách 2 — Chỉ ra tính chất đặc trưng:* $A = \{x in X | P(x)\}$.
  - _Phương pháp chuyển từ tính chất đặc trưng sang liệt kê:_ Giải phương trình / bất phương trình $P(x)$ rồi *đối chiếu điều kiện miền số $X$* ($NN^*, NN, ZZ, QQ, RR$).
  - _Ví dụ mẫu:_ Cho $A = \{x in ZZ | (x^2 - 4)(2x - 1) = 0\}$. Giải phương trình được $x = 2 in ZZ$, $x = -2 in ZZ$, $x = 1/2 in.not ZZ$ (loại!). Vậy $A = \{-2; 2\}$.
- *Tập rỗng ($emptyset$):* Là tập hợp không chứa phần tử nào.
- *Tập hợp con ($A subset B$):* $A subset B arrow.l.r.double (forall x, x in A arrow.r.double x in B)$. Tính chất: $emptyset subset A$ và $A subset A$ với mọi tập $A$; bắc cầu: $(A subset B " và " B subset C) arrow.r.double A subset C$.
- *Hai tập hợp bằng nhau ($A = B$):* $A = B arrow.l.r.double (A subset B " và " B subset A) arrow.l.r.double (forall x, x in A arrow.l.r.double x in B)$.

#formula-box("Công Thức Đếm Số Tập Hợp Con (Trọng tâm Câu 1 Trả lời ngắn Phần III — 0,5 điểm)", [
  Cho tập hợp hữu hạn $A$ có đúng *$n$ phần tử* ($n in NN$):\
  • *Tổng số tập hợp con của $A$:* *$2^n$* tập con (bao gồm cả tập rỗng $emptyset$ và chính tập $A$).\
  • *Số tập con khác rỗng* của $A$: *$2^n - 1$* tập con. #h(12pt) • *Số tập con thực sự* (khác $A$) của $A$: *$2^n - 1$* tập con.\
  • *Số tập con thực sự và khác rỗng* của $A$: *$2^n - 2$* tập con.\
  • *Số tập con có đúng $k$ phần tử* ($0 <= k <= n$): $C_n^k = frac(n!, k!(n - k)!)$ _(VD: Tập 5 phần tử có $C_5^2 = 10$ tập con gồm 2 phần tử)_.\
  • *Bài toán kẹp $M subset X subset N$* (với $M$ có $m$ phần tử, $N$ có $n$ phần tử, $M subset N$): Số tập hợp $X$ thỏa mãn là *$2^(n - m)$*.
])

*2. Các tập hợp số & 9 loại tập con thường dùng của $RR$ (Câu 1a, 1b Phần II)*
- Quan hệ bao hàm giữa các tập số: *$NN^* subset NN subset ZZ subset QQ subset RR$* (trong đó $NN^* = \{1; 2; 3; dots\}$, $NN = \{0; 1; 2; dots\}$).
- *Các khoảng, đoạn, nửa khoảng trên trục số thực $RR$* (với $a < b$):
  - *Đoạn:* $[a; b] = \{x in RR | a <= x <= b\}$. #h(16pt) *Khoảng:* $(a; b) = \{x in RR | a < x < b\}$; $(-infinity; +infinity) = RR$.
  - *Nửa khoảng:* $[a; b) = \{x in RR | a <= x < b\}$; #h(8pt) $(a; b] = \{x in RR | a < x <= b\}$.
  - *Khoảng / nửa khoảng vô cực:* $(-infinity; a) = \{x < a\}$; $(-infinity; a] = \{x <= a\}$; $(a; +infinity) = \{x > a\}$; $[a; +infinity) = \{x >= a\}$.

// ----------------------------------------------------------------------------
// CHỦ ĐỀ 1.3: CÁC PHÉP TOÁN TRÊN TẬP HỢP (BÀI 2 - PHẦN 2)
// ----------------------------------------------------------------------------
#lesson-header("1.3 (Chương I — Bài 2b)", "CÁC PHÉP TOÁN TRÊN TẬP HỢP", "P.I: Câu 4 | P.II: Câu 1c, 1d | P.III: Câu 2 | P.IV: Câu 1 TL", "2,25 điểm")

*1. Bốn phép toán trên tập hợp & Biểu đồ Ven (Câu 4 Phần I & Câu 2 Phần III)*

#align(center)[#image("assets/venn_operations.svg", width: 99%)]

*2. Thực hiện phép toán Giao, Hợp, Hiệu, Phần bù trên Trục số (Trọng tâm Câu 1 Tự luận — 1,0 điểm)*

#align(center)[#image("assets/number_line_intervals.svg", width: 99%)]

*3. Các điều kiện chứa tham số $m$ trên khoảng, đoạn (Trọng tâm Câu 1d Đúng/Sai — Mức Vận dụng)*
Cho hai tập hợp khác rỗng $A = [a; b]$ và $B = (m; m + k)$ (hoặc $[m; m + k]$). Khi đó:
- *Điều kiện bao hàm $A subset B$:* Đặt $A$ nằm trọn bên trong $B$ trên trục số $arrow.r.double m < a <= b < m + k$ (chú ý xét dấu bằng tại đầu mút: nếu ngoài vuông – trong vuông hoặc ngoài tròn – trong tròn thì lấy dấu $<=$; nếu *ngoài tròn – trong vuông* thì chỉ lấy dấu $<$ nghiêm ngặt!).
- *Điều kiện giao bằng rỗng ($A inter B = emptyset$):* $A$ nằm hẳn bên trái $B$ hoặc hẳn bên phải $B$: $b <= m$ hoặc $m + k <= a$.
- *Điều kiện giao khác rỗng ($A inter B != emptyset$):* Tìm điều kiện để $A inter B = emptyset$ trước, sau đó *lấy phần bù* trên miền tồn tại của $A, B$!

// ----------------------------------------------------------------------------
// CHỦ ĐỀ 2.1: BẤT PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN (BÀI 3)
// ----------------------------------------------------------------------------
#lesson-header("2.1 (Chương II — Bài 3)", "BẤT PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN", "P.I: Câu 5 (NB) | P.II: Câu 2a, 2b, 2c, 2d (1,0đ)", "1,25 điểm")

*1. Khái niệm & Nghiệm của Bất phương trình bậc nhất hai ẩn (Câu 5 Phần I & Câu 2a Phần II)*
- *Định nghĩa:* Bất phương trình bậc nhất hai ẩn $x, y$ có dạng tổng quát là *$a x + b y < c$* (hoặc $a x + b y <= c$, $a x + b y > c$, $a x + b y >= c$), trong đó $a, b, c in RR$ và *$a, b$ không đồng thời bằng $0$* ($a^2 + b^2 > 0$).
  - _Cảnh báo nhận diện (Câu 5 TN):_ BPT chứa $x^2, y^2, x y, frac(1, x), sqrt(x)$ hoặc có thêm ẩn thứ ba $z$ (như $x + y - 2z > 1$) *không phải* là BPT bậc nhất hai ẩn! Còn BPT khuyết một ẩn như $2x - 5 <= 0$ ($a = 2, b = 0$) hay $y > 3$ ($a = 0, b = 1$) *VẪN LÀ* BPT bậc nhất hai ẩn.
- *Nghiệm của BPT:* Cặp số $(x_0; y_0)$ thỏa mãn $a x_0 + b y_0 < c$ là một nghiệm. BPT bậc nhất hai ẩn luôn có *vô số nghiệm*.

*2. Biểu diễn và mô tả miền nghiệm trên mặt phẳng tọa độ $O x y$ (Câu 2b, 2c Phần II)*

#align(center)[#image("assets/linear_inequality_plane.svg", width: 99%)]

*3. Chuyển điều kiện bài toán thực tế về BPT bậc nhất hai ẩn (Câu 2d Phần II — Mức Vận dụng)*
- *Mô hình tổng chi phí / ngân sách:* Mua $x$ sản phẩm loại I (giá $a$ đồng/sp) và $y$ sản phẩm loại II (giá $b$ đồng/sp) với tổng số tiền *không vượt quá* $c$ đồng $arrow.r.double$ *$a x + b y <= c$* (với $x, y in NN$).
- *Mô hình thời gian / nguyên liệu tối đa:* Dùng *nhiều nhất* $c$ giờ máy $arrow.r.double a x + b y <= c$.
- *Mô hình chỉ tiêu / dinh dưỡng tối thiểu:* Cần thu được *ít nhất* (tối thiểu) $c$ đơn vị $arrow.r.double$ *$a x + b y >= c$*.

// ----------------------------------------------------------------------------
// CHỦ ĐỀ 2.2: HỆ BẤT PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN (BÀI 4)
// ----------------------------------------------------------------------------
#lesson-header("2.2 (Chương II — Bài 4)", "HỆ BPT BẬC NHẤT HAI ẨN & BÀI TOÁN TỐI ƯU", "P.I: Câu 6 (NB) | P.IV: Câu 3 Tự luận VDC (1,0đ)", "1,25 điểm")

*1. Hệ bất phương trình bậc nhất hai ẩn (Câu 6 Phần I)*
- *Hệ BPT bậc nhất hai ẩn* gồm hai hay nhiều BPT bậc nhất hai ẩn. Cặp số $(x_0; y_0)$ là *nghiệm của hệ* khi và chỉ khi nó *đồng thời là nghiệm của TẤT CẢ các BPT* trong hệ.
- _Mẹo làm Câu 6 TN trong 10 giây:_ Thay tọa độ từng đáp án $(x_0; y_0)$ vào từng BPT trong hệ; nếu vi phạm *bất kỳ 1 BPT nào* thì loại ngay đáp án đó!

*2. Phương pháp giải Bài toán Tìm phương án tối ưu (Quy hoạch tuyến tính — Câu 3 Tự luận VDC)*
- *Định lí cơ bản:* Giá trị lớn nhất ($max$) và giá trị nhỏ nhất ($min$) của biểu thức bậc nhất $F(x; y) = a x + b y$ trên miền nghiệm là một miền đa giác lồi $A_1 A_2 dots A_n$ luôn đạt được tại *một trong các đỉnh* của đa giác đó.

#align(center)[#image("assets/linear_programming_poly.svg", width: 99%)]

// ----------------------------------------------------------------------------
// CHỦ ĐỀ 3.1: GIÁ TRỊ LƯỢNG GIÁC CỦA GÓC TỪ 0° ĐẾN 180° (BÀI 5)
// ----------------------------------------------------------------------------
#lesson-header("3.1 (Chương III — Bài 5)", "GIÁ TRỊ LƯỢNG GIÁC CỦA GÓC TỪ 0° ĐẾN 180°", "P.I: Câu 7 (NB), Câu 8 (TH) | P.III: Câu 3 TLN (VD)", "1,00 điểm")

*1. Định nghĩa trên nửa đường tròn đơn vị, Bảng xét dấu & Góc bù / phụ nhau (Câu 7, 8 Phần I)*

#align(center)[#image("assets/unit_semicircle_trig.svg", width: 99%)]

*2. Các hệ thức lượng giác cơ bản & 3 Dạng toán trọng tâm (Câu 8 Phần I & Câu 3 Phần III)*
- *4 Hệ thức cơ bản:*
  *(1)* $sin^2 alpha + cos^2 alpha = 1$; #h(10pt)
  *(2)* $tan alpha dot cot alpha = 1$ ($0^degree < alpha < 180^degree, alpha != 90^degree$); #h(10pt)
  *(3)* $1 + tan^2 alpha = frac(1, cos^2 alpha)$ ($alpha != 90^degree$); #h(10pt)
  *(4)* $1 + cot^2 alpha = frac(1, sin^2 alpha)$ ($0^degree < alpha < 180^degree$).

#formula-box("3 Phương Pháp Giải Nhanh Câu 8 Phần I & Câu 3 Trả Lời Ngắn Phần III", [
  • *Dạng 1 (Câu 8 TN): Biết $sin alpha$ (hoặc $cos alpha$), tính các GTLG còn lại:*\
    Từ $sin^2 alpha + cos^2 alpha = 1 arrow.r.double cos alpha = plus.minus sqrt(1 - sin^2 alpha)$. *Nhìn góc $alpha$ để chọn dấu:* Nếu $0^degree < alpha < 90^degree$ (góc nhọn) thì lấy *$cos alpha > 0$*; nếu $90^degree < alpha < 180^degree$ (góc tù) thì lấy *$cos alpha < 0$*! Sau đó tính $tan alpha = frac(sin alpha, cos alpha), cot alpha = frac(1, tan alpha)$.\
  • *Dạng 2 (Câu 8 TN): Biết $tan alpha$ (hoặc $cot alpha$), tính $cos alpha, sin alpha$:*\
    Từ $1 + tan^2 alpha = frac(1, cos^2 alpha) arrow.r.double cos^2 alpha = frac(1, 1 + tan^2 alpha)$. Vì $cos alpha$ luôn *cùng dấu với $tan alpha$* trên $(0^degree; 180^degree)$ nên: nếu $tan alpha > 0 arrow.r.double cos alpha > 0$; nếu $tan alpha < 0 arrow.r.double cos alpha < 0$. Sau đó suy ra $sin alpha = tan alpha dot cos alpha$.\
  • *Dạng 3 (Câu 3 TLN — 0,5 điểm): Cho $tan alpha = k$, tính giá trị biểu thức phân thức $P$:*\
    – _Loại bậc nhất:_ $P = frac(a sin alpha + b cos alpha, c sin alpha + d cos alpha)$ $arrow.r$ *$P = frac(a tan alpha + b, c tan alpha + d) = frac(a k + b, c k + d)$*.\
    – _Loại bậc hai:_ $Q = frac(a sin^2 alpha + b sin alpha cos alpha + c cos^2 alpha, m sin^2 alpha + n sin alpha cos alpha + p cos^2 alpha)$ $arrow.r$ *$Q = frac(a tan^2 alpha + b tan alpha + c, m tan^2 alpha + n tan alpha + p)$*.\
    – _Loại không mẫu:_ $R = a sin^2 alpha + b sin alpha cos alpha + c cos^2 alpha = frac(a tan^2 alpha + b tan alpha + c, tan^2 alpha + 1)$ (vì $1 = sin^2 alpha + cos^2 alpha$).
])

// ----------------------------------------------------------------------------
// CHỦ ĐỀ 3.2: HỆ THỨC LƯỢNG TRONG TAM GIÁC (BÀI 6)
// ----------------------------------------------------------------------------
#lesson-header("3.2 (Chương III — Bài 6)", "HỆ THỨC LƯỢNG TRONG TAM GIÁC & GIẢI TAM GIÁC", "P.I: Câu 9, 10 | P.III: Câu 4 TLN | P.IV: Câu 2 TL", "2,00 điểm")

*1. Định lí Côsin, Định lí Sin, Đường trung tuyến & 5 Công thức Diện tích (Câu 9, 10 P.I & Câu 4 P.III)*
Cho $Delta A B C$ có ba cạnh $B C = a, C A = b, A B = c$; ba đường cao $h_a, h_b, h_c$; ba đường trung tuyến $m_a, m_b, m_c$; bán kính đường tròn ngoại tiếp $R$; bán kính đường tròn nội tiếp $r$; nửa chu vi $p = frac(a + b + c, 2)$ và diện tích $S$:
- *Định lí Côsin:*
  $ a^2 = b^2 + c^2 - 2 b c cos A #h(12pt) ; #h(12pt) b^2 = c^2 + a^2 - 2 c a cos B #h(12pt) ; #h(12pt) c^2 = a^2 + b^2 - 2 a b cos C $
  *Hệ quả tính góc:* $cos A = frac(b^2 + c^2 - a^2, 2 b c)$ ; #h(8pt) $cos B = frac(a^2 + c^2 - b^2, 2 a c)$ ; #h(8pt) $cos C = frac(a^2 + b^2 - c^2, 2 a b)$.
- *Định lí Sin:*
  $ frac(a, sin A) = frac(b, sin B) = frac(c, sin C) = 2 R #h(14pt) arrow.r.double #h(14pt) a = 2 R sin A comma #h(6pt) R = frac(a, 2 sin A) $
- *Công thức độ dài đường trung tuyến:*
  $ m_a^2 = frac(b^2 + c^2, 2) - frac(a^2, 4) = frac(2(b^2 + c^2) - a^2, 4) #h(12pt) ; #h(12pt) m_b^2 = frac(2(a^2 + c^2) - b^2, 4) #h(12pt) ; #h(12pt) m_c^2 = frac(2(a^2 + b^2) - c^2, 4) $
- *5 Công thức tính diện tích tam giác $S$:*
  $ S = frac(1, 2) a h_a = frac(1, 2) b c sin A = frac(a b c, 4 R) = p r = sqrt(p(p - a)(p - b)(p - c)) $

#align(center)[#image("assets/triangle_relations.svg", width: 99%)]

*2. Phương pháp giải 3 bài toán thực tiễn kinh điển (Trọng tâm Câu 2 Tự luận — 1,0 điểm & Câu 4 TLN)*
- *Bài toán 1 (Đo khoảng cách $A B$ qua hồ nước / đồi núi):* Chọn điểm $C$ nhìn thấy cả $A, B$; đo $C A = b, C B = a$ và góc $hat(A C B) = gamma$. Áp dụng *Định lí Côsin* trong $Delta A B C$: $A B = sqrt(a^2 + b^2 - 2 a b cos gamma)$.
- *Bài toán 2 (Đo chiều cao tháp $C H = h$ khi không tới được chân tháp $H$):* Đứng tại $A$ và $B$ thẳng hàng với $H$ ($A B = d$), ngắm đỉnh $C$ dưới góc nâng $hat(C A H) = alpha$ và $hat(C B H) = beta$ ($alpha < beta$). Trong $Delta A B C$ có $hat(A C B) = beta - alpha$. Áp dụng *Định lí Sin*: $frac(B C, sin alpha) = frac(A B, sin(beta - alpha)) arrow.r.double B C = frac(d sin alpha, sin(beta - alpha))$. Trong $Delta B C H$ vuông tại $H$: *$h = C H = B C sin beta = frac(d sin alpha sin beta, sin(beta - alpha))$*.
- *Bài toán 3 (Hai tàu thủy xuất phát từ cảng $O$):* Tàu 1 chạy tốc độ $v_1$, tàu 2 chạy tốc độ $v_2$ theo hai hướng hợp với nhau góc $alpha$. Sau thời gian $t$, quãng đường hai tàu đi được là $O A = v_1 t$ và $O B = v_2 t$. Khoảng cách giữa hai tàu là $A B = sqrt(O A^2 + O B^2 - 2 dot O A dot O B dot cos alpha)$.

// ----------------------------------------------------------------------------
// CHỦ ĐỀ 4.1: KHÁI NIỆM VECTƠ (BÀI 7)
// ----------------------------------------------------------------------------
#lesson-header("4.1 (Chương IV — Bài 7)", "CÁC KHÁI NIỆM MỞ ĐẦU VỀ VECTƠ", "Phần I: Câu 11 (NB), Câu 12 (TH)", "0,50 điểm")

*1. Các khái niệm cơ bản về Vectơ (Câu 11 Phần I)*
- *Vectơ:* Là một đoạn thẳng có hướng. Vectơ có điểm đầu (gốc) $A$, điểm cuối (ngọn) $B$ được kí hiệu là $arrow(A B)$. Vectơ còn được kí hiệu bằng chữ thường có mũi tên: $arrow(a), arrow(b), arrow(x), arrow(y)$.
- *Giá của vectơ $arrow(A B)$* (với $A != B$): Là đường thẳng $A B$ đi qua điểm đầu và điểm cuối của vectơ đó.
- *Độ dài của vectơ:* Là khoảng cách giữa điểm đầu và điểm cuối: $|arrow(A B)| = A B$. Vectơ có độ dài bằng $1$ gọi là *vectơ đơn vị*.
- *Hai vectơ cùng phương:* Hai vectơ được gọi là *cùng phương* nếu giá của chúng *song song hoặc trùng nhau*. Hai vectơ cùng phương thì chỉ có thể *cùng hướng* hoặc *ngược hướng*.
  - *Tính chất thẳng hàng:* Ba điểm phân biệt $A, B, C$ thẳng hàng $arrow.l.r.double$ hai vectơ $arrow(A B)$ và $arrow(A C)$ cùng phương.
- *Hai vectơ bằng nhau ($arrow(a) = arrow(b)$):* Hai vectơ $arrow(a)$ và $arrow(b)$ bằng nhau nếu chúng *cùng hướng* và có *cùng độ dài*:
  $ arrow(a) = arrow(b) arrow.l.r.double cases(arrow(a) " và " arrow(b) " cùng hướng", |arrow(a)| = |arrow(b)|) $
- *Hai vectơ đối nhau:* Cùng độ dài nhưng *ngược hướng* (VD: $arrow(A B)$ và $arrow(B A)$).
- *Vectơ-không ($arrow(0)$):* Là vectơ có điểm đầu và điểm cuối trùng nhau ($arrow(0) = arrow(A A) = arrow(B B)$). Độ dài $|arrow(0)| = 0$, và theo quy ước chuẩn SGK: *Vectơ-không ($arrow(0)$) cùng phương và cùng hướng với mọi vectơ!*

*2. Nhận diện & Chứng minh hai vectơ bằng nhau trong Hình học (Câu 12 Phần I)*

#align(center)[#image("assets/vector_concepts.svg", width: 99%)]

#trap-box("3 Cái Bẫy Hay Sai Nhất về Vectơ ở Câu 11 & Câu 12 Phần I", [
  • *Bẫy 1:* Tứ giác $A B C D$ là hình bình hành $arrow.l.r.double arrow(A B) = arrow(D C)$ (*chú ý đúng chiều đỉnh*: $A arrow.r B$ ứng với $D arrow.r C$; nếu viết $arrow(A B) = arrow(C D)$ là *SAI* vì hai vectơ đó ngược hướng!).\
  • *Bẫy 2:* Trong tam giác đều $A B C$ cạnh $a$, ta có $|arrow(A B)| = |arrow(A C)| = a$, nhưng *$arrow(A B) != arrow(A C)$* vì hai vectơ này không cùng hướng!\
  • *Bẫy 3:* Hai vectơ có độ dài bằng nhau ($|arrow(a)| = |arrow(b)|$) hoặc cùng phương chưa chắc đã bằng nhau; phải thỏa mãn *đồng thời cả 2 điều kiện*: *cùng hướng* VÀ *cùng độ dài*!
])

#pagebreak()
