# -*- coding: utf-8 -*-
"""PHẦN B – LÝ THUYẾT TRỌNG TÂM & 12 DẠNG TOÁN (Chương I)."""

from reportlab.lib import colors
from reportlab.lib.units import mm

from pdf_kit import (
    H1, H2, H3, H4, P, SP, box, bullets, formula, numbered, rule, tbl, CONTENT_W,
    VennFig, NumberLineFig, PRIMARY, TEAL,
)

CH = CONTENT_W


def _dang(n, title, muc_do, yeu_cau):
    return [
        H3(f"Dạng {n}. {title}"),
        P("{b}Mức độ:{/b} " + muc_do + "   •   {b}Yêu cầu cần đạt:{/b} " + yeu_cau, "small"),
        SP(2),
    ]


def part_b1() -> list:
    out = [
        H1("PHẦN B. LÝ THUYẾT TRỌNG TÂM VÀ CÁC DẠNG TOÁN"),
        P("Phần này đi theo đúng thứ tự bốn chương trong ma trận. Mỗi chương gồm: {b}(1){/b} lý thuyết cốt lõi "
          "trình bày bằng bảng – công thức; {b}(2){/b} các dạng toán thường gặp, mỗi dạng có quy trình giải, "
          "ví dụ mẫu giải chi tiết và lỗi hay mắc; {b}(3){/b} bài tập áp dụng ngay (đáp số ở Phần E). "
          "Bạn nên đọc lý thuyết, gấp sách lại làm ví dụ, rồi mới đối chiếu lời giải."),
        SP(6),

        H2("B.1. CHƯƠNG I – MỆNH ĐỀ VÀ TẬP HỢP"),
        P("Chương này chiếm {b}4,0 điểm{/b} trong đề (0,5 + 1,25 + 2,25) và phần lớn ở mức nhận biết – thông "
          "hiểu. Đây là vùng “ăn chắc điểm” nếu bạn dùng đúng kí hiệu và cẩn thận với dấu ngoặc."),

        H3("B.1.1. Mệnh đề – mệnh đề chứa biến – phủ định – kéo theo – tương đương"),
        tbl([
            ["Khái niệm", "Định nghĩa / cách viết", "Ví dụ"],
            ["Mệnh đề", "Câu khẳng định có tính {b}đúng hoặc sai{/b} (không thể vừa đúng vừa sai). "
                        "Câu hỏi, câu cảm thán, câu mệnh lệnh {b}không{/b} là mệnh đề.",
             "“5 là số nguyên tố” (Đ) · “17 chia hết cho 3” (S) · “Hôm nay trời đẹp quá!” (không là MĐ)"],
            ["Mệnh đề chứa biến", "Câu khẳng định chứa biến, trở thành mệnh đề khi gán giá trị cụ thể cho biến.",
             "P(n): “n chia hết cho 2”, n ∈ ℕ. P(4) đúng, P(5) sai."],
            ["Mệnh đề phủ định", "Kí hiệu {b}P̄{/b} (hoặc ¬P). {b}P̄ đúng khi P sai{/b} và ngược lại.",
             "P: “π là số hữu tỉ” (S) ⇒ P̄: “π không là số hữu tỉ” (Đ)."],
            ["Mệnh đề kéo theo", "P ⇒ Q (“nếu P thì Q”). {b}Chỉ sai khi P đúng và Q sai.{/b} "
                                  "P là {i}giả thiết{/i}, Q là {i}kết luận{/i}.",
             "“Nếu n chia hết cho 6 thì n chia hết cho 3” (Đ)."],
            ["Mệnh đề đảo", "Q ⇒ P. Mệnh đề đảo của một mệnh đề đúng {b}không nhất thiết{/b} đúng.",
             "“Nếu n chia hết cho 3 thì n chia hết cho 6” – sai (n = 3)."],
            ["Mệnh đề tương đương", "P ⇔ Q (“P khi và chỉ khi Q”): đúng khi {b}P và Q cùng đúng hoặc cùng sai{/b}.",
             "“Tam giác ABC đều ⇔ tam giác ABC có ba góc bằng 60°”."],
            ["Điều kiện cần – đủ", "P ⇒ Q: {b}P là điều kiện đủ{/b} để có Q; {b}Q là điều kiện cần{/b} để có P. "
                                    "P ⇔ Q: P là điều kiện {b}cần và đủ{/b} của Q.",
             "“n chia hết cho 6” là điều kiện đủ để “n chia hết cho 3”; “n chia hết cho 3” là điều kiện cần để "
             "“n chia hết cho 6”."],
            ["Kí hiệu ∀, ∃", "∀x ∈ X, P(x): đúng với {b}mọi{/b} x. ∃x ∈ X, P(x): có {b}ít nhất một{/b} x. "
                              "Phủ định: {b}∀ → ∃{/b} và {b}∃ → ∀{/b}, đồng thời phủ định P(x).",
             "A: “∀x ∈ ℝ, x² ≥ 0” (Đ) ⇒ Ā: “∃x ∈ ℝ, x² < 0” (S)."],
        ], widths=[30 * mm, CH - 30 * mm - 58 * mm, 58 * mm], fontsize=8.1),
        SP(3),
        box("note",
            [P("{b}Quy tắc phủ định “hai lần đổi”:{/b} đổi lượng từ (∀ ↔ ∃) và đổi vế sau (bỏ “không” thành "
               "“không”, thêm/bớt dấu so sánh ngược lại).", "box_body"),
             SP(2),
             P("“Mọi học sinh lớp 10A đều thích Toán” → phủ định: “{b}Có{/b} một học sinh lớp 10A {b}không{/b} "
               "thích Toán”.", "box_body"),
             P("“Tồn tại số thực x sao cho x² = −1” → phủ định: “{b}Với mọi{/b} số thực x, x² {b}≠{/b} −1”.", "box_body")]),
        SP(3),
        box("warn",
            [P("{b}Nhầm 1:{/b} phủ định “x > 3” thành “x < 3”. Sai – phải là “x ≤ 3”.", "box_body"),
             P("{b}Nhầm 2:{/b} coi “P ⇒ Q” đúng là “Q ⇒ P” cũng đúng. Sai – xem mệnh đề đảo ở trên.", "box_body"),
             P("{b}Nhầm 3:{/b} cho rằng câu “x + 1 > 0” là mệnh đề. Sai – đó là mệnh đề chứa biến.", "box_body")]),
        SP(4),

        *_dang(1, "Nhận diện mệnh đề, mệnh đề chứa biến", "Nhận biết",
               "phân biệt câu là mệnh đề / không là mệnh đề / mệnh đề chứa biến."),
        bullets([
            "Có thể {b}đúng hoặc sai{/b} → mệnh đề. Không xác định được đúng sai (câu hỏi, cảm thán, mệnh lệnh, "
            "câu chưa đủ thông tin) → không là mệnh đề.",
            "Chứa biến chưa gán giá trị → mệnh đề chứa biến.",
        ]),
        box("example",
            [P("{b}Ví dụ.{/b} Trong các câu sau, câu nào là mệnh đề? Xác định tính đúng – sai.", "box_body"),
             SP(2),
             bullets([
                 "(a) “Số 2026 chia hết cho 2.”", "(b) “Hãy nộp bài đúng giờ!”",
                 "(c) “2n + 1 là số lẻ.”", "(d) “Phương trình x² + 1 = 0 có nghiệm thực.”",
                 "(e) “Bạn có khỏe không?”",
             ], "bullet_small"),
             SP(2),
             P("{b}Giải.{/b} (a) là mệnh đề, {b}đúng{/b} (2026 = 2·1013). (b) là câu mệnh lệnh → không là mệnh đề. "
               "(c) là mệnh đề chứa biến (chưa gán n). (d) là mệnh đề, {b}sai{/b} vì x² + 1 ≥ 1 > 0 với mọi x. "
               "(e) là câu hỏi → không là mệnh đề.", "box_body")], title="VÍ DỤ MẪU – DẠNG 1"),
        SP(4),

        *_dang(2, "Lập mệnh đề phủ định (kể cả có ∀, ∃)", "Nhận biết – Thông hiểu",
               "phát biểu đúng mệnh đề phủ định và xét tính đúng sai của nó."),
        numbered([
            "Xác định mệnh đề gốc có lượng từ hay không.",
            "Nếu có: đổi ∀ ↔ ∃, giữ nguyên biến và điều kiện của biến.",
            "Phủ định vế sau: thêm “không” hoặc đảo dấu (>, ≥, <, ≤, =, ≠, chia hết ↔ không chia hết).",
            "Kết luận tính đúng – sai: P và P̄ {b}luôn trái ngược nhau{/b}.",
        ]),
        box("example",
            [P("{b}Ví dụ.{/b} Lập mệnh đề phủ định và xét tính đúng sai:", "box_body"),
             SP(2),
             P("A: “∀x ∈ ℕ, x² + 1 > 0”.", "box_body"),
             P("{b}Giải.{/b} Ā: “∃x ∈ ℕ, x² + 1 ≤ 0”. Vì x² + 1 ≥ 1 > 0 với mọi x ∈ ℕ nên Ā {b}sai{/b}, "
               "do đó A {b}đúng{/b}.", "box_body"),
             SP(3),
             P("B: “Tồn tại số tự nhiên n sao cho n² = n + 2”.", "box_body"),
             P("{b}Giải.{/b} B̄: “Với mọi số tự nhiên n, n² ≠ n + 2”. Giải n² = n + 2 ⇔ n = 2 (nhận) hoặc "
               "n = −1 (loại). Vậy B {b}đúng{/b} (vì n = 2 thỏa mãn) và B̄ {b}sai{/b}.", "box_body")],
            title="VÍ DỤ MẪU – DẠNG 2"),
        SP(4),

        *_dang(3, "Mệnh đề kéo theo, mệnh đề đảo, điều kiện cần – đủ", "Thông hiểu",
               "phát biểu P ⇒ Q, mệnh đề đảo, dùng đúng cụm “điều kiện cần”, “điều kiện đủ”."),
        tbl([
            ["Dạng cho trước", "Phát biểu P ⇒ Q", "Điều kiện cần", "Điều kiện đủ"],
            ["“Nếu P thì Q”", "P ⇒ Q", "Q là điều kiện cần để có P", "P là điều kiện đủ để có Q"],
            ["“Để có Q, cần có P”", "Q ⇒ P", "P", "Q"],
            ["“P là điều kiện đủ của Q”", "P ⇒ Q", "Q", "P"],
        ], widths=[48 * mm, 26 * mm, CH - 48 * mm - 26 * mm - 34 * mm, 34 * mm], fontsize=8.2),
        SP(2),
        box("example",
            [P("{b}Ví dụ.{/b} Cho định lí: “Nếu một tứ giác có hai đường chéo vuông góc và cắt nhau tại trung "
               "điểm mỗi đường thì tứ giác đó là hình thoi”.", "box_body"),
             SP(2),
             bullets([
                 "Phát biểu dạng P ⇒ Q: P = “tứ giác có hai đường chéo vuông góc và cắt nhau tại trung điểm "
                 "mỗi đường”; Q = “tứ giác là hình thoi”.",
                 "P là {b}điều kiện đủ{/b} để tứ giác là hình thoi; Q là {b}điều kiện cần{/b} để P xảy ra.",
                 "Mệnh đề đảo: “Nếu tứ giác là hình thoi thì hai đường chéo vuông góc và cắt nhau tại trung "
                 "điểm mỗi đường” – {b}đúng{/b}, nên ta có thể phát biểu “Tứ giác là hình thoi khi và chỉ khi …”.",
             ], "bullet_small")], title="VÍ DỤ MẪU – DẠNG 3"),
        SP(4),

        H3("B.1.2. Tập hợp – tập con – tập hợp bằng nhau"),
        tbl([
            ["Nội dung", "Cách viết – ghi nhớ"],
            ["Liệt kê phần tử", "A = {1; 2; 3; 5}. Mỗi phần tử viết {b}một lần{/b}, cách nhau bởi dấu “;”."],
            ["Chỉ ra tính chất đặc trưng", "A = {x ∈ ℕ | x là ước của 6} = {x ∈ ℕ : x | 6}."],
            ["Tập rỗng", "∅ – tập không có phần tử nào. {b}∅ là tập con của mọi tập hợp.{/b}"],
            ["Tập con", "A ⊂ B (A ⊆ B): mọi phần tử của A đều thuộc B. {b}∅ ⊂ A ⊂ A{/b} với mọi A. "
                        "A ⊄ B: có ít nhất một phần tử của A không thuộc B."],
            ["Hai tập bằng nhau", "A = B ⇔ A ⊂ B {b}và{/b} B ⊂ A ⇔ hai tập có đúng cùng các phần tử."],
            ["Số tập con", "Tập có n phần tử có {b}2{sup}n{/sup} tập con{/b} (kể cả ∅ và chính nó), trong đó "
                           "có 2{sup}n{/sup} − 1 tập con {b}khác rỗng{/b} và 2{sup}n{/sup} − 2 tập con thực sự."],
            ["Các tập số", "ℕ = {0; 1; 2; …}; ℕ* = {1; 2; 3; …}; ℤ = {…; −1; 0; 1; …}; "
                           "ℚ = {a/b | a, b ∈ ℤ, b ≠ 0}; ℝ. Ta có ℕ* ⊂ ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ."],
        ], widths=[38 * mm, CH - 38 * mm], fontsize=8.2),
        SP(3),
        box("note",
            [P("{b}Khoảng – đoạn – nửa khoảng (bắt buộc học thuộc):{/b}", "box_body"),
             SP(2),
             tbl([
                 ["Kí hiệu", "(a; b)", "[a; b]", "[a; b)", "(a; b]", "(−∞; a]", "[a; +∞)"],
                 ["Nghĩa là", "a < x < b", "a ≤ x ≤ b", "a ≤ x < b", "a < x ≤ b", "x ≤ a", "x ≥ a"],
                 ["Trên trục số", "bỏ cả 2 đầu", "lấy cả 2 đầu", "lấy a, bỏ b", "bỏ a, lấy b",
                  "tia trái, lấy a", "tia phải, lấy a"],
             ], widths=[24 * mm] + [(CH - 24 * mm - 18) / 6] * 6, fontsize=7.6, zebra=False),
             SP(2),
             P("Ngoài ra: (a; +∞) = {x | x > a}; (−∞; a) = {x | x < a}; (−∞; +∞) = ℝ.", "box_body")]),
        SP(4),

        *_dang(4, "Viết tập hợp, xét quan hệ tập con, đếm số tập con", "Nhận biết – Thông hiểu",
               "liệt kê đúng phần tử; dùng đúng ⊂, ⊄, ∈, ∉; tính 2ⁿ."),
        box("example",
            [P("{b}Ví dụ.{/b} Cho A = {x ∈ ℤ | −2 ≤ x < 3}. (a) Viết A bằng cách liệt kê. "
               "(b) Tập A có bao nhiêu tập con? (c) Cho B = {−2; 0; 2}. Xét quan hệ giữa B và A.", "box_body"),
             SP(2),
             P("{b}Giải.{/b} (a) Các số nguyên x thỏa −2 ≤ x < 3 là −2; −1; 0; 1; 2, nên "
               "A = {−2; −1; 0; 1; 2}.", "box_body"),
             P("(b) A có 5 phần tử ⇒ số tập con là 2{sup}5{/sup} = 32.", "box_body"),
             P("(c) Mọi phần tử của B (−2; 0; 2) đều thuộc A ⇒ {b}B ⊂ A{/b}. Ngoài ra B ≠ A nên B là tập con "
               "thực sự của A.", "box_body")], title="VÍ DỤ MẪU – DẠNG 4"),
        SP(4),

        H3("B.1.3. Các phép toán trên tập hợp"),
        tbl([
            ["Phép toán", "Định nghĩa", "Minh hoạ – lưu ý"],
            ["Giao A ∩ B", "x ∈ A ∩ B ⇔ x ∈ A {b}và{/b} x ∈ B", "Phần {b}chung{/b} của hai tập."],
            ["Hợp A ∪ B", "x ∈ A ∪ B ⇔ x ∈ A {b}hoặc{/b} x ∈ B (hoặc cả hai)",
             "Gom {b}tất cả{/b}, phần tử trùng chỉ viết một lần."],
            ["Hiệu A \\ B", "x ∈ A \\ B ⇔ x ∈ A {b}và{/b} x ∉ B", "{b}Lấy của A, bỏ của B{/b}. A \\ B ≠ B \\ A."],
            ["Phần bù C{sub}A{/sub}B", "Với B ⊂ A: C{sub}A{/sub}B = A \\ B", "Chỉ định nghĩa khi tập lớn chứa tập nhỏ."],
            ["Phần bù trong ℝ", "C{sub}ℝ{/sub}A = ℝ \\ A", "Là {b}phần còn lại{/b} của trục số khi bỏ A."],
        ], widths=[34 * mm, CH - 34 * mm - 66 * mm, 66 * mm], fontsize=8.2),
        SP(3),
        box("note",
            [P("{b}Quy tắc biểu diễn trên trục số:{/b} vẽ từng tập bằng một dòng, đánh dấu ngoặc tròn “( )” "
               "cho đầu mút {b}không lấy{/b} và ngoặc vuông “[ ]” cho đầu mút {b}lấy{/b}; tô phần chung "
               "(giao) hoặc phần gộp (hợp) rồi đọc lại kết quả.", "box_body"),
             SP(3),
             VennFig("intersection", "Hình 1. A ∩ B: phần tô đậm là phần chung"),
             SP(2),
             VennFig("union", "Hình 2. A ∪ B: phần tô là toàn bộ hai hình tròn")]),
        SP(4),

        *_dang(5, "Tìm giao, hợp, hiệu, phần bù của các khoảng – đoạn", "Thông hiểu – Vận dụng",
               "biểu diễn trên trục số và viết kết quả đúng kí hiệu."),
        numbered([
            "Vẽ trục số, biểu diễn từng tập (chú ý đầu mút lấy hay không lấy).",
            "{b}Giao{/b}: giữ phần {i}trùng{/i}. {b}Hợp{/b}: giữ {i}tất cả{/i}. {b}Hiệu A \\ B{/b}: giữ phần của A "
            "nằm {i}ngoài{/i} B.",
            "Đọc kết quả, kiểm tra lại hai đầu mút: đầu mút thuộc kết quả chỉ khi nó thuộc {b}mọi{/b} tập tham gia "
            "(với giao) hoặc thuộc {b}một{/b} tập (với hợp).",
        ]),
        box("example",
            [P("{b}Ví dụ.{/b} Cho A = [−2; 3) và B = (1; 5]. Tìm A ∩ B, A ∪ B, A \\ B, B \\ A và C{sub}ℝ{/sub}(A ∩ B).",
               "box_body"),
             SP(2),
             NumberLineFig([
                 dict(start=-2, end=3, label="A", color=PRIMARY, closed_left=True, closed_right=False),
                 dict(start=1, end=5, label="B", color=colors.HexColor("#0F5F63"),
                      closed_left=False, closed_right=True),
             ], -3, 6, caption="Hình 3. Biểu diễn A = [−2; 3) và B = (1; 5] trên trục số"),
             SP(2),
             bullets([
                 "{b}A ∩ B = (1; 3){/b}: phần trùng là từ 1 (không lấy, vì B mở tại 1) đến 3 (không lấy, vì A mở tại 3).",
                 "{b}A ∪ B = [−2; 5]{/b}: gộp lại được một đoạn liền, lấy −2 (của A) và 5 (của B).",
                 "{b}A \\ B = [−2; 1]{/b}: phần của A không nằm trong B, gồm cả điểm 1.",
                 "{b}B \\ A = [3; 5]{/b}: phần của B từ 3 đến 5, lấy cả hai đầu.",
                 "{b}C{sub}ℝ{/sub}(A ∩ B) = (−∞; 1] ∪ [3; +∞){/b}: bỏ khoảng (1; 3) khỏi trục số.",
             ], "bullet_small")], title="VÍ DỤ MẪU – DẠNG 5"),
        SP(2),
        box("warn",
            [P("Ba lỗi làm mất điểm cả câu:", "box_body"),
             bullets([
                 "Đầu mút của {b}giao{/b} phải lấy chỉ khi {i}cả hai{/i} tập đều lấy – ở ví dụ trên, 1 thuộc A "
                 "nhưng không thuộc B nên giao {b}mở{/b} tại 1.",
                 "A \\ B và B \\ A là {b}hai kết quả khác nhau{/b} – đừng viết nhầm thứ tự.",
                 "Phần bù trong ℝ của một đoạn là {b}hợp của hai tia{/b}, không phải một khoảng.",
             ], "bullet_small")]),
        SP(4),

        *_dang(6, "Bài toán thực tế dùng biểu đồ Ven (bài toán đếm)", "Vận dụng",
               "chuyển lời văn thành tập hợp, dùng công thức |A ∪ B| để tính."),
        formula("|A ∪ B| = |A| + |B| − |A ∩ B|", "Số phần tử của hợp = tổng số phần tử trừ số phần tử chung"),
        bullets([
            "“Vừa … vừa …” → phần {b}giao{/b}. “Chỉ …” → phần {b}hiệu{/b}.",
            "Số phần tử {b}không{/b} thuộc A cũng không thuộc B = |X| − |A ∪ B| (với X là tập vũ trụ).",
            "Với ba tập: |A ∪ B ∪ C| = |A| + |B| + |C| − |A ∩ B| − |B ∩ C| − |C ∩ A| + |A ∩ B ∩ C|.",
        ]),
        box("example",
            [P("{b}Ví dụ.{/b} Lớp 10A có 40 học sinh. Có 25 bạn tham gia câu lạc bộ Toán, 20 bạn tham gia câu lạc "
               "bộ Tin, trong đó 10 bạn tham gia cả hai câu lạc bộ. Hỏi có bao nhiêu bạn không tham gia câu lạc "
               "bộ nào?", "box_body"),
             SP(2),
             P("{b}Giải.{/b} Gọi A là tập học sinh tham gia CLB Toán, B là tập học sinh tham gia CLB Tin. "
               "Ta có |A| = 25, |B| = 20, |A ∩ B| = 10.", "box_body"),
             P("Số bạn tham gia ít nhất một CLB: |A ∪ B| = 25 + 20 − 10 = 35.", "box_body"),
             P("Số bạn không tham gia CLB nào: 40 − 35 = {b}5{/b} (bạn).", "box_body")],
            title="VÍ DỤ MẪU – DẠNG 6"),
        SP(2),
        box("tip",
            [P("{b}Mẹo kiểm tra:{/b} tổng “chỉ Toán” + “chỉ Tin” + “cả hai” + “không tham gia” phải bằng sĩ số "
               "lớp: 15 + 10 + 10 + 5 = 40. Nếu không khớp, bạn đã trừ/ cộng sai phần giao.", "box_body")]),
    ]
    return out


