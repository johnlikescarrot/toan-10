# -*- coding: utf-8 -*-
"""PHẦN B – Chương III (hệ thức lượng) và Chương IV (vectơ) + B.5 bảng công thức."""

from reportlab.lib.units import mm

from pdf_kit import (
    CONTENT_W as CH, H2, H3, P, SP, box, bullets, formula, numbered, tbl,
    HeightFig, ParallelogramFig, ACCENT, PRIMARY,
)

from content_b1 import _dang


def part_b3() -> list:
    out = [
        H2("B.3. CHƯƠNG III – HỆ THỨC LƯỢNG TRONG TAM GIÁC"),
        P("Chương này chiếm {b}3,0 điểm{/b} – nhiều thứ hai trong đề, và là nơi dễ mất điểm nhất vì phải nhớ "
          "nhiều công thức. Cách học hiệu quả: học {b}bảng giá trị lượng giác{/b} và {b}ba công thức gốc{/b} "
          "(côsin, sin, diện tích), mọi bài tập đều xoay quanh chúng."),

        H3("B.3.1. Giá trị lượng giác của một góc từ 0° đến 180°"),
        P("{b}Định nghĩa.{/b} Trong mặt phẳng toạ độ Oxy, lấy nửa đường tròn đơn vị (tâm O, bán kính 1) ở nửa "
          "mặt phẳng y ≥ 0. Với mỗi góc α (0° ≤ α ≤ 180°), lấy điểm M(x{sub}0{/sub}; y{sub}0{/sub}) trên nửa "
          "đường tròn sao cho ∠xOM = α. Khi đó:"),
        formula(["sin α = y{sub}0{/sub}        cos α = x{sub}0{/sub}",
                 "tan α = y{sub}0{/sub} / x{sub}0{/sub}   (x{sub}0{/sub} ≠ 0)        "
                 "cot α = x{sub}0{/sub} / y{sub}0{/sub}   (y{sub}0{/sub} ≠ 0)"]),
        SP(2),
        tbl([
            ["Góc α", "0°", "30°", "45°", "60°", "90°", "120°", "135°", "150°", "180°"],
            ["sin α", "0", "1/2", "√2/2", "√3/2", "1", "√3/2", "√2/2", "1/2", "0"],
            ["cos α", "1", "√3/2", "√2/2", "1/2", "0", "−1/2", "−√2/2", "−√3/2", "−1"],
            ["tan α", "0", "1/√3", "1", "√3", "‖", "−√3", "−1", "−1/√3", "0"],
            ["cot α", "‖", "√3", "1", "1/√3", "0", "−1/√3", "−1", "−√3", "‖"],
        ], widths=[20 * mm] + [(CH - 20 * mm) / 9] * 9, fontsize=8.0,
            align=["l"] + ["c"] * 9, zebra=False),
        SP(2),
        P("{i}Kí hiệu ‖: giá trị không xác định (tan 90° và cot 0°, cot 180° không tồn tại). Học bảng này "
          "bằng cách nhớ 3 cột gốc 30° – 45° – 60° rồi suy ra các góc còn lại bằng tính chất bù.{/i}", "small"),
        SP(3),
        box("note",
            [P("{b}Dấu của giá trị lượng giác{/b}", "box_body"),
             tbl([
                 ["Góc α", "sin", "cos", "tan", "cot"],
                 ["0° < α < 90° (nhọn)", "+", "+", "+", "+"],
                 ["α = 90°", "+", "0", "không xác định", "0"],
                 ["90° < α < 180° (tù)", "+", "−", "−", "−"],
             ], widths=[40 * mm, 22 * mm, 22 * mm, 40 * mm, CH - 40 * mm - 64 * mm - 20 * mm],
                 fontsize=8.2, zebra=False),
             SP(2),
             P("{b}Ghi nhớ:{/b} với 0° ≤ α ≤ 180° thì {b}sin α luôn không âm{/b}; cos đổi dấu khi qua 90°.",
               "box_body")]),
        SP(3),
        box("note",
            [P("{b}Hai góc bù nhau{/b} (α và 180° − α): {b}sin bằng nhau{/b}, còn cos, tan, cot {b}đổi dấu{/b}.",
               "box_body"),
             formula(["sin(180° − α) = sin α        cos(180° − α) = −cos α",
                      "tan(180° − α) = −tan α        cot(180° − α) = −cot α"]),
             P("{b}Hai góc phụ nhau{/b} (α và 90° − α): sin góc này bằng cos góc kia, tan góc này bằng cot góc kia.",
               "box_body"),
             formula(["sin(90° − α) = cos α        cos(90° − α) = sin α        tan(90° − α) = cot α"])]),
        SP(3),
        box("note",
            [P("{b}Các hệ thức lượng giác cơ bản{/b} (dùng để biến đổi biểu thức):", "box_body"),
             formula(["sin²α + cos²α = 1",
                      "tan α = sin α / cos α    (cos α ≠ 0)",
                      "cot α = cos α / sin α    (sin α ≠ 0)",
                      "tan α · cot α = 1",
                      "1 + tan²α = 1/cos²α    (cos α ≠ 0)",
                      "1 + cot²α = 1/sin²α    (sin α ≠ 0)"])]),
        SP(4),

        *_dang(1, "Tính giá trị lượng giác của góc đặc biệt", "Nhận biết",
               "dùng bảng giá trị và tính chất góc bù để tính nhanh, không cần máy tính."),
        box("example",
            [P("{b}Ví dụ.{/b} Tính sin 150°, cos 135°, tan 120°.", "box_body"),
             SP(2),
             P("{b}Giải.{/b} Dùng góc bù:", "box_body"),
             P("sin 150° = sin(180° − 30°) = sin 30° = {b}1/2{/b}.", "box_body"),
             P("cos 135° = −cos(180° − 135°) = −cos 45° = {b}−√2/2{/b} (góc tù nên cos âm).", "box_body"),
             P("tan 120° = −tan(180° − 120°) = −tan 60° = {b}−√3{/b}.", "box_body")],
            title="VÍ DỤ MẪU – DẠNG 1"),
        SP(2),
        box("tip",
            [P("{b}Bấm máy tính (Casio/Vinacal):{/b} bật chế độ {b}DEG{/b} (màn hình hiện D). "
               "Với sin/cos/tan: bấm phím rồi nhập số đo, ví dụ {b}sin 150{/b} → −? Nếu ra 0,5 là đúng. "
               "Với cot: không có phím cot, bấm {b}1 ÷ tan(α){/b}. Với góc cho bằng độ – phút – giây dùng phím "
               "{b}°′″{/b}.", "box_body"),
             P("{b}Kiểm tra dấu:{/b} nếu máy ra cos 120° = 0,5 thì bạn đang ở chế độ RAD hoặc nhập sai – "
               "cos của góc tù {b}phải âm{/b}.", "box_body")]),
        SP(4),

        *_dang(2, "Cho một giá trị lượng giác, tính các giá trị còn lại", "Thông hiểu",
               "dùng sin² + cos² = 1 và quan hệ tan = sin/cos, chú ý chọn dấu theo miền góc."),
        numbered([
            "Xác định góc α nhọn hay tù (đề cho 0° < α < 90° hay 90° < α < 180°) → quyết định {b}dấu{/b} của "
            "cos, tan, cot.",
            "Dùng sin²α + cos²α = 1 để tìm giá trị còn thiếu (lấy căn, chọn dấu theo bước 1).",
            "Tính tan = sin/cos, cot = cos/sin (hoặc 1/tan).",
        ]),
        box("example",
            [P("{b}Ví dụ.{/b} Cho sin α = 3/5 với 90° < α < 180°. Tính cos α, tan α, cot α.", "box_body"),
             SP(2),
             P("{b}Giải.{/b} Vì 90° < α < 180° nên cos α < 0. Ta có:", "box_body"),
             P("cos²α = 1 − sin²α = 1 − 9/25 = 16/25 ⇒ |cos α| = 4/5 ⇒ {b}cos α = −4/5{/b}.", "box_body"),
             P("tan α = sin α / cos α = (3/5) : (−4/5) = {b}−3/4{/b};   cot α = 1/tan α = {b}−4/3{/b}.", "box_body"),
             SP(2),
             P("{i}Nếu đề cho α nhọn thì cos α = +4/5 và tan α = 3/4 – chỉ khác dấu. Đây là lí do phải đọc kĩ "
               "điều kiện góc.{/i}", "box_body")], title="VÍ DỤ MẪU – DẠNG 2"),
        SP(4),

        *_dang(3, "Tính giá trị hoặc rút gọn biểu thức lượng giác", "Vận dụng",
               "dùng góc bù, hằng đẳng thức sin² + cos² = 1 để thu gọn."),
        box("example",
            [P("{b}Ví dụ.{/b} Tính giá trị biểu thức P = 3sin α + 4cos α, biết sin α = 3/5 và 90° < α < 180°.",
               "box_body"),
             SP(2),
             P("{b}Giải.{/b} Từ Dạng 2: cos α = −4/5. Vậy P = 3·(3/5) + 4·(−4/5) = 9/5 − 16/5 = {b}−7/5{/b}.",
               "box_body"),
             SP(3),
             P("{b}Ví dụ 2.{/b} Rút gọn Q = sin²α + sin²(180° − α) + 2cos²α.", "box_body"),
             P("{b}Giải.{/b} Vì sin(180° − α) = sin α nên sin²(180° − α) = sin²α. Do đó "
               "Q = 2sin²α + 2cos²α = 2(sin²α + cos²α) = {b}2{/b}.", "box_body")],
            title="VÍ DỤ MẪU – DẠNG 3"),
        SP(4),

        H3("B.3.2. Hệ thức lượng trong tam giác"),
        P("Kí hiệu thống nhất: tam giác ABC có BC = a, CA = b, AB = c; R là bán kính đường tròn ngoại tiếp, "
          "r là bán kính đường tròn nội tiếp, p = (a + b + c)/2 là nửa chu vi, S là diện tích."),
        SP(3),
        box("note",
            [P("{b}Định lí côsin{/b} – dùng khi biết {b}hai cạnh và góc xen giữa{/b}, hoặc {b}ba cạnh{/b}:",
               "box_body"),
             formula(["a² = b² + c² − 2bc·cos A",
                      "b² = c² + a² − 2ca·cos B        c² = a² + b² − 2ab·cos C"]),
             P("{b}Hệ quả{/b} – dùng để tìm góc khi biết ba cạnh:", "box_body"),
             formula(["cos A = (b² + c² − a²) / (2bc)",
                      "cos B = (c² + a² − b²) / (2ca)        cos C = (a² + b² − c²) / (2ab)"]),
             P("{b}Định lí sin{/b} – dùng khi biết {b}góc và cạnh đối diện{/b}, hoặc cần bán kính ngoại tiếp:",
               "box_body"),
             formula("a / sin A = b / sin B = c / sin C = 2R"),
             P("{b}Công thức diện tích{/b}:", "box_body"),
             formula(["S = ½·a·h{sub}a{/sub} = ½·ab·sin C = ½·bc·sin A = ½·ca·sin B",
                      "S = abc/(4R) = p·r = √(p(p − a)(p − b)(p − c))"]),
             P("{i}Công thức cuối là công thức Heron – dùng khi biết ba cạnh.{/i}", "box_body")]),
        SP(3),
        box("warn",
            [P("{b}Ba lỗi chết người khi dùng công thức:{/b}", "box_body"),
             bullets([
                 "Góc trong công thức côsin phải là góc {b}xen giữa{/b} hai cạnh còn lại: a² dùng cos {b}A{/b} "
                 "(A đối diện a). Dùng cos B là sai ngay.",
                 "Công thức diện tích ½ab·sin C dùng góc {b}C xen giữa{/b} a và b – không phải góc bất kỳ.",
                 "Khi tìm góc bằng máy tính: cos A < 0 ⇒ {b}A là góc tù{/b}; đừng vội kết luận tam giác vuông.",
             ], "bullet_small")]),
        SP(4),

        *_dang(4, "Giải tam giác: tính cạnh, góc, diện tích", "Thông hiểu – Vận dụng",
               "chọn đúng công thức theo dữ kiện đề cho (cạnh–góc–cạnh, cạnh–cạnh–cạnh, góc–cạnh)."),
        tbl([
            ["Dữ kiện đã biết", "Công cụ nên dùng", "Thứ tự tính"],
            ["Hai cạnh và góc xen giữa (b, c, A)", "Định lí côsin", "a → góc B (hệ quả côsin hoặc sin) → C = 180° − A − B → S"],
            ["Ba cạnh (a, b, c)", "Hệ quả côsin", "Góc lớn nhất trước (đối diện cạnh lớn nhất) → góc còn lại → S (Heron)"],
            ["Một cạnh và hai góc (a, B, C)", "Định lí sin", "A = 180° − B − C → b, c theo sin → S = ½ab·sin C"],
            ["Hai cạnh và góc không xen giữa", "Định lí sin (có thể 2 nghiệm)", "Dùng sin → kiểm tra tổng góc; loại nghiệm không hợp lí"],
        ], widths=[46 * mm, 36 * mm, CH - 46 * mm - 36 * mm], fontsize=8.1),
        SP(2),
        box("example",
            [P("{b}Ví dụ.{/b} Cho tam giác ABC có b = 5, c = 8 và A = 60°. Tính cạnh a và diện tích S.", "box_body"),
             SP(2),
             P("{b}Giải.{/b} Theo định lí côsin:", "box_body"),
             P("a² = b² + c² − 2bc·cos A = 25 + 64 − 2·5·8·(1/2) = 89 − 40 = 49 ⇒ {b}a = 7{/b}.", "box_body"),
             P("Diện tích: S = ½·b·c·sin A = ½·5·8·(√3/2) = {b}10√3 ≈ 17,32{/b}.", "box_body"),
             SP(2),
             P("{i}Nhận xét: 7² = 5² + 8² − 40 nên tam giác không vuông; nếu cos A = 0 thì a² = b² + c² "
               "(Pythagore) và tam giác vuông tại A.{/i}", "box_body")],
            title="VÍ DỤ MẪU – DẠNG 4"),
        SP(4),

        *_dang(5, "Nhận dạng tam giác, chứng minh hệ thức", "Vận dụng",
               "dùng côsin, sin, diện tích để chứng minh tam giác vuông / cân / đều hoặc đẳng thức."),
        box("example",
            [P("{b}Ví dụ.{/b} Cho tam giác ABC có a = 13, b = 14, c = 15. "
               "(a) Tính diện tích S, bán kính R, r. (b) Tam giác có góc nào tù không?", "box_body"),
             SP(2),
             P("{b}Giải.{/b} (a) Nửa chu vi p = (13 + 14 + 15)/2 = 21. Theo Heron:", "box_body"),
             P("S = √(21·8·7·6) = √7056 = {b}84{/b}.", "box_body"),
             P("Từ S = abc/(4R) ⇒ R = abc/(4S) = (13·14·15)/(4·84) = 2730/336 = {b}8,125{/b}.", "box_body"),
             P("Từ S = p·r ⇒ r = S/p = 84/21 = {b}4{/b}.", "box_body"),
             P("(b) Góc lớn nhất là C (đối diện cạnh 15). cos C = (a² + b² − c²)/(2ab) = "
               "(169 + 196 − 225)/(2·13·14) = 140/364 ≈ 0,385 > 0 ⇒ C nhọn. Vậy tam giác {b}không có góc tù{/b}.",
               "box_body")], title="VÍ DỤ MẪU – DẠNG 5"),
        SP(4),

        *_dang(6, "Bài toán thực tế: khoảng cách, chiều cao", "Vận dụng",
               "mô hình hoá bằng tam giác, chọn công thức, tính và trả lời có đơn vị."),
        numbered([
            "Vẽ hình, đặt tên điểm (A, B, C, T…) và ghi các số đo đã biết lên hình.",
            "Xác định tam giác chứa đại lượng cần tìm; kiểm tra đã biết những gì (2 cạnh + góc xen giữa? "
            "1 cạnh + 2 góc?).",
            "Áp dụng côsin / sin / diện tích; nếu cần, giải tam giác phụ trước (ví dụ tính đường cao trong "
            "tam giác nhỏ rồi mới tính khoảng cách lớn).",
            "Kết luận, làm tròn theo yêu cầu và ghi đơn vị (m, km…).",
        ]),
        box("example",
            [P("{b}Ví dụ.{/b} Từ hai vị trí A và B cách nhau 30 m trên mặt đất, người ta quan sát đỉnh T của "
               "một cột cờ. Góc nâng từ A là 30°, từ B là 60° (A, B, chân cột C thẳng hàng, B gần cột hơn). "
               "Biết mắt người quan sát cách mặt đất 1,6 m, tính chiều cao cột cờ (làm tròn đến 0,1 m).",
               "box_body"),
             SP(2),
             HeightFig(caption="Hình 6. Sơ đồ đo chiều cao cột cờ bằng hai góc nâng"),
             SP(2),
             P("{b}Giải.{/b} Xét tam giác ABT: góc tại A là 30°, góc tại B là 180° − 60° = 120° (vì góc nâng "
               "60° là góc ngoài). Suy ra ∠ATB = 180° − 30° − 120° = 30°.", "box_body"),
             P("Do ∠TAB = ∠ATB = 30° nên tam giác ABT cân tại B ⇒ {b}BT = AB = 30 m{/b}.", "box_body"),
             P("Trong tam giác vuông BTC: TC = BT·sin 60° = 30·(√3/2) = 15√3 ≈ 25,98 m.", "box_body"),
             P("Chiều cao cột cờ = TC + 1,6 ≈ 25,98 + 1,6 = {b}27,6 m{/b}.", "box_body"),
             SP(2),
             P("{i}Bài toán này giải bằng định lí sin cũng được: AT/sin 120° = 30/sin 30° ⇒ AT = 30√3, rồi "
               "TC = AT·sin 30° = 15√3. Hai cách cho cùng kết quả – hãy chọn cách bạn thấy chắc chắn hơn.{/i}",
               "box_body")], title="VÍ DỤ MẪU – DẠNG 6"),
        SP(3),
        box("tip",
            [P("{b}Hai mô hình thực tế hay gặp{/b}", "box_body"),
             bullets([
                 "{b}Khoảng cách giữa hai điểm có vật cản{/b} (không đo trực tiếp được): chọn một điểm thứ ba "
                 "nhìn thấy cả hai, đo hai cạnh và góc xen giữa → định lí côsin.",
                 "{b}Chiều cao vật{/b} (không trèo lên được): đo khoảng cách trên mặt đất và hai góc nâng → "
                 "định lí sin trong tam giác tạo bởi hai điểm quan sát và đỉnh vật.",
             ], "bullet_small")]),
    ]
    return out


