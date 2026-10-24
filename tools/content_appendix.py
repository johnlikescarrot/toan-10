# -*- coding: utf-8 -*-
"""PHẦN E – Phụ lục: ma trận & đặc tả gốc, sổ tay công thức, kĩ năng phòng thi."""
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import CondPageBreak, KeepTogether, PageBreak, Table, TableStyle

from pdfkit import (
    BLUE, CONTENT_W, FONT, FONT_B, GOLD, INK, LINE, NAVY, RED, SectionBanner, TEAL,
    TINT_BLUE, TINT_GOLD, bullets, callout, data_table, note, P, S, spacing, tip, warn,
)
from reportlab.lib.styles import ParagraphStyle


def story():
    st = []
    st.append(PageBreak())
    st.append(SectionBanner("PHẦN E", "Phụ lục: ma trận – đặc tả gốc và sổ tay công thức",
                            TEAL))
    st.append(spacing(0.3))
    st.append(P(
        "Phần này tái hiện <b>nguyên văn</b> nội dung tệp <i>“MA TRẬN TOÁN 10 – GIỮA KÌ I.docx”</i> "
        "(ma trận đề và bảng đặc tả) để các em đối chiếu, đồng thời bổ sung sổ tay công thức "
        "và các kĩ năng cần thiết khi vào phòng thi."))

    st += _matrix()
    st += _spec()
    st += _formula_book()
    st += _calculator()
    st += _checklist()
    return st


