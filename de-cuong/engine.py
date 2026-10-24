# -*- coding: utf-8 -*-
"""Bộ dựng PDF cho đề cương ôn tập (ReportLab Platypus).

Nội dung được mô tả bằng các "block" đơn giản trong content.py, engine này
chịu trách nhiệm biến chúng thành PDF có định dạng đẹp, tiếng Việt đầy đủ.
"""
import os
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, CondPageBreak, Flowable, Frame,
                                Image, KeepTogether, PageBreak, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle)

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "assets", "fonts")

# --------------------------------------------------------------------------
# Fonts
# --------------------------------------------------------------------------
pdfmetrics.registerFont(TTFont("DJ", os.path.join(FONT_DIR, "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DJ-B", os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont("DJ-I", os.path.join(FONT_DIR, "DejaVuSans-Oblique.ttf")))
pdfmetrics.registerFont(
    TTFont("DJ-BI", os.path.join(FONT_DIR, "DejaVuSans-BoldOblique.ttf"))
)
pdfmetrics.registerFontFamily("DJ", normal="DJ", bold="DJ-B", italic="DJ-I",
                              boldItalic="DJ-BI")

# Font phụ chỉ dùng cho kí hiệu "gạch ngang trên đầu" (P̅) – DejaVu đặt dấu lệch.
_STIX = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "assets", "fonts", "STIXGeneral.ttf")
if os.path.exists(_STIX):
    pdfmetrics.registerFont(TTFont("STIX", _STIX))

# --------------------------------------------------------------------------
# Palette
# --------------------------------------------------------------------------
NAVY = colors.HexColor("#16324F")
BLUE = colors.HexColor("#1F4E79")
TEAL = colors.HexColor("#0F6E63")
ACCENT = colors.HexColor("#C0392B")
GOLD = colors.HexColor("#B7791F")
GREY = colors.HexColor("#5B6770")
LIGHT = colors.HexColor("#EDF2F8")
LIGHT2 = colors.HexColor("#F6F7F3")
CREAM = colors.HexColor("#FBF7EC")
BORDER = colors.HexColor("#C6D2E0")

BODY_SIZE = 10.2
LEAD = 15.2


def S(name, **kw):
    base = dict(fontName="DJ", fontSize=BODY_SIZE, leading=LEAD,
                textColor=colors.HexColor("#1A1A1A"), alignment=TA_JUSTIFY,
                spaceAfter=0, spaceBefore=0)
    base.update(kw)
    return ParagraphStyle(name, **base)


STY = {
    "p": S("p", spaceAfter=4.5),
    "p_lead": S("p_lead", spaceAfter=6, firstLineIndent=0),
    "small": S("small", fontSize=9, leading=12.6, textColor=GREY),
    "bullet": S("bullet", spaceAfter=3, leftIndent=12, bulletIndent=1),
    "num": S("num", spaceAfter=3, leftIndent=16, bulletIndent=1),
    "h1": S("h1", fontName="DJ-B", fontSize=16.5, leading=21, textColor=colors.white,
            alignment=TA_LEFT),
    "h2": S("h2", fontName="DJ-B", fontSize=12.6, leading=17, textColor=NAVY,
            alignment=TA_LEFT, spaceBefore=2, spaceAfter=1),
    "h3": S("h3", fontName="DJ-B", fontSize=10.8, leading=15, textColor=TEAL,
            alignment=TA_LEFT, spaceAfter=1.5),
    "box_title": S("box_title", fontName="DJ-B", fontSize=10.4, leading=14,
                   textColor=NAVY, alignment=TA_LEFT, spaceAfter=2),
    "center": S("center", alignment=TA_CENTER),
    "eq": S("eq", fontName="DJ", fontSize=10.6, leading=16, alignment=TA_CENTER,
            spaceBefore=2, spaceAfter=4),
    "q": S("q", spaceAfter=2.5),
    "opt": S("opt", fontSize=10, leading=14, alignment=TA_LEFT, spaceAfter=0),
    "sect": S("sect", fontName="DJ-B", fontSize=13.4, leading=18, textColor=colors.white,
              alignment=TA_LEFT),
    "cell": S("cell", fontSize=9.1, leading=12.4, alignment=TA_LEFT),
    "cell_c": S("cell_c", fontSize=9.1, leading=12.4, alignment=TA_CENTER),
    "cell_h": S("cell_h", fontName="DJ-B", fontSize=9.1, leading=12.4,
                textColor=colors.white, alignment=TA_CENTER),
    "answer": S("answer", spaceAfter=4, leftIndent=10, borderPadding=0),
}

# --------------------------------------------------------------------------
# Inline markup:  **bold**  *italic*  _{sub}  ^{sup}  [[highlight]]
# --------------------------------------------------------------------------
_SUB = re.compile(r"_\{([^{}]*)\}")
_SUP = re.compile(r"\^\{([^{}]*)\}")


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def mk(t):
    """Chuyển markup nội tuyến sang thẻ của ReportLab."""
    t = esc(t)
    t = t.replace("&lt;br/&gt;", "<br/>")
    t = t.replace("@P", '<font name="STIX">P\u0305</font>')
    t = t.replace("@Q", '<font name="STIX">Q\u0305</font>')
    t = _SUP.sub(r"<super>\1</super>", t)
    t = _SUB.sub(r"<sub>\1</sub>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w])__(.+?)__(?![\w])", r"<i>\1</i>", t)
    t = t.replace("\n", "<br/>")
    return t


def P(t, style="p"):
    return Paragraph(mk(t), STY[style])


# --------------------------------------------------------------------------
# Block builders
# --------------------------------------------------------------------------
def h1(text, kicker=None):
    """Dải tiêu đề lớn, nền màu."""
    rows = []
    if kicker:
        small = S("k", fontName="DJ-B", fontSize=8.6, leading=11,
                  textColor=colors.HexColor("#BBD5EA"), alignment=TA_LEFT)
        rows.append([Paragraph(mk(kicker.upper()), small)])
    rows.append([Paragraph(mk(text), STY["h1"])])
    t = Table(rows, colWidths=[16.6 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, 0), 9),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 9),
        ("TOPPADDING", (0, 1), (-1, -1), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -2), 1),
    ]))
    return [Spacer(1, 10), t, Spacer(1, 9)]


