#import "template.typ": *

// ============================================================================
// PHẦN C — HỆ THỐNG LÝ THUYẾT TRỌNG TÂM, DẠNG TOÁN & BẪY HAY SAI (BÀI 1 -> BÀI 7)
// ============================================================================

= PHẦN C. HỆ THỐNG LÝ THUYẾT TRỌNG TÂM & PHƯƠNG PHÁP GIẢI (BÀI 1 → BÀI 7)

// ----------------------------------------------------------------------------
// CHƯƠNG I: MỆNH ĐỀ VÀ TẬP HỢP (4,00 ĐIỂM)
// ----------------------------------------------------------------------------
#chapter-banner(
  "CHƯƠNG I",
  "MỆNH ĐỀ VÀ TẬP HỢP",
  "Bài 1 & Bài 2 SGK Kết nối tri thức Tập 1",
  "TRỌNG TÂM SỐ 1: 4,00 ĐIỂM (40%)"
)

== Bài 1. Mệnh đề (Đơn vị 1.1 — Câu 1, Câu 2 Phần I: 0,50 điểm)

#theory-card("1. Mệnh đề, mệnh đề chứa biến và mệnh đề phủ định")[
  - *Mệnh đề lôgic (gọi tắt là mệnh đề):* Là một câu khẳng định *đúng* hoặc *sai*. Một câu không thể vừa đúng vừa sai.
    - *Không phải mệnh đề:* Câu nghi vấn (*“Mấy giờ rồi?”*), câu cầu khiến (*“Hãy học bài đi!”*), câu cảm thán (*“Trời đẹp quá!”*).
  - *Mệnh đề chứa biến $P(x)$:* Là câu khẳng định chứa biến $x$ (thuộc tập $X$) chưa xác định được tính đúng sai, nhưng khi thay mỗi giá trị cụ thể $x = x_0 in X$ thì $P(x_0)$ trở thành một mệnh đề có tính đúng/sai xác định.
    - *Ví dụ:* $P(n):$ *“$2n + 1$ chia hết cho $3$”* ($n in NN$). Với $n = 1$, $P(1)$ đúng; với $n = 2$, $P(2)$ sai.
  - *Mệnh đề phủ định $overline(P)$:* Thêm (hoặc bớt) từ *“không”*, *“không phải”* trước vị ngữ của $P$. Nếu $P$ đúng thì $overline(P)$ sai và ngược lại.
]

#theory-card("2. Mệnh đề kéo theo, mệnh đề đảo, mệnh đề tương đương & Điều kiện cần – đủ")[
  - *Mệnh đề kéo theo $P arrow.r.double Q$:* Phát biểu dạng *“Nếu $P$ thì $Q$”*. Mệnh đề $P arrow.r.double Q$ *chỉ sai khi $P$ đúng và $Q$ sai*.
  - *Định lí toán học & Điều kiện cần / đủ:* Khi $P arrow.r.double Q$ là một định lí đúng:
    - $P$ là *giả thiết*, là *điều kiện đủ* để có $Q$.
    - $Q$ là *kết luận*, là *điều kiện cần* để có $P$.
  - *Mệnh đề đảo của $P arrow.r.double Q$:* Là mệnh đề $Q arrow.r.double P$. *(Chú ý: Mệnh đề thuận đúng KHÔNG suy ra mệnh đề đảo đúng!)*
  - *Mệnh đề tương đương $P arrow.l.r.double Q$:* Đọc là *“$P$ khi và chỉ khi $Q$”* hoặc *“$P$ là điều kiện cần và đủ để có $Q$”*. Đúng khi cả hai chiều $P arrow.r.double Q$ và $Q arrow.r.double P$ đều đúng.
]

