#import "template.typ": *

// ============================================================================
// PHẦN D — NGÂN HÀNG CÂU HỎI & BÀI TẬP PHÂN DẠNG CHUẨN BẢNG ĐẶC TẢ (75 BÀI)
// ============================================================================

= PHẦN D. NGÂN HÀNG CÂU HỎI & BÀI TẬP PHÂN DẠNG KÈM LỜI GIẢI CHI TIẾT

== D.1. Dạng thức 1 — 48 Câu Trắc nghiệm nhiều phương án lựa chọn (Gấp 4 lần đề thi)

=== Nhóm 1 (Vị trí Câu 1 – Câu 2 Phần I): Mệnh đề & Lượng từ ∀, ∃ (Bài 1 SGK)

#mcq("1", "NB", [Trong các câu dưới đây, câu nào là một *mệnh đề toán học*?],
  [Bạn đã làm xong bài tập Toán chưa?],
  [$x^2 - 4 x + 3 = 0$.],
  [Số $17$ là một số nguyên tố.],
  [Đề kiểm tra hôm nay hay quá!],
  cols: 2
)

#mcq("2", "NB", [Trong các phát biểu sau, phát biểu nào là *mệnh đề chứa biến*?],
  [$pi$ là một số vô tỉ.],
  [$2 x - 5 > 1$ (với $x in RR$).],
  [Tam giác đều có ba góc bằng $60^circle$.],
  [Hãy giữ trật tự trong phòng thi!],
  cols: 2
)

#mcq("3", "NB", [Cho mệnh đề chứa biến $P(x):$ “$x^2 - 3 x + 2 = 0$” với $x in RR$. Mệnh đề nào sau đây *đúng*?],
  [$P(0)$], [$P(1)$], [$P(-1)$], [$P(3)$],
  cols: 4
)

#mcq("4", "NB", [Mệnh đề phủ định của mệnh đề $P:$ *“Số $2026$ chia hết cho $4$”* là:],
  [Số $2026$ chia hết cho $2$.],
  [Số $2026$ là một số lẻ.],
  [Số $2026$ không chia hết cho $4$.],
  [Số $2026$ lớn hơn $4$.],
  cols: 2
)

#mcq("5", "NB", [Cho hai mệnh đề $P:$ *“Tứ giác $A B C D$ là hình thoi”* và $Q:$ *“Tứ giác $A B C D$ có hai đường chéo vuông góc với nhau”*. Mệnh đề đảo của mệnh đề $P arrow.r.double Q$ là:],
  [Nếu tứ giác $A B C D$ là hình thoi thì hai đường chéo vuông góc với nhau.],
  [Nếu tứ giác $A B C D$ có hai đường chéo vuông góc với nhau thì $A B C D$ là hình thoi.],
  [Tứ giác $A B C D$ là hình thoi khi và chỉ khi hai đường chéo vuông góc.],
  [Nếu tứ giác $A B C D$ không là hình thoi thì hai đường chéo không vuông góc.],
  cols: 1
)

#mcq("6", "NB", [Dùng kí hiệu $forall$ hoặc $exists$ để viết mệnh đề: *“Mọi số thực đều có bình phương không âm”*:],
  [$exists x in RR, x^2 >= 0$],
  [$forall x in RR, x^2 > 0$],
  [$forall x in RR, x^2 >= 0$],
  [$forall x in NN, x^2 >= 0$],
  cols: 4
)

#mcq("7", "NB", [Tìm mệnh đề phủ định $overline(P)$ của mệnh đề $P:$ “$forall x in RR, x^2 + 2 x + 5 > 0$”:],
  [$overline(P):$ “$forall x in RR, x^2 + 2 x + 5 <= 0$”],
  [$overline(P):$ “$exists x in RR, x^2 + 2 x + 5 < 0$”],
  [$overline(P):$ “$exists x in RR, x^2 + 2 x + 5 <= 0$”],
  [$overline(P):$ “$exists x notin RR, x^2 + 2 x + 5 <= 0$”],
  cols: 2
)

#mcq("8", "NB", [Trong các mệnh đề chứa lượng từ dưới đây, mệnh đề nào *đúng*?],
  [$forall x in RR, x^2 > 0$.],
  [$exists n in NN, n^2 = 3$.],
  [$forall n in NN, n^2 + 1$ không chia hết cho $3$.],
  [$exists x in QQ, x^2 = 2$.],
  cols: 2
)

=== Nhóm 2 (Vị trí Câu 3 – Câu 4 Phần I): Tập hợp & Biểu đồ Ven (Bài 2 SGK)

#mcq("9", "NB", [Viết tập hợp $A = {x in NN | x < 5}$ bằng cách liệt kê các phần tử:],
  [$A = {1; 2; 3; 4}$],
  [$A = {0; 1; 2; 3; 4}$],
  [$A = {0; 1; 2; 3; 4; 5}$],
  [$A = {1; 2; 3; 4; 5}$],
  cols: 2
)

#mcq("10", "NB", [Hãy liệt kê các phần tử của tập hợp $X = {x in ZZ | (x^2 - 4)(2 x - 3) = 0}$:],
  [$X = {-2; 2; 3/2}$],
  [$X = {-2; 2}$],
  [$X = {2}$],
  [$X = emptyset$],
  cols: 4
)

#mcq("11", "NB", [Cho tập hợp $B = {x in NN^* | x <= 4}$. Tập hợp $B$ viết dưới dạng liệt kê là:],
  [$B = {0; 1; 2; 3; 4}$],
  [$B = {1; 2; 3}$],
  [$B = {1; 2; 3; 4}$],
  [$B = [1; 4]$],
  cols: 4
)

#mcq("12", "NB", [Tập hợp $M = {0; 2; 4; 6; 8}$ được viết bằng cách chỉ ra tính chất đặc trưng là:],
  [$M = {x in NN | x <= 8}$],
  [$M = {2 k | k in NN, k <= 4}$],
  [$M = {2 k + 1 | k in NN, k <= 4}$],
  [$M = {2 k | k in ZZ, k <= 4}$],
  cols: 2
)

#mcq("13", "NB", [Trên biểu đồ Ven của hai tập hợp $A$ và $B$, phần chung nằm đồng thời trong cả hai đường cong khép kín $A$ và $B$ biểu diễn tập hợp nào?],
  [$A union B$], [$A inter B$], [$A without B$], [$B without A$],
  cols: 4
)

#mcq("14", "NB", [Cho hai tập hợp $A = {-1; 0; 2; 5}$ và $B = {0; 2; 4; 6}$. Tập hợp $A inter B$ bằng:],
  [${0; 2}$], [${-1; 5}$], [${-1; 0; 2; 4; 5; 6}$], [${4; 6}$],
  cols: 4
)

