#import "style.typ": *

= Chuyên đề 1 · Mệnh đề và tập hợp

#note("MỤC TIÊU THEO MA TRẬN", [
  Nhận biết mệnh đề, mệnh đề chứa biến, mệnh đề phủ định; hiểu $forall, exists$; mô tả tập hợp; dùng kí hiệu tập hợp và khoảng–đoạn; biểu diễn trên trục số; thực hiện giao, hợp, hiệu, phần bù; đếm tập con; giải bài toán thực tế bằng biểu đồ Ven.

  *Vị trí đề ôn:* Câu 1–4 · ĐS 1a–d · TLN 1–2 · TL 1.
])

== 1.1. Mệnh đề toán học

=== a) Mệnh đề, mệnh đề chứa biến, mệnh đề phủ định

- *Mệnh đề* là một khẳng định có tính đúng hoặc sai xác định. Một mệnh đề không thể vừa đúng vừa sai.
- Câu hỏi, câu cầu khiến, câu cảm thán không phải mệnh đề.
- *Mệnh đề chứa biến* là khẳng định có biến; tính đúng–sai chỉ xác định sau khi thay biến bằng giá trị cụ thể. Ví dụ “$x>3$” là mệnh đề chứa biến; khi $x=5$ ta được mệnh đề đúng, khi $x=1$ ta được mệnh đề sai.
- *Phủ định* của mệnh đề $P$, kí hiệu $overline(P)$, là mệnh đề có tính đúng–sai trái ngược với $P$. Ta thường thêm “không” hoặc “không phải” một cách hợp lí.

#example("VÍ DỤ 1 · Nhận biết và phủ định", [
  Xét các câu: (1) “$2n$ là số chẵn”; (2) “Hãy đọc kĩ đề!”; (3) “$15$ chia hết cho $5$”. Câu nào là mệnh đề, mệnh đề chứa biến? Viết phủ định của (3).
], [
  (1) là *mệnh đề chứa biến* vì chưa biết $n$ và chưa có miền giá trị. (2) là câu cầu khiến nên không phải mệnh đề. (3) là *mệnh đề đúng*.

  Phủ định của (3) là: “$15$ *không* chia hết cho $5$”; đây là mệnh đề sai.
])

=== b) Mệnh đề kéo theo, đảo, tương đương

Với hai mệnh đề $P,Q$:

- “Nếu $P$ thì $Q$”, kí hiệu $P=>Q$: $P$ là *điều kiện đủ* để có $Q$; $Q$ là *điều kiện cần* để có $P$.
- Mệnh đề $Q=>P$ gọi là *mệnh đề đảo* của $P=>Q$.
- Nếu cả $P=>Q$ và $Q=>P$ đều đúng thì $P<=>Q$ đúng. Ta nói $P$ là *điều kiện cần và đủ* để có $Q$, hoặc “$P$ khi và chỉ khi $Q$”.

#warning("ĐIỀU CẦN — ĐIỀU ĐỦ RẤT DỄ VIẾT NGƯỢC", [
  Luôn bắt đầu từ chiều mũi tên $P=>Q$. Hãy nói: “Có $P$ là *đủ* để kết luận $Q$; muốn có $P$ thì *cần* $Q$”. Không suy ra mệnh đề đảo cũng đúng nếu chưa kiểm tra.
])

=== c) Mệnh đề chứa $forall$ và $exists$

- $forall$ đọc là “với mọi”; $exists$ đọc là “tồn tại”.
- Mệnh đề “$forall x in X, P(x)$” sai nếu tìm được *một phản ví dụ*.
- Mệnh đề “$exists x in X, P(x)$” đúng nếu chỉ ra được *một giá trị* thỏa mãn.

#remember("QUY TẮC PHỦ ĐỊNH LƯỢNG TỪ", [
  Đổi $forall$ thành $exists$, đổi $exists$ thành $forall$, đồng thời phủ định vị từ:
  $ overline(forall x in X: P(x)) quad<=>quad exists x in X,  overline(P(x)). $
  $ overline(exists x in X:  P(x)) quad<=>quad forall x in X,  overline(P(x)). $
  *Miền $X$ không đổi.*
])

#example("VÍ DỤ 2 · Phủ định có lượng từ", [
  Phủ định mệnh đề $P$: “$forall x in RR, x^2-2x+1>0$”. Mệnh đề $P$ đúng hay sai?
], [
  Phủ định là $overline(P)$: “$exists x in RR, x^2-2x+1<=0$”.

  Vì $x^2-2x+1=(x-1)^2>=0$ và tại $x=1$ biểu thức bằng $0$, nên $P$ sai, $overline(P)$ đúng. Phản ví dụ $x=1$ đủ để bác bỏ $P$.
])

== 1.2. Tập hợp và các kí hiệu

=== a) Hai cách mô tả tập hợp

+ *Liệt kê:* viết mỗi phần tử một lần, không kể thứ tự. Ví dụ $A={1;2;3}$.
+ *Nêu tính chất đặc trưng:* ví dụ $A={x in NN | 0<x<4}$.

Kí hiệu $a in A$: $a$ là phần tử của $A$; $a in.not A$: $a$ không thuộc $A$. Tập rỗng $emptyset$ không có phần tử nào.

=== b) Tập con, hai tập bằng nhau, số tập con