#theory-card("3. Mệnh đề chứa kí hiệu phổ biến (∀) và kí hiệu tồn tại (∃)")[
  - *Kí hiệu $forall$ (với mọi):* $forall x in X, P(x)$ đúng khi *mọi* phần tử $x_0 in X$ đều làm $P(x_0)$ đúng. Chỉ cần *1 phản ví dụ* $x_0 in X$ làm $P(x_0)$ sai thì mệnh đề $forall$ lập tức *sai*!
  - *Kí hiệu $exists$ (tồn tại / có ít nhất một):* $exists x in X, P(x)$ đúng khi chỉ cần *tìm được ít nhất 1 giá trị* $x_0 in X$ làm $P(x_0)$ đúng.
  - *Quy tắc phủ định mệnh đề chứa $forall, exists$:* Đổi lượng từ ($forall arrow.l.r exists$) đồng thời phủ định tính chất $P(x)$:
    - *Ví dụ:* Phủ định của $P:$ “$forall x in RR, x^2 - 2 x + 3 > 0$” là $overline(P):$ “$exists x in RR, x^2 - 2 x + 3 <= 0$”.
]

#trap-box("BẪY CÂU 1 – CÂU 2 PHẦN I (MỆNH ĐỀ)")[
  - *Bẫy 1:* Câu chứa biến như *“$x + 3 = 5$”* (không có $forall$ hay $exists$ đi kèm) là *mệnh đề chứa biến*, *KHÔNG phải là mệnh đề*! Nhưng *“$exists x in RR, x + 3 = 5$”* lại *LÀ một mệnh đề* (và là mệnh đề đúng).
  - *Bẫy 2:* Khi phủ định $>$ phải đổi thành *$<=$* (nhiều bạn đổi nhầm thành $<$ làm mất dấu bằng!). Không bao giờ phủ định điều kiện miền $x in RR$ thành $x notin RR$.
]

== Bài 2. Tập hợp và các phép toán trên tập hợp (Đơn vị 1.2 & 1.3 — 3,50 điểm)

#theory-card("1. Cách cho tập hợp, quan hệ phần tử – tập con & Số tập hợp con")[
  - *Hai cách xác định tập hợp:* (1) Liệt kê các phần tử: $A = {0; 1; 2; 3}$; (2) Chỉ ra tính chất đặc trưng: $A = {x in NN | x <= 3}$.
  - *Phân biệt kí hiệu:*
    - $a in A$ / $a notin A$: Quan hệ giữa *phần tử* và *tập hợp* (Ví dụ: $2 in {1; 2; 3}$, tuyệt đối không viết $2 subset {1; 2; 3}$).
    - $B subset A$ (hoặc $A supset B$): Quan hệ giữa *tập hợp* và *tập hợp* ($forall x, x in B arrow.r.double x in A$). Ví dụ: ${2} subset {1; 2; 3}$, $emptyset subset A$.
    - $A = B arrow.l.r.double A subset B "và" B subset A$.
  - *Công thức vàng đếm tập con (Câu 1 Trả lời ngắn):* Nếu $n(A) = n$ thì $A$ có đúng *$2^n$ tập hợp con* (trong đó có $C_n^k$ tập con gồm đúng $k$ phần tử).
]

#theory-card("2. Các tập con thường dùng của tập số thực ℝ (Khoảng – Đoạn – Nửa khoảng)")[
  #table(
    columns: (1.25fr, 1.75fr, 1.35fr, 1.65fr),
    align: (left + horizon, left + horizon, left + horizon, left + horizon),
    stroke: 0.5pt + c-border,
    inset: (x: 5pt, y: 4pt),
    fill: (x, y) => if y == 0 { c-blue-bg } else { white },
    [*Kí hiệu*], [*Định nghĩa điều kiện*], [*Kí hiệu*], [*Định nghĩa điều kiện*],
    [*Đoạn* $[a; b]$], [${x in RR | a <= x <= b}$], [*Nửa khoảng* $(a; +infinity)$], [${x in RR | x > a}$],
    [*Khoảng* $(a; b)$], [${x in RR | a < x < b}$], [*Nửa khoảng* $[a; +infinity)$], [${x in RR | x >= a}$],
    [*Nửa khoảng* $[a; b)$], [${x in RR | a <= x < b}$], [*Khoảng* $(-infinity; b)$], [${x in RR | x < b}$],
    [*Nửa khoảng* $(a; b]$], [${x in RR | a < x <= b}$], [*Nửa khoảng* $(-infinity; b]$], [${x in RR | x <= b}$],
  )
  *(Ghi nhớ: Đầu $plus.minus infinity$ LUÔN LUÔN dùng dấu ngoặc tròn `(` hoặc `)`, không bao giờ dùng ngoặc vuông!)*
]

