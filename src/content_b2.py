# -*- coding: utf-8 -*-
"""PHẦN B – Chương II: Bất phương trình và hệ bất phương trình bậc nhất hai ẩn."""

from reportlab.lib.units import mm

from pdf_kit import (
    CONTENT_W as CH, H2, H3, P, SP, box, bullets, formula, numbered, tbl,
    FeasibleFig, PRIMARY, TEAL, ACCENT, PURPLE,
)

from content_b1 import _dang


def part_b2() -> list:
    out = [
        H2("B.2. CHƯƠNG II – BẤT PHƯƠNG TRÌNH VÀ HỆ BẤT PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN"),
        P("Chương này chiếm {b}2,5 điểm{/b}: 1,25 điểm trắc nghiệm cho bất phương trình và 1,25 điểm cho hệ "
          "(gồm câu vận dụng cao ở phần tự luận). Điểm mấu chốt là {b}vẽ đúng đường thẳng biên{/b} và "
          "{b}chọn đúng nửa mặt phẳng{/b}."),

        H3("B.2.1. Bất phương trình bậc nhất hai ẩn"),
        tbl([
            ["Khái niệm", "Nội dung"],
            ["Định nghĩa", "Bất phương trình bậc nhất hai ẩn x, y có dạng tổng quát "
                           "{b}ax + by ≤ c{/b} (hoặc ≥, <, >), trong đó a, b, c là số thực cho trước, "
                           "{b}a và b không đồng thời bằng 0{/b}."],
            ["Nghiệm", "Cặp số (x{sub}0{/sub}; y{sub}0{/sub}) là nghiệm nếu thay vào ta được một bất đẳng "
                       "thức đúng. Mỗi nghiệm là một điểm trong mặt phẳng toạ độ."],
            ["Miền nghiệm", "Tập hợp tất cả các điểm biểu diễn nghiệm là một {b}nửa mặt phẳng{/b} "
                            "(kể cả bờ nếu bất phương trình có dấu ≤ hoặc ≥, không kể bờ nếu có dấu < hoặc >)."],
            ["Đường thẳng biên", "d: ax + by = c chia mặt phẳng thành hai nửa: một nửa gồm các điểm thoả "
                                 "ax + by < c, nửa kia thoả ax + by > c."],
        ], widths=[34 * mm, CH - 34 * mm], fontsize=8.3),
        SP(3),
        box("method",
            [P("{b}Quy tắc biểu diễn miền nghiệm của ax + by ≤ c{/b}", "box_body"),
             numbered([
                 "Vẽ đường thẳng d: ax + by = c (nét liền nếu có dấu ≤, ≥; nét đứt nếu có dấu <, >).",
                 "Chọn một điểm {b}thử{/b} không nằm trên d – thường là gốc O(0; 0) cho dễ tính.",
                 "Thay toạ độ điểm thử vào bất phương trình: nếu được bất đẳng thức đúng thì {b}miền nghiệm "
                 "là nửa mặt phẳng chứa điểm thử{/b} (kể cả bờ theo quy ước trên); nếu sai thì lấy nửa còn lại.",
                 "Kết luận: miền nghiệm là nửa mặt phẳng (tô màu) – nêu rõ bờ có lấy hay không.",
             ], "box_body")]),
        SP(2),
        box("warn",
            [P("{b}Đừng quên tô miền.{/b} Trong bài tự luận, vẽ đường thẳng mà không tô miền và không "
               "kết luận thì mất điểm phần “biểu diễn miền nghiệm”.", "box_body"),
             P("{b}Điểm O(0;0) nằm trên d{/b} (khi c = 0): không dùng được – chọn điểm khác, ví dụ (1; 0) "
               "hoặc (0; 1).", "box_body")]),
        SP(4),

        *_dang(1, "Nhận biết bất phương trình bậc nhất hai ẩn; kiểm tra một cặp số là nghiệm",
               "Nhận biết", "chỉ ra hệ số a, b, c; thử cặp số vào bất phương trình."),
        bullets([
            "Phải có {b}đúng hai ẩn{/b} x, y và bậc nhất (không có x², xy, sin x…). Ví dụ "
            "{b}2x − 3y + 5 ≤ 0{/b} là bất phương trình bậc nhất hai ẩn với a = 2, b = −3, c = −5 "
            "(sau khi chuyển 5 sang phải).",
            "{b}Không phải{/b}: x² + y ≤ 1 (có x²); 0x + 0y < 3 (a = b = 0); x − 2 < 0 (chỉ một ẩn).",
            "Thử nghiệm: thay số, tính, so sánh – chỉ cần một phản ví dụ để loại.",
        ]),
        box("example",
            [P("{b}Ví dụ.{/b} Cho bất phương trình 3x − y ≤ 6. Hỏi các cặp số sau có là nghiệm không: "
               "(0; 0), (3; 1), (2; 4)?", "box_body"),
             SP(2),
             P("{b}Giải.{/b} Thay lần lượt:", "box_body"),
             P("(0; 0): 3·0 − 0 = 0 ≤ 6 → {b}đúng{/b} ⇒ là nghiệm.   (3; 1): 9 − 1 = 8 > 6 → {b}sai{/b} ⇒ "
               "không là nghiệm.   (2; 4): 6 − 4 = 2 ≤ 6 → {b}đúng{/b} ⇒ là nghiệm.", "box_body")],
            title="VÍ DỤ MẪU – DẠNG 1"),
        SP(4),

        *_dang(2, "Biểu diễn miền nghiệm của một bất phương trình", "Thông hiểu",
               "vẽ đúng đường thẳng biên và chọn đúng nửa mặt phẳng, kết luận rõ bờ."),
        box("example",
            [P("{b}Ví dụ.{/b} Biểu diễn miền nghiệm của bất phương trình 2x + y ≤ 6.", "box_body"),
             SP(2),
             P("{b}Giải.{/b} Vẽ đường thẳng d: 2x + y = 6, đi qua hai điểm (0; 6) và (3; 0). "
               "Thay O(0; 0): 2·0 + 0 = 0 ≤ 6 đúng ⇒ miền nghiệm là nửa mặt phẳng {b}bờ d, chứa gốc O{/b} "
               "(kể cả đường thẳng d vì có dấu ≤).", "box_body"),
             SP(3),
             FeasibleFig(
                 lines=[(2, 1, 6), (1, 0, 0), (0, 1, 0)],
                 vertices=[(0, 0), (3, 0), (0, 6)],
                 xmax=7, ymax=8, width=260, height=205,
                 caption="Hình 4. Miền nghiệm của 2x + y ≤ 6 (tô màu) – nửa mặt phẳng chứa O",
                 vertex_labels=["O", "A", "B"],
             ),
], title="VÍ DỤ MẪU – DẠNG 2"),
        SP(2),
        box("tip",
            [P("{b}Mẹo chọn nhanh:{/b} nếu c > 0 thì O(0;0) thường thuộc miền nghiệm của “ax + by ≤ c”; "
               "nếu c < 0 thì O thường {b}không{/b} thuộc. Cách gọn nhất vẫn là {i}thử O{/i} – "
               "chỉ mất 5 giây.", "box_body")]),
        SP(4),

        H3("B.2.2. Hệ bất phương trình bậc nhất hai ẩn"),
        P("Hệ gồm hai hay nhiều bất phương trình bậc nhất hai ẩn. {b}Nghiệm của hệ{/b} là cặp số thoả "
          "{b}tất cả{/b} các bất phương trình trong hệ; {b}miền nghiệm của hệ{/b} là {b}giao{/b} các miền "
          "nghiệm thành phần. Miền nghiệm thường là một đa giác (có thể không bị chặn)."),
        SP(2),
        box("note",
            [P("{b}Miền nghiệm của hệ bị chặn bởi các đường thẳng{/b} là một đa giác lồi. Các đỉnh của đa giác "
               "là giao điểm của các đường thẳng biên – {b}chỉ cần xét các đỉnh{/b} khi tìm giá trị lớn nhất, "
               "nhỏ nhất của biểu thức bậc nhất F = ax + by.", "box_body")]),
        SP(3),

        *_dang(3, "Biểu diễn miền nghiệm của hệ bất phương trình", "Thông hiểu – Vận dụng",
               "vẽ từng đường biên, xác định giao các nửa mặt phẳng, nêu toạ độ các đỉnh."),
        numbered([
            "Vẽ tất cả các đường thẳng biên trên {b}cùng một{/b} hệ trục.",
            "Với mỗi bất phương trình, xác định nửa mặt phẳng nhận (thử O hoặc một điểm bất kỳ).",
            "Phần {b}chung{/b} của các nửa mặt phẳng là miền nghiệm; tô đậm và ghi toạ độ các đỉnh.",
            "Kiểm tra: một đỉnh là giao của hai đường biên nên phải thoả {b}mọi{/b} bất phương trình của hệ.",
        ]),
        box("example",
            [P("{b}Ví dụ.{/b} Biểu diễn miền nghiệm của hệ:", "box_body"),
             formula(["x ≥ 0,  y ≥ 0", "x + y ≤ 6", "2x + y ≤ 8"], "(1)"),
             P("{b}Giải.{/b} Bốn đường biên: Oy (x = 0), Ox (y = 0), d{sub}1{/sub}: x + y = 6, "
               "d{sub}2{/sub}: 2x + y = 8. Miền nghiệm nằm trong góc phần tư thứ nhất (do x ≥ 0, y ≥ 0).", "box_body"),
             P("Các đỉnh của miền:", "box_body"),
             bullets([
                 "O(0; 0).",
                 "d{sub}2{/sub} cắt Ox tại (4; 0) ⇒ A(4; 0).",
                 "d{sub}1{/sub} cắt d{sub}2{/sub}: giải hệ x + y = 6, 2x + y = 8 ⇒ x = 2, y = 4 ⇒ B(2; 4).",
                 "d{sub}1{/sub} cắt Oy tại (0; 6) ⇒ C(0; 6).",
             ], "bullet_small"),
             P("Miền nghiệm là tứ giác {b}OABC{/b} (kể cả biên) – xem Hình 5.", "box_body"),
             SP(3),
             FeasibleFig(
                 lines=[(1, 1, 6), (2, 1, 8), (1, 0, 0), (0, 1, 0)],
                 vertices=[(0, 0), (4, 0), (2, 4), (0, 6)],
                 xmax=6.2, ymax=7.2, width=230, height=195,
                 caption="Hình 5. Miền nghiệm của hệ (1) – tứ giác OABC",
                 vertex_labels=["O", "A(4; 0)", "B(2; 4)", "C(0; 6)"],
             )],
            title="VÍ DỤ MẪU – DẠNG 3"),
        SP(3),
        box("warn",
            [P("{b}Lỗi hay gặp:{/b} lấy giao của {i}các đường thẳng{/i} thay vì giao của {i}các nửa mặt phẳng{/i}. "
               "Hãy thử một điểm {b}bên trong{/b} miền dự kiến với đủ bốn bất phương trình – nếu có bất phương "
               "trình sai thì miền chọn sai.", "box_body")]),
        SP(4),

        *_dang(4, "Bài toán tối ưu: tìm giá trị lớn nhất, nhỏ nhất của F = ax + by",
               "Vận dụng – Vận dụng cao",
               "chuyển bài toán thực tế về hệ bất phương trình, tìm phương án tối ưu."),
        box("method",
            [P("{b}Quy trình 4 bước{/b}", "box_body"),
             numbered([
                 "Gọi ẩn (kèm đơn vị, điều kiện {b}nguyên không âm{/b} nếu là số lượng).",
                 "Viết các điều kiện ràng buộc thành hệ bất phương trình bậc nhất hai ẩn.",
                 "Viết hàm mục tiêu F = ax + by (lợi nhuận, chi phí, số tiền…).",
                 "Vẽ miền nghiệm, liệt kê {b}tất cả{/b} đỉnh, tính F tại từng đỉnh, so sánh và kết luận "
                 "(nhớ trả lời đúng câu hỏi và ghi đơn vị).",
             ], "box_body"),
             SP(2),
             P("{b}Định lí:{/b} nếu miền nghiệm là đa giác lồi thì F đạt giá trị lớn nhất và nhỏ nhất tại một "
               "trong các đỉnh của đa giác đó.", "box_body")]),
        SP(2),
        box("example",
            [P("{b}Ví dụ.{/b} Một xưởng may nhận may hai loại áo. Mỗi áo sơ mi cần 2 m vải và 3 giờ công, lãi "
               "50 000 đồng; mỗi áo khoác cần 3 m vải và 2 giờ công, lãi 70 000 đồng. Xưởng có 600 m vải và "
               "600 giờ công. Hỏi mỗi loại may bao nhiêu áo để lãi lớn nhất?", "box_body"),
             SP(2),
             P("{b}Giải.{/b} Gọi x, y (chiếc) lần lượt là số áo sơ mi và áo khoác, x ≥ 0, y ≥ 0, x, y nguyên.",
               "box_body"),
             formula(["2x + 3y ≤ 600   (vải)", "3x + 2y ≤ 600   (giờ công)", "x ≥ 0,  y ≥ 0"]),
             P("Lợi nhuận (nghìn đồng): {b}F = 50x + 70y{/b}.", "box_body"),
             P("Các đỉnh: O(0; 0), A(200; 0) (từ 3x + 2y = 600 với y = 0), B(0; 200), và giao điểm của "
               "2x + 3y = 600 với 3x + 2y = 600:", "box_body"),
             P("Giải hệ ⇒ x = y = 120 ⇒ C(120; 120).", "box_body"),
             SP(2),
             tbl([
                 ["Đỉnh", "O(0; 0)", "A(200; 0)", "B(0; 200)", "C(120; 120)"],
                 ["F = 50x + 70y (nghìn đồng)", "0", "10 000", "14 000", "{b}14 400{/b}"],
             ], widths=[52 * mm] + [(CH - 52 * mm) / 4] * 4, fontsize=8.3,
                 align=["l", "c", "c", "c", "c"]),
             SP(3),
             P("Vậy F lớn nhất bằng 14 400 nghìn đồng khi {b}x = y = 120{/b}: may 120 áo sơ mi và 120 áo khoác, "
               "lãi 14 400 000 đồng.", "box_body"),
             SP(2),
             P("{i}Kiểm tra ràng buộc: vải 2·120 + 3·120 = 600 (vừa đủ); công 3·120 + 2·120 = 600 (vừa đủ). "
               "Cả hai nguồn đều dùng hết – dấu hiệu bài toán được thiết kế để điểm tối ưu nằm ở giao điểm.{/i}",
               "box_body")], title="VÍ DỤ MẪU – DẠNG 4"),
        SP(3),
        box("exam",
            [P("{b}Ba điều phải viết trong bài tự luận tối ưu:{/b}", "box_body"),
             bullets([
                 "Hệ bất phương trình ràng buộc {b}kèm điều kiện x ≥ 0, y ≥ 0{/b} (nhiều bạn quên, mất 0,25 điểm).",
                 "Bảng giá trị F tại {b}tất cả{/b} các đỉnh.",
                 "Kết luận {b}có đơn vị{/b} và trả lời đúng câu hỏi (số lượng bao nhiêu, lãi bao nhiêu).",
             ], "bullet_small")]),
    ]
    return out