- $A subset B$ nếu mọi phần tử của $A$ đều thuộc $B$. Theo quy ước, $emptyset subset A$ và $A subset A$.
- $A=B$ khi $A subset B$ và $B subset A$.
- Nếu $A$ có $n$ phần tử hữu hạn thì số tập con của $A$ là $2^n$ (gồm cả $emptyset$ và $A$).

#table(
  columns: (2.3fr, 1.25fr, 1.8fr),
  table.header([#th[Loại tập con]], [#th[Công thức]], [#th[Điều kiện/ghi chú]]),
  [Tất cả], [$2^n$], [$n>=0$],
  [Khác rỗng], [$2^n-1$], [$n>=1$],
  [Khác chính $A$], [$2^n-1$], [$n>=1$],
  [Khác rỗng và khác $A$], [$2^n-2$], [$n>=1$],
)

#example("VÍ DỤ 3 · Mô tả tập và đếm tập con", [
  Cho $A={x in ZZ | -2<=x<3}$. Liệt kê $A$ và tính số tập con khác rỗng của $A$.
], [
  Các số nguyên thỏa mãn là $-2,-1,0,1,2$, nên $A={-2;-1;0;1;2}$ và $n(A)=5$.

  Số tập con khác rỗng là $2^5-1=31$.
])

=== c) Các tập số và khoảng–đoạn

#table(
  columns: (0.75fr, 2.2fr, 0.75fr, 2.2fr),
  table.header([#th[Kí hiệu]], [#th[Tập hợp]], [#th[Kí hiệu]], [#th[Tập hợp]]),
  [$NN$], [Số tự nhiên], [$NN^*$], [Số tự nhiên khác $0$],
  [$ZZ$], [Số nguyên], [$QQ$], [Số hữu tỉ],
  [$RR$], [Số thực], [$emptyset$], [Tập rỗng],
)

#table(
  columns: (1.1fr, 2.2fr, 2.2fr),
  table.header([#th[Kí hiệu]], [#th[Tập các số thực $x$]], [#th[Đầu mút trên trục số]]),
  [$(a;b)$], [$a<x<b$], [Hai đầu rỗng],
  [$[a;b]$], [$a<=x<=b$], [Hai đầu đặc],
  [$(a;b]$], [$a<x<=b$], [$a$ rỗng, $b$ đặc],
  [$[a;b)$], [$a<=x<b$], [$a$ đặc, $b$ rỗng],
  [$(a;+oo)$], [$x>a$], [$a$ rỗng, tô phần bên phải],
  [$[a;+oo)$], [$x>=a$], [$a$ đặc, tô phần bên phải],
  [$(-oo;a)$], [$x<a$], [$a$ rỗng, tô phần bên trái],
  [$(-oo;a]$], [$x<=a$], [$a$ đặc, tô phần bên trái],
  [$(-oo;+oo)$], [$x in RR$], [Toàn trục số],
)

#warning("DẤU NGOẶC QUYẾT ĐỊNH ĐẦU MÚT", [
  Dấu “$($” hoặc “$)$” loại đầu mút; dấu “$[$” hoặc “$]$” lấy đầu mút. Với $-oo,+oo$ luôn dùng ngoặc tròn vì vô cực không phải một số thực. Khi giao hai tập trên trục số, phần chung phải thỏa mãn *đồng thời cả hai điều kiện*.
])

== 1.3. Các phép toán trên tập hợp

#table(
  columns: (1fr, 2.1fr, 2.1fr),
  table.header([#th[Phép toán]], [#th[Định nghĩa]], [#th[Cách nhớ]]),
  [Giao $A inter B$], [Phần tử thuộc *cả $A$ và $B$*], [“Và” · phần chung],
  [Hợp $A union B$], [Phần tử thuộc $A$ *hoặc* $B$], [“Hoặc” · gom tất cả, không lặp],
  [Hiệu $A without B$], [Phần tử thuộc $A$ nhưng *không* thuộc $B$], [Lấy $A$, bỏ phần chung],
  [Phần bù $C_U A$], [Nếu $A subset U$: $C_U A=U without A$], [Phải biết rõ tập vũ trụ $U$],
)

Với hai tập hữu hạn:
$ n(A union B)=n(A)+n(B)-n(A inter B). $
Suy ra số phần tử không thuộc $A$ hoặc $B$ trong tập vũ trụ $U$ là
$ n(U)-n(A union B). $

#figure-local("assets/venn-giao.svg", 62%, [Phần giao là vùng chung của hai hình tròn. Hình này cũng xuất hiện trong Câu 4 của đề ôn.])

#example("VÍ DỤ 4 · Bốn phép toán trong một bài", [
  Cho $U={1;2;3;4;5;6;7}$, $A={1;2;3;4;5}$, $B={4;5;6}$. Tìm $A inter B$, $A union B$, $A without B$, $C_U A$.
], [
  $A inter B={4;5}$ vì chỉ $4,5$ thuộc cả hai tập.

  $A union B={1;2;3;4;5;6}$; mỗi phần tử chỉ viết một lần.

  $A without B={1;2;3}$; $C_U A=U without A={6;7}$.
])

#example("VÍ DỤ 5 · Giao và hợp trên trục số", [
  Cho $A=(-2;4]$, $B=[1;6)$. Tìm $A inter B$ và $A union B$.
], [
  Điều kiện chung là $x>-2$, $x<=4$, $x>=1$, $x<6$. Chọn điều kiện chặt hơn ở mỗi đầu: $x>=1$ và $x<=4$. Vậy
  $ A inter B=[1;4]. $
  Hợp gồm mọi điểm thuộc ít nhất một trong hai khoảng, hai phần nối liền nhau nên
  $ A union B=(-2;6). $
])

