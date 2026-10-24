#import "style.typ": *

= Đáp án và lời giải chi tiết đề ôn

#warning("CHỈ MỞ SAU KHI ĐÃ LÀM ĐỀ", [
  Chấm bằng bảng đáp án nhanh trước. Sau đó đọc lời giải của *cả câu đúng lẫn câu sai*: câu đúng nhờ phỏng đoán vẫn cần được ghi vào phiếu lỗi để kiểm tra lại phương pháp.
])

== 1. Bảng đáp án nhanh

=== Phần I · Chọn phương án

#table(
  columns: (1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr),
  table.header([#th[Câu]], [#th[1]], [#th[2]], [#th[3]], [#th[4]], [#th[5]], [#th[6]]),
  [*Đáp án*], [*C*], [*A*], [*D*], [*B*], [*B*], [*A*],
)
#v(5pt)
#table(
  columns: (1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr),
  table.header([#th[Câu]], [#th[7]], [#th[8]], [#th[9]], [#th[10]], [#th[11]], [#th[12]]),
  [*Đáp án*], [*C*], [*A*], [*D*], [*C*], [*D*], [*B*],
)

=== Phần II · Đúng–sai

#table(
  columns: (1.1fr, 1fr, 1fr, 1fr, 1fr),
  table.header([#th[Câu]], [#th[a]], [#th[b]], [#th[c]], [#th[d]]),
  [*ĐS1*], [*Đ*], [*Đ*], [*Đ*], [*S*],
  [*ĐS2*], [*Đ*], [*S*], [*Đ*], [*Đ*],
)

=== Phần III · Trả lời ngắn

#table(
  columns: (1fr, 1.5fr, 2.5fr),
  table.header([#th[Câu]], [#th[Đáp số]], [#th[Kết quả cần ghi]]),
  [TLN1], [$32$], [32],
  [TLN2], [$35$], [35],
  [TLN3], [$2$], [2],
  [TLN4], [$12$], [12],
)

== 2. Giải thích 12 câu chọn phương án

#drill("C1", [*Chọn C.* “$12$ chia hết cho $3$” là khẳng định có tính đúng xác định. Phương án A là mệnh đề chứa biến; B là câu cầu khiến; D là câu hỏi.])
#drill("C2", [*Chọn A.* Phủ định $exists$ thành $forall$, giữ miền $RR$ và phủ định $x^2+1=0$ thành $x^2+1!=0$.])
#drill("C3", [*Chọn D.* Với $x in ZZ$, $x^2<10<16$ nên $-3<=x<=3$; cả $0$ và $±3$ đều thỏa mãn.])
#drill("C4", [*Chọn B.* Phần tô màu là vùng chung của $A$ và $B$, tức $A inter B$.])
#drill("C5", [*Chọn B.* $2x-3y<=6$ có dạng $a x+b y<=c$. Các phương án còn lại chứa $x^2$, $1/y$ hoặc $x y$ nên không là bậc nhất hai ẩn.])
#drill("C6", [*Chọn A.* Với $(1;1)$: $1+1=2<=4$ và $1-1=0>=0$. Mỗi phương án còn lại vi phạm ít nhất một BPT.])
#drill("C7", [*Chọn C.* $cos 120°=cos(180°-60°)=-cos 60°=-1/2$.])
#drill("C8", [*Chọn A.* $cos^2 alpha=1-(3/5)^2=16/25$. Vì $alpha$ tù nên $cos alpha<0$, do đó $cos alpha=-4/5$.])
#drill("C9", [*Chọn D.* Định lí côsin cho cạnh $a$: $a^2=b^2+c^2-2b c cos A$, với $A$ là góc xen giữa $b,c$.])
#drill("C10", [*Chọn C.* $a^2=5^2+7^2-2.5.7.cos 60°=74-35=39$, nên $a=sqrt(39)$ vì $a>0$.])
#drill("C11", [*Chọn D.* Theo quy ước, vectơ-không cùng phương và cùng hướng với mọi vectơ. Cùng độ dài chưa đủ để hai vectơ bằng nhau; $arrow(A B)$ và $arrow(B A)$ thường khác nhau.])
#drill("C12", [*Chọn B.* Trong hình bình hành $A B C D$, $arrow(A B)$ và $arrow(D C)$ cùng hướng, cùng độ dài. Phương án A chọn hai vectơ ngược hướng.])

== 3. Giải thích câu đúng–sai

#solution-heading("ĐS1", "Tập hợp và các phép toán")

- *a) Đúng.* $2$ là một phần tử của $A$ nên $2 in A$; tập ${2}$ có mọi phần tử thuộc $A$ nên ${2} subset A$.
- *b) Đúng.* $(1;4]$ tương ứng $1<x<=4$: loại mút $1$, lấy mút $4$.
- *c) Đúng.* Phần chung là ${3;4}$; gom mọi phần tử không lặp được $A union B={1;2;3;4;5}$.
- *d) Sai.* $A without B$ chỉ giữ phần tử thuộc $A$ nhưng không thuộc $B$, nên kết quả đúng là ${1;2}$, không có $5$.

