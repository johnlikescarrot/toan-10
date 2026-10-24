#set document(title: "Đề cương ôn tập Toán 10 – Giữa học kì I 2026–2027", author: "Tài liệu ôn tập tự biên soạn theo ma trận THPT Hà Huy Tập", date: datetime(year: 2026, month: 10, day: 24))
#set text(font: "DejaVu Serif", size: 10.5pt, lang: "vi")
#set par(justify: true, leading: 0.62em)
#set page(paper: "a4", margin: (x: 19mm, top: 19mm, bottom: 19mm), numbering: "1", header: context { if counter(page).get().first() > 1 { text(font: "DejaVu Sans", size: 8pt, fill: rgb("526575"))[TOÁN 10 · KẾT NỐI TRI THỨC #h(1fr) GIỮA HỌC KÌ I · 2026–2027] } }, footer: context { align(center, text(size: 8pt, fill: rgb("526575"))[Ôn tập theo ma trận · Đề minh họa, không phải đề thi gốc #h(5mm) #counter(page).display()]) })
#set heading(numbering: none)
#show heading.where(level: 1): it => block(above: 0pt, below: 12pt)[#text(font: "DejaVu Sans", size: 21pt, weight: "bold", fill: rgb("123e55"), it.body)]
#show heading.where(level: 2): it => block(above: 10pt, below: 5pt)[#text(font: "DejaVu Sans", size: 12pt, weight: "bold", fill: rgb("166976"), it.body)]
#show heading.where(level: 3): it => block(above: 7pt, below: 4pt)[#text(size: 10.5pt, weight: "bold", it.body)]
#let note(body) = block(width: 100%, inset: 10pt, fill: rgb("edf5f6"), radius: 4pt, body)
#let warn(body) = block(width: 100%, inset: 10pt, fill: rgb("fff4df"), radius: 4pt, body)
#let answer(body) = block(inset: (left: 10pt), stroke: (left: 2pt + rgb("19848a")), body)
#let opts(a,b,c,d) = grid(columns: (1fr, 1fr), gutter: 5pt, [*A.* #a], [*B.* #b], [*C.* #c], [*D.* #d])
#let newpage() = pagebreak()

#v(17mm)
#text(font: "DejaVu Sans", size: 12pt, fill: rgb("166976"), weight: "bold")[SỔ TAY TỰ HỌC · KẾT NỐI TRI THỨC VỚI CUỘC SỐNG]
#v(9mm)
#text(font: "DejaVu Sans", size: 37pt, weight: "bold", fill: rgb("123e55"))[TOÁN 10]
#v(4mm)
#text(font: "DejaVu Sans", size: 25pt, weight: "bold")[Ôn tập giữa học kì I]
#v(3mm)
#text(size: 18pt)[Năm học 2026–2027]
#v(12mm)
#note[
*Đọc hiểu → Nắm phương pháp → Luyện dạng → Thi thử → Tự sửa lỗi*

Mệnh đề và tập hợp · Bất phương trình và hệ bất phương trình bậc nhất hai ẩn · Hệ thức lượng trong tam giác · Khái niệm vectơ.
]
#v(8mm)
Biên soạn theo tệp *“MA TRẬN TOÁN 10 - GIỮA KÌ I.docx”*, ghi tên Trường THPT Hà Huy Tập, Tổ Toán–Tin. Tài liệu độc lập phục vụ ôn tập; không phải ấn phẩm hoặc đề kiểm tra được nhà trường xác nhận.
#v(7mm)
#warn[*Thông tin quan trọng:* Tệp nguồn chỉ có ma trận và bảng đặc tả, không chứa đề thi hoặc đáp án gốc. Toàn bộ ví dụ, bài luyện và đề minh họa ở đây được tự biên soạn, có đáp án đầy đủ. Không thể khẳng định đây là “tất cả câu hỏi và đáp án của đề thi thật 2026–2027”.]
#v(1fr)
#text(size: 9pt)[Bản biên soạn ngày 24/10/2026 · Có nguồn tham khảo, bảng đối chiếu ma trận và hướng dẫn tự chấm.]
#newpage()
= Cách dùng tài liệu
#outline(title: [Mục lục], depth: 1, indent: auto)
#v(5pt)
== Lộ trình tự học trong 7 buổi
#table(columns: (auto, 1fr, 1fr), inset: 5pt, stroke: 0.4pt + luma(80%),
[*Buổi*], [*Trọng tâm*], [*Sản phẩm cần đạt*],
[1], [Mệnh đề, lượng từ], [Viết đúng phủ định; phân biệt cần và đủ.],
[2], [Tập hợp, khoảng và đoạn], [Giải phép toán, đếm tập con, bài toán hai nhóm.],
[3], [Bất phương trình hai ẩn], [Vẽ nửa mặt phẳng, xác định biên và điểm thử.],
[4], [Hệ bất phương trình], [Lập mô hình, tìm các đỉnh và tối ưu.],
[5], [Lượng giác và tam giác], [Chọn đúng sin/côsin/diện tích, dùng DEG.],
[6], [Vectơ và bài luyện], [Nhận diện cùng hướng, bằng nhau; chữa bài sai.],
[7], [Đề minh họa 90 phút], [Tự chấm, ghi nguyên nhân từng lỗi.])

Mỗi buổi gợi ý 60–90 phút. Đọc lý thuyết, che lời giải để tự làm ví dụ, rồi làm bài luyện trước khi xem đáp án. Nếu chỉ còn 2 ngày: ngày 1 học phần kiến thức và sửa bài luyện; ngày 2 làm đề thi thử, sau đó học lại đúng các mục mình mất điểm.
#newpage()
= 1. Giải mã ma trận và phạm vi
== 1.1. Những gì tệp Word thực sự cung cấp
Tệp nguồn có mục tiêu, hình thức kiểm tra, bảng ma trận, mô tả ba câu tự luận và bảng đặc tả. Các dòng “Câu 1”, “Câu 2”, … trong đặc tả là *mô tả năng lực cần kiểm tra*, không phải nội dung câu hỏi có dữ kiện cụ thể. Không có đáp án chính thức kèm theo.

Theo mục lục SGK Kết nối tri thức, phạm vi này ứng với Bài 1–7 của tập một: Bài 1 Mệnh đề; Bài 2 Tập hợp và các phép toán; Bài 3–4 Bất phương trình và hệ bất phương trình bậc nhất hai ẩn; Bài 5–6 Giá trị lượng giác và hệ thức lượng trong tam giác; Bài 7 Các khái niệm mở đầu về vectơ. Đối chiếu mục lục: #link("https://toanmath.com/2022/01/sach-giao-khoa-toan-10-tap-1-ket-noi-tri-thuc-voi-cuoc-song.html")[\[2\]]. Không mở rộng sang tổng, hiệu, tích vô hướng hay tọa độ vectơ.

== 1.2. Cấu trúc điểm phải nhớ
#table(columns: (1fr, auto, auto), inset: 7pt, stroke: 0.4pt + luma(80%),
[*Phần*], [*Số câu*], [*Điểm*],
[Nhiều phương án lựa chọn], [12], [3,0],
[Đúng–sai (4 ý/câu)], [2], [2,0],
[Trả lời ngắn], [4], [2,0],
[Tự luận], [3], [3,0],
[*Tổng · 90 phút*], [*21 câu lớn*], [*10,0*])

Mỗi câu lựa chọn đúng: 0,25 điểm. Mỗi câu trả lời ngắn: 0,5 điểm. Tự luận gồm 3 câu, mỗi câu 1 điểm. Mỗi câu đúng–sai được chấm theo *số ý trả lời đúng trong chính câu đó*:
#table(columns: (1fr, auto, auto, auto, auto, auto), inset: 5pt,
[Số ý đúng], [0], [1], [2], [3], [4],
[Điểm/câu], [0], [0,10], [0,25], [0,50], [1,00])
Không chia đều 0,25 điểm cho từng ý đúng–sai. Có 8 ý đúng–sai; con số “24” ở cột tổng trắc nghiệm của ma trận được hiểu là $12 + 8 + 4$, không phải 24 câu lớn độc lập.

Theo nhóm chương, ma trận hướng tới: *Mệnh đề–tập hợp 4,0 điểm (40%); bất phương trình–hệ 2,5 điểm (25%); lượng giác–tam giác 3,0 điểm (30%); khái niệm vectơ 0,5 điểm (5%)*. Ưu tiên thời gian luyện tập tương ứng, nhưng không bỏ phần vectơ nhận biết dễ lấy điểm.

== 1.3. Các điểm chưa thống nhất và cách biên soạn
- Mô tả tự luận câu 2 ghi MĐ2, còn ma trận và đặc tả có chỗ xếp vận dụng. Giữ đúng *dạng bài thực tiễn hệ thức lượng đơn giản*, không nâng độ khó tùy ý.
- Hàng hệ thức lượng trong đặc tả có ô số lượng nhận biết không khớp cách liệt kê câu 9–10. Ưu tiên số câu và mức độ ở bảng ma trận chính: câu 9 nhận biết, câu 10 thông hiểu.
- Các điểm phân bổ nhỏ trong nhóm đúng–sai chỉ dùng để tham khảo nội dung. Do thang điểm phi tuyến, không diễn giải chúng thành điểm cố định cho từng ý.
#newpage()
= 2. Mệnh đề: nói đúng bằng ngôn ngữ toán
== 2.1. Các khái niệm cốt lõi
*Mệnh đề* là câu khẳng định có giá trị đúng hoặc sai xác định. Câu hỏi, mệnh lệnh không phải mệnh đề. “$x+2>0$” khi chưa xác định $x$ là mệnh đề chứa biến; thay $x$ bằng một giá trị hoặc dùng lượng từ sẽ tạo mệnh đề.

*Phủ định* của $P$, kí hiệu $overline(P)$, trái giá trị đúng–sai với $P$. Phủ định “mọi” là “tồn tại ít nhất một”, không phải “mọi … không”.
#note[
$ not (forall x in X, P(x)) quad equiv quad exists x in X, not P(x). $
$ not (exists x in X, P(x)) quad equiv quad forall x in X, not P(x). $
$ not (a > b) equiv a <= b; quad not (a = b) equiv a != b. $
]
Phải giữ nguyên miền $X$ khi phủ định. $forall$ đọc là “với mọi”; $exists$ đọc là “tồn tại”. Một phản ví dụ đủ bác bỏ mệnh đề có “mọi”; một ví dụ đúng đủ chứng minh mệnh đề có “tồn tại”. Ngược lại, kiểm tra vài trường hợp đúng không chứng minh được khẳng định với mọi số thực.