#example("VÍ DỤ 6 · Bài toán thực tế bằng biểu đồ Ven", [
  Một nhóm có $36$ học sinh; $22$ em thích cầu lông, $17$ em thích bơi, $6$ em thích cả hai. Hỏi có bao nhiêu em thích ít nhất một môn và bao nhiêu em không thích môn nào?
], [
  Số em thích ít nhất một môn:
  $ 22+17-6=33. $
  Phải trừ $6$ vì nhóm thích cả hai môn đã được cộng hai lần.

  Số em không thích môn nào: $36-33=3$.

  Có thể điền ba vùng: chỉ cầu lông $22-6=16$; chỉ bơi $17-6=11$; cả hai $6$.
])

=== Lỗi thường gặp ở Chuyên đề 1

- Viết $2 subset A$ thay vì $2 in A$; hoặc ${2} in A$ thay vì ${2} subset A$.
- Quên $0$ khi liệt kê tập con của $NN$; quên rằng $emptyset$ cũng là một tập con.
- Cộng $n(A)+n(B)$ mà không trừ phần giao.
- Lấy phần bù nhưng không xác định tập vũ trụ.
- Phủ định $x>2$ thành $x<2$; đúng phải là $x<=2$.

== 1.4. Luyện nhanh Chuyên đề 1

#drill("1A", [Trong các câu sau, câu nào là mệnh đề: “$x^2=4$”; “$|-3|=3$”; “Đi nào!”?])
#drill("1B", [Phủ định mệnh đề “$exists x in QQ, x^2=2$”.])
#drill("1C", [Cho $A={x in NN | x<6, x "chẵn"}$ với quy ước $0 in NN$. Liệt kê $A$.])
#drill("1D", [Cho $A=(-1;3)$, $B=[0;5]$. Tìm $A inter B$, $A union B$ và $A without B$.])
#drill("1E", [Một tập có $6$ phần tử. Tính số tập con có đúng $1$ phần tử và tổng số tập con.])
#drill("1F", [Lớp có $42$ học sinh, $28$ em đăng kí âm nhạc, $20$ em đăng kí thể thao, $10$ em đăng kí cả hai. Tính số em đăng kí ít nhất một môn.])

#answer-strip([
  *Đáp án luyện nhanh:* 1A. “$|-3|=3$” là mệnh đề đúng; “$x^2=4$” là mệnh đề chứa biến; câu còn lại không phải mệnh đề.
  1B. “$forall x in QQ, x^2!=2$”.
  1C. $A={0;2;4}$.
  1D. $A inter B=[0;3)$; $A union B=(-1;5]$; $A without B=(-1;0)$.
  1E. Có $6$ tập con một phần tử; tổng cộng $2^6=64$ tập con.
  1F. $28+20-10=38$ học sinh.
])

= Chuyên đề 2 · Bất phương trình và hệ bất phương trình bậc nhất hai ẩn

#note("MỤC TIÊU THEO MA TRẬN", [
  Nhận biết BPT/hệ BPT bậc nhất hai ẩn và nghiệm; mô tả miền nghiệm; chuyển điều kiện thực tế thành BPT; biểu diễn miền nghiệm và giải bài toán tối ưu.

  *Vị trí đề ôn:* Câu 5–6 · ĐS 2a–d · TL 3.
])

== 2.1. Bất phương trình bậc nhất hai ẩn

BPT bậc nhất hai ẩn $x,y$ có một trong các dạng
$ a x+b y<c, quad a x+b y<=c, quad a x+b y>c, quad a x+b y>=c, $
trong đó $a,b,c$ là số thực đã cho và *$a,b$ không đồng thời bằng $0$*.

Cặp $(x_0;y_0)$ là nghiệm nếu thay vào ta được bất đẳng thức đúng. Trên $O x y$, tập hợp mọi điểm có tọa độ là nghiệm gọi là *miền nghiệm*.

=== Bốn bước biểu diễn miền nghiệm

+ Viết đường bờ $d:a x+b y=c$; tìm hai điểm của $d$ rồi vẽ.
+ Dùng *nét liền* cho $<=,>=$ (lấy bờ), *nét đứt* cho $<,>$ (không lấy bờ).
+ Chọn điểm thử không thuộc $d$, thường là $O(0;0)$ nếu $c!=0$.
+ Nếu điểm thử thỏa mãn, chọn nửa mặt phẳng chứa điểm đó; nếu không, chọn nửa còn lại. Ghi rõ có lấy bờ hay không.

#figure-local("assets/mien-nghiem-bpt.svg", 78%, [Miền nghiệm của $x+2y<=6$: nửa mặt phẳng chứa $O$, kể cả đường bờ $d$.])

#example("VÍ DỤ 1 · Kiểm tra nghiệm", [
  Cặp nào là nghiệm của $2x-y<=3$: $(1;0)$, $(2;3)$, $(0;-4)$?
], [
  Thay lần lượt:
  - $(1;0)$: $2.1-0=2<=3$ → thỏa mãn.
  - $(2;3)$: $2.2-3=1<=3$ → thỏa mãn.
  - $(0;-4)$: $2.0-(-4)=4>3$ → không thỏa mãn.
])