def exercises_b3() -> list:
    return [
        box("exam",
            [P("{b}Bài tập áp dụng (đáp số ở Phần E).{/b}", "box_body"),
             SP(2),
             P("{b}12.{/b} Tính: sin 120°, cos 150°, tan 135°, cot 120°.", "box_body"),
             P("{b}13.{/b} Cho cos α = −5/13 với 90° < α < 180°. Tính sin α, tan α.", "box_body"),
             P("{b}14.{/b} Rút gọn: A = sin²40° + sin²50° + cos²40° + cos²50°.", "box_body"),
             P("{b}15.{/b} Cho tam giác ABC có a = 13, b = 14, c = 15. Tính diện tích S và bán kính R, r.", "box_body"),
             P("{b}16.{/b} Cho tam giác ABC có AB = 5, AC = 7, góc A = 60°. Tính BC và diện tích tam giác.", "box_body"),
             P("{b}17.{/b} Cho tam giác ABC có a = 8, B = 45°, C = 60°. Tính góc A, cạnh b và c.", "box_body"),
             P("{b}18.{/b} Hai người đứng cách nhau 120 m trên bờ biển, cùng nhìn một hòn đảo. Góc tạo bởi "
               "phương nhìn từ người thứ nhất với đường nối hai người là 60°, và từ người thứ hai (về phía hòn "
               "đảo) là 45°. Tính khoảng cách từ người thứ nhất đến hòn đảo.", "box_body"),
            ], title="BÀI TẬP ÁP DỤNG"),
    ]