def h2(text):
    bar = Table([[""]], colWidths=[0.13 * cm], rowHeights=[0.42 * cm])
    bar.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), TEAL),
                             ("LEFTPADDING", (0, 0), (-1, -1), 0),
                             ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                             ("TOPPADDING", (0, 0), (-1, -1), 0),
                             ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    return [Spacer(1, 8),
            Table([[bar, Paragraph(mk(text), STY["h2"])]],
                  colWidths=[0.42 * cm, 16.2 * cm],
                  style=TableStyle([
                      ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                      ("LEFTPADDING", (0, 0), (-1, -1), 0),
                      ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                      ("TOPPADDING", (0, 0), (-1, -1), 1),
                      ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                      ("LINEBELOW", (1, 0), (1, 0), 0.6, BORDER),
                  ])),
            Spacer(1, 5)]


def h3(text):
    return [Spacer(1, 4), Paragraph(mk(text), STY["h3"]), Spacer(1, 1)]


def box(title, body, color=LIGHT, bar=BLUE, title_color=None):
    """Khung ghi nhớ / công thức – tách được qua nhiều trang."""
    rows = []
    if title:
        st = ParagraphStyle("bt", parent=STY["box_title"])
        if title_color is not None:
            st.textColor = title_color
        rows.append([Paragraph(mk(title), st)])
        rows.append([Spacer(1, 1.5)])
    for item in body:
        if isinstance(item, str):
            rows.append([P(item)])
        else:
            rows.append([item])
    n = len(rows)
    t = Table(rows, colWidths=[16.6 * cm], splitByRow=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, -1), color),
        ("LINEBEFORE", (0, 0), (0, -1), 2.6, bar),
        ("LINEAFTER", (0, 0), (0, -1), 0.4, BORDER),
        ("LINEABOVE", (0, 0), (-1, 0), 0.4, BORDER),
        ("LINEBELOW", (0, -1), (-1, -1), 0.4, BORDER),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 0.4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0.4),
        ("TOPPADDING", (0, 0), (-1, 0), 7),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 7),
        ("TOPPADDING", (0, 1), (-1, 1), 1.0),
    ]
    t.setStyle(TableStyle(style))
    # Khung ngắn thì giữ nguyên một khối; khung dài mới cho tách trang.
    if n <= 3:
        return [Spacer(1, 4), KeepTogether(t), Spacer(1, 7)]
    # khung dài: nếu gần cuối trang thì đẩy sang trang sau để không bị tách vụn
    return [CondPageBreak(4.2 * cm), Spacer(1, 4), t, Spacer(1, 7)]