#example("VÍ DỤ 2 · Mô tả miền nghiệm bằng lời giải", [
  Biểu diễn miền nghiệm của $x-2y>4$.
], [
  Đường bờ $d:x-2y=4$ đi qua $(4;0)$ và $(0;-2)$. Vì dấu $>$ nên vẽ $d$ *nét đứt*.

  Điểm $O(0;0)$ không thuộc $d$ nhưng $0-2.0=0<4$, nên $O$ không thuộc miền nghiệm.

  Kết luận: miền nghiệm là nửa mặt phẳng bờ $d$ *không chứa $O$ và không kể bờ $d$*.
])

== 2.2. Hệ bất phương trình bậc nhất hai ẩn

Hệ gồm từ hai BPT bậc nhất hai ẩn trở lên. Một cặp $(x_0;y_0)$ là nghiệm khi thỏa mãn *tất cả* các BPT. Miền nghiệm của hệ là *giao* các miền nghiệm thành phần.

#remember("CÁCH TRÌNH BÀY MIỀN NGHIỆM CỦA HỆ", [
  Xác định từng nửa mặt phẳng trên cùng hệ trục; gạch bỏ phần không thỏa mãn từng BPT. Phần còn lại là miền nghiệm. Khi cần tọa độ đỉnh, giải các hệ *phương trình* tương ứng với hai đường bờ cắt nhau, rồi kiểm tra đỉnh có thỏa mãn mọi bất đẳng thức không.
])

#example("VÍ DỤ 3 · Miền nghiệm tam giác", [
  Xác định miền nghiệm và các đỉnh của hệ
  $ cases(x>=0, y>=0, x+y<=6). $
], [
  $x>=0$ chọn nửa mặt phẳng bên phải $O y$; $y>=0$ chọn nửa mặt phẳng phía trên $O x$; $x+y<=6$ chọn nửa mặt phẳng chứa $O$ vì $0+0<=6$.

  Giao ba miền là tam giác có các đỉnh $O(0;0)$, $A(6;0)$, $B(0;6)$, kể cả ba cạnh.
])

== 2.3. Mô hình hóa bài toán thực tế và tối ưu

Khi lập mô hình:

+ Gọi ẩn kèm đơn vị và điều kiện (thường $x,y>=0$, có thể $x,y in NN$).
+ Chuyển “không vượt quá/tối đa” thành $<=$; “ít nhất/tối thiểu” thành $>=$.
+ Viết đủ mọi ràng buộc: nguyên liệu, thời gian, diện tích, nhu cầu, sức chứa.
+ Nếu tìm lợi nhuận/chi phí $F=m x+n y$, lập miền nghiệm và bảng giá trị tại các đỉnh.

Với miền nghiệm là *đa giác kín, giới hạn*, một hàm tuyến tính $F=m x+n y$ luôn có giá trị lớn nhất và nhỏ nhất; mỗi giá trị đó đạt được tại ít nhất một đỉnh (cũng có thể đạt trên cả một cạnh).

#example("VÍ DỤ 4 · Lập hệ từ lời văn", [
  Một xưởng sản xuất $x$ chiếc bàn và $y$ chiếc ghế. Mỗi bàn cần $3$ giờ, mỗi ghế cần $2$ giờ; tổng thời gian không quá $60$ giờ. Nhu cầu cần ít nhất $5$ chiếc bàn. Viết các ràng buộc.
], [
  Điều kiện tự nhiên: $x,y>=0$ và, nếu tính từng chiếc nguyên vẹn, $x,y in NN$.

  Ràng buộc thời gian: $3x+2y<=60$. Ràng buộc nhu cầu: $x>=5$.

  Vậy một hệ mô tả bài toán là
  $ cases(x>=5, y>=0, 3x+2y<=60, x in NN,  y in NN). $
])

#example("VÍ DỤ 5 · Tìm giá trị lớn nhất tại đỉnh", [
  Cho miền nghiệm của hệ $x>=0$, $y>=0$, $x+y<=40$, $x+2y<=60$. Tìm giá trị lớn nhất của $F=3x+4y$.
], [
  Bốn đỉnh của miền nghiệm là:
  - $O(0;0)$;
  - $A(40;0)$, giao của $y=0$ và $x+y=40$;
  - $B(20;20)$, giao của $x+y=40$ và $x+2y=60$;
  - $C(0;30)$, giao của $x=0$ và $x+2y=60$.

  #table(columns: (1fr, 1fr, 1fr, 1fr, 1fr),
    table.header([#th[Đỉnh]], [#th[$O$]], [#th[$A$]], [#th[$B$]], [#th[$C$]]),
    [$F=3x+4y$], [$0$], [$120$], [$140$], [$120$],
  )

  Vậy $max F=140$ tại $(x;y)=(20;20)$.
])

#warning("HAI SAI LẦM TRONG BÀI TỐI ƯU", [
  Không được chỉ thử một điểm bất kì rồi kết luận tối ưu. Cũng không được tự ý làm tròn nghiệm khi $x,y$ nguyên: nếu đỉnh tối ưu không nguyên, phải xét các điểm nguyên *thỏa mãn mọi ràng buộc* ở gần và so sánh, vì làm tròn có thể làm vi phạm ràng buộc.
])

== 2.4. Luyện nhanh Chuyên đề 2

