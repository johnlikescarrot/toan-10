# -*- coding: utf-8 -*-
"""
PHẦN B – KIẾN THỨC NỀN TẢNG VÀ DẠNG BÀI THEO TỪNG CHƯƠNG
(Chương trình Toán 10 "Kết nối tri thức": Bài 1 → Bài 7, tập 1)
"""

W = 498.0


def _vd(ctx, so, muc, de, lgiai, dap_an=None, luu_y=None):
    """Khung một ví dụ mẫu: đề – lời giải – đáp án."""
    ctx.h3("Ví dụ %s (%s). %s" % (so, muc, de))
    ctx.p("<b>Lời giải.</b> " + lgiai)
    if dap_an:
        ctx.p("<font color='#1E6B3A'><b>Đáp án:</b> %s</font>" % dap_an)
    if luu_y:
        ctx.p("<font color='#555555'><i>Ghi chú: %s</i></font>" % luu_y)


def _tuluyen(ctx, items, dap_ans):
    """Bài tập tự luyện kèm đáp án ngắn."""
    ctx.h3("Bài tập tự luyện")
    ctx.numbered(items)
    ctx.box("Đáp án tự luyện (gợi ý)", dap_ans, kind="ans")


# ==========================================================================
def chuong_1(ctx):
    ctx.h1("B.1. CHƯƠNG 1. MỆNH ĐỀ VÀ TẬP HỢP  (Bài 1 – Bài 2)")

    ctx.box("Mục tiêu của chương", [
        "Phân biệt được mệnh đề, mệnh đề chứa biến; xác định được tính đúng/sai của một mệnh đề "
        "toán học đơn giản.",
        "Lập được mệnh đề phủ định của một mệnh đề chứa kí hiệu ∀, ∃ và kiểm tra tính đúng/sai.",
        "Nhận biết mệnh đề kéo theo, mệnh đề đảo, mệnh đề tương đương; xác định được điều kiện cần, "
        "điều kiện đủ, điều kiện cần và đủ.",
        "Xác định được tập hợp bằng hai cách; so sánh hai tập hợp; biểu diễn được khoảng, đoạn, "
        "nửa khoảng trên trục số.",
        "Dùng được biểu đồ Ven để biểu diễn giao, hợp, phần bù của hai tập hợp; giải được bài toán "
        "thực tế về các phép toán trên tập hợp.",
    ], kind="info")

    # ---------------- 1.1 Mệnh đề ----------------
    ctx.h2("B.1.1. Mệnh đề, mệnh đề chứa biến")

    ctx.h3("a) Mệnh đề")
    ctx.bullets([
        "<b>Mệnh đề</b> là một khẳng định có tính <b>đúng</b> hoặc <b>sai</b> (tức là khẳng định "
        "được tính đúng hay sai).",
        "Mỗi mệnh đề chỉ có một trong hai giá trị: đúng hoặc sai; không thể vừa đúng vừa sai.",
        "Câu hỏi, câu cảm thán, câu mệnh lệnh <b>không phải</b> là mệnh đề (vì không xác định được "
        "tính đúng hay sai).",
    ])
    ctx.formula([
        "Mệnh đề: khẳng định có tính đúng hoặc sai.",
        "Ví dụ mệnh đề: “2 + 3 = 5” (đúng); “5 là số lẻ” (sai); “Hà Nội là thủ đô của Việt Nam” (đúng).",
        "Không phải mệnh đề: “Bạn thích học Toán chứ?”; “Ôi, đẹp quá!”; “Hãy mở cửa ra.”",
    ])

    ctx.h3("b) Mệnh đề chứa biến")
    ctx.bullets([
        "<b>Mệnh đề chứa biến</b> là mệnh đề chưa khẳng định được tính đúng hay sai khi chưa cho "
        "giá trị cụ thể của biến.",
        "Kí hiệu: <i>P</i>(<i>n</i>) nếu chỉ có một biến; <i>P</i>(<i>x</i>, <i>y</i>) nếu có hai biến.",
        "Thay giá trị cụ thể của biến ta được một mệnh đề mới, lúc đó mới xác định được tính đúng/sai.",
    ])
    ctx.box("Ví dụ", [
        "“5<i>n</i> + 3 chia hết cho 2” là mệnh đề chứa biến <i>n</i>.",
        "• <i>n</i> = 1: 5·1 + 3 = 8 chia hết cho 2 → mệnh đề <b>đúng</b>.",
        "• <i>n</i> = 2: 5·2 + 3 = 13 không chia hết cho 2 → mệnh đề <b>sai</b>.",
    ], kind="grey")

    # ---------------- 1.2 Phủ định ----------------
    ctx.h2("B.1.2. Mệnh đề phủ định")
    ctx.bullets([
        "<b>Phủ định</b> của một mệnh đề <i>P</i> là mệnh đề “<i>P</i> không đúng”, kí hiệu ¬<i>P</i>.",
        "<i>P</i> và ¬<i>P</i> có tính chất <b>đúng ngược nhau</b>: một trong hai đúng, một trong hai sai.",
        "Phủ định của “∀<i>x</i> ∈ <i>X</i> : <i>P</i>(<i>x</i>)” là “∃<i>x</i> ∈ <i>X</i> : ¬<i>P</i>(<i>x</i>)”.",
        "Phủ định của “∃<i>x</i> ∈ <i>X</i> : <i>P</i>(<i>x</i>)” là “∀<i>x</i> ∈ <i>X</i> : ¬<i>P</i>(<i>x</i>)”.",
    ])
    ctx.box("Hai chỗ rất dễ sai – kiểm tra kỹ", [
        "Phủ định của “<i>x</i> &gt; 0” là “<i>x</i> ≤ 0”, <b>không phải</b> “<i>x</i> &lt; 0”.",
        "Phủ định của “<i>x</i> ≥ 0” là “<i>x</i> &lt; 0”, <b>không phải</b> “<i>x</i> ≤ 0”.",
        "Phủ định của “<i>x</i> ≠ 0” là “<i>x</i> = 0”, <b>không phải</b> “<i>x</i> &gt; 0”.",
    ], kind="err")

    # ---------------- 1.3 Kéo theo, đảo ----------------
    ctx.h2("B.1.3. Mệnh đề kéo theo, mệnh đề đảo")
    ctx.bullets([
        "Mệnh đề <b>“Nếu <i>P</i> thì <i>Q</i>”</b> được gọi là mệnh đề kéo theo, kí hiệu "
        "<b><i>P</i> ⇒ <i>Q</i></b>; <i>P</i> là <i>điều kiện</i>, <i>Q</i> là <i>kết luận</i>.",
        "Mệnh đề <b><i>Q</i> ⇒ <i>P</i></b> là mệnh đề <b>đảo</b> của mệnh đề <i>P</i> ⇒ <i>Q</i>.",
        "Mệnh đề đảo của một mệnh đề đúng <b>chưa chắc</b> đúng (và ngược lại).",
        "Nhiều định lí toán học có dạng <i>P</i> ⇒ <i>Q</i> với <i>P</i>, <i>Q</i> đều đúng.",
    ])
    ctx.formula([
        "<i>P</i>: “<i>n</i> = 2”   và   <i>Q</i>: “<i>n</i>² = 4”.",
        "<i>P</i> ⇒ <i>Q</i> đúng (2² = 4).    <i>Q</i> ⇒ <i>P</i> sai (vì <i>n</i> = −2 thì <i>n</i>² = 4 nhưng <i>n</i> ≠ 2).",
    ])

    # ---------------- 1.4 Tương đương ----------------
    ctx.h2("B.1.4. Mệnh đề tương đương và điều kiện cần – đủ")
    ctx.bullets([
        "<b>Mệnh đề tương đương</b>: <i>P</i> ⇔ <i>Q</i> khi <i>P</i> ⇒ <i>Q</i> và <i>Q</i> ⇒ <i>P</i> "
        "đều đúng (hoặc cùng sai).",
        "Mệnh đề <i>P</i> ⇔ <i>Q</i> có tính chất bắc cầu: nếu <i>P</i> ⇔ <i>Q</i> và "
        "<i>Q</i> ⇔ <i>R</i> thì <i>P</i> ⇔ <i>R</i>.",
        "<b>Điều kiện cần và đủ</b>: <i>Q</i> là điều kiện cần và đủ của <i>P</i> khi <i>P</i> ⇔ <i>Q</i>.",
        "<b>Điều kiện cần</b>: <i>Q</i> là điều kiện cần của <i>P</i> nếu <i>Q</i> ⇒ <i>P</i>.",
        "<b>Điều kiện đủ</b>: <i>Q</i> là điều kiện đủ của <i>P</i> nếu <i>P</i> ⇒ <i>Q</i>.",
    ])
    ctx.box("Mẹo phân biệt", [
        "Hỏi: “<i>Q</i> có là điều kiện cần của <i>P</i> không?” → xét mệnh đề <b><i>Q</i> ⇒ <i>P</i></b>.",
        "Hỏi: “<i>Q</i> có là điều kiện đủ của <i>P</i> không?” → xét mệnh đề <b><i>P</i> ⇒ <i>Q</i></b>.",
        "Nếu <i>P</i> ⇔ <i>Q</i> thì <i>Q</i> vừa là điều kiện cần vừa là điều kiện đủ của <i>P</i>.",
    ], kind="grey")

    # ---------------- 1.5 Tập hợp ----------------
    ctx.h2("B.1.5. Tập hợp, tập hợp con, tập hợp bằng nhau, tập rỗng")
    ctx.bullets([
        "<b>Tập hợp</b> là tập hợp các phần tử <i>x</i> thỏa mãn một tính chất xác định: "
        "<i>A</i> = {<i>x</i> | <i>P</i>(<i>x</i>)}.",
        "<b>Hai cách cho một tập hợp</b>: (1) liệt kê từng phần tử; (2) nêu tính chất đặc trưng của "
        "các phần tử.",
        "<b>Tập hợp con</b>: <i>A</i> ⊂ <i>B</i> ⇔ mọi phần tử của <i>A</i> đều thuộc <i>B</i>.",
        "<b>Hai tập hợp bằng nhau</b>: <i>A</i> = <i>B</i> ⇔ <i>A</i> ⊂ <i>B</i> và <i>B</i> ⊂ <i>A</i>.",
        "<b>Tập rỗng</b> ∅: tập hợp không có phần tử nào; ∅ là tập con của mọi tập hợp.",
    ])
    ctx.formula([
        "A = {1; 2; 3; 4}   (liệt kê)        A = {<i>x</i> ∈ ℝ | <i>x</i>² &lt; 4}   (tính chất đặc trưng)",
        "A = {1; 2; 3; 4} = {<i>x</i> ∈ ℕ | 1 ≤ <i>x</i> ≤ 4}",
    ])

    ctx.h2("B.1.6. Một số tập hợp đặc biệt")
    ctx.table(
        [
            ["Tập hợp", "Kí hiệu", "Ý nghĩa"],
            ["Tập các số tự nhiên", "ℕ = {0; 1; 2; 3; …}", "Gồm 0 và các số nguyên dương."],
            ["Tập các số tự nhiên khác 0", "ℕ* = {1; 2; 3; …}", "Không chứa 0."],
            ["Tập các số nguyên", "ℤ = {…; −2; −1; 0; 1; 2; …}", "Số nguyên dương, 0 và số nguyên âm."],
            ["Tập các số hữu tỉ", "ℚ = {<i>a</i>/<i>b</i> | <i>a</i>, <i>b</i> ∈ ℤ, <i>b</i> ≠ 0}", "Các phân số bằng nhau."],
            ["Tập các số thực", "ℝ", "Chứa tất cả các số thực."],
            ["Khoảng", "(<i>a</i>;<i>b</i>) = {<i>x</i> | <i>a</i> &lt; <i>x</i> &lt; <i>b</i>}", "Không chứa hai đầu."],
            ["Đoạn thẳng", "[<i>a</i>;<i>b</i>] = {<i>x</i> | <i>a</i> ≤ <i>x</i> ≤ <i>b</i>}", "Chứa cả hai đầu."],
            ["Nửa khoảng", "(<i>a</i>;<i>b</i>], [<i>a</i>;<i>b</i>)", "Chứa một đầu, không chứa đầu kia."],
            ["Khoảng không giới hạn", "(−∞;<i>a</i>), (−∞;<i>a</i>], (<i>a</i>;+∞), [<i>a</i>;+∞), (−∞;+∞)",
             "∞ không phải là số, không dùng dấu bằng với ∞."],
        ],
        widths=[150, 150, W - 300],
        align=["l", "l", "l"],
    )
    ctx.caption("Bảng 7. Các tập hợp đặc biệt và kí hiệu khoảng – đoạn.")

    ctx.h2("B.1.7. Biểu đồ Ven và các phép toán trên tập hợp")
    ctx.bullets([
        "<b>Biểu đồ Ven</b>: mỗi tập hợp được vẽ bằng một hình tròn; các phần tử chung của hai tập "
        "hợp nằm ở vùng giao.",
        "<b>Giao</b> <i>A</i> ∩ <i>B</i>: tập hợp gồm các phần tử thuộc cả <i>A</i> và <i>B</i>.",
        "<b>Hợp</b> <i>A</i> ∪ <i>B</i>: tập hợp gồm các phần tử thuộc <i>A</i> hoặc <i>B</i> (hoặc cả hai).",
        "<b>Phần bù</b> của <i>A</i> trong <i>U</i>: <i>C</i><sub><i>U</i></sub>(<i>A</i>) = <i>U</i> \\ <i>A</i>.",
        "<b>Hiệu</b> <i>A</i> \\ <i>B</i> = <i>A</i> ∩ <i>C</i><sub><i>U</i></sub>(<i>B</i>).",
    ])
    ctx.formula([
        "A ⊂ B  ⇔  A ∩ B = A  ⇔  A ∪ B = B        (hay: B \\ A = ∅)",
        "Số tập hợp con của một tập hợp A có <i>n</i> phần tử (kể cả tập rỗng và chính A) là 2<sup><i>n</i></sup>.",
    ])

    ctx.h2("B.1.8. Dạng bài toán điển hình và lời giải mẫu")

    _vd(ctx, "1", "nhận biết",
        "Phân biệt mệnh đề và mệnh đề chứa biến.",
        "Một câu chỉ là mệnh đề khi xác định được tính đúng hoặc sai. Câu “2 + 3 = 5” là mệnh đề "
        "(đúng). Câu “<i>x</i> + 5 &gt; 3” chưa xác định được tính đúng hay sai khi chưa cho giá trị "
        "của <i>x</i> nên là <b>mệnh đề chứa biến</b>. Câu “Em yêu môn Toán” không phải mệnh đề.",
        "B. <i>x</i> + 5 &gt; 3.")

    _vd(ctx, "2", "nhận biết",
        "Phủ định mệnh đề chứa kí hiệu ∀ và ∃.",
        "Ta có: ¬(∀<i>x</i> ∈ <i>X</i> : <i>P</i>(<i>x</i>)) ⇔ ∃<i>x</i> ∈ <i>X</i> : ¬<i>P</i>(<i>x</i>) "
        "và ¬(∃<i>x</i> ∈ <i>X</i> : <i>P</i>(<i>x</i>)) ⇔ ∀<i>x</i> ∈ <i>X</i> : ¬<i>P</i>(<i>x</i>). "
        "Áp dụng: phủ định của “∀<i>x</i> ∈ ℝ, <i>x</i>² &gt; 0” là “∃<i>x</i> ∈ ℝ, <i>x</i>² ≤ 0”.",
        "“Tồn tại số thực <i>x</i> sao cho <i>x</i>² ≤ 0” (tức là <i>x</i> = 0).")

    _vd(ctx, "3", "thông hiểu",
        "Xác định điều kiện cần, điều kiện đủ, điều kiện cần và đủ.",
        "Cho <i>P</i>: “<i>x</i> = 3”, <i>Q</i>: “<i>x</i>² = 9”. Xét <i>P</i> ⇒ <i>Q</i>: nếu <i>x</i> = 3 "
        "thì <i>x</i>² = 9 → đúng. Xét <i>Q</i> ⇒ <i>P</i>: nếu <i>x</i>² = 9 thì <i>x</i> = 3 hoặc "
        "<i>x</i> = −3; với <i>x</i> = −3 mệnh đề <i>P</i> sai → <i>Q</i> ⇒ <i>P</i> sai. Vậy <i>Q</i> "
        "là điều kiện <b>đủ</b> của <i>P</i>, không phải điều kiện cần.",
        "D. <i>Q</i> là điều kiện đủ của <i>P</i>.")

    _vd(ctx, "4", "nhận biết",
        "Tập con, tập bằng nhau và tập rỗng.",
        "Với A = {1; 2; 3}, B = {1; 2; 3; 4}: mọi phần tử của A đều thuộc B nên A ⊂ B; "
        "nhưng 4 ∉ A nên B ⊄ A, do đó A ≠ B. Với tập hợp {<i>x</i> ∈ ℝ | <i>x</i>² + 1 = 0}: "
        "<i>x</i>² ≥ 0 với mọi <i>x</i> thật nên <i>x</i>² + 1 &gt; 0, tập hợp không có phần tử nào "
        "→ tập rỗng.",
        "A ⊂ B; và {<i>x</i> ∈ ℝ | <i>x</i>² + 1 = 0} = ∅.")

    _vd(ctx, "5", "thông hiểu",
        "Biểu diễn khoảng, đoạn trên trục số và tính số tập hợp con.",
        "Các tập hợp khoảng và đoạn trên trục số được biểu diễn bằng cách vẽ các điểm đầu, điểm "
        "cuối rồi tô đậm (đoạn) hoặc nét liền (khoảng). Với A = {1; 2; 3; 4; 5} có 5 phần tử, "
        "mỗi phần tử có 2 lựa chọn (lấy hoặc không lấy) nên số tập hợp con là 2<sup>5</sup> = 32.",
        "Số tập hợp con của A = 32.")

    _vd(ctx, "6", "vận dụng",
        "Bài toán thực tế về các phép toán trên tập hợp.",
        "Gọi <i>V</i> là tập học sinh tham gia CLB Văn nghệ, <i>T</i> là tập học sinh tham gia CLB "
        "Toán, <i>U</i> là tập học sinh của lớp. Ta có |<i>V</i>| = 28, |<i>T</i>| = 20, "
        "|<i>V</i> ∩ <i>T</i>| = 8, |<i>U</i>| = 45. Suy ra |<i>V</i> ∪ <i>T</i>| = 28 + 20 − 8 = 40. "
        "Số học sinh không tham gia CLB nào là 45 − 40 = 5; số học sinh chỉ tham gia CLB Văn nghệ "
        "là 28 − 8 = 20.",
        "5 học sinh không tham gia CLB nào; 20 học sinh chỉ tham gia CLB Văn nghệ.")

    _vd(ctx, "7", "vận dụng",
        "Tính giao, hợp, hiệu và phần bù của hai tập hợp.",
        "Cho U = {1; 2; 3; 4; 5; 6; 7; 8}, A = {1; 3; 5; 7}, B = {2; 3; 4; 5}. "
        "A ∩ B gồm các phần tử chung của A và B: {3; 5}. "
        "A ∪ B gồm mọi phần tử thuộc A hoặc B: {1; 2; 3; 4; 5; 7}. "
        "A \\ B gồm các phần tử thuộc A nhưng không thuộc B: {1; 7}. "
        "C<sub>U</sub>(A) gồm các phần tử thuộc U nhưng không thuộc A: {2; 4; 6; 8}.",
        "A ∩ B = {3; 5}; A ∪ B = {1; 2; 3; 4; 5; 7}; A \\ B = {1; 7}; C<sub>U</sub>(A) = {2; 4; 6; 8}.")

    ctx.h2("B.1.9. Lỗi thường gặp và cách tránh")
    ctx.box("Sáu lỗi hay mắc ở Chương 1", [
        "<b>1.</b> Phủ định “<i>x</i> &gt; 0” thành “<i>x</i> &lt; 0” → phải là “<i>x</i> ≤ 0”.",
        "<b>2.</b> Nghĩ “A ⊂ B” và “B ⊂ A” cùng đúng → chỉ một chiều đúng (trừ khi A = B).",
        "<b>3.</b> Quên rằng ∅ là tập con của mọi tập hợp và ∅ ⊂ ∅ (theo quy ước của sách).",
        "<b>4.</b> Cho rằng {<i>x</i> ∈ ℝ | <i>x</i>² = 2} là tập rỗng → thực ra có 2 phần tử "
        "±√2.",
        "<b>5.</b> Nhầm (a;b) với [a;b], hoặc dùng dấu “=” với ∞ → phải dùng ngoặc mở/đóng thích hợp.",
        "<b>6.</b> Đếm số tập hợp con mà quên tính cả tập rỗng và chính tập hợp đó.",
    ], kind="err")

    _tuluyen(ctx, [
        "Trong các phát biểu sau, phát biểu nào là mệnh đề chứa biến? A. 5 &gt; 3. B. <i>x</i>² ≥ 0. "
        "C. Hà Nội là thành phố đông dân nhất cả nước. D. 2 + 2 = 4.",
        "Phủ định của mệnh đề “∀<i>x</i> ∈ ℝ, <i>x</i>² ≥ 0” là mệnh đề nào? "
        "A. ∃<i>x</i> ∈ ℝ: <i>x</i>² &lt; 0.  B. ∃<i>x</i> ∈ ℝ: <i>x</i>² ≤ 0.  "
        "C. ∀<i>x</i> ∈ ℝ: <i>x</i>² &lt; 0.  D. ∃<i>x</i> ∈ ℝ: <i>x</i>² &gt; 0.",
        "Cho <i>P</i>: “<i>x</i> &gt; 1”, <i>Q</i>: “<i>x</i>² &gt; 1”. Mệnh đề nào sau đây đúng? "
        "A. <i>P</i> ⇒ <i>Q</i>.  B. <i>Q</i> ⇒ <i>P</i>.  C. <i>P</i> ⇔ <i>Q</i>.  "
        "D. Không có mệnh đề nào đúng.",
        "Tập hợp nào sau đây là tập rỗng? A. {<i>x</i> ∈ ℝ | <i>x</i>² + 1 = 0}.  "
        "B. {<i>x</i> ∈ ℝ | <i>x</i>² − 4 = 0}.  C. {<i>x</i> ∈ ℝ | <i>x</i>² ≥ 0}.  "
        "D. {<i>x</i> ∈ ℝ | <i>x</i>² − 2<i>x</i> + 1 ≤ 0}.",
        "Cho A = {1; 2; 3; 4}, B = {3; 4; 5}. Tập hợp A ∩ B là: A. {1; 2}.  B. {3; 4}.  "
        "C. {3; 4; 5}.  D. {1; 2; 3; 4; 5}.",
        "Số tập hợp con của một tập hợp có 3 phần tử là: A. 3.  B. 6.  C. 8.  D. 9.",
        "Cho A = (−2; 3), B = [1; 5). Tập hợp A ∪ B là: A. (−2; 3).  B. (−2; 5).  "
        "C. [1; 3).  D. (−2; 5].",
        "Phần bù của A = {1; 2; 3} trong U = {1; 2; 3; 4; 5} là: A. {4; 5}.  B. {1; 2}.  "
        "C. {1; 2; 3; 4; 5}.  D. {3; 4; 5}.",
        "Trong lớp có 40 học sinh, 25 học sinh thích bóng đá, 18 học sinh thích bơi và 10 học sinh "
        "thích cả hai môn. Hỏi có bao nhiêu học sinh không thích môn nào?",
        "Cho A = {<i>x</i> ∈ ℝ | <i>x</i>² − 3<i>x</i> + 2 = 0}. Viết A bằng cách liệt kê các "
        "phần tử.",
    ], [
        "1. B.",
        "2. B.",
        "3. A (x &gt; 1 ⇒ x² &gt; 1; còn x = −2 thì x² &gt; 1 nhưng x &gt; 1 sai).",
        "4. A (các phương án còn lại lần lượt là {−2; 2}, ℝ, {1}).",
        "5. B.",
        "6. C (2³ = 8).",
        "7. B.",
        "8. A.",
        "9. 40 − (25 + 18 − 10) = 40 − 33 = 7 học sinh.",
        "10. A = {1; 2}.",
    ])


