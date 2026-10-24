# -*- coding: utf-8 -*-
"""Nội dung: Chương IV (Vectơ – Bài 7) và Đề tham khảo số 1."""

PART4 = [
    ("h1", "CHƯƠNG IV – VECTƠ (BÀI 7: CÁC KHÁI NIỆM MỞ ĐẦU)", "Phần 4", "toc4"),
    ("lead", "Theo ma trận, phần Vectơ chỉ kiểm tra **Bài 7 – Các khái niệm mở đầu** với **2 câu trắc "
             "nghiệm (0,5 điểm)**: 1 câu nhận biết và 1 câu thông hiểu. Đây là phần **ít điểm nhất** "
             "nhưng cũng **dễ lấy trọn điểm nhất** – chỉ cần nắm chắc 6 khái niệm."),

    ("h2", "4.1  Khái niệm vectơ"),

    ("h3", "1. Vectơ là gì?"),
    ("p", "**Vectơ** là một **đoạn thẳng có hướng**, nghĩa là trong hai điểm mút của đoạn thẳng đã chỉ rõ "
          "đâu là **điểm đầu**, đâu là **điểm cuối**."),
    ("p", "Vectơ có điểm đầu A và điểm cuối B được kí hiệu là **AB^{→}** (đọc là \"vectơ AB\"). "
          "Vectơ còn được kí hiệu bởi một chữ cái thường in nghiêng có mũi tên, ví dụ "
          "**a^{→}**, **b^{→}**, **x^{→}**, **y^{→}**…"),
    ("p", "**Độ dài của vectơ** là khoảng cách giữa điểm đầu và điểm cuối của vectơ đó. "
          "Độ dài của vectơ AB^{→} kí hiệu là **|AB^{→}|**; như vậy **|AB^{→}| = AB** (độ dài đoạn thẳng)."),
    ("p", "**Vectơ-không** là vectơ có điểm đầu và điểm cuối trùng nhau, kí hiệu **0^{→}** "
          "(ví dụ AA^{→}). Vectơ-không có **độ dài bằng 0**."),

    ("h3", "2. Giá của vectơ"),
    ("p", "**Giá của vectơ** AB^{→} là **đường thẳng đi qua điểm đầu và điểm cuối** của vectơ đó, "
          "tức là đường thẳng AB."),
    ("note", "Vectơ-không **không có giá xác định** (vì A trùng B, không xác định được đường thẳng). "
             "Tuy vậy, người ta quy ước vectơ-không **cùng phương và cùng hướng với mọi vectơ**."),

    ("h3", "3. Hai vectơ cùng phương, cùng hướng, ngược hướng"),
    ("table",
     ["Khái niệm", "Định nghĩa"],
     [
         ["**Cùng phương**", "Hai vectơ có **giá song song hoặc trùng nhau**"],
         ["**Cùng hướng**", "Hai vectơ **cùng phương** và có **cùng chiều** (mũi tên chỉ về một phía)"],
         ["**Ngược hướng**", "Hai vectơ **cùng phương** và có **chiều ngược nhau**"],
     ],
     [3.6, 13.0],
     ["l", "l"]),
    ("box", "Ba điều cần khắc sâu", [
        "**Cùng phương ⊃ cùng hướng.** Hai vectơ cùng hướng thì **chắc chắn** cùng phương; nhưng hai "
        "vectơ cùng phương có thể **ngược hướng**. Vậy \"cùng hướng ⇒ cùng phương\" đúng, "
        "còn \"cùng phương ⇒ cùng hướng\" **sai**.",
        "**Ba điểm A, B, C thẳng hàng ⇔ AB^{→} và AC^{→} cùng phương.** Đây là công cụ để "
        "**chứng minh ba điểm thẳng hàng**.",
        "**Vectơ-không** cùng phương, cùng hướng với **mọi** vectơ (kể cả chính nó).",
    ]),

    ("h3", "4. Hai vectơ bằng nhau"),
    ("p", "Hai vectơ **a^{→}** và **b^{→}** được gọi là **bằng nhau**, kí hiệu **a^{→} = b^{→}**, nếu chúng "
          "**cùng hướng** và **cùng độ dài**."),
    ("eq", "a^{→} = b^{→}  ⇔  (a^{→} và b^{→} cùng hướng) **và** (|a^{→}| = |b^{→}|)"),
    ("p", "Hai vectơ được gọi là **đối nhau** nếu chúng **ngược hướng** và **cùng độ dài**; vectơ đối của "
          "**a^{→}** kí hiệu là **−a^{→}**. Đặc biệt, **AB^{→} và BA^{→} là hai vectơ đối nhau**."),

    ("box", "Hình bình hành – bộ ba đẳng thức vectơ phải nhớ", [
        "Cho hình bình hành **ABCD** (các đỉnh theo thứ tự A, B, C, D). Khi đó:",
        "**AB^{→} = DC^{→}**   và   **AD^{→} = BC^{→}**",
        "Ngược lại, nếu tứ giác ABCD có **AB^{→} = DC^{→}** thì ABCD là **hình bình hành**.",
        "__Cẩn thận:__ **AB^{→} = CD^{→}** là **sai** (vì AB^{→} và CD^{→} **ngược hướng**); "
        "**AD^{→} = CB^{→}** cũng **sai**.",
        "Với **hình chữ nhật** ABCD: AB^{→} = DC^{→}; nhưng **|AC^{→}| ≠ |AB^{→}|** nói chung.",
    ]),

    ("h3", "5. Bảng tổng hợp các khái niệm"),
    ("table",
     ["Khái niệm", "Định nghĩa ngắn", "Ví dụ"],
     [
         ["Vectơ", "Đoạn thẳng có hướng (rõ điểm đầu, điểm cuối)", "AB^{→}"],
         ["Độ dài vectơ", "Khoảng cách giữa điểm đầu và điểm cuối", "|AB^{→}| = AB"],
         ["Giá vectơ", "Đường thẳng đi qua điểm đầu và điểm cuối", "giá của AB^{→} là đường thẳng AB"],
         ["Cùng phương", "Giá song song hoặc trùng nhau", "AB^{→} và CD^{→} với AB ∥ CD"],
         ["Cùng hướng", "Cùng phương và cùng chiều", "AB^{→} và DC^{→} trong hình bình hành"],
         ["Ngược hướng", "Cùng phương và ngược chiều", "AB^{→} và BA^{→}"],
         ["Bằng nhau", "Cùng hướng và cùng độ dài", "AB^{→} = DC^{→}"],
         ["Đối nhau", "Ngược hướng và cùng độ dài", "AB^{→} và BA^{→}"],
         ["Vectơ-không", "Điểm đầu trùng điểm cuối, độ dài 0", "AA^{→} = 0^{→}"],
     ],
     [2.8, 7.0, 6.8],
     ["l", "l", "l"]),

    ("h2", "Các dạng toán thường gặp – Vectơ"),

    ("h3", "Dạng 1. Xác định các vectơ từ một hình cho trước"),
    ("box", "Ví dụ mẫu", [
        "**Ví dụ.** Cho hình bình hành ABCD tâm O. Hãy chỉ ra các vectơ bằng vectơ AB^{→}, các vectơ "
        "đối của AB^{→}.",
        "**Giải.** Vì ABCD là hình bình hành nên **AB^{→} = DC^{→}** (cùng hướng, cùng độ dài). "
        "Ngoài ra không có vectơ nào khác (tạo từ các đỉnh A, B, C, D, O) bằng AB^{→}.",
        "Vectơ **đối** của AB^{→} là **BA^{→}** (và **CD^{→}**, vì CD^{→} ngược hướng với AB^{→} và "
        "|CD^{→}| = |AB^{→}|).",
        "__Lưu ý quan trọng:__ **CD^{→} và BA^{→} cùng hướng, cùng độ dài** nên **CD^{→} = BA^{→}**; "
        "cả hai đều là vectơ **đối của AB^{→}**. Trong khi đó **AB^{→} và CD^{→} ngược hướng**, "
        "nên **AB^{→} ≠ CD^{→}**.",
    ]),

    ("h3", "Dạng 2. Chứng minh hai vectơ bằng nhau"),
    ("p", "**Phương pháp:** cần chỉ ra **hai điều** – (i) hai vectơ **cùng hướng**; (ii) hai vectơ "
          "**cùng độ dài**. Thường dùng tính chất hình học: hình bình hành, hình thoi, hình chữ nhật, "
          "trung điểm, tam giác đều."),
    ("box", "Ví dụ mẫu", [
        "**Ví dụ.** Cho tam giác ABC đều cạnh a, M là trung điểm BC. Chứng minh "
        "**|AB^{→}| = |AC^{→}|** nhưng **AB^{→} ≠ AC^{→}**.",
        "**Giải.** Vì tam giác đều cạnh a nên |AB^{→}| = AB = a và |AC^{→}| = AC = a. "
        "Vậy hai vectơ **cùng độ dài**. Tuy nhiên AB^{→} và AC^{→} có **giá khác nhau** (hai đường "
        "thẳng AB và AC cắt nhau tại A), nên chúng **không cùng phương**, do đó **không bằng nhau**.",
        "__Kết luận quan trọng:__ **cùng độ dài không suy ra bằng nhau.**",
    ]),

    ("h3", "Dạng 3. Chứng minh ba điểm thẳng hàng"),
    ("p", "**Phương pháp:** chứng minh **AB^{→} và AC^{→} cùng phương** (tức giá của chúng song song "
          "hoặc trùng nhau). Vì hai vectơ này có **chung điểm A**, nên chúng cùng phương khi và chỉ khi "
          "A, B, C thẳng hàng."),

    ("h3", "Dạng 4. Tính độ dài vectơ"),
    ("p", "**Phương pháp:** đưa về tính độ dài **đoạn thẳng** tương ứng, dùng định lí Py-ta-go (tam giác "
          "vuông), hệ thức lượng trong tam giác đều, hình vuông, hình thoi…"),
    ("box", "Ví dụ mẫu", [
        "**Ví dụ.** Cho hình vuông ABCD cạnh a. Tính |AB^{→}|, |AC^{→}|, |BD^{→}|.",
        "**Giải.** |AB^{→}| = AB = **a**. Đường chéo hình vuông cạnh a bằng a√2, nên "
        "|AC^{→}| = AC = **a√2** và |BD^{→}| = BD = **a√2**.",
    ]),
]


