# -*- coding: utf-8 -*-
"""PHẦN C – Đề luyện tập số 1 (bám đúng ma trận 24 câu/ý + 3 câu tự luận)."""
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import (
    CondPageBreak, Flowable, KeepTogether, PageBreak, Paragraph, Spacer, Table,
    TableStyle,
)

import figures
from pdfkit import (
    BLUE, CONTENT_W, GOLD, NAVY, RED, SectionBanner, TEAL, bullets, callout,
    data_table, note, P, S, spacing, tip, warn, LINE, FONT, FONT_B, INK,
)
from reportlab.lib.styles import ParagraphStyle


def options(a, b, c, d, width=CONTENT_W):
    """Bốn phương án xếp 2 cột."""
    st = ParagraphStyle("o", fontName=FONT, fontSize=9.7, leading=13.4, textColor=INK)
    data = [[P("A. " + a, "opt"), P("C. " + c, "opt")],
            [P("B. " + b, "opt"), P("D. " + d, "opt")]]
    t = Table(data, colWidths=[width / 2, width / 2])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
    ]))
    return t


def options1(a, b, c, d, width=CONTENT_W):
    """Bốn phương án xếp dọc (dùng khi phương án dài)."""
    data = [[P("A. " + a, "opt")], [P("B. " + b, "opt")],
            [P("C. " + c, "opt")], [P("D. " + d, "opt")]]
    t = Table(data, colWidths=[width])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (-1, -1), 0.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0.5),
    ]))
    return t


def q(num, text, style="q"):
    return P(f"<b>Câu {num}.</b> {text}", style)


def mcq(num, text, a, b, c, d):
    return KeepTogether([q(num, text), options(a, b, c, d)])


def mcq_fig(num, text, fig, a, b, c, d):
    return KeepTogether([q(num, text), fig, options(a, b, c, d)])


