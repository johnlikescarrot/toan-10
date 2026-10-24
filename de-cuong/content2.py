# -*- coding: utf-8 -*-
"""Nội dung: Chương II (Bất phương trình) và Chương III (Hệ thức lượng)."""

PART2 = [
    ("h1", "CHƯƠNG II – BẤT PHƯƠNG TRÌNH VÀ HỆ BẤT PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN",
     "Phần 2", "toc2"),
    ("lead", "Chương này chiếm khoảng **2,5 điểm** trong đề, trong đó có **1 câu tự luận vận dụng cao** "
             "về bài toán tối ưu – câu phân loại học sinh. Phần lý thuyết không khó, nhưng **kĩ năng vẽ "
             "miền nghiệm** phải thật chắc, vì mọi câu hỏi đều xoay quanh hình vẽ."),

    ("h2", "2.1  Bất phương trình bậc nhất hai ẩn"),
    ("mark", "toc2a"),

    ("h3", "1. Định nghĩa"),
    ("p", "**Bất phương trình bậc nhất hai ẩn x, y** là bất phương trình có một trong các dạng sau:"),
    ("eq", "ax + by ≤ c;     ax + by ≥ c;     ax + by < c;     ax + by > c"),
    ("p", "trong đó a, b, c là các số thực đã cho, **a và b không đồng thời bằng 0**, còn x và y là "
          "hai ẩn số."),
    ("p", "Số bộ **(x_{0}; y_{0})** được gọi là **một nghiệm** của bất phương trình nếu ta thay "
          "x = x_{0}, y = y_{0} vào bất phương trình thì được một **bất đẳng thức đúng**."),
    ("box", "Nhận diện nhanh", [
        "**Là** bất phương trình bậc nhất hai ẩn: 2x − 3y + 1 > 0;  5x ≤ 4;  −y + 2 ≥ x;  0·x + 3y < 6.",
        "**Không là**: x^{2} + y < 1 (vì có x^{2});  xy ≥ 3 (vì có tích xy);  1/x + y ≤ 2 "
        "(vì ẩn ở mẫu);  x^{2} + y^{2} ≤ 4.",
        "__Lưu ý:__ bất phương trình **một ẩn** như 3x − 1 > 0 vẫn là trường hợp riêng (b = 0). "
        "Chỉ cần **bậc của x và y đều bằng 1** và **không có tích xy**.",
    ]),

    ("h3", "2. Miền nghiệm của bất phương trình bậc nhất hai ẩn"),
    ("p", "Trong mặt phẳng tọa độ Oxy, đường thẳng **d: ax + by = c** chia mặt phẳng thành "
          "**hai nửa mặt phẳng** có bờ là d."),
    ("p", "**Miền nghiệm** của bất phương trình ax + by ≤ c là một nửa mặt phẳng (kể cả bờ d) gồm các "
          "điểm có tọa độ thỏa mãn bất phương trình."),

    ("h3", "3. Quy tắc biểu diễn miền nghiệm – 4 bước"),
    ("num", [
        "**Bước 1.** Vẽ đường thẳng **d: ax + by = c** (xác định bằng **hai điểm** dễ tìm: cho x = 0 "
        "tìm y, cho y = 0 tìm x).",
        "**Bước 2.** Chọn một điểm **M(x_{0}; y_{0})** không nằm trên d, **thuận lợi nhất là gốc tọa độ "
        "O(0; 0)** (nếu d không đi qua O).",
        "**Bước 3.** Tính giá trị **ax_{0} + by_{0}** rồi so sánh với c.",
        "**Bước 4.** Nếu bất đẳng thức **đúng** thì miền nghiệm là nửa mặt phẳng **chứa M**; nếu **sai** "
        "thì miền nghiệm là nửa mặt phẳng **không chứa M** (phần còn lại).",
    ]),
    ("box", "Hai lưu ý sống còn", [
        "Nếu bất phương trình có dấu **≤** hoặc **≥** thì **lấy cả bờ d** (vẽ đường **nét liền**). "
        "Nếu có dấu **<** hoặc **>** thì **không lấy bờ** (vẽ đường **nét đứt**).",
        "Nếu đường thẳng d **đi qua gốc O** thì phải chọn điểm khác, ví dụ **M(1; 0)** hoặc **M(0; 1)**.",
    ]),

    ("box", "Ví dụ mẫu – biểu diễn miền nghiệm", [
        "**Ví dụ.** Biểu diễn miền nghiệm của bất phương trình **2x + y ≤ 4**.",
        "**Giải.** Vẽ d: 2x + y = 4. Cho x = 0 ⇒ y = 4, được A(0; 4). Cho y = 0 ⇒ x = 2, được B(2; 0). "
        "Vẽ đường thẳng AB (nét liền vì có dấu ≤).",
        "Chọn O(0; 0): thay vào được 2·0 + 0 = 0 ≤ 4 — **đúng**. Vậy miền nghiệm là **nửa mặt phẳng "
        "bờ AB chứa gốc O** (kể cả bờ).",
        "__Kiểm tra ngược:__ điểm (3; 1) có 2·3 + 1 = 7 > 4 nên **không** thuộc miền nghiệm – và đúng là "
        "nó nằm ở nửa mặt phẳng không chứa O.",
    ]),

    ("h2", "2.2  Hệ bất phương trình bậc nhất hai ẩn"),
    ("mark", "toc2b"),

    ("h3", "1. Định nghĩa và miền nghiệm"),
    ("p", "**Hệ bất phương trình bậc nhất hai ẩn** là một hệ gồm hai hay nhiều bất phương trình bậc nhất "
          "hai ẩn. Mỗi nghiệm chung của tất cả các bất phương trình trong hệ gọi là **một nghiệm của hệ**."),
    ("p", "**Miền nghiệm của hệ** là **phần giao** của các miền nghiệm của từng bất phương trình "
          "trong hệ."),
    ("box", "Cách biểu diễn miền nghiệm của hệ", [
        "Vẽ **tất cả** các đường thẳng ứng với từng bất phương trình trên **cùng một** mặt phẳng tọa độ.",
        "Xác định miền nghiệm của **từng** bất phương trình (bằng cách thử điểm như trên).",
        "**Lấy phần giao** – thường là một **đa giác** (tam giác, tứ giác…). Nhớ **gạch bỏ** các phần "
        "không thuộc miền nghiệm để hình vẽ rõ ràng.",
        "Để **kiểm tra** kết quả, chọn một điểm nằm sâu trong miền giao và thử với **tất cả** các bất "
        "phương trình: nếu đúng hết thì hình vẽ đúng.",
    ]),

    ("h3", "2. Bài toán tối ưu (quy hoạch tuyến tính) – dạng câu tự luận 1,0 điểm"),
    ("p", "Đây là dạng bài **quan trọng nhất** của chương và **chắc chắn** có trong đề. Cấu trúc luôn "
          "gồm hai phần: **lập mô hình** và **tìm phương án tối ưu**."),
    ("box", "Quy trình 4 bước giải bài toán tối ưu", [
        "**Bước 1 – Đặt ẩn.** Gọi x, y lần lượt là số lượng sản phẩm loại I, loại II cần sản xuất. "
        "Luôn kèm điều kiện **x ≥ 0, y ≥ 0**.",
        "**Bước 2 – Lập hệ bất phương trình.** Mỗi điều kiện ràng buộc (nguyên liệu, thời gian, "
        "nhân công, vốn…) chuyển thành **một** bất phương trình bậc nhất hai ẩn.",
        "**Bước 3 – Xác định miền nghiệm và tọa độ các đỉnh.** Miền nghiệm là một đa giác; tìm tọa độ "
        "các đỉnh bằng cách **giải hệ phương trình** tạo bởi hai đường thẳng cắt nhau tại đỉnh đó.",
        "**Bước 4 – Tính giá trị hàm mục tiêu F(x; y)** tại **tất cả** các đỉnh rồi so sánh.",
        "__Định lí (quan trọng):__ nếu miền nghiệm là một đa giác lồi và F = ax + by thì F đạt "
        "**giá trị lớn nhất** và **giá trị nhỏ nhất** tại một trong các **đỉnh** của đa giác đó. "
        "Vì vậy **chỉ cần thử ở các đỉnh**, không cần xét điểm bên trong.",
    ]),

    ("box", "Ví dụ mẫu – bài toán tối ưu đầy đủ", [
        "**Đề bài.** Một xưởng sản xuất hai loại sản phẩm I và II. Mỗi sản phẩm loại I cần **3 kg** "
        "nguyên liệu và **1 giờ** công; mỗi sản phẩm loại II cần **2 kg** nguyên liệu và **2 giờ** công. "
        "Xưởng hiện có **120 kg** nguyên liệu và **80 giờ** công. Mỗi sản phẩm loại I cho lãi "
        "**4 triệu đồng**, loại II cho lãi **3 triệu đồng**. Hỏi xưởng nên sản xuất bao nhiêu sản phẩm "
        "mỗi loại để **lãi lớn nhất**?",
        "**Giải.** Gọi x, y (x, y ≥ 0) là số sản phẩm loại I và loại II cần sản xuất. Ta có hệ:",
        "• Nguyên liệu: 3x + 2y ≤ 120;   • Giờ công: x + 2y ≤ 80;   • x ≥ 0, y ≥ 0.",
        "Miền nghiệm là tứ giác OABC với **O(0; 0)**, **A(40; 0)**, **B(20; 30)**, **C(0; 40)** "
        "(xem Hình 3). Trong đó B là giao điểm của hai đường thẳng:",
        "Giải hệ { 3x + 2y = 120 ; x + 2y = 80 } ta được x = 20, y = 30 ⇒ B(20; 30).",
        "Hàm mục tiêu (tiền lãi, đơn vị triệu đồng): **F(x; y) = 4x + 3y**.",
        "• F(O) = 0;   • F(A) = 4·40 = **160**;   • F(B) = 4·20 + 3·30 = **170**;   "
        "• F(C) = 3·40 = **120**.",
        "Vậy F lớn nhất bằng **170 triệu đồng** khi **x = 20, y = 30**.",
        "**Kết luận:** xưởng nên sản xuất **20 sản phẩm loại I và 30 sản phẩm loại II** để lãi lớn nhất "
        "là **170 triệu đồng**.",
    ]),

    ("img", "assets/mien-nghiem.png", 11.6,
     "Hình 3. Miền nghiệm (tứ giác OABC) của hệ bất phương trình trong ví dụ mẫu"),

    ("h2", "Các dạng toán thường gặp – Bất phương trình"),

    ("h3", "Dạng 1. Kiểm tra một cặp số có là nghiệm không"),
    ("p", "**Phương pháp:** thay trực tiếp x, y vào bất phương trình. Nếu được bất đẳng thức đúng thì là "
          "nghiệm; ngược lại thì không. **Chú ý chiều của bất đẳng thức** khi tính ra số âm."),
    ("box", "Ví dụ mẫu", [
        "**Ví dụ.** Cặp số nào sau đây là nghiệm của bất phương trình 2x − y > 1: "
        "(1; 0), (0; 1), (1; 1)?",
        "**Giải.** (1; 0): 2 − 0 = 2 > 1 ⇒ **là nghiệm**. (0; 1): 0 − 1 = −1 > 1 **sai** ⇒ không là "
        "nghiệm. (1; 1): 2 − 1 = 1 > 1 **sai** (vì không có dấu bằng) ⇒ **không** là nghiệm.",
    ]),

    ("h3", "Dạng 2. Biểu diễn miền nghiệm của một bất phương trình"),
    ("p", "**Phương pháp:** theo đúng 4 bước ở mục 2.1. Nhớ phân biệt **nét liền / nét đứt** cho bờ."),

    ("h3", "Dạng 3. Biểu diễn miền nghiệm của hệ bất phương trình"),
    ("p", "**Phương pháp:** vẽ chung các đường thẳng, xác định từng nửa mặt phẳng rồi lấy giao. "
          "Miền nghiệm thường là một đa giác; cần **liệt kê đủ tọa độ các đỉnh** vì bước sau (tối ưu) "
          "sẽ dùng đến."),

    ("h3", "Dạng 4. Bài toán thực tế – tìm phương án tối ưu"),
    ("p", "**Phương pháp:** theo quy trình 4 bước ở khung trên. Khi trình bày, luôn viết đủ: "
          "**đặt ẩn và điều kiện → hệ bất phương trình → tọa độ các đỉnh → bảng giá trị hàm mục tiêu → "
          "kết luận** (kết luận phải trả lời đúng câu hỏi thực tế, có đơn vị)."),
    ("note", "Khi đề cho \"số sản phẩm\" thì x, y phải là **số nguyên không âm**. Tuy nhiên khi giải "
             "bằng phương pháp đỉnh, ta cứ giải trên miền thực; nếu đỉnh tìm được không nguyên thì cần "
             "kiểm tra thêm các điểm nguyên gần đỉnh. Trong đề thi giữa kì, các đỉnh thường được chọn "
             "là số nguyên nên kết quả luôn đẹp."),

    ("h2", "Tóm tắt công thức chương II"),
    ("table",
     ["Nội dung", "Công thức / cách làm"],
     [
         ["Dạng tổng quát", "ax + by ≤ c (a, b không đồng thời bằng 0)"],
         ["Nghiệm", "Bộ (x_{0}; y_{0}) thỏa mãn bất đẳng thức"],
         ["Miền nghiệm", "Một nửa mặt phẳng bờ d: ax + by = c"],
         ["Bờ", "≤, ≥: nét liền (lấy bờ);  <, >: nét đứt (không lấy bờ)"],
         ["Điểm thử", "O(0; 0) nếu d không qua O; nếu qua O thì dùng (1; 0) hoặc (0; 1)"],
         ["Miền nghiệm của hệ", "Giao các miền nghiệm thành phần (đa giác)"],
         ["Cực trị hàm F = ax + by", "Chỉ đạt tại các **đỉnh** của đa giác miền nghiệm"],
     ],
     [4.6, 12.0],
     ["l", "l"]),
]


