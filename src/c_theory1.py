# -*- coding: utf-8 -*-
"""PHẦN I – KIẾN THỨC TRỌNG TÂM (Chương I và II)."""
from kit import *
from kit import _p


def chapter1():
    s = []
    s += h1("01", "MỆNH ĐỀ VÀ TẬP HỢP",
            "Chương I – SGK Toán 10 KNTT: Bài 1. Mệnh đề • Bài 2. Tập hợp và các phép toán trên tập hợp")

    # ---------------------------------------------------------------- 1.1
    s.append(h2("1.1. Mệnh đề. Mệnh đề chứa biến"))
    s.append(P("**Mệnh đề** là một câu khẳng định mà tính đúng, sai của nó xác định được. "
               "Một câu khẳng định đúng là **mệnh đề đúng**, một câu khẳng định sai là **mệnh đề sai**. "
               "Mỗi mệnh đề chỉ có thể đúng hoặc sai, không thể vừa đúng vừa sai."))
    s.append(P("Câu cảm thán, câu hỏi, câu cầu khiến, câu chưa xác định được tính đúng sai "
               "(chứa biến) **không** phải là mệnh đề. Chú ý rằng mệnh đề không nhất thiết phải là "
               "câu khẳng định đúng – ví dụ “$5$ là số chẵn” vẫn là một mệnh đề (mệnh đề sai)."))
    s.append(P("**Mệnh đề chứa biến** là câu khẳng định phụ thuộc vào một hay nhiều biến, "
               "mỗi khi gán giá trị cụ thể cho biến ta được một mệnh đề. Chẳng hạn "
               "$P(n)$: “$n$ chia hết cho $3$” là mệnh đề chứa biến; $P(6)$ đúng, $P(7)$ sai."))

    s.append(h3("a) Mệnh đề phủ định"))
    s.append(P("Mệnh đề phủ định của $P$, kí hiệu $\\overline{P}$ (đọc là “không phải $P$”), "
               "được tạo thành bằng cách thêm (hoặc bớt) từ “không” hay “không phải” vào trước vị ngữ của $P$. "
               "Tính chất: $P$ đúng thì $\\overline{P}$ sai và ngược lại."))
    s.extend(box(["$P$: “$√2$ là số hữu tỉ” (sai) → $\\overline{P}$: “$√2$ không phải là số hữu tỉ” (đúng).",
                  "$P$: “$∀x ∈ ℝ, x^(2) + 1 > 0$” → $\\overline{P}$: “$∃x ∈ ℝ, x^(2) + 1 ≤ 0$”."],
                 kind="box", title="Ví dụ"))

    s.append(h3("b) Mệnh đề kéo theo – điều kiện cần, điều kiện đủ"))
    s.append(P("Cho hai mệnh đề $P$ và $Q$. Mệnh đề “Nếu $P$ thì $Q$”, kí hiệu $P ⇒ Q$, "
               "gọi là **mệnh đề kéo theo**. Mệnh đề $P ⇒ Q$ **chỉ sai khi $P$ đúng và $Q$ sai**; "
               "trong mọi trường hợp còn lại nó đều đúng."))
    s.append(P("Nếu $P ⇒ Q$ đúng thì ta nói: $P$ là **điều kiện đủ** để có $Q$; "
               "$Q$ là **điều kiện cần** để có $P$. Cần phân biệt rõ hai cụm từ này vì đề bài rất hay hỏi."))

    s.append(h3("c) Mệnh đề đảo – mệnh đề tương đương"))
    s.append(P("Mệnh đề $Q ⇒ P$ gọi là **mệnh đề đảo** của $P ⇒ Q$. Mệnh đề đảo của một mệnh đề đúng "
               "**không nhất thiết** đúng."))
    s.append(P("Nếu cả $P ⇒ Q$ và $Q ⇒ P$ đều đúng thì $P$ và $Q$ là hai mệnh đề **tương đương**, "
               "kí hiệu $P ⇔ Q$ (đọc: “$P$ khi và chỉ khi $Q$”). Khi đó $P$ là **điều kiện cần và đủ** để có $Q$. "
               "Mệnh đề $P ⇔ Q$ đúng khi $P$ và $Q$ **cùng đúng hoặc cùng sai**."))

    s.append(h3("d) Kí hiệu ∀, ∃ và phủ định của chúng"))
    s.append(P("Kí hiệu $∀$ đọc là “với mọi”, $∃$ đọc là “tồn tại” (ít nhất một). "
               "Đây là hai kí hiệu bị hỏi nhiều nhất trong phần trắc nghiệm nhận biết."))
    s.append(data_table([
        ["Mệnh đề", "Mệnh đề phủ định"],
        ["$∀x ∈ X, P(x)$  (mọi $x$ đều có tính chất $P$)", "$∃x ∈ X, \\overline{P}(x)$  (có $x$ không có tính chất $P$)"],
        ["$∃x ∈ X, P(x)$", "$∀x ∈ X, \\overline{P}(x)$"],
        ["$∀x ∈ X, P(x) ⇒ Q(x)$", "$∃x ∈ X, P(x)$ và $\\overline{Q}(x)$"],
    ], widths=[78 * mm, None], align_center=False))

    s.extend(box(["**Sai lầm cần tránh.** Phủ định của “$∀x ∈ ℝ, x^(2) ≥ 0$” là “$∃x ∈ ℝ, x^(2) < 0$”, "
                  "**không phải** “$∀x ∈ ℝ, x^(2) < 0$”. Dấu $∀$ đổi thành $∃$ và bất đẳng thức đổi chiều.",
                  "“$x^(2) > 4$” không phải mệnh đề (còn chứa biến); “$x^(2) > 4, ∀x ∈ ℝ$” mới là mệnh đề "
                  "(và là mệnh đề sai, vì $x = 0$)."],
                 kind="box_warn", title="Lỗi thường gặp"))

    # ---------------------------------------------------------------- 1.2
    s.append(h2("1.2. Tập hợp"))
    s.append(P("Tập hợp được xác định bằng hai cách: **liệt kê** các phần tử của nó, hoặc **chỉ ra tính chất "
               "đặc trưng** cho các phần tử của nó. Kí hiệu $x ∈ A$ (phần tử thuộc tập hợp), "
               "$x ∉ A$ (không thuộc). Tập hợp không có phần tử nào gọi là **tập rỗng**, kí hiệu $∅$."))
    s.append(P("**Tập con:** $A ⊂ B$ nếu mọi phần tử của $A$ đều là phần tử của $B$. "
               "Quy ước $∅ ⊂ A$ với mọi tập hợp $A$ và $A ⊂ A$. "
               "**Hai tập hợp bằng nhau:** $A = B ⇔ A ⊂ B$ và $B ⊂ A$, nghĩa là chúng có đúng cùng các phần tử."))

    s.append(h3("a) Các tập số thường dùng"))
    s.append(data_table([
        ["Kí hiệu", "Tên gọi", "Ghi nhớ nhanh"],
        ["$ℕ$", "Tập các số tự nhiên", "$0; 1; 2; 3; …$"],
        ["$ℕ^*$", "Tập các số tự nhiên khác $0$", "$1; 2; 3; …$"],
        ["$ℤ$", "Tập các số nguyên", "$…; −2; −1; 0; 1; 2; …$"],
        ["$ℚ$", "Tập các số hữu tỉ", "số viết được dạng $a/b$ với $a, b ∈ ℤ, b ≠ 0$"],
        ["$ℝ$", "Tập các số thực", "gồm cả số vô tỉ như $√2, π$"],
    ], widths=[20 * mm, 62 * mm, None], align_center=True))
    s.append(P("Ta có $ℕ^* ⊂ ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ$. Riêng $ℝ$ được biểu diễn bằng trục số: "
               "mỗi số thực ứng với đúng một điểm trên trục số và ngược lại."))

    s.append(h3("b) Các tập con thường dùng của ℝ (khoảng – đoạn – nửa khoảng)"))
    s.append(data_table([
        ["Kí hiệu", "Đọc là", "Điều kiện", "Bờ"],
        ["$(a; b)$", "khoảng $(a; b)$", "$a < x < b$", "không lấy hai đầu mút"],
        ["$[a; b]$", "đoạn $[a; b]$", "$a ≤ x ≤ b$", "lấy cả hai đầu mút"],
        ["$[a; b)$", "nửa khoảng $[a; b)$", "$a ≤ x < b$", "lấy $a$, không lấy $b$"],
        ["$(a; b]$", "nửa khoảng $(a; b]$", "$a < x ≤ b$", "lấy $b$, không lấy $a$"],
        ["$(−∞; a)$", "khoảng $(−∞; a)$", "$x < a$", "không lấy $a$"],
        ["$(−∞; a]$", "nửa khoảng $(−∞; a]$", "$x ≤ a$", "lấy $a$"],
        ["$(a; +∞)$", "khoảng $(a; +∞)$", "$x > a$", "không lấy $a$"],
        ["$[a; +∞)$", "nửa khoảng $[a; +∞)$", "$x ≥ a$", "lấy $a$"],
        ["$(−∞; +∞)$", "khoảng $(−∞; +∞)$", "$x ∈ ℝ$", "chính là $ℝ$"],
    ], widths=[24 * mm, 52 * mm, 40 * mm, None], align_center=True))
    s.extend(box(["**Mẹo nhớ:** dấu **ngoặc tròn** “(“ luôn đi với dấu **so sánh nghiêm ngặt** ($<$, $>$), "
                  "dấu **ngoặc vuông** “[” luôn đi với dấu **có dấu bằng** ($≤$, $≥$). "
                  "Hai đầu $−∞$ và $+∞$ **luôn** viết ngoặc tròn.",
                  "Khi biểu diễn trên trục số: đầu mút **không lấy** vẽ bằng dấu ngoặc tròn (○) và tô "
                  "phần bên trong, đầu mút **lấy** vẽ bằng ngoặc vuông (●)."],
                 kind="box_tip", title="Ghi nhớ & mẹo"))
    s.extend(figure("f1_numberline.png", 148,
                    "Hình 1. Cách biểu diễn $A = [−3; 5)$, $B = [1; +∞)$ và giao $A ∩ B = [1; 5)$ trên trục số. "
                    "Đầu mút **không lấy** vẽ bằng vòng tròn rỗng, đầu mút **lấy** vẽ bằng chấm đặc."))

    s.append(h3("c) Số tập con của một tập hợp hữu hạn"))
    s.append(P("Một tập hợp có $n$ phần tử ($n ∈ ℕ$) thì có $2^(n)$ tập con, trong đó có $1$ tập rỗng, "
               "$n$ tập con có đúng $1$ phần tử, và $2^(n) − 1$ tập con khác rỗng. "
               "Số tập con có đúng $k$ phần tử là $C_n^k$ (tổ hợp chập $k$ của $n$)."))
    s.extend(box(["Tập $A = {a; b; c}$ có $3$ phần tử nên có $2^(3) = 8$ tập con: $∅$, ${a}$, ${b}$, ${c}$, "
                  "${a; b}$, ${a; c}$, ${b; c}$, ${a; b; c}$.",
                  "Tập $A$ có $5$ phần tử có $2^(5) = 32$ tập con; trong đó có $C_5^2 = 10$ tập con gồm đúng $2$ phần tử."],
                 kind="box", title="Ví dụ"))

    # ---------------------------------------------------------------- 1.3
    s.append(h2("1.3. Các phép toán trên tập hợp"))
    s.append(P("Cho hai tập hợp $A$ và $B$ (đều là tập con của một tập nền $X$). Ta định nghĩa:"))
    s.append(data_table([
        ["Phép toán", "Kí hiệu", "Định nghĩa", "Đọc là"],
        ["Giao", "$A ∩ B$", "${x \\;|\\; x ∈ A$ và $x ∈ B}$", "giao của $A$ và $B$"],
        ["Hợp", "$A ∪ B$", "${x \\;|\\; x ∈ A$ hoặc $x ∈ B}$", "hợp của $A$ và $B$"],
        ["Hiệu", "$A \\setminus B$", "${x \\;|\\; x ∈ A$ và $x ∉ B}$", "$A$ trừ $B$"],
        ["Phần bù", "$C_X A$", "$X \\setminus A$ (với $A ⊂ X$)", "phần bù của $A$ trong $X$"],
    ], widths=[22 * mm, 24 * mm, 60 * mm, None], align_center=True))
    s.append(P("Trên biểu đồ Ven: $A ∩ B$ là phần **chung** của hai hình; $A ∪ B$ là toàn bộ phần "
               "**bị tô bởi ít nhất một** trong hai hình; $A \\setminus B$ là phần thuộc $A$ nhưng "
               "**nằm ngoài** $B$. Phần bù $C_X A$ chỉ được xác định khi nói rõ tập nền $X$."))
    s.extend(box(["**Công thức đếm số phần tử (rất hay dùng cho bài toán thực tế):**",
                  "Với hai tập hữu hạn: $|A ∪ B| = |A| + |B| − |A ∩ B|$.",
                  "Với ba tập hữu hạn: $|A ∪ B ∪ C| = |A| + |B| + |C| − |A ∩ B| − |B ∩ C| − |C ∩ A| + |A ∩ B ∩ C|$.",
                  "Số phần tử **không** thuộc $A$ trong tập nền $X$ là $|X| − |A|$."],
                 kind="box_tip", title="Công thức quan trọng"))

    s.append(h3("Ví dụ mẫu có lời giải"))
    s.append(P("**Ví dụ 1.** Cho $A = {x ∈ ℕ \\;|\\; x < 6}$, $B = {x ∈ ℕ \\;|\\; x$ là số chẵn, $x ≤ 8}$. "
               "Xác định $A$, $B$, $A ∩ B$, $A ∪ B$, $A \\setminus B$ và $B \\setminus A$."))
    s.extend(answer([
        "Liệt kê: $A = {0; 1; 2; 3; 4; 5}$ và $B = {0; 2; 4; 6; 8}$.",
        "$A ∩ B = {0; 2; 4}$.",
        "$A ∪ B = {0; 1; 2; 3; 4; 5; 6; 8}$ (chú ý mỗi phần tử chỉ viết một lần, sắp theo thứ tự tăng dần).",
        "$A \\setminus B = {1; 3; 5}$; $B \\setminus A = {6; 8}$. Hai kết quả này **khác nhau**, "
        "nên không được viết $A \\setminus B = B \\setminus A$.",
    ]))

    s.append(P("**Ví dụ 2.** Cho $A = [−2; 5)$, $B = (1; +∞)$. Tìm $A ∩ B$, $A ∪ B$, $A \\setminus B$ và $C_ℝ B$."))
    s.extend(answer([
        "Vẽ hai tập trên trục số rồi “chồng” chúng lên nhau:",
        "$A ∩ B = (1; 5)$ — chỉ giữ phần nằm trong **cả** hai tập (bỏ đầu mút $1$ vì $1 ∉ A$).",
        "$A ∪ B = [−2; +∞)$ — lấy phần thuộc **ít nhất một** tập; vì $B$ kéo dài tới $+∞$ và $A$ bắt đầu từ $−2$ nên hợp là nửa khoảng $[−2; +∞)$.",
        "$A \\setminus B = [−2; 1]$ — phần của $A$ nằm bên trái $1$, **lấy cả** điểm $1$ vì $1 ∉ B$.",
        "$C_ℝ B = ℝ \\setminus B = (−∞; 1]$ — phần bù trong $ℝ$ gồm các số **không** lớn hơn $1$, và lấy cả $1$.",
    ]))

    s.append(P("**Ví dụ 3.** Lớp 10A có $45$ học sinh. Trong đó $28$ bạn thích môn Toán, $22$ bạn thích môn Ngữ văn, "
               "$12$ bạn thích cả hai môn. Hỏi có bao nhiêu bạn không thích môn nào trong hai môn đó?"))
    s.extend(answer([
        "Gọi $T$, $V$ lần lượt là tập học sinh thích Toán, thích Văn. Số bạn thích ít nhất một môn là "
        "$|T ∪ V| = |T| + |V| − |T ∩ V| = 28 + 22 − 12 = 38$.",
        "Số bạn không thích môn nào là $45 − 38 = 7$ (bạn).",
        "**Nhận xét:** nếu chỉ cộng $28 + 22 = 50 > 45$ thì đã đếm hai lần nhóm thích cả hai môn – "
        "đó chính là lí do phải trừ đi $|T ∩ V|$.",
    ]))
    return s