#drill("2A", [Cặp $(2;1)$ có là nghiệm của $3x-2y<=5$ không?])
#drill("2B", [Miền nghiệm của $x+y<2$ có chứa $O(0;0)$ và có chứa đường $x+y=2$ không?])
#drill("2C", [Tìm ba đỉnh miền nghiệm của hệ $x>=0$, $y>=0$, $2x+y<=8$.])
#drill("2D", [Mỗi hộp loại A nặng $2$ kg, loại B nặng $5$ kg. Xe chở không quá $40$ kg. Viết BPT cho $x$ hộp A và $y$ hộp B.])
#drill("2E", [Trên miền tam giác có đỉnh $(0;0),(4;0),(0;3)$, tìm GTLN của $F=2x+5y$.])

#answer-strip([
  *Đáp án luyện nhanh:* 2A. Có, vì $3.2-2.1=4<=5$.
  2B. Có chứa $O$; không lấy đường bờ $x+y=2$ vì dấu $<$ nghiêm ngặt.
  2C. $(0;0),(4;0),(0;8)$.
  2D. $2x+5y<=40$, kèm $x,y>=0$ (và nguyên nếu số hộp nguyên vẹn).
  2E. Giá trị tại ba đỉnh là $0,8,15$ nên $max F=15$ tại $(0;3)$.
])

= Chuyên đề 3 · Hệ thức lượng trong tam giác

#note("MỤC TIÊU THEO MA TRẬN", [
  Nhận biết và tính giá trị lượng giác của góc từ $0°$ đến $180°$; dùng quan hệ góc phụ, góc bù; tính giá trị còn lại từ một giá trị đã cho; nhận biết và vận dụng định lí côsin, định lí sin, công thức diện tích; giải bài toán thực tế.

  *Vị trí đề ôn:* Câu 7–10 · TLN 3–4 · TL 2.
])

== 3.1. Giá trị lượng giác của góc từ $0°$ đến $180°$

Trên nửa đường tròn đơn vị, với $M(x_0;y_0)$ sao cho $angle x O M=alpha$:
$ sin alpha=y_0, quad cos alpha=x_0, quad tan alpha=(sin alpha)/(cos alpha) quad(alpha!=90°), $
$ cot alpha=(cos alpha)/(sin alpha) quad(alpha!=0°,  alpha!=180°). $

#figure-local("assets/nua-duong-tron-don-vi.svg", 73%, [Hoành độ của $M$ là $cos alpha$; tung độ của $M$ là $sin alpha$.])

=== a) Dấu và hệ thức cơ bản

- Với $0°<=alpha<=180°$: $sin alpha>=0$.
- $alpha$ nhọn: $cos alpha>0$, $tan alpha>0$; $alpha$ tù: $cos alpha<0$, $tan alpha<0$ khi xác định.
- $sin^2 alpha+cos^2 alpha=1$.
- $1+tan^2 alpha=1/(cos^2 alpha)$ khi $cos alpha!=0$; $1+cot^2 alpha=1/(sin^2 alpha)$ khi $sin alpha!=0$.

=== b) Hai góc bù, hai góc phụ

#table(
  columns: (1.55fr, 2.5fr),
  table.header([#th[Quan hệ]], [#th[Công thức]]),
  [Bù nhau], [$sin(180°-alpha)=sin alpha$],
  [], [$cos(180°-alpha)=-cos alpha$],
  [], [$tan(180°-alpha)=-tan alpha$; $cot(180°-alpha)=-cot alpha$ khi xác định],
  [Phụ nhau ($0°<=alpha<=90°$)], [$sin(90°-alpha)=cos alpha$; $cos(90°-alpha)=sin alpha$],
  [], [$tan(90°-alpha)=cot alpha$; $cot(90°-alpha)=tan alpha$ khi xác định],
)

=== c) Góc đặc biệt cần thuộc

#table(
  columns: (1fr, 0.8fr, 0.8fr, 0.8fr, 0.8fr, 0.8fr, 0.8fr),
  table.header([#th[$alpha$]], [#th[$0°$]], [#th[$30°$]], [#th[$45°$]], [#th[$60°$]], [#th[$90°$]], [#th[$180°$]]),
  [$sin alpha$], [$0$], [$1/2$], [$sqrt(2)/2$], [$sqrt(3)/2$], [$1$], [$0$],
  [$cos alpha$], [$1$], [$sqrt(3)/2$], [$sqrt(2)/2$], [$1/2$], [$0$], [$-1$],
  [$tan alpha$], [$0$], [$sqrt(3)/3$], [$1$], [$sqrt(3)$], [—], [$0$],
)

Dùng quan hệ bù suy ra:
$ sin 120°=sqrt(3)/2, quad cos 120°=-1/2, quad tan 120°=-sqrt(3); $
$ sin 135°=sqrt(2)/2, quad cos 135°=-sqrt(2)/2, quad tan 135°=-1; $
$ sin 150°=1/2, quad cos 150°=-sqrt(3)/2, quad tan 150°=-sqrt(3)/3. $

#note("DÙNG MÁY TÍNH CẦM TAY", [
  Đặt chế độ *DEG* trước khi bấm $sin$, $cos$, $tan$. Khi tìm góc từ một giá trị lượng giác, kiểm tra khoảng $0°$–$180°$: chức năng nghịch đảo của sin thường trả về góc nhọn; nếu bài toán cần góc tù, dùng quan hệ $alpha=180°-beta$ khi thích hợp. Giữ nhiều chữ số trong máy và chỉ làm tròn ở kết quả cuối.
])

