#import "template.typ": *

// ============================================================================
// PHẦN E: BỘ 02 ĐỀ KIỂM TRA GIỮA HỌC KÌ I NĂM HỌC 2026–2027 CHUẨN HÓA 100% MA TRẬN
// ============================================================================

= PHẦN E. BỘ 02 ĐỀ KIỂM TRA GIỮA HỌC KÌ I (2026–2027) CHUẨN MA TRẬN ĐẶC TẢ

// ============================================================================
// ĐỀ KIỂM TRA SỐ 01 (MÃ ĐỀ 101)
// ============================================================================

== E.1. Đề Kiểm Tra Giữa Học Kì I Năm Học 2026–2027 — Đề Số 01 (Mã Đề 101)

#block(
  width: 100%,
  fill: rgb("#F8FAFC"),
  stroke: 1pt + c-navy,
  radius: 6pt,
  inset: (x: 12pt, y: 8pt),
)[
  #grid(
    columns: (1fr, 1.25fr),
    align: (center + horizon, center + horizon),
    [
      *TRƯỜNG THPT HÀ HUY TẬP*\
      *TỔ TOÁN – TIN*\
      _(Đề chính thức Số 01 — Mã đề 101)_
    ],
    [
      *ĐỀ KIỂM TRA GIỮA HỌC KÌ I NĂM HỌC 2026–2027*\
      *MÔN: TOÁN, LỚP 10 — Thời gian làm bài: 90 phút*\
      *Hình thức: 70% Trắc nghiệm (7,0 đ) + 30% Tự luận (3,0 đ)*
    ]
  )
]

#section-heading("PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (3,0 điểm — từ Câu 1 đến Câu 12)")
_Mỗi câu hỏi thí sinh chỉ chọn một phương án đúng (0,25 điểm/câu)._

#mcq(1, badge("1.1-NB"), [Trong các phát biểu dưới đây, phát biểu nào là một *mệnh đề toán học*?],
  [Bạn có thích học môn Toán lớp 10 không?],
  [Phương trình $x^2 + 4 = 0$ vô nghiệm trên tập số thực $RR$.],
  [Hãy cố gắng làm bài kiểm tra giữa kì thật cẩn thận!],
  [$3 x - 7 > 2$.], cols: 2)

#mcq(2, badge("1.1-NB"), [Cho mệnh đề $P: "“" forall x in RR, x^2 - 4 x + 5 > 0 "”"$. Mệnh đề phủ định $overline(P)$ của mệnh đề $P$ là:],
  [$overline(P): "“" forall x in RR, x^2 - 4 x + 5 <= 0 "”"$.],
  [$overline(P): "“" exists x in RR, x^2 - 4 x + 5 < 0 "”"$.],
  [$overline(P): "“" exists x in RR, x^2 - 4 x + 5 <= 0 "”"$.],
  [$overline(P): "“" exists x in.not RR, x^2 - 4 x + 5 <= 0 "”"$.], cols: 2)

#mcq(3, badge("1.2-NB"), [Hãy viết tập hợp $A = \{x in ZZ | (x + 2)(x^2 - 9)(2 x - 3) = 0\}$ bằng cách liệt kê các phần tử:],
  [$A = \{-3; -2; 3; frac(3, 2)\}$.],
  [$A = \{-3; -2; 3\}$.],
  [$A = \{-2; 3\}$.],
  [$A = \{-3; 2; 3\}$.], cols: 4)

#mcq(4, badge("1.3-NB"), [Cho hai tập hợp $A$ và $B$ được biểu diễn bằng hai hình elip giao nhau trên biểu đồ Ven. Phần hình phẳng gồm tất cả các phần tử thuộc $A$ *hoặc* thuộc $B$ (lấy toàn bộ cả hai elip) biểu diễn tập hợp nào sau đây?],
  [$A inter B$.], [$A union B$.], [$A backslash B$.], [$B backslash A$.], cols: 4)

#mcq(5, badge("2.1-NB"), [Trong các bất phương trình sau đây, bất phương trình nào là *bất phương trình bậc nhất hai ẩn*?],
  [$x^2 + 2 y <= 5$.],
  [$2 x - 5 y + 3 > 0$.],
  [$3 x y - y < 4$.],
  [$x + y - 2 z >= 1$.], cols: 2)

#mcq(6, badge("2.2-NB"), [Cặp số $(x_0; y_0)$ nào dưới đây thuộc *miền nghiệm* của hệ bất phương trình bậc nhất hai ẩn $cases(2 x + y <= 5, x - 2 y + 4 > 0)$?],
  [$(1; 2)$.], [$(3; 1)$.], [$(-2; 3)$.], [$(2; 3)$.], cols: 4)

#mcq(7, badge("3.1-NB"), [Cho góc $alpha$ thỏa mãn $0^degree <= alpha <= 180^degree$. Trong các hệ thức liên hệ giữa hai góc bù nhau dưới đây, hệ thức nào *ĐÚNG*?],
  [$cos(180^degree - alpha) = cos alpha$.],
  [$sin(180^degree - alpha) = -sin alpha$.],
  [$cos(180^degree - alpha) = -cos alpha$.],
  [$tan(180^degree - alpha) = tan alpha$.], cols: 2)