def part_b4() -> list:
    out = [
        H2("B.4. CHƯƠNG IV – VECTƠ (KHÁI NIỆM VECTƠ)"),
        P("{b}Lưu ý phạm vi thi:{/b} theo ma trận, phần vectơ chỉ kiểm tra {b}khái niệm vectơ{/b} (0,5 điểm, "
          "2 câu nhận biết – thông hiểu). Các phép cộng, trừ vectơ và tích vô hướng {b}chưa{/b} nằm trong "
          "phạm vi giữa kì I – đừng học lan sang, nhưng phải thật chắc phần định nghĩa vì đây là điểm dễ lấy."),
        SP(3),
        tbl([
            ["Khái niệm", "Định nghĩa – ghi nhớ"],
            ["Vectơ", "Đoạn thẳng có {b}hướng{/b}: kí hiệu {b}AB{/b} (A là điểm đầu, B là điểm cuối) "
                      "hoặc {b}a{/b}, {b}b{/b}… Vectơ {b}AB{/b} còn được viết là $\\overrightarrow{AB}$ – "
                      "trong tài liệu này dùng chữ in đậm."],
            ["Giá của vectơ", "{b}Đường thẳng đi qua điểm đầu và điểm cuối{/b} của vectơ. Hai vectơ có giá "
                              "{b}song song hoặc trùng nhau{/b} thì gọi là {b}cùng phương{/b}."],
            ["Độ dài vectơ", "|{b}AB{/b}| = AB (độ dài đoạn thẳng). Độ dài là một {b}số không âm{/b}."],
            ["Hai vectơ cùng phương", "Giá song song hoặc trùng nhau. Khi đó chúng hoặc {b}cùng hướng{/b}, "
                                       "hoặc {b}ngược hướng{/b}."],
            ["Hai vectơ cùng hướng", "Cùng phương và {b}cùng chiều{/b} (mũi tên chỉ về một phía)."],
            ["Hai vectơ bằng nhau", "{b}Cùng hướng và cùng độ dài{/b}: {b}AB{/b} = {b}CD{/b} ⇔ cùng hướng và "
                                    "AB = CD. {b}Chỉ cần một trong hai điều kiện sai là không bằng nhau.{/b}"],
            ["Vectơ – không", "Vectơ có điểm đầu trùng điểm cuối: {b}AA{/b} = {b}0{/b}. "
                              "|{b}0{/b}| = 0; {b}0{/b} cùng phương, cùng hướng với {b}mọi{/b} vectơ."],
            ["Hai vectơ đối nhau", "Cùng độ dài nhưng {b}ngược hướng{/b}: {b}AB{/b} và {b}BA{/b} là hai vectơ "
                                    "đối nhau, kí hiệu {b}AB{/b} = −{b}BA{/b}."],
        ], widths=[36 * mm, CH - 36 * mm], fontsize=8.2),
        SP(3),
        box("warn",
            [P("{b}Ba câu hỏi tự kiểm tra trước khi kết luận “hai vectơ bằng nhau”{/b}", "box_body"),
             numbered([
                 "Hai vectơ có {b}cùng phương{/b} không? (nếu không → loại)",
                 "Chúng có {b}cùng hướng{/b} không? (cùng phương nhưng ngược chiều → không bằng nhau)",
                 "Độ dài có {b}bằng nhau{/b} không?",
             ], "box_body"),
             P("{b}Chú ý:{/b} {b}AB{/b} = {b}CD{/b} {b}không{/b} có nghĩa là đoạn thẳng AB = CD theo nghĩa "
               "“trùng nhau”; hai vectơ bằng nhau có thể nằm ở hai vị trí khác nhau.", "box_body")]),
        SP(4),

        *_dang(1, "Nhận diện các khái niệm vectơ qua hình vẽ", "Nhận biết",
               "chỉ ra vectơ cùng phương, cùng hướng, bằng nhau, đối nhau trong hình bình hành, "
               "tam giác đều, lục giác đều."),
        ParallelogramFig(caption="Hình 7. Hình bình hành ABCD – {b}AB{/b} = {b}DC{/b}, {b}AD{/b} = {b}BC{/b}"),
        SP(3),
        bullets([
            "Trong hình bình hành ABCD: {b}AB{/b} = {b}DC{/b} và {b}AD{/b} = {b}BC{/b} "
            "(cùng hướng, cùng độ dài). Ngược lại {b}AB{/b} và {b}CD{/b} là hai vectơ {b}đối nhau{/b}.",
            "Trong tam giác đều ABC: |{b}AB{/b}| = |{b}BC{/b}| = |{b}CA{/b}| nhưng ba vectơ này "
            "{b}không cùng phương{/b}, nên {b}không bằng nhau{/b}.",
            "Trong lục giác đều ABCDEF tâm O: các cạnh đều bằng nhau; các vectơ cùng hướng với {b}AB{/b} "
            "gồm {b}AB{/b}, {b}FO{/b}, {b}OC{/b}, {b}ED{/b}… (cùng phương và cùng chiều).",
            "{b}Vectơ – không{/b} {b}AA{/b} cùng phương, cùng hướng với {b}mọi{/b} vectơ, nhưng chỉ bằng "
            "{b}BB{/b}, {b}CC{/b} (tức bằng {b}0{/b}).",
        ]),
        box("example",
            [P("{b}Ví dụ.{/b} Cho hình bình hành ABCD tâm O. Hãy chỉ ra: (a) vectơ bằng {b}AB{/b}; "
               "(b) vectơ đối của {b}OA{/b}; (c) các vectơ cùng phương với {b}AC{/b}.", "box_body"),
             SP(2),
             P("{b}Giải.{/b} (a) {b}AB{/b} = {b}DC{/b} (vì ABCD là hình bình hành nên AB ∥ DC và AB = DC, "
               "cùng chiều).", "box_body"),
             P("(b) O là trung điểm AC nên {b}OA{/b} và {b}OC{/b} ngược hướng, cùng độ dài ⇒ {b}OC{/b} là "
               "vectơ đối của {b}OA{/b} (tức {b}OA{/b} = −{b}OC{/b}).", "box_body"),
             P("(c) {b}AC{/b} có giá là đường chéo AC. Hai vectơ cùng phương với {b}AC{/b} (cùng giá) chỉ có "
               "thể là {b}AC{/b} và {b}CA{/b} – ngược hướng nhau; các cạnh của hình bình hành không song song "
               "với đường chéo AC.", "box_body")], title="VÍ DỤ MẪU – DẠNG 1"),
        SP(4),

        *_dang(2, "Chứng minh hai vectơ bằng nhau; tính độ dài vectơ", "Thông hiểu",
               "dùng tính chất hình học (trung điểm, hình bình hành, tam giác đều) để suy ra cùng hướng "
               "và cùng độ dài."),
        numbered([
            "Xác định {b}giá{/b} của hai vectơ: có song song/trùng nhau không?",
            "Xác định {b}chiều{/b} (cùng hướng hay ngược hướng) – vẽ mũi tên để chắc chắn.",
            "So sánh {b}độ dài{/b}: dùng giả thiết (trung điểm, hình bình hành, tam giác đều…).",
            "Kết luận và ghi rõ căn cứ (ví dụ “vì ABCD là hình bình hành”).",
        ]),
        box("example",
            [P("{b}Ví dụ.{/b} Cho tam giác ABC, M và N lần lượt là trung điểm của AB và AC. "
               "Chứng tỏ {b}MN{/b} và {b}BC{/b} cùng hướng, và tính |{b}MN{/b}| biết BC = 10.", "box_body"),
             SP(2),
             P("{b}Giải.{/b} MN là đường trung bình của tam giác ABC nên MN ∥ BC và MN = ½BC. "
               "Hơn nữa, khi đi từ M đến N ta đi cùng chiều với khi đi từ B đến C ⇒ {b}MN{/b} và {b}BC{/b} "
               "{b}cùng hướng{/b}. Vậy |{b}MN{/b}| = ½|{b}BC{/b}| = {b}5{/b}.", "box_body"),
             SP(2),
             P("{i}Lưu ý: {b}MN{/b} và {b}BC{/b} cùng hướng nhưng khác độ dài nên {b}không bằng nhau{/b}. "
               "Quan hệ đúng giữa chúng là quan hệ về độ dài: |{b}MN{/b}| = ½|{b}BC{/b}|. Đừng viết "
               "{b}MN{/b} = ½{b}BC{/b} như một đẳng thức vectơ khi chưa định nghĩa phép nhân vectơ với số "
               "(nội dung của học kì sau).{/i}", "box_body")],
            title="VÍ DỤ MẪU – DẠNG 2"),
        SP(3),
        box("note",
            [P("{b}Phân biệt ba kí hiệu dễ lẫn{/b}", "box_body"),
             tbl([
                 ["Kí hiệu", "Nghĩa", "Ví dụ"],
                 ["{b}AB{/b}", "Vectơ từ A đến B (có hướng)", "{b}AB{/b} và {b}BA{/b} là hai vectơ đối nhau"],
                 ["|{b}AB{/b}|", "Độ dài vectơ = độ dài đoạn thẳng", "|{b}AB{/b}| = AB = 5"],
                 ["AB", "Độ dài đoạn thẳng (số)", "AB = 5 cm"],
             ], widths=[24 * mm, 60 * mm, CH - 84 * mm], fontsize=8.2, zebra=False)]),
    ]
    return out


