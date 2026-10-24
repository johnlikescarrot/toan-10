# -*- coding: utf-8 -*-
"""
PHẦN C – ĐỀ KIỂM TRA GIỮA HỌC KỲ I (21 câu, có đáp án)
PHẦN D – ĐÁP ÁN CHI TIẾT
PHẦN E – PHỤ LỤC
"""

W = 498.0

from dung_pdf import XANH_SANG


# ==========================================================================
# PHẦN C – ĐỀ THI
# ==========================================================================

def phan_c(ctx):
    ctx.h1("PHẦN C. ĐỀ KIỂM TRA GIỮA HỌC KỲ I NĂM HỌC 2026-2027")
    ctx.p(
        "Đề dưới đây được dựng hoàn toàn theo ma trận và bảng đặc tả của tài liệu nguồn "
        "(xem Phần A). Thí sinh làm bài trong <b>90 phút</b>, không dùng tài liệu."
    )
    ctx.box("THÔNG TIN ĐỀ THI", [
        "<b>Môn:</b> Toán   |   <b>Lớp:</b> 10   |   <b>Năm học:</b> 2026-2027   |   "
        "<b>Thời gian:</b> 90 phút",
        "<b>Tổng điểm:</b> 10,0   |   <b>Số câu:</b> 21   |   <b>Phần I:</b> 12 câu – 3,0 điểm   |   "
        "<b>Phần II:</b> 2 câu – 2,0 điểm   |   <b>Phần III:</b> 4 câu – 2,0 điểm   |   "
        "<b>Phần IV:</b> 3 câu – 3,0 điểm",
    ], kind="grey")

    # ---------------- PHẦN I ----------------
    ctx.h2("PHẦN I. TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN")
    ctx.p(
        "Chọn một phương án đúng nhất trong bốn phương án đã cho. <i>(3,0 điểm – mỗi câu 0,25 điểm)</i>"
    )
    ctx.question(
        1,
        "Trong các phát biểu sau, phát biểu nào là mệnh đề chứa biến?",
        ["A. 2 + 3 = 5.",
         "B. 3<i>x</i> + 5 &gt; 11.",
         "C. Hà Nội là thủ đô của Việt Nam.",
         "D. Em rất thích môn Toán."],
        points="0,25 điểm",
    )
    ctx.question(
        2,
        "Trong các mệnh đề sau, mệnh đề nào đúng?",
        ["A. ∀<i>x</i> ∈ ℝ: <i>x</i>² + 1 ≤ 0.",
         "B. ∃<i>x</i> ∈ ℝ: <i>x</i>² + 1 ≤ 0.",
         "C. ∀<i>x</i> ∈ ℝ: <i>x</i>² + 1 &gt; 0.",
         "D. ∃<i>x</i> ∈ ℝ: <i>x</i>² + 1 &lt; 0."],
        points="0,25 điểm",
    )
    ctx.question(
        3,
        "Tập hợp nào sau đây là tập rỗng?",
        ["A. {<i>x</i> ∈ ℝ | <i>x</i>² − 4 = 0}.",
         "B. {<i>x</i> ∈ ℝ | <i>x</i>² ≥ 0}.",
         "C. {<i>x</i> ∈ ℝ | <i>x</i>² + 1 = 0}.",
         "D. {<i>x</i> ∈ ℝ | <i>x</i>² − 2<i>x</i> + 1 = 0}."],
        points="0,25 điểm",
    )
    ctx.question(
        4,
        "Cho A = {1; 2; 3; 4}, B = {3; 4; 5}. Tập hợp A ∩ B và A ∪ B lần lượt là:",
        ["A. {3; 4} và {1; 2; 3; 4; 5}.",
         "B. {1; 2; 5} và {1; 2; 3; 4; 5}.",
         "C. {3; 4; 5} và {1; 2; 3; 4}.",
         "D. {1; 2} và {3; 4; 5}."],
        points="0,25 điểm",
    )
    ctx.question(
        5,
        "Trong các bất phương trình sau, bất phương trình nào là bất phương trình bậc nhất hai ẩn?",
        ["A. 2<i>x</i> + 3<i>y</i> ≤ 5.",
         "B. <i>x</i>² + <i>y</i>² = 1.",
         "C. <i>x</i> + <i>y</i> = 0.",
         "D. 3<i>x</i>² − 2<i>y</i> ≤ 7."],
        points="0,25 điểm",
    )
    ctx.question(
        6,
        "Mệnh đề nào sau đây mô tả <b>đúng</b> tập nghiệm của một hệ bất phương trình bậc nhất hai ẩn?",
        ["A. Là hợp của các miền nghiệm của các bất phương trình trong hệ.",
         "B. Là giao của các miền nghiệm của các bất phương trình trong hệ.",
         "C. Là một nửa mặt phẳng có chứa đường thẳng biên.",
         "D. Là một đường thẳng."],
        points="0,25 điểm",
    )
    ctx.question(
        7,
        "Với góc α có 0° ≤ α ≤ 180°, mệnh đề nào sau đây đúng?",
        ["A. tan α luôn tồn tại và có giá trị dương.",
         "B. cot α luôn tồn tại.",
         "C. −1 ≤ cos α ≤ 1.",
         "D. sin α luôn lấy giá trị âm."],
        points="0,25 điểm",
    )
    ctx.question(
        8,
        "Cho góc α (0° &lt; α &lt; 180°) thỏa mãn sin α = 1/2. Tính cos α.",
        ["A. cos α = √3/2.",
         "B. cos α = −√3/2.",
         "C. cos α = ±√3/2.",
         "D. cos α = ±1/2."],
        points="0,25 điểm",
    )
    ctx.question(
        9,
        "Trong tam giác ABC, cạnh <i>a</i> đối góc A. Công thức nào sau đây là công thức định lí côsin?",
        ["A. a² = b² + c² + 2bc·cos A.",
         "B. a² = b² + c² − 2bc·cos A.",
         "C. a² = b² + c² − 2bc·sin A.",
         "D. a = b + c − 2bc·cos A."],
        points="0,25 điểm",
    )
    ctx.question(
        10,
        "Cho tam giác ABC có BC = 6, CA = 8, AB = 5. Tính cos A.",
        ["A. 53/80.",
         "B. −1/20.",
         "C. 25/32.",
         "D. 3/4."],
        points="0,25 điểm",
    )
    ctx.question(
        11,
        "Hai vectơ <b>a</b> và <b>b</b> được gọi là bằng nhau khi:",
        ["A. chúng có cùng độ dài.",
         "B. chúng có cùng hướng.",
         "C. chúng có cùng độ dài và cùng hướng.",
         "D. chúng có cùng điểm đầu."],
        points="0,25 điểm",
    )
    ctx.question(
        12,
        "Cho hình bình hành ABCD. Mệnh đề nào sau đây đúng?",
        ["A. vectơ AB = vectơ CD.",
         "B. vectơ AB = vectơ DC.",
         "C. vectơ AC = vectơ BD.",
         "D. vectơ AD = vectơ BC."],
        points="0,25 điểm",
    )

    # ---------------- PHẦN II ----------------
    ctx.h2("PHẦN II. TRẮC NGHIỆM ĐÚNG SAI")
    ctx.p(
        "Trong mỗi câu, đánh dấu <b>Đ</b> nếu ý đó đúng và <b>S</b> nếu ý đó sai. "
        "<i>(2,0 điểm – trong mỗi câu: đúng 1 ý 0,1 điểm; đúng 2 ý 0,25 điểm; "
        "đúng 3 ý 0,5 điểm; đúng 4 ý 1,0 điểm)</i>"
    )
    ctx.question(
        13,
        "a) Nếu <i>x</i> ∈ A và <i>x</i> ∈ B thì <i>x</i> ∈ A ∩ B.",
        ["b) Nếu A ⊂ B thì A ∩ B = A.",
         "c) Tập hợp [<i>a</i>; <i>b</i>) với <i>a</i> &lt; <i>b</i> gồm các số <i>x</i> thỏa mãn "
         "<i>a</i> ≤ <i>x</i> &lt; <i>b</i>.",
         "d) Hai tập hợp bằng nhau khi chúng có cùng số phần tử."],
        points="1,0 điểm",
    )
    ctx.question(
        14,
        "a) Bất phương trình 2<i>x</i> − 3<i>y</i> ≤ 6 là bất phương trình bậc nhất hai ẩn.",
        ["b) Miền nghiệm của bất phương trình <i>ax</i> + <i>by</i> + <i>c</i> ≤ 0 "
         "(<i>a</i>, <i>b</i> không đồng thời bằng 0) là một nửa mặt phẳng không chứa đường thẳng "
         "<i>ax</i> + <i>by</i> + <i>c</i> = 0.",
         "c) Nghiệm của hệ bất phương trình bậc nhất hai ẩn là giao của các miền nghiệm của các "
         "bất phương trình trong hệ.",
         "d) Miền nghiệm của một hệ bất phương trình bậc nhất hai ẩn luôn là một nửa mặt phẳng."],
        points="1,0 điểm",
    )

    # ---------------- PHẦN III ----------------
    ctx.h2("PHẦN III. TRẮC NGHIỆM TRẢ LỜI NGẮN")
    ctx.p("<i>(2,0 điểm – mỗi câu 0,5 điểm)</i>")
    ctx.question(
        15,
        "Tập hợp A có 4 phần tử. Số tập hợp con của A (kể cả tập rỗng và chính tập A) bằng "
        "bao nhiêu?",
        points="0,5 điểm",
    )
    ctx.question(
        16,
        "Lớp 10A có 45 học sinh, trong đó 28 học sinh tham gia CLB Văn nghệ, 20 học sinh tham "
        "gia CLB Toán và có 8 học sinh tham gia cả hai CLB. Hỏi có bao nhiêu học sinh không tham gia "
        "CLB nào?",
        points="0,5 điểm",
    )
    ctx.question(
        17,
        "Cho góc α (0° &lt; α &lt; 180°) thỏa mãn sin α = 1/2. Tính giá trị của biểu thức "
        "P = 4cos²α + 3sin²α.",
        points="0,5 điểm",
    )
    ctx.question(
        18,
        "Cho tam giác ABC có BC = 5, CA = 7, AB = 8. Tính diện tích tam giác ABC.",
        points="0,5 điểm",
    )

    # ---------------- PHẦN IV ----------------
    ctx.h2("PHẦN IV. TỰ LUẬN")
    ctx.p("<i>(3,0 điểm – mỗi câu 1,0 điểm)</i>")
    ctx.question(
        19,
        "Cho A = {1; 2; 3; 4; 5}, B = {3; 4; 5; 6} và U = {1; 2; 3; 4; 5; 6; 7}. "
        "Tính A ∩ B, A ∪ B, A \\ B và phần bù của A trong U.",
        points="1,0 điểm – MĐ2",
    )
    ctx.question(
        20,
        "Một chiếc tháp có chiều cao 20 m. Người ta đi từ chân tháp đến điểm B cách chân tháp "
        "30 m rồi ngắm đỉnh tháp A (tháp vuông góc với mặt đất).",
        ["a) Tính khoảng cách AB.",
         "b) Tính số đo góc ngướng α = ∠ABC (làm tròn kết quả đến độ)."],
        points="1,0 điểm – MĐ2",
    )
    ctx.question(
        21,
        "Một xưởng sản xuất hai loại sản phẩm A và B. Để sản xuất <i>x</i> kg sản phẩm A và "
        "<i>y</i> kg sản phẩm B (<i>x</i>, <i>y</i> ≥ 0) thì cần dùng 2<i>x</i> + 3<i>y</i> (kg) "
        "nguyên liệu loại I và 4<i>x</i> + <i>y</i> (kg) nguyên liệu loại II. Kho có 14 kg nguyên "
        "liệu loại I và 12 kg nguyên liệu loại II.",
        ["a) Lập hệ bất phương trình biểu diễn điều kiện của bài toán.",
         "b) Biểu diễn miền nghiệm của hệ đó trên mặt phẳng tọa độ Oxy.",
         "c) Tìm giá trị lớn nhất của S = 3<i>x</i> + 2<i>y</i> (giá trị sản phẩm) trong miền "
         "nghiệm đó."],
        points="1,0 điểm – MĐ3",
    )


