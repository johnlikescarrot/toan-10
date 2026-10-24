# -*- coding: utf-8 -*-
"""Nội dung: Đáp án, lời giải chi tiết và Phụ lục."""

PART6 = [
    ("h1", "ĐÁP ÁN VÀ LỜI GIẢI CHI TIẾT", "Phần 6", "toc6"),
    ("mark", "toc6a"),

    ("h2", "Bảng đáp án nhanh"),
    ("p", "**Phần I – Trắc nghiệm nhiều phương án lựa chọn** (mỗi câu 0,25 điểm):"),
    ("table",
     ["Câu", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
     [["**Đáp án**", "**A**", "**A**", "**C**", "**D**", "**B**", "**C**", "**D**", "**B**", "**B**",
       "**A**", "**C**", "**D**"]],
     [1.9] + [1.2] * 12,
     ["c"] * 13),

    ("p", "**Phần II – Trắc nghiệm đúng – sai:**"),
    ("table",
     ["Câu", "a)", "b)", "c)", "d)", "Số ý đúng", "Điểm"],
     [
         ["**Câu 1**", "**ĐÚNG**", "**SAI**", "**ĐÚNG**", "**SAI**", "2", "0,25"],
         ["**Câu 2**", "**ĐÚNG**", "**ĐÚNG**", "**SAI**", "**SAI**", "2", "0,25"],
     ],
     [2.1, 2.0, 2.0, 2.0, 2.0, 3.0, 3.5],
     ["c", "c", "c", "c", "c", "c", "c"]),

    ("p", "**Phần III – Trắc nghiệm trả lời ngắn:**"),
    ("table",
     ["Câu", "1", "2", "3", "4"],
     [["**Đáp số**", "**32**", "**5**", "**1**", "**60**"]],
     [3.0, 3.4, 3.4, 3.4, 3.4],
     ["c", "c", "c", "c", "c"]),

    ("p", "**Phần IV – Tự luận:** đáp số tóm tắt"),
    ("table",
     ["Câu", "Kết quả"],
     [
         ["Câu 1", "A ∩ B = [1; 4);   A ∪ B = [−3; +∞);   A \\ B = [−3; 1);   C_{ℝ}B = (−∞; 1)"],
         ["Câu 2", "BC = 100√(3/2) ≈ **122 m**"],
         ["Câu 3", "x = 20 sản phẩm loại I, y = 30 sản phẩm loại II; lãi lớn nhất **170 triệu đồng**"],
     ],
     [2.0, 14.6],
     ["c", "l"]),

    ("note", "Thang điểm tham khảo: Phần I 12 × 0,25 = 3,0; Phần II 2 × 1,0 = 2,0 (điểm lũy tiến theo "
             "số ý đúng); Phần III 4 × 0,5 = 2,0; Phần IV 3 × 1,0 = 3,0. Tổng 10,0 điểm."),

    # =================== LỜI GIẢI PHẦN I ===================
    ("h1", "LỜI GIẢI CHI TIẾT – PHẦN I: TRẮC NGHIỆM", "Phần 6.2", "toc6b"),

    ("ah", "Câu 1. Chọn A."),
    ("p", "Mệnh đề là câu **khẳng định** có tính đúng – sai xác định. "
          "**A.** \"Hà Nội là thủ đô của Việt Nam\" là câu khẳng định và **đúng** ⇒ là mệnh đề."),
    ("bullets", [
        "**B.** \"x + 5 = 7\" chứa biến x, chưa xác định được đúng – sai ⇒ là **mệnh đề chứa biến**, "
        "không phải mệnh đề.",
        "**C.** \"Bạn có khỏe không?\" là **câu hỏi** ⇒ không phải mệnh đề.",
        "**D.** \"Hãy đóng cửa lại!\" là **câu mệnh lệnh** ⇒ không phải mệnh đề.",
    ]),

    ("ah", "Câu 2. Chọn A."),
    ("p", "Áp dụng quy tắc phủ định mệnh đề chứa lượng từ: phủ định của **∃** là **∀**, đồng thời "
          "phủ định phần thân của mệnh đề."),
    ("eq", "P: \"∃x ∈ ℝ, x^{2} + 1 = 0\"   ⇒   @P: \"∀x ∈ ℝ, x^{2} + 1 ≠ 0\""),
    ("bullets", [
        "**B.** Sai vì vẫn giữ **∃**, chỉ đổi phần thân.",
        "**C.** Sai vì chỉ đổi lượng từ, **không** phủ định phần thân.",
        "**D.** Đây là một mệnh đề **đúng** (vì x^{2} + 1 ≥ 1 > 0) và nó **tương đương** với @P, "
        "nhưng **không phải** là mệnh đề phủ định theo đúng hình thức. Trong đề thi, hãy chọn đáp án "
        "**đúng hình thức logic**: \"∀x ∈ ℝ, x^{2} + 1 ≠ 0\".",
    ]),
    ("note", "Về mặt logic, @P và mệnh đề ở D có cùng giá trị chân lí (đều đúng), nên một số đề chấp nhận "
             "cả hai. Khi gặp tình huống này, ưu tiên đáp án **đổi ∀/∃ và thêm \"≠\"** – đó là cách "
             "trình bày chuẩn trong sách giáo khoa."),

    ("ah", "Câu 3. Chọn C."),
    ("p", "Vì **x ∈ ℤ** và **−2 < x ≤ 3** nên x ∈ {−1; 0; 1; 2; 3}."),
    ("p", "Tập A có **5** phần tử. Chú ý: **−2 không thuộc A** (vì dấu **<**), còn **3 thuộc A** "
          "(vì dấu **≤**)."),
    ("note", "Bẫy thường gặp: chọn B (6 phần tử) do nhầm −2 ∈ A; hoặc chọn A (4 phần tử) do bỏ sót số 0."),

    ("ah", "Câu 4. Chọn D."),
    ("p", "A ∩ B gồm các phần tử **vừa thuộc A vừa thuộc B**: 3 và 4 đều có mặt trong cả hai tập. "
          "Vậy **A ∩ B = {3; 4}**."),
    ("bullets", [
        "**A.** {1; 2} = A \\ B (phần của A không thuộc B).",
        "**B.** {5} = B \\ A.",
        "**C.** {1; 2; 3; 4; 5} = A ∪ B.",
    ]),

    ("ah", "Câu 5. Chọn B."),
    ("p", "Bất phương trình bậc nhất hai ẩn có dạng ax + by ≤ c với **bậc của x và y đều bằng 1** "
          "và **không có tích xy**."),
    ("bullets", [
        "**A.** x^{2} + y < 3 — có **x^{2}** ⇒ bậc hai.",
        "**C.** x + y^{2} > 0 — có **y^{2}** ⇒ bậc hai.",
        "**D.** 1/x + y ≤ 2 — ẩn x ở **mẫu** ⇒ không phải bậc nhất.",
        "**B.** 2x − y ≥ 1 — đúng dạng ax + by ≥ c với a = 2, b = −1, c = 1.",
    ]),

    ("ah", "Câu 6. Chọn C."),
    ("p", "Hệ bất phương trình bậc nhất hai ẩn là hệ gồm các bất phương trình **đều** là bậc nhất hai ẩn. "
          "Chỉ có hệ ở **C** thỏa mãn: 2x + y ≤ 3 và x − y > 1 đều là bậc nhất hai ẩn."),
    ("bullets", [
        "**A.** có x^{2} ⇒ loại.   **B.** có 2/x ⇒ loại.   **D.** có y^{2} ⇒ loại.",
    ]),

    ("ah", "Câu 7. Chọn D."),
    ("p", "Ta có **sin 30° = 1/2** và **cos 60° = 1/2**. Do đó:"),
    ("eq", "sin 30° + cos 60° = 1/2 + 1/2 = **1**"),
    ("note", "Đây là câu dùng **bảng giá trị lượng giác của các góc đặc biệt**. Hãy học thuộc bảng này – "
             "mỗi kì thi đều có ít nhất một câu hỏi trực tiếp từ bảng."),

    ("ah", "Câu 8. Chọn B."),
    ("p", "Từ hệ thức cơ bản **sin^{2}α + cos^{2}α = 1**:"),
    ("eq", "sin^{2}α = 1 − cos^{2}α = 1 − (−3/5)^{2} = 1 − 9/25 = 16/25"),
    ("p", "Suy ra sin α = ±4/5. Vì **0° < α < 180°** nên **sin α > 0**, do đó **sin α = 4/5**."),
    ("note", "__Sai lầm thường gặp:__ chọn A (−4/5) vì thấy cos âm nên suy ra sin cũng âm. "
             "Trên khoảng 0° – 180°, **sin luôn dương**. Chỉ cos mới đổi dấu."),

    ("ah", "Câu 9. Chọn B."),
    ("p", "Định lí côsin trong tam giác ABC:"),
    ("eq", "a^{2} = b^{2} + c^{2} − 2bc·cos A"),
    ("note", "Ghi nhớ: **bình phương một cạnh** bằng tổng bình phương **hai cạnh kia** trừ **2 lần tích** "
             "hai cạnh đó nhân **cos của góc xen giữa**. Dấu **trừ** là dấu hiệu nhận biết định lí côsin "
             "(khác với Py-ta-go ở chỗ có thêm số hạng −2bc·cos A)."),

    ("ah", "Câu 10. Chọn A."),
    ("p", "Diện tích tam giác theo công thức **S = ½·b·c·sin A** (hai cạnh b, c và góc xen giữa A):"),
    ("eq", "S = ½ · 6 · 8 · sin 30° = ½ · 48 · ½ = **12**"),
    ("note", "Nếu quên nhân ½ sẽ ra 24 (đáp án nhiễu B). Nếu nhầm sin 30° = √3/2 sẽ ra 12√3 (nhiễu C)."),

    ("ah", "Câu 11. Chọn C."),
    ("p", "**C.** \"Hai vectơ cùng hướng thì cùng phương\" — **đúng**, vì cùng hướng là trường hợp đặc "
          "biệt của cùng phương (cùng phương **và** cùng chiều)."),
    ("bullets", [
        "**A.** Sai: hai vectơ cùng phương có thể **ngược hướng**.",
        "**B.** Sai: vectơ-không được quy ước **cùng phương với mọi vectơ**.",
        "**D.** Sai: hai vectơ bằng nhau thì **cùng độ dài** (chứ không phải khác độ dài).",
    ]),

    ("ah", "Câu 12. Chọn D."),
    ("p", "Trong hình bình hành ABCD (đỉnh theo thứ tự), cạnh AB **song song và bằng** cạnh DC, "
          "và hai vectơ AB^{→}, DC^{→} **cùng hướng**. Do đó **AB^{→} = DC^{→}**."),
    ("bullets", [
        "**A.** AB^{→} và CD^{→} **ngược hướng** (dù cùng độ dài) ⇒ không bằng nhau.",
        "**B.** AD^{→} và BC^{→} là hai cạnh bên, **ngược hướng** ⇒ AD^{→} = CB^{→} mới đúng.",
        "**C.** AB^{→} và BC^{→} không cùng phương (trừ trường hợp suy biến) ⇒ không thể bằng nhau.",
    ]),
    ("note", "__Câu này là câu \"ăn điểm\" của phần Vectơ:__ chỉ cần nhớ **AB^{→} = DC^{→}** và "
             "**AD^{→} = BC^{→}** trong hình bình hành ABCD."),

    # =================== LỜI GIẢI PHẦN II ===================
    ("h1", "LỜI GIẢI CHI TIẾT – PHẦN II: ĐÚNG – SAI", "Phần 6.3", "toc6c"),

    ("ah", "Câu 1.  Đáp án: a) ĐÚNG – b) SAI – c) ĐÚNG – d) SAI."),
    ("p", "Trước hết viết lại hai tập hợp dưới dạng khoảng, đoạn:"),
    ("bullets", [
        "A = {x ∈ ℝ | −2 ≤ x < 3} = **[−2; 3)**  (lấy −2, không lấy 3).",
        "B = {x ∈ ℝ | x ≥ 1} = **[1; +∞)**  (lấy 1).",
    ]),
    ("tfa", 1, [
        ("a", "A = [−2; 3).",
         "Đ"),
        ("b", "B = (1; +∞) — sai vì B lấy cả điểm 1, phải là **[1; +∞)**.",
         "S"),
        ("c", "A ∩ B = [1; 3) — phần chung của [−2; 3) và [1; +∞) là [1; 3).",
         "Đ"),
        ("d", "A \\ B = [−2; 1) — không phải (−2; 1). Vì −2 ∈ A và −2 ∉ B nên −2 **phải** thuộc A \\ B.",
         "S"),
    ]),
    ("p", "**Minh họa trên trục số** (vẽ nhanh khi làm bài):"),
    ("bullets", [
        "A: tô từ −2 (nét liền) đến 3 (nở).",
        "B: tô từ 1 (nét liền) sang phải.",
        "⇒ Phần **cả hai cùng tô** là [1; 3) ⇒ A ∩ B = [1; 3).",
        "⇒ Phần **chỉ A tô** là [−2; 1) ⇒ A \\ B = [−2; 1).",
    ]),
    ("note", "Với 2 ý đúng trên 4, câu này được **0,25 điểm** theo thang điểm lũy tiến của nhà trường. "
             "Nếu chỉ sai ý d) thì đã được 0,5 điểm – vì vậy hãy kiểm tra kĩ **đầu mút** của mỗi khoảng."),

    ("ah", "Câu 2.  Đáp án: a) ĐÚNG – b) ĐÚNG – c) SAI – d) SAI."),
    ("bullets", [
        "**a)** Thay x = 1, y = 1: 2·1 + 1 = 3 ≤ 4 ⇒ bất đẳng thức **đúng** nên (1; 1) là một nghiệm. "
        "⇒ **ĐÚNG**.",
        "**b)** Thay O(0; 0): 2·0 + 0 = 0 ≤ 4 ⇒ **đúng** nên O thuộc miền nghiệm. ⇒ **ĐÚNG**.",
        "**c)** Xét A(2; 0): 2·2 + 0 = 4 ✔ **thuộc** d. Xét B(0; 2): 2·0 + 2 = 2 ≠ 4 ✘ **không thuộc** d. "
        "⇒ **SAI** (đường thẳng d đi qua A(2; 0) và C(0; **4**)).",
        "**d)** Vì O(0; 0) **thuộc** miền nghiệm nên miền nghiệm là nửa mặt phẳng **chứa** O, "
        "⇒ phát biểu **SAI**.",
    ]),
    ("p", "**Cách biểu diễn đầy đủ (để kiểm chứng):** vẽ d: 2x + y = 4 qua A(2; 0) và C(0; 4), nét **liền** "
          "(vì có dấu ≤). Thử O(0; 0) thấy đúng ⇒ miền nghiệm là nửa mặt phẳng bờ d **chứa O**, "
          "kể cả bờ."),

    # =================== LỜI GIẢI PHẦN III ===================
    ("h1", "LỜI GIẢI CHI TIẾT – PHẦN III: TRẢ LỜI NGẮN", "Phần 6.4", "toc6d"),

    ("ah", "Câu 1.  Đáp số: 32."),
    ("p", "Tập A có **n = 5** phần tử (1; 2; 3; 4; 5). Số tập con của một tập có n phần tử là **2^{n}**."),
    ("eq", "Số tập con = 2^{5} = **32**"),
    ("p", "Trong đó có: 1 tập rỗng, 5 tập con có 1 phần tử, 10 tập con có 2 phần tử "
          "(C(5;2) = 10), 10 tập con có 3 phần tử, 5 tập con có 4 phần tử, 1 tập con có 5 phần tử. "
          "Tổng: 1 + 5 + 10 + 10 + 5 + 1 = 32 ✔"),
    ("note", "Nếu đề hỏi **số tập con khác rỗng** thì đáp số là 32 − 1 = **31**. "
             "Nếu hỏi **số tập con có đúng 2 phần tử** thì là **10**."),

    ("ah", "Câu 2.  Đáp số: 5."),
    ("p", "Gọi A là tập học sinh thích Toán, B là tập học sinh thích Ngữ văn. Theo đề: "
          "n(A) = 25, n(B) = 20, n(A ∩ B) = 10."),
    ("p", "Số học sinh thích **ít nhất một** trong hai môn:"),
    ("eq", "n(A ∪ B) = n(A) + n(B) − n(A ∩ B) = 25 + 20 − 10 = **35**"),
    ("p", "Số học sinh **không thích môn nào**:  40 − 35 = **5** (học sinh)."),
    ("note", "__Kiểm tra bằng sơ đồ Ven:__ chỉ thích Toán = 25 − 10 = 15; chỉ thích Văn = 20 − 10 = 10; "
             "thích cả hai = 10. Tổng = 15 + 10 + 10 = 35 ✔. "
             "Công thức n(A ∪ B) = n(A) + n(B) − n(A ∩ B) là công thức **bắt buộc phải nhớ** cho dạng "
             "toán thực tế này."),

    ("ah", "Câu 3.  Đáp số: 1."),
    ("p", "**Bước 1 – Tính sin α.** Từ sin^{2}α + cos^{2}α = 1:"),
    ("eq", "sin^{2}α = 1 − (−3/5)^{2} = 1 − 9/25 = 16/25 ⇒ sin α = ±4/5"),
    ("p", "**Bước 2 – Xét dấu.** Vì **90° < α < 180°** (góc tù) nên **sin α > 0**, suy ra "
          "**sin α = 4/5**."),
    ("p", "**Bước 3 – Tính P:**"),
    ("eq", "P = 2sin α + cos α = 2·(4/5) + (−3/5) = 8/5 − 3/5 = 5/5 = **1**"),
    ("note", "__Bẫy:__ nếu bỏ qua bước xét dấu và lấy sin α = −4/5 thì P = −8/5 − 3/5 = −11/5 – "
             "đây là đáp án sai. Luôn xác định **khoảng của góc** trước khi kết luận dấu."),

    ("ah", "Câu 4.  Đáp số: 60 (độ)."),
    ("p", "Biết **ba cạnh**, muốn tìm góc ta dùng **hệ quả định lí côsin**. Áp dụng cho góc A "
          "(cạnh đối diện là BC = a = 7, hai cạnh kề là AB = c = 5 và AC = b = 8):"),
    ("eq", "cos A = (b^{2} + c^{2} − a^{2}) / (2bc) = (8^{2} + 5^{2} − 7^{2}) / (2·8·5)"),
    ("eq", "cos A = (64 + 25 − 49) / 80 = 40 / 80 = 1/2"),
    ("p", "Vì **0° < A < 180°** và cos A = 1/2 nên **A = 60°**."),
    ("note", "Khi biết ba cạnh, nên tính **góc lớn nhất trước** (góc đối diện cạnh lớn nhất) – "
             "nếu góc đó nhọn thì cả ba góc đều nhọn, tránh được sai lầm về góc tù. Ở đây cạnh lớn nhất "
             "là AC = 8 nên có thể kiểm tra góc B: cos B = (49 + 25 − 64)/(2·7·5) = 10/70 = 1/7 > 0 "
             "⇒ góc B nhọn ✔."),

    # =================== LỜI GIẢI PHẦN IV ===================
    ("h1", "LỜI GIẢI CHI TIẾT – PHẦN IV: TỰ LUẬN", "Phần 6.5", "toc6e"),

    ("ah", "Câu 1 (1,0 điểm). Phép toán trên tập hợp"),
    ("p", "**Bước 1.** Viết lại hai tập hợp dưới dạng khoảng, đoạn:"),
    ("bullets", [
        "A = {x ∈ ℝ | −3 ≤ x < 4} = **[−3; 4)**",
        "B = {x ∈ ℝ | x ≥ 1} = **[1; +∞)**",
    ]),
    ("p", "**Bước 2.** Biểu diễn trên trục số: A tô từ −3 (lấy) đến 4 (không lấy); "
          "B tô từ 1 (lấy) sang phải **+∞**."),
    ("p", "**a) (0,5 điểm)**"),
    ("eq", "**A ∩ B = [1; 4)**"),
    ("eq", "**A ∪ B = [−3; +∞)**"),
    ("p", "**b) (0,5 điểm)**"),
    ("eq", "**A \\ B = [−3; 1)**"),
    ("eq", "**C_{ℝ}B = (−∞; 1)**"),
    ("bullets", [
        "**A \\ B:** lấy phần của A mà **không** thuộc B. Các số từ −3 đến dưới 1 là thỏa mãn ⇒ **[−3; 1)**. "
        "Chú ý **không lấy 1** vì 1 ∈ B.",
        "**C_{ℝ}B:** phần bù của B trong ℝ gồm các số thực **không** thuộc B, tức x < 1 ⇒ **(−∞; 1)**. "
        "Chú ý **không lấy 1** vì 1 ∈ B.",
    ]),
    ("note", "__Thang điểm gợi ý:__ viết đúng A, B dạng khoảng – đoạn: 0,25 đ; mỗi kết quả đúng ở a) và b) "
             "được 0,25 đ nhưng phải có **trục số minh họa** để được điểm tối đa."),
    ("note", "**Lỗi mất điểm:** viết A ∩ B = (1; 4) — sai vì 1 ∈ B và 1 ∈ A nên 1 ∈ A ∩ B."),

    ("ah", "Câu 2 (1,0 điểm). Ứng dụng hệ thức lượng – bài toán thực tiễn"),
    ("p", "**Tóm tắt.** Tam giác ABC có AB = 100 m, góc A = 60°, góc B = 75°. Cần tính **BC**."),
    ("p", "**Bước 1 – Tính góc thứ ba của tam giác.** Tổng ba góc trong tam giác bằng 180°:"),
    ("eq", "C = 180° − A − B = 180° − 60° − 75° = **45°**"),
    ("p", "**Bước 2 – Áp dụng định lí sin.** Trong tam giác ABC:"),
    ("eq", "BC / sin A = AB / sin C   ⇒   BC = AB · sin A / sin C"),
    ("p", "**Bước 3 – Thay số:**"),
    ("eq", "BC = 100 · sin 60° / sin 45° = 100 · (√3/2) / (√2/2) = 100 · √3/√2 = 100√(3/2)"),
    ("p", "Tính giá trị: √(3/2) = √1,5 ≈ 1,2247, do đó:"),
    ("eq", "BC ≈ 100 · 1,2247 ≈ **122,47 (m)**"),
    ("p", "**Kết luận:** khoảng cách từ vị trí B đến chiếc thuyền xấp xỉ **122 m**."),
    ("note", "__Thang điểm gợi ý:__ nêu được tam giác và các yếu tố đã biết: 0,25 đ; tính đúng góc "
             "C = 45°: 0,25 đ; viết đúng định lí sin và thay số: 0,25 đ; ra kết quả và kết luận có đơn vị: "
             "0,25 đ."),
    ("note", "**Lỗi mất điểm:** dùng định lí côsin (không đủ dữ kiện) hoặc nhầm cạnh đối diện. "
             "Cần nhớ: **mỗi tỉ số trong định lí sin là (cạnh) / (sin góc đối diện cạnh đó)**."),

    ("ah", "Câu 3 (1,0 điểm). Hệ bất phương trình bậc nhất hai ẩn – bài toán tối ưu"),
    ("p", "**a) Lập mô hình (0,5 điểm)**"),
    ("p", "Gọi **x** là số sản phẩm loại I, **y** là số sản phẩm loại II cần sản xuất "
          "(x ≥ 0, y ≥ 0, đơn vị: sản phẩm)."),
    ("bullets", [
        "Điều kiện **nguyên liệu**: mỗi sản phẩm I cần 3 kg, mỗi sản phẩm II cần 2 kg, có 120 kg "
        "⇒ **3x + 2y ≤ 120**.",
        "Điều kiện **giờ công**: mỗi sản phẩm I cần 1 giờ, mỗi sản phẩm II cần 2 giờ, có 80 giờ "
        "⇒ **x + 2y ≤ 80**.",
        "Điều kiện **không âm**: **x ≥ 0, y ≥ 0**.",
    ]),
    ("p", "Ta được hệ bất phương trình:"),
    ("eq", "{ 3x + 2y ≤ 120 ;  x + 2y ≤ 80 ;  x ≥ 0 ;  y ≥ 0 }"),
    ("p", "**Miền nghiệm** là **tứ giác OABC** (kể cả biên) với:"),
    ("bullets", [
        "**O(0; 0)** — gốc tọa độ.",
        "**A(40; 0)** — giao của đường 3x + 2y = 120 với trục **Ox** (y = 0) ⇒ 3x = 120 ⇒ x = 40.",
        "**B(20; 30)** — giao của 3x + 2y = 120 và x + 2y = 80.",
        "**C(0; 40)** — giao của x + 2y = 80 với **Oy** (x = 0) ⇒ 2y = 80 ⇒ y = 40.",
    ]),
    ("p", "Tìm B: trừ vế theo vế hai phương trình: (3x + 2y) − (x + 2y) = 120 − 80 ⇒ 2x = 40 "
          "⇒ **x = 20**; thay vào x + 2y = 80 được 2y = 60 ⇒ **y = 30**. Vậy **B(20; 30)**."),
    ("note", "Phải **kiểm tra** B có thuộc miền nghiệm không: 3·20 + 2·30 = 120 ✔ và "
             "20 + 2·30 = 80 ✔ — B nằm trên **cả hai** đường biên nên là đỉnh của đa giác."),

    ("p", "**b) Tìm phương án tối ưu (0,5 điểm)**"),
    ("p", "Hàm mục tiêu (tổng tiền lãi, đơn vị **triệu đồng**):"),
    ("eq", "F(x; y) = 4x + 3y"),
    ("p", "Theo định lí về giá trị lớn nhất – nhỏ nhất của hàm bậc nhất trên một đa giác lồi, F chỉ có "
          "thể đạt giá trị lớn nhất tại một trong các **đỉnh**. Ta lập bảng:"),
    ("table",
     ["Đỉnh", "Tọa độ (x; y)", "F = 4x + 3y", "Tiền lãi"],
     [
         ["O", "(0; 0)", "4·0 + 3·0 = **0**", "0 triệu"],
         ["A", "(40; 0)", "4·40 + 3·0 = **160**", "160 triệu"],
         ["B", "(20; 30)", "4·20 + 3·30 = **170**", "**170 triệu**"],
         ["C", "(0; 40)", "4·0 + 3·40 = **120**", "120 triệu"],
     ],
     [1.6, 3.6, 5.4, 5.0],
     ["c", "c", "c", "c"]),
    ("p", "Giá trị lớn nhất của F là **170**, đạt được tại **x = 20, y = 30**."),
    ("p", "**Kết luận:** xưởng nên sản xuất **20 sản phẩm loại I** và **30 sản phẩm loại II**, "
          "khi đó tổng tiền lãi lớn nhất là **170 triệu đồng**."),
    ("note", "__Thang điểm gợi ý:__ đặt ẩn kèm điều kiện: 0,1 đ; lập đúng hệ bất phương trình: 0,2 đ; "
             "xác định đúng miền nghiệm và các đỉnh: 0,2 đ; lập hàm mục tiêu và lập bảng giá trị: 0,25 đ; "
             "kết luận đúng: 0,25 đ."),
    ("note", "**Lỗi mất điểm:** quên điều kiện x, y ≥ 0; tính sai đỉnh B (nhầm thành (30; 20)); "
             "hoặc kết luận mà **không trả lời đúng câu hỏi thực tế** (thiếu số lượng mỗi loại hoặc "
             "thiếu đơn vị tiền)."),
]


# ==========================================================================
# PHỤ LỤC
# ==========================================================================
PART7 = [
    ("h1", "PHỤ LỤC – CÔNG THỨC, LỖI THƯỜNG GẶP VÀ CHIẾN LƯỢC PHÒNG THI",
     "Phần 7", "toc7"),

    ("h2", "A. Bảng công thức tổng hợp toàn bộ giữa học kì I"),
    ("table",
     ["Chủ đề", "Công thức / kết quả cần nhớ"],
     [
         ["Mệnh đề", "P ⇒ Q sai **chỉ khi** P đúng, Q sai."],
         ["Phủ định ∀, ∃", "¬(∀x, P) = ∃x, ¬P;   ¬(∃x, P) = ∀x, ¬P"],
         ["Điều kiện cần – đủ", "P ⇒ Q: **P là điều kiện đủ**, **Q là điều kiện cần**"],
         ["Số tập con", "Tập có n phần tử ⇒ **2^{n}** tập con (khác rỗng: 2^{n} − 1)"],
         ["Phép toán tập hợp", "A ∩ B (giao), A ∪ B (hợp), A \\ B (hiệu), C_{A}B (phần bù khi B ⊂ A)"],
         ["Công thức tập hợp", "**n(A ∪ B) = n(A) + n(B) − n(A ∩ B)**"],
         ["BPT bậc nhất 2 ẩn", "ax + by ≤ c; miền nghiệm là nửa mặt phẳng bờ d: ax + by = c"],
         ["Cực trị", "F = ax + by đạt max/min tại **đỉnh** của đa giác miền nghiệm"],
         ["Góc bù", "sin(180° − α) = sin α;   cos(180° − α) = −cos α"],
         ["Hệ thức cơ bản", "sin^{2}α + cos^{2}α = 1;   1 + tan^{2}α = 1/cos^{2}α"],
         ["Định lí côsin", "a^{2} = b^{2} + c^{2} − 2bc·cos A"],
         ["Hệ quả côsin", "cos A = (b^{2} + c^{2} − a^{2})/(2bc)"],
         ["Định lí sin", "a/sin A = b/sin B = c/sin C = **2R**"],
         ["Diện tích", "S = ½bc·sin A = abc/(4R) = p·r = √(p(p−a)(p−b)(p−c))"],
         ["Vectơ", "AB^{→} = DC^{→} trong hình bình hành ABCD; |AB^{→}| = AB"],
     ],
     [4.2, 12.4],
     ["l", "l"]),

    ("h2", "B. Mười lỗi mất điểm phổ biến nhất"),
    ("num", [
        "**Nhầm \"cùng phương\" với \"cùng hướng\".** Cùng hướng ⇒ cùng phương (đúng); "
        "cùng phương ⇒ cùng hướng (**sai**).",
        "**Quên xét dấu khi tính sin, cos.** Góc tù ⇒ cos **âm**; sin luôn **dương** trên 0° – 180°.",
        "**Nhầm ngoặc khoảng – đoạn.** (a; b) khác [a; b]; và +∞, −∞ **luôn** đi với ngoặc tròn.",
        "**Sai đầu mút khi tìm giao.** A = (1; 3], B = [3; 5) ⇒ A ∩ B = ∅ (vì 3 ∉ A).",
        "**Không đổi chiều bất phương trình** khi nhân/chia hai vế với số **âm**.",
        "**Bỏ điều kiện x ≥ 0, y ≥ 0** trong bài toán tối ưu ⇒ miền nghiệm sai ⇒ kết quả sai.",
        "**Nhầm công thức diện tích:** S = ½bc·sin A chứ **không phải** bc·sin A (thiếu ½).",
        "**Nhầm cạnh – góc trong định lí sin:** phải là cạnh / sin **góc đối diện** cạnh đó.",
        "**Tính sai tọa độ đỉnh** của đa giác: phải **giải hệ** hai phương trình đường biên, không "
        "đọc bằng mắt trên hình.",
        "**Không kết luận theo câu hỏi thực tế:** thiếu đơn vị, thiếu \"mỗi loại bao nhiêu\".",
    ]),

    ("h2", "C. Chiến lược làm bài 90 phút"),
    ("table",
     ["Giai đoạn", "Thời gian", "Việc cần làm"],
     [
         ["Lượt 1", "≈ 35 phút", "Làm **hết** phần trắc nghiệm (I, II, III). Câu nào không chắc thì "
                                 "**đánh dấu** và đoán, tuyệt đối không bỏ trống."],
         ["Lượt 2", "≈ 40 phút", "Làm **3 câu tự luận** theo thứ tự **dễ → khó**: Câu 1 (tập hợp) → "
                                 "Câu 2 (hệ thức lượng) → Câu 3 (tối ưu)."],
         ["Lượt 3", "≈ 15 phút", "**Rà soát**: kiểm tra phiếu trả lời, xem lại các câu đã đánh dấu, "
                                 "kiểm tra đơn vị và kết luận của bài tự luận."],
     ],
     [2.2, 2.6, 11.8],
     ["l", "c", "l"]),

    ("box", "Năm mẹo phòng thi", [
        "**Câu đúng – sai:** xử lí từng ý **độc lập**; nếu chắc 3 ý thì đã có 0,5 điểm, hãy tập trung "
        "vào ý còn lại thay vì làm lại từ đầu.",
        "**Câu trả lời ngắn:** kết quả thường là **số nguyên** hoặc số đơn giản. Nếu ra số lẻ kì lạ, "
        "hãy kiểm tra lại phép tính.",
        "**Bài tự luận tối ưu:** luôn vẽ hình (dù chỉ phác) – giám khảo chấm theo **các bước**, "
        "vẽ hình đúng giúp bạn không nhầm đỉnh.",
        "**Bài thực tiễn hệ thức lượng:** viết rõ \"Xét tam giác ABC…\" trước khi dùng công thức, "
        "đó là 0,25 điểm trình bày.",
        "**Máy tính cầm tay:** kiểm tra đang ở chế độ **độ (DEG)** khi tính sin, cos của góc cho bằng độ.",
    ]),

    ("h2", "D. Phiếu tự đánh giá trước kì thi"),
    ("p", "Hãy tự đánh dấu ✔ vào ô mà bạn đã nắm chắc. Nếu còn ô trống, hãy quay lại phần tương ứng "
          "trong đề cương để ôn lại."),
    ("table",
     ["Nội dung", "Đã nắm", "Cần ôn lại"],
     [
         ["Nhận biết mệnh đề, mệnh đề chứa biến", "☐", "☐"],
         ["Lập mệnh đề phủ định (kể cả với ∀, ∃)", "☐", "☐"],
         ["Mệnh đề kéo theo, đảo, tương đương; điều kiện cần – đủ", "☐", "☐"],
         ["Viết tập hợp bằng liệt kê / chỉ ra tính chất đặc trưng", "☐", "☐"],
         ["Chuyển đổi qua lại giữa kí hiệu khoảng – đoạn và trục số", "☐", "☐"],
         ["Tìm giao, hợp, hiệu, phần bù", "☐", "☐"],
         ["Bài toán thực tế dùng n(A ∪ B)", "☐", "☐"],
         ["Nhận biết bất phương trình bậc nhất hai ẩn", "☐", "☐"],
         ["Biểu diễn miền nghiệm của bất phương trình và hệ", "☐", "☐"],
         ["Giải bài toán tối ưu (4 bước)", "☐", "☐"],
         ["Bảng giá trị lượng giác của góc đặc biệt", "☐", "☐"],
         ["Công thức hai góc bù nhau", "☐", "☐"],
         ["Tính sin khi biết cos (và ngược lại), xét dấu", "☐", "☐"],
         ["Định lí côsin và hệ quả", "☐", "☐"],
         ["Định lí sin", "☐", "☐"],
         ["Các công thức diện tích tam giác (kể cả Heron)", "☐", "☐"],
         ["Giải tam giác; bài toán đo khoảng cách, chiều cao", "☐", "☐"],
         ["Khái niệm vectơ, giá, độ dài, cùng phương, cùng hướng", "☐", "☐"],
         ["Hai vectơ bằng nhau; hình bình hành ABCD", "☐", "☐"],
     ],
     [11.0, 2.6, 3.0],
     ["l", "c", "c"]),

    ("gap", 10),
    ("box", "Lời nhắn cuối", [
        "Bạn đã có trong tay **toàn bộ** kiến thức mà đề kiểm tra sẽ hỏi. Ma trận cho thấy **5,0 điểm "
        "đầu tiên** chỉ ở mức **nhận biết – thông hiểu**; đó là phần điểm mà bất kì học sinh nào "
        "chăm chỉ cũng lấy được trọn vẹn.",
        "Hãy học thuộc **bảng giá trị lượng giác**, **ba định lí** của tam giác và **quy tắc 4 bước** "
        "cho bài toán tối ưu. Ba thứ đó chiếm gần một nửa số điểm của đề.",
        "Cuối cùng: làm lại **Đề tham khảo số 1** thêm một lần nữa vào đêm trước ngày thi, "
        "nhưng lần này **không xem đáp án** cho đến khi hết 90 phút.",
        "**Chúc bạn thi tốt!**",
    ]),
]