#example("VÍ DỤ 1 · Dùng hai góc bù", [
  Tính $sin 150°$, $cos 150°$, $tan 150°$.
], [
  Vì $150°=180°-30°$ nên sin giữ nguyên, cos và tan đổi dấu:
  $ sin 150°=sin 30°=1/2; $
  $ cos 150°=-cos 30°=-sqrt(3)/2; $
  $ tan 150°=-tan 30°=-sqrt(3)/3. $
])

#example("VÍ DỤ 2 · Biết một giá trị, tính các giá trị còn lại", [
  Cho $90°<alpha<180°$ và $cos alpha=-5/13$. Tính $sin alpha$ và $tan alpha$.
], [
  Vì $alpha$ tù nên $sin alpha>0$. Do đó
  $ sin alpha=sqrt(1-cos^2 alpha)=sqrt(1-25/169)=sqrt(144/169)=12/13. $
  Suy ra
  $ tan alpha=(sin alpha)/(cos alpha)=(12/13)/(-5/13)=-12/5. $
  Không chọn $sin alpha=-12/13$ vì sin của góc từ $0°$ đến $180°$ luôn không âm.
])

== 3.2. Hệ thức lượng trong tam giác

Xét tam giác $A B C$ với quy ước $a=B C$, $b=C A$, $c=A B$; $R,r$ lần lượt là bán kính đường tròn ngoại tiếp, nội tiếp; $p=(a+b+c)/2$; $S$ là diện tích.

#figure-local("assets/tam-giac-ki-hieu.svg", 65%, [Quy ước cạnh đối diện: cạnh $a$ đối diện góc $A$, cạnh $b$ đối diện góc $B$, cạnh $c$ đối diện góc $C$.])

=== a) Định lí côsin

$ a^2=b^2+c^2-2b c cos A; quad b^2=c^2+a^2-2c a cos B; quad c^2=a^2+b^2-2a b cos C. $

Hệ quả:
$ cos A=(b^2+c^2-a^2)/(2b c); quad cos B=(c^2+a^2-b^2)/(2c a); quad cos C=(a^2+b^2-c^2)/(2a b). $

Dùng khi biết *hai cạnh và góc xen giữa*, hoặc *ba cạnh* và cần tìm góc.

=== b) Định lí sin

$ a/(sin A)=b/(sin B)=c/(sin C)=2R. $

Dùng khi biết một cặp cạnh–góc đối và thêm một góc/cạnh nữa. Luôn nhớ $A+B+C=180°$.

=== c) Các công thức diện tích

$ S=1/2 b c sin A=1/2 c a sin B=1/2 a b sin C; $
$ S=(a b c)/(4R); quad S=p r; $
$ S=sqrt(p(p-a)(p-b)(p-c)) quad "(công thức Heron)". $

Ngoài ra, với đường cao $h_a$ ứng với cạnh $a$: $S=1/2 a h_a$.

#example("VÍ DỤ 3 · Hai cạnh và góc xen giữa", [
  Tam giác $A B C$ có $b=4$, $c=6$, $A=60°$. Tính $a$ và diện tích $S$.
], [
  Theo định lí côsin:
  $ a^2=4^2+6^2-2.4.6.cos 60°=16+36-48.1/2=28. $
  Vậy $a=sqrt(28)=2sqrt(7)$.

  Diện tích:
  $ S=1/2.4.6.sin 60°=12.sqrt(3)/2=6sqrt(3). $
])

#example("VÍ DỤ 4 · Dùng định lí sin", [
  Tam giác $A B C$ có $a=8$, $A=30°$, $B=45°$. Tính $b$.
], [
  Theo định lí sin:
  $ b=a.(sin B)/(sin A)=8.(sin 45°)/(sin 30°)=8.(sqrt(2)/2)/(1/2)=8sqrt(2). $
])

#example("VÍ DỤ 5 · Ba cạnh — công thức Heron", [
  Tính diện tích tam giác có ba cạnh $13,14,15$.
], [
  Nửa chu vi $p=(13+14+15)/2=21$.
  $ S=sqrt(21(21-13)(21-14)(21-15))=sqrt(21.8.7.6)=sqrt(7056)=84. $
])

=== d) Sơ đồ giải tam giác và bài toán thực tế

+ Vẽ hình, ghi dữ kiện và đơn vị; xác định cạnh/góc cần tìm.
+ Biết hai cạnh và góc xen giữa → định lí côsin; biết ba cạnh → côsin để tìm góc hoặc Heron để tìm diện tích.
+ Biết hai góc và một cạnh → tìm góc thứ ba rồi dùng định lí sin.
+ Kiểm tra nghiệm: cạnh dương; góc trong khoảng $(0°;180°)$; tổng ba góc $180°$; kết quả thực tế có đơn vị.

#warning("DẤU CỦA COS GÓC TÙ LÀ MỐI QUAN HỆ, KHÔNG PHẢI LỖI MÁY TÍNH", [
  Nếu $A>90°$ thì $cos A<0$, nên $-2b c cos A$ trở thành một đại lượng dương. Khi bấm máy, đặt máy ở chế độ *độ (DEG)*, không dùng radian. Chỉ làm tròn ở bước cuối và ghi đơn vị của kết quả.
])

== 3.3. Luyện nhanh Chuyên đề 3