== 2.2. Kéo theo, đảo, tương đương; điều kiện cần và đủ
$P => Q$ đọc là “Nếu $P$ thì $Q$”; chỉ sai khi $P$ đúng mà $Q$ sai. Mệnh đề đảo là $Q => P$, không tự động đúng theo mệnh đề ban đầu.
#table(columns: (auto, auto, auto, auto), inset: 6pt,
[$P$], [$Q$], [$P => Q$], [$P <=> Q$],
[Đ], [Đ], [Đ], [Đ], [Đ], [S], [S], [S], [S], [Đ], [Đ], [S], [S], [S], [Đ], [Đ])

Khi $P => Q$ đúng: $P$ là *điều kiện đủ* để có $Q$; $Q$ là *điều kiện cần* để có $P$. Khi cả hai chiều đều đúng, $P <=> Q$: $P$ là điều kiện cần và đủ của $Q$.

*Ví dụ:* Với số nguyên $n$, “$n$ chia hết cho 4” là điều kiện đủ để “$n$ chẵn”; “$n$ chẵn” là điều kiện cần để “$n$ chia hết cho 4”. Chiều đảo sai vì $n=2$. Còn “$n$ chẵn” $<=>$ “$n^2$ chẵn” là tương đương: bình phương số chẵn là chẵn; bình phương số lẻ là lẻ.

== 2.3. Ví dụ mẫu có giải thích
*Ví dụ M1.* Phủ định $P$: “$forall x in RR, x^2 > 0$”; xét đúng–sai.
#answer[$overline(P)$ là “$exists x in RR, x^2 <= 0$”. $P$ sai vì $x=0$; $overline(P)$ đúng. Dấu $>$ đổi thành $<=$, không đổi thành $<$.]
*Ví dụ M2.* “$exists n in ZZ, n^2=2$” đúng hay sai? Phủ định?
#answer[Mệnh đề sai: số nguyên có trị tuyệt đối không quá 1 có bình phương $<=1$; trị tuyệt đối từ 2 có bình phương $>=4$. Phủ định đúng là “$forall n in ZZ, n^2 != 2$”.]
#newpage()
= 3. Tập hợp và các phép toán
== 3.1. Phần tử, tập con và đếm tập con
- $x in A$: $x$ là phần tử của $A$; $B subset.eq A$: mọi phần tử của $B$ đều thuộc $A$. Không viết $2 subset.eq A$ khi muốn nói số 2 thuộc $A$.
- $A=B$ khi $A subset.eq B$ và $B subset.eq A$. Không đếm lặp phần tử; thứ tự liệt kê không quan trọng.
- $emptyset$ không có phần tử; $emptyset subset.eq A$ với mọi $A$. $\{emptyset\}$ có đúng một phần tử, khác $emptyset$.
- Quy ước trong tài liệu: $NN=\{0;1;2; dots\}$, $NN^*=\{1;2;3; dots\}$; $ZZ subset.eq QQ subset.eq RR$.

Tập có $n$ phần tử có $2^n$ tập con vì mỗi phần tử có hai lựa chọn: chọn hoặc không chọn. Tập con khác rỗng: $2^n-1$; tập con khác chính tập đã cho: $2^n-1$; khác rỗng và khác chính nó: $2^n-2$ (khi $n>=1$).

*Ví dụ T1.* $A=\{x in ZZ | -2 < x <= 2\}=\{-1;0;1;2\}$. Có $2^4=16$ tập con, 15 tập con khác rỗng, 14 tập con khác rỗng và khác $A$.

== 3.2. Khoảng, đoạn, nửa khoảng
#table(columns: (1fr, 1fr), inset: 5pt,
[*Kí hiệu*], [*Điều kiện tương đương*],
[$(a;b)$], [$a<x<b$], [$[a;b]$], [$a<=x<=b$],
[$(a;b]$], [$a<x<=b$], [$[a;b)$], [$a<=x<b$],
[$(-infinity;a)$; $(-infinity;a]$], [$x<a$; $x<=a$],
[$(a;+infinity)$; $[a;+infinity)$], [$x>a$; $x>=a$])
Dấu ngoặc vuông lấy đầu mút, ngoặc tròn không lấy đầu mút. $plus.minus infinity$ không là số thực nên luôn đi với ngoặc tròn. Khi vẽ: chấm đặc biểu thị lấy đầu mút; chấm rỗng biểu thị bỏ đầu mút. Tô đúng phần trục số thỏa điều kiện.

== 3.3. Bốn phép toán cần thành thạo
#note[
$A inter B=\{x | x in A " và " x in B\}$ — phần chung.

$A union B=\{x | x in A " hoặc " x in B\}$ — ít nhất một tập.

$A without B=\{x | x in A " và " x in.not B\}$ — thuộc $A$, bỏ phần thuộc $B$.

Nếu $A subset.eq U$ thì $C_U A=U without A$ — phần bù luôn gắn với tập vũ trụ $U$.
]
*Biểu đồ Ven:* giao là miền chồng lên nhau của hai hình; hợp là toàn bộ hai hình; hiệu $A without B$ chỉ giữ miền bên trong $A$ nhưng bên ngoài $B$; phần bù là miền trong khung $U$ nằm ngoài $A$.
#newpage()
= 4. Tập hợp: phương pháp và ứng dụng
== 4.1. Quy trình xử lí khoảng, đoạn
(1) Vẽ cùng một trục số, ghi các đầu mút từ nhỏ đến lớn. (2) Với giao, lấy phần chung; với hợp, lấy phần được phủ ít nhất một lần. (3) Xét riêng từng đầu mút bằng điều kiện thuộc/không thuộc. (4) Với hiệu, giữ các điểm thuộc tập đứng trước, loại mọi điểm thuộc tập đứng sau.

*Ví dụ T2.* $A=[-2;3)$, $B=(1;5]$. Tìm giao, hợp, hiệu và phần bù của $A$ trong $RR$.
#answer[
$ A inter B=(1;3), quad A union B=[-2;5]. $
$ A without B=[-2;1], quad B without A=[3;5]. $
$ C_RR A=(-infinity;-2) union [3;+infinity). $
Điểm 1 thuộc $A$ nhưng không thuộc $B$ nên được giữ trong $A without B$. Điểm 3 không thuộc $A$ nhưng thuộc $B$ nên thuộc $B without A$ và phần bù của $A$.
]

*Ví dụ T3.* Với $m in RR$, tìm $m$ để $[m;m+2] subset.eq [-1;5]$.
#answer[Đoạn bên trái có độ dài 2 nên luôn không rỗng. Cần và đủ $m>=-1$ và $m+2<=5$. Vậy $-1<=m<=3$. Với bài toán “hai đoạn có giao khác rỗng”, phải kiểm tra thứ tự và việc lấy đầu mút, không dùng nguyên điều kiện tập con.]

== 4.2. Bài toán thực tế hai nhóm
Với hai tập hữu hạn:
$ n(A union B)=n(A)+n(B)-n(A inter B). $
#note[
Chỉ thuộc $A$: $n(A)-n(A inter B)$.

Chỉ thuộc một trong hai: $n(A)+n(B)-2n(A inter B)$.

Không thuộc nhóm nào: $n(U)-n(A union B)$.
]
*Ví dụ T4.* Lớp có 45 học sinh; 25 em thích bóng đá, 20 em thích cầu lông, 8 em thích cả hai. Hỏi số em thích ít nhất một môn, đúng một môn, không thích môn nào trong hai môn đó.
#answer[Ít nhất một môn: $25+20-8=37$. Đúng một môn: $25+20-2 dot 8=29$. Không môn nào: $45-37=8$. Kiểm tra bốn miền rời nhau: chỉ bóng đá 17, cả hai 8, chỉ cầu lông 12, không môn nào 8; tổng bằng 45.]
#warn[*Dễ mất điểm:* Nhầm “ít nhất một” với “đúng một”; nhầm $A without B$ với $B without A$; quên ghi tập vũ trụ khi lấy phần bù; bỏ đầu mút chỉ vì phép toán là hiệu.]
#newpage()
= 5. Bất phương trình bậc nhất hai ẩn
== 5.1. Nhận dạng và kiểm tra nghiệm
Dạng $a x+b y<=c$ (hoặc $<,>,>=$), trong đó $a,b,c$ là số đã biết và $a,b$ không đồng thời bằng 0. Một cặp $(x_0;y_0)$ là nghiệm khi thay vào được bất đẳng thức đúng.

$2x-y<=3$ là bậc nhất hai ẩn; $x^2+y<=3$ và $x y>=1$ không phải. Dù một hệ số bằng 0, $0x+2y<4$ vẫn đúng dạng. Trái lại $0x+0y<=4$ không đúng định nghĩa dạng này.

== 5.2. Cách vẽ miền nghiệm không nhầm phía
#note[
*Bước 1.* Vẽ đường biên $d: a x+b y=c$ qua hai điểm phân biệt.

*Bước 2.* Chọn điểm thử không thuộc $d$, thường là $O(0;0)$.

*Bước 3.* Thay tọa độ điểm thử. Nếu đúng, chọn phía chứa điểm thử; nếu sai, chọn phía đối diện.

*Bước 4.* Dấu $<=$ hoặc $>=$: lấy cả biên (nét liền). Dấu $<$ hoặc $>$: không lấy biên (nét đứt).
]
Nếu $d$ qua $O$, dùng điểm thử khác như $(1;0)$ hoặc $(0;1)$ nhưng phải kiểm tra điểm đó không nằm trên $d$. Viết rõ miền tô là miền nghiệm hay miền loại để người đọc không hiểu ngược.

*Ví dụ B1.* Biểu diễn miền nghiệm $2x+y<=4$.
#answer[Biên $2x+y=4$ qua $A(2;0)$, $B(0;4)$. Điểm $O$ không thuộc biên và $0<=4$ đúng. Miền nghiệm là nửa mặt phẳng chứa $O$, kể cả đường thẳng $A B$. Nếu đổi thành $2x+y<4$, miền cùng phía nhưng bỏ biên.]

*Ví dụ B2.* Miền nghiệm $x-y>0$ nằm phía nào?
#answer[Biên $y=x$ đi qua $O$, không dùng $O$ để thử. Chọn $M(1;0)$: $1-0>0$ đúng. Miền nghiệm là $y<x$, phía dưới đường $y=x$, không kể đường biên.]

== 5.3. Từ lời văn sang bất phương trình
#table(columns: (1fr, 1fr), inset: 5pt,
[*Cụm từ*], [*Cách viết*],
[Không quá / tối đa 40], [$<=40$],
[Ít nhất / không dưới 10], [$>=10$],
[Hơn 5 / dưới 8], [$>5$ / $<8$])
*Ví dụ B3.* Mỗi vé thường giá 30 nghìn đồng, vé ưu đãi 20 nghìn đồng. Gọi $x,y$ là số vé từng loại. Ngân sách không quá 600 nghìn đồng cho điều kiện $30x+20y<=600$, hay $3x+2y<=60$, với $x,y in NN$. Không đổi dấu chỉ vì chia hai vế cho số dương 10.
#newpage()
= 6. Hệ bất phương trình và tối ưu
== 6.1. Miền nghiệm của hệ là giao các miền
Một cặp số phải thỏa *tất cả* bất phương trình. Vẽ từng đường biên, chọn từng nửa mặt phẳng, lấy phần chung. Có hệ vô nghiệm; có hệ có miền nghiệm không bị chặn. Không mặc định mọi hệ đều cho một tam giác.