def story():
    st = []
    st.append(PageBreak())
    st.append(SectionBanner("PHẦN C", "Đề luyện tập số 1", GOLD))
    st.append(spacing(0.25))
    st.append(note([
        P("Đề được biên soạn bám <b>từng ô</b> của ma trận: 12 câu trắc nghiệm chọn phương án "
          "(9 Nhận biết + 3 Thông hiểu), 2 câu đúng – sai (8 ý: 2 NB + 4 TH + 2 VD), "
          "4 câu trả lời ngắn (2 TH + 2 VD), 3 câu tự luận (1 TH + 1 VD + 1 VDC). "
          "Các em hãy <b>bấm đồng hồ 90 phút</b> và làm nghiêm túc như thi thật.", "small")],
        color=BLUE, bg=colors.HexColor("#EAF1F8"), title="Hướng dẫn làm đề", icon="i"))

    # ---------------- tiêu đề đề ----------------
    st.append(spacing(0.3))
    c_left = ParagraphStyle("hl", fontName=FONT, fontSize=9.2, leading=12.6,
                            alignment=1, textColor=INK)
    c_right = ParagraphStyle("hr", fontName=FONT, fontSize=9.2, leading=13.2,
                             alignment=1, textColor=INK)
    head = Table([[Paragraph("TRƯỜNG THPT HÀ HUY TẬP<br/>TỔ TOÁN – TIN", c_left),
                   Paragraph("<b>ĐỀ LUYỆN TẬP SỐ 1</b><br/>"
                             "KÌ THI GIỮA HỌC KÌ I – NĂM HỌC 2026 – 2027<br/>"
                             "<b>MÔN: TOÁN – LỚP 10</b><br/>"
                             "Thời gian làm bài: 90 phút (không kể thời gian phát đề)", c_right)]],
                 colWidths=[CONTENT_W * 0.34, CONTENT_W * 0.66])
    head.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.8, NAVY),
        ("INNERGRID", (0, 0), (-1, -1), 0.8, NAVY),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    st.append(head)
    st.append(spacing(0.2))
    st.append(P("Họ và tên học sinh: ………………………………………………  Lớp: …………  "
                "Điểm: …………", "small"))
    st.append(P("(Thí sinh không được sử dụng tài liệu; được phép dùng máy tính cầm tay.)", "caption"))

    # ==================================================================
    # PHẦN I
    # ==================================================================
    st.append(spacing(0.15))
    st.append(P("PHẦN I. TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN (12 câu, 3,0 điểm)", "h3"))
    st.append(P("Chọn một phương án đúng nhất trong bốn phương án A, B, C, D.", "small"))

    st.append(mcq(1, "Trong các câu sau, câu nào <b>là mệnh đề</b>?", "x + 1 &gt; 2.", "Hôm nay trời đẹp quá!", "17 là số nguyên tố.",
                      "Bạn có thích học môn Toán không?"))

    st.append(mcq(2, "Cho mệnh đề P: “∀x ∈ ℝ, x² + x + 1 &gt; 0”. Mệnh đề phủ định của P là", "∀x ∈ ℝ, x² + x + 1 &lt; 0.", "∀x ∈ ℝ, x² + x + 1 ≤ 0.",
                      "∃x ∈ ℝ, x² + x + 1 &gt; 0.", "∃x ∈ ℝ, x² + x + 1 ≤ 0."))

    st.append(mcq(3, "Cho tập hợp A = {x ∈ ℝ | x² − 3x + 2 = 0}. Tập hợp A được viết bằng cách "
                   "liệt kê các phần tử là", "{1; −2}.", "(−1; 2).", "{1; 2}.", "{−1; −2}."))

    st.append(mcq_fig(4, "Cho hai tập hợp A và B được biểu diễn bởi biểu đồ Ven dưới đây. "
                         "Phần được <b>tô màu</b> là tập hợp nào?",
                      figures.venn_intersection(width=CONTENT_W, height=132,
                                                note=None, caption=None),
                      "A ∪ B.", "A ∩ B.", "A \\ B.", "B \\ A."))

    st.append(mcq(5, "Bất phương trình nào sau đây là <b>bất phương trình bậc nhất hai ẩn</b>?", "2x + 3y &lt; 5.", "x² + y &gt; 1.", "x + 1/y ≤ 2.", "x + y − z ≥ 0."))

    st.append(mcq(6, "Hệ bất phương trình nào sau đây là <b>hệ bất phương trình bậc nhất hai ẩn</b>?", "x + y &gt; 1 và 2x − y ≤ 3.", "x² + y ≤ 1 và x ≥ 0.",
                      "1/x + y &lt; 2 và y &gt; 0.", "x + y &gt; 1 và x − y + z &lt; 2."))

    st.append(spacing(0.1))
    st.append(mcq(7, "Cho góc α thoả mãn 90° &lt; α &lt; 180°. Khẳng định nào sau đây <b>đúng</b>?", "sin α &lt; 0.", "cos α &gt; 0.", "tan α &lt; 0.", "cot α &gt; 0."))

    st.append(mcq(8, "Cho góc α thoả mãn 90° &lt; α &lt; 180° và sin α = 3/5. Giá trị của cos α bằng", "4/5.", "−4/5.", "−5/4.", "3/4."))

    st.append(mcq(9, "Trong tam giác ABC có BC = a, CA = b, AB = c. Khẳng định nào sau đây <b>đúng</b>?", "a² = b² + c² − 2bc·cos A.", "a² = b² + c² + 2bc·cos A.",
                      "a² = b² + c² − bc·cos A.", "a² = b² + c² − 2bc·cos B."))

    st.append(mcq(10, "Cho tam giác ABC có AB = 5, AC = 8 và góc BAC = 60°. Độ dài cạnh BC bằng", "7.", "√89.", "129.", "√129."))

    st.append(mcq(11, "Khẳng định nào sau đây là <b>sai</b>?", "Vectơ – không cùng phương với mọi vectơ.",
                      "Vectơ – không cùng hướng với mọi vectơ.",
                      "Hai vectơ cùng phương thì cùng hướng.",
                      "Độ dài của vectơ – không bằng 0."))

    st.append(mcq_fig(12, "Cho hình bình hành ABCD (các đỉnh theo thứ tự A, B, C, D). "
                          "Khẳng định nào sau đây <b>đúng</b>?",
                      figures.parallelogram(width=CONTENT_W, height=136,
                                            caption="Hình 1 (dùng cho câu 12)"),
                      "AB = CD.", "AB = DC.", "AB = BC.", "AC = BD."))

    # ==================================================================
    # PHẦN II
    # ==================================================================
    st.append(spacing(0.3))
    st.append(KeepTogether([
        P("PHẦN II. TRẮC NGHIỆM ĐÚNG – SAI (2 câu, 2,0 điểm)", "h3"),
        P("Trong mỗi câu, hãy xác định mỗi ý sau là <b>Đúng (Đ)</b> hay <b>Sai (S)</b>. "
          "Cách tính điểm mỗi câu: đúng 1 ý được 0,1; đúng 2 ý được 0,25; "
          "đúng 3 ý được 0,5; đúng cả 4 ý được 1,0 điểm.", "small"),
        spacing(0.1)]))
    st.append(KeepTogether([
        q(1, "Cho hai tập hợp <b>A = (−∞; 3]</b> và <b>B = [−2; 5)</b>. Xét tính đúng sai "
            "của các mệnh đề sau:"),
        _ds_table([
        ("a)", "3 ∈ (−∞; 3)."),
        ("b)", "Trên trục số, tập hợp B được biểu diễn bởi đoạn thẳng nối hai điểm −2 và 5, "
               "trong đó điểm −2 được tô đậm (thuộc tập hợp) còn điểm 5 được để trống "
               "(không thuộc tập hợp)."),
        ("c)", "A ∩ B = (−2; 3]."),
        ("d)", "Cho C = [5; +∞). Phần bù của B trong ℝ là ℝ \\ B = (−∞; −2) ∪ [5; +∞)."),
    ])]))

    st.append(KeepTogether([
        q(2, "Cho bất phương trình <b>2x − y ≤ 3</b> (1). Xét tính đúng sai của các mệnh đề sau:"),
        _ds_table([
        ("a)", "Cặp số (1; −2) là một nghiệm của bất phương trình (1)."),
        ("b)", "Điểm O(0; 0) thuộc miền nghiệm của bất phương trình (1)."),
        ("c)", "Miền nghiệm của (1) là nửa mặt phẳng bờ d: 2x − y = 3 <b>không</b> chứa điểm O "
               "(kể cả bờ d)."),
        ("d)", "Một xưởng sản xuất x sản phẩm loại I và y sản phẩm loại II trong một ngày. Mỗi sản phẩm "
               "loại I cần 2 giờ công, mỗi sản phẩm loại II cần 1 giờ công và tổng thời gian làm việc "
               "không vượt quá 3 giờ. Điều kiện của x và y được mô tả bởi bất phương trình 2x + y ≤ 3."),
    ])]))

    # ==================================================================
    # PHẦN III
    # ==================================================================
    st.append(CondPageBreak(7.5 * cm))
    st.append(P("PHẦN III. TRẮC NGHIỆM TRẢ LỜI NGẮN (4 câu, 2,0 điểm)", "h3"))
    st.append(P("Chỉ ghi <b>đáp số</b> vào ô “Trả lời”. Không cần trình bày lời giải.", "small"))

    st.append(q(1, "Cho tập hợp A = {1; 2; 3; 4; 5}. Số tập con của tập hợp A là bao nhiêu?"))
    st.append(q(2, "Lớp 10A có 40 học sinh, trong đó có 25 học sinh tham gia câu lạc bộ Toán, "
                   "20 học sinh tham gia câu lạc bộ Tin học và 10 học sinh tham gia cả hai câu lạc bộ. "
                   "Hỏi có bao nhiêu học sinh <b>không</b> tham gia câu lạc bộ nào trong hai câu lạc bộ trên?"))
    st.append(q(3, "Cho góc α thoả mãn 90° &lt; α &lt; 180° và sin α = 3/5. Tính giá trị của biểu thức "
                   "P = 5cos α + 1."))
    st.append(q(4, "Cho tam giác ABC có AB = 5, AC = 8, BC = 7. Tính số đo góc A (theo đơn vị độ)."))
    st.append(spacing(0.1))
    st.append(_answer_grid(4))

    # ==================================================================
    # PHẦN IV
    # ==================================================================
    st.append(spacing(0.3))
    st.append(P("PHẦN IV. TỰ LUẬN (3 câu, 3,0 điểm)", "h3"))

    st.append(q(1, "<i>(1,0 điểm)</i> Cho hai tập hợp A = [−2; 3) và B = (1; 5]. "
                   "Xác định các tập hợp sau:<br/>"
                   "a) A ∩ B;    b) A ∪ B;    c) A \\ B;    d) phần bù của A trong ℝ."))

    st.append(q(2, "<i>(1,0 điểm)</i> Hai chiếc tàu thuỷ cùng xuất phát từ vị trí C, đi thẳng theo hai "
                   "hướng tạo với nhau một góc 60°. Tàu thứ nhất chạy với tốc độ 30 km/h, tàu thứ hai "
                   "chạy với tốc độ 40 km/h. Sau 2 giờ, hai tàu cách nhau bao nhiêu kilômét "
                   "(làm tròn kết quả đến hàng phần chục)?"))
    st.append(P("(Vẽ hình minh hoạ và trình bày rõ các bước tính.)", "small"))

    st.append(q(3, "<i>(1,0 điểm)</i> Một xưởng may có 100 m vải và 80 giờ công. May một chiếc áo cần "
                   "2 m vải và 1 giờ công, lãi 40 nghìn đồng một chiếc; may một chiếc quần cần 1 m vải "
                   "và 2 giờ công, lãi 30 nghìn đồng một chiếc. Hỏi xưởng cần may bao nhiêu áo và bao "
                   "nhiêu quần để tiền lãi thu được là lớn nhất? Tính số tiền lãi đó."))
    st.append(P("(Trình bày rõ việc lập hệ bất phương trình, xác định miền nghiệm và tìm phương án tối ưu.)",
                "small"))

    # ---------------- phiếu trả lời ----------------
    st.append(CondPageBreak(9.0 * cm))
    st.append(spacing(0.3))
    st.append(P("PHIẾU TRẢ LỜI CỦA HỌC SINH", "h3"))
    st.append(P("Họ và tên: ………………………………………………………………………  Lớp: ………………", "small"))
    st.append(spacing(0.15))
    st.append(_answer_sheet())
    st.append(spacing(0.25))
    st.append(data_table(
        ["Phần", "Cách ghi", "Lưu ý khi tô"],
        [["I (câu 1 – 12)", "Tô kín <b>một</b> ô tròn A, B, C hoặc D",
          "Tô đúng câu, đúng hàng; nếu tô sai phải tẩy sạch"],
         ["II (câu 1 – 2)", "Ghi chữ <b>Đ</b> hoặc <b>S</b> vào 4 dòng a, b, c, d",
          "Không bỏ trống ý nào – đúng 1 ý vẫn được 0,1 điểm"],
         ["III (câu 1 – 4)", "Ghi <b>đáp số</b> vào ô tương ứng",
          "Ghi đúng đơn vị, đúng số chữ số thập phân theo yêu cầu"],
         ["IV (câu 1 – 3)", "Trình bày lời giải vào giấy thi",
          "Ghi rõ bước, kết luận có đơn vị; không dùng bút xoá"]],
        widths=[3.0 * cm, 6.6 * cm, 7.2 * cm], align_center_cols=[0], font_size=8.4))

    st.append(spacing(0.4))
    st.append(P("———————————  HẾT  ———————————", "body_c"))
    st.append(P("Cán bộ coi thi không giải thích gì thêm.", "caption"))

    return st