# ==========================================================================
# ĐỀ THAM KHẢO
# ==========================================================================
EXAM = [
    ("h1", "ĐỀ THAM KHẢO SỐ 1", "Phần 5", "toc5"),
    ("p", "**Thời gian làm bài: 90 phút** (không kể thời gian phát đề). "
          "Đề được thiết kế **đúng 100% cấu trúc và phân bố mức độ** của ma trận đề kiểm tra giữa học "
          "kì I năm học 2026 – 2027."),

    ("table",
     ["Phần", "Nội dung", "Số câu", "Điểm"],
     [
         ["I", "Trắc nghiệm nhiều phương án lựa chọn", "12", "3,0"],
         ["II", "Trắc nghiệm đúng – sai", "2", "2,0"],
         ["III", "Trắc nghiệm trả lời ngắn", "4", "2,0"],
         ["IV", "Tự luận", "3", "3,0"],
     ],
     [1.4, 10.2, 2.2, 2.4],
     ["c", "l", "c", "c"]),

    # ---------------- PHẦN I ----------------
    ("h2", "PHẦN I. TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN (12 câu – 3,0 điểm)"),
    ("small", "Chọn một phương án đúng nhất trong bốn phương án A, B, C, D."),

    ("q", 1, "Câu nào sau đây **là mệnh đề** toán học?"),
    ("opts", [
        "Hà Nội là thủ đô của Việt Nam.",
        "x + 5 = 7.",
        "Bạn có khỏe không?",
        "Hãy đóng cửa lại!",
    ]),

    ("q", 2, "Mệnh đề phủ định của mệnh đề P: \"∃x ∈ ℝ, x^{2} + 1 = 0\" là"),
    ("opts", [
        "\"∀x ∈ ℝ, x^{2} + 1 ≠ 0\".",
        "\"∃x ∈ ℝ, x^{2} + 1 ≠ 0\".",
        "\"∀x ∈ ℝ, x^{2} + 1 = 0\".",
        "\"∀x ∈ ℝ, x^{2} + 1 > 0\".",
    ]),

    ("q", 3, "Cho tập hợp A = {x ∈ ℤ | −2 < x ≤ 3}. Số phần tử của tập hợp A là"),
    ("opts", ["4.", "6.", "5.", "3."]),

    ("q", 4, "Cho hai tập hợp A = {1; 2; 3; 4} và B = {3; 4; 5}. Tập hợp A ∩ B là"),
    ("opts", ["{1; 2}.", "{5}.", "{1; 2; 3; 4; 5}.", "{3; 4}."]),

    ("q", 5, "Bất phương trình nào sau đây **là bất phương trình bậc nhất hai ẩn**?"),
    ("opts", [
        "x^{2} + y < 3.",
        "2x − y ≥ 1.",
        "x + y^{2} > 0.",
        "1/x + y ≤ 2.",
    ]),

    ("q", 6, "Hệ bất phương trình nào sau đây **là hệ bất phương trình bậc nhất hai ẩn**?"),
    ("opts", [
        "{ x^{2} + y ≤ 3 ;  x − y > 1 }",
        "{ 2/x + y ≤ 3 ;  x − y > 1 }",
        "{ 2x + y ≤ 3 ;  x − y > 1 }",
        "{ 2x + y^{2} ≤ 3 ;  x − y > 1 }",
    ]),

    ("q", 7, "Giá trị của biểu thức **sin 30° + cos 60°** bằng"),
    ("opts", ["0.", "2.", "√3.", "1."]),

    ("q", 8, "Cho góc α thỏa mãn **90° < α < 180°** và **cos α = −3/5**. Giá trị của **sin α** bằng"),
    ("opts", ["−4/5.", "4/5.", "2/5.", "16/25."]),

    ("q", 9, "Trong tam giác ABC, theo **định lí côsin** ta có"),
    ("opts", [
        "a^{2} = b^{2} + c^{2} + 2bc·cos A.",
        "a^{2} = b^{2} + c^{2} − 2bc·cos A.",
        "a^{2} = b^{2} + c^{2} − bc·cos A.",
        "a^{2} = b^{2} − c^{2} + 2bc·cos A.",
    ]),

    ("q", 10, "Tam giác ABC có **b = 6, c = 8** và **góc A = 30°**. Diện tích tam giác ABC bằng"),
    ("opts", ["12.", "24.", "12√3.", "6√3."]),

    ("q", 11, "Khẳng định nào sau đây **đúng**?"),
    ("opts", [
        "Hai vectơ cùng phương thì cùng hướng.",
        "Vectơ-không không cùng phương với vectơ nào.",
        "Hai vectơ cùng hướng thì cùng phương.",
        "Hai vectơ bằng nhau thì có độ dài khác nhau.",
    ]),

    ("q", 12, "Cho hình bình hành ABCD (các đỉnh theo thứ tự A, B, C, D). Khẳng định nào sau đây **đúng**?"),
    ("opts", [
        "AB^{→} = CD^{→}.",
        "AD^{→} = BC^{→}.",
        "AB^{→} = BC^{→}.",
        "AB^{→} = DC^{→}.",
    ]),

    # ---------------- PHẦN II ----------------
    ("h2", "PHẦN II. TRẮC NGHIỆM ĐÚNG – SAI (2 câu – 2,0 điểm)"),
    ("small", "Trong mỗi câu, hãy xác định mỗi phát biểu a), b), c), d) là **đúng** hay **sai**. "
              "Điểm: đúng 1 ý 0,1 – đúng 2 ý 0,25 – đúng 3 ý 0,5 – đúng 4 ý 1,0 điểm."),

    ("tf", 1, "Cho hai tập hợp **A = {x ∈ ℝ | −2 ≤ x < 3}** và **B = {x ∈ ℝ | x ≥ 1}**. Xét tính "
              "đúng – sai của các phát biểu sau:", [
        ("a", "Tập hợp A được viết dưới dạng nửa khoảng là A = [−2; 3)."),
        ("b", "Tập hợp B được viết dưới dạng khoảng là B = (1; +∞)."),
        ("c", "A ∩ B = [1; 3)."),
        ("d", "A \\ B = (−2; 1)."),
    ]),

    ("tf", 2, "Cho bất phương trình bậc nhất hai ẩn **2x + y ≤ 4**, kí hiệu là (1). Xét tính đúng – sai "
              "của các phát biểu sau:", [
        ("a", "Cặp số (1; 1) là một nghiệm của bất phương trình (1)."),
        ("b", "Điểm O(0; 0) thuộc miền nghiệm của bất phương trình (1)."),
        ("c", "Đường thẳng d: 2x + y = 4 đi qua hai điểm A(2; 0) và B(0; 2)."),
        ("d", "Miền nghiệm của (1) là nửa mặt phẳng bờ d **không** chứa điểm O(0; 0), kể cả bờ d."),
    ]),

    # ---------------- PHẦN III ----------------
    ("h2", "PHẦN III. TRẮC NGHIỆM TRẢ LỜI NGẮN (4 câu – 2,0 điểm)"),
    ("small", "Viết kết quả của mỗi câu vào ô trả lời (chỉ ghi số hoặc giá trị, không ghi đơn vị)."),

    ("q", 1, "Cho tập hợp A = {1; 2; 3; 4; 5}. Số **tập con** của tập hợp A là bao nhiêu?"),

    ("q", 2, "Lớp 10A có 40 học sinh, trong đó có 25 học sinh thích môn Toán, 20 học sinh thích môn Ngữ "
             "văn và 10 học sinh thích cả hai môn. Số học sinh **không thích môn nào** trong hai môn trên "
             "là bao nhiêu?"),

    ("q", 3, "Cho góc α thỏa mãn **90° < α < 180°** và **cos α = −3/5**. Tính giá trị của biểu thức "
             "**P = 2sin α + cos α**."),

    ("q", 4, "Cho tam giác ABC có **AB = 5, AC = 8, BC = 7**. Tính số đo góc A (theo đơn vị độ)."),

    # ---------------- PHẦN IV ----------------
    ("h2", "PHẦN IV. TỰ LUẬN (3 câu – 3,0 điểm)"),

    ("q", 1, "__(1,0 điểm)__ Cho hai tập hợp **A = {x ∈ ℝ | −3 ≤ x < 4}** và "
             "**B = {x ∈ ℝ | x ≥ 1}**.<br/>"
             "a) Tìm A ∩ B và A ∪ B.<br/>"
             "b) Tìm A \\ B và phần bù C_{ℝ}B."),

    ("q", 2, "__(1,0 điểm)__ Hai người quan sát đứng tại hai vị trí A và B trên bờ biển, cách nhau "
             "**100 m**. Họ cùng quan sát một chiếc thuyền đang ở vị trí C trên mặt biển. Người ta đo "
             "được **góc BAC = 60°** và **góc ABC = 75°**. "
             "Tính khoảng cách từ vị trí B đến chiếc thuyền (làm tròn đến mét). "
             "Nêu rõ các bước giải và định lí đã sử dụng."),

    ("q", 3, "__(1,0 điểm)__ Một xưởng sản xuất hai loại sản phẩm I và II. Mỗi sản phẩm loại I cần "
             "**3 kg** nguyên liệu và **1 giờ** công; mỗi sản phẩm loại II cần **2 kg** nguyên liệu và "
             "**2 giờ** công. Xưởng hiện có **120 kg** nguyên liệu và **80 giờ** công. Mỗi sản phẩm "
             "loại I cho lãi **4 triệu đồng**, mỗi sản phẩm loại II cho lãi **3 triệu đồng**.<br/>"
             "a) Gọi x, y lần lượt là số sản phẩm loại I và loại II cần sản xuất. Lập hệ bất phương "
             "trình biểu thị các điều kiện của bài toán và xác định miền nghiệm.<br/>"
             "b) Tìm số sản phẩm mỗi loại cần sản xuất để tổng tiền lãi lớn nhất và tính số tiền lãi đó."),

    ("gap", 6),
    ("note", "Hết đề. Đáp án và lời giải chi tiết ở Phần 6 (trang tiếp theo). "
             "Trước khi xem đáp án, hãy tự bấm đồng hồ 90 phút và làm bài nghiêm túc."),
]