#mcq(8, badge("3.1-TH"), [Cho góc tù $alpha$ ($90^degree < alpha < 180^degree$) thỏa mãn $sin alpha = frac(4, 5)$. Giá trị của $cos alpha$ bằng:],
  [$frac(3, 5)$.], [$-frac(3, 5)$.], [$-frac(4, 3)$.], [$frac(1, 5)$.], cols: 4)

#mcq(9, badge("3.2-NB"), [Cho tam giác $A B C$ có độ dài ba cạnh $B C = a, A C = b, A B = c$. Khẳng định nào dưới đây là *ĐÚNG*?],
  [$b^2 = a^2 + c^2 + 2 a c cos B$.],
  [$b^2 = a^2 + c^2 - 2 a c cos B$.],
  [$S_(Delta A B C) = a c sin B$.],
  [$b^2 = a^2 + c^2 - a c cos B$.], cols: 2)

#mcq(10, badge("3.2-TH"), [Cho tam giác $A B C$ có $A B = 4, A C = 6$ và góc $hat(B A C) = 120^degree$. Độ dài cạnh $B C$ của tam giác $A B C$ bằng:],
  [$sqrt(28)$.], [$2sqrt(19)$.], [$2sqrt(7)$.], [$76$.], cols: 4)

#mcq(11, badge("4.1-NB"), [Khẳng định nào dưới đây là *ĐÚNG* khi nói về vectơ?],
  [Vectơ-không ($arrow(0)$) cùng phương và cùng hướng với mọi vectơ.],
  [Hai vectơ cùng phương với nhau thì luôn bằng nhau.],
  [Hai vectơ có cùng độ dài thì luôn cùng hướng.],
  [Hai vectơ $arrow(A B)$ và $arrow(B A)$ là hai vectơ bằng nhau.], cols: 1)

#mcq(12, badge("4.1-TH"), [Cho hình bình hành $A B C D$ có tâm là $O$. Trong các khẳng định sau, khẳng định nào *SAI*?],
  [$arrow(A B) = arrow(D C)$.],
  [$arrow(A O) = arrow(O C)$.],
  [$arrow(A D) = arrow(C B)$.],
  [$|arrow(A B)| = |arrow(C D)|$.], cols: 4)

#section-heading("PHẦN II. Câu trắc nghiệm đúng sai (2,0 điểm — Câu 1 và Câu 2)")
_Trong mỗi ý *a), b), c), d)* ở mỗi câu, thí sinh chọn *Đúng* hoặc *Sai*. (Đúng 1 ý: 0,1đ; 2 ý: 0,25đ; 3 ý: 0,5đ; 4 ý: 1,0đ)._

#tf-question(
  "1",
  "Mục 1.2 & 1.3: Tập hợp & Các phép toán trên tập hợp",
  [Cho hai tập hợp $A = \{x in RR | -3 <= x < 2\}$ và $B = (-1; 5]$ trên trục số thực $RR$, cùng tập hợp chứa tham số $M = [m; m + 2]$ (với $m in RR$).],
  none,
  [Dùng kí hiệu nửa khoảng, tập hợp $A$ được viết là $A = [-3; 2)$, trong đó $-3 in A$ và $2 in.not A$.],
  [Tập hợp các số nguyên thuộc cả tập $A$ và tập $NN$ là $A inter NN = \{0; 1; 2\}$.],
  [Thực hiện phép toán trên $RR$: $A inter B = (-1; 2)$, $A union B = [-3; 5]$ và $C_(RR) A = (-infinity; -3) union [2; +infinity)$.],
  [Có đúng $3$ giá trị nguyên của tham số $m$ để $M subset A$.],
)

#tf-question(
  "2",
  "Mục 2.1: Bất phương trình bậc nhất hai ẩn & Thực tế",
  [Cho bất phương trình bậc nhất hai ẩn $x + 2 y <= 4$ có miền nghiệm được biểu diễn trên mặt phẳng tọa độ $O x y$ như hình vẽ bên dưới (phần không bị gạch chéo, kể cả bờ $d$).],
  image("assets/exam1_geometry_bpt.svg", width: 47%),
  [Cặp số $(1; 1)$ là một nghiệm của bất phương trình $x + 2 y <= 4$, còn cặp số $(3; 2)$ không phải là nghiệm.],
  [Đường thẳng bờ $d: x + 2 y = 4$ đi qua hai điểm $A(4; 0)$ và $B(0; 2)$.],
  [Miền nghiệm của bất phương trình $x + 2 y <= 4$ là nửa mặt phẳng bờ $d$ *không chứa* gốc tọa độ $O(0; 0)$.],
  [Bạn Lan có $40.000$ đồng đi mua $x$ chiếc bút chì (giá $10.000$ đồng/chiếc) và $y$ quyển sổ tay (giá $20.000$ đồng/quyển). Điều kiện để bạn Lan không chi vượt quá số tiền đang có được biểu thị bởi bất phương trình $x + 2 y <= 4$ (với $x, y in NN$).],
)