def _ds_table(rows):
    """Bảng đúng – sai với cột Đ/S để trống cho học sinh điền."""
    data = [[P("<b>Ý</b>", "cell_h"), P("<b>Mệnh đề</b>", "cell_h"),
             P("<b>Đ/S</b>", "cell_h")]]
    for i, (lab, text) in enumerate(rows):
        data.append([P(lab, "cell_c"), P(text, "cell"), P("", "cell_c")])
    t = Table(data, colWidths=[1.3 * cm, CONTENT_W - 3.5 * cm, 2.2 * cm])
    cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("GRID", (0, 0), (-1, -1), 0.5, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("BACKGROUND", (2, 1), (2, -1), colors.HexColor("#F7F9FA")),
        ("TOPPADDING", (2, 1), (2, -1), 9),
        ("BOTTOMPADDING", (2, 1), (2, -1), 9),
    ]
    t.setStyle(TableStyle(cmds))
    return t


class _Bubble(Flowable):
    """Ô tròn có chữ cái bên trong (phiếu tô đáp án)."""

    def __init__(self, letter, d=15.0, color=colors.HexColor("#33414F")):
        super().__init__()
        self.letter, self.d, self.color = letter, d, color
        self.width = self.height = d + 2

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        r = self.d / 2.0
        c.setLineWidth(0.8)
        c.setStrokeColor(self.color)
        c.circle(self.width / 2.0, self.height / 2.0, r, stroke=1, fill=0)
        c.setFillColor(self.color)
        c.setFont(FONT_B, self.d * 0.52)
        c.drawCentredString(self.width / 2.0, self.height / 2.0 - self.d * 0.18,
                            self.letter)


