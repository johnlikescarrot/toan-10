# -*- coding: utf-8 -*-
"""PHẦN I – KIẾN THỨC TRỌNG TÂM (Chương III và IV)."""
from kit import *
from kit import _p


def chapter3():
    s = []
    s += h1("03", "HỆ THỨC LƯỢNG TRONG TAM GIÁC",
            "Chương III – SGK Toán 10 KNTT: Bài 5. Giá trị lượng giác của một góc từ 0° đến 180° • Bài 6. Hệ thức lượng trong tam giác")

    s.append(h2("3.1. Giá trị lượng giác của một góc từ 0° đến 180°"))
    s.append(P("Trong mặt phẳng toạ độ $Oxy$, lấy nửa đường tròn đơn vị (tâm $O$, bán kính $1$) nằm phía trên trục "
               "$Ox$. Với mỗi góc $α$ có $0° ≤ α ≤ 180°$, có duy nhất điểm $M(x_0; y_0)$ trên nửa đường tròn đó sao cho "
               "$\\widehat{xOM} = α$. Khi đó:"))
    s.append(data_table([
        ["Giá trị lượng giác", "Định nghĩa", "Điều kiện xác định"],
        ["$sin α$", "$y_0$ (tung độ của $M$)", "luôn xác định"],
        ["$cos α$", "$x_0$ (hoành độ của $M$)", "luôn xác định"],
        ["$tan α$", "$y_0 / x_0$", "$α ≠ 90°$"],
        ["$cot α$", "$x_0 / y_0$", "$α ≠ 0°$ và $α ≠ 180°$"],
    ], widths=[34 * mm, 62 * mm, None], align_center=True))
    s.append(P("Với mọi góc $α$ ta luôn có $−1 ≤ sin α ≤ 1$ và $−1 ≤ cos α ≤ 1$. "
               "**Dấu** của các giá trị lượng giác phụ thuộc vào $α$ là góc nhọn hay góc tù:"))

    s.append(data_table([
        ["Góc $α$", "$sin α$", "$cos α$", "$tan α$", "$cot α$"],
        ["$0° < α < 90°$ (nhọn)", "$+$", "$+$", "$+$", "$+$"],
        ["$α = 90°$", "$1$", "$0$", "không xác định", "$0$"],
        ["$90° < α < 180°$ (tù)", "$+$", "$−$", "$−$", "$−$"],
        ["$α = 0°$", "$0$", "$1$", "$0$", "không xác định"],
        ["$α = 180°$", "$0$", "$−1$", "$0$", "không xác định"],
    ], widths=[52 * mm, 25 * mm, 25 * mm, 33 * mm, None], align_center=True))
    s.extend(box(["**Mẹo nhớ dấu:** góc nhọn thì **tất cả dương**; góc tù thì **chỉ sin dương** "
                  "(cos, tan, cot đều âm). Lí do: điểm $M$ ở góc phần tư thứ hai có hoành độ âm, tung độ dương."],
                 kind="box_tip", title="Ghi nhớ"))

    s.append(h3("a) Giá trị lượng giác của các góc đặc biệt"))
    s.append(data_table([
        ["$α$", "$0°$", "$30°$", "$45°$", "$60°$", "$90°$", "$120°$", "$135°$", "$150°$", "$180°$"],
        ["$sin α$", "$0$", "$1/2$", "$√2/2$", "$√3/2$", "$1$", "$√3/2$", "$√2/2$", "$1/2$", "$0$"],
        ["$cos α$", "$1$", "$√3/2$", "$√2/2$", "$1/2$", "$0$", "$−1/2$", "$−√2/2$", "$−√3/2$", "$−1$"],
        ["$tan α$", "$0$", "$√3/3$", "$1$", "$√3$", "‖", "$−√3$", "$−1$", "$−√3/3$", "$0$"],
        ["$cot α$", "‖", "$√3$", "$1$", "$√3/3$", "$0$", "$−√3/3$", "$−1$", "$−√3$", "‖"],
    ], widths=[17 * mm] + [14.6 * mm] * 9, align_center=True))
    s.append(P("Kí hiệu “‖” nghĩa là giá trị lượng giác đó **không xác định** tại góc tương ứng."))

    s.append(h3("b) Hai góc bù nhau, hai góc phụ nhau"))
    s.append(data_table([
        ["Liên hệ", "Công thức"],
        ["Hai góc **bù** nhau: $α$ và $180° − α$",
         "$sin(180° − α) = sin α$;  $cos(180° − α) = −cos α$;  $tan(180° − α) = −tan α$;  $cot(180° − α) = −cot α$"],
        ["Hai góc **phụ** nhau: $α$ và $90° − α$",
         "$sin(90° − α) = cos α$;  $cos(90° − α) = sin α$;  $tan(90° − α) = cot α$;  $cot(90° − α) = tan α$"],
    ], widths=[52 * mm, None], align_center=False))
    s.extend(box(["**Cách nhớ nhanh:** hai góc bù nhau thì **sin giữ nguyên, cos và tan đổi dấu**. "
                  "Nhờ đó $sin 150° = sin 30° = 1/2$ nhưng $cos 150° = −cos 30° = −√3/2$.",
                  "Đây cũng là chìa khoá để tra bảng giá trị lượng giác: mọi góc tù đều đưa được về góc nhọn bù với nó."],
                 kind="box_tip", title="Ghi nhớ"))

    s.append(h3("c) Các hệ thức lượng giác cơ bản"))
    s.append(formula("$sin^(2) α + cos^(2) α = 1$"))
    s.append(formula("$tan α = sin α / cos α$ (khi $cos α ≠ 0$)  ;  $cot α = cos α / sin α$ (khi $sin α ≠ 0$)  ;  $tan α · cot α = 1$"))
    s.append(formula("$1 + tan^(2) α = 1 / cos^(2) α$ (khi $cos α ≠ 0$)  ;  $1 + cot^(2) α = 1 / sin^(2) α$ (khi $sin α ≠ 0$)"))
    s.append(P("Hai hệ thức cuối rất hữu ích khi đề cho $tan α$ hoặc $cot α$ mà phải tìm $sin α$, $cos α$."))

    s.append(h3("d) Dùng máy tính cầm tay"))
    s.extend(steps([
        "Chuyển máy sang đơn vị **độ** (màn hình hiện chữ **D** hoặc **DEG**). Nếu quên bước này, kết quả sẽ sai hoàn toàn.",
        "Tính $sin$, $cos$, $tan$: bấm phím tương ứng rồi nhập số đo góc.",
        "Tính $cot α$: không có phím $cot$, hãy bấm $1 ÷ tan α$ (nhớ $α ≠ 0°, 180°$).",
        "Tìm góc khi biết giá trị lượng giác: dùng $sin^(−1)$, $cos^(−1)$, $tan^(−1)$ (SHIFT + sin/cos/tan).",
    ]))
    s.extend(box(["**Ví dụ:** $sin 120° ≈ 0,8660$; $cos 135° ≈ −0,7071$; $cot 40° = 1/tan 40° ≈ 1,1918$.",
                  "Kết quả âm là bình thường với góc tù – không được tự ý bỏ dấu trừ."],
                 kind="box", title="Minh hoạ"))

    s.append(h3("e) Dạng toán: cho một giá trị lượng giác, tính giá trị biểu thức"))
    s.append(P("**Phương pháp.** Dùng $sin^(2) α + cos^(2) α = 1$ (hoặc $1 + tan^(2) α = 1/cos^(2) α$) để suy ra giá trị lượng giác "
               "còn thiếu, rồi thay vào biểu thức cần tính. **Bắt buộc** phải xét dấu theo điều kiện của góc: góc nhọn thì "
               "$cos α > 0$, góc tù thì $cos α < 0$ và $tan α < 0$."))
    s.append(P("**Ví dụ.** Cho $sin α = 3/5$ với $90° < α < 180°$. Tính $cos α$, $tan α$ và giá trị của "
               "$A = 3 sin α + 2 cos α$."))
    s.extend(answer([
        "Từ $sin^(2) α + cos^(2) α = 1$ suy ra $cos^(2) α = 1 − (3/5)^(2) = 16/25$, nên $cos α = ±4/5$.",
        "Vì $90° < α < 180°$ nên $cos α < 0$, do đó $cos α = −4/5$.",
        "$tan α = sin α / cos α = (3/5) : (−4/5) = −3/4$.",
        "$A = 3·(3/5) + 2·(−4/5) = 9/5 − 8/5 = 1/5$.",
    ]))

    # ---------------------------------------------------------------- 3.2
    s.append(h2("3.2. Hệ thức lượng trong tam giác"))
    s.append(P("Xét tam giác $ABC$ có các cạnh $a = BC$, $b = CA$, $c = AB$ (cạnh đối diện với góc $A$, $B$, $C$ tương ứng); "
               "$R$ là bán kính đường tròn ngoại tiếp, $r$ là bán kính đường tròn nội tiếp, $p = (a + b + c)/2$ là nửa chu vi, "
               "$S$ là diện tích, $m_a$ là độ dài đường trung tuyến kẻ từ $A$."))

    s.extend(figure("f4_triangle.png", 62,
                    "Hình 4. Tam giác $ABC$ với $a = BC$, $b = CA$, $c = AB$ — cạnh $a$ đối diện góc $A$, …"))

    s.append(h3("a) Định lí côsin"))
    s.append(formula("$a^(2) = b^(2) + c^(2) − 2bc·cos A$  ;  $b^(2) = c^(2) + a^(2) − 2ca·cos B$  ;  $c^(2) = a^(2) + b^(2) − 2ab·cos C$"))
    s.append(P("**Hệ quả** (dùng để tìm góc khi biết ba cạnh):"))
    s.append(formula("$cos A = (b^(2) + c^(2) − a^(2)) / (2bc)$  ;  $cos B = (c^(2) + a^(2) − b^(2)) / (2ca)$  ;  $cos C = (a^(2) + b^(2) − c^(2)) / (2ab)$"))
    s.append(P("Khi $A = 90°$ thì $cos A = 0$ và định lí côsin trở về **định lí Pythagore** $a^(2) = b^(2) + c^(2)$. "
               "Như vậy định lí Pythagore chỉ là trường hợp riêng của định lí côsin."))

    s.append(h3("b) Định lí sin"))
    s.append(formula("$a / sin A = b / sin B = c / sin C = 2R$"))
    s.append(P("Từ đó $a = 2R·sin A$, $sin A = a/(2R)$ … Định lí sin đặc biệt hữu ích khi biết một cạnh và hai góc, "
               "hoặc khi cần tìm bán kính đường tròn ngoại tiếp."))

    s.append(h3("c) Công thức tính diện tích tam giác"))
    s.append(data_table([
        ["Công thức", "Ý nghĩa", "Dùng khi biết"],
        ["$S = ½·a·h_a$", "nửa tích cạnh và chiều cao tương ứng", "một cạnh và chiều cao"],
        ["$S = ½·a·b·sin C = ½·b·c·sin A = ½·c·a·sin B$", "nửa tích hai cạnh và sin góc xen giữa", "hai cạnh và góc xen giữa"],
        ["$S = a·b·c / (4R)$", "qua bán kính ngoại tiếp", "ba cạnh và $R$"],
        ["$S = p·r$", "qua nửa chu vi và bán kính nội tiếp", "nửa chu vi và $r$"],
        ["$S = √(p(p − a)(p − b)(p − c))$", "công thức Heron", "ba cạnh"],
    ], widths=[62 * mm, 52 * mm, None], align_center=False))

    s.append(h3("d) Độ dài đường trung tuyến"))
    s.append(formula("$m_a^(2) = (2b^(2) + 2c^(2) − a^(2)) / 4$  ;  $m_b^(2) = (2c^(2) + 2a^(2) − b^(2)) / 4$  ;  $m_c^(2) = (2a^(2) + 2b^(2) − c^(2)) / 4$"))

    s.append(h3("e) Quy trình giải tam giác"))
    s.append(data_table([
        ["Dữ kiện đã biết", "Công cụ nên dùng", "Thứ tự tính"],
        ["Ba cạnh $a, b, c$", "Định lí côsin (hệ quả) + Heron", "tính góc lớn nhất trước (đối diện cạnh lớn nhất), rồi góc thứ hai, góc còn lại $= 180° − …$"],
        ["Hai cạnh và góc xen giữa (ví dụ $b, c, A$)", "Định lí côsin rồi định lí sin", "$a$ trước, sau đó $B$ hoặc $C$, cuối cùng góc còn lại"],
        ["Một cạnh và hai góc (ví dụ $a, B, C$)", "Định lí sin", "$A = 180° − B − C$, rồi $b$, $c$"],
        ["Hai cạnh và góc **không** xen giữa", "Định lí sin (có thể có 0, 1 hoặc 2 nghiệm hình)", "xét cẩn thận khả năng góc tù"],
    ], widths=[52 * mm, 52 * mm, None], align_center=False))

    s.append(h3("f) Ứng dụng thực tiễn"))
    s.append(P("Các bài toán đo đạc thường được mô hình hoá thành một tam giác: hai điểm đã biết khoảng cách và hai góc "
               "nhìn (bài toán **giao hội**), hoặc một điểm không tới được. Khi đó:"))
    s.extend(steps([
        "Vẽ hình, đặt tên các điểm $A, B, C$ và xác định rõ đại lượng cần tìm là **cạnh** hay **góc** của tam giác nào.",
        "Góc thứ ba $= 180°$ trừ tổng hai góc đã biết (tổng ba góc trong tam giác bằng $180°$).",
        "Chọn định lí phù hợp: có **góc xen giữa hai cạnh** → định lí côsin; có **một cạnh và hai góc** → định lí sin.",
        "Nếu bài toán có chiều cao vuông góc (tháp, cột), tách thành hai tam giác vuông và dùng tỉ số lượng giác.",
    ]))
    s.extend(box(["**Lưu ý trình bày:** nêu rõ đơn vị và làm tròn theo yêu cầu đề (thường 2 chữ số thập phân), "
                  "ghi kết luận bằng câu văn “Vậy khoảng cách … là … m”."],
                 kind="box_warn", title="Lỗi thường gặp"))

    s.append(P("**Ví dụ.** Từ hai vị trí $A$ và $B$ cách nhau $100$ m trên bờ, người ta quan sát một điểm $C$ ở bên kia sông. "
               "Biết $\\widehat{BAC} = 45°$ và $\\widehat{ABC} = 70°$. Tính khoảng cách từ $A$ đến $C$ (làm tròn đến hàng phần trăm)."))
    s.extend(answer([
        "Trong tam giác $ABC$: $\\widehat{C} = 180° − 45° − 70° = 65°$.",
        "Theo định lí sin: $AC / sin B = AB / sin C$, suy ra $AC = AB·sin B / sin C = 100·sin 70° / sin 65°$.",
        "$AC ≈ 100 · 0,9397 / 0,9063 ≈ 103,68$ (m).",
        "Vậy khoảng cách từ $A$ đến $C$ khoảng $103,68$ m.",
    ]))
    return s