# ==========================================================================
def _matrix():
    st = []
    st.append(P("E.1. Ma trận đề kiểm tra (nguyên văn)", "h2"))
    st.append(P(
        "Bảng dưới đây giữ nguyên cấu trúc và số liệu của ma trận gốc. "
        "Kí hiệu: <b>NB</b> – Nhận biết, <b>TH</b> – Thông hiểu, <b>VD</b> – Vận dụng, "
        "<b>VDC</b> – Vận dụng cao.", "small"))

    head_c = ParagraphStyle("mc", fontName=FONT_B, fontSize=6.9, leading=8.4,
                            alignment=1, textColor=colors.white)
    num = ParagraphStyle("mn", fontName=FONT, fontSize=7.4, leading=9,
                         alignment=1, textColor=INK)
    txt = ParagraphStyle("mt", fontName=FONT, fontSize=7.3, leading=9.2, textColor=INK)
    tot = ParagraphStyle("mo", fontName=FONT_B, fontSize=7.3, leading=9.2, textColor=INK)

    w_t = 0.60 * cm
    w_txt1 = 2.30 * cm
    w_txt2 = 3.10 * cm
    w_lvl = [0.60 * cm] * 12
    w_end = [0.95 * cm] * 4
    widths = [w_t, w_txt1, w_txt2] + w_lvl + w_end

    rows = [["TT", "Nội dung kiến thức", "Đơn vị kiến thức"] + [""] * 16]

    data = []
    # hàng header 1
    h1 = [P("TT", head_c), P("Nội dung<br/>kiến thức", head_c), P("Đơn vị kiến thức", head_c)]
    h1 += [P("Trắc nghiệm chọn phương án", head_c), "", ""]
    h1 += [P("Trắc nghiệm đúng – sai", head_c), "", ""]
    h1 += [P("Trả lời ngắn", head_c), "", ""]
    h1 += [P("Tự luận", head_c), "", ""]
    h1 += [P("Số câu", head_c), ""]
    h1 += [P("Điểm", head_c), ""]
    data.append(h1)
    # hàng header 2
    h2 = ["", "", ""]
    for _ in range(4):
        h2 += [P("NB", head_c), P("TH", head_c), P("VD", head_c)]
    h2 += [P("TN", head_c), P("TL", head_c), P("TN", head_c), P("TL", head_c)]
    data.append(h2)

    body = [
        ("1", "Mệnh đề. Tập hợp.", "1.1. Mệnh đề",
         [2, "", "", "", "", "", "", "", "", "", "", ""], ["2", "", "0,5", ""]),
        ("", "", "1.2. Tập hợp",
         [1, "", "", 1, 1, "", "", 1, "", "", "", ""], ["4", "", "1,25", ""]),
        ("", "", "1.3. Các phép toán trên tập hợp",
         [1, "", "", "", 1, 1, "", "", 1, 1, "", ""], ["4", "1", "1,25", "1,0"]),
        ("2", "Bất phương trình và hệ bất phương trình bậc nhất hai ẩn",
         "2.1. Bất phương trình bậc nhất hai ẩn",
         [1, "", "", 1, 2, 1, "", "", "", "", "", ""], ["5", "", "1,25", ""]),
        ("", "", "2.2. Hệ bất phương trình bậc nhất hai ẩn",
         [1, "", "", "", "", "", "", "", "", "", "", 1], ["1", "1", "0,25", "1,0"]),
        ("3", "Hệ thức lượng trong tam giác.",
         "3.1. Giá trị lượng giác của một góc từ 0° đến 180°",
         [1, 1, "", "", "", "", "", "", 1, "", "", ""], ["3", "", "1,0", ""]),
        ("", "", "3.2. Hệ thức lượng trong tam giác",
         [1, 1, "", "", "", "", "", 1, "", "", 1, ""], ["3", "1", "1,0", "1,0"]),
        ("4", "Vectơ", "4.1. Khái niệm vectơ",
         [1, 1, "", "", "", "", "", "", "", "", "", ""], ["2", "", "0,5", ""]),
    ]
    for tt, nd, dv, lv, tail in body:
        r = [P(tt, num), P(nd, txt if nd else txt), P(dv, txt)]
        r += [P(str(x) if x != "" else "", num) for x in lv]
        r += [P(tail[0], tot), P(tail[1], tot), P(tail[2], tot), P(tail[3], tot)]
        data.append(r)

    r = [P("", num), P("Tổng", tot), P("", txt)]
    r += [P(x, tot) for x in ["9", "3", "0", "2", "4", "2", "", "2", "2", "1", "1", "1"]]
    r += [P("24", tot), P("3", tot), P("7,0", tot), P("3,0", tot)]
    data.append(r)

    t = Table(data, colWidths=widths, repeatRows=2)
    cmds = [
        ("BACKGROUND", (0, 0), (-1, 1), NAVY),
        ("SPAN", (0, 0), (0, 1)), ("SPAN", (1, 0), (1, 1)), ("SPAN", (2, 0), (2, 1)),
        ("SPAN", (3, 0), (5, 0)), ("SPAN", (6, 0), (8, 0)),
        ("SPAN", (9, 0), (11, 0)), ("SPAN", (12, 0), (14, 0)),
        ("SPAN", (15, 0), (16, 0)), ("SPAN", (17, 0), (18, 0)),
        ("GRID", (0, 0), (-1, -1), 0.4, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 2.2),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2.2),
        ("TOPPADDING", (0, 0), (-1, -1), 2.6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.6),
        # tô nền các ô có số liệu
        ("BACKGROUND", (0, 2), (-1, -2), colors.white),
    ]
    # tô nhẹ nền các ô khác 0
    for ri, (tt, nd, dv, lv, tail) in enumerate(body, start=2):
        for ci, v in enumerate(lv):
            if v not in ("", 0):
                cmds.append(("BACKGROUND", (3 + ci, ri), (3 + ci, ri),
                             colors.HexColor("#EAF1F8")))
        for k, v in enumerate(tail):
            if v not in ("", "0"):
                cmds.append(("BACKGROUND", (15 + k, ri), (15 + k, ri),
                             colors.HexColor("#FBF3DF")))
    cmds.append(("BACKGROUND", (0, len(data) - 1), (-1, len(data) - 1),
                 colors.HexColor("#E4EAF1")))
    t.setStyle(TableStyle(cmds))
    st.append(t)

    st.append(P("Bảng E.1. Ma trận đề kiểm tra giữa kì I môn Toán 10 – năm học 2026–2027 "
                "(nguyên văn theo tệp gốc).", "caption"))

    st.append(spacing(0.2))
    st.append(P("E.1.1. Cách tính điểm phần trắc nghiệm đúng – sai (theo ma trận)", "h3"))
    st.append(P("Phần đúng – sai có 2 câu, mỗi câu 4 ý, tổng 2,0 điểm. Điểm của mỗi câu phụ thuộc số ý "
                "làm đúng, theo quy định ghi trong đề cương gốc:", "small"))
    st.append(data_table(
        ["Số ý đúng trong một câu", "1 ý", "2 ý", "3 ý", "4 ý"],
        [["Điểm được tính", "0,1", "0,25", "0,5", "<b>1,0</b>"],
         ["Tỉ lệ so với điểm tối đa", "10%", "25%", "50%", "100%"]],
        widths=[6.2 * cm, 2.6 * cm, 2.6 * cm, 2.6 * cm, 2.6 * cm],
        align_center_cols=[0, 1, 2, 3, 4]))
    st.append(spacing(0.1))
    st.append(note([
        P("Nhận xét quan trọng: 3 ý đúng chỉ được 0,5 điểm – <b>bằng một nửa</b> của 4 ý đúng. "
          "Vì thế hãy cố gắng xử lý <b>trọn vẹn</b> cả 4 ý của mỗi câu thay vì bỏ dở.", "small"),
        P("Tổng điểm phần này là 2,0 (2 câu × 1,0). Nếu chỉ làm đúng 2 ý ở mỗi câu, các em "
          "mất 1,5 điểm – tương đương 6 câu trắc nghiệm.", "small"),
    ], color=BLUE, bg=TINT_BLUE, title="Vì sao phải làm hết cả 4 ý?", icon="i"))

    st.append(spacing(0.15))
    st.append(tip([
        P("<b>Đọc ma trận như thế nào?</b> Mỗi dòng cho biết một đơn vị kiến thức có bao nhiêu câu ở "
          "từng mức độ và từng hình thức. Ví dụ dòng 1.3: có 1 câu trắc nghiệm chọn phương án mức NB, "
          "1 ý đúng–sai mức TH, 1 ý đúng–sai mức VD, 1 câu trả lời ngắn mức VD và 1 câu tự luận mức TH "
          "⇒ đó chính là 4 câu/ý trắc nghiệm (0,25 + 0,25 + 0,25 + 0,5 điểm) và câu 1 tự luận 1,0 điểm.",
          "small")]))
    return st