*Ví dụ H1.* Xét $x>=0$, $y>=0$, $x+y<=6$, $2x+y<=8$.
#answer[Trong góc phần tư thứ nhất, phần chung có các đỉnh $O(0;0)$, $A(4;0)$, $B(2;4)$, $C(0;6)$. Giao $x+y=6$ với $2x+y=8$ cho $B(2;4)$. Giao $(0;8)$ của đường thứ hai với trục tung bị loại vì không thỏa $x+y<=6$. Chỉ giữ giao điểm thỏa toàn hệ.]

== 6.2. Bài toán phương án tối ưu: 5 bước
1. Chọn ẩn, đơn vị và miền giá trị (số lượng sản phẩm thường nguyên không âm).
2. Từ mỗi nguồn lực, lập một bất phương trình. Ghi rõ đại lượng cần tối ưu $F=p x+q y$.
3. Vẽ miền nghiệm; xác định các đỉnh và kiểm tra điều kiện toàn hệ.
4. Nếu miền là đa giác lồi đóng, bị chặn, giá trị lớn nhất/nhỏ nhất của hàm tuyến tính đạt tại ít nhất một đỉnh. Tính $F$ ở tất cả các đỉnh.
5. Kết luận bằng lời, kiểm tra đơn vị, tính nguyên, lượng nguồn lực đã dùng.

Nếu các đỉnh tối ưu không nguyên trong bài toán đòi hỏi nguyên, chưa thể kết luận ngay phương án nguyên tốt nhất chỉ bằng cách làm tròn. Cần xét thêm các điểm nguyên khả thi thích hợp. Với miền không bị chặn, không áp dụng máy móc việc so sánh một danh sách đỉnh để khẳng định tồn tại cực trị.

*Ví dụ H2.* Một xưởng làm $x$ sản phẩm loại I và $y$ loại II. Tổng số không quá 6; máy cho $2x+y<=8$ giờ. Lãi lần lượt 3 và 2 trăm nghìn đồng. Tìm lãi lớn nhất, biết $x,y in NN$.
#answer[
Miền là tứ giác H1. Lãi $F=3x+2y$ (trăm nghìn đồng).
#table(columns: (1fr, auto, auto, auto, auto), inset: 5pt,
[Đỉnh], [$(0;0)$], [$(4;0)$], [$(2;4)$], [$(0;6)$],
[$F$], [0], [12], [14], [12])
Cực đại trên miền liên tục là 14 tại $(2;4)$. Điểm này nguyên nên cũng tối ưu cho bài toán sản phẩm. Làm 2 sản phẩm loại I và 4 loại II, lãi 1,4 triệu đồng; dùng đủ $2+4=6$ suất và $2 dot 2+4=8$ giờ.
]
#warn[*Kiểm tra bắt buộc:* Không quên $x,y>=0$; không nhầm hàm lợi nhuận với điều kiện tài nguyên; không nhận một giao điểm nằm ngoài miền nghiệm; ghi đơn vị tiền tệ nhất quán.]
#newpage()
= 7. Giá trị lượng giác từ 0° đến 180°
== 7.1. Định nghĩa và điều kiện xác định
Trên nửa đường tròn đơn vị phía trên trục hoành, điểm $M(x;y)$ ứng với góc $alpha in [0 degree;180 degree]$ tính từ tia $O x$. Khi đó:
$cos alpha=x, quad sin alpha=y, quad tan alpha=y/x\ (x != 0), quad cot alpha=x/y\ (y != 0).$

$sin alpha>=0$ trên cả đoạn; $cos alpha>0$ khi $alpha<90 degree$, bằng 0 tại $90 degree$, âm khi $alpha>90 degree$. $tan$ không xác định tại $90 degree$; $cot$ không xác định tại $0 degree$ và $180 degree$.

== 7.2. Bảng góc đặc biệt
#table(columns: (auto, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr), inset: 5pt,
[$alpha$], [$0 degree$], [$30 degree$], [$45 degree$], [$60 degree$], [$90 degree$], [$180 degree$],
[$sin alpha$], [0], [$1/2$], [$sqrt(2)/2$], [$sqrt(3)/2$], [1], [0],
[$cos alpha$], [1], [$sqrt(3)/2$], [$sqrt(2)/2$], [$1/2$], [0], [$-1$],
[$tan alpha$], [0], [$sqrt(3)/3$], [1], [$sqrt(3)$], [KXĐ], [0],
[$cot alpha$], [KXĐ], [$sqrt(3)$], [1], [$sqrt(3)/3$], [0], [KXĐ])

== 7.3. Công thức tối thiểu phải nhớ
#note[
$sin^2 alpha+cos^2 alpha=1.$
$tan alpha=(sin alpha)/(cos alpha), quad cot alpha=(cos alpha)/(sin alpha).$
$1+tan^2 alpha=1/(cos^2 alpha), quad 1+cot^2 alpha=1/(sin^2 alpha).$
Hai góc bù:
$sin(180 degree-alpha)=sin alpha, quad cos(180 degree-alpha)=-cos alpha.$
$tan(180 degree-alpha)=-tan alpha, quad cot(180 degree-alpha)=-cot alpha.$
Hai góc phụ (trong miền phù hợp):
$sin(90 degree-alpha)=cos alpha, quad cos(90 degree-alpha)=sin alpha.$
]
Các công thức thương chỉ dùng khi mẫu khác 0. Hệ thức $tan alpha dot cot alpha=1$ đòi hỏi cả hai cùng xác định.

*Ví dụ L1.* $90 degree<alpha<180 degree$, $sin alpha=3/5$. Tính $cos alpha$, $tan alpha$, $T=(2sin alpha-cos alpha)/(sin alpha+cos alpha)$.
#answer[$cos alpha=-sqrt(1-9/25)=-4/5$ vì góc tù. $tan alpha=-3/4$. $T=(6/5+4/5)/(3/5-4/5)=-10$. Mẫu $-1/5 !=0$, nên biểu thức xác định.]
#warn[*Máy tính:* Đặt chế độ DEG trước khi tính góc theo độ. Dùng phím nghịch đảo để tìm góc (ví dụ $cos^(-1)$), không nhầm với $1/cos$. Giữ số chưa làm tròn trong phép tính trung gian.]
#newpage()
= 8. Hệ thức lượng trong tam giác
Trong tam giác không suy biến $A B C$: $a=B C$, $b=C A$, $c=A B$; cạnh $a$ đối góc $A$, tương tự cho $b,B$ và $c,C$. $p=(a+b+c)/2$ là nửa chu vi; $R,r$ lần lượt là bán kính ngoại tiếp, nội tiếp; $S$ là diện tích.
== 8.1. Bảng công thức và khi nào dùng
#table(columns: (1.6fr, 1fr), inset: 7pt, stroke: 0.4pt + luma(80%),
[*Công thức*], [*Tình huống thuận lợi*],
[$a^2=b^2+c^2-2b c cos A$], [Biết hai cạnh và góc xen giữa.],
[$cos A=(b^2+c^2-a^2)/(2b c)$], [Biết ba cạnh, cần góc.],
[$a/(sin A)=b/(sin B)=c/(sin C)=2R$], [Có cặp cạnh–góc đối diện.],
[$S=1/2 b c sin A=1/2 c a sin B=1/2 a b sin C$], [Hai cạnh và góc xen giữa.],
[$S=sqrt(p(p-a)(p-b)(p-c))$], [Biết ba cạnh (Heron).],
[$S=p r=(a b c)/(4R)$], [Tính bán kính hoặc diện tích.],
[$S=1/2 a h_a$], [Liên hệ đường cao $h_a$.])
Đổi vòng $a,b,c$ và $A,B,C$ được các công thức còn lại. Các công thức được đối chiếu tại #link("https://vietjack.com/toan-10-kn/ly-thuyet-bai-6-he-thuc-luong-trong-tam-giac.jsp")[\[4\]]; kí hiệu căn, phân số trong tài liệu này đã được viết lại đầy đủ.

== 8.2. Chọn đường giải tam giác
- Biết hai góc và một cạnh: tìm góc còn lại bằng $180 degree-A-B$, dùng định lí sin.
- Biết hai cạnh và góc xen giữa: côsin tìm cạnh thứ ba; dùng côsin hoặc sin tìm góc, nhớ kiểm tra góc tù.
- Biết ba cạnh: kiểm tra bất đẳng thức tam giác; dùng côsin tìm góc và Heron tính diện tích.
- Biết hai cạnh và góc không xen giữa: có thể có 0, 1 hoặc 2 tam giác. $sin B=k$ có thể cho $B=beta$ hoặc $180 degree-beta$; giữ các khả năng thỏa $A+B<180 degree$.

*Ví dụ G1.* $b=5$, $c=8$, $A=60 degree$. Tính $a,S,R$.
#answer[
$a^2=25+64-2 dot 5 dot 8 dot 1/2=49$, nên $a=7$.

$S=1/2 dot 5 dot 8 dot (sqrt(3)/2)=10sqrt(3)$.

$R=a/(2sin A)=7/sqrt(3)=7sqrt(3)/3$.
]

*Ví dụ G2.* Ba cạnh bằng 13, 14, 15. $p=21$; $S=sqrt(21 dot 8 dot 7 dot 6)=84$; $r=S/p=4$; $R=(13 dot 14 dot 15)/(4 dot 84)=65/8$.
#newpage()
= 9. Từ tam giác đến bài toán đo đạc
== 9.1. Khoảng cách qua vật cản
*Ví dụ G3.* Hai điểm $A,B$ trên bờ cách nhau 80 m. Nhìn đỉnh tháp $C$ trên bờ đối diện, đo được $angle C A B=45 degree$, $angle C B A=60 degree$. Tính khoảng cách $A C$ (làm tròn 0,1 m).
#answer[
Vẽ tam giác $A B C$ với đáy $A B=80$, góc ở $A$ là $45 degree$, góc ở $B$ là $60 degree$. Góc $C=75 degree$.

Theo định lí sin: $(A C)/(sin 60 degree)=80/(sin 75 degree)$.

$A C=(80sin 60 degree)/(sin 75 degree) approx 71.7$ m. Đây là khoảng cách xiên $A C$ trong mô hình mặt phẳng, không phải khoảng cách vuông góc từ $C$ đến đường bờ $A B$.
]