# ==========================================================================
def chuong_2(ctx):
    ctx.h1("B.2. CHƯƠNG 2. BẤT PHƯƠNG TRÌNH VÀ HỆ BẤT PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN  (Bài 3 – Bài 4)")

    ctx.box("Mục tiêu của chương", [
        "Nhận biết được bất phương trình bậc nhất hai ẩn; xác định nghiệm và miền nghiệm của nó "
        "trên mặt phẳng tọa độ.",
        "Mô tả được miền nghiệm của bất phương trình và của hệ bất phương trình bậc nhất hai ẩn.",
        "Chuyển được điều kiện của bài toán thực tế về dạng bất phương trình, hệ bất phương trình "
        "bậc nhất hai ẩn.",
        "Tìm được giá trị lớn nhất, giá trị nhỏ nhất của một biểu thức trên miền nghiệm của hệ.",
    ], kind="info")

    ctx.h2("B.2.1. Bất phương trình bậc nhất hai ẩn")
    ctx.bullets([
        "<b>Phương trình bậc nhất hai ẩn</b>: <i>ax</i> + <i>by</i> + <i>c</i> = 0 với <i>a</i>, <i>b</i> "
        "không đồng thời bằng 0.",
        "<b>Bất phương trình bậc nhất hai ẩn</b>: <i>ax</i> + <i>by</i> + <i>c</i> &lt; 0 (hoặc ≤ 0, "
        "&gt; 0, ≥ 0) với <i>a</i>, <i>b</i> không đồng thời bằng 0.",
        "<b>Nghiệm</b> của bất phương trình là cặp số (<i>x</i><sub>0</sub>; <i>y</i><sub>0</sub>) "
        "thỏa mãn bất phương trình.",
        "<b>Miền nghiệm</b> của bất phương trình là tập hợp tất cả điểm M(<i>x</i>; <i>y</i>) thỏa "
        "mãn bất phương trình; trên mặt phẳng tọa độ là một <b>nửa mặt phẳng</b> có chứa biên là "
        "đường thẳng <i>ax</i> + <i>by</i> + <i>c</i> = 0. Nếu dấu là &lt; hoặc &gt; thì biên "
        "<b>không</b> thuộc miền nghiệm.",
    ])
    ctx.h3("Ba bước vẽ miền nghiệm")
    ctx.numbered([
        "<b>Bước 1.</b> Vẽ đường thẳng <i>ax</i> + <i>by</i> + <i>c</i> = 0 (nếu <i>b</i> ≠ 0 thì "
        "công thức <i>y</i> = −(<i>a</i>/<i>b</i>)<i>x</i> − <i>c</i>/<i>b</i>).",
        "<b>Bước 2.</b> Xác định nửa mặt phẳng chứa các điểm thỏa mãn bất phương trình.",
        "<b>Bước 3.</b> Chọn một điểm thử (thường là điểm gốc O) và thay vào để tô màu nửa mặt phẳng; "
        "đường thẳng là biên của miền nghiệm.",
    ])
    ctx.formula([
        "2<i>x</i> − 3<i>y</i> ≤ 6   ⇔   <i>y</i> ≥ (2/3)<i>x</i> − 2",
        "Điểm thử O(0; 0):  2·0 − 3·0 = 0 ≤ 6  ⇒  gốc O nằm trong miền nghiệm.",
    ])

    ctx.h2("B.2.2. Hệ bất phương trình bậc nhất hai ẩn")
    ctx.bullets([
        "<b>Hệ bất phương trình bậc nhất hai ẩn</b> là tập hợp hai bất phương trình bậc nhất hai ẩn.",
        "<b>Nghiệm</b> của hệ là điểm thỏa mãn <b>cả hai</b> bất phương trình; tức là là <b>giao</b> "
        "của hai miền nghiệm.",
        "Miền nghiệm của hệ là giao của các miền nghiệm: có thể là một miền kín (hình tam giác, "
        "tứ giác…), một nửa mặt phẳng, hoặc rỗng.",
        "Hệ vô nghiệm khi hai miền nghiệm không có điểm chung.",
    ])
    ctx.formula([
        "Hệ:  { <i>x</i> + <i>y</i> ≤ 5 ;   <i>x</i> − <i>y</i> ≥ 0 }",
        "Miền nghiệm: giao của hai nửa mặt phẳng → một góc phẳng có đỉnh tại giao điểm của hai đường thẳng.",
    ])

    ctx.h2("B.2.3. Bài toán thực tế và bài toán tối ưu")
    ctx.bullets([
        "<b>Các bước:</b> (1) đặt ẩn số và thiết lập hệ bất phương trình theo các ràng buộc của bài "
        "toán (kể cả <i>x</i> ≥ 0, <i>y</i> ≥ 0); (2) biểu diễn miền nghiệm trên mặt phẳng tọa độ; "
        "(3) tính giá trị của biểu thức cần tối ưu tại các <b>đỉnh</b> của miền nghiệm; (4) kết luận.",
        "Nếu biển thức đạt cực trị tại cả hai đỉnh thì giá trị lớn nhất (nhỏ nhất) vẫn là giá trị đó.",
    ])
    ctx.box("Mẹo kiểm tra nhanh", [
        "Sau khi tìm các đỉnh, luôn <b>thử lại từng đỉnh</b> vào hệ để chắc chắn đỉnh đó thuộc "
        "miền nghiệm.",
        "Nếu nghiệm tối ưu có dạng phân số, kiểm tra lại phép tính ở đỉnh đó.",
    ], kind="grey")

    ctx.h2("B.2.4. Dạng bài toán điển hình và lời giải mẫu")

    _vd(ctx, "1", "nhận biết",
        "Phân biệt bất phương trình bậc nhất hai ẩn với các phương trình khác.",
        "Bất phương trình bậc nhất hai ẩn có dạng <i>ax</i> + <i>by</i> + <i>c</i> &lt; 0 (hoặc ≤, >, ≥) "
        "với <i>a</i>, <i>b</i> không đồng thời bằng 0. <i>x</i> + <i>y</i> = 0 là <b>phương trình</b> "
        "bậc nhất hai ẩn chứ không phải bất phương trình; <i>x</i>² + <i>y</i>² = 1 là phương trình "
        "bậc hai; 3<i>x</i>² − 2<i>y</i> ≤ 7 không phải bậc nhất vì có <i>x</i>².",
        "A. 2<i>x</i> + 3<i>y</i> ≤ 5.")

    _vd(ctx, "2", "nhận biết",
        "Kiểm tra một điểm có thuộc miền nghiệm hay không.",
        "Thay lần lượt tọa độ vào bất phương trình 2<i>x</i> − <i>y</i> ≤ 3: "
        "(0; 0) → 0 ≤ 3 ✓; (2; 0) → 4 ≤ 3 ✗; (0; 4) → −4 ≤ 3 ✓; (3; 3) → 3 ≤ 3 ✓ "
        "(thuộc đường thẳng biên).",
        "Cặp <b>(2; 0)</b> không thuộc miền nghiệm.")

    _vd(ctx, "3", "thông hiểu",
        "Mô tả miền nghiệm của bất phương trình bậc nhất hai ẩn.",
        "Với <i>x</i> + <i>y</i> ≤ 4: đường thẳng biên <i>x</i> + <i>y</i> = 4 chia mặt phẳng thành "
        "hai nửa mặt phẳng. Gốc O có 0 + 0 = 0 ≤ 4 nên thuộc miền nghiệm. Vì dấu là “≤” nên các "
        "điểm nằm trên đường thẳng biên không thuộc miền nghiệm.",
        "Nửa mặt phẳng chứa gốc O, <b>không</b> chứa các điểm trên đường thẳng <i>x</i> + <i>y</i> = 4.")

    _vd(ctx, "4", "nhận biết",
        "Nhận biết nghiệm và miền nghiệm của hệ bất phương trình.",
        "Một cặp số là nghiệm của hệ khi nó thỏa mãn <b>cả hai</b> bất phương trình, tức là là điểm "
        "chung của hai miền nghiệm. Vì vậy miền nghiệm của hệ là <b>giao</b> của các miền nghiệm, "
        "không phải hợp.",
        "B. Nghiệm của hệ là giao của các miền nghiệm của từng bất phương trình trong hệ.")

    _vd(ctx, "5", "vận dụng",
        "Chuyển điều kiện thực tế về dạng hệ bất phương trình.",
        "Gọi <i>x</i> là số kg nguyên liệu loại A, <i>y</i> là số kg nguyên liệu loại B. "
        "Loại A dùng 2 kg A và 3 kg B cho 1 kg sản phẩm, loại B dùng 3 kg A và 2 kg B. "
        "Kho có 8 kg nguyên liệu A và 10 kg nguyên liệu B. Sản lượng không được vượt quá số nguyên "
        "liệu có: 2<i>x</i> + 3<i>y</i> ≤ 8 và 3<i>x</i> + 2<i>y</i> ≤ 10; số lượng không âm: "
        "<i>x</i> ≥ 0, <i>y</i> ≥ 0.",
        "Hệ: { 2<i>x</i> + 3<i>y</i> ≤ 8 ; 3<i>x</i> + 2<i>y</i> ≤ 10 ; <i>x</i> ≥ 0 ; <i>y</i> ≥ 0 }.")

    _vd(ctx, "6", "vận dụng cao",
        "Bài toán tìm phương án tối ưu.",
        "Gọi <i>x</i> là số cây loại A, <i>y</i> là số cây loại B. Ràng buộc: 2<i>x</i> + <i>y</i> ≤ 10 "
        "(phân bón), <i>x</i> + 2<i>y</i> ≤ 8 (chất điều hòa), <i>x</i>, <i>y</i> ≥ 0. "
        "Thu nhập P = 3<i>x</i> + 4<i>y</i> (triệu đồng). "
        "Các đỉnh của miền nghiệm: O(0; 0), A(5; 0), B(4; 2), C(0; 4). "
        "Tính P: P(O) = 0; P(A) = 15; P(B) = 3·4 + 4·2 = 20; P(C) = 16. "
        "Giá trị lớn nhất là 20, đạt tại <i>x</i> = 4, <i>y</i> = 2.",
        "Thu nhập lớn nhất <b>20 triệu đồng</b>, đạt khi trồng 4 cây loại A và 2 cây loại B.",
        "Cách xác định đỉnh: B là giao điểm của <i>y</i> = 10 − 2<i>x</i> và <i>y</i> = (8 − <i>x</i>)/2, "
        "giải ra <i>x</i> = 4, <i>y</i> = 2.")

    ctx.h2("B.2.5. Lỗi thường gặp và cách tránh")
    ctx.box("Sáu lỗi hay mắc ở Chương 2", [
        "<b>1.</b> Vẽ đường thẳng nhưng không chọn điểm thử → tô sai nửa mặt phẳng.",
        "<b>2.</b> Quên rằng với dấu &lt; hoặc &gt; thì đường thẳng biên <b>không</b> thuộc miền nghiệm.",
        "<b>3.</b> Nhầm miền nghiệm của hệ là <b>hợp</b> thay vì <b>giao</b>.",
        "<b>4.</b> Lập hệ cho bài toán thực tế mà quên điều kiện <i>x</i> ≥ 0, <i>y</i> ≥ 0.",
        "<b>5.</b> Khi tìm giá trị lớn nhất chỉ thử ở gốc O mà không thử các đỉnh còn lại.",
        "<b>6.</b> Sai dấu khi chuyển điều kiện “không vượt quá” (≤) và “ít nhất là” (≥).",
    ], kind="err")

    _tuluyen(ctx, [
        "Phương trình nào sau đây là bất phương trình bậc nhất hai ẩn? A. 2<i>x</i> + 3<i>y</i> ≤ 6.  "
        "B. <i>x</i>² + <i>y</i>² = 4.  C. <i>x</i> + <i>y</i> = 0.  D. 3<i>x</i>² − 2<i>y</i> ≤ 5.",
        "Trong các cặp số sau, cặp nào <b>không</b> thuộc miền nghiệm của bất phương trình "
        "2<i>x</i> − <i>y</i> ≤ 3? A. (0; 0).  B. (2; 0).  C. (0; 4).  D. (3; 3).",
        "Miền nghiệm của bất phương trình <i>x</i> + <i>y</i> ≤ 4 là: "
        "A. nửa mặt phẳng chứa gốc O và chứa cả điểm trên đường thẳng biên.  "
        "B. nửa mặt phẳng chứa gốc O và không chứa điểm trên đường thẳng biên.  "
        "C. nửa mặt phẳng không chứa gốc O và không chứa điểm trên đường thẳng biên.  "
        "D. nửa mặt phẳng không chứa gốc O và có chứa điểm trên đường thẳng biên.",
        "Nghiệm của hệ bất phương trình bậc nhất hai ẩn là: A. hợp của các miền nghiệm.  "
        "B. giao của các miền nghiệm.  C. một nửa mặt phẳng.  D. một đường thẳng.",
        "Có 8 kg nguyên liệu A và 10 kg nguyên liệu B. Sản phẩm loại I cần 2 kg A và 3 kg B; "
        "sản phẩm loại II cần 3 kg A và 2 kg B. Lập hệ bất phương trình biểu diễn điều kiện sản xuất.",
        "Miền nghiệm của một hệ bất phương trình bậc nhất hai ẩn thường có dạng: "
        "A. một nửa mặt phẳng.  B. một đường thẳng.  C. giao của hai nửa mặt phẳng, là một miền kín.  "
        "D. tập rỗng.",
        "Cho hệ { <i>x</i> + <i>y</i> ≤ 5 ; <i>x</i> ≥ 0 ; <i>y</i> ≥ 0 }. Miền nghiệm có các đỉnh: "
        "A. (0; 0), (5; 0), (0; 5).  B. (5; 0), (0; 5).  C. (0; 0), (5; 5).  D. (5; 0), (0; 0).",
        "Trong miền nghiệm của hệ { <i>x</i> + <i>y</i> ≤ 5 ; <i>x</i> + 2<i>y</i> ≤ 8 ; "
        "<i>x</i> ≥ 0 ; <i>y</i> ≥ 0 }, giá trị lớn nhất của P = 2<i>x</i> + 3<i>y</i> là: "
        "A. 12.  B. 13.  C. 14.  D. 15.",
        "Miền nghiệm của hệ { 2<i>x</i> + <i>y</i> ≤ 10 ; <i>x</i> + 2<i>y</i> ≤ 8 ; <i>x</i> ≥ 0 ; "
        "<i>y</i> ≥ 0 } có đỉnh (4; 2). Đúng hay sai? Nếu sai thì giá trị lớn nhất của "
        "P = 3<i>x</i> + 4<i>y</i> bằng bao nhiêu?",
        "Có 12 kg phân bón và 9 kg chất điều hòa. Cây loại A cần 2 kg phân, 1 kg chất điều hòa, "
        "cho thu hoạch 3 triệu đồng/cây; cây loại B cần 1 kg phân, 2 kg chất điều hòa, cho thu hoạch "
        "4 triệu đồng/cây. Trồng bao nhiêu cây mỗi loại để thu nhập lớn nhất?",
    ], [
        "1. A.",
        "2. B (2·2 − 0 = 4 &gt; 3).",
        "3. B.",
        "4. B.",
        "5. { 2<i>x</i> + 3<i>y</i> ≤ 8 ; 3<i>x</i> + 2<i>y</i> ≤ 10 ; <i>x</i> ≥ 0 ; <i>y</i> ≥ 0 }.",
        "6. C.",
        "7. A.",
        "8. B (các đỉnh O(0;0), (5;0), (2;3), (0;4); P lần lượt bằng 0, 10, 13, 12).",
        "9. Đúng. Giá trị lớn nhất của P là 20, đạt tại (4; 2).",
        "10. Hệ { 2<i>x</i> + <i>y</i> ≤ 12 ; <i>x</i> + 2<i>y</i> ≤ 9 } (cùng <i>x</i>, <i>y</i> ≥ 0); "
        "P = 3<i>x</i> + 4<i>y</i> lớn nhất bằng 23 triệu đồng tại <i>x</i> = 5, <i>y</i> = 2.",
    ])