# ==========================================================================
def _spec():
    st = []
    st.append(CondPageBreak(10.2 * cm))
    st.append(P("E.2. Bảng đặc tả đề kiểm tra (nguyên văn, lược bớt câu chữ lặp)", "h2"))
    st.append(P(
        "Bảng đặc tả mô tả chi tiết <b>yêu cầu cần đạt</b> ứng với từng câu hỏi. Cột cuối cùng do tài "
        "liệu bổ sung, giúp các em biết <b>câu nào trong đề luyện tương ứng</b> với yêu cầu đó.", "small"))

    rows = [
        ("1.1. Mệnh đề",
         "<b>Nhận biết:</b> Câu 1 – biết thế nào là mệnh đề, mệnh đề phủ định, mệnh đề chứa biến. "
         "Câu 2 – biết ý nghĩa kí hiệu ∀ (với mọi) và kí hiệu ∃ (tồn tại).",
         "2", "–", "–", "–", "I.1, I.2"),
        ("1.2. Tập hợp",
         "<b>Nhận biết:</b> Câu 3 – biết cho tập hợp bằng cách liệt kê các phần tử hoặc chỉ ra tính chất "
         "đặc trưng. Câu 1a (ĐS) – sử dụng đúng các kí hiệu ∈, ∉, ⊂, ⊄ và các kí hiệu "
         "(a; b), [a; b], (a; b], [a; b), (−∞; a), (−∞; a], (a; +∞), [a; +∞), (−∞; +∞).<br/>"
         "<b>Thông hiểu:</b> Câu 1b – biểu diễn được các khoảng, đoạn trên trục số; lấy được ví dụ về "
         "tập hợp, tập hợp con, tập hợp bằng nhau. Câu 1 (TLN) – tìm số tập con của một tập hợp.",
         "1+1", "1+1", "–", "–", "I.3; II.1a, 1b; III.1"),
        ("1.3. Các phép toán trên tập hợp",
         "<b>Nhận biết:</b> Câu 4 – biết dùng biểu đồ Ven để biểu diễn giao, hợp của hai tập hợp.<br/>"
         "<b>Thông hiểu:</b> Câu 1c, Câu 1 (TL) – thực hiện được các phép toán giao, hợp, phần bù của "
         "một tập con.<br/><b>Vận dụng:</b> Câu 1d – vận dụng phép toán tập hợp; Câu 2 (TLN) – bài toán "
         "thực tế dùng các phép toán tập hợp.",
         "1", "1+1TL", "1+1", "–", "I.4; II.1c, 1d; III.2; IV.1"),
        ("2.1. Bất phương trình bậc nhất hai ẩn",
         "<b>Nhận biết:</b> Câu 5 – nhận biết bất phương trình bậc nhất hai ẩn; Câu 2a – nhận biết nghiệm "
         "và miền nghiệm của bất phương trình bậc nhất hai ẩn trên mặt phẳng toạ độ.<br/>"
         "<b>Thông hiểu:</b> Câu 2b, 2c – mô tả được miền nghiệm trên mặt phẳng toạ độ.<br/>"
         "<b>Vận dụng:</b> Câu 2d – chuyển được điều kiện của bài toán thực tế về dạng bất phương trình "
         "bậc nhất hai ẩn.",
         "1+1", "2", "1", "–", "I.5; II.2a→2d"),
        ("2.2. Hệ bất phương trình bậc nhất hai ẩn",
         "<b>Nhận biết:</b> Câu 6 – nhận biết hệ bất phương trình bậc nhất hai ẩn; nhận biết nghiệm và "
         "miền nghiệm của hệ trên mặt phẳng toạ độ.<br/>"
         "<b>Vận dụng cao:</b> Câu 3 (TL) – mô tả miền nghiệm của hệ trên mặt phẳng toạ độ, tìm giá trị "
         "tối ưu của bài toán.",
         "1", "–", "–", "1TL", "I.6; IV.3"),
        ("3.1. Giá trị lượng giác của một góc từ 0° đến 180°",
         "<b>Nhận biết:</b> Câu 7 – nhận biết giá trị lượng giác của một góc từ 0° đến 180°; nhận biết "
         "hệ thức liên hệ giữa giá trị lượng giác của các góc phụ nhau, bù nhau; tính được giá trị lượng "
         "giác bằng máy tính cầm tay.<br/><b>Thông hiểu:</b> Câu 8 – tính giá trị lượng giác của một góc "
         "khi biết một trong bốn giá trị lượng giác của nó.<br/><b>Vận dụng:</b> Câu 3 (TLN) – cho biết "
         "một giá trị lượng giác, tính giá trị của một biểu thức.",
         "1", "1", "1", "–", "I.7, I.8; III.3"),
        ("3.2. Hệ thức lượng trong tam giác",
         "<b>Nhận biết:</b> Câu 9 – nhận biết các hệ thức lượng cơ bản: định lí côsin, định lí sin, "
         "công thức tính diện tích tam giác.<br/><b>Thông hiểu:</b> Câu 10, Câu 4 (TLN) – sử dụng các "
         "hệ thức lượng để tính cạnh, góc chưa biết và diện tích, ứng dụng giải bài toán thực tiễn đơn "
         "giản.<br/><b>Vận dụng:</b> Câu 2 (TL) – giải tam giác và vận dụng vào bài toán thực tiễn "
         "(xác định khoảng cách khi gặp vật cản, chiều cao của vật khi không thể đo trực tiếp…).",
         "2", "1+1TLN", "1TL", "–", "I.9, I.10; III.4; IV.2"),
        ("4.1. Khái niệm vectơ",
         "<b>Nhận biết:</b> Câu 11 – biết các khái niệm và tính chất: vectơ, vectơ – không, độ dài vectơ, "
         "hai vectơ cùng phương, cùng hướng, hai vectơ bằng nhau; biết vectơ – không cùng phương và cùng "
         "hướng với mọi vectơ.<br/><b>Thông hiểu:</b> Câu 12 – hiểu khái niệm và đặc điểm của các vectơ, "
         "vectơ – không, độ dài vectơ, hai vectơ cùng phương, bằng nhau; chứng minh được hai vectơ bằng "
         "nhau trong một số trường hợp đơn giản.",
         "1", "1", "–", "–", "I.11, I.12"),
    ]
    data = [["Đơn vị kiến thức", "Mức độ kiến thức, kĩ năng cần kiểm tra, đánh giá",
             "NB", "TH", "VD", "VDC", "Câu tương ứng<br/>trong đề luyện"]]
    for dv, nd, nb, th, vd, vdc, cau in rows:
        data.append([dv, nd, nb, th, vd, vdc, cau])
    t = data_table(data[0], data[1:],
                   widths=[3.2 * cm, 9.2 * cm, 0.85 * cm, 0.95 * cm,
                           0.8 * cm, 0.85 * cm, 2.3 * cm],
                   align_center_cols=[2, 3, 4, 5, 6], font_size=8.0)
    st.append(t)
    st.append(P("Bảng E.2. Bảng đặc tả đề kiểm tra (tái hiện theo tệp gốc; cột cuối là phần bổ sung "
                "của tài liệu).", "caption"))

    st.append(spacing(0.1))
    st.append(P("E.2.1. Mục tiêu của đề kiểm tra (nguyên văn)", "h3"))
    st.append(P(
        "<b>Về kiến thức:</b> kiểm tra kiến thức đại số và hình học đến hết giữa học kì 1 lớp 10, gồm: "
        "Chương 1 – Mệnh đề và tập hợp; Chương 2 – Bất phương trình, hệ bất phương trình bậc nhất hai ẩn; "
        "Chương 3 – Hệ thức lượng trong tam giác; Chương 4 – Vectơ.", "small"))
    st.append(P("<b>Về kĩ năng:</b> thành thạo các dạng toán sau:", "small"))
    st.extend(bullets([
        "Mệnh đề: mệnh đề, mệnh đề phủ định, mệnh đề chứa biến, mệnh đề đảo, mệnh đề tương đương; "
        "mệnh đề chứa kí hiệu ∀, ∃; xác định điều kiện cần, điều kiện đủ, điều kiện cần và đủ; lập mệnh đề "
        "phủ định của mệnh đề có chứa ∀, ∃; xét tính đúng/sai của mệnh đề trong trường hợp đơn giản.",
        "Tập hợp và các phép toán trên tập hợp: tập con, hai tập hợp bằng nhau, tập rỗng; các kí hiệu "
        "ℕ*, ℕ, ℤ, ℚ, ℝ và các khoảng, đoạn, nửa khoảng; thực hiện các phép toán trên tập hợp.",
        "Biểu diễn miền nghiệm của bất phương trình, hệ bất phương trình bậc nhất hai ẩn trên mặt phẳng "
        "toạ độ và vận dụng vào giải quyết bài toán thực tiễn.",
        "Định nghĩa và tính giá trị lượng giác của một góc từ 0° đến 180°; mối quan hệ giữa giá trị lượng "
        "giác của hai góc bù nhau (và phụ nhau).",
        "Định lí sin, định lí côsin, công thức tính diện tích tam giác; vận dụng vào giải tam giác và "
        "các tình huống thực tế.",
        "Các khái niệm: vectơ, độ dài vectơ, giá vectơ, hai vectơ cùng phương, ngược hướng, cùng hướng, "
        "bằng nhau, đối nhau, vectơ – không.",
    ], style="bullet2", bullet="–"))
    return st