== 9.2. Chiều cao với một góc nâng
*Ví dụ G4.* Đứng cách chân tháp 40 m trên mặt đất ngang, máy đặt cao 1,5 m so với mặt đất, góc nâng tới đỉnh là $35 degree$. Tính chiều cao tháp, làm tròn 0,1 m.
#answer[Phần chiều cao từ ngang máy đến đỉnh tháp là $40tan 35 degree$. Tổng chiều cao $h=40tan 35 degree+1.5 approx 29.5$ m. Nếu quên cộng 1,5 m sẽ trả lời sai dù công thức lượng giác đúng.]

== 9.3. Một tình huống cần kiểm tra hai nghiệm góc
*Ví dụ G5.* Biết $A=30 degree$, $a=5$, $b=8$. Có bao nhiêu tam giác?
#answer[
$sin B=(b sin A)/a=0.8$. Có $B_1 approx 53.13 degree$ hoặc $B_2 approx 126.87 degree$. Cả hai đều có $A+B<180 degree$ nên đều hợp lệ. Khi đó $C_1 approx 96.87 degree$, $C_2 approx 23.13 degree$. Có hai tam giác, không được chỉ lấy kết quả mặc định của phím $sin^(-1)$.
]

== 9.4. Checklist trình bày bài thực tế
1. Vẽ hình sơ đồ, ghi tên điểm và dữ kiện, nêu giả thiết mặt đất ngang hoặc cùng mặt phẳng nếu đề cho.
2. Chỉ rõ góc và cạnh đối diện trước khi thế vào định lí sin.
3. Nếu dùng côsin, phải đúng góc xen giữa hai cạnh được nhân.
4. Ghi công thức, thay số, giữ đủ chữ số trung gian rồi làm tròn theo đề.
5. Kết luận đúng đại lượng được hỏi, có đơn vị; chiều dài dương, góc tam giác có tổng $180 degree$.
#warn[*Lỗi phổ biến:* Dùng $a=2R$ thay vì $a=2R sin A$; dùng cả chu vi trong $S=p r$; bỏ căn trong Heron; nhầm diện tích với chiều dài; coi khoảng cách xiên là chiều cao.]
#newpage()
= 10. Vectơ: chỉ học đúng phạm vi
== 10.1. Các khái niệm mở đầu
Vectơ là đoạn thẳng có hướng. $arrow(A B)$ có điểm đầu $A$, điểm cuối $B$. Nếu $A != B$, giá là đường thẳng $A B$; độ dài $|arrow(A B)|=A B>=0$.

Với hai vectơ khác vectơ-không:
- *Cùng phương* khi giá song song hoặc trùng nhau.
- Nếu cùng phương thì chúng có thể cùng hướng hoặc ngược hướng.
- *Bằng nhau* khi cùng hướng và cùng độ dài. Chỉ độ dài bằng nhau chưa đủ.
- *Đối nhau* khi cùng độ dài và ngược hướng; $arrow(B A)$ đối với $arrow(A B)$. Không cần học quy tắc cộng để nhận diện cặp đối nhau trong phạm vi ma trận.

Vectơ có điểm đầu trùng điểm cuối là vectơ-không; $arrow(A A)=arrow(B B)=arrow(0)$, độ dài 0. Theo quy ước SGK, vectơ-không cùng hướng và cùng phương với mọi vectơ. Không gán cho nó một giá duy nhất. Quy ước này được đối chiếu tại #link("https://vietjack.com/toan-10-kn/ly-thuyet-bai-7-cac-khai-niem-mo-dau.jsp")[\[5\]].

== 10.2. Các nhận xét nên thuộc
- Với $A,B,C$ phân biệt, $arrow(A B)$ và $arrow(A C)$ cùng phương khi và chỉ khi $A,B,C$ thẳng hàng.
- Nếu $arrow(A B)=arrow(A C)$ thì $B=C$ (cùng điểm đầu thì cùng điểm cuối).
- Cho điểm $O$ và vectơ $arrow(a)$, có duy nhất điểm $M$ sao cho $arrow(O M)=arrow(a)$.
- Quan hệ cùng phương không được suy luận bắc cầu qua vectơ-không. Hai vectơ không cùng phương vẫn đều cùng phương với $arrow(0)$.

== 10.3. Ví dụ mẫu
*Ví dụ V1.* Hình bình hành $A B C D$ có các đỉnh theo thứ tự. Chỉ ra cặp bằng nhau và cặp đối nhau.
#answer[$arrow(A B)=arrow(D C)$ vì $A B$ và $D C$ song song, cùng hướng và bằng độ dài. $arrow(A D)=arrow(B C)$. Hai vectơ $arrow(A B)$ và $arrow(C D)$ đối nhau, không bằng nhau. Nếu $O$ là giao hai đường chéo thì $arrow(A O)=arrow(O C)$ do $O$ là trung điểm $A C$.]

*Ví dụ V2.* $M$ là trung điểm $A B$, $A != B$.
#answer[$arrow(A M)$ và $arrow(M B)$ cùng hướng, cùng độ dài nên bằng nhau. $arrow(M A)$ và $arrow(M B)$ ngược hướng và cùng độ dài nên đối nhau. $arrow(A B)$ và $arrow(A M)$ cùng hướng nhưng không bằng nhau vì $A B=2A M$.]
#warn[Không đưa tổng, hiệu, nhân vectơ với số, tọa độ hoặc tích vô hướng vào phần thi thử: các nội dung đó chưa được yêu cầu trong tệp nguồn.]
#newpage()
#heading(level: 1, outlined: false)[Hình minh họa · Tập hợp và vectơ]
== Đọc bốn miền trong biểu đồ Ven (ví dụ T4)
#align(center, image("hinh/ven.svg", width: 100%, height: 47mm, fit: "contain"))
Hai vòng tròn là hai nhóm học sinh. Số 8 ở miền chồng là số thích *cả hai* môn; số 8 ở ngoài cả hai vòng là số *không thích môn nào*. Hai số bằng nhau trong ví dụ này nhưng ý nghĩa hoàn toàn khác. Hợp gồm ba miền $17+8+12=37$; đúng một môn gồm hai miền $17+12=29$.

== Nhìn đầu mút trên trục số (ví dụ T2)
#align(center, image("hinh/truc-so.svg", width: 100%, height: 47mm, fit: "contain"))
Đường đậm là phần được lấy. Chấm rỗng: bỏ đầu mút; chấm đặc: lấy đầu mút. Phần chung của $A=[-2;3)$ và $B=(1;5]$ chỉ là $(1;3)$; 1 bị loại do không thuộc $B$, 3 bị loại do không thuộc $A$.

== Kiểm tra chiều mũi tên trong hình bình hành
#align(center, image("hinh/vecto.svg", width: 100%, height: 47mm, fit: "contain"))
Các đỉnh theo thứ tự $A,B,C,D$. Cạnh dưới đi từ $A$ đến $B$ có hướng như cạnh trên đi từ $D$ đến $C$, nên $arrow(A B)=arrow(D C)$. Nếu đổi vectơ thứ hai thành $arrow(C D)$ thì hướng bị đảo; hai vectơ khi ấy đối nhau.
#newpage()
#heading(level: 1, outlined: false)[Hình minh họa · Miền nghiệm và đo đạc]
== Miền nghiệm là phần chung, không phải hợp (H1)
#align(center, image("hinh/mien-nghiem.svg", width: 100%, height: 79mm, fit: "contain"))
Phần tô là tứ giác $O A B C$. Các giao điểm như $(6;0)$ hoặc $(0;8)$ nằm trên một đường biên nhưng vi phạm điều kiện còn lại, nên không phải đỉnh miền nghiệm. Để kiểm tra mỗi đỉnh, thay tọa độ vào *toàn bộ* hệ. Hình vẽ cho miền liên tục; khi đếm sản phẩm, chỉ các điểm nguyên mới là phương án hợp lệ.

== Gắn đúng cạnh với góc đối diện (câu IV.2)
#align(center, image("hinh/tam-giac.svg", width: 100%, height: 60mm, fit: "contain"))
Theo hình, $A C$ đối diện góc $B=75 degree$, còn $A B$ đối diện góc $C=60 degree$. Vì thế phải lập:
$ (A C)/(sin 75 degree)=(A B)/(sin 60 degree). $
Không dùng góc $45 degree$ cho cạnh $A C$. Hình là sơ đồ phục vụ lập luận, không dùng thước đo trên hình để suy ra đáp số.

#note[*Cách tự kiểm tra hình vẽ:* Ghi đầy đủ tên điểm, đánh dấu góc, phân biệt nét biên và phía lấy. Nếu hình và điều kiện đại số mâu thuẫn, hãy kiểm tra lại điểm thử hoặc dữ kiện trước khi tiếp tục tính.]
#newpage()
= 11. Bài luyện theo từng dạng
*28 bài tự biên soạn.* Làm độc lập trước khi xem lời giải ở phần 12. NB: nhận biết; TH: thông hiểu; VD: vận dụng; VDC: vận dụng cao. Mức độ là định hướng học tập, không phải xác nhận từ nhà trường.
== Nhóm A · Mệnh đề (B01–B04)
*B01 · NB.* Trong các câu: (a) “17 là số nguyên tố”; (b) “Hãy mở sách”; (c) “$x^2=9$”; (d) “Có số nguyên có bình phương bằng 9”, câu nào là mệnh đề? Xét đúng–sai khi là mệnh đề.

*B02 · TH.* Viết phủ định và xét đúng–sai của:
(a) $forall x in RR, x^2+1>0$; (b) $exists n in NN, n+1=0$.

*B03 · TH.* Với $n in ZZ$, cho $P$: “$n$ chia hết cho 6”, $Q$: “$n$ chia hết cho 3”. Xét $P=>Q$, mệnh đề đảo và nêu điều kiện cần, điều kiện đủ.

*B04 · VD.* Xét mệnh đề “$forall x in RR, x^2>=x$”. Nếu sai, đưa phản ví dụ; giải thích vì sao thử $x=0,1,2$ chưa đủ kết luận.

== Nhóm B · Tập hợp và khoảng (B05–B08)
*B05 · NB.* Liệt kê $A=\{x in ZZ | -3<=x<2\}$. Tập $A$ có bao nhiêu tập con? Bao nhiêu tập con khác rỗng và khác $A$?

*B06 · TH.* Cho $A=(-infinity;2]$, $B=(-1;5)$. Tính $A inter B$, $A union B$, $A without B$, $B without A$ và $C_RR B$.

*B07 · TH.* $U=\{1;2;3;4;5;6\}$, $A=\{1;2;4\}$, $B=\{2;3;4\}$. Tìm $A inter B$, $A union B$, $C_U A$. Phân biệt $emptyset$ và $\{emptyset\}$ về số phần tử.

*B08 · VD.* Cho $A=[m;m+3]$ và $B=[1;5]$. Tìm $m$ để: (a) $A subset.eq B$; (b) $A inter B !=emptyset$.