def _answer_sheet():
    """Phiếu tô đáp án: 12 câu A–D, 2 câu Đ/S, 4 câu trả lời ngắn."""
    lab = ParagraphStyle("al", fontName=FONT, fontSize=8.0, leading=10.4,
                         alignment=1, textColor=INK)
    labb = ParagraphStyle("alb", fontName=FONT_B, fontSize=8.4, leading=11,
                          alignment=1, textColor=NAVY)
    head = ParagraphStyle("ah", fontName=FONT_B, fontSize=8.2, leading=10.6,
                          alignment=1, textColor=colors.white)
    box = ParagraphStyle("ab", fontName=FONT, fontSize=10.5, leading=13,
                         alignment=1, textColor=colors.HexColor("#9AA7B4"))

    rows = []
    for r in range(6):
        q1, q2 = r + 1, r + 7
        rows.append([Paragraph(f"<b>{q1}</b>", labb)]
                    + [_Bubble(x) for x in "ABCD"]
                    + [Paragraph("", lab), Paragraph(f"<b>{q2}</b>", labb)]
                    + [_Bubble(x) for x in "ABCD"])
    data = [[Paragraph("Câu", head), Paragraph("A", head), Paragraph("B", head),
             Paragraph("C", head), Paragraph("D", head), Paragraph("", head),
             Paragraph("Câu", head), Paragraph("A", head), Paragraph("B", head),
             Paragraph("C", head), Paragraph("D", head)]] + rows
    w0, wc = 1.30 * cm, 1.22 * cm
    widths = [w0, wc, wc, wc, wc, 0.36 * cm, w0, wc, wc, wc, wc]
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="CENTER")
    cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("GRID", (0, 0), (-1, -1), 0.45, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BACKGROUND", (5, 0), (5, -1), colors.white),
        ("LINEAFTER", (4, 0), (4, -1), 0.45, colors.white),
        ("TOPPADDING", (0, 0), (-1, -1), 3.0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.0),
        ("LEFTPADDING", (0, 0), (-1, -1), 2),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2),
        ("ALIGN", (1, 1), (4, -1), "CENTER"),
        ("ALIGN", (7, 1), (10, -1), "CENTER"),
        ("SPAN", (5, 0), (5, -1)),
        ("BACKGROUND", (0, 1), (-1, -1), colors.white),
    ]
    t.setStyle(TableStyle(cmds))
    return t


def _answer_grid(n):
    data = [[P(f"<b>Câu {i + 1}</b>", "cell_c") for i in range(n)],
            [P("", "cell_c") for _ in range(n)]]
    t = Table(data, colWidths=[CONTENT_W / n] * n)
    t.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.6, NAVY),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, LINE),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EAF1F8")),
        ("TOPPADDING", (1, 1), (-1, 1), 14),
        ("BOTTOMPADDING", (1, 1), (-1, 1), 14),
        ("TOPPADDING", (0, 0), (-1, 0), 4),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 4),
    ]))
    return t
