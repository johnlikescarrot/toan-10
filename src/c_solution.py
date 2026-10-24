# -*- coding: utf-8 -*-
"""PHẦN III – ĐÁP ÁN VÀ LỜI GIẢI CHI TIẾT (đủ 24 câu)."""
from kit import *
from kit import _p
from c_exam import MCQ, TRUE_FALSE, SHORT

SOL = {
    1: ["Mệnh đề phải là câu **khẳng định** có tính đúng – sai xác định.",
        "A là câu hỏi, C là câu cầu khiến → không phải mệnh đề. D chứa biến $x$ nên chưa xác định được tính đúng sai.",
        "B là câu khẳng định đúng → là mệnh đề. **Chọn B.**"],
    2: ["Kí hiệu $∀$ đọc là “với mọi” (kí hiệu phổ biến), $∃$ đọc là “tồn tại”.",
        "Vậy “$∀x ∈ ℝ, x^(2) ≥ 0$” đọc là: với mọi số thực $x$, ta có $x^(2) ≥ 0$. **Chọn B.**",
        "Lưu ý: mệnh đề này **đúng**, vì bình phương của mọi số thực đều không âm."],
    3: ["Kiểm tra từng phần tử: $4 ∉ A$ nên A sai; $5 ∈ A$ nên B đúng; $2 ∈ A$ nên C sai; $7 ∈ A$ nên D sai.",
        "**Chọn B.**"],
    4: ["$A ∩ B$ gồm các phần tử **vừa thuộc** $A$ **vừa thuộc** $B$: chỉ có $3$ và $4$.",
        "**Chọn B.** Nếu đề hỏi $A ∪ B$ thì đáp án là ${1; 2; 3; 4; 5}$ (phương án C)."],
    5: ["Bất phương trình bậc nhất hai ẩn có dạng $ax + by ≤ c$ với $a, b$ không đồng thời bằng $0$; "
        "các ẩn $x, y$ đều ở bậc nhất.",
        "B có $x^(2)$; C có tích $xy$; D có ẩn ở mẫu → loại. **Chọn A.**"],
    6: ["Hệ bất phương trình bậc nhất hai ẩn chỉ gồm các bất phương trình bậc nhất hai ẩn.",
        "B, C, D đều chứa $x^(2)$, $xy$ hoặc $1/x$ → loại. **Chọn A.**"],
    7: ["Áp dụng công thức hai góc bù nhau: $sin(180° − α) = sin α$.",
        "Vậy $sin 150° = sin(180° − 30°) = sin 30° = 1/2$. **Chọn B.**",
        "Chú ý: nếu là $cos 150°$ thì kết quả là $−cos 30° = −√3/2$ (đổi dấu)."],
    8: ["Dùng $sin^(2) α + cos^(2) α = 1$: $sin^(2) α = 1 − (−3/5)^(2) = 1 − 9/25 = 16/25$, "
        "suy ra $sin α = ±4/5$.",
        "Vì $90° < α < 180°$ (góc tù) nên $sin α > 0$, do đó $sin α = 4/5$. **Chọn A.**",
        "Phương án C, D là bẫy: đó là giá trị của $sin^(2) α$, không phải $sin α$."],
    9: ["Định lí côsin: $a^(2) = b^(2) + c^(2) − 2bc·cos A$ → A sai (dấu “+”), D sai (góc phải là $A$).",
        "Diện tích $S = ½·a·b·sin C$ → C thiếu hệ số $½$. Định lí sin $a/sin A = 2R$ → B đúng. **Chọn B.**"],
    10: ["Áp dụng định lí côsin với góc $A$ xen giữa hai cạnh $b, c$: "
         "$a^(2) = b^(2) + c^(2) − 2bc·cos A = 25 + 64 − 2·5·8·cos 60°$.",
         "$cos 60° = 1/2$ nên $a^(2) = 89 − 40 = 49$, suy ra $a = 7$. **Chọn A.**",
         "Phương án C là bẫy vì quên lấy căn bậc hai."],
    11: ["Với hình bình hành $ABCD$ (các đỉnh đặt theo thứ tự vòng quanh), hai cạnh $AB$ và $DC$ song song, "
         "bằng nhau và **cùng hướng**, do đó $\\v{AB} = \\v{DC}$.",
         "$\\v{AB}$ và $\\v{CD}$ tuy cùng độ dài nhưng **ngược hướng** nên không bằng nhau – đây chính là bẫy của phương án A. "
         "**Chọn B.**"],
    12: ["A, B, D đúng theo tính chất hình bình hành: $\\v{AB} = \\v{DC}$, $\\v{AD} = \\v{BC}$, "
         "và $\\v{AB}$, $\\v{DC}$ cùng hướng.",
         "Hai đường chéo $AC$ và $BD$ không song song, độ dài nói chung khác nhau nên $\\v{AC} ≠ \\v{BD}$. "
         "**Chọn C.**"],
}