== Nhóm C · Tập hợp trong thực tế (B09–B12)
*B09 · TH.* Trong 40 học sinh, 22 em học tiếng Anh, 18 em học tiếng Nhật, 7 em học cả hai. Có bao nhiêu em học ít nhất một trong hai thứ tiếng? Không học thứ tiếng nào trong hai thứ tiếng đó?

*B10 · VD.* Có 50 người; 30 người thích trà, 28 người thích cà phê và mỗi người thích ít nhất một loại. Tính số người thích cả hai và số người chỉ thích trà.

*B11 · VD.* Trong 36 học sinh, 20 em chơi bóng đá, 17 em chơi bóng chuyền, 5 em không chơi môn nào trong hai môn đó. Có bao nhiêu em chỉ chơi đúng một môn?

*B12 · VD.* Một nhóm có 24 người thích bơi, 19 người thích chạy. Biết 31 người thích đúng một trong hai hoạt động. Có bao nhiêu người thích cả hai? Bao nhiêu người thích ít nhất một?
#newpage()
#heading(level: 1, outlined: false)[11. Bài luyện theo từng dạng (tiếp)]
== Nhóm D · Bất phương trình và hệ (B13–B16)
*B13 · NB.* Chọn các bất phương trình bậc nhất hai ẩn: (a) $3x-2y>1$; (b) $x y<=2$; (c) $0x+4y>=8$; (d) $x^2+y<5$. Kiểm tra $(1;-1)$ có thỏa (a) không.

*B14 · TH.* Mô tả miền nghiệm của $x+2y>4$: đường biên, điểm thử, phía được lấy và có lấy biên không.

*B15 · TH.* Tìm các đỉnh miền nghiệm $x>=0$, $y>=0$, $x+y<=5$, $x<=3$. Tìm giá trị lớn nhất của $F=2x+y$ trên miền đó.

*B16 · VDC.* Một tổ làm sản phẩm I và II. Mỗi sản phẩm I dùng 2 giờ máy, 1 giờ công; mỗi sản phẩm II dùng 1 giờ máy, 2 giờ công. Có tối đa 8 giờ máy, 10 giờ công. Lãi tương ứng 300 và 400 nghìn đồng/sản phẩm. Lập hệ và tìm phương án có lãi cao nhất, biết số sản phẩm là số nguyên không âm.

== Nhóm E · Giá trị lượng giác (B17–B20)
*B17 · NB.* Tính $sin 150 degree$, $cos 120 degree$, $tan 135 degree$, $cot 90 degree$. Chỉ ra trong bốn giá trị đó giá trị nào bằng 0.

*B18 · TH.* Góc $alpha$ tù, $cos alpha=-5/13$. Tính $sin alpha$, $tan alpha$.

*B19 · VD.* $90 degree<alpha<180 degree$, $sin alpha=4/5$. Tính $T=(sin alpha+2cos alpha)/(2sin alpha-cos alpha)$.

*B20 · VD.* $0 degree<alpha<90 degree$, $tan alpha=2$. Tính $P=(3sin alpha-cos alpha)/(sin alpha+cos alpha)$ mà không cần tính riêng $sin alpha$ và $cos alpha$.

== Nhóm F · Tam giác (B21–B24)
*B21 · TH.* Tam giác có $b=6$, $c=8$, góc xen giữa $A=60 degree$. Tính $a$ và $S$.

*B22 · TH.* Tam giác có $a=10$, $A=30 degree$, $B=45 degree$. Tính $C$, $b$, bán kính ngoại tiếp $R$.

*B23 · TH.* Tam giác có ba cạnh 5, 5, 6. Tính $S$, $r$, $R$.

*B24 · VD.* Hai vị trí quan sát $A,B$ cách nhau 100 m, tạo với mục tiêu $C$ tam giác có $A=45 degree$, $B=75 degree$. Tính $A C$ và khoảng cách vuông góc từ $C$ đến đường thẳng $A B$, làm tròn 0,1 m.

== Nhóm G · Vectơ (B25–B28)
*B25 · NB.* Ba điểm $A,B,C$ thẳng hàng theo thứ tự đó, $A B=B C=2$ cm. So sánh hướng, độ dài của $arrow(A B)$, $arrow(B C)$, $arrow(C B)$, $arrow(A C)$.

*B26 · TH.* Trong hình bình hành $A B C D$ không suy biến, giao hai đường chéo là $O$. Tìm các vectơ bằng $arrow(A B)$, $arrow(A O)$ có điểm đầu và cuối thuộc $\{A;B;C;D;O\}$.

*B27 · TH.* Xét: (a) Hai vectơ cùng độ dài thì bằng nhau; (b) Hai vectơ bằng nhau thì cùng phương; (c) Vectơ-không cùng hướng với mọi vectơ; (d) Hai vectơ cùng phương với một vectơ thứ ba thì cùng phương với nhau. Có cần điều kiện gì cho (d)?

*B28 · TH.* Tam giác $A B C$ không suy biến. Có bao nhiêu vectơ khác vectơ-không có điểm đầu và cuối là các đỉnh tam giác? Bao nhiêu vectơ-không phân biệt về giá trị?
#newpage()
= 12. Lời giải bài luyện
== B01–B08 · Logic và tập hợp
*B01.* (a) là mệnh đề đúng vì 17 chỉ có hai ước dương là 1 và 17. (b) là mệnh lệnh, không là mệnh đề. (c) là mệnh đề chứa biến, chưa là mệnh đề có giá trị xác định khi chưa cho $x$. (d) là mệnh đề đúng, lấy số nguyên 3 hoặc $-3$.

*B02.* (a) Phủ định: $exists x in RR, x^2+1<=0$. Vì $x^2>=0$ nên $x^2+1>=1$, mệnh đề ban đầu đúng, phủ định sai. (b) Phủ định: $forall n in NN, n+1 !=0$. Do $n>=0$ nên $n+1>=1$, mệnh đề ban đầu sai, phủ định đúng.

*B03.* $P=>Q$ đúng: $n=6k$ thì $n=3(2k)$. Đảo $Q=>P$ sai, lấy $n=3$. Chia hết cho 6 là điều kiện đủ để chia hết cho 3; chia hết cho 3 là điều kiện cần để chia hết cho 6.

*B04.* Sai, chẳng hạn $x=1/2$ cho $1/4<1/2$. Ba giá trị $0,1,2$ chỉ kiểm tra ba trường hợp, còn lượng từ $forall$ đòi hỏi mọi số thực. Muốn chứng minh đúng phải có lập luận bao quát toàn miền.

*B05.* $A=\{-3;-2;-1;0;1\}$ có 5 phần tử, $2^5=32$ tập con. Khác rỗng và khác $A$: $32-2=30$.

*B06.*
$ A inter B=(-1;2], quad A union B=(-infinity;5). $
$ A without B=(-infinity;-1], quad B without A=(2;5). $
$ C_RR B=(-infinity;-1] union [5;+infinity). $
Hai đầu $-1,5$ không thuộc $B$ nên thuộc phần bù. Điểm 2 thuộc $A$ và $B$, không thuộc hai hiệu.

*B07.* $A inter B=\{2;4\}$; $A union B=\{1;2;3;4\}$; $C_U A=\{3;5;6\}$. Tập rỗng có 0 phần tử; tập chỉ chứa tập rỗng có 1 phần tử.

*B08.* (a) $m>=1$ và $m+3<=5$, suy ra $m in [1;2]$. (b) Hai đoạn giao khác rỗng khi $m<=5$ và $m+3>=1$, suy ra $m in [-2;5]$. Hai giá trị biên đều được lấy vì các đoạn đóng: $m=-2$ giao tại 1; $m=5$ giao tại 5.

== B09–B12 · Phân chia nhóm
*B09.* Ít nhất một: $22+18-7=33$. Không học cả hai thứ tiếng đang xét: $40-33=7$.

*B10.* Số thích cả hai: $30+28-50=8$. Chỉ thích trà: $30-8=22$. Chỉ thích cà phê: $28-8=20$; tổng $22+8+20=50$ kiểm tra đúng.

*B11.* Ít nhất một môn: $36-5=31$. Cả hai: $20+17-31=6$. Đúng một môn: $31-6=25$ (hoặc $20+17-2 dot 6=25$).

*B12.* Gọi $t$ là số người thích cả hai. $24+19-2t=31$, nên $t=6$. Số thích ít nhất một: $24+19-6=37$. Không cần biết tổng số người của nhóm để trả lời hai đại lượng này.
#newpage()
#heading(level: 1, outlined: false)[12. Lời giải bài luyện (tiếp)]
== B13–B16 · Nửa mặt phẳng và tối ưu
*B13.* (a), (c) đúng dạng; (b) chứa tích $x y$, (d) chứa $x^2$, không đúng dạng. Với $(1;-1)$, $3 dot 1-2 dot (-1)=5>1$ nên là nghiệm của (a).

*B14.* Biên $x+2y=4$ qua $(4;0)$ và $(0;2)$. Thử $O(0;0)$ không thuộc biên, $0>4$ sai. Lấy nửa mặt phẳng không chứa $O$, tức $y>2-x/2$; bỏ đường biên.

*B15.* Các đỉnh $(0;0)$, $(3;0)$, $(3;2)$, $(0;5)$. $F$ lần lượt bằng 0, 6, 8, 5. Do miền đóng và bị chặn, giá trị lớn nhất là 8 tại $(3;2)$.

*B16.* Chọn $x,y in NN$ là số sản phẩm I, II. Hệ:
$ x>=0, quad y>=0, quad 2x+y<=8, quad x+2y<=10. $
Lãi $F=300x+400y$ (nghìn đồng). Giao hai đường tài nguyên: $2x+y=8$, $x+2y=10$ cho $(x;y)=(2;4)$. Miền liên tục có các đỉnh $(0;0)$, $(4;0)$, $(2;4)$, $(0;5)$. Lãi tương ứng 0, 1200, 2200, 2000 nghìn đồng. Tối đa 2200 nghìn đồng tại $(2;4)$; đây là điểm nguyên nên đáp ứng bài toán sản phẩm. Phương án dùng $2 dot 2+4=8$ giờ máy và $2+2 dot 4=10$ giờ công.

== B17–B20 · Lượng giác
*B17.* $sin 150 degree=sin 30 degree=1/2$; $cos 120 degree=-cos 60 degree=-1/2$; $tan 135 degree=-tan 45 degree=-1$; $cot 90 degree=0$. Chỉ giá trị cuối bằng 0.

*B18.* Góc tù có $sin alpha>0$, do đó $sin alpha=sqrt(1-25/169)=12/13$. $tan alpha=(12/13)/(-5/13)=-12/5$.