#mcq("15", "NB", [Cho tập hợp $A = {x in RR | -2 <= x < 5}$. Viết tập $A$ dưới dạng đoạn, khoảng, nửa khoảng:],
  [$(-2; 5)$], [$[-2; 5]$], [$[-2; 5)$], [$(-2; 5]$],
  cols: 4
)

#mcq("16", "NB", [Cho tập hợp $B subset A$ được biểu diễn bằng hai vòng tròn lồng nhau trên biểu đồ Ven. Phần hình vành khăn nằm trong $A$ nhưng nằm ngoài $B$ biểu diễn tập hợp nào?],
  [$A inter B$], [$A union B$], [$B without A$], [$C_A B$],
  cols: 4
)

=== Nhóm 3 (Vị trí Câu 5 – Câu 6 Phần I): BPT & Hệ BPT bậc nhất hai ẩn (Bài 3 & Bài 4 SGK)

#mcq("17", "NB", [Bất phương trình nào sau đây là *bất phương trình bậc nhất hai ẩn*?],
  [$2 x^2 - 3 y < 5$],
  [$3 x - 4 y >= 7$],
  [$x + 2 y - z <= 1$],
  [$x y + 2 x > 3$],
  cols: 4
)

#mcq("18", "NB", [Bất phương trình nào dưới đây *KHÔNG phải* là bất phương trình bậc nhất hai ẩn?],
  [$x - 5 y + 2 < 0$],
  [$2 y >= -3$],
  [$0 x + 0 y <= 4$],
  [$-3^2 x + y > 1$],
  cols: 4
)

#mcq("19", "NB", [Cặp số $(x_0; y_0)$ nào sau đây là một *nghiệm* của bất phương trình $2 x - 3 y < 4$?],
  [$(2; 0)$], [$(5; 2)$], [$(1; 2)$], [$(3; 0)$],
  cols: 4
)

#block(breakable: false)[
  #grid(
    columns: (1.35fr, 0.85fr),
    gutter: 10pt,
    align: (left + horizon, center + horizon),
    [
      *Câu 20.* #lv-badge("NB") Phần *không bị gạch chéo* (kể cả bờ) trong hình vẽ bên biểu diễn miền nghiệm của bất phương trình nào dưới đây?
      #v(4pt)
      #grid(
        columns: (1fr, 1fr),
        row-gutter: 4pt,
        [*A.* $3 x + 2 y >= 6$], [*B.* $3 x + 2 y <= 6$],
        [*C.* $2 x + 3 y <= 6$], [*D.* $3 x + 2 y < 6$],
      )
    ],
    [#image("assets/bank_bpt_graph1.svg", width: 100%)]
  )
]

#mcq("21", "NB", [Hệ nào dưới đây là một *hệ bất phương trình bậc nhất hai ẩn*?],
  [$cases(x + y^2 <= 4, 2 x - y > 1)$],
  [$cases(2 x - y <= 3, x + 4 y >= -2)$],
  [$cases(x + y = 2, 3 x - y = 1)$],
  [$cases(1/x + y > 0, x - y < 5)$],
  cols: 4
)

#mcq("22", "NB", [Điểm nào sau đây thuộc miền nghiệm của hệ bất phương trình $cases(x + y >= 2, 2 x - y <= 3)$?],
  [$M(0; 0)$], [$N(1; 2)$], [$P(3; 1)$], [$Q(-1; 2)$],
  cols: 4
)

#mcq("23", "NB", [Miền nghiệm của hệ bất phương trình $cases(x >= 0, y >= 0, x + y <= 4)$ trên mặt phẳng tọa độ $O x y$ là hình gì?],
  [Một nửa mặt phẳng], [Một tam giác], [Một hình chữ nhật], [Một ngũ giác],
  cols: 4
)

#mcq("24", "NB", [Cho hệ bất phương trình $cases(x - y > 0, x + 2 y <= 6, y >= 0)$. Cặp số nào sau đây *KHÔNG* là nghiệm của hệ?],
  [$(2; 1)$], [$(3; 0)$], [$(1; 2)$], [$(4; 1)$],
  cols: 4
)

=== Nhóm 4 (Vị trí Câu 7 – Câu 8 Phần I): Giá trị lượng giác góc 0° → 180° (Bài 5 SGK)

#mcq("25", "NB", [Giá trị chính xác của $cos 120^circle$ bằng:],
  [$1/2$], [$-1/2$], [$sqrt(3)/2$], [$-sqrt(3)/2$],
  cols: 4
)

#mcq("26", "NB", [Với mọi góc $alpha$ thỏa mãn $0^circle <= alpha <= 180^circle$, khẳng định nào sau đây *đúng*?],
  [$sin(180^circle - alpha) = -sin alpha$],
  [$cos(180^circle - alpha) = cos alpha$],
  [$sin(180^circle - alpha) = sin alpha$],
  [$tan(180^circle - alpha) = tan alpha$],
  cols: 2
)

#mcq("27", "NB", [Cho góc tù $alpha$ ($90^circle < alpha < 180^circle$). Khẳng định nào dưới đây *đúng* về dấu các giá trị lượng giác?],
  [$sin alpha > 0$ và $cos alpha > 0$],
  [$sin alpha < 0$ và $cos alpha < 0$],
  [$sin alpha > 0$ và $cos alpha < 0$],
  [$tan alpha > 0$ và $cot alpha < 0$],
  cols: 2
)

#mcq("28", "TH", [Cho góc $alpha$ thỏa mãn $sin alpha = 3/5$ và $90^circle < alpha < 180^circle$. Giá trị của $cos alpha$ là:],
  [$4/5$], [$-4/5$], [$2/5$], [$-3/4$],
  cols: 4
)

#mcq("29", "TH", [Cho góc $alpha in [0^circle; 180^circle]$ biết $cos alpha = -1/3$. Giá trị của biểu thức $P = 2 sin^2 alpha + 5 cos^2 alpha$ bằng:],
  [$7/3$], [$19/9$], [$5/3$], [$23/9$],
  cols: 4
)

#mcq("30", "TH", [Biết $tan alpha = 2$. Giá trị của biểu thức $A = (3 sin alpha - 2 cos alpha) / (sin alpha + cos alpha)$ bằng:],
  [$4/3$], [$8/3$], [$1/3$], [$-4/3$],
  cols: 4
)

#mcq("31", "NB", [Với hai góc phụ nhau $alpha$ và $90^circle - alpha$ ($0^circle < alpha < 90^circle$), hệ thức nào sau đây *SAI*?],
  [$sin(90^circle - alpha) = cos alpha$],
  [$cos(90^circle - alpha) = sin alpha$],
  [$tan(90^circle - alpha) = cot alpha$],
  [$tan(90^circle - alpha) = -cot alpha$],
  cols: 2
)

#mcq("32", "TH", [Cho biết $tan alpha = -2$. Khi đó giá trị của $cos^2 alpha$ bằng:],
  [$1/5$], [$4/5$], [$-1/5$], [$1/3$],
  cols: 4
)

