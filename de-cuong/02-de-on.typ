#import "style.typ": *

= Đề ôn tổng hợp · 90 phút

#source-note("BẢN ÔN TẬP BIÊN SOẠN MỚI", [
  Đề dưới đây bám sát từng vị trí của *ma trận và bảng đặc tả 2026–2027* được cung cấp. Đây *không phải nguyên văn đề thi chính thức* vì tệp nguồn không chứa đề thi. Học sinh làm trong 90 phút, không xem phần đáp án cho đến khi hoàn thành.
])

#align(center)[
  #text(fill: navy, size: 15pt, weight: "bold")[ĐỀ ÔN KIỂM TRA GIỮA HỌC KÌ I]\
  #text(weight: "bold")[MÔN: TOÁN 10 · NĂM HỌC 2026–2027]\
  #text(size: 9.5pt, fill: muted)[Thời gian: 90 phút · Tổng điểm: 10 · Không kể thời gian phát đề]
]
#v(5pt)
#block[
  #set par(justify: false)
  #grid(columns: (1.5fr, 0.85fr, 0.75fr), column-gutter: 8pt,
    [Họ và tên: ..................................],
    [Lớp: ................],
    [Điểm: ..............],
  )
]

== Phần I · Trắc nghiệm nhiều phương án lựa chọn

*12 câu · 3,0 điểm.* Mỗi câu chỉ chọn *một* phương án đúng.

#exam-question("C1", level: "NB")[
  Trong các câu sau, câu nào là một *mệnh đề*?
  #two-options([$x+2>5$.], [Các em hãy đọc kĩ đề!], [$12$ chia hết cho $3$.], [Bạn đã hoàn thành bài tập chưa?])
]

#exam-question("C2", level: "NB")[
  Phủ định của mệnh đề “$exists x in RR, x^2+1=0$” là
  #two-options(
    [$forall x in RR, x^2+1!=0$.],
    [$forall x in RR, x^2+1=0$.],
    [$exists x in RR, x^2+1!=0$.],
    [$exists x in RR, x^2+1>0$.],
  )
]

#exam-question("C3", level: "NB")[
  Tập hợp $A={x in ZZ | x^2<10}$ được viết bằng cách liệt kê là
  #two-options(
    [${0;1;2;3}$.],
    [${-3;-2;-1;1;2;3}$.],
    [${-3;-2;-1;0;1;2}$.],
    [${-3;-2;-1;0;1;2;3}$.],
  )
]

#exam-question("C4", level: "NB")[
  Trong biểu đồ Ven dưới đây, phần tô màu biểu diễn tập hợp nào?
  #figure-local("assets/venn-giao.svg", 49%, [Hai tập $A,B$ trong cùng tập vũ trụ $U$.])
  #two-options([$A union B$.], [$A inter B$.], [$A without B$.], [$U without (A union B)$.])
]

#exam-question("C5", level: "NB")[
  Bất phương trình nào sau đây là *bất phương trình bậc nhất hai ẩn* $x,y$?
  #two-options([$x^2+y>1$.], [$2x-3y<=6$.], [$x+1/y>=2$.], [$x y<4$.])
]

#exam-question("C6", level: "NB")[
  Cặp số nào là nghiệm của hệ $cases(x+y<=4, x-y>=0)$?
  #four-options([$(1;1)$], [$(0;5)$], [$(-1;2)$], [$(3;2)$])
]

#exam-question("C7", level: "NB")[
  Giá trị của $cos 120°$ bằng
  #four-options([$sqrt(3)/2$], [$1/2$], [$-1/2$], [$-sqrt(3)/2$])
]

#exam-question("C8", level: "TH")[
  Cho $90°<alpha<180°$ và $sin alpha=3/5$. Giá trị của $cos alpha$ là
  #four-options([$-4/5$], [$4/5$], [$-3/4$], [$3/4$])
]

#exam-question("C9", level: "NB")[
  Với tam giác $A B C$ có $a=B C$, $b=C A$, $c=A B$, công thức nào là *định lí côsin*?
  #two-options(
    [$a^2=b^2+c^2+2b c cos A$.],
    [$a^2=b^2+c^2-2b c sin A$.],
    [$a=b^2+c^2-2b c cos A$.],
    [$a^2=b^2+c^2-2b c cos A$.],
  )
]

#exam-question("C10", level: "TH")[
  Tam giác $A B C$ có $b=5$, $c=7$, $A=60°$. Độ dài cạnh $a$ bằng
  #four-options([$6$], [$sqrt(74)$], [$sqrt(39)$], [$sqrt(109)$])
]

#exam-question("C11", level: "NB")[
  Khẳng định nào sau đây *đúng*?
  #two-options(
    [$|arrow(A B)|=-A B$ với mọi $A,B$.],
    [$arrow(A B)=arrow(B A)$ với mọi $A,B$.],
    [Hai vectơ có cùng độ dài thì bằng nhau.],
    [Vectơ-không cùng phương và cùng hướng với mọi vectơ.],
  )
]

#exam-question("C12", level: "TH")[
  Cho hình bình hành $A B C D$. Đẳng thức vectơ nào sau đây đúng?
  #two-options(
    [$arrow(A B)=arrow(C D)$.],
    [$arrow(A B)=arrow(D C)$.],
    [$arrow(A D)=arrow(C B)$.],
    [$arrow(A C)=arrow(B D)$.],
  )
]