#section-heading("PHẦN III. Câu trắc nghiệm trả lời ngắn (2,0 điểm — từ Câu 1 đến Câu 4)")
_Mỗi câu trả lời đúng được 0,50 điểm._

- *Câu 1* #badge("1.2-TH")*:* Cho tập hợp $A = \{x in NN | x < 4\}$. Hỏi tập hợp $A$ có tất cả bao nhiêu tập hợp con?
- *Câu 2* #badge("1.3-VD")*:* Lớp 10A2 của trường THPT Hà Huy Tập có $40$ học sinh, trong đó có $22$ học sinh tham gia câu lạc bộ Toán học, $18$ học sinh tham gia câu lạc bộ Tin học và $8$ học sinh không tham gia câu lạc bộ nào trong hai câu lạc bộ trên. Hỏi có bao nhiêu học sinh của lớp 10A2 tham gia đồng thời *cả hai* câu lạc bộ Toán học và Tin học?
- *Câu 3* #badge("3.1-VD")*:* Cho góc $alpha in (0^degree; 180^degree)$ thỏa mãn $tan alpha = 2$. Tính giá trị của biểu thức $P = frac(2 sin alpha + 5 cos alpha, 2 sin alpha - cos alpha)$.
- *Câu 4* #badge("3.2-TH")*:* Một mảnh vườn hình tam giác $A B C$ có hai cạnh $A B = 10" m", A C = 16" m"$ và góc xen giữa $hat(B A C) = 30^degree$. Tính diện tích của mảnh vườn đó theo đơn vị mét vuông ($"m"^2$).

#section-heading("PHẦN IV. Tự luận (3,0 điểm — Câu 1, Câu 2 và Câu 3)")

- *Câu 1 (1,0 điểm — MĐ2 / Mục 1.3 Thông hiểu):* Cho hai tập hợp số thực $A = [-4; 2)$ và $B = (-1; 5]$. Hãy xác định và biểu diễn trên trục số các tập hợp sau: $A inter B$, $A union B$, $A backslash B$ và $C_(RR) A$.
- *Câu 2 (1,0 điểm — MĐ2 / Mục 3.2 Vận dụng):* Để đo khoảng cách giữa hai bến thuyền $A$ và $B$ nằm ở hai bên một cù lao trên sông (không thể căng thước đo trực tiếp từ $A$ đến $B$), người ta chọn một vị trí $C$ trên bờ sông sao cho nhìn thấy cả $A$ và $B$. Tiến hành đo đạc, người ta thu được $C A = 80" m"$, $C B = 50" m"$ và góc $hat(A C B) = 60^degree$.\
  *a)* Tính khoảng cách giữa hai bến thuyền $A$ và $B$.\
  *b)* Tính diện tích mặt nước giới hạn bởi tam giác $A B C$ (làm tròn đến hàng phần mười của $"m"^2$).
- *Câu 3 (1,0 điểm — MĐ3 / Mục 2.2 Vận dụng cao):* Một xưởng sản xuất đồ gỗ mỹ nghệ dự định đóng hai loại bàn học kiểu I và kiểu II. Để đóng $1$ chiếc bàn kiểu I cần $3" m"^2$ gỗ thông và $2$ giờ công thợ, thu được tiền lãi là $500$ nghìn đồng. Để đóng $1$ chiếc bàn kiểu II cần $2" m"^2$ gỗ thông và $4$ giờ công thợ, thu được tiền lãi là $600$ nghìn đồng. Biết trong tuần này xưởng chỉ có tối đa $18" m"^2$ gỗ thông và $20$ giờ công thợ. Hỏi xưởng cần đóng bao nhiêu chiếc bàn mỗi kiểu để tổng số tiền lãi thu được trong tuần là lớn nhất? Tính số tiền lãi lớn nhất đó.