=== Nhóm 5 (Vị trí Câu 9 – Câu 10 Phần I): Hệ thức lượng trong tam giác (Bài 6 SGK)

#mcq("33", "NB", [Cho tam giác $A B C$ có $B C = a, A C = b, A B = c$. Định lí Côsin khẳng định hệ thức nào sau đây *đúng*?],
  [$a^2 = b^2 + c^2 + 2 b c cos A$],
  [$a^2 = b^2 + c^2 - 2 b c cos A$],
  [$a^2 = b^2 + c^2 - b c cos A$],
  [$a^2 = b^2 + c^2 - 2 b c sin A$],
  cols: 2
)

#mcq("34", "NB", [Cho tam giác $A B C$ có bán kính đường tròn ngoại tiếp là $R$. Theo Định lí Sin, đẳng thức nào *đúng*?],
  [$a / (sin A) = R$],
  [$a / (sin A) = 2 R$],
  [$a / (cos A) = 2 R$],
  [$(sin A) / a = 2 R$],
  cols: 4
)

#mcq("35", "NB", [Cho tam giác $A B C$ có diện tích $S$, nửa chu vi $p$, bán kính ngoại tiếp $R$ và nội tiếp $r$. Công thức nào *SAI*?],
  [$S = 1/2 a b sin C$],
  [$S = p r$],
  [$S = (a b c) / (4 R)$],
  [$S = (a b c) / (2 R)$],
  cols: 4
)

#mcq("36", "TH", [Cho tam giác $A B C$ có $b = 5, c = 8$ và $hat(A) = 60^circle$. Độ dài cạnh $a$ bằng:],
  [$7$], [$sqrt(129)$], [$49$], [$sqrt(39)$],
  cols: 4
)

#mcq("37", "TH", [Cho tam giác $A B C$ có cạnh $B C = 6$ và góc $hat(A) = 30^circle$. Bán kính đường tròn ngoại tiếp $R$ bằng:],
  [$3$], [$6$], [$12$], [$3 sqrt(3)$],
  cols: 4
)

#mcq("38", "TH", [Tam giác $A B C$ có ba cạnh $a = 13, b = 14, c = 15$. Bán kính đường tròn nội tiếp $r$ của tam giác bằng:],
  [$4$], [$6$], [$84$], [$65/8$],
  cols: 4
)

#mcq("39", "TH", [Cho tam giác $A B C$ có $A B = 6, A C = 8$ và $hat(A) = 120^circle$. Diện tích $S$ của tam giác $A B C$ là:],
  [$24$], [$12$], [$12 sqrt(3)$], [$24 sqrt(3)$],
  cols: 4
)

#mcq("40", "TH", [Hai vị trí $A, B$ ở hai bên bờ hồ. Từ điểm $C$ trên bờ, người ta đo được $C A = 40 "m"$, $C B = 60 "m"$ và $goc(A C B) = 60^circle$. Khoảng cách $A B$ bằng:],
  [$20 sqrt(7) "m"$], [$20 sqrt(19) "m"$], [$50 "m"$], [$40 sqrt(3) "m"$],
  cols: 4
)

=== Nhóm 6 (Vị trí Câu 11 – Câu 12 Phần I): Khái niệm mở đầu về Vectơ (Bài 7 SGK)

#mcq("41", "NB", [Theo chương trình SGK *Kết nối tri thức với cuộc sống*, khẳng định nào dưới đây *đúng* về vectơ-không $vt(0)$?],
  [Vectơ-không không cùng phương với mọi vectơ.],
  [Vectơ-không cùng phương và cùng hướng với mọi vectơ.],
  [Vectơ-không có độ dài bằng $1$.],
  [Vectơ-không cùng phương nhưng ngược hướng với mọi vectơ.],
  cols: 1
)

#mcq("42", "NB", [Hai vectơ được gọi là *bằng nhau* khi và chỉ khi:],
  [Chúng có cùng độ dài.],
  [Chúng cùng phương và có cùng độ dài.],
  [Chúng cùng hướng và có cùng độ dài.],
  [Giá của chúng trùng nhau.],
  cols: 2
)

#mcq("43", "NB", [Cho ba điểm phân biệt $A, B, C$. Từ ba điểm này lập được bao nhiêu vectơ *khác vectơ-không* có điểm đầu và điểm cuối là các điểm đã cho?],
  [$3$], [$6$], [$9$], [$4$],
  cols: 4
)

#mcq("44", "NB", [Ba điểm phân biệt $A, B, C$ thẳng hàng khi và chỉ khi:],
  [$|vt(A B)| = |vt(A C)|$],
  [$vt(A B) = vt(B C)$],
  [$vt(A B)$ và $vt(A C)$ cùng phương],
  [$vt(A B)$ và $vt(A C)$ cùng hướng],
  cols: 2
)

#mcq("45", "TH", [Cho hình bình hành $A B C D$ có tâm $O$. Khẳng định nào dưới đây *đúng*?],
  [$vt(A B) = vt(C D)$],
  [$vt(A O) = vt(C O)$],
  [$vt(A D) = vt(B C)$],
  [$vt(O B) = vt(O D)$],
  cols: 4
)

#mcq("46", "TH", [Cho hình lục giác đều $A B C D E F$ tâm $O$. Số các vectơ *khác $vt(0)$* (có điểm đầu và điểm cuối lấy từ 6 đỉnh và tâm $O$) *bằng* vectơ $vt(A B)$ (không kể chính $vt(A B)$) là:],
  [$2$], [$3$], [$4$], [$6$],
  cols: 4
)

#mcq("47", "TH", [Cho tam giác $A B C$ có $M, N, P$ lần lượt là trung điểm của các cạnh $A B, B C, C A$. Vectơ nào dưới đây bằng vectơ $vt(M N)$?],
  [$vt(A P)$], [$vt(P A)$], [$vt(P C)$], [$vt(C P)$],
  cols: 4
)

#mcq("48", "TH", [Cho hình thoi $A B C D$ cạnh $a$ có $goc(B A D) = 60^circle$. Khẳng định nào dưới đây *đúng*?],
  [$vt(A B) = vt(A D)$],
  [$|vt(A C)| = a$],
  [$|vt(B D)| = a$],
  [$vt(B A) = vt(D C)$],
  cols: 4
)

=== Bảng đáp án & Hướng dẫn giải nhanh 48 câu Dạng thức 1