def exercises_b4() -> list:
    return [
        box("exam",
            [P("{b}Bài tập áp dụng (đáp số ở Phần E).{/b}", "box_body"),
             SP(2),
             P("{b}19.{/b} Cho hình vuông ABCD cạnh 4. Tính |{b}AB{/b}|, |{b}AC{/b}| và chỉ ra một vectơ bằng "
               "{b}AB{/b}.", "box_body"),
             P("{b}20.{/b} Cho tam giác đều ABC cạnh 3, M là trung điểm BC. Tính |{b}AM{/b}|.", "box_body"),
             P("{b}21.{/b} Cho hình bình hành ABCD. Khẳng định “{b}AB{/b} = {b}CD{/b}” đúng hay sai? Vì sao?",
               "box_body"),
             P("{b}22.{/b} Cho lục giác đều ABCDEF tâm O. Kể tên ba vectơ bằng vectơ {b}AB{/b}.", "box_body"),
            ], title="BÀI TẬP ÁP DỤNG"),
    ]


def part_b5() -> list:
    """B.5 – Bảng công thức cần nhớ (tổng hợp toàn bộ chương trình giữa kì I)."""
    out = [
        H2("B.5. BẢNG CÔNG THỨC CẦN NHỚ (TỔNG HỢP)"),
        P("Trang này để {b}học thuộc{/b} và {b}dò nhanh{/b} trước giờ kiểm tra. Nếu chỉ còn 20 phút, đọc đúng "
          "trang này."),
        SP(4),
        H3("1) Mệnh đề – tập hợp"),
        tbl([
            ["Nội dung", "Công thức / quy tắc"],
            ["Phủ định ∀, ∃", "Phủ định của “∀x ∈ X, P(x)” là “∃x ∈ X, P̄(x)”; phủ định của “∃x ∈ X, P(x)” là "
                               "“∀x ∈ X, P̄(x)”."],
            ["P ⇒ Q", "Chỉ sai khi P đúng, Q sai. P là điều kiện đủ, Q là điều kiện cần."],
            ["Số tập con", "Tập n phần tử có 2{sup}n{/sup} tập con; 2{sup}n{/sup} − 1 tập con khác rỗng."],
            ["Giao – hợp – hiệu", "A ∩ B = {x | x ∈ A và x ∈ B}; A ∪ B = {x | x ∈ A hoặc x ∈ B}; "
                                   "A \\ B = {x | x ∈ A và x ∉ B}."],
            ["Phần bù", "C{sub}A{/sub}B = A \\ B (khi B ⊂ A); C{sub}ℝ{/sub}A = ℝ \\ A."],
            ["Đếm bằng Ven", "|A ∪ B| = |A| + |B| − |A ∩ B|."],
            ["Khoảng – đoạn", "(a; b): a < x < b · [a; b]: a ≤ x ≤ b · (−∞; a]: x ≤ a · [a; +∞): x ≥ a."],
        ], widths=[38 * mm, CH - 38 * mm], fontsize=8.2),
        SP(4),

        H3("2) Bất phương trình bậc nhất hai ẩn"),
        tbl([
            ["Nội dung", "Công thức / quy tắc"],
            ["Dạng", "ax + by ≤ c (≥, <, >) với a² + b² ≠ 0."],
            ["Miền nghiệm", "Là một nửa mặt phẳng bờ là đường thẳng ax + by = c."],
            ["Cách xác định", "Thử điểm O(0; 0) (nếu O ∉ d): đúng → lấy nửa chứa O; sai → lấy nửa còn lại."],
            ["Hệ bất phương trình", "Miền nghiệm = giao các miền nghiệm thành phần (đa giác lồi)."],
            ["Tối ưu F = ax + by", "F đạt max, min tại các {b}đỉnh{/b} của miền nghiệm: lập bảng giá trị tại "
                                    "từng đỉnh rồi so sánh."],
        ], widths=[38 * mm, CH - 38 * mm], fontsize=8.2),
        SP(4),

        H3("3) Giá trị lượng giác"),
        tbl([
            ["Nội dung", "Công thức"],
            ["Định nghĩa", "Với M(x{sub}0{/sub}; y{sub}0{/sub}) trên nửa đường tròn đơn vị: sin α = y{sub}0{/sub}, "
                           "cos α = x{sub}0{/sub}, tan α = y{sub}0{/sub}/x{sub}0{/sub}, "
                           "cot α = x{sub}0{/sub}/y{sub}0{/sub}."],
            ["Cơ bản", "sin²α + cos²α = 1; tan α = sin α/cos α; cot α = cos α/sin α; tan α·cot α = 1."],
            ["Mở rộng", "1 + tan²α = 1/cos²α; 1 + cot²α = 1/sin²α."],
            ["Góc bù", "sin(180° − α) = sin α; cos(180° − α) = −cos α; tan(180° − α) = −tan α; "
                       "cot(180° − α) = −cot α."],
            ["Góc phụ", "sin(90° − α) = cos α; cos(90° − α) = sin α; tan(90° − α) = cot α."],
            ["Dấu", "0° < α < 90°: tất cả dương. 90° < α < 180°: sin dương, cos – tan – cot âm."],
        ], widths=[30 * mm, CH - 30 * mm], fontsize=8.2),
    ]
    return out