#v(2pt)
#solution-card("ĐÁP ÁN & HƯỚNG DẪN CHẤM CHI TIẾT — ĐỀ KIỂM TRA SỐ 01 (MÃ ĐỀ 101)", [
  #set text(size: 8.4pt)
  *1. PHẦN I (3,00 điểm — 0,25 đ/câu):*\
  #table(
    columns: (1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr),
    align: center + horizon,
    stroke: 0.5pt + c-border,
    fill: (x, y) => if calc.even(y) { rgb("#EFF6FF") } else { white },
    inset: 3pt,
    [*1. B*], [*2. C*], [*3. B*], [*4. B*], [*5. B*], [*6. A*], [*7. C*], [*8. B*], [*9. B*], [*10. B*], [*11. A*], [*12. C*],
  )
  _Giải nhanh các câu tính toán Phần I:_ *Câu 3:* Nghiệm $x in \{-3; -2; 3; 3/2\}$, vì $x in ZZ$ nên loại $3/2 arrow.r.double A = \{-3; -2; 3\}$. *Câu 6:* Thay $(1; 2)$ vào hệ: $2(1) + 2 = 4 <= 5$ (đúng) và $1 - 2(2) + 4 = 1 > 0$ (đúng). *Câu 8:* Vì $90^degree < alpha < 180^degree arrow.r.double cos alpha = -sqrt(1 - (4/5)^2) = -3/5$. *Câu 10:* $B C = sqrt(4^2 + 6^2 - 2 dot 4 dot 6 cos 120^degree) = sqrt(52 + 24) = sqrt(76) = 2sqrt(19)$. *Câu 12:* Trong hình bình hành $A B C D$, $arrow(A D) = arrow(B C) != arrow(C B)$.

  #v(1.5pt)
  *2. PHẦN II (2,00 điểm):*\
  • *Câu 1:* *a) Đúng | b) Sai | c) Đúng | d) Đúng.* _(Ý b sai vì $2 in.not A$ nên $A inter NN = \{0; 1\}$ chỉ có $2$ phần tử; ý d đúng vì $M subset A arrow.l.r.double -3 <= m$ và $m + 2 < 2 arrow.l.r.double -3 <= m < 0 arrow.r.double m in \{-3; -2; -1\}$ có đúng $3$ giá trị nguyên; tại $m = 0$ thì $2 in M$ nhưng $2 in.not A$)_. \
  • *Câu 2:* *a) Đúng | b) Đúng | c) Sai | d) Đúng.* _(Ý c sai vì thay $O(0; 0)$ vào $0 + 2(0) = 0 <= 4$ luôn đúng, nên miền nghiệm *có chứa* gốc tọa độ $O$; ý d: $10.000 x + 20.000 y <= 40.000 arrow.l.r.double x + 2 y <= 4$)_.

  #v(1.5pt)
  *3. PHẦN III (2,00 điểm — 0,50 đ/câu):*\
  • *Câu 1:* Điền *`16`* _($A = \{0; 1; 2; 3\}$ có $4$ phần tử $arrow.r.double$ số tập con là $2^4 = 16$)_. #h(8pt)
  • *Câu 2:* Điền *`8`* _($n(T union T i) = 40 - 8 = 32 arrow.r.double n(T inter T i) = 22 + 18 - 32 = 8$)_.\
  • *Câu 3:* Điền *`3`* _(Chia cả tử và mẫu cho $cos alpha$: $P = frac(2 tan alpha + 5, 2 tan alpha - 1) = frac(2 dot 2 + 5, 2 dot 2 - 1) = frac(9, 3) = 3$)_. #h(8pt)
  • *Câu 4:* Điền *`40`* _($S = frac(1, 2) A B dot A C sin 30^degree = frac(1, 2) dot 10 dot 16 dot frac(1, 2) = 40" m"^2$)_.

  #v(1.5pt)
  *4. PHẦN IV – TỰ LUẬN (3,00 điểm):*\
  • *Câu 1 (1,00 đ):* Biểu diễn đúng trên trục số và tìm đúng mỗi tập hợp được *0,25 đ*:
    – *$A inter B = (-1; 2)$* *(0,25 đ)*; #h(6pt) – *$A union B = [-4; 5]$* *(0,25 đ)*; #h(6pt) – *$A backslash B = [-4; -1]$* _(do $-1 in.not B$)_ *(0,25 đ)*; #h(6pt) – *$C_(RR) A = (-infinity; -4) union [2; +infinity)$* *(0,25 đ)*.\
  • *Câu 2 (1,00 đ):*
    – a) Áp dụng Định lí Côsin trong $Delta A B C$: $A B^2 = 80^2 + 50^2 - 2 dot 80 dot 50 dot cos 60^degree = 4900$ *(0,25 đ)* $arrow.r.double$ Khoảng cách giữa hai bến thuyền: *$A B = 70" m"$* *(0,25 đ)*.\
    – b) Diện tích tam giác $A B C$: $S = frac(1, 2) dot C A dot C B dot sin 60^degree = frac(1, 2) dot 80 dot 50 dot frac(sqrt(3), 2) = #strong[$1000sqrt(3) approx 1732,1" m"^2$]$. *(0,50 đ)*\
  • *Câu 3 (1,00 đ):*
    – Gọi $x, y$ ($x, y in NN$) là số bàn kiểu I và kiểu II cần đóng. Hệ BPT: $cases(x >= 0 comma y >= 0, 3 x + 2 y <= 18, 2 x + 4 y <= 20 arrow.l.r.double x + 2 y <= 10)$. Hàm lợi nhuận: $F(x; y) = 500 x + 600 y$ (nghìn đồng). *(0,25 đ)*\
    – Miền nghiệm là tứ giác lồi $O A B C$ với 4 đỉnh: $O(0; 0)$, $A(6; 0)$, $B(4; 3)$ (giao của $3 x + 2 y = 18$ và $x + 2 y = 10$), và $C(0; 5)$. *(0,25 đ)*\
    – Giá trị tại các đỉnh: $F(0; 0) = 0$; $F(6; 0) = 3000$; *$F(4; 3) = 500 dot 4 + 600 dot 3 = 3800$*; $F(0; 5) = 3000$. *(0,25 đ)*\
    – *Kết luận:* Đóng *$4$ chiếc bàn kiểu I* và *$3$ chiếc bàn kiểu II* để thu được tiền lãi lớn nhất là *$3.800$ nghìn đồng ($3,8$ triệu đồng)*. *(0,25 đ)*
])