def bullets(items, style="bullet", bullet="•"):
    out = []
    for it in items:
        if isinstance(it, str):
            out.append(Paragraph(mk(it), STY[style], bulletText=bullet))
        else:
            out.append(it)
    return out + [Spacer(1, 3)]


def nums(items):
    out = []
    for i, it in enumerate(items, 1):
        out.append(Paragraph(mk(it), STY["num"], bulletText=f"{i}."))
    return out + [Spacer(1, 3)]


def table(header, rows, widths=None, align=None, head_bg=BLUE, zebra=True,
          font_size=9.1):
    ncol = len(header) if header else len(rows[0])
    if widths is None:
        widths = [16.6 / ncol] * ncol
    total = sum(widths)
    widths = [w * 16.6 / total for w in widths]
    data = []
    if header:
        data.append([Paragraph(mk(h), STY["cell_h"]) for h in header])
    for r in rows:
        data.append([Paragraph(mk(c), STY["cell_c" if (align and align[j] == "c")
                                  else "cell"]) for j, c in enumerate(r)])
    t = Table(data, colWidths=[w * cm for w in widths],
              repeatRows=1 if header else 0)
    cmds = [
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("GRID", (0, 0), (-1, -1), 0.4, BORDER),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
    ]
    if header:
        cmds += [("BACKGROUND", (0, 0), (-1, 0), head_bg),
                 ("VALIGN", (0, 0), (-1, 0), "MIDDLE")]
    if zebra:
        start = 1 if header else 0
        for i in range(start, len(data)):
            if (i - start) % 2 == 1:
                cmds.append(("BACKGROUND", (0, i), (-1, i), LIGHT2))
    t.setStyle(TableStyle(cmds))
    return [Spacer(1, 3), t, Spacer(1, 8)]


def question(num, text, tag=None):
    """Một câu hỏi: số câu in đậm phía trước."""
    label = f"**Câu {num}.** "
    if tag:
        label += f"__({tag})__ "
    return Paragraph(mk(label + text), STY["q"])


def options(items, cols=None):
    """Bốn phương án A, B, C, D. Tự chọn 2 cột nếu các phương án ngắn."""
    letters = "ABCD"
    cells = [Paragraph(mk(f"**{letters[i]}. ** {it}"), STY["opt"])
             for i, it in enumerate(items)]
    if cols is None:
        longest = max(len(i) for i in items)
        cols = 2 if longest <= 44 else 1
    nrow = (len(cells) + cols - 1) // cols
    data = [[cells[r * cols + c] if r * cols + c < len(cells) else ""
             for c in range(cols)] for r in range(nrow)]
    if cols == 2:
        widths = [8.3 * cm, 8.3 * cm]
    else:
        widths = [16.6 * cm]
    t = Table(data, colWidths=widths)
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (0, -1), 9),
        ("LEFTPADDING", (1, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2),
        ("TOPPADDING", (0, 0), (-1, -1), 0.8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.6),
    ]))
    return [t, Spacer(1, 6)]


def tf_question(num, text, items):
    """Câu trắc nghiệm đúng – sai: items = [(nhãn, phát biểu, 'Đ'/'S')]"""
    out = [question(num, text)]
    rows = []
    for it in items:
        label, stmt = it[0], it[1]
        rows.append([Paragraph(mk(f"**{label})**"), STY["cell"]),
                     Paragraph(mk(stmt), STY["cell"])])
    t = Table(rows, colWidths=[1.0 * cm, 15.3 * cm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2),
        ("TOPPADDING", (0, 0), (-1, -1), 1.2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.4),
        ("BACKGROUND", (0, 0), (-1, -1), colors.white),
    ]))
    out += [t, Spacer(1, 6)]
    return out