def part_b5_tail() -> list:
    out = [
        H2("B.5. BẢNG CÔNG THỨC CẦN NHỚ (tiếp theo)"),
        SP(2),
        H3("4) Hệ thức lượng trong tam giác"),
        tbl([
            ["Nội dung", "Công thức"],
            ["Định lí côsin", "a² = b² + c² − 2bc·cos A"],
            ["Hệ quả côsin", "cos A = (b² + c² − a²)/(2bc)"],
            ["Định lí sin", "a/sin A = b/sin B = c/sin C = 2R"],
            ["Diện tích", "S = ½ah{sub}a{/sub} = ½ab·sin C = abc/(4R) = pr = √(p(p−a)(p−b)(p−c))"],
            ["Liên hệ góc – cạnh", "Cạnh lớn hơn ⇔ góc đối diện lớn hơn; a² < b² + c² ⇔ A nhọn; "
                                    "a² = b² + c² ⇔ A vuông; a² > b² + c² ⇔ A tù."],
        ], widths=[32 * mm, CH - 32 * mm], fontsize=8.2),
        SP(4),

        H3("5) Vectơ"),
        tbl([
            ["Nội dung", "Ghi nhớ"],
            ["Định nghĩa", "Vectơ là đoạn thẳng có hướng; kí hiệu {b}AB{/b}."],
            ["Độ dài", "|{b}AB{/b}| = AB ≥ 0."],
            ["Cùng phương", "Giá song song hoặc trùng nhau."],
            ["Bằng nhau", "Cùng hướng {b}và{/b} cùng độ dài."],
            ["Đối nhau", "Cùng độ dài, ngược hướng: {b}AB{/b} = −{b}BA{/b}."],
            ["Vectơ – không", "{b}0{/b} = {b}AA{/b}; |{b}0{/b}| = 0; cùng phương, cùng hướng với mọi vectơ."],
        ], widths=[32 * mm, CH - 32 * mm], fontsize=8.2),
        SP(4),
        box("tip",
            [P("{b}Kĩ thuật bấm máy tính cho chương lượng giác{/b}", "box_body"),
             tbl([
                 ["Cần tính", "Thao tác trên máy"],
                 ["sin α, cos α, tan α", "Chọn DEG → bấm sin/cos/tan → nhập α → ="],
                 ["cot α", "1 ÷ tan α (hoặc tan(90° − α) nếu α nhọn)"],
                 ["α khi biết sin α", "SHIFT sin (sin⁻¹) → nhập giá trị → = (chú ý có thể có hai nghiệm bù nhau)"],
                 ["α khi biết cos α", "SHIFT cos → nhập giá trị → = ; nếu cos âm, kết quả đã là góc tù"],
                 ["Kiểm tra sin² + cos²", "Bấm sin α → x² → + → cos α → x² → = ; phải bằng 1"],
             ], widths=[48 * mm, CH - 48 * mm], fontsize=8.2, zebra=False),
             SP(2),
             P("{b}Mẹo nhớ bảng GTLG:{/b} viết 0, 1, 2, 3, 4 lần lượt dưới sin của 0°, 30°, 45°, 60°, 90°; "
               "lấy căn rồi chia 2. Cos là dãy ngược lại. Tan = sin/cos.", "box_body")]),
    ]
    return out