def chapter4():
    s = []
    s += h1("04", "VECTƠ",
            "Chương IV – SGK Toán 10 KNTT: Bài 7 → Bài 11 (trọng tâm giữa kì I: Bài 7. Các khái niệm mở đầu)")

    s.append(h2("4.1. Các khái niệm mở đầu"))
    s.append(P("**Vectơ** là một đoạn thẳng có hướng, nghĩa là trong hai điểm mút của đoạn thẳng đã chỉ rõ điểm đầu và "
               "điểm cuối. Vectơ có điểm đầu $A$, điểm cuối $B$ kí hiệu là $\\v{AB}$; vectơ còn được kí hiệu bởi chữ "
               "thường in đậm như $\\v{a}$, $\\v{b}$, $\\v{x}$, $\\v{y}$."))
    s.append(data_table([
        ["Khái niệm", "Định nghĩa", "Ghi nhớ"],
        ["**Giá của vectơ**", "đường thẳng đi qua điểm đầu và điểm cuối của vectơ", "mỗi vectơ có một giá"],
        ["**Độ dài vectơ** $|\\v{AB}|$", "độ dài đoạn thẳng $AB$", "$|\\v{AB}| = AB ≥ 0$; là một **số**, không phải vectơ"],
        ["**Hai vectơ cùng phương**", "giá của chúng song song hoặc trùng nhau", "kí hiệu $\\v{a} ∥ \\v{b}$"],
        ["**Hai vectơ cùng hướng**", "cùng phương và có cùng chiều", "cùng hướng thì cùng phương, ngược lại **không**"],
        ["**Hai vectơ bằng nhau**", "cùng hướng và cùng độ dài", "$\\v{AB} = \\v{CD} ⇔ \\v{AB}, \\v{CD}$ cùng hướng và $AB = CD$"],
        ["**Hai vectơ đối nhau**", "cùng độ dài và ngược hướng", "$\\v{AB}$ và $\\v{BA}$ là hai vectơ đối nhau"],
        ["**Vectơ – không** $\\v{0}$", "vectơ có điểm đầu trùng điểm cuối, $|\\v{0}| = 0$", "cùng phương, cùng hướng với **mọi** vectơ"],
    ], widths=[40 * mm, 62 * mm, None], align_center=False))

    s.extend(box(["**Ba điểm thẳng hàng ⇔ ba vectơ cùng phương.** Cụ thể $A, B, C$ thẳng hàng $⇔ \\v{AB}$ và $\\v{AC}$ "
                  "cùng phương. Đây là công cụ chuẩn để chứng minh thẳng hàng bằng vectơ.",
                  "**Vectơ bằng nhau không cần cùng điểm đầu.** $\\v{AB} = \\v{DC}$ chỉ đòi hỏi cùng hướng và cùng độ dài; "
                  "khi đó tứ giác $ABCD$ là hình bình hành (nếu $A, B, C, D$ không thẳng hàng)."],
                 kind="box_tip", title="Ghi nhớ"))

    s.append(P("**Chứng minh hai vectơ bằng nhau.** Cách 1: chứng minh tứ giác tạo bởi bốn điểm là hình bình hành "
               "(hoặc hình thoi, hình chữ nhật, hình vuông) rồi dùng tính chất hai cạnh đối song song và bằng nhau. "
               "Cách 2: tính độ dài và chỉ ra cùng hướng. Cách 3: dùng trung điểm – với $I$ là trung điểm của $AB$ thì "
               "$\\v{IA} = \\v{BI}$ và $\\v{IA} = −\\v{IB}$."))

    # ---------------------------------------------------------------- 4.2
    s.append(h2("4.2. Tổng và hiệu của hai vectơ"))
    s.append(h3("a) Quy tắc ba điểm và quy tắc hình bình hành"))
    s.append(formula("Quy tắc ba điểm:  $\\v{AB} + \\v{BC} = \\v{AC}$   (với ba điểm $A, B, C$ bất kì)"))
    s.append(formula("Quy tắc hình bình hành:  $\\v{AB} + \\v{AD} = \\v{AC}$   ($ABCD$ là hình bình hành)"))
    s.append(P("Phép cộng vectơ có tính chất **giao hoán** ($\\v{a} + \\v{b} = \\v{b} + \\v{a}$) và **kết hợp** "
               "($(\\v{a} + \\v{b}) + \\v{c} = \\v{a} + (\\v{b} + \\v{c})$), cộng với $\\v{0}$ không đổi kết quả."))
    s.append(P("**Hiệu của hai vectơ:** $\\v{a} − \\v{b} = \\v{a} + (−\\v{b})$. Với ba điểm $A, B, C$ bất kì ta có "
               "**quy tắc hiệu** $\\v{AB} − \\v{AC} = \\v{CB}$ (chú ý chiều: “cuối trừ đầu” – từ $B$ đến $C$)."))

    s.append(h3("b) Tính chất trung điểm và trọng tâm"))
    s.append(data_table([
        ["Vị trí", "Đẳng thức vectơ", "Hệ quả với điểm $M$ bất kì"],
        ["$I$ là trung điểm của $AB$", "$\\v{IA} + \\v{IB} = \\v{0}$", "$\\v{MA} + \\v{MB} = 2\\v{MI}$"],
        ["$G$ là trọng tâm $ΔABC$", "$\\v{GA} + \\v{GB} + \\v{GC} = \\v{0}$", "$\\v{MA} + \\v{MB} + \\v{MC} = 3\\v{MG}$"],
    ], widths=[52 * mm, 52 * mm, None], align_center=True))

    # ---------------------------------------------------------------- 4.3
    s.append(h2("4.3. Tích của một vectơ với một số"))
    s.append(P("Tích của vectơ $\\v{a}$ với số thực $k$ là một vectơ, kí hiệu $k\\v{a}$, xác định như sau: "
               "cùng hướng với $\\v{a}$ nếu $k > 0$, ngược hướng với $\\v{a}$ nếu $k < 0$, và có độ dài bằng $|k|·|\\v{a}|$."))
    s.append(P("Các tính chất: $k(l\\v{a}) = (kl)\\v{a}$; $(k + l)\\v{a} = k\\v{a} + l\\v{a}$; "
               "$k(\\v{a} + \\v{b}) = k\\v{a} + k\\v{b}$; $1\\v{a} = \\v{a}$; $(−1)\\v{a} = −\\v{a}$."))
    s.append(P("**Điều kiện cùng phương:** $\\v{a}$ và $\\v{b}$ ($\\v{b} ≠ \\v{0}$) cùng phương $⇔$ tồn tại số $k$ sao cho "
               "$\\v{a} = k\\v{b}$. Từ đó, ba điểm $A, B, C$ thẳng hàng $⇔ \\v{AB} = k\\v{AC}$."))

    # ---------------------------------------------------------------- 4.4
    s.append(h2("4.4. Vectơ trong mặt phẳng toạ độ"))
    s.append(P("Trong mặt phẳng $Oxy$ với hai vectơ đơn vị $\\v{i}$, $\\v{j}$ (lần lượt cùng hướng với $Ox$, $Oy$ và có độ dài $1$):"))
    s.append(data_table([
        ["Đối tượng", "Công thức"],
        ["Vectơ $\\v{u} = (x; y)$", "$\\v{u} = x\\v{i} + y\\v{j}$"],
        ["Vectơ $\\v{AB}$ với $A(x_A; y_A)$, $B(x_B; y_B)$", "$\\v{AB} = (x_B − x_A;\\; y_B − y_A)$"],
        ["Tổng – hiệu – nhân với số", "$\\v{u} + \\v{v} = (x_1 + x_2;\\; y_1 + y_2)$; $\\v{u} − \\v{v} = (x_1 − x_2;\\; y_1 − y_2)$; $k\\v{u} = (kx_1;\\; ky_1)$"],
        ["Độ dài vectơ", "$|\\v{u}| = √(x^(2) + y^(2))$; $AB = √((x_B − x_A)^(2) + (y_B − y_A)^(2))$"],
        ["Cùng phương", "$\\v{u} ∥ \\v{v} ⇔ x_1 y_2 − x_2 y_1 = 0$"],
        ["Trung điểm $I$ của $AB$", "$x_I = (x_A + x_B)/2$; $y_I = (y_A + y_B)/2$"],
        ["Trọng tâm $G$ của $ΔABC$", "$x_G = (x_A + x_B + x_C)/3$; $y_G = (y_A + y_B + y_C)/3$"],
    ], widths=[62 * mm, None], align_center=False))

    # ---------------------------------------------------------------- 4.5
    s.append(h2("4.5. Tích vô hướng của hai vectơ"))
    s.append(formula("$\\v{a} · \\v{b} = |\\v{a}| · |\\v{b}| · cos(\\v{a}, \\v{b})$"))
    s.append(P("Bình phương vô hướng: $\\v{a} · \\v{a} = \\v{a}^(2) = |\\v{a}|^(2)$. "
               "Với hai vectơ khác $\\v{0}$: $\\v{a} ⊥ \\v{b} ⇔ \\v{a} · \\v{b} = 0$."))
    s.append(P("Biểu thức toạ độ: nếu $\\v{a} = (x_1; y_1)$, $\\v{b} = (x_2; y_2)$ thì "
               "$\\v{a} · \\v{b} = x_1 x_2 + y_1 y_2$, do đó $cos(\\v{a}, \\v{b}) = (x_1 x_2 + y_1 y_2) / "
               "(√(x_1^(2) + y_1^(2)) · √(x_2^(2) + y_2^(2)))$."))

    s.extend(box(["**Bảng tổng hợp công cụ chứng minh bằng vectơ:**",
                  "Ba điểm $A, B, C$ thẳng hàng $⇔ \\v{AB}$ và $\\v{AC}$ cùng phương.",
                  "$AB ⊥ CD ⇔ \\v{AB} · \\v{CD} = 0$.",
                  "$ABCD$ là hình bình hành $⇔ \\v{AB} = \\v{DC}$.",
                  "$I$ là trung điểm $AB ⇔ \\v{IA} + \\v{IB} = \\v{0}$; $G$ là trọng tâm $⇔ \\v{GA} + \\v{GB} + \\v{GC} = \\v{0}$.",
                  "$M$ thuộc đường tròn tâm $I$ bán kính $R ⇔ IM = R$ (dùng toạ độ để tính)."],
                 kind="box_tip", title="Sổ tay công thức"))

    s.append(h2x("4.6. Bảng tổng kết Phần I – nhìn một lần, nhớ cả bốn chương"))
    s.append(data_table([
        ["Chương", "Phải nhớ nhất", "Dạng bài chắc chắn có trong đề", "Bẫy hay gặp"],
        ["I. Mệnh đề – Tập hợp",
         "phủ định của $∀$, $∃$; $P ⇒ Q$; $2^(n)$ tập con; quy ước ngoặc tròn/vuông",
         "nhận biết mệnh đề; phủ định; giao – hợp – hiệu – phần bù trên trục số; đếm phần tử",
         "đổi dấu $∀ ↔ ∃$; lấy/không lấy đầu mút"],
        ["II. Bất phương trình bậc nhất hai ẩn",
         "3 bước biểu diễn miền nghiệm; nét liền/nét đứt; thử $F$ tại các đỉnh",
         "nhận biết bất phương trình/hệ; mô tả miền nghiệm; bài toán tối ưu",
         "bỏ sót đỉnh là giao điểm của hai đường biên"],
        ["III. Hệ thức lượng trong tam giác",
         "$sin^(2) + cos^(2) = 1$; góc bù; định lí côsin, định lí sin; 5 công thức diện tích",
         "nhận biết công thức; tính cạnh – góc – diện tích; bài toán khoảng cách, chiều cao",
         "quên đổi dấu $cos$, $tan$ của góc tù; thiếu hệ số $½$"],
        ["IV. Vectơ",
         "cùng phương – cùng hướng – bằng nhau; vectơ – không; quy tắc ba điểm",
         "nhận biết khái niệm vectơ; đếm vectơ bằng nhau trong hình bình hành/đa giác đều",
         "nhầm $\\v{AB} = \\v{CD}$ với $\\v{AB} = \\v{DC}$"],
    ], widths=[40 * mm, 46 * mm, 52 * mm, None], align_center=False))

    s.append(h2x("4.7. Tự kiểm tra nhanh trước khi làm đề"))
    s.append(P("Che cột “Trả lời”, tự đọc câu hỏi và trả lời thành tiếng. Nếu sai từ 3 câu trở lên, "
               "hãy quay lại đúng mục lí thuyết tương ứng ở trên trước khi làm Phần II."))
    s.append(data_table([
        ["Câu hỏi tự kiểm tra", "Trả lời", "Mục cần xem lại"],
        ["Câu “$x + 3 > 5$” có phải mệnh đề không?", "Không – còn chứa biến", "1.1"],
        ["Phủ định của “$∃x ∈ ℤ, x^(2) = 2$” là gì?", "“$∀x ∈ ℤ, x^(2) ≠ 2$”", "1.1"],
        ["Tập $n$ phần tử có bao nhiêu tập con?", "$2^(n)$", "1.2"],
        ["$[−2; 3) ∩ (1; 5]$ bằng bao nhiêu?", "$(1; 3)$", "1.3"],
        ["Gốc $O$ thuộc miền nghiệm của $x − y + 1 > 0$ không?", "Có, vì $0 − 0 + 1 = 1 > 0$", "2.1"],
        ["Bất phương trình có dấu “$<$” thì vẽ bờ thế nào?", "Nét đứt (không kể bờ)", "2.1"],
        ["Giá trị lớn nhất của $F = ax + by$ trên miền đa giác đạt ở đâu?", "Tại một trong các đỉnh", "2.2"],
        ["$cos 120°$ bằng bao nhiêu?", "$−1/2$", "3.1"],
        ["Cho $sin α = 1/3$, $α$ tù. $cos α$ bằng bao nhiêu?", "$−2√2/3$", "3.1"],
        ["Công thức tính $cos A$ theo ba cạnh?", "$cos A = (b^(2) + c^(2) − a^(2)) / (2bc)$", "3.2"],
        ["$\v{AB} + \v{BC}$ bằng vectơ nào?", "$\v{AC}$", "4.2"],
        ["Trong hình bình hành $ABCD$, $\v{AB}$ bằng vectơ nào?", "$\v{DC}$", "4.1"],
    ], widths=[72 * mm, 48 * mm, None], align_center=False))
    return s