# ==========================================================================
def _formula_book():
    st = []
    st.append(CondPageBreak(10.2 * cm))
    st.append(P("E.3. Sổ tay công thức cần thuộc (1 trang ôn nhanh)", "h2"))

    # Chương 1
    st.append(P("Chương 1. Mệnh đề – Tập hợp", "h3"))
    t1 = data_table(
        ["Nội dung", "Công thức / quy tắc"],
        [["Phủ định ∀, ∃", "¬(∀x ∈ X, P(x)) ⇔ ∃x ∈ X, ¬P(x);   ¬(∃x ∈ X, P(x)) ⇔ ∀x ∈ X, ¬P(x)"],
         ["Mệnh đề kéo theo", "P ⇒ Q chỉ sai khi P đúng và Q sai"],
         ["Tương đương", "P ⇔ Q đúng khi P, Q cùng đúng hoặc cùng sai"],
         ["Số tập con", "Tập có n phần tử có 2<super>n</super> tập con (2<super>n</super> − 1 tập con khác rỗng)"],
         ["Giao – Hợp – Hiệu", "A ∩ B = {x | x ∈ A <b>và</b> x ∈ B};  A ∪ B = {x | x ∈ A <b>hoặc</b> x ∈ B};  "
                               "A \\ B = {x | x ∈ A <b>và</b> x ∉ B}"],
         ["Phần bù", "C<sub>A</sub>B = A \\ B (chỉ xác định khi B ⊂ A)"],
         ["Quan hệ bao hàm", "A ∩ B ⊂ A ⊂ A ∪ B;   ∅ ⊂ A với mọi A"],
         ["Ngoặc", "Ngoặc vuông ⇔ có dấu “=” ⇔ lấy đầu mút; ngoặc tròn ⇔ không lấy; "
                   "−∞, +∞ luôn dùng ngoặc tròn"]],
        widths=[3.6 * cm, 13.2 * cm])
    st.append(t1)

    # Chương 2
    st.append(spacing(0.08))
    st.append(P("Chương 2. Bất phương trình bậc nhất hai ẩn", "h3"))
    t2 = data_table(
        ["Nội dung", "Công thức / quy tắc"],
        [["Dạng tổng quát", "ax + by ≤ c (≥, &lt;, &gt;) với a² + b² &gt; 0"],
         ["Miền nghiệm", "Là một nửa mặt phẳng (kể cả bờ nếu có dấu “=”)"],
         ["Cách xác định", "Vẽ bờ d: ax + by = c → thử điểm M ∉ d → kết luận nửa mặt phẳng chứa/không chứa M"],
         ["Miền nghiệm của hệ", "Giao các miền nghiệm của từng bất phương trình (thường là một đa giác)"],
         ["Bài toán tối ưu", "F = ax + by đạt max, min tại các <b>đỉnh</b> của đa giác miền nghiệm"]],
        widths=[3.6 * cm, 13.2 * cm])
    st.append(t2)

    # Chương 3
    st.append(spacing(0.08))
    st.append(P("Chương 3. Hệ thức lượng trong tam giác", "h3"))
    t3 = data_table(
        ["Nội dung", "Công thức"],
        [["Hệ thức cơ bản", "sin²α + cos²α = 1;   tan α·cot α = 1;   1 + tan²α = 1/cos²α;   "
                              "1 + cot²α = 1/sin²α"],
         ["Hai góc bù nhau", "sin(180° − α) = sin α;   cos(180° − α) = −cos α;   "
                              "tan(180° − α) = −tan α;   cot(180° − α) = −cot α"],
         ["Hai góc phụ nhau", "sin(90° − α) = cos α;   cos(90° − α) = sin α;   "
                               "tan(90° − α) = cot α"],
         ["Định lí côsin", "a² = b² + c² − 2bc·cos A;   cos A = (b² + c² − a²)/(2bc)"],
         ["Định lí sin", "a/sin A = b/sin B = c/sin C = 2R"],
         ["Diện tích", "S = (1/2)ab sin C = abc/(4R) = pr = √(p(p − a)(p − b)(p − c))"],
         ["Trung tuyến", "m<sub>a</sub>² = (b² + c²)/2 − a²/4"],
         ["Tổng ba góc", "A + B + C = 180°;   a &gt; b ⇔ A &gt; B"]],
        widths=[3.6 * cm, 13.2 * cm], font_size=8.3)
    st.append(t3)

    # Chương 4
    st.append(spacing(0.08))
    st.append(P("Chương 4. Vectơ", "h3"))
    t4 = data_table(
        ["Nội dung", "Khẳng định"],
        [["Cùng phương", "Giá của hai vectơ song song hoặc trùng nhau"],
         ["Bằng nhau", "Cùng hướng <b>và</b> cùng độ dài"],
         ["Vectơ đối", "BA là vectơ đối của AB"],
         ["Vectơ – không", "Cùng phương, cùng hướng với mọi vectơ; độ dài bằng 0"],
         ["Thẳng hàng", "A, B, C thẳng hàng ⇔ AB và AC cùng phương"]],
        widths=[3.6 * cm, 13.2 * cm])
    st.append(t4)
    return st