#align(center)[#image("assets/number_line_intervals.svg", width: 98%)]

#theory-card("3. Bốn phép toán trên tập hợp & Biểu đồ Ven")[
  - *Giao* $A inter B = {x | x in A "và" x in B}$ (phần chung của hai tập hợp).
  - *Hợp* $A union B = {x | x in A "hoặc" x in B}$ (gộp tất cả phần tử của cả hai tập hợp, mỗi phần tử liệt kê 1 lần).
  - *Hiệu* $A without B = {x | x in A "và" x notin B}$ (giữ phần thuộc $A$, gạch bỏ phần thuộc $B$).
  - *Phần bù* $C_A B = A without B$ (chỉ dùng khi $B subset A$). Hay gặp nhất: *$C_RR A = RR without A$*.
  #v(3pt)
  #align(center)[#image("assets/venn_operations.svg", width: 98%)]
]

#method-box("DẠNG 1 (CÂU 1d ĐÚNG/SAI) — TÌM THAM SỐ m TRONG PHÉP TOÁN TẬP HỢP")[
  Cho hai khoảng/đoạn khác rỗng $A = [a; b]$ và $B = [m; m + 2]$:
  - *Để $B subset A$:* Vẽ trục số xếp thứ tự đầu mút $arrow.r.double a <= m$ *và* $m + 2 <= b$ (kiểm tra kỹ dấu `=` tại từng đầu mút bằng cách thay trực tiếp $m$ biên vào xem $B subset A$ còn đúng không!).
  - *Để $A inter B = emptyset$:* Hoặc $B$ nằm hẳn bên trái $A$ ($m + 2 < a$), hoặc $B$ nằm hẳn bên phải $A$ ($m > b$).
  - *Để $A inter B != emptyset$:* Làm *phần bù* cực nhanh! Tìm $m$ để $A inter B = emptyset$ trước, rồi lấy phần bù trên tập điều kiện của $m$!
]

#method-box("DẠNG 2 (CÂU 2 TRẢ LỜI NGẮN) — BÀI TOÁN ĐẾM THỰC TẾ BẰNG BIỂU ĐỒ VEN")[
  #align(center)[#image("assets/venn_counting_model.svg", width: 98%)]
  #v(2pt)
  *Ví dụ mẫu:* Lớp 10A có $42$ học sinh, trong đó có $24$ em giỏi Toán, $18$ em giỏi Tiếng Anh và $6$ em không giỏi môn nào trong hai môn trên. Hỏi có bao nhiêu em giỏi *cả hai môn*?
  - *Giải nhanh:* Số học sinh giỏi ít nhất 1 môn là $n(T union A) = 42 - 6 = 36$. Áp dụng công thức: $n(T inter A) = n(T) + n(A) - n(T union A) = 24 + 18 - 36 = bold(6)$ (học sinh). *(Nếu hỏi giỏi ĐÚNG 1 môn: lấy $(24 - 6) + (18 - 6) = 30$ học sinh!)*
]

// ----------------------------------------------------------------------------
// CHƯƠNG II: BẤT PHƯƠNG TRÌNH & HỆ BPT BẬC NHẤT HAI ẨN (2,50 ĐIỂM)
// ----------------------------------------------------------------------------
#chapter-banner(
  "CHƯƠNG II",
  "BẤT PHƯƠNG TRÌNH & HỆ BẤT PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN",
  "Bài 3 & Bài 4 SGK Kết nối tri thức Tập 1",
  "TRỌNG TÂM SỐ 3: 2,50 ĐIỂM (25%)"
)

== Bài 3. Bất phương trình bậc nhất hai ẩn (Đơn vị 2.1 — Câu 5 P.I & Câu 2 Đúng/Sai: 1,25 điểm)