# ==========================================================================
# PHẦN D – ĐÁP ÁN CHI TIẾT
# ==========================================================================

def phan_d(ctx):
    ctx.h1("PHẦN D. ĐÁP ÁN CHI TIẾT CHO ĐỀ KIỂM TRA GIỮA HỌC KỲ I 2026-2027")

    ctx.h2("D.1. Đáp án Phần I – Trắc nghiệm nhiều phương án lựa chọn (3,0 điểm)")
    ctx.table(
        [
            ["Câu", "A", "B", "C", "D", "Câu", "A", "B", "C", "D"],
            ["1", "B", "", "", "", "7", "C", "", "", ""],
            ["2", "", "", "C", "", "8", "", "", "C", ""],
            ["3", "", "", "C", "", "9", "", "B", "", ""],
            ["4", "A", "", "", "", "10", "A", "", "", ""],
            ["5", "A", "", "", "", "11", "", "", "C", ""],
            ["6", "", "B", "", "", "12", "", "B", "", ""],
        ],
        widths=[30, 30, 30, 30, 30, 30, 30, 30, 30, 30],
        align=["c"] * 10,
        head_bg=XANH_SANG,
    )
    ctx.caption("Bảng 10. Đáp án Phần I (mỗi câu 0,25 điểm; tổng 3,0 điểm).")

    ctx.h3("Giải thích ngắn từng câu (Phần I)")
    ctx.numbered([
        "<b>Câu 1 – B.</b> “3<i>x</i> + 5 &gt; 11” chưa xác định được tính đúng hay sai khi chưa "
        "cho giá trị của <i>x</i>. A và C là mệnh đề đã xác định được tính đúng/sai; D là câu cảm "
        "thán, không phải mệnh đề.",
        "<b>Câu 2 – C.</b> Với mọi số thực <i>x</i> ta luôn có <i>x</i>² ≥ 0 nên <i>x</i>² + 1 &gt; 0. "
        "Phương án A và D sai; B sai vì <i>x</i>² + 1 ≥ 1 &gt; 0 với mọi <i>x</i>.",
        "<b>Câu 3 – C.</b> <i>x</i>² + 1 ≥ 1 nên <i>x</i>² + 1 = 0 không có nghiệm thực → tập rỗng. "
        "A = {−2; 2}, B = ℝ, D = {1}.",
        "<b>Câu 4 – A.</b> A ∩ B là tập các phần tử chung {3; 4}; A ∪ B là tập các phần tử thuộc "
        "A hoặc B {1; 2; 3; 4; 5}.",
        "<b>Câu 5 – A.</b> 2<i>x</i> + 3<i>y</i> ≤ 5 có dạng <i>ax</i> + <i>by</i> + <i>c</i> ≤ 0 với "
        "<i>a</i>, <i>b</i> không đồng thời bằng 0. B là phương trình bậc hai; C là phương trình (không "
        "phải bất phương trình); D có <i>x</i>² nên không phải bậc nhất.",
        "<b>Câu 6 – B.</b> Nghiệm của hệ là tập các điểm thỏa mãn cả hai bất phương trình, tức là "
        "giao của hai miền nghiệm.",
        "<b>Câu 7 – C.</b> Với mọi góc có giá trị lượng giác trong [0°; 180°] ta có "
        "−1 ≤ cos α ≤ 1. A sai vì tan 90° không xác định; B sai vì cot 0° và cot 180° không xác "
        "định; D sai vì sin α ≥ 0.",
        "<b>Câu 8 – C.</b> 0° &lt; α &lt; 180° và sin α = 1/2 cho α = 30° hoặc α = 150°. Dùng "
        "sin²α + cos²α = 1: cos²α = 1 − 1/4 = 3/4 nên cos α = ±√3/2.",
        "<b>Câu 9 – B.</b> Định lí côsin: a² = b² + c² − 2bc·cos A.",
        "<b>Câu 10 – A.</b> a = BC = 6, b = CA = 8, c = AB = 5. "
        "cos A = (b² + c² − a²)/(2bc) = (64 + 25 − 36)/(2·8·5) = 53/80.",
        "<b>Câu 11 – C.</b> Định nghĩa: hai vectơ bằng nhau khi có cùng độ dài và cùng hướng.",
        "<b>Câu 12 – B.</b> Hình bình hành ABCD có AB ∥ DC và AB = DC, cùng chiều A → B và D → C, "
        "nên vectơ AB = vectơ DC. Vectơ AB và vectơ CD ngược hướng.",
    ])

    ctx.h2("D.2. Đáp án Phần II – Trắc nghiệm đúng sai (2,0 điểm)")
    ctx.table(
        [
            ["Câu", "ý a", "ý b", "ý c", "ý d", "Số ý đúng", "Điểm câu"],
            ["13", "Đúng", "Đúng", "Đúng", "Sai", "3", "0,5"],
            ["14", "Đúng", "Sai", "Đúng", "Sai", "2", "0,25"],
        ],
        widths=[50, 60, 60, 60, 60, 90, W - 380],
        align=["c"] * 7,
    )
    ctx.caption("Bảng 11. Đáp án và cách quy điểm Phần II (tổng 0,75 điểm).")

    ctx.h3("Giải thích từng ý (Phần II)")
    ctx.bullets([
        "<b>Câu 13 a) Đúng</b> – định nghĩa giao của hai tập hợp.",
        "<b>Câu 13 b) Đúng</b> – nếu A ⊂ B thì mọi phần tử của A đều thuộc B nên A ∩ B = A.",
        "<b>Câu 13 c) Đúng</b> – <i>a</i> ≤ <i>x</i> &lt; <i>b</i> là đúng với nửa khoảng [<i>a</i>; <i>b</i>).",
        "<b>Câu 13 d) Sai</b> – hai tập hợp bằng nhau khi mọi phần tử của tập này đều thuộc tập kia và "
        "ngược lại; số phần tử bằng nhau chỉ là điều kiện <b>đủ</b> khi các phần tử cùng loại.",
        "<b>Câu 14 a) Đúng</b> – 2<i>x</i> − 3<i>y</i> ≤ 6 là bất phương trình bậc nhất hai ẩn.",
        "<b>Câu 14 b) Sai</b> – miền nghiệm của bất phương trình ≤ 0 là nửa mặt phẳng <b>có chứa</b> "
        "đường thẳng biên <i>ax</i> + <i>by</i> + <i>c</i> = 0 (biên là các điểm có <i>ax</i> + "
        "<i>by</i> + <i>c</i> = 0, thuộc miền nghiệm vì 0 ≤ 0).",
        "<b>Câu 14 c) Đúng</b> – nghiệm của hệ là giao của các miền nghiệm.",
        "<b>Câu 14 d) Sai</b> – miền nghiệm của hệ là giao của hai nửa mặt phẳng, thường là một miền "
        "kín (hình góc, đa giác), có thể rỗng, không phải một nửa mặt phẳng.",
    ])
    ctx.box("Cách quy điểm Phần II (nhắc lại)", [
        "Trong mỗi câu: đúng 1 ý → 0,1 điểm; đúng 2 ý → 0,25 điểm; đúng 3 ý → 0,5 điểm; "
        "đúng 4 ý → 1,0 điểm. Nếu thí sinh không trả lời hoặc trả lời cả 4 ý đều “Đ” thì câu đó "
        "được 0 điểm.",
    ], kind="grey")

    ctx.h2("D.3. Đáp án Phần III – Trắc nghiệm trả lời ngắn (2,0 điểm)")
    ctx.question(
        15,
        "Tập hợp A có 4 phần tử. Số tập hợp con của A (kể cả tập rỗng và chính tập A) bằng "
        "bao nhiêu?",
        points="0,5 điểm",
        note="Lời giải: Mỗi phần tử của A có hai lựa chọn: được lấy vào tập con hoặc không. "
              "Số tập hợp con là 2⁴ = 16 (gồm cả tập rỗng và chính A).",
    )
    ctx.question(
        16,
        "Lớp 10A có 45 học sinh, trong đó 28 học sinh tham gia CLB Văn nghệ, 20 học sinh tham "
        "gia CLB Toán và có 8 học sinh tham gia cả hai CLB. Hỏi có bao nhiêu học sinh không tham gia "
        "CLB nào?",
        points="0,5 điểm",
        note="Lời giải: Gọi V là tập học sinh tham gia CLB Văn nghệ, T là tập học sinh tham gia "
              "CLB Toán. |V ∪ T| = 28 + 20 − 8 = 40. Số học sinh không tham gia CLB nào là "
              "45 − 40 = 5.",
    )
    ctx.question(
        17,
        "Cho góc α (0° &lt; α &lt; 180°) thỏa mãn sin α = 1/2. Tính giá trị của biểu thức "
        "P = 4cos²α + 3sin²α.",
        points="0,5 điểm",
        note="Lời giải: sin²α = 1/4. Từ sin²α + cos²α = 1 suy ra cos²α = 1 − 1/4 = 3/4. "
              "Do đó P = 4·(3/4) + 3·(1/4) = 3 + 3/4 = 15/4 = 3,75.",
    )
    ctx.question(
        18,
        "Cho tam giác ABC có BC = 5, CA = 7, AB = 8. Tính diện tích tam giác ABC.",
        points="0,5 điểm",
        note="Lời giải: a = BC = 5, b = CA = 7, c = AB = 8. "
              "cos A = (b² + c² − a²)/(2bc) = (49 + 64 − 25)/(2·7·8) = 88/112 = 11/14. "
              "sin A = √(1 − (11/14)²) = √(75/196) = 5√3/14. "
              "S = ½·b·c·sin A = ½·7·8·(5√3/14) = 10√3 ≈ 17,32 (đơn vị diện tích).",
    )

    ctx.h2("D.4. Đáp án Phần IV – Tự luận (3,0 điểm)")

    ctx.h3("Câu 19 (MĐ2 – 1,0 điểm). Các phép toán trên tập hợp")
    ctx.p(
        "A ∩ B = {3; 4; 5};  A ∪ B = {1; 2; 3; 4; 5; 6};  A \\ B = {1; 2};  "
        "C<sub>U</sub>(A) = U \\ A = {6; 7}."
    )
    ctx.p("<b>Hướng dẫn chấm điểm:</b> mỗi kết quả 0,25 điểm; thiếu hoặc sai một kết quả trừ "
           "0,25 điểm; nếu sai từ hai kết quả trở lên thì câu được 0 điểm.")

    ctx.h3("Câu 20 (MĐ2 – 1,0 điểm). Bài toán thực tiễn với hệ thức lượng trong tam giác")
    ctx.p(
        "a) Tam giác ABC vuông tại C nên AB = √(AC² + BC²) = √(20² + 30²) = √1300 = 10√13 "
        "≈ 36,06 (m).<br/>"
        "b) tan α = AC/BC = 20/30 = 2/3 ⇒ α ≈ 33,69° ≈ 34°."
    )
    ctx.p("<b>Hướng dẫn chấm điểm:</b> thiết lập được tam giác ABC vuông tại C và nhận ra AB là cạnh "
           "huyền: 0,25 điểm; tính đúng AB ≈ 36,06 m: 0,25 điểm; đặt đúng tan α = AC/BC: 0,25 điểm; "
           "kết luận α ≈ 34°: 0,25 điểm.")

    ctx.h3("Câu 21 (MĐ3 – 1,0 điểm). Hệ bất phương trình bậc nhất hai ẩn và bài toán tối ưu")
    ctx.p(
        "a) Hệ bất phương trình biểu diễn điều kiện của bài toán:<br/>"
        "{ 2<i>x</i> + 3<i>y</i> ≤ 14 ; 4<i>x</i> + <i>y</i> ≤ 12 ; <i>x</i> ≥ 0 ; <i>y</i> ≥ 0 }."
    )
    ctx.p(
        "b) Miền nghiệm là miền phẳng giới hạn bởi các đường thẳng 2<i>x</i> + 3<i>y</i> = 14, "
        "4<i>x</i> + <i>y</i> = 12, <i>x</i> = 0, <i>y</i> = 0 (lấy phần giao với góc phần tư thứ nhất), "
        "có các đỉnh O(0; 0), A(3; 0), B(2,2; 3,2), C(0; 14/3)."
    )
    ctx.p(
        "c) Tính S = 3<i>x</i> + 2<i>y</i> tại các đỉnh:<br/>"
        "S(O) = 0;  S(A) = 9;  S(B) = 3·2,2 + 2·3,2 = 13;  S(C) = 28/3 ≈ 9,33.<br/>"
        "Vậy <b>S lớn nhất = 13</b>, đạt khi <i>x</i> = 2,2 và <i>y</i> = 3,2 (sản xuất 2,2 kg sản "
        "phẩm A và 3,2 kg sản phẩm B)."
    )
    ctx.p("<b>Hướng dẫn chấm điểm:</b> lập đúng hệ và chỉ ra điều kiện <i>x</i>, <i>y</i> ≥ 0: "
           "0,25 điểm; xác định đúng các đỉnh của miền nghiệm: 0,25 điểm; lập bảng tính S tại các "
           "đỉnh: 0,25 điểm; kết luận S lớn nhất = 13 tại (2,2; 3,2): 0,25 điểm.")