PART3 = [
    ("h1", "CHƯƠNG III – HỆ THỨC LƯỢNG TRONG TAM GIÁC", "Phần 3", "toc3"),
    ("lead", "Đây là chương \"được điểm\" của đề: **khoảng 3,0 điểm** gồm 2 câu trắc nghiệm nhận biết, "
             "1 câu thông hiểu, 1 câu trả lời ngắn vận dụng và **1 câu tự luận thực tiễn**. Kiến thức ít, "
             "công thức gọn – chỉ cần học thuộc **bảng giá trị lượng giác** và **3 định lí**."),

    ("h2", "3.1  Giá trị lượng giác của một góc từ 0° đến 180°"),
    ("mark", "toc3a"),

    ("h3", "1. Định nghĩa"),
    ("p", "Trong mặt phẳng tọa độ Oxy, lấy nửa đường tròn đơn vị (nửa trên của đường tròn tâm O bán "
          "kính 1). Với mỗi góc α (0° ≤ α ≤ 180°), ta xác định được **duy nhất** điểm M trên nửa đường "
          "tròn đó sao cho góc xOM = α. Giả sử M có tọa độ **(x_{0}; y_{0})**. Khi đó:"),
    ("table",
     ["Giá trị lượng giác", "Kí hiệu", "Định nghĩa"],
     [
         ["Sin", "sin α", "y_{0} (tung độ của M)"],
         ["Côsin", "cos α", "x_{0} (hoành độ của M)"],
         ["Tang", "tan α", "y_{0}/x_{0}  (xác định khi x_{0} ≠ 0, tức α ≠ 90°)"],
         ["Côtang", "cot α", "x_{0}/y_{0}  (xác định khi y_{0} ≠ 0, tức α ≠ 0° và α ≠ 180°)"],
     ],
     [3.4, 2.4, 10.8],
     ["l", "c", "l"]),
    ("p", "Vì M nằm trên nửa đường tròn đơn vị nên **−1 ≤ cos α ≤ 1**, **0 ≤ sin α ≤ 1** "
          "với mọi α ∈ [0°; 180°]."),
    ("box", "Dấu của các giá trị lượng giác (rất hay hỏi)", [
        "Với **0° < α < 90°** (góc nhọn): **sin α > 0, cos α > 0, tan α > 0, cot α > 0**.",
        "Với **α = 90°**: sin 90° = 1, cos 90° = 0, **tan 90° và cot 90° không xác định**.",
        "Với **90° < α < 180°** (góc tù): **sin α > 0** nhưng **cos α < 0, tan α < 0, cot α < 0**.",
        "__Ghi nhớ một câu:__ \"**sin luôn dương** trên 0°–180°; cos chỉ dương khi góc **nhọn**\".",
    ]),

    ("h3", "2. Bảng giá trị lượng giác của các góc đặc biệt"),
    ("table",
     ["α", "0°", "30°", "45°", "60°", "90°", "120°", "135°", "150°", "180°"],
     [
         ["**sin α**", "0", "1/2", "√2/2", "√3/2", "1", "√3/2", "√2/2", "1/2", "0"],
         ["**cos α**", "1", "√3/2", "√2/2", "1/2", "0", "−1/2", "−√2/2", "−√3/2", "−1"],
         ["**tan α**", "0", "√3/3", "1", "√3", "║", "−√3", "−1", "−√3/3", "0"],
         ["**cot α**", "║", "√3", "1", "√3/3", "0", "−√3/3", "−1", "−√3", "║"],
     ],
     [1.9, 1.3, 1.6, 1.6, 1.6, 1.3, 1.6, 1.6, 1.6, 1.6],
     ["c", "c", "c", "c", "c", "c", "c", "c", "c", "c"]),
    ("note", "Kí hiệu **║** nghĩa là giá trị **không xác định**. Cách nhớ nhanh: sin tăng dần từ 0 đến 1 "
             "rồi giảm về 0 (đối xứng qua 90°); cos giảm dần từ 1 về −1."),

    ("h3", "3. Hai góc bù nhau và hai góc phụ nhau"),
    ("box", "Hai góc BÙ nhau (tổng bằng 180°) – công thức cốt lõi của chương", [
        "**sin(180° − α) = sin α**   ← sin **giữ nguyên**",
        "**cos(180° − α) = −cos α**   ← cos **đổi dấu**",
        "**tan(180° − α) = −tan α**",
        "**cot(180° − α) = −cot α**",
        "__Ví dụ:__ sin 150° = sin 30° = 1/2;  cos 150° = −cos 30° = −√3/2;  "
        "tan 135° = −tan 45° = −1.",
    ]),
    ("box", "Hai góc PHỤ nhau (tổng bằng 90°)", [
        "**sin(90° − α) = cos α**;   **cos(90° − α) = sin α**",
        "**tan(90° − α) = cot α**;   **cot(90° − α) = tan α**",
        "__Ví dụ:__ sin 60° = cos 30° = √3/2.",
    ]),

    ("h3", "4. Các hệ thức lượng giác cơ bản"),
    ("eq", "sin^{2}α + cos^{2}α = 1        (đúng với **mọi** α)"),
    ("eq", "tan α = sin α / cos α    (cos α ≠ 0)"),
    ("eq", "cot α = cos α / sin α    (sin α ≠ 0)"),
    ("eq", "tan α · cot α = 1    (α ≠ 0°, 90°, 180°)"),
    ("eq", "1 + tan^{2}α = 1/cos^{2}α        và        1 + cot^{2}α = 1/sin^{2}α"),

    ("box", "Cách tính sin khi biết cos (và ngược lại) – dùng liên tục", [
        "Từ **sin^{2}α + cos^{2}α = 1** suy ra **sin α = √(1 − cos^{2}α)** và **cos α = ±√(1 − sin^{2}α)**.",
        "**Bước quan trọng nhất: xác định dấu.**",
        "• Nếu **0° < α < 90°** (nhọn) ⇒ cos α **> 0**, chọn dấu **+**.",
        "• Nếu **90° < α < 180°** (tù) ⇒ cos α **< 0**, chọn dấu **−**.",
        "Còn **sin α luôn dương** với 0° < α < 180° nên **không cần** xét dấu của sin.",
    ]),

    ("h2", "3.2  Hệ thức lượng trong tam giác"),
    ("mark", "toc3b"),
    ("p", "Xét tam giác ABC với các cạnh: **a = BC** (đối diện góc A), **b = CA** (đối diện góc B), "
          "**c = AB** (đối diện góc C); R là bán kính đường tròn **ngoại tiếp**, r là bán kính đường tròn "
          "**nội tiếp**, p = (a + b + c)/2 là **nửa chu vi**, S là **diện tích**."),

    ("h3", "1. Định lí côsin"),
    ("box", "Định lí côsin", [
        "**a^{2} = b^{2} + c^{2} − 2bc·cos A**",
        "**b^{2} = c^{2} + a^{2} − 2ca·cos B**",
        "**c^{2} = a^{2} + b^{2} − 2ab·cos C**",
        "**Hệ quả** (dùng để tính góc khi biết 3 cạnh):",
        "**cos A = (b^{2} + c^{2} − a^{2}) / (2bc)**, tương tự cho cos B và cos C.",
        "__Dùng khi biết:__ **2 cạnh và góc xen giữa** (tìm cạnh thứ ba) hoặc **3 cạnh** (tìm góc).",
        "__Ghi nhớ:__ cạnh bên trái **bình phương** = tổng bình phương **hai cạnh còn lại** "
        "trừ **2 lần tích** hai cạnh đó **nhân cos góc xen giữa**.",
    ]),

    ("h3", "2. Định lí sin"),
    ("box", "Định lí sin", [
        "**a / sin A = b / sin B = c / sin C = 2R**",
        "Hệ quả: **a = 2R·sin A**, **sin A = a / (2R)**, **R = a / (2 sin A)**.",
        "__Dùng khi biết:__ **1 cạnh và 2 góc** (tìm các cạnh còn lại) hoặc **1 cạnh và góc đối diện** "
        "(tìm bán kính R).",
    ]),

    ("h3", "3. Công thức tính diện tích tam giác"),
    ("box", "Năm công thức diện tích – chọn theo dữ kiện đề cho", [
        "**(1)** S = ½·a·h_{a}   (h_{a} là đường cao kẻ từ A) – công thức quen thuộc.",
        "**(2)** S = ½·ab·sin C = ½·bc·sin A = ½·ca·sin B   (biết 2 cạnh và góc xen giữa).",
        "**(3)** S = abc / (4R)   (biết 3 cạnh và bán kính ngoại tiếp).",
        "**(4)** S = p·r   (biết nửa chu vi và bán kính nội tiếp).",
        "**(5)** S = √(p(p − a)(p − b)(p − c))   – **công thức Heron** (biết 3 cạnh).",
    ]),

    ("h3", "4. Giải tam giác"),
    ("p", "**Giải tam giác** là tìm **tất cả** các cạnh và góc còn lại của tam giác khi biết một số yếu tố "
          "xác định tam giác đó. Bốn trường hợp thường gặp:"),
    ("table",
     ["Biết", "Cách làm", "Công cụ"],
     [
         ["2 cạnh và góc xen giữa (b, c, A)", "Tính a trước, rồi tính góc còn lại", "Định lí côsin"],
         ["3 cạnh (a, b, c)", "Tính góc lớn nhất trước (tránh nhầm góc tù)", "Hệ quả định lí côsin"],
         ["1 cạnh và 2 góc (a, B, C)", "Tính góc thứ ba: A = 180° − B − C; rồi tính b, c",
          "Định lí sin"],
         ["2 cạnh và góc **không** xen giữa", "Dùng định lí sin, chú ý có thể có **2 nghiệm hình**",
          "Định lí sin"],
     ],
     [4.6, 8.2, 3.8],
     ["l", "l", "l"]),

    ("h3", "5. Ứng dụng thực tiễn – dạng câu tự luận chắc chắn có"),
    ("p", "Hai mô hình thực tế hay gặp nhất:"),
    ("num", [
        "**Đo khoảng cách giữa hai điểm mà không thể đo trực tiếp** (có vật cản, hai điểm ở hai bên "
        "bờ sông…): chọn một điểm thứ ba nhìn thấy cả hai, đo **một cạnh** và **hai góc** của tam giác "
        "tạo thành, rồi dùng **định lí sin** để tính cạnh cần tìm.",
        "**Đo chiều cao của vật** (cột cờ, tòa nhà, ngọn núi): đặt hai vị trí quan sát trên mặt đất "
        "cách nhau một khoảng đã biết, đo hai **góc nâng**, dùng **định lí sin** để tính khoảng cách "
        "tới chân vật rồi nhân với **tan** góc nâng để ra chiều cao (cộng thêm chiều cao giác kế).",
    ]),
    ("box", "Ví dụ mẫu – đo khoảng cách", [
        "**Đề bài.** Hai người quan sát đứng ở hai vị trí A và B trên bờ, cách nhau **100 m**. Họ cùng "
        "nhìn về một chiếc thuyền ở vị trí C trên biển. Biết góc BAC = **60°**, góc ABC = **75°**. "
        "Tính khoảng cách từ B đến thuyền (làm tròn đến mét).",
        "**Giải.** Trong tam giác ABC: góc C = 180° − 60° − 75° = **45°**.",
        "Theo định lí sin: BC / sin A = AB / sin C, suy ra",
        "BC = AB · sin A / sin C = 100 · sin 60° / sin 45° = 100 · (√3/2)/(√2/2) = 100√(3/2) ≈ **122 m**.",
        "**Kết luận:** khoảng cách từ B đến thuyền khoảng **122 m**.",
        "__Lưu ý trình bày:__ phải nêu rõ **tam giác nào**, **góc nào**, **định lí nào dùng** – "
        "đó chính là các điểm thành phần của thang điểm 1,0 điểm.",
    ]),

    ("h2", "Tóm tắt công thức chương III"),
    ("table",
     ["Công thức", "Nội dung", "Dùng khi"],
     [
         ["Hai góc bù", "sin(180°−α) = sin α;  cos(180°−α) = −cos α", "Đưa góc tù về góc nhọn"],
         ["Hệ thức cơ bản", "sin^{2}α + cos^{2}α = 1", "Biết 1 giá trị, tìm giá trị khác"],
         ["Định lí côsin", "a^{2} = b^{2} + c^{2} − 2bc·cos A", "2 cạnh + góc xen giữa; hoặc 3 cạnh"],
         ["Hệ quả côsin", "cos A = (b^{2} + c^{2} − a^{2})/(2bc)", "3 cạnh → tìm góc"],
         ["Định lí sin", "a/sin A = b/sin B = c/sin C = 2R", "1 cạnh + 2 góc; tìm R"],
         ["Diện tích (2)", "S = ½·bc·sin A", "2 cạnh + góc xen giữa"],
         ["Diện tích (3)", "S = abc/(4R)", "Biết 3 cạnh + R"],
         ["Diện tích (4)", "S = p·r", "Biết nửa chu vi + r"],
         ["Heron", "S = √(p(p−a)(p−b)(p−c))", "Biết 3 cạnh"],
     ],
     [3.0, 8.0, 5.6],
     ["l", "l", "l"]),
]