#table(
  columns: (1fr,) * 12,
  align: center + horizon,
  stroke: 0.5pt + c-border,
  inset: (x: 2pt, y: 4pt),
  fill: (x, y) => if calc.even(y) { c-blue-bg } else { white },
  [*1.C*], [*2.B*], [*3.B*], [*4.C*], [*5.B*], [*6.C*], [*7.C*], [*8.C*], [*9.B*], [*10.B*], [*11.C*], [*12.B*],
  [*13.B*], [*14.A*], [*15.C*], [*16.D*], [*17.B*], [*18.C*], [*19.C*], [*20.B*], [*21.B*], [*22.B*], [*23.B*], [*24.C*],
  [*25.B*], [*26.C*], [*27.C*], [*28.B*], [*29.A*], [*30.A*], [*31.D*], [*32.A*], [*33.B*], [*34.B*], [*35.D*], [*36.A*],
  [*37.B*], [*38.A*], [*39.C*], [*40.A*], [*41.B*], [*42.C*], [*43.B*], [*44.C*], [*45.C*], [*46.B*], [*47.C*], [*48.C*],
)

#block(width: 100%, fill: c-zebra, stroke: 0.6pt + c-border, radius: 5pt, inset: 8pt)[
  #set text(size: 8.2pt)
  *Giải nhanh các câu trọng tâm dễ nhầm:*
  - *Câu 8:* Mọi số tự nhiên $n = 3k, 3k+1, 3k+2$ đều có $n^2 equiv 0$ hoặc $1 (mod 3)$ nên $n^2 + 1 equiv 1$ hoặc $2 (mod 3)$, không chia hết cho $3$ $arrow.r$ *C đúng*. (Câu A sai tại $x = 0$).
  - *Câu 10:* $(x^2 - 4)(2x - 3) = 0 arrow.l.r.double x in {-2; 2; 3/2}$, vì $x in ZZ$ nên loại $3/2$, còn $X = {-2; 2}$.
  - *Câu 18:* $0x + 0y <= 4$ vi phạm điều kiện $a, b$ không đồng thời bằng $0$.
  - *Câu 20:* Bờ đi qua $(2; 0)$ và $(0; 3)$ có PT $x/2 + y/3 = 1 arrow.l.r.double 3x + 2y = 6$. Bờ liền và miền nghiệm chứa $O(0;0)$ nên $3x + 2y <= 6$.
  - *Câu 28:* $alpha$ tù nên $cos alpha = -sqrt(1 - (3/5)^2) = -4/5$. *Câu 29:* $P = 2(1 - 1/9) + 5(1/9) = 21/9 = 7/3$.
  - *Câu 30:* Chia tử và mẫu cho $cos alpha$: $A = (3 tan alpha - 2)/(tan alpha + 1) = (6 - 2)/(2 + 1) = 4/3$. *Câu 32:* $cos^2 alpha = 1/(1 + tan^2 alpha) = 1/5$.
  - *Câu 36:* $a^2 = 5^2 + 8^2 - 2 dot 5 dot 8 cos 60^circle = 49 arrow.r.double a = 7$. *Câu 37:* $R = 6/(2 sin 30^circle) = 6$.
  - *Câu 38:* $p = 21, S = sqrt(21 dot 8 dot 7 dot 6) = 84 arrow.r.double r = S/p = 84/21 = 4$. *Câu 40:* $A B = sqrt(40^2 + 60^2 - 2 dot 40 dot 60 cos 60^circle) = sqrt(2800) = 20 sqrt(7) "m"$.
  - *Câu 46:* Ba vectơ bằng $vt(A B)$ là $vt(F O), vt(O C), vt(E D)$. *Câu 47:* $M N$ là đường trung bình song song và bằng $1/2 A C = P C$, cùng chiều từ $M arrow.r N$ với $P arrow.r C$ nên $vt(M N) = vt(P C)$. *Câu 48:* Tam giác $A B D$ cân tại $A$ có góc $60^circle$ nên đều cạnh $a arrow.r.double |vt(B D)| = B D = a$.
]

== D.2. Dạng thức 2 — 06 Câu Trắc nghiệm Đúng / Sai chuẩn Ma trận (24 mệnh đề)

#tf-question(
  "Câu ĐS 1 (Chuẩn vị trí Câu 1 Phần II — Tập hợp):",
  [Cho hai tập hợp $A = [-3; 2)$ và $B = (0; 5]$ trên trục số thực $RR$. Xét tính đúng sai của các mệnh đề:],
  [*(NB)* Phần tử $-3 in A$ và phần tử $2 in A$.],
  [*(TH)* Tập hợp $A inter ZZ$ có tất cả $5$ phần tử nguyên.],
  [*(TH)* Tập hợp giao $A inter B = (0; 2)$ và phần bù $C_RR (A union B) = (-infinity; -3) union (5; +infinity)$.],
  [*(VD)* Với tập hợp $C = (m - 1; m + 2)$, có đúng $3$ giá trị nguyên của tham số $m$ để $C subset A$.]
)

#tf-question(
  "Câu ĐS 2 (Chuẩn vị trí Câu 1 Phần II — Tập hợp & Tham số):",
  [Cho hai tập hợp $A = {x in RR | -3 <= x <= 3}$ và $B = (1; +infinity)$. Xét tính đúng sai của các mệnh đề:],
  [*(NB)* Viết dưới dạng đoạn thì $A = [-3; 3]$ và $emptyset subset A$.],
  [*(TH)* Hiệu của hai tập hợp đã cho là $A without B = [-3; 1)$.],
  [*(TH)* Phần bù của $B$ trong $RR$ là $C_RR B = (-infinity; 1]$.],
  [*(VD)* Cho tập hợp $M = (2 m - 1; 2 m + 3)$. Có đúng $4$ giá trị nguyên của $m$ để $M inter A != emptyset$.]
)

#tf-question(
  "Câu ĐS 3 (Chuẩn vị trí Câu 1 Phần II — Tập hợp liệt kê & Thực tế):",
  [Lớp 10A có $45$ học sinh, trong đó tập hợp $T$ gồm $25$ bạn giỏi Toán, tập hợp $E$ gồm $20$ bạn giỏi Tiếng Anh và có $8$ bạn không giỏi môn nào trong hai môn trên. Xét tính đúng sai:],
  [*(NB)* Số phần tử của tập hợp $T$ được kí hiệu là $n(T) = 25$ và $T subset E$.],
  [*(TH)* Tập hợp các học sinh giỏi ít nhất một trong hai môn Toán hoặc Tiếng Anh là $T union E$ có $37$ học sinh.],
  [*(TH)* Tập hợp các học sinh giỏi cả hai môn Toán và Tiếng Anh là $T inter E$ có $8$ học sinh.],
  [*(VD)* Số học sinh chỉ giỏi đúng một trong hai môn (Toán hoặc Tiếng Anh) là $29$ học sinh.]
)