#theory-card("1. Nhận dạng, nghiệm và quy tắc 3 bước biểu diễn miền nghiệm")[
  - *Định nghĩa:* BPT bậc nhất hai ẩn $x, y$ có dạng $a x + b y <= c$ (hoặc $<, >, >=$) trong đó $a, b, c in RR$ và *$a, b$ không đồng thời bằng $0$* ($a^2 + b^2 != 0$); bậc của $x$ và $y$ đều không vượt quá $1$, không chứa $x y, x^2, sqrt(x), 1/x$.
  - *Nghiệm:* Cặp số $(x_0; y_0)$ thỏa mãn bất đẳng thức số là một nghiệm. Mọi BPT bậc nhất hai ẩn đều có *vô số nghiệm*.
  - *Quy trình 3 bước biểu diễn miền nghiệm (chuẩn SGK Kết nối tri thức):*
    1. *Bước 1:* Vẽ đường thẳng bờ $d: a x + b y = c$ trên $O x y$ (lấy 2 giao điểm với hai trục tọa độ). Vẽ *nét liền* nếu có dấu `=`, *nét đứt* nếu không có dấu `=`.
    2. *Bước 2:* Chọn điểm thử $M_0(x_0; y_0) notin d$ (thường chọn $O(0; 0)$ nếu $c != 0$; nếu $c = 0$ thì chọn $(1; 0)$ hoặc $(0; 1)$).
    3. *Bước 3:* Thay tọa độ $M_0$ vào BPT. Nếu *đúng* thì nửa mặt phẳng chứa $M_0$ là miền nghiệm (gạch bỏ nửa kia); nếu *sai* thì gạch bỏ nửa mặt phẳng chứa $M_0$.
  #v(3pt)
  #align(center)[#image("assets/halfplane_steps.svg", width: 98%)]
]

#method-box("MẸO ĐỌC NGƯỢC PHƯƠNG TRÌNH BỜ TỪ HÌNH VẼ TRONG 5 GIÂY (CÂU 2b, 2c Đ/S)")[
  Khi hình vẽ cho đường bờ $d$ đi qua $A(x_0; 0)$ trên $O x$ và $B(0; y_0)$ trên $O y$:
  1. Lập tức viết phương trình đoạn chắn: $x / x_0 + y / y_0 = 1$, quy đồng khử mẫu được $a x + b y = c$.
  2. Nhìn gốc $O(0; 0)$: nếu $O$ nằm trong *phần không bị gạch* (miền nghiệm) thì thay $(0; 0)$ vào vế trái phải thỏa mãn dấu bất đẳng thức so với $c$! Nhìn nét bờ (liền hay đứt) để chốt dấu $<=, >=$ hay $<, >$.
]

== Bài 4. Hệ bất phương trình bậc nhất hai ẩn (Đơn vị 2.2 — Câu 6 P.I & Câu 3 Tự luận VDC: 1,25 điểm)

#theory-card("Quy trình 4 bước vàng giải bài toán thực tế Quy hoạch tuyến tính (Câu 3 Tự luận — 1,0 điểm)")[
  - *Bước 1 (Đặt ẩn & Lập hệ BPT — 0,25 điểm):* Gọi $x, y$ là hai đại lượng cần tìm (chú ý điều kiện $x >= 0, y >= 0$, có thể thêm $x, y in NN$ nếu là số xe, số máy). Dịch từng câu ràng buộc (nguyên liệu, thời gian máy, diện tích, vốn...) thành hệ BPT bậc nhất hai ẩn. Viết biểu thức mục tiêu cần tối ưu $F(x; y) = p x + q y$ (lợi nhuận hoặc chi phí).
  - *Bước 2 (Biểu diễn miền nghiệm — 0,25 điểm):* Vẽ từng đường thẳng bờ trên cùng mặt phẳng $O x y$, gạch bỏ các miền không thỏa mãn để xác định *miền đa giác nghiệm lồi* (ví dụ tứ giác $O A B C$).
  - *Bước 3 (Tìm tọa độ các đỉnh — 0,25 điểm):* Giải các hệ phương trình bậc nhất hai ẩn tương ứng với giao điểm của từng cặp đường bờ cắt nhau để tìm chính xác tọa độ tất cả các đỉnh của miền đa giác.
  - *Bước 4 (Tính giá trị $F$ tại các đỉnh & Kết luận — 0,25 điểm):* Tính $F(x; y)$ tại từng đỉnh, so sánh để kết luận giá trị lớn nhất (hoặc nhỏ nhất) và trả lời đúng câu hỏi thực tế của đề bài.
  #v(3pt)
  #align(center)[#image("assets/lp_feasible_theory.svg", width: 98%)]
]