# ==========================================================================
def _calculator():
    st = []
    st.append(CondPageBreak(10.2 * cm))
    st.append(P("E.4. Kĩ năng dùng máy tính cầm tay (Casio fx-580VN X)", "h2"))
    st.append(P(
        "Máy tính là công cụ được phép dùng, giúp tiết kiệm rất nhiều thời gian ở chương 3. "
        "Tuyệt đối không dùng máy để thay cho việc hiểu bản chất – đề có nhiều câu hỏi lí thuyết."))

    calc = data_table(
        ["Cần làm", "Thao tác", "Lưu ý"],
        [["Tính sin, cos, tan của góc α",
          "Nhập số đo góc → phím <b>sin</b> / <b>cos</b> / <b>tan</b>",
          "Kiểm tra máy đang ở chế độ <b>độ</b> (chữ D ở góc màn hình), không phải radian"],
         ["Tìm góc khi biết sin α",
          "<b>SHIFT</b> + <b>sin</b> (sin⁻¹) rồi nhập giá trị",
          "Kết quả trong khoảng 0°–180° là đúng với bài toán tam giác"],
         ["Tìm góc khi biết cos α",
          "<b>SHIFT</b> + <b>cos</b> (cos⁻¹)",
          "Máy trả về 0°–180°; nếu góc tù, kết quả vẫn đúng vì cos âm cho góc &gt; 90°"],
         ["Tính cot α",
          "Tính 1/tan α (không có phím cot)",
          "Cot không xác định khi α = 0°, 180°"],
         ["Tính √, lũy thừa",
          "Phím <b>√</b> và <b>x²</b>",
          "Với √5200, bấm √ rồi 5200 để có kết quả chính xác"],
         ["Đổi phân số ↔ số thập phân",
          "<b>S⇔D</b>",
          "Dùng để nhận ra đáp số “đẹp” như 1/2, 7/8"],
         ["Lưu kết quả trung gian",
          "<b>STO</b> + biến (A, B, C, D…)",
          "Rất hữu ích khi tính nhiều bước để tránh sai số làm tròn"]],
        widths=[3.9 * cm, 6.6 * cm, 6.6 * cm], font_size=8.2)
    st.append(calc)

    st.append(spacing(0.2))
    st.append(warn([
        P("<b>Đừng làm tròn quá sớm.</b> Hãy giữ kết quả trên máy (hoặc dùng STO) đến bước cuối rồi mới "
          "làm tròn theo yêu cầu của đề. Làm tròn ở bước giữa là nguyên nhân phổ biến khiến đáp án lệch "
          "so với đáp án đúng trong câu trả lời ngắn.", "small")]))

    st.append(spacing(0.2))
    st.append(P("Ba mẹo loại trừ đáp án khi làm trắc nghiệm", "h3"))
    st.extend(bullets([
        "<b>Loại theo dấu:</b> nếu biết cos α &lt; 0 (góc tù) thì loại ngay mọi phương án dương.",
        "<b>Loại theo đơn vị/độ lớn:</b> độ dài cạnh phải dương; cạnh lớn nhất đối diện góc lớn nhất; "
        "trong tam giác a &lt; b + c.",
        "<b>Thay số ngược:</b> với câu hỏi “cặp nào là nghiệm”, thay lần lượt từng phương án vào bất "
        "phương trình – nhanh hơn nhiều so với giải.",
    ], bullet="▸"))
    return st