#tf-question(
  "Câu ĐS 4 (Chuẩn vị trí Câu 2 Phần II — Bất phương trình bậc nhất hai ẩn):",
  [Cho bất phương trình bậc nhất hai ẩn $2 x - y + 4 >= 0$ $(1)$. Xét tính đúng sai của các mệnh đề:],
  [*(NB)* Cặp số $(0; 0)$ là một nghiệm của bất phương trình $(1)$, còn cặp số $(-3; 1)$ không là nghiệm của $(1)$.],
  [*(TH)* Đường thẳng bờ $d: 2 x - y + 4 = 0$ cắt trục hoành tại $A(-2; 0)$ và cắt trục tung tại $B(0; 4)$.],
  [*(TH)* Miền nghiệm của bất phương trình $(1)$ là nửa mặt phẳng bờ $d$ (không kể bờ $d$) chứa gốc tọa độ $O$.],
  [*(VD)* Một xưởng cần ít nhất $2 x - y + 4 >= 0$ để cân đối ca trực; trong các điểm nguyên thuộc góc phần tư thứ hai ($x < 0, y > 0$), điểm $(-1; 1)$ thuộc miền nghiệm của $(1)$.]
)

#block(breakable: false)[
  #grid(
    columns: (1.42fr, 0.78fr),
    gutter: 8pt,
    align: (left + top, center + horizon),
    [
      #tf-question(
        "Câu ĐS 5 (Chuẩn vị trí Câu 2 Phần II — Đọc đồ thị miền nghiệm):",
        [Cho hình vẽ bên biểu diễn miền nghiệm (phần *không bị gạch*, bờ là đường nét đứt $d$) của một bất phương trình bậc nhất hai ẩn:],
        [*(NB)* Gốc tọa độ $O(0; 0)$ thuộc miền nghiệm được biểu diễn trên hình.],
        [*(TH)* Đường thẳng bờ $d$ có phương trình là $x - 2 y = 2$.],
        [*(TH)* Phần không bị gạch biểu diễn miền nghiệm của BPT $x - 2 y <= 2$.],
        [*(VD)* Nếu một bài toán thực tế có điều kiện ràng buộc trùng với miền nghiệm trên và $x, y in NN^*$, thì cặp $(3; 1)$ thỏa mãn điều kiện.]
      )
    ],
    [#image("assets/bank_bpt_graph2.svg", width: 100%)]
  )
]

#tf-question(
  "Câu ĐS 6 (Chuẩn vị trí Câu 2 Phần II — BPT gắn mô hình thực tế):",
  [Nhân dịp hội trại trường THPT Hà Huy Tập, chi đoàn 10A bán vé xem văn nghệ gồm vé học sinh giá $40$ nghìn đồng/vé và vé khách mời giá $80$ nghìn đồng/vé. Chi đoàn đặt mục tiêu tổng số tiền thu được *ít nhất* là $4$ triệu đồng. Gọi $x, y$ lần lượt là số vé học sinh và số vé khách mời bán được ($x, y in NN$):],
  [*(NB)* Tổng số tiền bán vé thu được tính theo đơn vị nghìn đồng là $40 x + 80 y$.],
  [*(TH)* Bất phương trình mô tả mục tiêu doanh thu của chi đoàn (sau khi rút gọn) là $x + 2 y >= 100$.],
  [*(TH)* Trên mặt phẳng $O x y$, miền nghiệm của BPT $x + 2 y >= 100$ là nửa mặt phẳng bờ $d: x + 2 y = 100$ chứa gốc tọa độ $O(0; 0)$.],
  [*(VD)* Nếu chi đoàn bán được $30$ vé học sinh và $40$ vé khách mời thì đã hoàn thành vượt mục tiêu đề ra.]
)

#block(width: 100%, fill: c-blue-bg, stroke: 0.7pt + c-blue-bd, radius: 5pt, inset: 8pt)[
  #set text(size: 8.2pt)
  *Đáp án & Giải chi tiết 06 Câu Đúng / Sai:*
  - *Câu ĐS 1:* *a) Sai* (vì $2 notin [-3; 2)$); *b) Đúng* ($A inter ZZ = {-3; -2; -1; 0; 1}$ gồm 5 số); *c) Đúng* ($A union B = [-3; 5]$); *d) Đúng* (vì $C != emptyset$, $C subset A arrow.l.r.double m - 1 >= -3$ và $m + 2 <= 2 arrow.l.r.double -2 <= m <= 0 arrow.r.double m in {-2; -1; 0}$: xét biên $m = 0$ thì $C = (-1; 2) subset [-3; 2)$ thỏa mãn!).
  - *Câu ĐS 2:* *a) Đúng*; *b) Sai* (vì $1 notin B$ nên $1$ còn lại trong $A without B = [-3; 1]$); *c) Đúng*; *d) Đúng* ($M inter A = emptyset arrow.l.r.double 2m + 3 <= -3$ hoặc $2m - 1 >= 3 arrow.l.r.double m <= -3$ hoặc $m >= 2$; suy ra $M inter A != emptyset arrow.l.r.double -3 < m < 2 arrow.r.double m in {-2; -1; 0; 1}$ gồm 4 số nguyên).
  - *Câu ĐS 3:* *a) Sai* ($T$ không phải tập con của $E$); *b) Đúng* ($45 - 8 = 37$); *c) Đúng* ($25 + 20 - 37 = 8$); *d) Đúng* ($(25 - 8) + (20 - 8) = 17 + 12 = 29$).
  - *Câu ĐS 4:* *a) Đúng* ($0 - 0 + 4 >= 0$; $2(-3) - 1 + 4 = -3 < 0$); *b) Đúng*; *c) Sai* (vì có dấu $>=$ nên miền nghiệm *có kể bờ $d$*); *d) Đúng* ($2(-1) - 1 + 4 = 1 >= 0$).
  - *Câu ĐS 5:* *a) Đúng*; *b) Đúng* ($x/2 + y/(-1) = 1 arrow.l.r.double x - 2y = 2$); *c) Sai* (vì bờ nét đứt nên BPT ngặt $x - 2y < 2$, không có dấu `=`); *d) Đúng* (thay $(3; 1)$: $3 - 2(1) = 1 < 2$).
  - *Câu ĐS 6:* *a) Đúng*; *b) Đúng* ($40x + 80y >= 4000 arrow.l.r.double x + 2y >= 100$); *c) Sai* (thay $(0;0)$ được $0 >= 100$ vô lí nên *không* chứa $O$); *d) Đúng* ($30 + 2 dot 40 = 110 >= 100$, thu được $4,4$ triệu đồng).
]

== D.3. Dạng thức 3 — 12 Câu Trắc nghiệm Trả lời ngắn chuẩn Ma trận (0,5 điểm/câu)

#sa-question("Câu TLN 1 (Vị trí Câu 1 P.III — Tập con):", "TH",
  [Cho tập hợp $A = {x in ZZ | x^2 <= 4}$. Tập hợp $A$ có tất cả bao nhiêu tập hợp con?])

#sa-question("Câu TLN 2 (Vị trí Câu 1 P.III — Tập con khác rỗng):", "TH",
  [Cho tập hợp $B = {x in NN^* | x < 6 "và" x "là ước của" 12}$. Tìm số tập hợp con *khác rỗng* của tập hợp $B$.])