def tf_answer(num, items):
    rows = [[Paragraph(mk("**" + l + ")**"), STY["cell"]),
             Paragraph(mk(s), STY["cell"]),
             Paragraph(mk("**ĐÚNG**" if a == "Đ" else "**SAI**"), STY["cell_c"])]
            for l, s, a in items]
    t = Table(rows, colWidths=[0.9 * cm, 14.2 * cm, 1.6 * cm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.35, BORDER),
        ("BACKGROUND", (0, 0), (-1, -1), colors.white),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 2.4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.4),
    ]))
    return [t, Spacer(1, 6)]


def answer_head(text):
    st = ParagraphStyle("ah", parent=STY["p"], fontName="DJ-B", textColor=TEAL,
                        spaceBefore=2, spaceAfter=2)
    return [Paragraph(mk(text), st)]


def note(text, color=GOLD):
    """Dòng ghi chú nhỏ in nghiêng."""
    st = ParagraphStyle("nt", parent=STY["small"], textColor=color)
    return [Spacer(1, 1), Paragraph(mk(text), st), Spacer(1, 3)]


def pb():
    return [PageBreak()]


def gap(h=6):
    return [Spacer(1, h)]


# --------------------------------------------------------------------------
# Cover
# --------------------------------------------------------------------------
def cover(meta):
    out = []
    out.append(Spacer(1, 0.7 * cm))

    head = S("ch", fontName="DJ-B", fontSize=12, leading=17, textColor=NAVY,
             alignment=TA_CENTER)
    out.append(Paragraph(mk(meta["school"]), head))
    out.append(Paragraph(mk(meta["group"]), S("cg", fontName="DJ", fontSize=10.8,
                                              leading=15, textColor=GREY,
                                              alignment=TA_CENTER)))
    out.append(Spacer(1, 0.35 * cm))

    rule = Table([[""]], colWidths=[16.6 * cm], rowHeights=[1.6])
    rule.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), GOLD)]))
    out.append(rule)
    out.append(Spacer(1, 1.1 * cm))

    out.append(Paragraph(mk("ĐỀ CƯƠNG ÔN TẬP"), S(
        "t1", fontName="DJ-B", fontSize=30, leading=38, textColor=NAVY,
        alignment=TA_CENTER)))
    out.append(Paragraph(mk("GIỮA HỌC KÌ I"), S(
        "t2", fontName="DJ-B", fontSize=25, leading=33, textColor=TEAL,
        alignment=TA_CENTER)))
    out.append(Spacer(1, 0.25 * cm))
    out.append(Paragraph(mk("MÔN: TOÁN – LỚP 10"), S(
        "t3", fontName="DJ-B", fontSize=16, leading=22, textColor=colors.HexColor("#1A1A1A"),
        alignment=TA_CENTER)))
    out.append(Paragraph(mk("Bộ sách KẾT NỐI TRI THỨC VỚI CUỘC SỐNG"), S(
        "t4", fontSize=11, leading=16, textColor=GREY, alignment=TA_CENTER)))
    out.append(Spacer(1, 0.9 * cm))

    inner = [
        Paragraph(mk("NĂM HỌC 2026 – 2027"), S(
            "y", fontName="DJ-B", fontSize=14, leading=20, textColor=ACCENT,
            alignment=TA_CENTER)),
        Spacer(1, 6),
        Paragraph(mk("Bám sát Ma trận – Bảng đặc tả đề kiểm tra của nhà trường"),
                  S("m1", fontSize=10.5, leading=15, textColor=GREY,
                    alignment=TA_CENTER)),
        Spacer(1, 10),
        Paragraph(mk("TÓM TẮT LÝ THUYẾT  •  PHƯƠNG PHÁP GIẢI  •  ĐỀ THAM KHẢO<br/>"
                     "ĐÁP ÁN – LỜI GIẢI CHI TIẾT 100% CÂU HỎI"), S(
            "m2", fontName="DJ-B", fontSize=10.2, leading=16, textColor=NAVY,
            alignment=TA_CENTER)),
    ]
    t = Table([[inner]], colWidths=[16.6 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CREAM),
        ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#E3D3A8")),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
    ]))
    out.append(t)
    out.append(Spacer(1, 1.5 * cm))

    # Hộp thông tin nhanh
    info = [
        [Paragraph(mk("**Thời gian làm bài**"), STY["cell"]),
         Paragraph(mk("90 phút"), STY["cell"])],
        [Paragraph(mk("**Hình thức**"), STY["cell"]),
         Paragraph(mk("12 TN nhiều lựa chọn + 2 TN đúng–sai + 4 trả lời ngắn + 3 tự luận"),
                   STY["cell"])],
        [Paragraph(mk("**Nội dung**"), STY["cell"]),
         Paragraph(mk("Chương I, II, III và Bài 1 (Vectơ) – Chương IV"), STY["cell"])],
        [Paragraph(mk("**Điểm số**"), STY["cell"]),
         Paragraph(mk("3,0 + 2,0 + 2,0 + 3,0 = 10,0 điểm"), STY["cell"])],
    ]
    t2 = Table(info, colWidths=[3.4 * cm, 12.2 * cm])
    t2.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.4, BORDER),
        ("BACKGROUND", (0, 0), (0, -1), LIGHT),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    out.append(t2)
    out.append(Spacer(1, 1.3 * cm))
    out.append(Paragraph(mk("Tài liệu lưu hành nội bộ – dùng cho học sinh ôn thi giữa học kì I"),
                        S("ft", fontSize=9, leading=13, textColor=GREY,
                          alignment=TA_CENTER)))
    return out