# ==========================================================================
def _checklist():
    st = []
    st.append(CondPageBreak(10.2 * cm))
    st.append(P("E.5. Checklist trước khi vào phòng thi", "h2"))
    st.append(P("Hãy tự đánh dấu ✓ vào từng ô khi các em đã thực sự làm được (không nhìn tài liệu)."))

    items = [
        ("Chương 1", [
            "Phân biệt được mệnh đề và mệnh đề chứa biến",
            "Lập được phủ định của mệnh đề có ∀, ∃",
            "Phát biểu được điều kiện cần, điều kiện đủ, điều kiện cần và đủ",
            "Viết được tập hợp bằng hai cách; đếm được số tập con (2ⁿ)",
            "Nhớ chính xác 9 kí hiệu khoảng, đoạn, nửa khoảng của ℝ",
            "Tìm được giao, hợp, hiệu của hai khoảng bằng trục số",
            "Giải được bài toán thực tế bằng biểu đồ Ven",
        ]),
        ("Chương 2", [
            "Nhận diện được bất phương trình / hệ bất phương trình bậc nhất hai ẩn",
            "Kiểm tra được một cặp số có là nghiệm hay không",
            "Biểu diễn đúng miền nghiệm (nét liền/nét đứt, kể bờ hay không)",
            "Tìm được toạ độ các đỉnh của miền nghiệm",
            "Lập được hệ bất phương trình từ bài toán thực tế",
            "Tính được giá trị lớn nhất/nhỏ nhất của F = ax + by",
        ]),
        ("Chương 3", [
            "Thuộc bảng giá trị lượng giác của các góc đặc biệt",
            "Nhớ quy tắc “sin bù, cos đối dấu”",
            "Xác định đúng dấu của sin, cos, tan, cot theo khoảng của α",
            "Tính được giá trị lượng giác khi biết một giá trị (kèm xét dấu)",
            "Viết đúng định lí côsin, định lí sin, hệ quả",
            "Thuộc 5 công thức diện tích và công thức trung tuyến",
            "Giải được bài toán thực tế về khoảng cách, chiều cao",
        ]),
        ("Chương 4", [
            "Định nghĩa được vectơ, giá, độ dài, vectơ – không",
            "Phân biệt cùng phương / cùng hướng / ngược hướng",
            "Chỉ ra được hai vectơ bằng nhau, hai vectơ đối nhau",
            "Nhớ 3 tính chất đặc biệt của vectơ – không",
        ]),
    ]
    for title, lst in items:
        data = [[P(f"<b>{title}</b>", "cell_l"), P("", "cell_c")]]
        for i, it in enumerate(lst, 1):
            data.append([P(f"{i}. {it}", "cell_l"), P("☐", "cell_c")])
        t = Table(data, colWidths=[CONTENT_W - 1.6 * cm, 1.6 * cm])
        cmds = [
            ("SPAN", (0, 0), (1, 0)),
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EAF1F8")),
            ("GRID", (0, 0), (-1, -1), 0.45, LINE),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 3.4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3.4),
            ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ]
        t.setStyle(TableStyle(cmds))
        st.append(t)
        st.append(spacing(0.15))

    st.append(spacing(0.2))
    st.append(callout("Những việc cần chuẩn bị", [
        P("• Máy tính cầm tay (đã kiểm tra pin), bút bi, bút chì, thước kẻ, compa, tẩy.", "small"),
        P("• Đến sớm 15 phút; đọc kĩ <b>quy định về hiệu lệnh và cách tô phiếu trả lời</b>.", "small"),
        P("• Khi nhận đề: ghi ngay họ tên, số báo danh; rà soát đủ số trang trước khi làm.", "small"),
        P("• Làm câu dễ trước; câu khó đánh dấu để quay lại. <b>Không</b> bỏ trống ô trả lời nào.", "small"),
        P("• Dành 2 phút cuối để kiểm tra: số báo danh, các ô đã tô, đơn vị của đáp số.", "small"),
    ], color=GOLD, bg=TINT_GOLD, icon="★"))

    st.append(spacing(0.2))
    st.append(P("E.6. Tự đánh giá kết quả sau khi làm đề luyện (Phần C)", "h2"))
    st.append(callout("Thang đánh giá", [
        P("• <b>9 – 10 điểm:</b> đã sẵn sàng. Làm lại đề sau 2 ngày để kiểm tra độ ổn định.", "small"),
        P("• <b>7 – 8,5 điểm:</b> xem lại các câu sai ở Phần I (thường do bất cẩn dấu và ngoặc).", "small"),
        P("• <b>5 – 6,5 điểm:</b> học lại Phần A ở các mục tương ứng, rồi làm lại Phần B theo từng dạng.",
          "small"),
        P("• <b>Dưới 5 điểm:</b> bắt đầu lại từ Phần A.1 và A.3 (mệnh đề – tập hợp) vì đây là nền tảng "
          "chiếm tới 40% số điểm của đề.", "small"),
    ], color=NAVY, bg=TINT_BLUE, icon="★"))

    st.append(spacing(0.3))
    st.append(P("Lời nhắn cuối", "h3"))
    st.append(P("Các em thân mến, đề kiểm tra giữa học kì I không nhằm “đánh đố” mà để xác nhận rằng "
                "các em đã nắm được những viên gạch đầu tiên của chương trình Toán 10. Chỉ cần nắm chắc "
                "định nghĩa, thuộc đúng công thức và cẩn thận với dấu – ngoặc, các em hoàn toàn có thể "
                "đạt điểm cao. Hãy học theo lộ trình 7 ngày ở trang đầu, làm đề trong đúng 90 phút, "
                "và chữa lỗi một cách nghiêm túc.", "body"))
    st.append(P("Chúc các em bình tĩnh, tự tin và đạt kết quả cao nhất!", "body_c"))
    st.append(P("— HẾT TÀI LIỆU —", "caption"))
    return st
