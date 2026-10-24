# -*- coding: utf-8 -*-
"""PHẦN C – ĐỀ MẪU (27 câu) và PHẦN D – ĐÁP ÁN, LỜI GIẢI CHI TIẾT."""

from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import KeepTogether, Table, TableStyle

from pdf_kit import (
    ACCENT, ACCENT_SOFT, BORDER, CONTENT_W as CH, GREEN, GREEN_SOFT, INK, MUTED,
    PRIMARY, PRIMARY_DARK, PRIMARY_SOFT, STYLES, WHITE, H1, H2, H3, H4, P, SP, box,
    bullets, formula, numbered, tbl, FeasibleFig, HeightFig,
)


# --------------------------------------------------------------------------
# Khung đề
# --------------------------------------------------------------------------

def exam_header() -> list:
    head = Table([[
        P("{b}TRƯỜNG THPT HÀ HUY TẬP{/b}{br}TỔ TOÁN – TIN", "small"),
        P("{b}ĐỀ KIỂM TRA GIỮA HỌC KÌ I{/b}{br}NĂM HỌC 2026 – 2027{br}"
          "{i}Môn: TOÁN – Lớp 10{/i}{br}Thời gian làm bài: 90 phút (không kể thời gian phát đề)", "small"),
    ]], colWidths=[CH * 0.32, CH * 0.68])
    head.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))
    return [
        H1("PHẦN C. ĐỀ MẪU – KIỂM TRA GIỮA HỌC KÌ I"),
        P("{i}Đề luyện tập được dựng theo đúng ma trận và bảng đặc tả của Tổ Toán – Tin (24 câu trắc nghiệm, "
          "3 câu tự luận, 10 điểm, 90 phút). Đáp án và lời giải ở Phần D.{/i}", "small"),
        SP(5),
        head,
        SP(3),
        tbl([
            ["Phần", "Nội dung", "Số câu", "Điểm"],
            ["I", "Trắc nghiệm nhiều phương án lựa chọn (Câu 1 – Câu 12)", "12", "3,0"],
            ["II", "Trắc nghiệm Đúng – Sai (Câu 1 – Câu 2, mỗi câu 4 ý)", "2", "2,0"],
            ["III", "Trắc nghiệm trả lời ngắn (Câu 1 – Câu 4)", "4", "2,0"],
            ["IV", "Tự luận (Câu 1 – Câu 3)", "3", "3,0"],
        ], widths=[16 * mm, CH - 16 * mm - 20 * mm - 20 * mm, 20 * mm, 20 * mm],
            align=["c", "l", "c", "c"], fontsize=8.3),
        SP(3),
        box("exam",
            [P("{b}Hướng dẫn làm bài:{/b} Phần I khoanh tròn một chữ cái; Phần II ghi Đ hoặc S cho từng ý; "
               "Phần III điền kết quả vào chỗ trống (ghi đúng dạng: phân số, căn thức hoặc số thập phân); "
               "Phần IV trình bày lời giải vào giấy thi. Không dùng tài liệu; được dùng máy tính cầm tay "
               "không có chức năng soạn thảo.", "box_body")]),
    ]


def _q(num: str, text: str) -> P:
    return P("{b}Câu " + str(num) + ".{/b} " + text, "question")