# --------------------------------------------------------------------------
# Document
# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
# Đánh dấu trang để dựng mục lục (build 2 lượt)
# --------------------------------------------------------------------------
class Mark(Flowable):
    def __init__(self, key, store):
        Flowable.__init__(self)
        self.key = key
        self.store = store
        self.width = 0.0
        self.height = 0.0

    def draw(self):
        try:
            self.store[self.key] = self.canv.getPageNumber() - 1
        except Exception:
            pass


def toc(entries, store):
    rows = []
    st_l = S("tl", fontSize=10.2, leading=15, alignment=TA_LEFT)
    st_n = S("tn", fontName="DJ-B", fontSize=9, leading=15, textColor=TEAL,
             alignment=TA_LEFT)
    st_p = S("tp", fontName="DJ-B", fontSize=10, leading=15, textColor=NAVY,
             alignment=TA_CENTER)
    for label, title, key in entries:
        pg = store.get(key)
        rows.append([Paragraph(mk(label), st_n),
                     Paragraph(mk(title), st_l),
                     Paragraph(str(pg) if pg else "–", st_p)])
    t = Table(rows, colWidths=[1.35 * cm, 13.45 * cm, 1.6 * cm])
    style = [
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4.2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.2),
        ("LINEBELOW", (0, 0), (-1, -2), 0.35, colors.HexColor("#DCE3EC")),
    ]
    t.setStyle(TableStyle(style))
    return [Spacer(1, 2), t, Spacer(1, 6)]


def img(path, width_cm=11.0, caption=None):
    from PIL import Image as PILImage
    w, h = PILImage.open(path).size
    iw = width_cm * cm
    ih = iw * h / w
    out = [Spacer(1, 4), Image(path, width=iw, height=ih)]
    out.append(Spacer(1, 2))
    if caption:
        st = S("cap", fontSize=8.8, leading=12.5, textColor=GREY,
               alignment=TA_CENTER)
        out.append(Paragraph(mk(caption), st))
    out.append(Spacer(1, 7))
    return out