#pagebreak()

// ============================================================================
// ĐỀ KIỂM TRA SỐ 02 (MÃ ĐỀ 102)
// ============================================================================

== E.2. Đề Kiểm Tra Giữa Học Kì I Năm Học 2026–2027 — Đề Số 02 (Mã Đề 102)

#block(
  width: 100%,
  fill: rgb("#F8FAFC"),
  stroke: 1pt + c-navy,
  radius: 6pt,
  inset: (x: 12pt, y: 8pt),
)[
  #grid(
    columns: (1fr, 1.25fr),
    align: (center + horizon, center + horizon),
    [
      *TRƯỜNG THPT HÀ HUY TẬP*\
      *TỔ TOÁN – TIN*\
      _(Đề chính thức Số 02 — Mã đề 102)_
    ],
    [
      *ĐỀ KIỂM TRA GIỮA HỌC KÌ I NĂM HỌC 2026–2027*\
      *MÔN: TOÁN, LỚP 10 — Thời gian làm bài: 90 phút*\
      *Hình thức: 70% Trắc nghiệm (7,0 đ) + 30% Tự luận (3,0 đ)*
    ]
  )
]

#section-heading("PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (3,0 điểm — từ Câu 1 đến Câu 12)")

#mcq(1, badge("1.1-NB"), [Cho mệnh đề chứa biến $P(n): "“" n^2 + 1 " chia hết cho " 5 "”"$ với $n in NN$. Mệnh đề nào dưới đây là *mệnh đề ĐÚNG*?],
  [$P(1)$.], [$P(2)$.], [$P(4)$.], [$P(5)$.], cols: 4)

#mcq(2, badge("1.1-NB"), [Cho mệnh đề $P: "“" exists x in RR, 2 x - 3 = 0 "”"$. Mệnh đề phủ định $overline(P)$ của mệnh đề $P$ là:],
  [$overline(P): "“" forall x in RR, 2 x - 3 != 0 "”"$.],
  [$overline(P): "“" exists x in RR, 2 x - 3 != 0 "”"$.],
  [$overline(P): "“" forall x in RR, 2 x - 3 = 0 "”"$.],
  [$overline(P): "“" forall x in RR, 2 x - 3 > 0 "”"$.], cols: 2)

#mcq(3, badge("1.2-NB"), [Cho tập hợp $B = \{x in NN^* | x <= 4\}$. Tập hợp $B$ được viết bằng cách liệt kê các phần tử là:],
  [$B = \{0; 1; 2; 3; 4\}$.],
  [$B = \{1; 2; 3; 4\}$.],
  [$B = \{1; 2; 3\}$.],
  [$B = (0; 4]$.], cols: 4)

#mcq(4, badge("1.3-NB"), [Cho hai tập hợp $A = \{1; 2; 4; 6\}$ và $B = \{2; 3; 4; 8\}$. Tập hợp giao $A inter B$ bằng:],
  [$\{1; 6\}$.], [$\{2; 4\}$.], [$\{3; 8\}$.], [$\{1; 2; 3; 4; 6; 8\}$.], cols: 4)

#mcq(5, badge("2.1-NB"), [Cặp số $(x_0; y_0)$ nào dưới đây là một *nghiệm* của bất phương trình bậc nhất hai ẩn $3 x - y + 2 < 0$?],
  [$(0; 0)$.], [$(1; 2)$.], [$(-2; 1)$.], [$(2; 5)$.], cols: 4)

#mcq(6, badge("2.2-NB"), [Trong các hệ dưới đây, hệ nào là một *hệ bất phương trình bậc nhất hai ẩn*?],
  [$cases(x - 3 y <= 6, 2 x + y > -1)$],
  [$cases(x^2 + y^2 <= 4, x - y >= 0)$],
  [$cases(2 x - y = 1, x + 3 y = 5)$],
  [$cases(x + 2 y - z < 3, 2 x + y > 0)$], cols: 4)

#mcq(7, badge("3.1-NB"), [Giá trị của biểu thức $M = sin 30^degree + cos 120^degree + cot 45^degree$ bằng:],
  [$1$.], [$2$.], [$0$.], [$frac(3, 2)$.], cols: 4)

#mcq(8, badge("3.1-TH"), [Cho góc nhọn $alpha$ ($0^degree < alpha < 90^degree$) biết $cos alpha = frac(3, 5)$. Giá trị của $tan alpha$ bằng:],
  [$frac(4, 5)$.], [$frac(4, 3)$.], [$-frac(4, 3)$.], [$frac(3, 4)$.], cols: 4)