# ==========================================================================
# PHẦN E – PHỤ LỤC
# ==========================================================================

def phan_e(ctx):
    ctx.h1("PHẦN E. PHỤ LỤC")

    ctx.h2("E.1. Bảng công thức cần nhớ (tóm tắt một trang)")
    ctx.table(
        [
            ["Chương", "Nội dung", "Công thức / khái niệm"],
            ["1", "Mệnh đề",
             "¬(∀x ∈ X: P(x)) ⇔ ∃x ∈ X: ¬P(x);  ¬(∃x ∈ X: P(x)) ⇔ ∀x ∈ X: ¬P(x);<br/>"
             "P ⇒ Q: điều kiện P, kết luận Q;  đảo: Q ⇒ P;  tương đương: P ⇔ Q."],
            ["1", "Tập hợp",
             "A ⊂ B ⇔ A ∩ B = A ⇔ A ∪ B = B;  A \\ B = A ∩ C<sub>U</sub>(B);<br/>"
             "(a;b) = {x | a &lt; x &lt; b};  [a;b] = {x | a ≤ x ≤ b};<br/>"
             "Số tập hợp con của tập hợp n phần tử = 2<sup>n</sup>."],
            ["2", "Bất phương trình bậc nhất hai ẩn",
             "ax + by + c ≤ 0 (hoặc &lt;, &gt;, ≥), a và b không đồng thời bằng 0;<br/>"
             "Miền nghiệm: nửa mặt phẳng có chứa biên (dấu ≤, ≥) hoặc không chứa biên (dấu &lt;, &gt;)."],
            ["2", "Hệ bất phương trình",
             "Nghiệm của hệ = giao các miền nghiệm;  bài toán tối ưu: xét giá trị của biểu thức "
             "tại các đỉnh của miền nghiệm."],
            ["3", "Giá trị lượng giác",
             "sin(180° − α) = sin α;  cos(180° − α) = −cos α;  tan(180° − α) = −tan α;<br/>"
             "sin²α + cos²α = 1."],
            ["3", "Hệ thức lượng trong tam giác",
             "a² = b² + c² − 2bc·cos A;  a/sin A = b/sin B = c/sin C = 2R;<br/>"
             "S = ½·b·c·sin A = ½·a·c·sin B = ½·a·b·sin C."],
            ["4", "Vectơ",
             "Hai vectơ bằng nhau ⇔ cùng độ dài và cùng hướng;  hai vectơ đối nhau ⇔ cùng độ dài "
             "và ngược hướng;  vectơ-không: |0| = 0, cùng phương và cùng hướng với mọi vectơ."],
        ],
        widths=[44, 116, W - 160],
        align=["c", "l", "l"],
    )
    ctx.caption("Bảng 12. Bảng tổng hợp công thức cần nhớ trước khi làm bài.")

    ctx.h2("E.2. Bảng đáp án nhanh cho toàn bộ 21 câu")
    ctx.table(
        [
            ["Câu", "Phần", "Đáp án", "Điểm"],
            ["1", "I", "B", "0,25"],
            ["2", "I", "C", "0,25"],
            ["3", "I", "C", "0,25"],
            ["4", "I", "A", "0,25"],
            ["5", "I", "A", "0,25"],
            ["6", "I", "B", "0,25"],
            ["7", "I", "C", "0,25"],
            ["8", "I", "C", "0,25"],
            ["9", "I", "B", "0,25"],
            ["10", "I", "A", "0,25"],
            ["11", "I", "C", "0,25"],
            ["12", "I", "B", "0,25"],
            ["13", "II", "a) Đúng; b) Đúng; c) Đúng; d) Sai → 3 ý đúng", "0,5"],
            ["14", "II", "a) Đúng; b) Sai; c) Đúng; d) Sai → 2 ý đúng", "0,25"],
            ["15", "III", "16 tập hợp con (2⁴)", "0,5"],
            ["16", "III", "5 học sinh", "0,5"],
            ["17", "III", "P = 15/4 = 3,75", "0,5"],
            ["18", "III", "S = 10√3 ≈ 17,32", "0,5"],
            ["19", "IV", "A ∩ B = {3; 4; 5};  A ∪ B = {1; 2; 3; 4; 5; 6};  "
                         "A \\ B = {1; 2};  C<sub>U</sub>(A) = {6; 7}", "1,0"],
            ["20", "IV", "AB = 10√13 ≈ 36,06 m;  α ≈ 34°", "1,0"],
            ["21", "IV", "Hệ: 2x + 3y ≤ 14; 4x + y ≤ 12; x, y ≥ 0.  "
                         "S<sub>max</sub> = 13 tại (2,2; 3,2)", "1,0"],
            ["", "Tổng", "", "10,0"],
        ],
        widths=[34, 34, W - 108, 40],
        align=["c", "c", "l", "c"],
        head_bg=XANH_SANG,
    )
    ctx.caption("Bảng 13. Đáp án nhanh (dùng để tự chấm nhanh bài làm).")

    ctx.h2("E.3. Phiếu tự đánh giá sau khi làm đề")
    ctx.p(
        "Mỗi mục đánh dấu: <b>✓</b> nếu làm được ngay và không cần tra cứu; <b>△</b> nếu làm được "
        "nhưng phải nhờ gợi ý hoặc tra sách; <b>✗</b> nếu không làm được. Các mục đánh dấu "
        "<b>△</b> và <b>✗</b> chính là danh sách việc cần ôn trước ngày kiểm tra."
    )
    ctx.table(
        [
            ["TT", "Nội dung cần kiểm tra", "Câu hỏi / mục lý thuyết", "✓", "△", "✗"],
            ["1", "Phân biệt mệnh đề, mệnh đề chứa biến; phủ định mệnh đề chứa ∀, ∃",
             "Câu 1, 2, 13 – B.1.1, B.1.2", "", "", ""],
            ["2", "Mệnh đề kéo theo, đảo, tương đương; điều kiện cần – đủ",
             "B.1.3, B.1.4", "", "", ""],
            ["3", "Tập hợp: hai cách xác định; tập con; tập bằng nhau; tập rỗng",
             "Câu 3, 13 – B.1.5", "", "", ""],
            ["4", "Kí hiệu khoảng, đoạn, nửa khoảng; biểu diễn trên trục số",
             "Câu 13 – B.1.6", "", "", ""],
            ["5", "Biểu đồ Ven; giao, hợp, phần bù, hiệu của hai tập hợp",
             "Câu 4, 19 – B.1.7", "", "", ""],
            ["6", "Số tập hợp con của một tập hợp", "Câu 15 – B.1.7", "", "", ""],
            ["7", "Bài toán thực tế về các phép toán trên tập hợp", "Câu 16 – B.1.8", "", "", ""],
            ["8", "Bất phương trình bậc nhất hai ẩn; nghiệm và miền nghiệm",
             "Câu 5, 14 – B.2.1", "", "", ""],
            ["9", "Hệ bất phương trình bậc nhất hai ẩn; miền nghiệm của hệ",
             "Câu 6, 14 – B.2.2", "", "", ""],
            ["10", "Lập hệ bất phương trình từ bài toán thực tế; bài toán tối ưu",
             "Câu 21 – B.2.3", "", "", ""],
            ["11", "Giá trị lượng giác của góc 0° đến 180°; góc bù nhau",
             "Câu 7, 17 – B.3.1", "", "", ""],
            ["12", "Định lí côsin, định lí sin, công thức diện tích tam giác",
             "Câu 9, 10, 18 – B.3.2", "", "", ""],
            ["13", "Giải tam giác và ứng dụng vào bài toán thực tiễn",
             "Câu 20 – B.3.3", "", "", ""],
            ["14", "Khái niệm vectơ, vectơ-không, độ dài, phương, hướng",
             "Câu 11 – B.4.1", "", "", ""],
            ["15", "Cùng phương, cùng hướng, bằng nhau, đối nhau; chứng minh hai vectơ bằng nhau",
             "Câu 12 – B.4.2", "", "", ""],
            ["16", "Kĩ năng làm bài: phân bổ thời gian, kiểm tra lại, trình bày tự luận",
             "Toàn đề", "", "", ""],
        ],
        widths=[26, 232, 110, 26, 26, W - 420],
        align=["c", "l", "l", "c", "c", "c"],
    )
    ctx.caption("Bảng 14. Phiếu tự đánh giá theo 16 mục kiến thức – kỹ năng.")

    ctx.h2("E.4. Gợi ý sử dụng tài liệu")
    ctx.numbered([
        "<b>Giáo viên:</b> dùng Phần A.3 và A.4 (hai bảng nguyên bản) để đối chiếu khi ra đề; "
        "dùng Phần D làm đáp án và hướng dẫn chấm; dùng Phần E.3 để tổng hợp kết quả lớp theo mức độ.",
        "<b>Học sinh:</b> học theo lộ trình 8 tuần ở A.7; làm bài theo Phần C, tự chấm bằng Bảng 12; "
        "dùng Phần B để bù lỗ hổng theo Phiếu tự đánh giá.",
        "<b>Phụ lục công thức (E.1):</b> in ra làm tờ gợi nhớ dán vào góc bàn học trong tuần ôn "
        "cuối.",
    ])

    ctx.h2("E.5. Tài liệu tham khảo và căn cứ xây dựng")
    ctx.bullets([
        "<b>Tài liệu gốc của đề cương:</b> “MA TRẬN TOÁN 10 - GIỮA KÌ I.docx” – Trường THPT "
        "Hà Huy Tập, Tổ Toán-Tin (ma trận đề kiểm tra và bảng đặc tả đề kiểm tra giữa học kỳ I "
        "năm học 2026-2027).",
        "<b>Giáo trình:</b> Toán 10, tập 1, bộ sách “Kết nối tri thức” (Bài 1 Mệnh đề; Bài 2 Tập hợp "
        "và các phép toán trên tập hợp; Bài 3 Bất phương trình bậc nhất hai ẩn; Bài 4 Hệ bất "
        "phương trình bậc nhất hai ẩn; Bài 5 Giá trị lượng giác của một góc từ 0° đến 180°; "
        "Bài 6 Hệ thức lượng trong tam giác; Bài 7 Các khái niệm mở đầu về vectơ).",
    ])
    ctx.p(
        "Các kí hiệu đặc biệt trong tài liệu gốc (ký hiệu phổ biến ∀, ký hiệu tồn tại ∃ và ký hiệu "
        "vô cùng ∞ trong cách ghi khoảng) được giữ nguyên khi trích dẫn."
    )