def exercises_b1() -> list:
    return [
        box("exam",
            [P("{b}Bài tập áp dụng (đáp số ở Phần E).{/b}", "box_body"),
             SP(2),
             P("{b}1.{/b} Trong các câu sau, câu nào là mệnh đề? Nêu tính đúng sai: "
               "(a) “−7 là số nguyên âm”; (b) “x² ≥ 0 với mọi x ∈ ℝ”; (c) “Giải giúp mình bài này!”; "
               "(d) “n là số chẵn”.", "box_body"),
             P("{b}2.{/b} Lập mệnh đề phủ định của: A: “∀x ∈ ℝ, x² + 2x + 3 > 0”; "
               "B: “∃n ∈ ℕ, n² + 1 chia hết cho 4”. Xét tính đúng sai của A, B.", "box_body"),
             P("{b}3.{/b} Viết tập hợp sau bằng cách liệt kê: A = {x ∈ ℕ | x² < 30}; "
               "B = {x ∈ ℤ | |x| ≤ 2}.", "box_body"),
             P("{b}4.{/b} Cho A = (−∞; 4] và B = (−3; 7). Tìm A ∩ B, A ∪ B, A \\ B, C{sub}ℝ{/sub}(A ∪ B).", "box_body"),
             P("{b}5.{/b} Lớp 10B có 45 học sinh; 30 bạn thích bóng đá, 22 bạn thích bóng rổ, 12 bạn thích cả hai. "
               "Hỏi có bao nhiêu bạn không thích môn nào trong hai môn đó?", "box_body"),
             P("{b}6.{/b} Tập hợp M = {1; 2; 3; 4; 5; 6} có bao nhiêu tập con có đúng 1 phần tử? "
               "Bao nhiêu tập con khác rỗng?", "box_body"),
            ], title="BÀI TẬP ÁP DỤNG – CHƯƠNG I"),
    ]