#trap-box("BẪY MẤT ĐIỂM OAN Ở BÀI TOÁN THỰC TẾ CHƯƠNG II")[
  1. *Không đồng nhất đơn vị:* Đề cho nguyên liệu tổng là *4 tấn* nhưng định mức mỗi sản phẩm là *kg* $arrow.r$ bắt buộc phải đổi *4 tấn = 4000 kg* trước khi lập BPT! Tương tự với *giờ – phút*, *triệu đồng – nghìn đồng*.
  2. *Quên điều kiện không âm $x >= 0, y >= 0$:* Làm thiếu 2 cạnh trên trục $O x, O y$ khiến miền nghiệm không khép kín thành đa giác!
]

// ----------------------------------------------------------------------------
// CHƯƠNG III: HỆ THỨC LƯỢNG TRONG TAM GIÁC (3,00 ĐIỂM)
// ----------------------------------------------------------------------------
#chapter-banner(
  "CHƯƠNG III",
  "HỆ THỨC LƯỢNG TRONG TAM GIÁC",
  "Bài 5 & Bài 6 SGK Kết nối tri thức Tập 1",
  "TRỌNG TÂM SỐ 2: 3,00 ĐIỂM (30%)"
)

== Bài 5. Giá trị lượng giác của một góc từ 0° đến 180° (Đơn vị 3.1 — 1,00 điểm)

#align(center)[#image("assets/unit_semicircle.svg", width: 98%)]

#method-box("HAI DẠNG TOÁN CHẮC CHẮN GẶP Ở BÀI 5 (CÂU 8 P.I & CÂU 3 TRẢ LỜI NGẮN)")[
  1. *Dạng 1 (Câu 8 P.I): Cho 1 GTLG của góc $alpha$, tính GTLG còn lại:*
     - Nếu biết $sin alpha$ (hoặc $cos alpha$): Dùng $sin^2 alpha + cos^2 alpha = 1$. *Cực kỳ chú ý góc $alpha$ nhọn ($cos alpha > 0$) hay góc $alpha$ tù ($cos alpha < 0$)* để chọn dấu `+` hoặc `-` khi khai căn!
     - Nếu biết $tan alpha$ (hoặc $cot alpha$): Từ dấu của $tan alpha$ suy ra ngay dấu của $cos alpha$: $tan alpha > 0 arrow.r.double alpha$ nhọn ($cos alpha > 0$); $tan alpha < 0 arrow.r.double alpha$ tù ($cos alpha < 0$). Áp dụng $1 + tan^2 alpha = 1 / (cos^2 alpha)$ tìm $cos alpha$, rồi suy ra $sin alpha = tan alpha dot cos alpha$.
  2. *Dạng 2 (Câu 3 TLN): Cho $tan alpha = k$ (hoặc $cot alpha = k$), tính biểu thức đồng bậc $P$:*
     - *Loại phân thức bậc nhất:* $P = (a sin alpha + b cos alpha) / (c sin alpha + d cos alpha) = (a tan alpha + b) / (c tan alpha + d)$ *(chia cả tử và mẫu cho $cos alpha != 0$)*.
     - *Loại bậc hai:* $Q = (a sin^2 alpha + b sin alpha cos alpha + c cos^2 alpha) / (m sin^2 alpha + n cos^2 alpha) = (a tan^2 alpha + b tan alpha + c) / (m tan^2 alpha + n)$ *(chia cả tử và mẫu cho $cos^2 alpha$)*.
     - *Đặc biệt nếu mẫu không có lượng giác:* $M = a sin^2 alpha + b sin alpha cos alpha + c cos^2 alpha = (a sin^2 alpha + b sin alpha cos alpha + c cos^2 alpha) / (sin^2 alpha + cos^2 alpha) = (a tan^2 alpha + b tan alpha + c) / (tan^2 alpha + 1)$!
]