#drill("3A", [Tính $sin 135°+cos 120°$.])
#drill("3B", [Cho $0°<alpha<90°$ và $sin alpha=5/13$. Tính $cos alpha$, $tan alpha$.])
#drill("3C", [Cho $a=5$, $b=7$, $C=60°$. Tính $c$.])
#drill("3D", [Cho $b=6$, $B=45°$, $A=30°$. Tính $a$.])
#drill("3E", [Cho $a=8$, $b=10$, $C=120°$. Tính diện tích $S$.])
#drill("3F", [Tính bán kính ngoại tiếp $R$ của tam giác có $a=10$, $A=30°$.])

#answer-strip([
  *Đáp án luyện nhanh:* 3A. $sqrt(2)/2-1/2=(sqrt(2)-1)/2$.
  3B. $cos alpha=12/13$, $tan alpha=5/12$.
  3C. $c^2=25+49-2.5.7.1/2=39$, nên $c=sqrt(39)$.
  3D. $a=b.(sin A)/(sin B)=6.(1/2)/(sqrt(2)/2)=3sqrt(2)$.
  3E. $S=1/2.8.10.sin 120°=20sqrt(3)$.
  3F. $2R=a/(sin A)=20$, nên $R=10$.
])

= Chuyên đề 4 · Vectơ — Các khái niệm mở đầu

#note("MỤC TIÊU THEO MA TRẬN", [
  Nhận biết vectơ, điểm đầu–điểm cuối, độ dài, giá; hai vectơ cùng phương, cùng hướng, ngược hướng, bằng nhau; vectơ-không; chứng minh hai vectơ bằng nhau trong trường hợp đơn giản.

  *Vị trí đề ôn:* Câu 11–12. *Không* kiểm tra các phép toán vectơ trong ma trận này.
])

== 4.1. Vectơ, độ dài và giá

- Vectơ là một đoạn thẳng có hướng. Vectơ có điểm đầu $A$, điểm cuối $B$ kí hiệu $arrow(A B)$.
- $arrow(A B)$ khác $arrow(B A)$ nếu $A!=B$ vì điểm đầu, điểm cuối và hướng khác nhau.
- Độ dài $arrow(A B)$ là độ dài đoạn $A B$: $|arrow(A B)|=A B>=0$.
- Đường thẳng đi qua điểm đầu và điểm cuối gọi là *giá* của vectơ.
- Nếu điểm đầu trùng điểm cuối, ta có *vectơ-không*, kí hiệu $arrow(0)$: $arrow(A A)=arrow(0)$, $|arrow(0)|=0$. Theo quy ước trong chương trình, vectơ-không cùng phương và cùng hướng với mọi vectơ.

== 4.2. Cùng phương, cùng hướng, bằng nhau

- Hai vectơ khác không *cùng phương* nếu giá của chúng song song hoặc trùng nhau.
- Hai vectơ cùng phương thì cùng hướng hoặc ngược hướng.
- Hai vectơ *bằng nhau* khi có *cùng độ dài và cùng hướng*.
- Hai vectơ *đối nhau* khi có *cùng độ dài và ngược hướng*. Chẳng hạn $arrow(A B)$ và $arrow(B A)$ đối nhau; vectơ đối của vectơ-không là vectơ-không.
- Hai vectơ có cùng độ dài chưa chắc bằng nhau; cùng phương cũng chưa chắc cùng hướng.

#figure-local("assets/hinh-binh-hanh-vecto.svg", 72%, [Trong hình bình hành $A B C D$: $arrow(A B)=arrow(D C)$ và $arrow(A D)=arrow(B C)$.])

#remember("DẤU HIỆU TRONG HÌNH BÌNH HÀNH", [
  Với đỉnh viết theo thứ tự $A,B,C,D$: $arrow(A B)=arrow(D C)$ (không phải $arrow(C D)$) và $arrow(A D)=arrow(B C)$. Hai vectơ bằng nhau không cần có cùng điểm đầu.
])

#example("VÍ DỤ 1 · Tính độ dài vectơ", [
  Cho hình chữ nhật $A B C D$ có $A B=6$, $B C=8$. Tính $|arrow(A C)|$.
], [
  $A C$ là đường chéo hình chữ nhật nên tam giác $A B C$ vuông tại $B$:
  $ A C=sqrt(A B^2+B C^2)=sqrt(36+64)=10. $
  Vậy $|arrow(A C)|=10$.
])

#example("VÍ DỤ 2 · Chứng minh hai vectơ bằng nhau", [
  Cho hình bình hành $A B C D$. Chứng minh $arrow(A B)=arrow(D C)$.
], [
  Vì $A B C D$ là hình bình hành nên $A B$ song song và bằng $D C$. Hơn nữa, hướng từ $A$ đến $B$ trùng với hướng từ $D$ đến $C$.

  Hai vectơ có cùng độ dài và cùng hướng nên $arrow(A B)=arrow(D C)$.
])

#example("VÍ DỤ 3 · Phân biệt các khái niệm", [
  Cho $arrow(A B)$ và $arrow(C D)$ có cùng độ dài $5$ nhưng giá vuông góc với nhau. Hai vectơ có cùng phương hoặc bằng nhau không?
], [
  Hai giá vuông góc nên không song song hoặc trùng nhau; do đó hai vectơ *không cùng phương*. Vì không cùng phương nên cũng không cùng hướng; dù cùng độ dài, chúng *không bằng nhau*.
])

=== Lỗi thường gặp ở Chuyên đề 4