#mcq(9, badge("3.2-NB"), [Cho tam giác $A B C$ có các cạnh $B C = a, A C = b, A B = c$ và diện tích là $S$. Công thức nào dưới đây là *ĐÚNG*?],
  [$S = frac(1, 2) a b cos C$.],
  [$S = frac(1, 2) a b sin C$.],
  [$S = a b sin C$.],
  [$S = frac(1, 2) a b sin A$.], cols: 4)

#mcq(10, badge("3.2-TH"), [Cho tam giác $A B C$ có góc $hat(B) = 45^degree$, góc $hat(C) = 60^degree$ và cạnh $A C = b = 4sqrt(2)$. Độ dài cạnh $A B = c$ của tam giác $A B C$ bằng:],
  [$4sqrt(3)$.], [$4sqrt(6)$.], [$8$.], [$2sqrt(6)$.], cols: 4)

#mcq(11, badge("4.1-NB"), [Hai vectơ khác vectơ-không được gọi là *cùng phương* khi và chỉ khi:],
  [Giá của chúng vuông góc với nhau.],
  [Giá của chúng song song hoặc trùng nhau.],
  [Chúng có độ dài bằng nhau.],
  [Chúng có cùng điểm đầu.], cols: 2)

#mcq(12, badge("4.1-TH"), [Cho lục giác đều $A B C D E F$ có tâm là $O$. Vectơ nào dưới đây *bằng* với vectơ $arrow(O A)$?],
  [$arrow(O D)$.], [$arrow(D O)$.], [$arrow(B C)$.], [$arrow(E F)$.], cols: 4)

#section-heading("PHẦN II. Câu trắc nghiệm đúng sai (2,0 điểm — Câu 1 và Câu 2)")

#tf-question(
  "1",
  "Mục 1.2 & 1.3: Tập hợp & Các phép toán trên tập hợp",
  [Cho tập hợp $A = \{x in RR | -1 < x <= 4\}$, tập hợp $B = [2; +infinity)$ và tập hợp chứa tham số $D = (m - 2; m + 1)$ (với $m in RR$).],
  none,
  [Sử dụng kí hiệu nửa khoảng, ta có $A = (-1; 4]$, tập rỗng $emptyset subset A$ và $-1 in.not A$.],
  [Biểu diễn trên trục số, tập hợp $A$ chứa đúng $6$ số nguyên.],
  [Ta có $A inter B = [2; 4]$, $A backslash B = (-1; 2)$ và phần bù $C_(RR) B = (-infinity; 2)$.],
  [Điều kiện của tham số $m$ để $A inter D = emptyset$ là $m <= -2$ hoặc $m >= 6$.],
)

#tf-question(
  "2",
  "Mục 2.1: Bất phương trình bậc nhất hai ẩn & Thực tế",
  [Cho bất phương trình bậc nhất hai ẩn $2 x + y >= 4$ có miền nghiệm là phần mặt phẳng không bị gạch chéo (kể cả bờ $d$) như hình vẽ bên dưới.],
  image("assets/exam2_geometry_bpt.svg", width: 56%),
  [Cặp số $(2; 1)$ là một nghiệm của bất phương trình $2 x + y >= 4$, còn gốc tọa độ $O(0; 0)$ không phải là nghiệm.],
  [Đường thẳng bờ $d: 2 x + y = 4$ cắt trục hoành tại điểm $A(2; 0)$ và cắt trục tung tại điểm $B(0; 4)$.],
  [Miền nghiệm của bất phương trình $2 x + y >= 4$ là nửa mặt phẳng bờ $d$ không chứa gốc tọa độ $O(0; 0)$ và *không kể đường thẳng bờ* $d$.],
  [Một đội tình nguyện cần quyên góp ít nhất $4$ triệu đồng bằng cách bán $x$ vé xem ca nhạc loại VIP (giá $200$ nghìn đồng/vé) và $y$ vé loại Thường (giá $100$ nghìn đồng/vé). Điều kiện để đội đạt chỉ tiêu quyên góp được mô tả bởi bất phương trình $2 x + y >= 40$ (với $x, y in NN$).],
)

#section-heading("PHẦN III. Câu trắc nghiệm trả lời ngắn (2,0 điểm — từ Câu 1 đến Câu 4)")