def _opts(options, per_row: int = 2) -> Table:
    rows = []
    row = []
    for i, opt in enumerate(options):
        row.append(P("{b}" + chr(65 + i) + ".{/b} " + opt, "option"))
        if len(row) == per_row:
            rows.append(row)
            row = []
    if row:
        while len(row) < per_row:
            row.append("")
        rows.append(row)
    w = (CH - 4) / per_row
    t = Table(rows, colWidths=[w] * per_row)
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2),
        ("TOPPADDING", (0, 0), (-1, -1), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t


def part_c() -> list:
    out = exam_header()
    out += [
        SP(6),
        H2("PHẦN I. TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN (12 câu · 3,0 điểm)"),
        P("{i}Chọn một phương án đúng nhất trong mỗi câu.{/i}", "small"),
        SP(4),
    ]

    mcq = [
        ("1", "Trong các câu sau, câu nào là {b}mệnh đề{/b}?",
         ["Hôm nay là thứ mấy?", "Số 2026 chia hết cho 4.", "Hãy mở cửa sổ giúp tôi.",
          "x + 3 > 5."]),
        ("2", "Mệnh đề phủ định của mệnh đề “∀x ∈ ℝ, x² + 1 > 0” là:",
         ["∀x ∈ ℝ, x² + 1 ≤ 0", "∃x ∈ ℝ, x² + 1 ≤ 0", "∃x ∈ ℝ, x² + 1 > 0",
          "∀x ∈ ℝ, x² + 1 < 0"]),
        ("3", "Cho tập hợp A = {x ∈ ℕ | x ≤ 4 và x là số chẵn}. Tập A viết dưới dạng liệt kê là:",
         ["{0; 2; 4}", "{2; 4}", "{1; 3}", "{0; 2; 4; 6}"]),
        ("4", "Cho hai tập hợp A = {1; 2; 3; 5}, B = {2; 3; 4}. Tập A ∩ B là:",
         ["{1; 5}", "{2; 3}", "{1; 2; 3; 4; 5}", "{4}"]),
        ("5", "Bất phương trình nào sau đây là bất phương trình bậc nhất hai ẩn?",
         ["2x² + y ≥ 1", "x − 3y < 4", "x + y − z > 0", "1/x + y ≤ 3"]),
        ("6", "Điểm nào sau đây thuộc miền nghiệm của hệ bất phương trình {x + y ≤ 4; x − y ≥ 0}?",
         ["(3; 2)", "(1; 2)", "(2; 1)", "(0; 3)"]),
        ("7", "Giá trị của cos 120° bằng:",
         ["1/2", "−1/2", "√3/2", "−√3/2"]),
        ("8", "Cho sin α = 4/5 với 0° < α < 90°. Giá trị của cos α là:",
         ["3/5", "−3/5", "9/25", "1/5"]),
        ("9", "Trong tam giác ABC, định lí côsin được viết đúng là:",
         ["a² = b² + c² + 2bc·cos A", "a² = b² + c² − 2bc·cos A",
          "a² = b² + c² − bc·cos A", "a = b + c − 2bc·cos A"]),
        ("10", "Cho tam giác ABC có AB = 5, AC = 8 và góc A = 60°. Độ dài cạnh BC bằng:",
         ["7", "√129", "√39", "49"]),
        ("11", "Khẳng định nào sau đây là {b}đúng{/b}?",
         ["Hai vectơ cùng phương thì cùng hướng.",
          "Hai vectơ cùng hướng thì cùng phương.",
          "Hai vectơ có cùng độ dài thì bằng nhau.",
          "Vectơ – không không cùng phương với vectơ nào."]),
        ("12", "Cho hình bình hành ABCD. Khẳng định nào sau đây là {b}đúng{/b}?",
         ["{b}AB{/b} = {b}CD{/b}", "{b}AB{/b} = {b}DC{/b}", "{b}AD{/b} = {b}CB{/b}",
          "{b}AC{/b} = {b}BD{/b}"]),
    ]
    for num, text, opts in mcq:
        out += [_q(num, text), SP(1.5), _opts(opts), SP(4)]

    out += [
        SP(2),
        H2("PHẦN II. TRẮC NGHIỆM ĐÚNG – SAI (2 câu · 2,0 điểm)"),
        P("{i}Trong mỗi câu, ghi Đ (đúng) hoặc S (sai) cho từng ý a), b), c), d). "
          "Cách tính điểm mỗi câu: đúng 1 ý 0,1; 2 ý 0,25; 3 ý 0,5; 4 ý 1,0 điểm.{/i}", "small"),
        SP(4),
    ]

    ds1 = [
        ("a", "3 ∈ A", "Đ"),
        ("b", "A ∩ B = (2; 4)", "Đ"),
        ("c", "A ∪ B = [−1; 6)", "S"),
        ("d", "C{sub}ℝ{/sub}(A \\ B) = (−∞; −1) ∪ (2; +∞)", "Đ"),
    ]
    ds2 = [
        ("a", "Cặp số (1; 3) là một nghiệm của bất phương trình.", "Đ"),
        ("b", "Cặp số (3; 1) là một nghiệm của bất phương trình.", "S"),
        ("c", "Điểm O(0; 0) thuộc miền nghiệm của bất phương trình.", "Đ"),
        ("d", "Đường thẳng d: 2x + y = 6 cắt trục Oy tại điểm (0; 3).", "S"),
    ]

    for num, intro, items in [
        ("1", "Cho hai tập hợp A = [−1; 4) và B = (2; 6]. Xét tính đúng – sai của các mệnh đề sau:",
         ds1),
        ("2", "Cho bất phương trình 2x + y ≤ 6 có miền nghiệm (I). Xét tính đúng – sai của các "
              "khẳng định sau:", ds2),
    ]:
        rows = [["Ý", "Mệnh đề", "Đ/S"]]
        for k, text, _ in items:
            rows.append([k + ")", text, ""])
        t = tbl(rows, widths=[12 * mm, CH - 12 * mm - 22 * mm, 22 * mm], fontsize=8.6,
                align=["c", "l", "c"], zebra=False)
        out += [_q(num, intro), SP(2), t, SP(6)]

    out += [
        H2("PHẦN III. TRẮC NGHIỆM TRẢ LỜI NGẮN (4 câu · 2,0 điểm)"),
        P("{i}Điền kết quả vào chỗ trống. Chỉ ghi kết quả cuối cùng, không cần trình bày.{/i}", "small"),
        SP(4),
        _q("1", "Cho tập hợp A = {1; 2; 3; 4; 5}. Số tập con của A là ...................."),
        SP(4),
        _q("2", "Lớp 10A có 40 học sinh, trong đó có 25 bạn tham gia câu lạc bộ Toán, 20 bạn tham gia câu lạc "
                "bộ Tin và 10 bạn tham gia cả hai câu lạc bộ. Số học sinh của lớp {b}không{/b} tham gia câu lạc "
                "bộ nào là ...................."),
        SP(4),
        _q("3", "Cho sin α = 3/5 với 90° < α < 180°. Giá trị của biểu thức P = 3sin α + 4cos α "
                "là ...................."),
        SP(4),
        _q("4", "Cho tam giác ABC có AB = 4, AC = 6 và góc A = 120°. Diện tích tam giác ABC "
                "là .................... (đơn vị diện tích)"),
        SP(6),

        H2("PHẦN IV. TỰ LUẬN (3 câu · 3,0 điểm)"),
        SP(2),
        P("{b}Câu 1 (1,0 điểm).{/b} Cho hai tập hợp A = [−3; 5) và B = (1; 7]. "
          "Tìm A ∩ B, A ∪ B, A \\ B và C{sub}ℝ{/sub}B.", "question"),
        SP(3),
        P("{b}Câu 2 (1,0 điểm).{/b} Từ hai vị trí A và B cách nhau 25 m trên mặt đất, người ta đo góc nâng "
          "tới đỉnh T của một ngọn tháp: từ A được 35°, từ B được 50° (A, B và chân tháp thẳng hàng, B gần "
          "tháp hơn). Biết mắt người đo cách mặt đất 1,5 m, tính chiều cao của tháp (làm tròn đến 0,1 m).",
          "question"),
        SP(3),
        P("{b}Câu 3 (1,0 điểm).{/b} Một xưởng sản xuất hai loại sản phẩm A và B. Mỗi sản phẩm A cần 1 giờ "
          "gia công và 2 kg nguyên liệu; mỗi sản phẩm B cần 1 giờ gia công và 1 kg nguyên liệu. Xưởng có "
          "60 giờ gia công và 100 kg nguyên liệu. Lợi nhuận thu được là 3 triệu đồng cho mỗi sản phẩm A và "
          "2 triệu đồng cho mỗi sản phẩm B.", "question"),
        SP(2),
        P("{b}a){/b} Gọi x, y lần lượt là số sản phẩm A và B cần sản xuất. Viết hệ bất phương trình biểu thị "
          "các điều kiện của bài toán.", "question"),
        P("{b}b){/b} Biểu diễn miền nghiệm của hệ bất phương trình đó.", "question"),
        P("{b}c){/b} Hỏi xưởng cần sản xuất bao nhiêu sản phẩm mỗi loại để lợi nhuận lớn nhất? "
          "Tính lợi nhuận lớn nhất đó.", "question"),
        SP(6),
        P("{b}— HẾT —{/b}", "caption"),
    ]
    return out


# --------------------------------------------------------------------------
# PHẦN D – ĐÁP ÁN
# --------------------------------------------------------------------------

def _ans_block(num: str, body, kind: str = "answer"):
    return [P("{b}Câu " + str(num) + ".{/b} " + body, "answer"), SP(3)]


def part_d() -> list:
    out = [
        H1("PHẦN D. ĐÁP ÁN VÀ LỜI GIẢI CHI TIẾT"),
        P("Mỗi câu gồm: {b}đáp án{/b} (để chấm nhanh) và {b}lời giải{/b} (để hiểu vì sao). Khi tự chấm, "
          "hãy chấm theo lời giải chứ không chỉ so đáp số: một đáp số đúng nhưng lập luận sai vẫn là lỗi cần "
          "sửa trước kì thi."),
        SP(5),
        H2("D.1. Đáp án nhanh"),
        H3("Phần I – Trắc nghiệm lựa chọn"),
        tbl([
            ["Câu", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
            ["Đáp án", "B", "B", "A", "B", "B", "C", "B", "A", "B", "A", "B", "B"],
        ], widths=[22 * mm] + [(CH - 22 * mm) / 12] * 12, fontsize=8.6, zebra=False,
            align=["l"] + ["c"] * 12),
        SP(3),
        H3("Phần II – Đúng / Sai"),
        tbl([
            ["Câu", "Ý a", "Ý b", "Ý c", "Ý d", "Số ý đúng", "Điểm"],
            ["Câu 1", "Đ", "Đ", "S", "Đ", "3/4", "0,5"],
            ["Câu 2", "Đ", "S", "Đ", "S", "2/4", "0,25"],
        ], widths=[20 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm, 30 * mm, CH - 20 * mm - 72 * mm - 30 * mm],
            fontsize=8.6, align=["l", "c", "c", "c", "c", "c", "c"]),
        SP(3),
        H3("Phần III – Trả lời ngắn"),
        tbl([
            ["Câu", "1", "2", "3", "4"],
            ["Kết quả", "32", "5", "−7/5 = −1,4", "6√3 ≈ 10,39"],
        ], widths=[26 * mm] + [(CH - 26 * mm) / 4] * 4, fontsize=8.6, zebra=False,
            align=["l"] + ["c"] * 4),
        SP(3),
        H3("Phần IV – Tự luận: thang điểm"),
        tbl([
            ["Câu", "Nội dung", "Điểm"],
            ["1", "A ∩ B đúng", "0,25"],
            ["", "A ∪ B đúng", "0,25"],
            ["", "A \\ B đúng", "0,25"],
            ["", "C{sub}ℝ{/sub}B đúng", "0,25"],
            ["2", "Vẽ hình, xác định tam giác ABT và các góc (∠ATB = 25°)", "0,25"],
            ["", "Tính BT bằng định lí sin", "0,25"],
            ["", "Tính chiều cao tháp TC = BT·sin 50°", "0,25"],
            ["", "Cộng chiều cao mắt 1,5 m và kết luận ≈ 27,5 m", "0,25"],
            ["3", "Lập đúng hệ bất phương trình (kể cả x ≥ 0, y ≥ 0)", "0,25"],
            ["", "Vẽ đúng miền nghiệm (tứ giác, kể cả biên)", "0,25"],
            ["", "Lập bảng giá trị F tại các đỉnh", "0,25"],
            ["", "Kết luận đúng số lượng và lợi nhuận lớn nhất", "0,25"],
        ], widths=[14 * mm, CH - 14 * mm - 20 * mm, 20 * mm], fontsize=8.2,
            align=["c", "l", "c"]),
        SP(6),

        H2("D.2. Lời giải Phần I – Trắc nghiệm lựa chọn"),
        H3("Câu 1 – B"),
        P("{b}Giải.{/b} Mệnh đề là câu khẳng định có tính đúng hoặc sai. (A) là câu hỏi; (C) là câu cầu khiến; "
          "(D) chứa biến x chưa gán giá trị nên là mệnh đề chứa biến. Chỉ (B) là mệnh đề (và là mệnh đề "
          "{b}sai{/b}, vì 2026 = 4·506 + 2 nên không chia hết cho 4).", "answer"),
        SP(4),
        H3("Câu 2 – B"),
        P("{b}Giải.{/b} Phủ định của “∀x ∈ ℝ, P(x)” là “∃x ∈ ℝ, P̄(x)”. Ở đây P(x): “x² + 1 > 0” nên "
          "P̄(x): “x² + 1 ≤ 0”. Vậy mệnh đề phủ định là {b}∃x ∈ ℝ, x² + 1 ≤ 0{/b} (mệnh đề này sai, do đó "
          "mệnh đề gốc đúng).", "answer"),
        SP(4),
        H3("Câu 3 – A"),
        P("{b}Giải.{/b} x ∈ ℕ, x ≤ 4 và x chẵn ⇒ x ∈ {0; 2; 4}. Lưu ý: trong chương trình Kết nối tri thức, "
          "ℕ = {0; 1; 2; …} nên {b}0 được tính{/b}. Nếu quên số 0 sẽ chọn nhầm B.", "answer"),
        SP(4),
        H3("Câu 4 – B"),
        P("{b}Giải.{/b} A ∩ B gồm các phần tử {b}chung{/b}: 2 và 3 ⇒ A ∩ B = {2; 3}. "
          "(A) là A \\ B; (C) là A ∪ B.", "answer"),
        SP(4),
        H3("Câu 5 – B"),
        P("{b}Giải.{/b} Bất phương trình bậc nhất hai ẩn có dạng ax + by ≤ c (≥, <, >) với a, b không "
          "đồng thời bằng 0. (A) có x²; (C) có ba ẩn x, y, z; (D) có 1/x (không phải bậc nhất). "
          "Chỉ (B) thoả mãn: a = 1, b = −3, c = 4.", "answer"),
        SP(4),
        H3("Câu 6 – C"),
        P("{b}Giải.{/b} Thử từng điểm vào cả hai bất phương trình:", "answer"),
        tbl([
            ["Điểm", "x + y ≤ 4", "x − y ≥ 0", "Kết luận"],
            ["(3; 2)", "5 ≤ 4 sai", "1 ≥ 0 đúng", "loại"],
            ["(1; 2)", "3 ≤ 4 đúng", "−1 ≥ 0 sai", "loại"],
            ["(2; 1)", "3 ≤ 4 đúng", "1 ≥ 0 đúng", "{b}nhận{/b}"],
            ["(0; 3)", "3 ≤ 4 đúng", "−3 ≥ 0 sai", "loại"],
        ], widths=[24 * mm, 40 * mm, 40 * mm, CH - 104 * mm], fontsize=8.3,
            align=["c", "c", "c", "c"], zebra=False),
        SP(4),
        H3("Câu 7 – B"),
        P("{b}Giải.{/b} cos 120° = −cos(180° − 120°) = −cos 60° = {b}−1/2{/b}. Góc tù nên cos âm; "
          "1/2 và √3/2 là giá trị của các góc nhọn.", "answer"),
        SP(4),
        H3("Câu 8 – A"),
        P("{b}Giải.{/b} α nhọn nên cos α > 0. cos²α = 1 − sin²α = 1 − 16/25 = 9/25 ⇒ "
          "cos α = {b}3/5{/b}. (9/25 là cos²α – bẫy thường gặp.)", "answer"),
        SP(4),
        H3("Câu 9 – B"),
        P("{b}Giải.{/b} a² = b² + c² − 2bc·cos A. Nhớ: {b}a{/b} là cạnh đối diện góc {b}A{/b}, và dấu là "
          "{b}trừ{/b}.", "answer"),
        SP(4),
        H3("Câu 10 – A"),
        P("{b}Giải.{/b} BC² = AB² + AC² − 2·AB·AC·cos A = 25 + 64 − 2·5·8·(1/2) = 89 − 40 = 49 ⇒ "
          "BC = {b}7{/b}.", "answer"),
        SP(4),
        H3("Câu 11 – B"),
        P("{b}Giải.{/b} Cùng hướng ⇒ cùng phương (đúng). (A) sai vì hai vectơ cùng phương có thể {b}ngược{/b} "
          "hướng. (C) sai vì bằng nhau cần cả cùng hướng. (D) sai vì vectơ – không cùng phương với "
          "{b}mọi{/b} vectơ.", "answer"),
        SP(4),
        H3("Câu 12 – B"),
        P("{b}Giải.{/b} ABCD là hình bình hành nên AB ∥ DC và AB = DC. Đi từ A đến B cùng chiều với đi "
          "từ D đến C, nên {b}AB{/b} và {b}DC{/b} {b}cùng hướng{/b} và cùng độ dài ⇒ {b}AB{/b} = {b}DC{/b}. "
          "Ngược lại, {b}AB{/b} và {b}CD{/b} cùng độ dài nhưng {b}ngược hướng{/b} nên là hai vectơ đối nhau "
          "⇒ (A) sai. (C) sai vì {b}AD{/b} = {b}BC{/b}, không phải {b}CB{/b}. (D) sai vì hai đường chéo "
          "không song song.", "answer"),
        P("{i}Mẹo: vẽ hình, đặt mũi tên rồi so chiều – chỉ mất 5 giây và tránh được bẫy này.{/i}", "small"),
        SP(6),

        H2("D.3. Lời giải Phần II – Đúng / Sai"),
        H3("Câu 1 – Đ, Đ, S, Đ (3/4 ý đúng ⇒ 0,5 điểm)"),
        P("{b}a) Đ.{/b} A = [−1; 4) nên 3 ∈ A (vì −1 ≤ 3 < 4).", "answer"),
        P("{b}b) Đ.{/b} A ∩ B = [−1; 4) ∩ (2; 6] = (2; 4): phần chung là từ 2 (không lấy, vì B mở tại 2) "
          "đến 4 (không lấy, vì A mở tại 4).", "answer"),
        P("{b}c) S.{/b} A ∪ B = [−1; 4) ∪ (2; 6] = {b}[−1; 6]{/b}, không phải [−1; 6). Vì 6 ∈ B (B lấy 6) "
          "nên hợp phải {b}lấy{/b} 6. Đây là lỗi hay gặp nhất ở dạng này.", "answer"),
        P("{b}d) Đ.{/b} A \\ B = [−1; 2] (phần của A không nằm trong B, gồm cả điểm 2). Khi đó "
          "C{sub}ℝ{/sub}(A \\ B) = (−∞; −1) ∪ (2; +∞).", "answer"),
        SP(3),
        box("warn",
            [P("Ý c) là bài học: khi lấy {b}hợp{/b}, đầu mút nào {b}thuộc một trong hai tập{/b} thì thuộc hợp. "
               "Đừng bê nguyên dấu ngoặc của tập “trội” sang kết quả.", "box_body")]),
        SP(4),
        H3("Câu 2 – Đ, S, Đ, S (2/4 ý đúng ⇒ 0,25 điểm)"),
        P("{b}a) Đ.{/b} 2·1 + 3 = 5 ≤ 6 ⇒ (1; 3) là nghiệm.", "answer"),
        P("{b}b) S.{/b} 2·3 + 1 = 7 > 6 ⇒ (3; 1) {b}không{/b} là nghiệm.", "answer"),
        P("{b}c) Đ.{/b} 2·0 + 0 = 0 ≤ 6 ⇒ O(0; 0) thuộc miền nghiệm. Vậy miền nghiệm là nửa mặt phẳng "
          "bờ d chứa O.", "answer"),
        P("{b}d) S.{/b} Cho x = 0 ⇒ y = 6, vậy d cắt Oy tại {b}(0; 6){/b}, không phải (0; 3). "
          "(Điểm (0; 3) nằm trên d’ : 2x + y = 3.)", "answer"),
        SP(6),

        H2("D.4. Lời giải Phần III – Trả lời ngắn"),
        H3("Câu 1 – 32"),
        P("{b}Giải.{/b} A có 5 phần tử nên số tập con là 2{sup}5{/sup} = {b}32{/b} (kể cả ∅ và chính A). "
          "Nếu đề hỏi “tập con khác rỗng” thì đáp số là 31; “tập con có đúng 2 phần tử” thì dùng tổ hợp "
          "C(5,2) = 10 – đọc kĩ yêu cầu.", "answer"),
        SP(4),
        H3("Câu 2 – 5"),
        P("{b}Giải.{/b} Gọi A, B là tập học sinh tham gia CLB Toán, Tin. |A ∪ B| = 25 + 20 − 10 = 35. "
          "Số bạn không tham gia CLB nào: 40 − 35 = {b}5{/b}.", "answer"),
        SP(4),
        H3("Câu 3 – −7/5 (= −1,4)"),
        P("{b}Giải.{/b} 90° < α < 180° nên cos α < 0: cos²α = 1 − 9/25 = 16/25 ⇒ cos α = −4/5. "
          "Vậy P = 3·(3/5) + 4·(−4/5) = 9/5 − 16/5 = {b}−7/5{/b}.", "answer"),
        SP(4),
        H3("Câu 4 – 6√3 ≈ 10,39"),
        P("{b}Giải.{/b} S = ½·AB·AC·sin A = ½·4·6·sin 120° = 12·(√3/2) = {b}6√3 ≈ 10,39{/b}. "
          "Lưu ý sin 120° = sin 60° = √3/2 (không phải −√3/2).", "answer"),
        SP(6),

        H2("D.5. Lời giải Phần IV – Tự luận"),
        H3("Câu 1 (1,0 điểm) – Các phép toán trên tập hợp"),
        P("{b}Giải.{/b} Biểu diễn A = [−3; 5) và B = (1; 7] trên trục số:", "answer"),
        SP(2),
    ]
    from pdf_kit import NumberLineFig
    out += [
        NumberLineFig([
            dict(start=-3, end=5, label="A", color=PRIMARY, closed_left=True, closed_right=False),
            dict(start=1, end=7, label="B", color=colors.HexColor("#0F5F63"),
                 closed_left=False, closed_right=True),
        ], -4, 8, caption="Hình 8. A = [−3; 5) và B = (1; 7]"),
        SP(3),
        bullets([
            "{b}A ∩ B = (1; 5){/b}: phần chung, mở tại 1 (B không lấy 1) và tại 5 (A không lấy 5).",
            "{b}A ∪ B = [−3; 7]{/b}: gộp lại thành một đoạn liền, lấy −3 (của A) và 7 (của B).",
            "{b}A \\ B = [−3; 1]{/b}: phần của A nằm ngoài B, gồm cả điểm 1 (vì 1 ∉ B).",
            "{b}C{sub}ℝ{/sub}B = (−∞; 1] ∪ (7; +∞){/b}: bỏ khoảng (1; 7] khỏi trục số.",
        ]),
        SP(2),
        box("warn",
            [P("Ba điểm dễ mất điểm: (1) đầu mút 5 của A ∩ B phải {b}mở{/b}; (2) A \\ B {b}giữ{/b} điểm 1; "
               "(3) phần bù của B gồm {b}hai tia{/b} và phải {b}lấy{/b} 1 nhưng {b}không lấy{/b} 7.", "box_body")]),
        SP(6),

        H3("Câu 2 (1,0 điểm) – Chiều cao ngọn tháp"),
        P("{b}Giải.{/b} Kí hiệu C là chân tháp, T là đỉnh tháp, A và B là hai vị trí đo (A, B, C thẳng hàng, "
          "B gần tháp hơn).", "answer"),
        HeightFig(caption="Hình 9. Sơ đồ đo chiều cao tháp (bài tự luận câu 2 – minh hoạ)"),
        SP(2),
        P("{b}Bước 1.{/b} Xét tam giác ABT: ∠TAB = 35°; góc kề bù với góc nâng 50° tại B là "
          "∠ABT = 180° − 50° = 130°. Suy ra ∠ATB = 180° − 35° − 130° = {b}25°{/b}.", "answer"),
        P("{b}Bước 2.{/b} Áp dụng định lí sin trong tam giác ABT:", "answer"),
        formula("BT / sin 35° = AB / sin 25°   ⇒   BT = 25·sin 35° / sin 25° ≈ 33,94 (m)"),
        SP(2),
        P("{b}Bước 3.{/b} Trong tam giác vuông BTC (vuông tại C):", "answer"),
        formula("TC = BT·sin 50° ≈ 33,94·0,7660 ≈ 26,0 (m)"),
        SP(2),
        P("{b}Bước 4.{/b} Chiều cao tháp = TC + 1,5 ≈ 26,0 + 1,5 = {b}27,5 m{/b}.", "answer"),
        SP(2),
        P("{i}Nhận xét: dùng định lí sin trong tam giác ABT là cách gọn nhất. Nếu tính AT trước rồi "
          "TC = AT·sin 35° cũng cho cùng kết quả – cả hai đều được điểm tối đa nếu lập luận đúng.{/i}", "small"),
        SP(6),

        H3("Câu 3 (1,0 điểm) – Bài toán tối ưu"),
        P("{b}a) Lập hệ bất phương trình.{/b} Gọi x, y (sản phẩm) lần lượt là số sản phẩm A và B, "
          "x ≥ 0, y ≥ 0. Điều kiện về giờ gia công và nguyên liệu:", "answer"),
        formula(["x + y ≤ 60      (giờ gia công)", "2x + y ≤ 100      (kg nguyên liệu)",
                 "x ≥ 0,  y ≥ 0"]),
        SP(2),
        P("{b}b) Miền nghiệm{/b} là tứ giác OABC (kể cả biên) với O(0; 0), A(50; 0), B(40; 20), C(0; 60). "
          "Thật vậy: 2x + y = 100 cắt Ox tại (50; 0); x + y = 60 cắt Oy tại (0; 60); hai đường cắt nhau tại "
          "nghiệm của hệ {x + y = 60; 2x + y = 100} ⇒ x = 40, y = 20.", "answer"),
        SP(3),
        FeasibleFig(
            lines=[(1, 1, 60), (2, 1, 100), (1, 0, 0), (0, 1, 0)],
            vertices=[(0, 0), (50, 0), (40, 20), (0, 60)],
            xmax=58, ymax=68, width=250, height=205,
            caption="Hình 10. Miền nghiệm của hệ – tứ giác OABC",
            vertex_labels=["O", "A(50; 0)", "B(40; 20)", "C(0; 60)"],
        ),
        SP(3),
        P("{b}c) Tối ưu.{/b} Lợi nhuận F = 3x + 2y (triệu đồng). Vì miền nghiệm là đa giác lồi nên F đạt "
          "giá trị lớn nhất tại một đỉnh:", "answer"),
        tbl([
            ["Đỉnh", "O(0; 0)", "A(50; 0)", "B(40; 20)", "C(0; 60)"],
            ["F = 3x + 2y", "0", "150", "{b}160{/b}", "120"],
        ], widths=[40 * mm] + [(CH - 40 * mm) / 4] * 4, fontsize=8.6,
            align=["l", "c", "c", "c", "c"], zebra=False),
        SP(3),
        P("Vậy F lớn nhất bằng {b}160 triệu đồng{/b} khi {b}x = 40, y = 20{/b}: sản xuất 40 sản phẩm A và "
          "20 sản phẩm B.", "answer"),
        P("{i}Kiểm tra: 40 + 20 = 60 (hết giờ gia công); 2·40 + 20 = 100 (hết nguyên liệu). "
          "Cả hai nguồn đều dùng hết – dấu hiệu điểm tối ưu nằm ở giao điểm, đúng như kết quả.{/i}", "small"),
        SP(6),

        H2("D.6. Nhận xét sau khi chấm"),
        tbl([
            ["Mức điểm", "Ý nghĩa", "Việc cần làm"],
            ["9 – 10", "Nắm rất chắc, kể cả câu vận dụng cao.", "Duy trì: làm lại đề trong 80 phút để luyện tốc độ."],
            ["7 – 8,5", "Chắc lý thuyết, còn lỗi ở câu vận dụng hoặc trình bày.", "Xem lại D.5 câu 2–3 và cách trình bày tự luận."],
            ["5 – 6,5", "Đã nắm phần nhận biết – thông hiểu nhưng hổng kĩ năng.", "Ôn lại B.2 (miền nghiệm), B.3 (công thức tam giác), làm Phần E."],
            ["Dưới 5", "Thiếu nền tảng ở một hoặc hai chương.", "Quay lại Phần B theo chương bị mất điểm nhiều nhất; học bảng B.5 trước."],
        ], widths=[26 * mm, 62 * mm, CH - 88 * mm], fontsize=8.3, align=["c", "l", "l"]),
    ]
    return out