- Đồng nhất đoạn thẳng $A B$ với vectơ $arrow(A B)$.
- Nói hai vectơ cùng độ dài thì bằng nhau.
- Viết $arrow(A B)=arrow(C D)$ trong hình bình hành $A B C D$; thực tế hai vectơ này ngược hướng.
- Cho rằng vectơ-không có độ dài tùy ý; đúng là $|arrow(0)|=0$.

== 4.3. Luyện nhanh Chuyên đề 4

#drill("4A", [Cho tam giác đều $A B C$ cạnh $a$. Tính $|arrow(A B)|$ và $|arrow(B A)|$.])
#drill("4B", [Hai vectơ có giá trùng nhau thì có thể kết luận gì về phương?])
#drill("4C", [Trong hình bình hành $A B C D$, điền vectơ bằng $arrow(A D)$.])
#drill("4D", [Nếu $arrow(A B)=arrow(0)$ thì hai điểm $A,B$ có quan hệ gì?])
#drill("4E", [Hai vectơ ngược hướng có thể cùng phương không? Có nhất thiết cùng độ dài không?])

#answer-strip([
  *Đáp án luyện nhanh:* 4A. Cả hai đều bằng $a$.
  4B. Chúng cùng phương; chưa kết luận cùng hướng hay ngược hướng nếu chưa nhìn hướng.
  4C. $arrow(B C)$.
  4D. $A$ trùng $B$.
  4E. Ngược hướng thì cùng phương; không nhất thiết cùng độ dài.
])

= Bảng công thức và quy trình ôn nhanh

== 5.1. Một trang công thức cốt lõi

#table(
  columns: (1.3fr, 3.8fr),
  table.header([#th[Chủ đề]], [#th[Phải nhớ]]),
  [Phủ định lượng từ], [$overline(forall x in X: P(x))<=>exists x in X, overline(P(x))$; $overline(exists x in X: P(x))<=>forall x in X, overline(P(x))$],
  [Tập hợp], [$A inter B$: cả hai; $A union B$: ít nhất một; $A without B$: thuộc $A$ không thuộc $B$; $C_U A=U without A$],
  [Đếm], [Số tập con: $2^n$; $n(A union B)=n(A)+n(B)-n(A inter B)$],
  [BPT hai ẩn], [Vẽ bờ → chọn nét liền/đứt → thử điểm → chọn nửa mặt phẳng → ghi có/không lấy bờ],
  [Hệ BPT], [Miền nghiệm là giao các miền thành phần; tọa độ đỉnh từ giao các đường bờ],
  [Tối ưu], [Với đa giác kín giới hạn, lập bảng $F=m x+n y$ tại các đỉnh để tìm max/min],
  [Lượng giác], [$sin^2 alpha+cos^2 alpha=1$; $tan alpha=(sin alpha)/(cos alpha)$; sin góc bù giữ nguyên, cos/tan/cot đổi dấu],
  [Định lí côsin], [$a^2=b^2+c^2-2b c cos A$; $cos A=(b^2+c^2-a^2)/(2b c)$],
  [Định lí sin], [$a/(sin A)=b/(sin B)=c/(sin C)=2R$],
  [Diện tích], [$S=1/2b c sin A=(a b c)/(4R)=p r=sqrt(p(p-a)(p-b)(p-c))$],
  [Vectơ], [$|arrow(A B)|=A B$; bằng nhau $=>$ cùng độ dài và cùng hướng; $|arrow(0)|=0$],
)

== 5.2. Sơ đồ chọn công cụ theo dữ kiện

#grid(columns: (1fr, 1fr), column-gutter: 9pt, row-gutter: 9pt,
  note("TẬP HỢP HỮU HẠN", [Liệt kê nếu cần → đánh dấu phần chung → tính giao trước → hợp/hiệu/phần bù sau → kiểm tra số phần tử.]),
  note("KHOẢNG–ĐOẠN", [Vẽ trục số → chú ý đầu đặc/rỗng → giao lấy phần chồng nhau → hợp lấy phần được tô ít nhất một lần.]),
  note("MIỀN NGHIỆM", [Đường bờ → điểm thử → nửa mặt phẳng → giao với các ràng buộc khác → tìm đỉnh nếu cần tối ưu.]),
  note("TAM GIÁC", [Hai cạnh + góc xen: côsin. Hai góc + một cạnh: sin. Ba cạnh: côsin/Heron. Hai cạnh + góc xen: diện tích bằng $1/2a b sin C$.]),
  note("MỆNH ĐỀ", [Xác định đúng–sai trước khi gọi là mệnh đề → phủ định vị từ → với lượng từ, đổi $forall$ và $exists$ nhưng giữ miền.]),
  note("VECTƠ", [Nhìn giá để xét phương → nhìn mũi tên để xét hướng → so độ dài → chỉ kết luận bằng nhau khi đủ cả hướng và độ dài.]),
)

#remember("KIỂM TRA CUỐI BÀI TRONG 60 GIÂY", [
  *Mệnh đề:* phủ định có đủ dấu bằng không?
  *Tập hợp:* đầu mút và phần tử chung đã đúng chưa?
  *BPT:* nét bờ và phía miền nghiệm có khớp điểm thử không?
  *Lượng giác:* máy ở DEG, dấu cos/tan đã đúng chưa?
  *Tam giác:* công thức có đúng cặp cạnh–góc và kết quả có đơn vị không?
  *Vectơ:* đã đủ cùng hướng *và* cùng độ dài chưa?
])