def exercises_b2() -> list:
    return [
        box("exam",
            [P("{b}Bài tập áp dụng (đáp số ở Phần E).{/b}", "box_body"),
             SP(2),
             P("{b}7.{/b} Trong các bất phương trình sau, bất phương trình nào là bậc nhất hai ẩn? "
               "(a) 3x − 2y < 5; (b) x² + y ≥ 1; (c) 0x + 4y ≤ 8; (d) x + y − z > 0.", "box_body"),
             P("{b}8.{/b} Biểu diễn miền nghiệm của: (a) x + 2y ≤ 4; (b) 3x − y > 3.", "box_body"),
             P("{b}9.{/b} Biểu diễn miền nghiệm của hệ: x ≥ 0, y ≥ 0, x + y ≤ 5, x + 2y ≤ 8. "
               "Tìm toạ độ các đỉnh.", "box_body"),
             P("{b}10.{/b} Tìm giá trị lớn nhất của F = 2x + 3y trên miền nghiệm của hệ ở bài 9.", "box_body"),
             P("{b}11.{/b} Một cửa hàng bán hai loại bánh: bánh ngọt lãi 20 000 đồng/chiếc, bánh mặn lãi "
               "15 000 đồng/chiếc. Mỗi ngày cửa hàng làm được tối đa 80 chiếc, trong đó bánh ngọt không quá 50 "
               "chiếc, và tổng số bánh mặn không ít hơn 20 chiếc. Hỏi mỗi ngày nên làm bao nhiêu chiếc mỗi loại "
               "để lãi lớn nhất?", "box_body"),
            ], title="BÀI TẬP ÁP DỤNG – CHƯƠNG II"),
    ]