TF_SOL = {
    13: [("a)", "Đúng", "Vì $x$ nguyên và $−3 ≤ x ≤ 2$ nên $x ∈ {−3; −2; −1; 0; 1; 2}$."),
        ("b)", "Sai", "Đếm được $6$ phần tử, không phải $5$."),
        ("c)", "Đúng", "Tập có $6$ phần tử nên có $2^(6) = 64$ tập con."),
        ("d)", "Sai", "Có $3$ số nguyên âm là $−3; −2; −1$.")],
    14: [("a)", "Đúng", "Thay $x = 0, y = 0$: $0 − 0 + 3 = 3 > 0$ thoả mãn."),
        ("b)", "Sai", "Thay $x = 2, y = 8$: $4 − 8 + 3 = −1 > 0$ là sai, nên $M$ không thuộc miền nghiệm."),
        ("c)", "Đúng", "Bất phương trình có dấu “$>$” (không kể bờ) nên bờ vẽ bằng nét đứt; bờ chính là $Δ: 2x − y + 3 = 0$."),
        ("d)", "Sai", "Thay $x = −2, y = 0$: $−4 − 0 + 3 = −1 > 0$ sai. Miền nghiệm là nửa mặt phẳng **chứa** $O(0;0)$.")],
}


def solutions():
    s = []
    s += h1("06", "ĐÁP ÁN VÀ LỜI GIẢI CHI TIẾT",
            "Giải thích từng bước cho cả 24 câu – kèm cảnh báo về các phương án gây nhiễu")

    s.append(h2("Đáp án nhanh"))
    s.append(data_table([
        ["Câu", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
        ["Đáp án"] + [m[4] for m in MCQ],
    ], widths=[20 * mm] + [13.6 * mm] * 12, align_center=True))
    s.append(data_table([
        ["Đúng – sai", "a)", "b)", "c)", "d)", "Trả lời ngắn", "Kết quả"],
        ["Câu 13", "Đ", "S", "Đ", "S", "Câu 15", "$−2/5$"],
        ["Câu 14", "Đ", "S", "Đ", "S", "Câu 16", "$10√3 ≈ 17,32$"],
    ], widths=[26 * mm, 13 * mm, 13 * mm, 13 * mm, 13 * mm, 30 * mm, None], align_center=True))

    # ---------------------------------------------------------- phần I
    s.append(h2("PHẦN I. Trắc nghiệm chọn phương án"))
    for num, lvl, text, opts, ans, topic in MCQ:
        s.append(h3("Câu %d. %s — đáp án %s" % (num, topic, ans)))
        s.extend(answer(SOL[num], label="Lời giải"))

    # ---------------------------------------------------------- phần II
    s.append(h2("PHẦN II. Trắc nghiệm đúng – sai"))
    for num, lead, stmts, _ in TRUE_FALSE:
        s.append(h3("Câu %d." % num))
        s.append(P(lead, "body_tight"))
        rows = [["Ý", "Nhận định", "Kết luận", "Giải thích"]]
        for (mark, txt, val), (m2, verdict, why) in zip(stmts, TF_SOL[num]):
            rows.append([mark, txt, "<b>%s</b>" % verdict, why])
        s.append(data_table(rows, widths=[10 * mm, 58 * mm, 22 * mm, None], align_center=False))
        s.append(Spacer(1, 8))
    s.append(P("**Cách tính điểm phần đúng – sai:** đúng 1 ý được 0,1; đúng 2 ý được 0,25; đúng 3 ý được 0,5; "
               "đúng cả 4 ý được 1,0 điểm. Vì vậy chỉ cần chắc chắn 2 ý là đã có điểm, nhưng để đạt điểm cao "
               "phải kiểm tra **cả bốn** ý – đừng bỏ trống ý nào."))

    # ---------------------------------------------------------- phần III
    s.append(h2("PHẦN III. Trắc nghiệm trả lời ngắn"))

    s.append(h3("Câu 15. Cho $90° < α < 180°$ và $tan α = −2$. Tính $P = sin α · cos α$."))
    s.extend(answer([
        "Từ $1 + tan^(2) α = 1/cos^(2) α$ suy ra $1 + 4 = 5 = 1/cos^(2) α$, do đó $cos^(2) α = 1/5$.",
        "Vì $α$ là góc tù nên $cos α < 0$, suy ra $cos α = −1/√5$.",
        "Mặt khác $tan α = sin α / cos α ⇒ sin α = tan α · cos α = (−2)·(−1/√5) = 2/√5$ (phù hợp $sin α > 0$).",
        "$P = sin α · cos α = (2/√5)·(−1/√5) = −2/5$.",
        "**Cách khác nhanh hơn:** $P = sin α cos α = tan α · cos^(2) α = (−2)·(1/5) = −2/5$.",
        "**Đáp số: $P = −2/5 = −0,4$.**",
    ]))

    s.append(h3("Câu 16. Cho tam giác $ABC$ có $AB = 5$, $AC = 8$, $\\widehat{A} = 60°$. Tính diện tích $S$."))
    s.extend(answer([
        "Góc $A$ là góc xen giữa hai cạnh $AB$ và $AC$, nên dùng công thức $S = ½·AB·AC·sin A$.",
        "$S = ½ · 5 · 8 · sin 60° = 20 · (√3/2) = 10√3$.",
        "$√3 ≈ 1,73205$ nên $S ≈ 17,3205 ≈ 17,32$ (đơn vị diện tích).",
        "**Đáp số: $S = 10√3 ≈ 17,32$.** Lưu ý: $sin 60° = √3/2$, không phải $1/2$ – đây là lỗi phổ biến nhất.",
    ]))

    # ---------------------------------------------------------- phần IV
    s.append(h2("PHẦN IV. Tự luận"))

    s.append(h3("Câu 19 (1,0 điểm). Các phép toán trên tập hợp"))
    s.append(P("Cho $A = {x ∈ ℝ \\;|\\; −3 ≤ x < 5} = [−3; 5)$ và $B = {x ∈ ℝ \\;|\\; x ≥ 1} = [1; +∞)$."))
    s.extend(answer([
        "**Bước 1 – chuyển về kí hiệu khoảng, đoạn:** $A = [−3; 5)$, $B = [1; +∞)$. Vẽ hai tập trên cùng một trục số.",
        "**$A ∩ B = [1; 5)$.** Vì $1 ∈ A$ (do $−3 ≤ 1 < 5$) nên đầu mút $1$ **được lấy**, còn $5 ∉ B$ nên $5$ không lấy.",
        "**$A ∪ B = [−3; +∞)$.** Hai tập “phủ” liền nhau từ $−3$ trở đi nên hợp là nửa khoảng $[−3; +∞)$.",
        "**$A \\setminus B = [−3; 1)$.** Đó là phần thuộc $A$ mà **không** thuộc $B$, tức các số $x$ thoả $−3 ≤ x < 1$. "
        "Đầu mút $1$ **không lấy** vì $1 ∈ B$.",
        "**$C_ℝ B = ℝ \\setminus B = (−∞; 1)$.** Phần bù gồm các số thực **không** thoả $x ≥ 1$, tức $x < 1$. "
        "Đầu mút $1$ **không lấy** vì $1 ∈ B$.",
        "**Kết luận:** $A ∩ B = [1; 5)$; $A ∪ B = [−3; +∞)$; $A \\setminus B = [−3; 1)$; $C_ℝ B = (−∞; 1)$.",
    ]))
    s.extend(box(["**Thang điểm gợi ý:** mỗi kết quả đúng 0,25 điểm. Nếu chỉ vẽ trục số đúng mà chưa viết kết quả theo "
                  "kí hiệu khoảng thì không có điểm tối đa.",
                  "**Lỗi thường gặp:** viết $A \\setminus B = [−3; 1]$ (lấy nhầm đầu mút $1$); "
                  "viết $C_ℝ B = (−∞; 1]$ (lấy nhầm $1$ dù $1 ∈ B$). Hãy luôn tự hỏi: “điểm đầu mút có thuộc tập bị trừ không?”"],
                 kind="box_warn", title="Chấm – chữa"))

    s.append(h3("Câu 20 (1,0 điểm). Định lí sin – bài toán thực tiễn"))
    s.append(P("Từ hai vị trí $A$, $B$ cách nhau $80$ m trên bờ biển, quan sát hòn đảo $C$ với "
               "$\\widehat{BAC} = 75°$, $\\widehat{ABC} = 60°$. Tính $AC$ và $BC$."))
    s.extend(answer([
        "**Bước 1 – dựng tam giác:** ba điểm $A, B, C$ tạo thành tam giác $ABC$ với $AB = 80$ m; "
        "cần tìm hai cạnh $AC$ (đối diện góc $B$) và $BC$ (đối diện góc $A$).",
        "**Bước 2 – tìm góc thứ ba:** $\\widehat{C} = 180° − 75° − 60° = 45°$.",
        "**Bước 3 – chọn công cụ:** đã biết một cạnh $AB$ và **hai góc** của tam giác nên dùng **định lí sin**: "
        "$AB / sin C = AC / sin B = BC / sin A$.",
        "**Tính $AC$:** $AC = AB · sin B / sin C = 80 · sin 60° / sin 45° = 80 · (√3/2) / (√2/2) = 80√(3/2) = 40√6 ≈ 97,98$ (m).",
        "**Tính $BC$:** $BC = AB · sin A / sin C = 80 · sin 75° / sin 45°$. "
        "Với $sin 75° = (√6 + √2)/4 ≈ 0,9659$: $BC ≈ 80 · 0,9659 / 0,7071 ≈ 109,28$ (m).",
        "**Kết luận:** khoảng cách từ $A$ đến đảo khoảng $97,98$ m; từ $B$ đến đảo khoảng $109,28$ m.",
    ]))
    s.extend(box(["**Vì sao chọn định lí sin mà không phải định lí côsin?** Định lí côsin cần **hai cạnh** và góc xen giữa, "
                  "ở đây chỉ biết một cạnh. Định lí sin phù hợp với dữ kiện “một cạnh – hai góc”.",
                  "**Kiểm tra hợp lí:** góc $C$ nhỏ nhất ($45°$) nên cạnh $AB = 80$ m phải nhỏ nhất – đúng, vì "
                  "$80 < 97,98 < 109,28$ và $45° < 60° < 75°$. Quan hệ cạnh – góc giúp phát hiện kết quả sai."],
                 kind="box_tip", title="Phân tích – kiểm tra"))

    s.append(h3("Câu 21 (1,0 điểm). Hệ bất phương trình – bài toán tối ưu"))
    s.append(P("Nông trại có $8$ ha đất, vốn không quá $180$ triệu đồng. Cà rốt: $20$ triệu/ha, lãi $30$ triệu/ha. "
               "Khoai tây: $30$ triệu/ha, lãi $40$ triệu/ha. Tìm phương án lợi nhuận lớn nhất."))
    s.extend(answer([
        "**Bước 1 – đặt ẩn.** Gọi $x$ (ha) là diện tích trồng cà rốt, $y$ (ha) là diện tích trồng khoai tây; "
        "$x ≥ 0$, $y ≥ 0$.",
        "**Bước 2 – lập hệ bất phương trình.** Ràng buộc diện tích: $x + y ≤ 8$. "
        "Ràng buộc vốn: $20x + 30y ≤ 180$, chia cả hai vế cho $10$ được $2x + 3y ≤ 18$. "
        "Vậy hệ là $\\{x + y ≤ 8;\\; 2x + 3y ≤ 18;\\; x ≥ 0;\\; y ≥ 0\\}$.",
        "**Bước 3 – hàm mục tiêu.** Lợi nhuận $F(x; y) = 30x + 40y$ (triệu đồng).",
        "**Bước 4 – vẽ miền nghiệm và tìm các đỉnh.** Các đường biên: $x + y = 8$ (qua $(8; 0)$ và $(0; 8)$); "
        "$2x + 3y = 18$ (qua $(9; 0)$ và $(0; 6)$); hai trục toạ độ. Miền nghiệm là tứ giác $OMPN$ với "
        "$O(0; 0)$, $M(8; 0)$, $N(0; 6)$ và $P$ là giao điểm của hai đường thẳng $x + y = 8$, $2x + 3y = 18$.",
        "**Tìm $P$:** giải hệ. Từ $x + y = 8$ suy ra $x = 8 − y$; thay vào $2x + 3y = 18$: "
        "$16 − 2y + 3y = 18 ⇒ y = 2$, do đó $x = 6$. Vậy $P(6; 2)$.",
        "**Bước 5 – lập bảng giá trị của $F$ tại bốn đỉnh:**",
    ]))
    s.append(data_table([
        ["Đỉnh", "$O(0; 0)$", "$M(8; 0)$", "$N(0; 6)$", "$P(6; 2)$"],
        ["$F = 30x + 40y$", "$0$", "$240$", "$240$", "$30·6 + 40·2 = 260$"],
    ], widths=[38 * mm, 30 * mm, 30 * mm, 30 * mm, None], align_center=True))
    s.extend(answer([
        "Giá trị lớn nhất của $F$ là $260$, đạt tại đỉnh $P(6; 2)$; ba đỉnh còn lại cho $0$; $240$; $240$.",
        "Trồng $6$ ha cà rốt và $2$ ha khoai tây (tổng $8$ ha; vốn $20·6 + 30·2 = 180$ triệu đồng – dùng đúng "
        "toàn bộ vốn), lợi nhuận lớn nhất là $260$ triệu đồng.",
    ], label="Kết luận"))
    s.extend(box(["**Thang điểm gợi ý:** đặt ẩn và điều kiện 0,25; lập đúng hệ bất phương trình 0,25; "
                  "xác định đúng miền nghiệm và các đỉnh 0,25; tính $F$ tại các đỉnh và kết luận 0,25.",
                  "**Bẫy thường gặp:** chỉ thử ở $O$, $M$, $N$ mà quên đỉnh $P$ – đây chính là đỉnh cho lời giải tối ưu. "
                  "Luôn tìm **giao điểm của các đường biên** để không bỏ sót đỉnh."],
                 kind="box_warn", title="Chấm – chữa"))
    return s