# --------------------------------------------------------------------------
# Bổ sung: bài tập tự luyện chương II và III
# --------------------------------------------------------------------------
PART2_EXTRA = [
    ("h2", "Bài tập tự luyện chương II"),
    ("bullets", [
        "**Bài 1.** Cặp số nào sau đây là nghiệm của bất phương trình **x − 2y < 3**: "
        "(1; 0), (0; 2), (−1; 1), (3; 0)?",
        "**Bài 2.** Biểu diễn miền nghiệm của bất phương trình **x + 2y ≥ 4** trên mặt phẳng tọa độ.",
        "**Bài 3.** Biểu diễn miền nghiệm của hệ { x + y ≤ 6 ; 2x + y ≤ 8 ; x ≥ 0 ; y ≥ 0 }, chỉ rõ tọa độ "
        "các đỉnh của miền nghiệm.",
        "**Bài 4.** Một gia đình có 40 kg gạo và 30 kg thịt dùng để nấu hai loại bánh A và B. Mỗi bánh "
        "loại A cần 2 kg gạo và 1 kg thịt; mỗi bánh loại B cần 1 kg gạo và 2 kg thịt. Mỗi bánh loại A "
        "lãi 3 triệu, mỗi bánh loại B lãi 2 triệu. Tìm số bánh mỗi loại để lãi lớn nhất.",
    ]),
    ("box", "Đáp số và gợi ý", [
        "**Bài 1.** (1; 0): 1 < 3 ✔ là nghiệm.  (0; 2): −4 < 3 ✔ **là nghiệm**.  (−1; 1): −3 < 3 ✔ "
        "**là nghiệm**.  (3; 0): 3 < 3 ✘ (không có dấu bằng) ⇒ **không** là nghiệm.",
        "**Bài 2.** Vẽ d: x + 2y = 4 qua (4; 0) và (0; 2), nét **liền**. Thử O(0; 0) được 0 ≥ 4 sai ⇒ "
        "miền nghiệm là nửa mặt phẳng bờ d **không chứa O**, kể cả bờ.",
        "**Bài 3.** Các đỉnh: **O(0; 0), (4; 0), (2; 4), (0; 6)**. "
        "Trong đó (2; 4) là giao của x + y = 6 và 2x + y = 8.",
        "**Bài 4.** Gọi x, y là số bánh loại A, B. Hệ: 2x + y ≤ 40; x + 2y ≤ 30; x, y ≥ 0. "
        "Các đỉnh: (0; 0), (20; 0), (0; 15), **(50/3; 20/3)** là giao của hai đường thẳng. "
        "Hàm lợi nhuận F = 3x + 2y: F(0;0) = 0; F(20;0) = 60; F(0;15) = 30; "
        "F(50/3; 20/3) = 50 + 40/3 ≈ **63,33** ⇒ lớn nhất tại **x = 50/3, y = 20/3**. "
        "Vì số bánh phải nguyên, xét các điểm nguyên gần đó: **(16; 6)** cho F = 60 và "
        "**(17; 6)**: 2·17 + 6 = 40 ✔, 17 + 12 = 29 ≤ 30 ✔ ⇒ F = 51 + 12 = **63**. "
        "Vậy sản xuất **17 bánh loại A và 6 bánh loại B** để lãi lớn nhất (63 triệu, gần bằng cận trên).",
    ]),
]