#sa-question("Câu TLN 3 (Vị trí Câu 1 P.III — Tập con kẹp giữa):", "TH",
  [Cho hai tập hợp $A = {1; 2}$ và $B = {1; 2; 3; 4; 5; 6}$. Có bao nhiêu tập hợp $X$ thỏa mãn $A subset X subset B$?])

#sa-question("Câu TLN 4 (Vị trí Câu 2 P.III — Thực tế 2 tập hợp):", "VD",
  [Một lớp có $40$ học sinh, trong đó có $22$ em thích bóng đá, $18$ em thích cầu lông và $7$ em không thích môn nào trong hai môn trên. Có bao nhiêu em thích *cả hai môn*?])

#sa-question("Câu TLN 5 (Vị trí Câu 2 P.III — Thực tế 3 tập hợp):", "VD",
  [Khảo sát $50$ học sinh đội tuyển khối 10: có $25$ em thích Toán, $23$ em thích Lý, $20$ em thích Hóa; $11$ em thích cả Toán và Lý, $8$ em thích cả Lý và Hóa, $9$ em thích cả Toán và Hóa; có $5$ em thích cả ba môn. Hỏi có bao nhiêu em *không thích môn nào* trong ba môn trên?])

#sa-question("Câu TLN 6 (Vị trí Câu 2 P.III — Thực tế phần riêng):", "VD",
  [Đoàn du lịch gồm $100$ khách tham quan miền Trung, trong đó $65$ người đã đến Huế, $55$ người đã đến Đà Nẵng và $30$ người đã đến cả hai thành phố này. Hỏi có bao nhiêu khách *chỉ đến Huế mà không đến Đà Nẵng*?])

#sa-question("Câu TLN 7 (Vị trí Câu 3 P.III — Biểu thức lượng giác bậc nhất):", "VD",
  [Cho góc $alpha$ thỏa mãn $tan alpha = 3$. Tính giá trị biểu thức $P = (2 sin alpha + 4 cos alpha) / (3 sin alpha - cos alpha)$ *(viết dưới dạng số thập phân)*.])

#sa-question("Câu TLN 8 (Vị trí Câu 3 P.III — Biểu thức lượng giác bậc hai):", "VD",
  [Biết $tan alpha = -2$. Tính giá trị của biểu thức $Q = (5 sin^2 alpha - 3 sin alpha cos alpha + 2 cos^2 alpha) / (sin^2 alpha + 3 cos^2 alpha)$.])

#sa-question("Câu TLN 9 (Vị trí Câu 3 P.III — Hệ thức tổng tích):", "VD",
  [Cho góc nhọn $alpha$ thỏa mãn $sin alpha + cos alpha = 7/5$. Tính giá trị của tích $M = sin alpha dot cos alpha$ *(viết dạng số thập phân)*.])

#sa-question("Câu TLN 10 (Vị trí Câu 4 P.III — Tính góc tam giác):", "TH",
  [Cho tam giác $A B C$ có độ dài ba cạnh $a = 7, b = 8, c = 5$. Số đo góc $hat(A)$ bằng bao nhiêu độ?])

#sa-question("Câu TLN 11 (Vị trí Câu 4 P.III — Đường cao Heron):", "TH",
  [Cho tam giác $A B C$ có ba cạnh $a = 10, b = 17, c = 21$. Tính độ dài đường cao $h_c$ kẻ từ đỉnh $C$ xuống cạnh $A B$.])

#sa-question("Câu TLN 12 (Vị trí Câu 4 P.III — Đo chiều cao tháp):", "TH",
  [Từ hai điểm $A$ và $B$ thẳng hàng với chân tháp $H$ (cùng phía, $A B = 30 "m"$), người ta ngắm đỉnh tháp $C$ với góc nâng lần lượt là $30^circle$ và $60^circle$ (bỏ qua chiều cao giác kế). Tính chiều cao của tháp theo mét *(làm tròn đến hàng phần mười)*.])

#block(width: 100%, fill: c-teal-bg, stroke: 0.7pt + c-teal-bd, radius: 5pt, inset: 8pt)[
  #set text(size: 8.2pt)
  *Đáp số chuẩn tô phiếu & Giải nhanh 12 Câu Trả lời ngắn:*
  - *TLN 1:* *`32`* — $A = {-2; -1; 0; 1; 2}$ có $n = 5$ phần tử $arrow.r.double 2^5 = 32$.
  - *TLN 2:* *`15`* — $B = {1; 2; 3; 4}$ có $4$ phần tử $arrow.r.double$ số tập con khác rỗng là $2^4 - 1 = 15$.
  - *TLN 3:* *`16`* — Tập $X$ gồm ${1; 2}$ hợp thêm một tập con tùy ý của ${3; 4; 5; 6}$ $arrow.r.double 2^(6 - 2) = 16$.
  - *TLN 4:* *`7`* — $n(A union B) = 40 - 7 = 33 arrow.r.double n(A inter B) = 22 + 18 - 33 = 7$.
  - *TLN 5:* *`5`* — $n(T union L union H) = 25 + 23 + 20 - (11 + 8 + 9) + 5 = 45 arrow.r.double$ không thích môn nào: $50 - 45 = 5$.
  - *TLN 6:* *`35`* — Chỉ đến Huế: $n(H without D) = 65 - 30 = 35$.
  - *TLN 7:* *`1,25`* — Chia tử và mẫu cho $cos alpha$: $P = (2 dot 3 + 4)/(3 dot 3 - 1) = 10/8 = 1,25$.
  - *TLN 8:* *`4`* — Chia tử và mẫu cho $cos^2 alpha$: $Q = (5(-2)^2 - 3(-2) + 2)/((-2)^2 + 3) = 28/7 = 4$.
  - *TLN 9:* *`0,48`* — Bình phương hai vế: $1 + 2 sin alpha cos alpha = 49/25 arrow.r.double sin alpha cos alpha = 12/25 = 0,48$.
  - *TLN 10:* *`60`* — $cos A = (8^2 + 5^2 - 7^2)/(2 dot 8 dot 5) = 40/80 = 1/2 arrow.r.double hat(A) = 60^circle$.
  - *TLN 11:* *`8`* — $p = 24$, $S = sqrt(24 dot 14 dot 7 dot 3) = 84 arrow.r.double h_c = (2 S)/c = 168/21 = 8$.
  - *TLN 12:* *`26`* (hoặc `26,0`) — $goc(A C B) = 60^circle - 30^circle = 30^circle = goc(B A C) arrow.r.double B C = A B = 30 "m" arrow.r.double C H = 30 sin 60^circle = 15 sqrt(3) approx 26,0 "m"$.
]

== D.4. Dạng thức 4 — 09 Bài toán Tự luận mẫu chuẩn Ma trận (Kèm thang điểm 0,25đ)