# ==========================================================================
def chuong_3(ctx):
    ctx.h1("B.3. CHƯƠNG 3. HỆ THỨC LƯỢNG TRONG TAM GIÁC  (Bài 5 – Bài 6)")

    ctx.box("Mục tiêu của chương", [
        "Định nghĩa và tính được các giá trị lượng giác của một góc từ 0° đến 180°.",
        "Thành thạo các hệ thức liên hệ giữa các giá trị lượng giác của hai góc bù nhau.",
        "Nắm vững định lí côsin, định lí sin và công thức tính diện tích tam giác.",
        "Giải được tam giác và vận dụng vào bài toán thực tiễn (đo chiều cao, đo khoảng cách "
        "giữa hai địa điểm).",
    ], kind="info")

    ctx.h2("B.3.1. Giá trị lượng giác của một góc từ 0° đến 180°")
    ctx.bullets([
        "Với 0° ≤ <i>α</i> ≤ 180°, lấy điểm M trên cung tròn đơn vị tâm O sao cho bán kính OM "
        "thuộc góc <i>α</i>; P là hình chiếu của M trên Ox, T là hình chiếu của M trên Oy.",
        "<b>sin <i>α</i></b> = <i>y</i><sub>M</sub> (khoảng cách có dấu từ M đến Ox); "
        "<b>cos <i>α</i></b> = <i>x</i><sub>M</sub>; <b>tan <i>α</i></b> = <i>y</i><sub>M</sub>/<i>x</i><sub>M</sub> "
        "(<i>x</i><sub>M</sub> ≠ 0); <b>cot <i>α</i></b> = <i>x</i><sub>M</sub>/<i>y</i><sub>M</sub> "
        "(<i>y</i><sub>M</sub> ≠ 0).",
        "Với 0° &lt; <i>α</i> &lt; 180°: sin <i>α</i> &gt; 0; cos <i>α</i> &gt; 0 nếu <i>α</i> &lt; 90°, "
        "= 0 nếu <i>α</i> = 90°, &lt; 0 nếu <i>α</i> &gt; 90°; tan <i>α</i> cùng dấu với cos <i>α</i>.",
    ])
    ctx.formula([
        "sin 0° = 0      cos 0° = 1      tan 0° = 0",
        "sin 30° = 1/2   cos 30° = √3/2    tan 30° = √3/3",
        "sin 45° = √2/2  cos 45° = √2/2    tan 45° = 1",
        "sin 60° = √3/2  cos 60° = 1/2      tan 60° = √3",
        "sin 90° = 1     cos 90° = 0        tan 90° không xác định",
        "sin 180° = 0    cos 180° = −1      cot 0° và cot 180° không xác định",
    ])
    ctx.h3("Quan hệ giữa hai góc bù nhau")
    ctx.formula([
        "Nếu <i>α</i> + <i>β</i> = 180° thì:",
        "sin <i>β</i> = sin(180° − <i>α</i>) = sin <i>α</i>",
        "cos <i>β</i> = cos(180° − <i>α</i>) = −cos <i>α</i>",
        "tan <i>β</i> = tan(180° − <i>α</i>) = −tan <i>α</i>",
    ])

    ctx.h2("B.3.2. Hệ thức lượng trong tam giác")
    ctx.p(
        "Cho tam giác ABC với các cạnh <i>a</i> = BC (đối góc A), <i>b</i> = CA (đối góc B), "
        "<i>c</i> = AB (đối góc C) và bán kính đường tròn ngoại tiếp là R."
    )
    ctx.h3("a) Định lí côsin")
    ctx.formula([
        "a² = b² + c² − 2bc·cos A        b² = a² + c² − 2ac·cos B        c² = a² + b² − 2ab·cos C",
        "Hệ quả:   cos A = (b² + c² − a²) / (2bc)      cos B = (a² + c² − b²) / (2ac)      "
        "cos C = (a² + b² − c²) / (2ab)",
    ])
    ctx.h3("b) Định lí sin")
    ctx.formula([
        "a / sin A = b / sin B = c / sin C = 2R",
    ])
    ctx.h3("c) Công thức tính diện tích tam giác")
    ctx.formula([
        "S = ½·a·h<sub>a</sub> = ½·b·h<sub>b</sub> = ½·c·h<sub>c</sub>",
        "S = ½·b·c·sin A = ½·a·c·sin B = ½·a·b·sin C",
    ])
    ctx.h3("d) Giải tam giác – chọn công thức đúng")
    ctx.table(
        [
            ["Dữ kiện đã biết", "Dùng công thức", "Lưu ý"],
            ["Hai cạnh và góc xen giữa", "Công thức côsin", "Tính cạnh thứ ba trước, rồi tính góc."],
            ["Hai góc và một cạnh", "Định lí sin", "Tính cạnh đối góc chưa biết trước."],
            ["Ba cạnh", "Công thức côsin", "Tính góc bằng hệ quả của công thức côsin."],
            ["Một cạnh và hai góc", "Định lí sin", "Tính góc thứ ba rồi tính cạnh còn lại."],
            ["Một cạnh và một góc đối diện", "Định lí sin", "Có thể có hai nghiệm – phải xét điều kiện."],
        ],
        widths=[160, 130, W - 290],
        align=["l", "l", "l"],
    )
    ctx.caption("Bảng 9. Bảng tra công thức khi giải tam giác.")

    ctx.h2("B.3.3. Dạng bài toán điển hình và lời giải mẫu")

    _vd(ctx, "1", "nhận biết",
        "Xác định dấu của các giá trị lượng giác.",
        "Với 90° &lt; <i>α</i> &lt; 180°: góc nằm ở góc phần hai nên sin <i>α</i> &gt; 0 (trục tung "
        "đứng) và cos <i>α</i> &lt; 0 (trục hoành nằm bên trái); tan <i>α</i> &lt; 0.",
        "B. sin <i>α</i> &gt; 0 và cos <i>α</i> &lt; 0.")

    _vd(ctx, "2", "nhận biết – thông hiểu",
        "Quan hệ giữa các giá trị lượng giác của hai góc bù nhau.",
        "<i>α</i> và <i>β</i> bù nhau khi <i>α</i> + <i>β</i> = 180°. Theo bảng giá trị lượng giác: "
        "sin 30° = 1/2 và sin 150° = 1/2 (bù nhau); cos 30° = √3/2 và cos 150° = −√3/2 (ngược dấu); "
        "tan 30° = √3/3 và tan 150° = −√3/3.",
        "sin <i>α</i> = sin <i>β</i>; cos <i>α</i> = −cos <i>β</i>; tan <i>α</i> = −tan <i>β</i>.")

    _vd(ctx, "3", "thông hiểu",
        "Tính giá trị lượng giác của một góc khi biết một giá trị lượng giác.",
        "Cho 0° &lt; <i>α</i> &lt; 180° và sin <i>α</i> = 1/2. Vì <i>α</i> thuộc (0°; 180°) nên có hai "
        "khả năng <i>α</i> = 30° hoặc <i>α</i> = 150°. Dùng công thức "
        "sin²<i>α</i> + cos²<i>α</i> = 1: cos²<i>α</i> = 1 − 1/4 = 3/4 nên |cos <i>α</i>| = √3/2. "
        "Với <i>α</i> = 30°: cos <i>α</i> = √3/2, tan <i>α</i> = √3/3; với <i>α</i> = 150°: "
        "cos <i>α</i> = −√3/2, tan <i>α</i> = −√3/3.",
        "cos <i>α</i> = ±√3/2 và tan <i>α</i> = ±√3/3 (cùng dấu).")

    _vd(ctx, "4", "nhận biết",
        "Định lí côsin – công thức cần nhớ.",
        "Theo định lí côsin: bình phương một cạnh bằng tổng bình phương hai cạnh còn lại trừ đi hai "
        "lần tích của hai cạnh đó nhân với côsin của góc xen giữa chúng. Với góc A và cạnh a đối "
        "góc A: a² = b² + c² − 2bc·cos A.",
        "A. a² = b² + c² − 2bc·cos A.")

    _vd(ctx, "5", "thông hiểu",
        "Tính cạnh chưa biết và góc chưa biết của tam giác.",
        "Tam giác ABC có a = BC = 5, b = CA = 8, C = 60°. Áp dụng công thức côsin: "
        "c² = a² + b² − 2ab·cos C = 25 + 64 − 2·5·8·(1/2) = 89 − 40 = 49 ⇒ c = 7. "
        "Góc A: cos A = (b² + c² − a²)/(2bc) = (64 + 49 − 25)/(2·8·7) = 88/112 = 11/14 ⇒ "
        "A ≈ 38,2°.",
        "c = 7;  A ≈ 38,2°.")

    _vd(ctx, "6", "thông hiểu",
        "Tính diện tích tam giác.",
        "Với tam giác ở ví dụ 5: S = ½·a·b·sin C = ½·5·8·(√3/2) = 10√3 ≈ 17,32 (đơn vị diện tích).",
        "S = 10√3 ≈ 17,32.")

    _vd(ctx, "7", "vận dụng",
        "Bài toán thực tiễn: chiều cao của tháp và góc ngướng.",
        "Chiếc tháp có chiều cao 20 m, chân tháp cách điểm B 30 m. Tam giác ABC vuông tại C "
        "(AC = 20, BC = 30). Theo định lí Pythagoras: AB = √(20² + 30²) = √1300 = 10√13 ≈ 36,06 m. "
        "Góc ngướng α = ∠ABC nên tan α = AC/BC = 20/30 = 2/3 ⇒ α ≈ 33,69° ≈ 34°.",
        "AB = 10√13 ≈ 36,06 m;  α ≈ 34°.")

    _vd(ctx, "8", "vận dụng",
        "Bài toán thực tiễn: đo chiều cao của vật khi không thể đo trực tiếp.",
        "Người đo đứng tại A, ngắm đỉnh nhà B qua đỉnh cây C (C nằm giữa A và B), AB = 30 m, "
        "AC = 20 m, góc BAC = 30°. Vì BC ⊥ AB nên chiều cao nhà bằng BC = AB·sin 30° = 30·(1/2) = 15 m.",
        "Chiều cao ngôi nhà là 15 m.")

    ctx.h2("B.3.4. Lỗi thường gặp và cách tránh")
    ctx.box("Sáu lỗi hay mắc ở Chương 3", [
        "<b>1.</b> Nhầm tan(180° − <i>α</i>) = tan <i>α</i> → thực ra bằng −tan <i>α</i>.",
        "<b>2.</b> Dùng định lí sin khi chưa biết góc nào ứng với cạnh nào.",
        "<b>3.</b> Quên điều kiện xác định: tan <i>α</i> cần <i>x</i><sub>M</sub> ≠ 0, cot <i>α</i> "
        "cần <i>y</i><sub>M</sub> ≠ 0.",
        "<b>4.</b> Trong công thức côsin, nhầm cạnh đối góc (a đối A, b đối B, c đối C).",
        "<b>5.</b> Tính diện tích bằng ½ab·sin C nhưng a, b lại không chứa góc C ở giữa.",
        "<b>6.</b> Bấm máy tính ở chế độ RAD thay vì DEG → kết quả sai hoàn toàn.",
    ], kind="err")

    _tuluyen(ctx, [
        "Cho <i>α</i> ∈ (90°; 180°). Mệnh đề nào sau đây đúng? A. sin <i>α</i> &gt; 0 và cos <i>α</i> &gt; 0.  "
        "B. sin <i>α</i> &gt; 0 và cos <i>α</i> &lt; 0.  C. sin <i>α</i> &lt; 0 và cos <i>α</i> &lt; 0.  "
        "D. tan <i>α</i> &gt; 0.",
        "Tính sin 30° + cos 60°: A. 1.  B. 1/2.  C. √3/2.  D. 2.",
        "Nếu <i>α</i> + <i>β</i> = 180° thì mệnh đề nào đúng? A. sin <i>α</i> = sin <i>β</i>.  "
        "B. cos <i>α</i> = cos <i>β</i>.  C. tan <i>α</i> = tan <i>β</i>.  D. sin <i>α</i> = −sin <i>β</i>.",
        "Tính cos 135°: A. −√2/2.  B. √2/2.  C. −1/2.  D. 1/2.",
        "Tam giác ABC có a = 7, b = 8, C = 60°. Tính c.",
        "Tam giác ABC có a = 5, b = 8, C = 60°. Tính diện tích tam giác ABC.",
        "Tam giác ABC có a = 5, b = 8, C = 60°. Tính số đo góc A (làm tròn đến độ).",
        "Tam giác vuông cân ABC có cạnh huyền bằng 10. Tính diện tích tam giác ABC.",
        "Chiếc tháp cao 20 m được quan sát từ điểm cách chân tháp 30 m. Tính khoảng cách từ mắt "
        "người quan sát đến đỉnh tháp và số đo góc ngướng (làm tròn đến độ).",
        "Để đo chiều cao của một ngôi nhà, người ta đứng tại A và ngắm đỉnh nhà B qua đỉnh cây C; "
        "biết AB = 30 m, AC = 20 m, góc BAC = 30°. Tính chiều cao ngôi nhà.",
    ], [
        "1. B.",
        "2. A (1/2 + 1/2 = 1).",
        "3. A.",
        "4. A (135° = 180° − 45° nên cos 135° = −cos 45° = −√2/2).",
        "5. c² = 49 + 64 − 2·7·8·(1/2) = 57 ⇒ c = √57 ≈ 7,55.",
        "6. S = ½·5·8·sin 60° = 10√3 ≈ 17,32.",
        "7. cos A = (64 + 49 − 25)/112 = 11/14 ⇒ A ≈ 38,2°.",
        "8. Hai cạnh huyền... cạnh vuông = 10/√2 = 5√2; S = ½·(5√2)² = 25.",
        "9. AB = 10√13 ≈ 36,06 m; góc ngướng ≈ 34°.",
        "10. BC = AB·sin 30° = 15 m.",
    ])