*B19.* $cos alpha=-3/5$. Tử số $4/5-6/5=-2/5$; mẫu $8/5+3/5=11/5 !=0$. Vậy $T=-2/11$.

*B20.* Góc nhọn nên $cos alpha>0$. Chia cả tử và mẫu cho $cos alpha$:
$ P=(3tan alpha-1)/(tan alpha+1)=(6-1)/(2+1)=5/3. $
Mẫu dương, phép chia hợp lệ. Không cần suy ra sin và côsin riêng lẻ.

== B21–B24 · Tam giác
*B21.* $a^2=6^2+8^2-2 dot 6 dot 8 cos 60 degree=52$, nên $a=2sqrt(13)$. $S=1/2 dot 6 dot 8 sin 60 degree=12sqrt(3)$.

*B22.* $C=105 degree$. $b=(a sin B)/(sin A)=10sqrt(2)$; $R=a/(2sin A)=10$. Đơn vị độ dài giống đơn vị của cạnh $a$.
#newpage()
#heading(level: 1, outlined: false)[12. Lời giải bài luyện (kết)]
*B23.* $p=(5+5+6)/2=8$. $S=sqrt(8 dot 3 dot 3 dot 2)=12$. $r=S/p=3/2$; $R=(5 dot 5 dot 6)/(4 dot 12)=25/8$. Cũng có thể hạ đường cao ứng với cạnh 6: chiều cao $sqrt(25-9)=4$ nên $S=6 dot 4/2=12$.

*B24.* $C=60 degree$. Theo định lí sin:
$ A C=(100sin 75 degree)/(sin 60 degree) approx 111.5 " m". $
Hạ $C H$ vuông góc $A B$. Do góc $A=45 degree$ và cả $A,B$ đều nhọn, $H$ nằm trên đoạn $A B$. $C H=A C sin 45 degree approx 78.9$ m. Phải tính từ biểu thức $A C$ chưa làm tròn để tránh sai số tích lũy. Khoảng cách vuông góc khác độ dài $A C$.

== B25–B28 · Đọc đúng hướng vectơ
*B25.* $arrow(A B)$, $arrow(B C)$, $arrow(A C)$ cùng hướng; $arrow(C B)$ ngược hướng với chúng. Độ dài ba vectơ đầu tiên trong danh sách đề bài là 2 cm, 2 cm, 2 cm; vectơ cuối $arrow(A C)$ dài 4 cm. Do vậy $arrow(A B)=arrow(B C)$; $arrow(C B)$ đối với cả hai; $arrow(A C)$ không bằng $arrow(A B)$.

*B26.* Các vectơ bằng $arrow(A B)$ là $arrow(A B)$ và $arrow(D C)$. Các vectơ bằng $arrow(A O)$ là $arrow(A O)$ và $arrow(O C)$. Vì hình bình hành không suy biến, hai đường chéo cắt nhau nhưng không cùng phương; các đoạn theo cạnh không thể cùng phương với đường chéo $A C$. Vậy không có thêm cặp nào trong tập điểm đã cho.

*B27.* (a) Sai: $arrow(A B)$ và $arrow(B A)$ với $A !=B$ cùng độ dài nhưng ngược hướng. (b) Đúng theo định nghĩa. (c) Đúng theo quy ước. (d) Sai nếu không thêm điều kiện: chọn hai vectơ không cùng phương, chúng vẫn cùng phương với vectơ thứ ba là $arrow(0)$. Nếu vectơ thứ ba khác $arrow(0)$ thì (d) đúng.

*B28.* Có $3 dot 2=6$ vectơ khác vectơ-không: $arrow(A B)$, $arrow(A C)$, $arrow(B A)$, $arrow(B C)$, $arrow(C A)$, $arrow(C B)$. Vì tam giác không suy biến nên các vectơ này khác nhau. Có 3 cách ghi vectơ-không ($arrow(A A)$, $arrow(B B)$, $arrow(C C)$) nhưng chúng bằng nhau, chỉ có *1 giá trị vectơ-không phân biệt*.

== Nhật kí tự sửa lỗi
#table(columns: (auto, 1fr, 1fr, 1fr), inset: 7pt,
[*Bài*], [*Em đã sai vì…*], [*Cách sửa*], [*Bài cần làm lại*],
[……], [……………………], [……………………], [……………………],
[……], [……………………], [……………………], [……………………],
[……], [……………………], [……………………], [……………………])
Hãy phân loại lỗi thành: chưa thuộc định nghĩa, sai dấu/đầu mút, chọn sai công thức, lập sai mô hình, sai tính toán hoặc thiếu kết luận. Chỉ đọc đáp án mà không xác định nguyên nhân sẽ khó cải thiện điểm số.
#newpage()
= 13. Đề minh họa 90 phút
#note[*TỰ BIÊN SOẠN THEO MA TRẬN 2026–2027 — KHÔNG PHẢI ĐỀ THI GỐC.*

Thời gian 90 phút · Thang điểm 10 · Đánh số lại từ 1 trong từng phần. Có thể dùng máy tính cầm tay theo quy định của kỳ kiểm tra thực tế.]
== Phần I. Lựa chọn một đáp án đúng (3,0 điểm)
Mỗi câu có đúng một đáp án; mỗi câu đúng được 0,25 điểm.

*I.1.* Câu nào sau đây là một mệnh đề?
#opts([Hãy tính $2+3$.], [Bạn học lớp nào?], [Số 7 là số nguyên tố.], [$x+1=0$ (chưa cho $x$).])

*I.2.* Phủ định của “$forall x in RR, x^2+1>0$” là
#opts([$forall x in RR, x^2+1<=0$.], [$exists x in RR, x^2+1<=0$.], [$exists x in RR, x^2+1<0$.], [$forall x in RR, x^2+1>=0$.])

*I.3.* Tập $A=\{x in ZZ | -1<x<=2\}$ là
#opts([$\{0;1;2\}$.], [$\{-1;0;1;2\}$.], [$\{0;1\}$.], [$\{1;2\}$.])

*I.4.* Trong biểu đồ Ven của hai tập $A,B$, miền nằm trong cả hai hình biểu diễn tập nào?
#opts([$A union B$.], [$A without B$.], [$B without A$.], [$A inter B$.])

*I.5.* Bất phương trình nào là bậc nhất hai ẩn?
#opts([$x^2+y<=2$.], [$x y>1$.], [$2x-3y>=6$.], [$x^2+y^2<4$.])

*I.6.* Cặp nào là nghiệm của hệ $x>=0$, $y>=0$, $x+y<=3$?
#opts([$(2;2)$.], [$(1;1)$.], [$(-1;2)$.], [$(0;4)$.])

*I.7.* $cos 120 degree$ bằng
#opts([$-1/2$.], [$1/2$.], [$sqrt(3)/2$.], [$-sqrt(3)/2$.])

*I.8.* $90 degree<alpha<180 degree$, $sin alpha=5/13$. Giá trị $cos alpha$ là
#opts([$12/13$.], [$-5/13$.], [$5/12$.], [$-12/13$.])
#newpage()
#heading(level: 1, outlined: false)[13. Đề minh họa (tiếp)]
*I.9.* Với tam giác $A B C$, $a=B C$, $b=C A$, $c=A B$, $R$ là bán kính đường tròn ngoại tiếp. Công thức nào đúng?
#opts([$a^2=b^2+c^2+2b c cos A$.], [$a=R sin A$.], [$a/(sin A)=2R$.], [$S=b c sin A$.])

*I.10.* Tam giác có hai cạnh 3 và 4, góc xen giữa $60 degree$. Độ dài cạnh còn lại là
#opts([$sqrt(13)$.], [5.], [7.], [$sqrt(37)$.])

*I.11.* Vectơ-không có độ dài bằng
#opts([1.], [0.], [$-1$.], [Không xác định.])

*I.12.* Cho hình bình hành $A B C D$ không suy biến, các đỉnh theo thứ tự. Khẳng định nào đúng?
#opts([$arrow(A B)=arrow(C D)$.], [$arrow(A B)=arrow(B A)$.], [$arrow(A D)=arrow(C B)$.], [$arrow(A B)=arrow(D C)$.])

== Phần II. Đúng–sai (2,0 điểm)
Với mỗi câu, chọn đúng hoặc sai cho *từng* ý a, b, c, d. Mỗi câu được chấm theo số ý trả lời đúng: 1 ý → 0,10; 2 ý → 0,25; 3 ý → 0,50; 4 ý → 1,00 điểm; không ý nào → 0 điểm.

*II.1.* Cho $A=[-2;3)$, $B=(1;5]$. Xét các khẳng định:

*a)* $-2 in A$ và $3 in.not A$.

*b)* Tập $B$ được biểu diễn trên trục số bằng phần từ 1 đến 5, lấy đầu mút 1 và bỏ đầu mút 5.

*c)* $A inter B=(1;3)$.

*d)* $C_RR(A union B)=(-infinity;-2) union (5;+infinity)$.

*II.2.* Một cơ sở dự định sản xuất $x$ sản phẩm I, $y$ sản phẩm II ($x,y in NN$). Mỗi sản phẩm I dùng 2 kg nguyên liệu, mỗi sản phẩm II dùng 1 kg. Lượng nguyên liệu có tối đa 8 kg. Xét bất phương trình $2x+y<=8$ trên mặt phẳng tọa độ:

*a)* Điểm $M(2;3)$ là một nghiệm của bất phương trình.

*b)* Đường biên đi qua hai điểm $(4;0)$ và $(0;8)$.

*c)* Miền nghiệm là nửa mặt phẳng không chứa $O(0;0)$, kể cả biên.

*d)* Điều kiện nguyên liệu trong tình huống đã cho được mô hình hóa bởi $2x+y>=8$.
#newpage()
#heading(level: 1, outlined: false)[13. Đề minh họa (kết)]
== Phần III. Trả lời ngắn (2,0 điểm)
Mỗi câu đúng được 0,50 điểm. Nếu đề có yêu cầu làm tròn, chỉ làm tròn kết quả cuối cùng.

*III.1.* Một tập hợp có 5 phần tử. Hỏi tập hợp đó có bao nhiêu tập con *khác rỗng*?
#v(4mm)
Trả lời: ……………………………………………………………………………
#v(4mm)
*III.2.* Lớp có 42 học sinh; 25 em tham gia câu lạc bộ Toán, 21 em tham gia câu lạc bộ Tiếng Anh và 6 em không tham gia câu lạc bộ nào trong hai câu lạc bộ đó. Có bao nhiêu học sinh tham gia *cả hai* câu lạc bộ?
#v(4mm)
Trả lời: ……………………………………………………………………………
#v(4mm)
*III.3.* $90 degree<alpha<180 degree$ và $sin alpha=4/5$. Tính $T=(2sin alpha-cos alpha)/(sin alpha+cos alpha)$.
#v(4mm)
Trả lời: ……………………………………………………………………………
#v(4mm)
*III.4.* Tam giác có ba cạnh dài 10 cm, 10 cm và 12 cm. Tính diện tích tam giác, đơn vị $"cm"^2$.
#v(4mm)
Trả lời: ……………………………………………………………………………