== Phần II · Trắc nghiệm đúng–sai

*2 câu · 2,0 điểm.* Đánh dấu *Đ* hoặc *S* cho từng ý. Trong mỗi câu: đúng 1 ý được 0,1 điểm; đúng 2 ý được 0,25 điểm; đúng 3 ý được 0,5 điểm; đúng 4 ý được 1,0 điểm.

#exam-question("ĐS1", level: "NB–VD")[
  Cho $U={1;2;3;4;5;6}$, $A={1;2;3;4}$, $B={3;4;5}$. Xét tính đúng–sai của các khẳng định:
  #table(
    columns: (0.45fr, 5.4fr, 0.65fr),
    table.header([#th[Ý]], [#th[Khẳng định]], [#th[Đ/S]]),
    [a], [$2 in A$ và ${2} subset A$.], [],
    [b], [Tập $(1;4]$ được biểu diễn trên trục số bằng đầu mút $1$ rỗng, đầu mút $4$ đặc và phần nối giữa hai mút.], [],
    [c], [$A inter B={3;4}$ và $A union B={1;2;3;4;5}$.], [],
    [d], [$A without B={1;2;5}$.], [],
  )
]

#exam-question("ĐS2", level: "NB–VD")[
  Cho bất phương trình $x+2y<=4$ và đường thẳng $d:x+2y=4$. Xét tính đúng–sai:
  #table(
    columns: (0.45fr, 5.4fr, 0.65fr),
    table.header([#th[Ý]], [#th[Khẳng định]], [#th[Đ/S]]),
    [a], [Cặp $(2;1)$ là một nghiệm của bất phương trình.], [],
    [b], [Miền nghiệm là nửa mặt phẳng bờ $d$ *không* chứa gốc $O(0;0)$.], [],
    [c], [Đường $d$ được vẽ nét liền và được tính vào miền nghiệm.], [],
    [d], [Nếu $x,y$ là số gói hàng loại A, B; mỗi gói A nặng $1$ kg, mỗi gói B nặng $2$ kg và tổng khối lượng không quá $4$ kg thì điều kiện khối lượng được mô hình bởi $x+2y<=4$, với $x,y in NN$ (do đó $x>=0$, $y>=0$).], [],
  )
]

== Phần III · Trắc nghiệm trả lời ngắn

*4 câu · 2,0 điểm.* Mỗi câu 0,5 điểm. Chỉ ghi kết quả cuối cùng vào chỗ trống; nên ghi nháp đủ bước để tự kiểm tra.

#exam-question("TLN1", level: "TH")[
  Tập hợp $A$ có $5$ phần tử. Hỏi $A$ có bao nhiêu tập hợp con (kể cả tập rỗng và chính $A$)?

  *Đáp số:* ....................................
]

#exam-question("TLN2", level: "VD")[
  Trong một nhóm $40$ học sinh, có $25$ em thích môn Toán, $18$ em thích môn Vật lí và $8$ em thích cả hai môn. Hỏi có bao nhiêu em thích *ít nhất một* trong hai môn?

  *Đáp số:* ....................................
]

#exam-question("TLN3", level: "VD")[
  Cho $90°<alpha<180°$ và $cos alpha=-1/3$. Tính giá trị biểu thức
  $ P=3 sin^2alpha+2 cos alpha. $

  *Đáp số:* ....................................
]

#exam-question("TLN4", level: "TH")[
  Tam giác $A B C$ có $b=6$, $c=8$, $A=150°$. Tính diện tích tam giác $A B C$.

  *Đáp số:* ....................................
]

== Phần IV · Tự luận

*3 câu · 3,0 điểm.* Trình bày rõ công thức, các bước biến đổi và kết luận.

#exam-question("TL1", level: "TH · 1,0 đ")[
  Cho $U={1;2;3;4;5;6;7;8}$, $A={1;2;3;4;5;6}$, $B={4;5;6;7}$.

  a) Tìm $A inter B$ và $A union B$.

  b) Tìm $A without B$ và $C_U A$.
]

#exam-question("TL2", level: "VD · 1,0 đ")[
  Hai vị trí $A,B$ ở hai bên một phần mặt hồ nên không thể đo trực tiếp khoảng cách $A B$. Người ta chọn điểm $C$ có thể đo được $C A=80$ m, $C B=50$ m và $angle A C B=60°$. Tính khoảng cách $A B$.
  #figure-local("assets/tam-giac-thuc-te.svg", 58%, [Sơ đồ minh họa, hình không vẽ theo đúng tỉ lệ.])
]

#exam-question("TL3", level: "VDC · 1,0 đ")[
  Một cơ sở sản xuất hai loại sản phẩm X, Y. Gọi $x,y$ lần lượt là số sản phẩm X, Y sản xuất trong một ngày ($x,y in NN$). Các ràng buộc được cho bởi
  $ cases(x+y<=50, 2x+y<=80, x>=0, y>=0). $
  Lợi nhuận thu được là $F=3x+2y$ (triệu đồng). Xác định miền nghiệm của hệ ràng buộc và tìm phương án sản xuất để lợi nhuận lớn nhất trong ngày.
]

#v(10pt)
#align(center)[#std.line(length: 35%, stroke: 0.8pt + line)\ #text(weight: "bold", fill: navy)[HẾT]\ #text(size: 9pt, fill: muted)[Hãy kiểm tra lại các câu đã đánh dấu trước khi xem đáp án.]]