# --------------------------------------------------------------------------
# Bổ sung: bài tập tự luyện chương IV
# --------------------------------------------------------------------------
PART4_EXTRA = [
    ("h2", "Bài tập tự luyện chương IV"),
    ("bullets", [
        "**Bài 1.** Cho hình vuông ABCD cạnh 2. Tính |AB^{→}|, |BD^{→}|, |CD^{→}|.",
        "**Bài 2.** Cho hình bình hành ABCD tâm O. Chỉ ra: a) các vectơ bằng AB^{→}; "
        "b) các vectơ đối của OB^{→}.",
        "**Bài 3.** Cho tam giác ABC đều cạnh a, M là trung điểm BC. So sánh |AB^{→}| và |AC^{→}|; "
        "AB^{→} và AC^{→} có bằng nhau không? Vì sao?",
        "**Bài 4.** Cho bốn điểm A, B, C, D. Chứng minh rằng nếu AB^{→} = DC^{→} thì tứ giác ABCD là "
        "hình bình hành.",
        "**Bài 5.** Cho lục giác đều ABCDEF tâm O. Kể tên các vectơ bằng vectơ OA^{→} (khác OA^{→}).",
    ]),
    ("box", "Đáp số và gợi ý", [
        "**Bài 1.** |AB^{→}| = 2;  |BD^{→}| = 2√2 (đường chéo);  |CD^{→}| = 2.",
        "**Bài 2.** a) AB^{→} = DC^{→}.  b) Vectơ đối của OB^{→} là **BO^{→}** và **OD^{→}** "
        "(vì OD^{→} ngược hướng, cùng độ dài với OB^{→}).",
        "**Bài 3.** |AB^{→}| = |AC^{→}| = a (cùng độ dài), nhưng AB^{→} và AC^{→} có **giá khác nhau** "
        "(hai đường thẳng AB, AC cắt nhau) nên **không cùng phương**, do đó **không bằng nhau**.",
        "**Bài 4.** Từ AB^{→} = DC^{→} suy ra AB ∥ DC và AB = DC ⇒ tứ giác ABCD có một cặp cạnh đối "
        "song song và bằng nhau ⇒ **ABCD là hình bình hành**.",
        "**Bài 5.** Trong lục giác đều, các vectơ bằng OA^{→} là **FO^{→}**, **CB^{→}**, **ED^{→}** "
        "(cùng hướng, cùng độ dài bằng cạnh lục giác).",
    ]),
]