== Phần IV. Tự luận (3,0 điểm)
*IV.1 · 1,0 điểm.* Cho $A=[-3;2)$, $B=[0;5]$. Tìm $A inter B$, $A union B$ và $C_RR A$.
#v(5mm)
*IV.2 · 1,0 điểm.* Hai điểm quan sát $A,B$ cùng nằm trên một bờ sông, cách nhau 60 m. Một vị trí $C$ trên bờ đối diện tạo thành tam giác $A B C$ với $angle C A B=45 degree$ và $angle C B A=75 degree$. Tính khoảng cách $A C$ theo mô hình mặt phẳng, làm tròn đến 0,1 m.
#v(5mm)
*IV.3 · 1,0 điểm.* Một xưởng làm hai loại sản phẩm. Mỗi sản phẩm loại I cần 2 giờ máy và 1 giờ công; mỗi sản phẩm loại II cần 1 giờ máy và 2 giờ công. Xưởng có tối đa 12 giờ máy và 12 giờ công. Lãi mỗi sản phẩm loại I là 500 nghìn đồng, loại II là 400 nghìn đồng. Hỏi xưởng nên làm bao nhiêu sản phẩm mỗi loại để có lãi lớn nhất? Biết số sản phẩm là số nguyên không âm; trình bày mô hình, miền nghiệm và cách xác định phương án tối ưu.
#v(6mm)
#align(center)[*HẾT ĐỀ MINH HỌA*]
#newpage()
= 14. Đáp án và lời giải đề minh họa
== 14.1. Bảng đáp án nhanh
#table(columns: (auto, auto, auto, auto, auto, auto, auto), inset: 7pt,
[Câu I], [1], [2], [3], [4], [5], [6],
[Đáp án], [C], [B], [A], [D], [C], [B],
[Câu I], [7], [8], [9], [10], [11], [12],
[Đáp án], [A], [D], [C], [A], [B], [D])
#table(columns: (auto, auto, auto, auto, auto), inset: 7pt,
[Câu II], [a], [b], [c], [d],
[1], [Đ], [S], [Đ], [Đ],
[2], [Đ], [Đ], [S], [S])
#table(columns: (auto, auto, auto, auto, auto), inset: 7pt,
[Câu III], [1], [2], [3], [4],
[Đáp án], [31], [10], [11], [48])
Đáp số tự luận: IV.1 $[0;2)$, $[-3;5]$, $(-infinity;-3) union [2;+infinity)$; IV.2 66,9 m; IV.3 4 sản phẩm I, 4 sản phẩm II, lãi 3,6 triệu đồng.

== 14.2. Giải thích toàn bộ phần lựa chọn
*I.1 — C.* “Số 7 là số nguyên tố” là câu khẳng định đúng. A là yêu cầu, B là câu hỏi, D chứa biến chưa được xác định.

*I.2 — B.* Đổi $forall$ thành $exists$, giữ miền $RR$, đổi $>$ thành $<=$. Phương án C bỏ trường hợp bằng 0 nên không phải phủ định đúng về cấu trúc logic, dù cả B và C đều sai với biểu thức cụ thể này.

*I.3 — A.* Số nguyên lớn hơn $-1$ và không quá 2 là 0, 1, 2. Không lấy $-1$; có lấy 2.

*I.4 — D.* “Nằm trong cả hai” đúng định nghĩa giao, không phải hợp hay hiệu.

*I.5 — C.* Có dạng $a x+b y>=c$ với hệ số $(2;-3)$ không đồng thời bằng 0. Các phương án khác chứa $x^2$, $x y$ hoặc $y^2$.

*I.6 — B.* $(1;1)$ có hai tọa độ không âm và tổng $2<=3$. A có tổng 4, C có hoành độ âm, D có tổng 4, nên đều không thỏa hệ.

*I.7 — A.* $cos 120 degree=cos(180 degree-60 degree)=-cos 60 degree=-1/2$.

*I.8 — D.* $cos^2 alpha=1-25/169=144/169$. Góc tù có côsin âm nên $cos alpha=-12/13$.
#newpage()
#heading(level: 1, outlined: false)[14. Lời giải đề minh họa (tiếp)]
*I.9 — C.* Định lí sin cho $a/sin A=2R$. A sai dấu trước tích, B thiếu hệ số 2, D thiếu hệ số $1/2$.

*I.10 — A.* Theo côsin, cạnh cần tìm có bình phương $3^2+4^2-2 dot 3 dot 4 cos 60 degree=13$; cạnh dương nên bằng $sqrt(13)$.

*I.11 — B.* Độ dài vectơ-không được quy ước bằng 0.

*I.12 — D.* Hai vectơ $arrow(A B)$ và $arrow(D C)$ cùng hướng, cùng độ dài. A và C đảo chiều một cạnh, B đảo điểm đầu–cuối của cùng đoạn nên sai với hình không suy biến.

== 14.3. Giải thích từng ý đúng–sai
*II.1a — Đúng.* Ngoặc vuông ở $-2$ nghĩa là lấy $-2$; ngoặc tròn ở 3 nghĩa là bỏ 3.

*II.1b — Sai.* $B=(1;5]$ phải bỏ đầu mút 1 (chấm rỗng) và lấy đầu mút 5 (chấm đặc), ngược mô tả trong đề.

*II.1c — Đúng.* Đồng thời $-2<=x<3$ và $1<x<=5$ tương đương $1<x<3$. Hai đầu đều bỏ.

*II.1d — Đúng.* $A union B=[-2;5]$, nên phần bù trong $RR$ là $(-infinity;-2) union (5;+infinity)$. Hai đầu $-2,5$ thuộc hợp nên không thuộc phần bù.

*II.2a — Đúng.* Thay $M(2;3)$: $2 dot 2+3=7<=8$.

*II.2b — Đúng.* Thay $(4;0)$ và $(0;8)$ đều được vế trái bằng 8; hai điểm phân biệt xác định đường thẳng biên $2x+y=8$.

*II.2c — Sai.* $O$ không thuộc biên và thỏa $0<=8$. Miền nghiệm phải là nửa mặt phẳng *chứa* $O$, kể cả biên. Ở đây xét riêng bất phương trình trên toàn mặt phẳng; nếu xét sản xuất thì còn lấy giao với $x,y>=0$ và xét số nguyên.

*II.2d — Sai.* Tiêu hao nguyên liệu là $2x+y$ kg, “tối đa 8 kg” phải là $2x+y<=8$. Dấu $>=$ biểu thị ít nhất 8 kg, không đúng điều kiện đã nêu.

== 14.4. Trả lời ngắn có lập luận
*III.1.* Có $2^5=32$ tập con, bỏ tập rỗng còn *31*.

*III.2.* Số tham gia ít nhất một câu lạc bộ là $42-6=36$. Số tham gia cả hai là $25+21-36=10$. Đáp án *10 học sinh*.

*III.3.* $cos alpha=-sqrt(1-16/25)=-3/5$ vì góc tù.
$ T=(2 dot 4/5-(-3/5))/(4/5+(-3/5))=(11/5)/(1/5)=11. $
Mẫu khác 0, đáp án *11*.

*III.4.* $p=(10+10+12)/2=16$ cm. Heron:
$S=sqrt(16(16-10)(16-10)(16-12))=sqrt(2304)=48$ $"cm"^2$. Đáp án số là *48*.
#newpage()
#heading(level: 1, outlined: false)[14. Lời giải tự luận và gợi ý chấm]
== IV.1 · Phép toán tập hợp (1,0 điểm)
$ A inter B=[0;2), quad A union B=[-3;5]. $
$ C_RR A=(-infinity;-3) union [2;+infinity). $
Giao lấy phần từ 0 đến 2, có 0 nhưng không có 2. Hợp liền từ $-3$ đến 5, lấy cả hai đầu. Phần bù bỏ $-3$ vì thuộc $A$, lấy 2 vì không thuộc $A$.

*Gợi ý điểm:* giao đúng 0,25; hợp đúng 0,25; phần bù đúng hai phía và hai đầu mút 0,50. Đây là hướng dẫn tự chấm của tài liệu, không phải đáp án chấm chính thức.

== IV.2 · Đo khoảng cách (1,0 điểm)
Trong tam giác $A B C$, $A B=60$ m; góc $C=180 degree-45 degree-75 degree=60 degree$.

Áp dụng định lí sin:
$ (A C)/(sin B)=(A B)/(sin C) => A C=(60sin 75 degree)/(sin 60 degree). $
Suy ra $A C approx 66.9213$ m. Vậy khoảng cách cần tìm là *66,9 m* (làm tròn đến 0,1 m).

*Gợi ý điểm:* xác định góc $C$ 0,25; lập hệ thức sin đúng 0,50; tính và kết luận đúng đơn vị, làm tròn 0,25. Một cách giải khác đúng được tính tương đương.

== IV.3 · Phương án sản xuất (1,0 điểm)
Gọi $x,y$ là số sản phẩm loại I, II, $x,y in NN$. Điều kiện:
$ 2x+y<=12, quad x+2y<=12, quad x>=0, quad y>=0. $
Hàm lãi $F=500x+400y$ (nghìn đồng). Xét miền liên tục của hệ trong góc phần tư thứ nhất. Các đỉnh:
- $O(0;0)$;
- $A(6;0)$ vì trên trục hoành $x<=6$;
- $B(4;4)$ là giao $2x+y=12$ và $x+2y=12$;
- $C(0;6)$ vì trên trục tung $y<=6$.

Miền là tứ giác đóng, bị chặn $O A B C$. So sánh giá trị tại các đỉnh:
#table(columns: (1fr, auto, auto, auto, auto), inset: 6pt,
[Đỉnh], [$O$], [$A$], [$B$], [$C$],
[$F$ (nghìn đồng)], [0], [3000], [3600], [2400])
Lãi liên tục lớn nhất là 3600 nghìn đồng tại $B(4;4)$. Vì $B$ có tọa độ nguyên, phương án này cũng đạt cực đại trong các phương án sản phẩm nguyên. Vậy làm *4 sản phẩm loại I, 4 sản phẩm loại II*, thu lãi lớn nhất *3,6 triệu đồng*. Kiểm tra dùng đủ $2 dot 4+4=12$ giờ máy và $4+2 dot 4=12$ giờ công.