def chapter2():
    s = []
    s += h1("02", "BẤT PHƯƠNG TRÌNH VÀ HỆ BẤT PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN",
            "Chương II – SGK Toán 10 KNTT: Bài 3. Bất phương trình bậc nhất hai ẩn • Bài 4. Hệ bất phương trình bậc nhất hai ẩn")

    s.append(h2("2.1. Bất phương trình bậc nhất hai ẩn"))
    s.append(P("**Bất phương trình bậc nhất hai ẩn** $x, y$ có dạng tổng quát "
               "$ax + by ≤ c$ (hoặc $ax + by ≥ c$, $ax + by < c$, $ax + by > c$), trong đó "
               "$a, b, c$ là các số thực đã cho, $a$ và $b$ **không đồng thời bằng $0$**, còn $x, y$ là hai ẩn."))
    s.append(P("Mỗi cặp số $(x_0; y_0)$ thoả mãn bất phương trình được gọi là một **nghiệm** của bất phương trình đó. "
               "Trong mặt phẳng toạ độ $Oxy$, tập hợp các điểm có toạ độ là nghiệm của bất phương trình "
               "gọi là **miền nghiệm** của nó."))
    s.extend(box(["**Nhận biết nhanh:** biểu thức chỉ có $x$, $y$ ở **bậc nhất** và không có tích $xy$, "
                  "không có $x^(2)$, $y^(2)$, không có ẩn ở mẫu, không có căn của ẩn.",
                  "Ví dụ: $2x − 3y + 1 ≤ 0$ là bất phương trình bậc nhất hai ẩn; "
                  "$x^(2) + y > 1$, $xy ≥ 2$, $1/x + y < 3$ **không phải**."],
                 kind="box_tip", title="Ghi nhớ"))

    s.append(h3("Quy tắc biểu diễn miền nghiệm (3 bước)"))
    s.append(P("Xét bất phương trình $ax + by + c ≤ 0$ (các dấu khác làm hoàn toàn tương tự)."))
    s.extend(steps([
        "**Bước 1.** Vẽ đường thẳng $Δ: ax + by + c = 0$ trong mặt phẳng toạ độ (chỉ cần xác định hai điểm phân biệt thuộc $Δ$, thường là hai giao điểm với các trục toạ độ).",
        "**Bước 2.** Lấy một điểm $M_0(x_0; y_0)$ **không thuộc** $Δ$ (thường chọn gốc $O(0; 0)$ cho nhanh) và tính $ax_0 + by_0 + c$.",
        "**Bước 3.** Nếu $ax_0 + by_0 + c ≤ 0$ thì miền nghiệm là nửa mặt phẳng **chứa** $M_0$ (kể cả bờ $Δ$ vì có dấu “=”), ngược lại là nửa mặt phẳng **không chứa** $M_0$.",
    ]))
    s.extend(box(["**Quy ước vẽ bờ:** bất phương trình có dấu $≤$ hoặc $≥$ → miền nghiệm **kể cả bờ**, vẽ $Δ$ bằng "
                  "**nét liền**. Bất phương trình có dấu $<$ hoặc $>$ → miền nghiệm **không kể bờ**, vẽ $Δ$ bằng "
                  "**nét đứt** (nét đứt cũng là dấu hiệu để giám khảo chấm điểm hình vẽ).",
                  "**Cách nhanh:** nếu $b ≠ 0$, từ $ax + by + c ≤ 0$ suy ra $y ≤ −(a/b)x − c/b$ (khi $b > 0$), "
                  "tức miền nghiệm nằm **phía dưới** đường thẳng; khi $b < 0$ thì ngược lại."],
                 kind="box_warn", title="Lưu ý khi vẽ"))

    s.append(h3("Ví dụ mẫu có lời giải"))
    s.append(P("**Ví dụ 1.** Biểu diễn miền nghiệm của bất phương trình $2x + y − 4 ≤ 0$."))
    s.extend(answer([
        "Vẽ $Δ: 2x + y − 4 = 0$. Cho $y = 0 ⇒ x = 2$; cho $x = 0 ⇒ y = 4$. Vậy $Δ$ đi qua $A(2; 0)$ và $B(0; 4)$.",
        "Chọn $O(0; 0) ∉ Δ$: ta có $2·0 + 0 − 4 = −4 ≤ 0$ nên $O$ **thuộc** miền nghiệm.",
        "Vậy miền nghiệm là nửa mặt phẳng bờ $Δ$ (kể cả $Δ$) **chứa gốc toạ độ $O$** — chính là nửa mặt phẳng "
        "nằm phía dưới đường thẳng trong hình vẽ.",
    ]))
    s.extend(figure("f2_halfplane.png", 82,
                    "Hình 2. Miền nghiệm của $2x + y − 4 ≤ 0$ là nửa mặt phẳng bờ $Δ$, kể cả bờ, chứa $O(0; 0)$."))

    # ---------------------------------------------------------------- 2.2
    s.append(h2("2.2. Hệ bất phương trình bậc nhất hai ẩn"))
    s.append(P("**Hệ bất phương trình bậc nhất hai ẩn** là một hệ gồm hai hay nhiều bất phương trình bậc nhất hai ẩn. "
               "Mỗi cặp số $(x_0; y_0)$ thoả mãn **tất cả** các bất phương trình của hệ gọi là một **nghiệm** của hệ. "
               "**Miền nghiệm** của hệ là giao các miền nghiệm của từng bất phương trình trong hệ."))
    s.extend(steps([
        "Biểu diễn miền nghiệm của **từng** bất phương trình trên cùng một mặt phẳng toạ độ.",
        "Phần **chung** (giao) của các miền vừa tìm là miền nghiệm của hệ — thường là một miền **đa giác** "
        "(tam giác, tứ giác, ngũ giác…) có thể bị chặn hoặc không bị chặn.",
        "Xác định toạ độ các **đỉnh** của miền đa giác bằng cách giải hệ phương trình tạo bởi hai đường thẳng biên cắt nhau.",
    ]))

    s.append(h3("Bài toán tối ưu (quy hoạch tuyến tính) – dạng Vận dụng cao của đề"))
    s.append(P("Cho biểu thức $F(x; y) = ax + by$ xác định trên một miền đa giác (miền nghiệm của một hệ bất phương trình). "
               "Bài toán yêu cầu tìm giá trị **lớn nhất** hoặc **nhỏ nhất** của $F$."))
    s.extend(steps([
        "**Bước 1.** Đặt ẩn $x, y$ cho hai đại lượng cần tìm, kèm điều kiện $x ≥ 0$, $y ≥ 0$ (hoặc điều kiện tự nhiên khác).",
        "**Bước 2.** Chuyển các điều kiện ràng buộc của bài toán thành một **hệ bất phương trình** bậc nhất hai ẩn (nguồn nguyên liệu, thời gian, số tiền, khối lượng…). Lập biểu thức mục tiêu $F(x; y)$.",
        "**Bước 3.** Vẽ miền nghiệm (miền đa giác) và xác định toạ độ các đỉnh.",
        "**Bước 4.** Tính $F$ tại **tất cả** các đỉnh rồi so sánh. Giá trị lớn nhất (nhỏ nhất) của $F$ trên miền đa giác đạt được tại một trong các đỉnh.",
    ]))
    s.extend(box(["**Vì sao chỉ cần thử ở các đỉnh?** Trên mỗi cạnh của đa giác, $F$ là hàm bậc nhất của một biến nên "
                  "đơn điệu – giá trị lớn nhất và nhỏ nhất chỉ có thể rơi vào hai đầu mút, tức các đỉnh. "
                  "Do đó chỉ cần lập **bảng giá trị tại các đỉnh** là đủ kết luận.",
                  "**Lưu ý khi kết luận:** phải kiểm tra điều kiện nguyên (số áo, số xe, số người… là số tự nhiên) và "
                  "trả lời đúng câu hỏi (giá trị lớn nhất của $F$ hay số lượng $x, y$)."],
                 kind="box_tip", title="Ghi nhớ"))

    s.append(P("**Ví dụ 2.** Một xưởng may sản xuất hai loại áo $A$ và $B$. Mỗi áo loại $A$ cần $2$ m vải và "
               "$4$ giờ công; mỗi áo loại $B$ cần $3$ m vải và $3$ giờ công. Xưởng có $240$ m vải và "
               "$300$ giờ công. Lợi nhuận thu được là $200$ nghìn đồng cho mỗi áo loại $A$ và $250$ nghìn đồng "
               "cho mỗi áo loại $B$. Hỏi xưởng cần may bao nhiêu áo mỗi loại để lợi nhuận lớn nhất?"))
    s.extend(figure("f3b_coat.png", 72,
                    "Hình 3. Miền nghiệm của hệ (phần tô màu) là tứ giác $OMPN$ với $O(0; 0)$, $M(75; 0)$, "
                    "$N(0; 80)$, $P(30; 60)$ — bốn đỉnh cần thử giá trị của $F$."))
    s.extend(answer([
        "Gọi $x, y$ lần lượt là số áo loại $A$ và loại $B$ cần may ($x, y ∈ ℕ$).",
        "Ràng buộc vải: $2x + 3y ≤ 240$. Ràng buộc giờ công: $4x + 3y ≤ 300$. Điều kiện: $x ≥ 0, y ≥ 0$.",
        "Lợi nhuận $F(x; y) = 200x + 250y$ (nghìn đồng). Ta cần tìm giá trị lớn nhất của $F$ trên miền nghiệm của hệ "
        "$\\{2x + 3y ≤ 240;\\; 4x + 3y ≤ 300;\\; x ≥ 0;\\; y ≥ 0\\}$.",
        "Vẽ các đường biên và tìm đỉnh của miền đa giác $O(0; 0)$, $M(75; 0)$, $N(0; 80)$, $P(30; 60)$ — trong đó $P$ là "
        "giao điểm của hai đường $2x + 3y = 240$ và $4x + 3y = 300$ (trừ vế theo vế được $2x = 60 ⇒ x = 30$, "
        "suy ra $y = 60$).",
        "Tính $F$: $F(O) = 0$; $F(M) = 200·75 = 15\\,000$; $F(N) = 250·80 = 20\\,000$; $F(P) = 200·30 + 250·60 = "
        "6\\,000 + 15\\,000 = 21\\,000$.",
        "So sánh: $F$ lớn nhất bằng $21\\,000$ (nghìn đồng) $= 21$ triệu đồng, đạt tại $x = 30$, $y = 60$.",
        "**Kết luận:** may $30$ áo loại $A$ và $60$ áo loại $B$ để lợi nhuận lớn nhất là $21$ triệu đồng.",
    ]))
    return s