class Doc(BaseDocTemplate):
    def __init__(self, filename, title, **kw):
        BaseDocTemplate.__init__(self, filename, pagesize=A4,
                                 leftMargin=2.0 * cm, rightMargin=2.0 * cm,
                                 topMargin=2.35 * cm, bottomMargin=1.85 * cm,
                                 title=title, author="Tổ Toán – Tin",
                                 subject="Đề cương ôn tập giữa học kì I – Toán 10",
                                 **kw)
        frame = Frame(self.leftMargin, self.bottomMargin,
                      self.width, self.height, id="body",
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id="all", frames=[frame], onPage=self._decorate),
        ])
        self.running = ""

    def _decorate(self, canv, doc):
        w, h = A4
        canv.saveState()
        if doc.page == 1:
            canv.setFillColor(NAVY)
            canv.rect(0, h - 1.15 * cm, w, 1.15 * cm, stroke=0, fill=1)
            canv.setFillColor(GOLD)
            canv.rect(0, 0, w, 0.6 * cm, stroke=0, fill=1)
            canv.restoreState()
            return
        # header
        canv.setFillColor(NAVY)
        canv.rect(0, h - 0.95 * cm, w, 0.95 * cm, stroke=0, fill=1)
        canv.setFont("DJ-B", 8.4)
        canv.setFillColor(colors.white)
        canv.drawString(2.0 * cm, h - 0.62 * cm,
                        "ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I – TOÁN 10")
        canv.setFont("DJ", 8.4)
        canv.drawRightString(w - 2.0 * cm, h - 0.62 * cm,
                             "Năm học 2026 – 2027  ·  KNTT")
        canv.setFillColor(GOLD)
        canv.rect(0, h - 1.05 * cm, w, 0.1 * cm, stroke=0, fill=1)
        # footer
        canv.setStrokeColor(BORDER)
        canv.setLineWidth(0.5)
        canv.line(2.0 * cm, 1.5 * cm, w - 2.0 * cm, 1.5 * cm)
        canv.setFont("DJ-I", 7.9)
        canv.setFillColor(GREY)
        canv.drawString(2.0 * cm, 1.1 * cm,
                        "Tổ Toán – Tin · Trường THPT Hà Huy Tập")
        canv.setFont("DJ-B", 8.2)
        canv.setFillColor(NAVY)
        canv.drawRightString(w - 2.0 * cm, 1.1 * cm, f"{doc.page - 1}")
        canv.setFont("DJ", 7.9)
        canv.setFillColor(GREY)
        canv.drawRightString(w - 2.0 * cm - 0.55 * cm, 1.1 * cm, "Trang")
        canv.restoreState()


def build(blocks, filename, title):
    """Dựng 3 lượt: (1) lấy số trang, (2) điền mục lục, (3) ổn định lại số trang."""
    store = {}
    Doc(filename, title).build(_story(blocks, store))
    Doc(filename, title).build(_story(blocks, store))
    Doc(filename, title).build(_story(blocks, store))
    return filename


def _story(blocks, store):
    story = []
    first_h1 = True
    for b in blocks:
        kind = b[0]
        if kind == "cover":
            story += cover(b[1])
            story.append(PageBreak())
            first_h1 = True
            continue
        if kind == "h1":
            # mỗi phần lớn bắt đầu trên trang mới (trừ phần đầu)
            if not first_h1:
                story.append(PageBreak())
            first_h1 = False
            if len(b) > 3:
                story.append(Mark(b[3], store))
            story += h1(b[1], b[2] if len(b) > 2 else None)
        elif kind == "h2":
            story.append(CondPageBreak(2.6 * cm))
            story += h2(b[1])
        elif kind == "h3":
            story.append(CondPageBreak(2.2 * cm))
            story += h3(b[1])
        elif kind == "p":
            story.append(P(b[1]))
        elif kind == "lead":
            story.append(P(b[1], "p_lead"))
        elif kind == "small":
            story.append(P(b[1], "small"))
        elif kind == "eq":
            story.append(P(b[1], "eq"))
        elif kind == "bullet":
            story += bullets(b[1])
        elif kind == "bullets":
            story += bullets(b[1])
        elif kind == "nums":
            story += nums(b[1])
        elif kind == "num":
            story += nums(b[1])
        elif kind == "box":
            story += box(b[1], b[2], *(b[3:]))
        elif kind == "table":
            story += table(b[1], b[2], b[3] if len(b) > 3 else None,
                           b[4] if len(b) > 4 else None)
        elif kind == "q":
            story.append(question(b[1], b[2], b[3] if len(b) > 3 else None))
        elif kind == "opts":
            story += options(b[1], b[2] if len(b) > 2 else None)
        elif kind == "tf":
            story += tf_question(b[1], b[2], b[3])
        elif kind == "tfa":
            story += tf_answer(b[1], b[2])
        elif kind == "ah":
            story += answer_head(b[1])
        elif kind == "note":
            story += note(b[1])
        elif kind == "gap":
            story += gap(b[1] if len(b) > 1 else 6)
        elif kind == "pb":
            story.append(PageBreak())
        elif kind == "keep":
            story.append(KeepTogether(b[1]))
        elif kind == "toc":
            story += toc(b[1], store)
        elif kind == "mark":
            story.append(Mark(b[1], store))
        elif kind == "img":
            story += img(b[1], b[2] if len(b) > 2 else 11.0,
                         b[3] if len(b) > 3 else None)
        else:
            raise ValueError(f"Unknown block: {kind}")
    return story