== Bài 6. Hệ thức lượng trong tam giác (Đơn vị 3.2 — 2,00 điểm: P.I, P.III & Câu 2 Tự luận)

#align(center)[#image("assets/triangle_theorems.svg", width: 98%)]

#theory-card("Phân loại chiến thuật Giải tam giác & Ứng dụng đo đạc thực tiễn (Câu 2 Tự luận — 1,0 điểm)")[
  - *Trường hợp 1 — Biết hai cạnh và góc xen giữa ($b, c, hat(A)$):*
    1. Dùng *Định lí Côsin* tính cạnh thứ ba: $a = sqrt(b^2 + c^2 - 2 b c cos A)$.
    2. Dùng hệ quả Côsin tính góc tiếp theo: $cos B = (a^2 + c^2 - b^2) / (2 a c) arrow.r.double hat(B)$, rồi $hat(C) = 180^circle - (hat(A) + hat(B))$.
    3. Tính diện tích nhanh bằng $S = 1/2 b c sin A$, từ đó suy ra $R = (a b c)/(4 S)$ và $h_a = (2 S)/a$.
  - *Trường hợp 2 — Biết một cạnh và hai góc ($a, hat(B), hat(C)$):*
    1. Tính ngay góc thứ ba: $hat(A) = 180^circle - (hat(B) + hat(C))$.
    2. Dùng *Định lí Sin* tính hai cạnh còn lại và bán kính $R$: $b = (a sin B)/(sin A)$, $c = (a sin C)/(sin A)$, $R = a / (2 sin A)$.
  - *Trường hợp 3 — Biết độ dài cả ba cạnh ($a, b, c$):*
    1. Dùng hệ quả Định lí Côsin để tìm các góc $hat(A), hat(B), hat(C)$.
    2. Tính nửa chu vi $p = (a + b + c)/2$ và dùng *công thức Heron* tính diện tích: $S = sqrt(p(p - a)(p - b)(p - c))$, suy ra $r = S/p$, $R = (a b c)/(4 S)$, $h_a = (2 S)/a$.
  #v(2pt)
  #align(center)[#image("assets/realworld_trig_models.svg", width: 88%)]
]

#trap-box("3 BẪY KINH ĐIỂN TRONG HỆ THỨC LƯỢNG TAM GIÁC")[
  #set text(size: 8.5pt)
  #set par(leading: 0.45em)
  1. *Nhầm dấu trừ thành dấu cộng trong Định lí Côsin:* $a^2 = b^2 + c^2 bold(- 2 b c cos A)$. Khi $hat(A) = 120^circle$, vì $cos 120^circle = -1/2 < 0$ nên $-2 b c cos 120^circle = +b c > 0$ (cạnh đối diện góc tù phải là cạnh lớn nhất!).
  2. *Góc nâng và tầm mắt người quan sát:* Nếu giác kế đặt cách mặt đất $h_0 = 1,5 "m"$, sau khi tính được chiều cao phần trên $C H'$, phải *cộng thêm $1,5 "m"$* mới ra chiều cao thật của tháp/cột cờ so với mặt đất!
  3. *Làm tròn trung gian quá sớm:* Trong bài toán thực tế nhiều bước (như Mô hình 2 đo chiều cao tháp), hãy giữ nguyên biểu thức chính xác hoặc lưu vào biến nhớ `A, B` trên Casio, *chỉ làm tròn ở kết quả cuối cùng*!
]