=== Nhóm Tự luận 1 (Chuẩn Câu 1 Tự luận — 1,0 điểm, MĐ2/Thông hiểu): Các phép toán trên tập hợp

#theory-card("Bài TL 1 (1,0 điểm) — Phép toán giao, hợp, hiệu và phần bù trên ℝ")[
  *Đề bài:* Cho hai tập hợp $A = [-4; 3)$ và $B = (0; 6]$. Hãy xác định các tập hợp $A inter B$, $A union B$, $A without B$ và $C_RR A$.
  - *Lời giải & Biểu điểm:*
    - $A inter B = (0; 3)$ *(0,25 điểm)*.
    - $A union B = [-4; 6]$ *(0,25 điểm)*.
    - $A without B = [-4; 0]$ *(chú ý $0 notin B$ nên $0 in A without B$!)* *(0,25 điểm)*.
    - $C_RR A = RR without A = (-infinity; -4) union [3; +infinity)$ *(chú ý đổi ngoặc vuông $arrow.l.r$ tròn!)* *(0,25 điểm)*.
]

#theory-card("Bài TL 2 (1,0 điểm) — Kết hợp giải phương trình / bất phương trình trước khi thực hiện phép toán")[
  *Đề bài:* Cho $A = {x in RR | -2 < x <= 5}$ và $B = {x in RR | x >= 2}$. Viết $A, B$ dưới dạng khoảng/nửa khoảng và tìm $A inter B$, $C_RR B$, $(C_RR B) inter A$.
  - *Lời giải & Biểu điểm:*
    - Viết đúng $A = (-2; 5]$ và $B = [2; +infinity)$ *(0,25 điểm)*.
    - $A inter B = [2; 5]$ *(0,25 điểm)*.
    - $C_RR B = RR without [2; +infinity) = (-infinity; 2)$ *(0,25 điểm)*.
    - $(C_RR B) inter A = (-infinity; 2) inter (-2; 5] = (-2; 2)$ *(0,25 điểm)*.
]

#theory-card("Bài TL 3 (1,0 điểm) — Phép toán tập hợp kết hợp tìm điều kiện tham số cơ bản")[
  *Đề bài:* a) Cho $A = (-infinity; 2]$ và $B = (-3; +infinity)$. Tìm $A inter B$, $A union B$, $C_RR A$. #h(6pt) b) Cho $M = [m; m + 3]$. Tìm $m$ để $M subset (-3; 5]$.
  - *Lời giải & Biểu điểm:*
    - a) $A inter B = (-3; 2]$ *(0,25đ)*; $A union B = RR = (-infinity; +infinity)$ *(0,25đ)*; $C_RR A = (2; +infinity)$ *(0,25đ)*.
    - b) Vì $m < m + 3$ nên $M != emptyset$. Để $[m; m + 3] subset (-3; 5] arrow.l.r.double cases(m > -3, m + 3 <= 5) arrow.l.r.double -3 < m <= 2$ *(0,25đ)*.
]

=== Nhóm Tự luận 2 (Chuẩn Câu 2 Tự luận — 1,0 điểm, MĐ2/Vận dụng): Hệ thức lượng thực tiễn

#theory-card("Bài TL 4 (1,0 điểm) — Đo khoảng cách giữa hai địa điểm bị ngăn bởi đồi núi / hồ nước")[
  *Đề bài:* Để tính khoảng cách giữa hai địa điểm $A$ và $B$ ở hai bên một ngọn đồi (không đo trực tiếp được), người ta chọn vị trí $C$ sao cho nhìn thấy cả $A, B$ và đo được $C A = 80 "m"$, $C B = 100 "m"$, góc $goc(A C B) = 120^circle$. Tính khoảng cách $A B$ và diện tích tam giác $A B C$ (làm tròn đến hàng phần trăm).
  - *Lời giải & Biểu điểm:*
    - Áp dụng Định lí Côsin trong $triangle A B C$: $A B^2 = C A^2 + C B^2 - 2 dot C A dot C B dot cos goc(A C B)$ *(0,25đ)*.
    - Thay số: $A B^2 = 80^2 + 100^2 - 2 dot 80 dot 100 dot cos 120^circle = 6400 + 10000 - 16000 dot (-1/2) = 24400$ *(0,25đ)*.
    - Suy ra $A B = sqrt(24400) = 20 sqrt(61) approx 156,20 "m"$ *(0,25đ)*.
    - Diện tích: $S_(A B C) = 1/2 dot C A dot C B dot sin 120^circle = 1/2 dot 80 dot 100 dot sqrt(3)/2 = 2000 sqrt(3) approx 3464,10 "m"^2$ *(0,25đ)*.
]

#theory-card("Bài TL 5 (1,0 điểm) — Bài toán hai tàu thủy xuất phát từ cảng biển")[
  *Đề bài:* Hai tàu thủy cùng xuất phát từ cảng $O$ tại cùng một thời điểm, đi thẳng theo hai hướng hợp với nhau góc $120^circle$. Tàu thứ nhất chạy với tốc độ $20 "km/h"$, tàu thứ hai chạy với tốc độ $30 "km/h"$. Hỏi sau $2$ giờ hai tàu cách nhau bao nhiêu kilômét (làm tròn đến hàng phần trăm)?
  - *Lời giải & Biểu điểm:*
    - Sau $2$ giờ, quãng đường hai tàu đi được là: $O A = 20 dot 2 = 40 "km"$ và $O B = 30 dot 2 = 60 "km"$ *(0,25đ)*.
    - Trong $triangle O A B$ có $goc(A O B) = 120^circle$, áp dụng Định lí Côsin: $A B^2 = O A^2 + O B^2 - 2 dot O A dot O B dot cos 120^circle$ *(0,25đ)*.
    - Tính được: $A B^2 = 40^2 + 60^2 - 2 dot 40 dot 60 dot (-1/2) = 1600 + 3600 + 2400 = 7600$ *(0,25đ)*.
    - Vậy khoảng cách giữa hai tàu là $A B = sqrt(7600) = 20 sqrt(19) approx 87,18 "km"$ *(0,25đ)*.
]