PART4_SUMMARY = [
    ("h2", "Tóm tắt chương IV – những gì cần thuộc lòng"),
    ("table",
     ["Nội dung", "Phát biểu / công thức"],
     [
         ["Vectơ", "Đoạn thẳng có hướng: rõ **điểm đầu** và **điểm cuối**"],
         ["Kí hiệu", "AB^{→} (vectơ AB) hoặc a^{→}, b^{→}, x^{→}, y^{→}…"],
         ["Độ dài", "|AB^{→}| = AB (khoảng cách giữa điểm đầu và điểm cuối)"],
         ["Vectơ-không", "AA^{→} = 0^{→}; độ dài bằng 0; **cùng phương, cùng hướng với mọi vectơ**"],
         ["Giá của vectơ", "Đường thẳng đi qua điểm đầu và điểm cuối"],
         ["Cùng phương", "Giá **song song hoặc trùng** nhau"],
         ["Cùng hướng", "Cùng phương **và** cùng chiều"],
         ["Ngược hướng", "Cùng phương **và** ngược chiều"],
         ["Bằng nhau", "**Cùng hướng** và **cùng độ dài**: a^{→} = b^{→}"],
         ["Đối nhau", "**Ngược hướng** và **cùng độ dài**: vectơ đối của a^{→} là −a^{→}"],
         ["Hình bình hành ABCD", "AB^{→} = DC^{→};   AD^{→} = BC^{→}"],
         ["Ba điểm thẳng hàng", "A, B, C thẳng hàng ⇔ AB^{→} và AC^{→} **cùng phương**"],
     ],
     [4.2, 12.4],
     ["l", "l"]),
    ("box", "Ba câu hỏi tự kiểm tra cuối chương IV", [
        "**1.** Hai vectơ cùng phương có nhất thiết cùng hướng không? → **Không.** "
        "Ví dụ AB^{→} và BA^{→} cùng phương nhưng ngược hướng.",
        "**2.** Hai vectơ cùng độ dài có nhất thiết bằng nhau không? → **Không.** "
        "Ví dụ AB^{→} và AC^{→} trong tam giác đều cùng độ dài nhưng khác giá.",
        "**3.** Trong hình bình hành ABCD, AB^{→} bằng vectơ nào? → **DC^{→}** "
        "(không phải CD^{→}, vì AB^{→} và CD^{→} ngược hướng).",
    ]),
]