- *Câu 1* #badge("1.2-TH")*:* Cho tập hợp $M = \{x in ZZ | -2 <= x <= 2\}$. Hỏi tập hợp $M$ có tất cả bao nhiêu tập hợp con *khác tập rỗng*?
- *Câu 2* #badge("1.3-VD")*:* Một lớp học có $38$ học sinh, trong đó có $24$ học sinh giỏi môn Toán, $19$ học sinh giỏi môn Vật lí và $5$ học sinh không giỏi môn nào trong hai môn trên. Hỏi lớp đó có bao nhiêu học sinh *chỉ giỏi đúng môn Toán* (không giỏi môn Vật lí)?
- *Câu 3* #badge("3.1-VD")*:* Cho góc $alpha in (0^degree; 180^degree)$ thỏa mãn $cot alpha = 2$. Tính giá trị của biểu thức $Q = frac(5 sin alpha + 3 cos alpha, 3 sin alpha - cos alpha)$.
- *Câu 4* #badge("3.2-TH")*:* Cho tam giác $A B C$ có ba cạnh lần lượt là $a = 7, b = 8, c = 5$. Tính bán kính $r$ của đường tròn nội tiếp tam giác $A B C$ _(làm tròn kết quả đến hàng phần trăm)_.

#section-heading("PHẦN IV. Tự luận (3,0 điểm — Câu 1, Câu 2 và Câu 3)")

- *Câu 1 (1,0 điểm — MĐ2 / Mục 1.3 Thông hiểu):* Cho hai tập hợp $A = \{x in RR | -2 <= x <= 3\}$ và $B = (1; +infinity)$. Hãy viết tập hợp $A$ dưới dạng đoạn và xác định các tập hợp: $A inter B$, $A union B$, $A backslash B$, $C_(RR) B$.
- *Câu 2 (1,0 điểm — MĐ2 / Mục 3.2 Vận dụng):* Để xác định chiều cao $C H$ của một tháp truyền hình mà không thể tiến tới chân tháp $H$, người ta đặt giác kế tại hai điểm $A$ và $B$ thẳng hàng với chân tháp $H$ trên mặt đất nằm ngang (cùng phía so với $H$) cách nhau một đoạn $A B = 40" m"$. Từ $A$ và $B$, người ta ngắm đỉnh tháp $C$ với các góc nâng lần lượt là $hat(C A H) = 30^degree$ và $hat(C B H) = 45^degree$ (bỏ qua chiều cao của giác kế).\
  *a)* Tính khoảng cách $B C$ từ vị trí $B$ đến đỉnh tháp $C$ (làm tròn đến hàng phần mười của mét).\
  *b)* Tính chiều cao $C H$ của tháp truyền hình (làm tròn đến hàng phần mười của mét).
- *Câu 3 (1,0 điểm — MĐ3 / Mục 2.2 Vận dụng cao):* Một trang trại chăn nuôi cần thuê xe vận chuyển ít nhất $450$ con lợn và $35$ tấn cám. Nơi cho thuê xe chỉ có tối đa $12$ xe tải lớn và $10$ xe tải nhỏ. Một chiếc xe tải lớn có thể chở tối đa $50$ con lợn và $5$ tấn cám với giá thuê là $4$ triệu đồng/chuyến. Một chiếc xe tải nhỏ có thể chở tối đa $30$ con lợn và $1$ tấn cám với giá thuê là $2$ triệu đồng/chuyến. Hỏi trang trại cần thuê bao nhiêu xe mỗi loại để tổng chi phí thuê xe là thấp nhất? Tính chi phí thấp nhất đó.