PART3_EXTRA = [
    ("h2", "Bài tập tự luyện chương III"),
    ("bullets", [
        "**Bài 1.** Tính: a) sin 120°;  b) cos 135°;  c) tan 150°;  d) cot 120°.",
        "**Bài 2.** Cho sin α = 5/13 và 90° < α < 180°. Tính cos α và tan α.",
        "**Bài 3.** Rút gọn biểu thức A = sin^{2}x + cos^{2}x + 2sin x·cos x − 1.",
        "**Bài 4.** Tam giác ABC có a = 7, b = 8, góc C = 60°. Tính cạnh c và diện tích S.",
        "**Bài 5.** Tam giác ABC có góc A = 45°, góc B = 60°, cạnh a = 10. Tính cạnh b và "
        "bán kính đường tròn ngoại tiếp R.",
        "**Bài 6.** Tam giác ABC có ba cạnh 5, 6, 7. Tính diện tích bằng công thức Heron và bán kính r "
        "của đường tròn nội tiếp.",
        "**Bài 7.** Từ hai vị trí A, B cách nhau 80 m trên bờ, người ta đo được góc tạo bởi phương nhìn "
        "tới một cây ở bên kia sông là 65° (tại A) và 50° (tại B). Tính khoảng cách từ A đến cây.",
    ]),
    ("box", "Đáp số và gợi ý", [
        "**Bài 1.** a) sin 120° = sin 60° = **√3/2**.  b) cos 135° = −cos 45° = **−√2/2**.  "
        "c) tan 150° = −tan 30° = **−√3/3**.  d) cot 120° = −cot 60° = **−√3/3**.",
        "**Bài 2.** cos^{2}α = 1 − 25/169 = 144/169; góc tù nên **cos α = −12/13**; "
        "**tan α = sin α / cos α = (5/13)/(−12/13) = −5/12**.",
        "**Bài 3.** A = (sin x + cos x)^{2} − 1 = 1 + 2sin x cos x − 1 = **2sin x·cos x = sin 2x** "
        "(ở lớp 10 có thể dừng ở **2sin x·cos x**).",
        "**Bài 4.** c^{2} = 49 + 64 − 2·7·8·cos 60° = 113 − 56 = 57 ⇒ **c = √57**. "
        "S = ½·7·8·sin 60° = **14√3**.",
        "**Bài 5.** Góc C = 75°. b = a·sin B / sin A = 10·sin 60° / sin 45° = 10·(√3/2)/(√2/2) = "
        "**5√6**. R = a / (2sin A) = 10 / (2·√2/2) = 10/√2 = **5√2**.",
        "**Bài 6.** p = 9; S = √(9·4·3·2) = √216 = **6√6**. r = S/p = 6√6/9 = **2√6/3**.",
        "**Bài 7.** Góc C = 180° − 65° − 50° = 65°. AC = AB·sin B / sin C = 80·sin 50° / sin 65° "
        "≈ 80·0,766/0,906 ≈ **68 m**.",
    ]),
]