# ==========================================================================
def chuong_4(ctx):
    ctx.h1("B.4. CHƯƠNG 4. VECTƠ  (Bài 7. Các khái niệm mở đầu)")

    ctx.box("Mục tiêu của chương", [
        "Biết khái niệm vectơ, cách biểu diễn vectơ bằng hình vẽ và bằng cặp điểm.",
        "Nhận biết độ dài vectơ, phương vectơ, hướng vectơ; vectơ-không.",
        "Nhận biết hai vectơ cùng phương, hai vectơ cùng hướng, hai vectơ bằng nhau, hai vectơ đối nhau.",
        "Chứng minh được hai vectơ bằng nhau trong một số trường hợp đơn giản.",
    ], kind="info")

    ctx.h2("B.4.1. Khái niệm vectơ")
    ctx.bullets([
        "<b>Vectơ</b> là một đại lượng hình học có <b>độ lớn</b> và <b>hướng</b>.",
        "Biểu diễn vectơ bằng hình vẽ: một mũi tên có điểm đầu và điểm cuối. Biểu diễn bằng kí "
        "hiệu: <b>vectơ AB</b> có điểm đầu A, điểm cuối B (đọc là “vectơ A B”).",
        "Các đại lượng vectơ: <b>độ dài</b> |AB| (khoảng cách giữa A và B), <b>phương</b> "
        "(đường thẳng chứa vectơ), <b>hướng</b> (chiều của mũi tên).",
        "Các đại lượng không phải là vectơ: khối lượng, thể tích, diện tích, tốc độ (đơn vị kg, m³, "
        "m², km/h…) vì chỉ có độ lớn, không có hướng.",
    ])
    ctx.formula([
        "Hai vectơ <b>cùng phương</b>: đường thẳng chứa chúng song song hoặc trùng nhau.",
        "Hai vectơ <b>cùng hướng</b>: cùng phương và cùng chiều.",
        "Hai vectơ <b>bằng nhau</b>: có cùng độ dài và cùng hướng  (ký hiệu <b>a</b> = <b>b</b>).",
        "Hai vectơ <b>đối nhau</b>: có cùng độ dài và ngược hướng.",
        "<b>Vectơ-không</b> (ký hiệu <b>0</b>): vectơ có điểm đầu và điểm cuối trùng nhau, "
        "độ dài bằng 0; <b>cùng phương và cùng hướng với mọi vectơ</b>.",
    ])
    ctx.box("Phân biệt thật rõ", [
        "<b>Cùng phương</b> ≠ <b>cùng hướng</b>: hai vectơ cùng phương có thể ngược hướng.",
        "<b>Bằng nhau</b> ⊂ <b>cùng hướng</b>: hai vectơ cùng hướng chưa chắc bằng nhau "
        "(độ dài có thể khác).",
        "<b>Đối nhau</b> ≠ <b>bằng nhau</b>: hai vectơ đối nhau có cùng độ dài nhưng ngược hướng.",
    ], kind="grey")

    ctx.h2("B.4.2. Dạng bài toán điển hình và lời giải mẫu")

    _vd(ctx, "1", "nhận biết",
        "Phân biệt đại lượng vectơ và đại lượng không phải vectơ.",
        "Vectơ phải có cả độ lớn và hướng. “Quãng đường xe ô tô đi từ A đến B” có cả độ dài và "
        "hướng (từ A sang B) nên là vectơ. “Tốc độ” của xe chỉ có độ lớn (km/h) nên không phải "
        "vectơ (cần nói <i>vận tốc</i> mới là vectơ). “Khối lượng”, “nhiệt độ” cũng không phải vectơ.",
        "B. Quãng đường ô tô đi từ A đến B.")

    _vd(ctx, "2", "nhận biết",
        "Điều kiện để hai vectơ bằng nhau.",
        "Theo định nghĩa: hai vectơ bằng nhau khi chúng có cùng độ dài và cùng hướng. "
        "Chỉ cần một trong hai điều kiện đó thì chưa đủ (ví dụ hai vectơ cùng độ dài nhưng ngược "
        "hướng là hai vectơ đối nhau, không phải bằng nhau).",
        "A. Có cùng độ dài và cùng hướng.")

    _vd(ctx, "3", "nhận biết",
        "Đặc điểm của vectơ-không.",
        "Vectơ-không có điểm đầu và điểm cuối trùng nhau nên độ dài bằng 0. Về phương và hướng, "
        "vectơ-không được coi là có cùng phương và cùng hướng với mọi vectơ.",
        "B. Có độ dài bằng 0 và cùng phương, cùng hướng với mọi vectơ.")

    _vd(ctx, "4", "thông hiểu",
        "Chứng minh hai vectơ bằng nhau.",
        "Cho hình bình hành ABCD. Theo tính chất hình bình hành: AB ∥ DC và AB = DC. Vậy hai vectơ "
        "AB và DC có cùng phương (hai đường thẳng song song) và cùng hướng (chiều A → B và D → C "
        "cùng chiều), đồng thời có cùng độ dài. Theo định nghĩa, hai vectơ bằng nhau.",
        "Vectơ AB = vectơ DC.")

    _vd(ctx, "5", "thông hiểu",
        "Phân biệt vectơ bằng nhau và vectơ đối nhau.",
        "Cho M là trung điểm của đoạn thẳng BC. Khi đó MB = MC (độ dài bằng nhau) nhưng hai vectơ "
        "MB và MC <b>ngược hướng</b> (M → B và M → C là hai chiều đối nhau trên cùng một đường "
        "thẳng). Vì vậy MB và MC là hai vectơ <b>đối nhau</b>, không phải hai vectơ bằng nhau.",
        "Hai vectơ MB và MC đối nhau nhau.")

    ctx.h2("B.4.3. Lỗi thường gặp và cách tránh")
    ctx.box("Năm lỗi hay mắc ở Chương 4", [
        "<b>1.</b> Cho rằng “cùng phương” đã đủ để hai vectơ bằng nhau → thiếu điều kiện cùng độ dài.",
        "<b>2.</b> Nhầm “cùng phương” với “cùng hướng”.",
        "<b>3.</b> Nghĩ vectơ-không không có phương, không có hướng → thực tế vectơ-không cùng phương "
        "và cùng hướng với mọi vectơ.",
        "<b>4.</b> Nhầm hai vectơ đối nhau với hai vectơ bằng nhau.",
        "<b>5.</b> Tưởng vectơ AB và vectơ BA là bằng nhau → chúng đối nhau nhau.",
    ], kind="err")

    _tuluyen(ctx, [
        "Trong các đại lượng sau, đại lượng nào là vectơ? A. Khối lượng của người A.  "
        "B. Lực kéo.  C. Thể tích bình.  D. Tốc độ của xe.",
        "Về phương và hướng, vectơ-không: A. không có phương và không có hướng.  "
        "B. có cùng phương và cùng hướng với mọi vectơ.  C. chỉ có cùng phương với mọi vectơ.  "
        "D. chỉ có cùng hướng với mọi vectơ.",
        "Hai vectơ có cùng độ dài thì: A. chúng bằng nhau.  B. chúng cùng phương.  "
        "C. chúng cùng hướng.  D. chưa kết luận được gì về phương và hướng.",
        "Vectơ AB và vectơ BA: A. bằng nhau.  B. đối nhau nhau.  C. cùng phương.  D. không xác định.",
        "Hai vectơ bằng nhau thì: A. có cùng độ dài nhưng ngược hướng.  B. có cùng độ dài và cùng "
        "hướng.  C. có độ dài khác nhau.  D. chỉ cần cùng phương là đủ.",
        "“Hai vectơ cùng phương” nghĩa là: A. hai đường thẳng chứa chúng song song hoặc trùng nhau.  "
        "B. chúng có cùng độ dài.  C. chúng có cùng hướng.  D. chúng có cùng điểm đầu.",
        "Cho hình bình hành ABCD. Vectơ nào sau đây bằng vectơ AB? A. vectơ CD.  B. vectơ DC.  "
        "C. vectơ BA.  D. vectơ CA.",
        "Hai vectơ <b>a</b> và <b>b</b> cùng phương nhưng ngược hướng và có cùng độ dài. Khi đó "
        "<b>a</b> và <b>b</b>: A. bằng nhau.  B. đối nhau nhau.  C. không thể kết luận.  D. cùng hướng.",
        "Vectơ-không: A. chỉ có độ dài bằng 0.  B. có độ dài bằng 0, đồng thời cùng phương và cùng "
        "hướng với mọi vectơ.  C. có độ dài bằng 1.  D. không tồn tại.",
        "Cho M là trung điểm của đoạn thẳng AB. Cặp vectơ nào sau đây là hai vectơ đối nhau nhau? "
        "A. vectơ MA và vectơ MB.  B. vectơ AM và vectơ AB.  C. vectơ AM và vectơ BM.  "
        "D. vectơ MA và vectơ AB.",
    ], [
        "1. B.",
        "2. B.",
        "3. D.",
        "4. B.",
        "5. B.",
        "6. A.",
        "7. B.",
        "8. B.",
        "9. B.",
        "10. A (MA và MB cùng độ dài, ngược hướng).",
    ])