#theory-card("Bài TL 6 (1,0 điểm) — Đo chiều cao tháp khi không tới được chân tháp (Có chiều cao giác kế)")[
  *Đề bài:* Để đo chiều cao của một tháp cổ $C H$ ($H$ là chân tháp trên mặt đất ngang), người ta đặt giác kế cao $1,5 "m"$ tại hai vị trí $A, B$ thẳng hàng với $H$ ($A B = 25 "m"$, $B$ nằm giữa $A$ và $H$). Góc nâng ngắm đỉnh tháp $C$ từ $A$ và $B$ lần lượt là $32^circle$ và $50^circle$. Tính chiều cao thật của tháp (làm tròn đến hàng phần trăm).
  - *Lời giải & Biểu điểm:*
    - Gọi $A', B', H'$ là các điểm ngang tầm đặt giác kế ($A' B' = 25 "m"$, $H H' = 1,5 "m"$). Trong $triangle C A' B'$: $goc(A' C B') = 50^circle - 32^circle = 18^circle$ *(0,25đ)*.
    - Áp dụng Định lí Sin trong $triangle C A' B'$: $(C B')/(sin 32^circle) = (A' B')/(sin 18^circle) arrow.r.double C B' = (25 dot sin 32^circle)/(sin 18^circle) approx 42,87 "m"$ *(0,25đ)*.
    - Trong $triangle C B' H'$ vuông tại $H'$: $C H' = C B' dot sin 50^circle = (25 dot sin 32^circle dot sin 50^circle)/(sin 18^circle) approx 32,84 "m"$ *(0,25đ)*.
    - Chiều cao của tháp so với mặt đất: $C H = C H' + 1,5 approx 32,84 + 1,5 =$ *$34,34 "m"$* *(0,25đ)*.
]

=== Nhóm Tự luận 3 (Chuẩn Câu 3 Tự luận — 1,0 điểm, MĐ3/Vận dụng cao): Hệ BPT tối ưu thực tiễn

#theory-card("Bài TL 7 (1,0 điểm) — Bài toán phân bổ sản xuất kinh điển")[
  *Đề bài:* Một cơ sở mộc sản xuất hai mẫu bàn học loại I và loại II. Mỗi chiếc loại I cần $1$ công thợ và $2$ tấm gỗ, lãi $3$ trăm nghìn đồng; mỗi chiếc loại II cần $2$ công thợ và $1$ tấm gỗ, lãi $4$ trăm nghìn đồng. Một tuần cơ sở có tối đa $8$ công thợ và $10$ tấm gỗ. Hỏi cần đóng bao nhiêu bàn mỗi loại để tiền lãi cao nhất?
  - *Lời giải & Biểu điểm:*
    - Gọi $x, y$ ($x, y >= 0; x, y in NN$) là số bàn loại I, II. Hệ BPT ràng buộc: $cases(x >= 0 comma y >= 0, x + 2 y <= 8, 2 x + y <= 10)$. Hàm lãi $F(x; y) = 3 x + 4 y$ (trăm nghìn) *(0,25đ)*.
    - Biểu diễn miền nghiệm là tứ giác lồi $O A B C$ *(như Hình mục Bài 4)* với 4 đỉnh: $O(0; 0), A(0; 4), B(4; 2), C(5; 0)$ *(0,50đ)*.
    - Tính $F$: $F(0;0) = 0$; $F(0;4) = 16$; *$F(4;2) = 20$*; $F(5;0) = 15$. Vậy lãi lớn nhất là *$20$ trăm nghìn ($2$ triệu đồng)* khi đóng *$4$ bàn loại I và $2$ bàn loại II* *(0,25đ)*.
]

#theory-card("Bài TL 8 (1,0 điểm) — Bài toán khẩu phần dinh dưỡng tối thiểu chi phí")[
  *Đề bài:* Một vận động viên cần bổ sung mỗi ngày ít nhất $12$ đơn vị chất đạm và $10$ đơn vị vitamin từ hai loại thực phẩm $X$ (giá $50$ nghìn/khẩu phần $100 "g"$, chứa $3$ đv đạm + $1$ đv vitamin) và $Y$ (giá $40$ nghìn/khẩu phần $100 "g"$, chứa $1$ đv đạm + $2$ đv vitamin). Tìm khối lượng khẩu phần $X, Y$ cần dùng mỗi ngày để chi phí thấp nhất.
  - *Lời giải & Biểu điểm:*
    - Gọi $x, y >= 0$ là số khẩu phần $X, Y$. Hệ BPT ràng buộc: $cases(x >= 0 comma y >= 0, 3 x + y >= 12, x + 2 y >= 10)$. Chi phí $F(x; y) = 50 x + 40 y$ (nghìn đồng) *(0,25đ)*.
    - Miền nghiệm trên mặt phẳng $O x y$ là miền đa giác lồi không bị chặn có $3$ đỉnh biên: $A(0; 12)$, giao điểm $B(14/5; 18/5)$ *(nghiệm của hệ $3x+y=12$ và $x+2y=10$, tức $x = 2,8; y = 3,6$)* và $C(10; 0)$ *(0,50đ)*.
    - Tính giá trị $F$ tại các đỉnh: $F(0; 12) = 480$; *$F(2,8; 3,6) = 50 dot 2,8 + 40 dot 3,6 = 284$*; $F(10; 0) = 500$. Vậy chi phí thấp nhất là *$284$ nghìn đồng/ngày* khi dùng *$2,8$ khẩu phần $X$ và $3,6$ khẩu phần $Y$* *(nếu ràng buộc mua nguyên gói $x, y in NN$ thì tối ưu tại $(3; 4)$ tốn $310$ nghìn đồng)* *(0,25đ)*.
]

#theory-card("Bài TL 9 (1,0 điểm) — Bài toán pha chế nước giải khát (Mẫu kinh điển SGK Kết nối tri thức)")[
  *Đề bài:* Trong một cuộc thi pha chế, mỗi đội được cấp tối đa $24 "g"$ hương liệu, $9$ lít nước và $210 "g"$ đường để pha nước cam loại I và loại II. Pha $1$ lít loại I cần $30 "g"$ đường, $1$ lít nước, $1 "g"$ hương liệu (được $60$ điểm thưởng); pha $1$ lít loại II cần $10 "g"$ đường, $1$ lít nước, $4 "g"$ hương liệu (được $80$ điểm thưởng). Hỏi cần pha bao nhiêu lít mỗi loại để tổng điểm thưởng tối đa?
  - *Lời giải & Biểu điểm:*
    - Gọi $x, y >= 0$ là số lít nước cam loại I, II. Hệ BPT: $cases(x >= 0 comma y >= 0, 30 x + 10 y <= 210, x + y <= 9, x + 4 y <= 24) arrow.l.r.double cases(x >= 0 comma y >= 0, 3 x + y <= 21, x + y <= 9, x + 4 y <= 24)$. Hàm điểm: $F(x; y) = 60 x + 80 y$ *(0,25đ)*.
    - Miền nghiệm là ngũ giác lồi $O A B C D$ có 5 đỉnh: $O(0; 0), A(0; 6), B(4; 5), C(6; 3), D(7; 0)$ *(0,50đ)*.
    - Thay vào $F$: $F(0;0) = 0$; $F(0;6) = 480$; *$F(4;5) = 640$*; $F(6;3) = 600$; $F(7;0) = 420$. Vậy đạt tối đa *$640$ điểm* khi pha *$4$ lít loại I và $5$ lít loại II* *(0,25đ)*.
]

#pagebreak()