#solution-heading("ĐS2", "Nghiệm, miền nghiệm và mô hình thực tế")

- *a) Đúng.* Thay $(2;1)$: $2+2.1=4<=4$.
- *b) Sai.* Thay $O(0;0)$: $0+2.0=0<=4$, nên miền nghiệm là nửa mặt phẳng bờ $d$ *có chứa $O$*.
- *c) Đúng.* Dấu $<=$ cho phép lấy dấu bằng, nên đường bờ thuộc miền nghiệm và được vẽ nét liền.
- *d) Đúng.* $x$ gói nặng $1$ kg và $y$ gói nặng $2$ kg có tổng khối lượng $x+2y$; “không quá $4$ kg” cho $x+2y<=4$. Số gói còn phải thỏa mãn điều kiện không âm và nguyên.

== 4. Lời giải phần trả lời ngắn

#solution-heading("TLN1", "Số tập con")
Tập có $n$ phần tử có $2^n$ tập con. Với $n=5$:
$ 2^5=32. $
*Ghi đáp số: $32$.* Thang điểm: 0,5 nếu đúng kết quả.

#solution-heading("TLN2", "Bài toán hai tập hợp")
Gọi $T,V$ lần lượt là tập học sinh thích Toán, Vật lí. Theo công thức cộng phần tử:
$ n(T union V)=25+18-8=35. $
Trừ $8$ vì nhóm thích cả hai môn đã được tính hai lần. *Ghi đáp số: $35$.* Thang điểm: 0,5 nếu đúng kết quả.

#solution-heading("TLN3", "Biểu thức lượng giác")
Từ $sin^2 alpha+cos^2 alpha=1$ và $cos alpha=-1/3$:
$ sin^2 alpha=1-1/9=8/9. $
Không cần tính dấu của $sin alpha$ vì biểu thức chỉ chứa $sin^2 alpha$. Thay vào:
$ P=3.8/9+2.(-1/3)=8/3-2/3=2. $
*Ghi đáp số: $2$.* Thang điểm: 0,5 nếu đúng kết quả.

#solution-heading("TLN4", "Diện tích tam giác")
Hai cạnh $b,c$ kẹp góc $A$, nên
$ S=1/2 b c sin A=1/2.6.8.sin 150°=24.1/2=12. $
*Ghi đáp số: $12$.* Thang điểm: 0,5 nếu đúng kết quả; nếu đề yêu cầu đơn vị diện tích thì dùng đơn vị vuông tương ứng.

== 5. Tự luận · Lời giải và thang điểm

#solution-heading("TL1", "Các phép toán tập hợp · 1,0 điểm")

a) Phần tử thuộc cả $A$ và $B$ là $4,5,6$:
$ A inter B={4;5;6}. $
Gom mọi phần tử của hai tập, mỗi phần tử viết một lần:
$ A union B={1;2;3;4;5;6;7}. $

b) Trong $A$, loại các phần tử đã thuộc $B$:
$ A without B={1;2;3}. $
Phần bù của $A$ trong $U$:
$ C_U A=U without A={7;8}. $