#v(4pt)
#solution-card("ĐÁP ÁN & HƯỚNG DẪN CHẤM CHI TIẾT — ĐỀ KIỂM TRA SỐ 02 (MÃ ĐỀ 102)", [
  *1. PHẦN I (3,00 điểm — 0,25 đ/câu):*\
  #set text(size: 8.5pt)
  #table(
    columns: (1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr),
    align: center + horizon,
    stroke: 0.5pt + c-border,
    fill: (x, y) => if calc.even(y) { rgb("#EFF6FF") } else { white },
    inset: 3.5pt,
    [*1. B*], [*2. A*], [*3. B*], [*4. B*], [*5. C*], [*6. A*], [*7. A*], [*8. B*], [*9. B*], [*10. A*], [*11. B*], [*12. B*],
  )
  #set text(size: 8.9pt)
  _Giải nhanh các câu tính toán Phần I:_ *Câu 1:* Với $n = 2 arrow.r.double 2^2 + 1 = 5 dots.v 5$ (đúng). *Câu 5:* Thay $(-2; 1)$: $3(-2) - 1 + 2 = -5 < 0$ (đúng). *Câu 7:* $sin 30^degree + cos 120^degree + cot 45^degree = frac(1, 2) + (-frac(1, 2)) + 1 = 1$. *Câu 8:* $sin alpha = frac(4, 5) arrow.r.double tan alpha = frac(4, 3)$. *Câu 10:* Định lí Sin: $frac(c, sin 60^degree) = frac(b, sin 45^degree) arrow.r.double c = frac(4sqrt(2) dot (sqrt(3)/2), sqrt(2)/2) = 4sqrt(3)$. *Câu 12:* Tâm $O$ là trung điểm của đường chéo chính $A D$ nên $arrow(O A) = arrow(D O)$ (cùng hướng từ $D$ tới $A$ và cùng độ dài bằng bán kính đường tròn ngoại tiếp).

  #v(3pt)
  *2. PHẦN II (2,00 điểm):*\
  • *Câu 1:* *a) Đúng | b) Sai | c) Đúng | d) Đúng.*\
    _(Ý b sai vì $A inter ZZ = \{0; 1; 2; 3; 4\}$ chỉ có $5$ số nguyên; ý d đúng vì $A inter D = emptyset arrow.l.r.double m + 1 <= -1$ hoặc $m - 2 >= 4 arrow.l.r.double m <= -2$ hoặc $m >= 6$)_. \
  • *Câu 2:* *a) Đúng | b) Đúng | c) Sai | d) Đúng.*\
    _(Ý c sai vì BPT có dấu $>=$ nên miền nghiệm *có kể cả đường bờ* $d$; ý d đúng vì $200 x + 100 y >= 4000 arrow.l.r.double 2 x + y >= 40$)_.

  #v(3pt)
  *3. PHẦN III (2,00 điểm — 0,50 đ/câu):*\
  • *Câu 1:* Điền *`31`* _($M = \{-2; -1; 0; 1; 2\}$ có $5$ phần tử $arrow.r.double$ số tập con khác rỗng là $2^5 - 1 = 31$)_. #h(10pt)
  • *Câu 2:* Điền *`14`* _($n(T union L) = 38 - 5 = 33 arrow.r.double n(T inter L) = 24 + 19 - 33 = 10 arrow.r.double$ Chỉ giỏi Toán: $24 - 10 = 14$)_.\
  • *Câu 3:* Điền *`11`* _(Chia cả tử và mẫu cho $sin alpha$: $Q = frac(5 + 3 cot alpha, 3 - cot alpha) = frac(5 + 3 dot 2, 3 - 2) = 11$)_. #h(10pt)
  • *Câu 4:* Điền *`1,73`* _($p = frac(7+8+5, 2) = 10 arrow.r.double S = sqrt(10 dot 3 dot 2 dot 5) = 10sqrt(3) arrow.r.double r = frac(S, p) = sqrt(3) approx 1,73$)_.

  #v(3pt)
  *4. PHẦN IV – TỰ LUẬN (3,00 điểm):*\
  • *Câu 1 (1,00 đ):* Viết đúng *$A = [-2; 3]$* *(0,20 đ)*.\
    – *$A inter B = [-2; 3] inter (1; +infinity) = (1; 3]$* *(0,20 đ)*; #h(10pt) – *$A union B = [-2; 3] union (1; +infinity) = [-2; +infinity)$* *(0,20 đ)*;\
    – *$A backslash B = [-2; 3] backslash (1; +infinity) = [-2; 1]$* *(0,20 đ)*; #h(10pt) – *$C_(RR) B = RR backslash (1; +infinity) = (-infinity; 1]$* *(0,20 đ)*.\
  • *Câu 2 (1,00 đ):*\
    – a) Trong $Delta A B C$: $hat(A C B) = hat(C B H) - hat(C A H) = 45^degree - 30^degree = 15^degree$. *(0,25 đ)*\
      Áp dụng Định lí Sin trong $Delta A B C$: $frac(B C, sin 30^degree) = frac(A B, sin 15^degree) arrow.r.double B C = frac(40 dot sin 30^degree, sin 15^degree) = frac(20, sin 15^degree) approx #strong[$77,3" m"$]$. *(0,25 đ)*\
    – b) Trong $Delta B C H$ vuông tại $H$: chiều cao của tháp là $C H = B C dot sin 45^degree = frac(20 sin 45^degree, sin 15^degree) = 20(sqrt(3) + 1) approx #strong[$54,6" m"$]$. *(0,50 đ)*\
  • *Câu 3 (1,00 đ):*\
    – Gọi $x, y$ ($x, y in NN$) là số xe tải lớn và xe tải nhỏ cần thuê. Hệ BPT ràng buộc:\
      $cases(0 <= x <= 12 comma 0 <= y <= 10, 50 x + 30 y >= 450 arrow.l.r.double 5 x + 3 y >= 45, 5 x + y >= 35)$. Hàm chi phí cần tìm GTNN: $F(x; y) = 4 x + 2 y$ (triệu đồng). *(0,25 đ)*\
    – Miền nghiệm là ngũ giác lồi $A B C D E$ với các đỉnh: $A(6; 5)$ (giao của $5 x + 3 y = 45$ và $5 x + y = 35$), $B(9; 0)$, $C(12; 0)$, $D(12; 10)$ và $E(5; 10)$ (giao của $y = 10$ và $5 x + y = 35$). *(0,25 đ)*\
    – Tính chi phí tại các đỉnh: *$F(6; 5) = 4 dot 6 + 2 dot 5 = 34$*; $F(9; 0) = 36$; $F(12; 0) = 48$; $F(12; 10) = 68$; $F(5; 10) = 40$. *(0,25 đ)*\
    – *Kết luận:* Cần thuê *$6$ xe tải lớn* và *$5$ xe tải nhỏ* để chi phí thuê xe thấp nhất là *$34$ triệu đồng*. *(0,25 đ)*
])