def phan_b(ctx):
    ctx.h1("PHẦN B. KIẾN THỨC NỀN TẢNG VÀ DẠNG BÀI THEO TỪNG CHƯƠNG")
    ctx.p(
        "Mỗi chương được trình bày theo cùng một bố cục: <b>mục tiêu</b> → <b>tóm tắt lý thuyết</b> → "
        "<b>công thức cần nhớ</b> → <b>dạng bài toán điển hình kèm lời giải mẫu</b> → "
        "<b>lỗi thường gặp</b> → <b>bài tập tự luyện có đáp án</b>. "
        "Các ví dụ được chọn đúng theo các mức độ nhận thức NB – TH – VD – VDC như bảng đặc tả ở A.4."
    )
    ctx.table(
        [
            ["Chương", "Bài học trong sách “Kết nối tri thức”", "Nội dung chính trong đề cương"],
            ["Chương 1. Mệnh đề và tập hợp", "Bài 1. Mệnh đề; Bài 2. Tập hợp và các phép toán trên tập hợp",
             "Mệnh đề, mệnh đề chứa biến, phủ định, kéo theo – đảo, tương đương, điều kiện cần – đủ; "
             "tập hợp, tập con, tập rỗng, kí hiệu khoảng – đoạn; biểu đồ Ven; giao, hợp, phần bù, hiệu; "
             "số tập hợp con."],
            ["Chương 2. Bất phương trình và hệ bất phương trình bậc nhất hai ẩn",
             "Bài 3. Bất phương trình bậc nhất hai ẩn; Bài 4. Hệ bất phương trình bậc nhất hai ẩn",
             "Nghiệm và miền nghiệm của bất phương trình; hình học của hệ; bài toán thực tế; "
             "bài toán tối ưu trên miền nghiệm."],
            ["Chương 3. Hệ thức lượng trong tam giác",
             "Bài 5. Giá trị lượng giác của một góc từ 0° đến 180°; Bài 6. Hệ thức lượng trong tam giác",
             "Giá trị lượng giác và dấu; quan hệ giữa góc bù nhau; định lí côsin, định lí sin, "
             "diện tích tam giác; giải tam giác và ứng dụng thực tiễn."],
            ["Chương 4. Vectơ", "Bài 7. Các khái niệm mở đầu",
             "Vectơ, vectơ-không, độ dài, phương, hướng; cùng phương, cùng hướng, bằng nhau, đối nhau; "
             "chứng minh hai vectơ bằng nhau."],
        ],
        widths=[104, 150, W - 254],
        align=["l", "l", "l"],
    )
    ctx.caption("Bảng 8. Bản đồ từ chương trình sang đề cương ôn tập.")
    ctx.page_break()

    chuong_1(ctx)
    ctx.page_break()
    chuong_2(ctx)
    ctx.page_break()
    chuong_3(ctx)
    ctx.page_break()
    chuong_4(ctx)