*Gợi ý điểm:* chọn ẩn và lập hệ 0,25; lập hàm lãi 0,25; xác định đúng các đỉnh và so sánh 0,25; kết luận phương án nguyên và số tiền 0,25. Không chỉ ghi đáp số mà bỏ mô hình tối ưu.
#newpage()
= 15. Đối chiếu từng vị trí câu hỏi
Bảng này chỉ rõ đề minh họa phủ đủ các vị trí trong *bảng đặc tả*. Kí hiệu I, II, III, IV lần lượt chỉ bốn phần của đề. “NB/TH/VD/VDC” theo hướng của ma trận; riêng điểm chưa thống nhất đã được ghi ở phần 1.
#table(columns: (auto, 1.1fr, auto, 1.4fr), inset: 5pt, stroke: 0.4pt + luma(80%),
[*Vị trí*], [*Đơn vị kiến thức*], [*Mức*], [*Năng lực được kiểm tra*],
[I.1], [Mệnh đề], [NB], [Nhận biết mệnh đề, phân biệt câu chứa biến.],
[I.2], [Mệnh đề], [NB], [Hiểu lượng từ và cấu trúc phủ định.],
[I.3], [Tập hợp], [NB], [Tính chất đặc trưng → liệt kê phần tử.],
[I.4], [Phép toán tập hợp], [NB], [Nhận diện miền giao trong Ven.],
[I.5], [Bất phương trình], [NB], [Nhận đúng dạng bậc nhất hai ẩn.],
[I.6], [Hệ bất phương trình], [NB], [Kiểm tra nghiệm của hệ.],
[I.7], [Giá trị lượng giác], [NB], [Góc bù và góc đặc biệt.],
[I.8], [Giá trị lượng giác], [TH], [Tìm côsin từ sin và miền góc.],
[I.9], [Hệ thức lượng], [NB], [Nhận diện định lí sin.],
[I.10], [Hệ thức lượng], [TH], [Áp dụng định lí côsin.],
[I.11], [Khái niệm vectơ], [NB], [Nhận biết độ dài vectơ-không.],
[I.12], [Khái niệm vectơ], [TH], [Hai vectơ bằng nhau.],
[II.1a], [Tập hợp], [NB], [Thuộc/không thuộc.],
[II.1b], [Tập hợp], [TH], [Biểu diễn nửa khoảng trên trục số.],
[II.1c], [Phép toán tập hợp], [TH], [Giao hai khoảng, đoạn.],
[II.1d], [Phép toán tập hợp], [VD], [Hợp rồi lấy phần bù.],
[II.2a], [Bất phương trình], [NB], [Thay tọa độ kiểm tra nghiệm.],
[II.2b], [Bất phương trình], [TH], [Đường biên qua hai điểm.],
[II.2c], [Bất phương trình], [TH], [Chọn nửa mặt phẳng nghiệm.],
[II.2d], [Bất phương trình], [VD], [Chuyển điều kiện nguyên liệu thành bất phương trình.],
[III.1], [Tập hợp], [TH], [Đếm tập con khác rỗng.],
[III.2], [Phép toán tập hợp], [VD], [Thực tế hai nhóm có người ngoài cả hai.],
[III.3], [Giá trị lượng giác], [VD], [Tính biểu thức khi biết một giá trị lượng giác.],
[III.4], [Hệ thức lượng], [TH], [Dùng Heron tính diện tích.],
[IV.1], [Phép toán tập hợp], [TH], [Giao, hợp, phần bù.],
[IV.2], [Hệ thức lượng], [VD\*], [Đo khoảng cách bằng định lí sin.],
[IV.3], [Hệ bất phương trình], [VDC], [Lập mô hình, tìm phương án tối ưu.])
*IV.2:* Dạng đơn giản, đúng yêu cầu thực tế của nguồn; phần mô tả tự luận ghi MĐ2 trong khi ô ma trận có chỗ ghi VD.
#newpage()
= 16. Tự chấm và ôn tập lần cuối
== 16.1. Quản lí 90 phút
Gợi ý: lựa chọn 15 phút, đúng–sai 15 phút, trả lời ngắn 15 phút, tự luận 35 phút và 10 phút kiểm tra. Không nhất thiết làm theo thứ tự; đánh dấu câu khó để quay lại. Trước khi tính số, đọc kỹ “khác rỗng”, “ít nhất”, “tối đa”, “làm tròn”.

== 16.2. Tính điểm minh bạch
Gọi $k$ là số câu đúng phần I; $r_1,r_2$ là số ý đúng ở mỗi câu II; $h$ là số câu đúng phần III; $t$ là điểm phần IV theo gợi ý. Khi đó:
$ "Điểm"=0.25k+f(r_1)+f(r_2)+0.5h+t. $
Trong đó $f(0)=0$, $f(1)=0.10$, $f(2)=0.25$, $f(3)=0.50$, $f(4)=1.00$.

*Ví dụ:* Đúng 10 câu I, câu II.1 đúng 3 ý, II.2 đúng 4 ý, phần III đúng 3 câu, tự luận 2,25 điểm: tổng $2.5+0.5+1+1.5+2.25=7.75$ điểm. Việc ghi hoặc làm tròn điểm theo quy định cụ thể của nhà trường, không tự làm tròn từng phần.

== 16.3. Một trang kiến thức phải nhớ
#note[
*Logic:* Phủ định $forall$ → $exists$, phủ định $exists$ → $forall$, đồng thời phủ định mệnh đề bên trong. $P=>Q$: $P$ đủ, $Q$ cần.

*Tập hợp:* $n$ phần tử → $2^n$ tập con; giao = chung; hợp = ít nhất một; phần bù = trong vũ trụ nhưng ngoài tập. $n(A union B)=n(A)+n(B)-n(A inter B)$.

*Bất phương trình:* Vẽ biên → chọn điểm thử không trên biên → xác định phía → xét có lấy biên. Hệ là phần giao. Tối ưu tuyến tính trên đa giác đóng bị chặn: so sánh các đỉnh; kiểm tra tính nguyên.

*Lượng giác:* $sin^2 alpha+cos^2 alpha=1$. Góc tù có sin dương, côsin âm. Góc bù: sin giữ nguyên, cos/tan/cot đổi dấu (khi xác định).

*Tam giác:* $a^2=b^2+c^2-2b c cos A$;
$a/sin A=2R$; $S=1/2b c sin A=p r=(a b c)/(4R)$;
$S=sqrt(p(p-a)(p-b)(p-c))$, $p=(a+b+c)/2$.

*Vectơ:* Bằng nhau = cùng hướng và cùng độ dài. Đảo điểm đầu–cuối → vectơ đối. Vectơ-không dài 0, cùng phương và cùng hướng với mọi vectơ theo quy ước.
]

== 16.4. Trước khi nộp bài
□ Mỗi câu lựa chọn chỉ chọn một đáp án. □ Mỗi câu đúng–sai có đủ 4 lựa chọn. □ Không bỏ dấu âm ở kết quả lượng giác. □ Khoảng, đoạn có đúng dấu ngoặc. □ Hình miền nghiệm ghi rõ phía lấy và biên. □ Kết quả thực tế có đơn vị và làm tròn đúng. □ Máy tính đang ở DEG.
#newpage()
= 17. Nguồn tham khảo và giới hạn
Các nguồn được tra cứu ngày *24/10/2026*. Chỉ dùng để đối chiếu phạm vi, thuật ngữ và công thức; không coi các trang luyện tập là văn bản chính thức của Bộ hoặc nhà trường. Không sao chép một đề kiểm tra có sẵn. Mọi bài toán có dữ kiện trong phần 2–14 đều được biên soạn cho tài liệu này.

*0. Tài liệu đầu vào do người dùng cung cấp.* “MA TRẬN TOÁN 10 - GIỮA KÌ I.docx”, ghi Trường THPT Hà Huy Tập, Tổ Toán–Tin, năm học 2026–2027, 90 phút. Nguồn chính để quyết định cấu trúc và vị trí câu hỏi; giữ nguyên tệp trong kho mã. Có bản trích xuất văn bản và mã SHA-256 tại thư mục `kiem-chung/`.

*1. Trang giới thiệu SGK của HEID.* “Sách giáo khoa Toán Lớp 10 Tập 1 | Kết nối tri thức với cuộc sống”. Dùng xác nhận tên sách, NXB Giáo dục Việt Nam, nhóm tác giả, năm xuất bản 2022; không dùng phần trường thông tin ở dưới trang có dữ liệu lẫn lớp/bộ sách.
#link("https://heid.vn/product/sgk-toan-lop-10-tap-1-ket-noi-tri-thuc/")[heid.vn/product/sgk-toan-lop-10-tap-1-ket-noi-tri-thuc/]

*2. TOANMATH.* Mục lục “Sách giáo khoa Toán 10 (tập 1) (Kết Nối Tri Thức Với Cuộc Sống)”. Dùng đối chiếu Bài 1–7. Không sử dụng những lời giới thiệu rộng về chính sách áp dụng toàn quốc làm căn cứ pháp lý.
#link("https://toanmath.com/2022/01/sach-giao-khoa-toan-10-tap-1-ket-noi-tri-thuc-voi-cuoc-song.html")[toanmath.com · SGK Toán 10 tập 1 · mục lục]

*3. Loigiaihay.* “Giải mục 1 trang 6, 7 SGK Toán 10 tập 1 – Kết nối tri thức”. Dùng đối chiếu cách nhận biết mệnh đề, câu hỏi và câu chứa biến; không chép ví dụ của trang.
#link("https://loigiaihay.com/giai-muc-1-trang-6-7-sgk-toan-10-tap-1-ket-noi-tri-thuc-a105281.html")[loigiaihay.com · Mệnh đề · trang 6–7]

*4. VietJack.* “Hệ thức lượng trong tam giác lớp 10 (Lý thuyết Toán 10 Kết nối tri thức)”. Dùng đối chiếu kí hiệu cạnh–góc, sin, côsin và các công thức diện tích. Một số căn/phân số bị mất trong bản văn bản web; tài liệu đã khôi phục và kiểm tra toán học, không sao chép văn bản lỗi.
#link("https://vietjack.com/toan-10-kn/ly-thuyet-bai-6-he-thuc-luong-trong-tam-giac.jsp")[vietjack.com · Lý thuyết Bài 6]

*5. VietJack.* “Các khái niệm mở đầu lớp 10 (Lý thuyết Toán 10 Kết nối tri thức)”. Dùng đối chiếu quy ước vectơ-không và định nghĩa vectơ bằng nhau.
#link("https://vietjack.com/toan-10-kn/ly-thuyet-bai-7-cac-khai-niem-mo-dau.jsp")[vietjack.com · Lý thuyết Bài 7]

#warn[*Giới hạn cần nhắc lại:* Không có đề thi/đáp án gốc trong dữ liệu được cung cấp. Tài liệu bảo đảm phủ các vị trí kiến thức được mô tả trong ma trận, không cam kết dự đoán hay tái tạo đề thi chính thức. Khi có đề gốc hợp lệ, cần đối chiếu và bổ sung riêng, không đổi nhãn đề minh họa thành đề thật.]