#table(
  columns: (3.8fr, 1fr),
  table.header([#th[Ý chấm]], [#th[Điểm]]),
  [$A inter B={4;5;6}$], [0,25],
  [$A union B={1;2;3;4;5;6;7}$], [0,25],
  [$A without B={1;2;3}$], [0,25],
  [$C_U A={7;8}$], [0,25],
)

#solution-heading("TL2", "Khoảng cách qua vật cản · 1,0 điểm")

Tam giác $A B C$ có hai cạnh $C A=80$, $C B=50$ và góc xen giữa $C=60°$. Theo định lí côsin:
$ A B^2=C A^2+C B^2-2.C A.C B.cos C $
$ =80^2+50^2-2.80.50.cos 60° $
$ =6400+2500-8000.1/2=4900. $
Vì $A B>0$ nên $A B=sqrt(4900)=70$ (m).

*Kết luận:* khoảng cách hai vị trí là $A B=70$ m.

#table(
  columns: (3.8fr, 1fr),
  table.header([#th[Ý chấm]], [#th[Điểm]]),
  [Viết đúng định lí côsin và thay đủ $80,50,60°$], [0,50],
  [Tính $A B^2=4900$, suy ra $A B=70$], [0,25],
  [Kết luận với đơn vị mét], [0,25],
)

#solution-heading("TL3", "Miền nghiệm và phương án tối ưu · 1,0 điểm")

Miền nghiệm nằm trong góc phần tư thứ nhất do $x>=0,y>=0$. Vì $O(0;0)$ thỏa mãn $x+y<=50$ và $2x+y<=80$, ta chọn các nửa mặt phẳng chứa $O$ của hai đường bờ tương ứng.

Miền nghiệm là tứ giác $O A B C$, kể cả biên, với:
- $O(0;0)$;
- $A(40;0)$, giao của $y=0$ với $2x+y=80$ (điểm này cũng thỏa mãn $x+y<=50$);
- $B(30;20)$, giao của $x+y=50$ và $2x+y=80$;
- $C(0;50)$, giao của $x=0$ với $x+y=50$.

#figure-local("assets/mien-nghiem-he.svg", 69%, [Miền tứ giác $O A B C$ và bốn đỉnh cần xét.])

Lập bảng giá trị của $F=3x+2y$:
#table(
  columns: (1.25fr, 1fr, 1fr, 1fr, 1fr),
  table.header([#th[Đỉnh]], [#th[$O(0;0)$]], [#th[$A(40;0)$]], [#th[$B(30;20)$]], [#th[$C(0;50)$]]),
  [$F$ (triệu đồng)], [$0$], [$120$], [$130$], [$100$],
)

Giá trị lớn nhất là $130$ tại $B(30;20)$. Cặp này có $x,y$ nguyên không âm và thỏa mãn $30+20=50$, $2.30+20=80$.

*Kết luận:* sản xuất *30 sản phẩm X và 20 sản phẩm Y* để lợi nhuận lớn nhất *130 triệu đồng/ngày*.

#table(
  columns: (3.8fr, 1fr),
  table.header([#th[Ý chấm]], [#th[Điểm]]),
  [Xác định đúng miền nghiệm và bốn đỉnh $O,A,B,C$], [0,40],
  [Tính đúng $F$ tại bốn đỉnh và chọn giá trị lớn nhất], [0,30],
  [Nêu phương án $(30;20)$ và lợi nhuận $130$ triệu đồng], [0,30],
)

== 6. Phiếu tự chấm và chữa lỗi

#table(
  columns: (1.4fr, 1fr, 1.5fr, 2.4fr),
  table.header([#th[Nhóm câu]], [#th[Điểm]], [#th[Lỗi mắc]], [#th[Việc làm lại sau 24 giờ]]),
  [Chọn phương án / 3,0], [........], [........................], [............................................],
  [Đúng–sai / 2,0], [........], [........................], [............................................],
  [Trả lời ngắn / 2,0], [........], [........................], [............................................],
  [Tự luận / 3,0], [........], [........................], [............................................],
  [*Tổng / 10,0*], [........], [], [],
)