// ----------------------------------------------------------------------------
// CHƯƠNG IV: VECTƠ — BÀI 7: CÁC KHÁI NIỆM MỞ ĐẦU (0,50 ĐIỂM)
// ----------------------------------------------------------------------------
#chapter-banner(
  "CHƯƠNG IV",
  "VECTƠ — BÀI 7: CÁC KHÁI NIỆM MỞ ĐẦU",
  "Bài 7 SGK Kết nối tri thức Tập 1 (Giới hạn đúng Ma trận Giữa kì I)",
  "NẮM CHẮC TRỌN VẸN: 0,50 ĐIỂM (5%)"
)

== Bài 7. Các khái niệm mở đầu về vectơ (Đơn vị 4.1 — Câu 11, Câu 12 Phần I: 0,50 điểm)

#theory-card("Tổng hợp toàn bộ khái niệm, tính chất và cách đếm vectơ (Bài 7 SGK KNTT)")[
  #set text(size: 8.6pt)
  #set par(leading: 0.46em)
  - *Vectơ:* Là một đoạn thẳng có hướng. Kí hiệu $vt(A B)$ có điểm đầu $A$, điểm cuối $B$. Với hai điểm phân biệt $A, B$ tạo được *2 vectơ khác $vt(0)$* là $vt(A B)$ và $vt(B A)$ *(tổng quát: $n$ điểm phân biệt tạo được $n(n - 1)$ vectơ khác $vt(0)$)*.
  - *Giá của vectơ:* Đường thẳng đi qua điểm đầu và điểm cuối của vectơ ($A != B$).
  - *Hai vectơ cùng phương:* Giá của chúng *song song* hoặc *trùng nhau*. Ba điểm phân biệt $A, B, C$ thẳng hàng $arrow.l.r.double vt(A B)$ và $vt(A C)$ cùng phương. Hai vectơ cùng phương thì hoặc *cùng hướng*, hoặc *ngược hướng* (không cùng phương thì không xét hướng!).
  - *Độ dài vectơ:* $|vt(A B)| = A B >= 0$. Vectơ có độ dài bằng $1$ gọi là *vectơ đơn vị*.
  - *Hai vectơ bằng nhau & đối nhau:*
    - *Bằng nhau:* $vt(a) = vt(b) arrow.l.r.double$ cùng hướng *VÀ* cùng độ dài ($|vt(a)| = |vt(b)|$). Với điểm $O$ và $vt(a)$ cho trước, tồn tại *duy nhất* điểm $A$ sao cho $vt(O A) = vt(a)$.
    - *Đối nhau:* Ngược hướng *VÀ* cùng độ dài. Ví dụ $vt(B A)$ là vectơ đối của $vt(A B)$, kí hiệu $vt(B A) = -vt(A B)$.
  - *Vectơ-không $vt(0)$:* Điểm đầu trùng điểm cuối ($vt(A A) = vt(B B) = vt(0)$), có độ dài $|vt(0)| = 0$, và theo quy ước SGK *Kết nối tri thức*: *$vt(0)$ cùng phương và cùng hướng với mọi vectơ*.
  #v(1.5pt)
  #align(center)[#image("assets/vector_concepts_hex.svg", width: 82%)]
]

#trap-box("BẪY CÂU 11 – CÂU 12 PHẦN I (VECTƠ)")[
  #set text(size: 8.4pt)
  #set par(leading: 0.44em)
  - *Bẫy 1:* Trong tam giác đều $A B C$ cạnh $a$, $|vt(A B)| = |vt(A C)| = a$ nhưng *$vt(A B) != vt(A C)$* vì hai vectơ này không cùng phương (cắt nhau tại $A$)! Đừng nhầm $A B = A C$ (độ dài đoạn thẳng bằng nhau) với $vt(A B) = vt(A C)$!
  - *Bẫy 2:* Khi đếm “có bao nhiêu vectơ khác $vt(0)$ cùng phương với $vt(A B)$” tạo bởi các đỉnh hình lục giác đều $A B C D E F$ tâm $O$: nhớ đếm cả hai chiều trên mỗi đường thẳng song song/trùng với $A B$ và chú ý đề có tính điểm tâm $O$ hay chỉ tính 6 đỉnh lục giác, có trừ chính $vt(A B)$ ra hay không!
]

#pagebreak()
