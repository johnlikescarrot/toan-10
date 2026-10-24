# -*- coding: utf-8 -*-
"""Khung dựng PDF cho Đề cương ôn tập Toán 10 (ReportLab).

- Font: Noto Sans (tiếng Việt) + DejaVu Sans (ký hiệu toán không có trong Noto).
- Cú pháp soạn thảo (xem inline()):
    $...$      : đoạn công thức -> chữ nghiêng
    ^x / ^{...}: chỉ số trên (mũ)
    _x / _{...}: chỉ số dưới
    \\v{AB}    : vectơ (in đậm)
"""
import os
import re

from fontTools.ttLib import TTFont
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import paraparser as _pp

_pp.supFraction = 0.34
_pp.subFraction = 0.34
from reportlab.pdfbase.ttfonts import TTFont as RLTTFont
from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether, PageBreak,
                                PageTemplate, Paragraph, Spacer, Table, TableStyle)
from reportlab.platypus.tableofcontents import TableOfContents

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = os.path.join(HERE, "assets", "fonts")

# ----------------------------------------------------------------- font setup
NAVY = colors.HexColor("#12395B")
TEAL = colors.HexColor("#0E6E6E")
ACCENT = colors.HexColor("#B4560F")
INK = colors.HexColor("#1A1A1A")
GREY = colors.HexColor("#5B6770")
LIGHT = colors.HexColor("#F2F6F9")
LIGHT2 = colors.HexColor("#FBF4E9")
LIGHT3 = colors.HexColor("#EFF8F3")
RULE = colors.HexColor("#C9D6DF")

MATH_FONT = "DejaVu"


def _register():
    reg = {
        "Noto": ("NotoSans-Regular.ttf", None),
        "Noto-Bold": ("NotoSans-Bold.ttf", None),
        "Noto-Italic": ("NotoSans-Italic.ttf", None),
        "Noto-BoldItalic": ("NotoSans-BoldItalic.ttf", None),
        "NotoSerif": ("NotoSerif-Regular.ttf", None),
        "NotoSerif-Bold": ("NotoSerif-Bold.ttf", None),
        "DejaVu": ("DejaVuSans.ttf", None),
        "DejaVu-Bold": ("DejaVuSans-Bold.ttf", None),
    }
    for name, (fn, _) in reg.items():
        pdfmetrics.registerFont(RLTTFont(name, os.path.join(FONT_DIR, fn)))
    pdfmetrics.registerFontFamily(
        "Noto", normal="Noto", bold="Noto-Bold", italic="Noto-Italic",
        boldItalic="Noto-BoldItalic")
    pdfmetrics.registerFontFamily(
        "NotoSerif", normal="NotoSerif", bold="NotoSerif-Bold",
        italic="NotoSerif", boldItalic="NotoSerif-Bold")
    pdfmetrics.registerFontFamily(
        "DejaVu", normal="DejaVu", bold="DejaVu-Bold", italic="DejaVu",
        boldItalic="DejaVu-Bold")


_register()

_COVERED = None


def _covered():
    global _COVERED
    if _COVERED is None:
        t = TTFont(os.path.join(FONT_DIR, "NotoSans-Regular.ttf"))
        s = set()
        for tb in t["cmap"].tables:
            s |= set(tb.cmap)
        _COVERED = s
    return _COVERED


def _sym(text):
    """Bọc các ký hiệu Noto không có bằng font DejaVu (chỉ xét ký tự > 127)."""
    cov = _covered()
    out, buf, mode = [], [], None
    for ch in text:
        need = ord(ch) > 127 and ord(ch) not in cov
        if need != mode:
            if buf:
                seg = "".join(buf)
                out.append(seg if not mode else '<font name="DejaVu">%s</font>' % seg)
            buf, mode = [], need
        buf.append(ch)
    if buf:
        seg = "".join(buf)
        out.append(seg if not mode else '<font name="DejaVu">%s</font>' % seg)
    return "".join(out)


_TAG = re.compile(r"(<[^<>]*>)")
_MATH = re.compile(r"\$(.+?)\$", re.S)


_BOLD = re.compile(r"\*\*(.+?)\*\*", re.S)


def inline(s):
    """Chuyển chuỗi soạn thảo thành markup, an toàn với các thẻ đã có."""
    s = _BOLD.sub(r"<b>\1</b>", s)
    parts = []
    for seg in _MATH.split(s):
        parts.append(seg)
    # _MATH.split trả về xen kẽ: text, math, text, ... (math ở vị trí lẻ)
    res = []
    for idx, seg in enumerate(parts):
        if idx % 2 == 1:
            res.append("<i>" + _math_body(seg) + "</i>")
        elif idx % 2 == 0 and idx > 0 and idx < len(parts) - 1 and seg.strip() == "":
            # khoảng trắng giữa hai công thức -> nới rộng cho dễ đọc
            res.append("\u2003" * max(2, min(4, len(seg) // 2)))
        else:
            for piece in _TAG.split(seg):
                if piece.startswith("<") and piece.endswith(">"):
                    res.append(piece)
                else:
                    res.append(_sym(piece))
    return "".join(res)


def _math_body(s):
    # --- xử lí lệnh soạn thảo
    for a, b in ((r"\;", " "), (r"\,", " "), (r"\:", " "),
                 (r"\!", ""), (r"\ ", " ")):
        s = s.replace(a, b)
    s = s.replace(r"\overline{", "\x02")
    s = s.replace(r"\v{", "\x01")
    s = s.replace(r"\widehat{", "\x03")
    # đổi các lệnh LaTeX thông dụng sang kí hiệu Unicode
    for k in sorted(_CMD, key=len, reverse=True):
        s = s.replace("\\" + k, _CMD[k])
    s = s.replace("\\", "")          # bỏ các dấu \ còn lại

    out, buf, i = [], [], 0
    while i < len(s):
        ch = s[i]
        if ch in "\x01\x02\x03":     # vectơ / gạch trên / dấu mũ
            j = s.index("}", i)
            arg = s[i + 1:j]
            out.append("".join(buf)); buf = []
            if ch == "\x01":
                out.append("<b>%s</b>" % _sym(arg))
            elif ch == "\x02":
                out.append(_sym(arg + "\u0305"))
            else:
                out.append(_sym(arg + "\u0302"))
            i = j + 1
            continue
        if ch in "^_":
            tag = "super" if ch == "^" else "sub"
            i += 1
            if i < len(s) and s[i] in "{(":
                close = "}" if s[i] == "{" else ")"
                j = s.index(close, i)
                arg, i = s[i + 1:j], j + 1
            else:
                arg, i = (s[i] if i < len(s) else ""), i + 1
            buf.append('<%s size="6.6">%s</%s>' % (tag, _sym(arg), tag))
            continue
        buf.append(ch)
        i += 1
    out.append("".join(buf))
    return _sym("".join(out))


_CMD = {
    "cup": "∪", "cap": "∩", "setminus": "∖", "subset": "⊂", "subseteq": "⊆",
    "supset": "⊃", "in": "∈", "notin": "∉", "emptyset": "∅", "varnothing": "∅",
    "forall": "∀", "exists": "∃", "Rightarrow": "⇒", "Leftrightarrow": "⇔",
    "rightarrow": "→", "to": "→", "leftarrow": "←", "mapsto": "↦",
    "le": "≤", "leq": "≤", "ge": "≥", "geq": "≥", "ne": "≠", "neq": "≠",
    "pm": "±", "mp": "∓", "times": "×", "cdot": "·", "div": "÷",
    "infty": "∞", "sqrt": "√", "approx": "≈", "equiv": "≡", "sim": "∼",
    "angle": "∠", "perp": "⊥", "parallel": "∥", "degree": "°",
    "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "Delta": "Δ",
    "theta": "θ", "lambda": "λ", "mu": "μ", "pi": "π", "rho": "ρ",
    "sigma": "σ", "varphi": "φ", "omega": "ω", "Omega": "Ω",
    "R": "ℝ", "N": "ℕ", "Z": "ℤ", "Q": "ℚ",
    "Leftarrow": "⇐", "iff": "⇔", "dots": "…",
}

# --------------------------------------------------------------------- styles
def _p(name, **kw):
    base = dict(fontName="Noto", fontSize=10, leading=15.2, textColor=INK,
                alignment=TA_JUSTIFY, spaceBefore=0, spaceAfter=0)
    base.update(kw)
    return ParagraphStyle(name, **base)


S = {
    "body": _p("body", spaceAfter=4.5),
    "body_tight": _p("body_tight", spaceAfter=2),
    "lead": _p("lead", fontSize=10.5, leading=16.5, textColor=NAVY),
    "h1": _p("h1", fontName="Noto-Bold", fontSize=17, leading=22, textColor=colors.white,
             alignment=TA_LEFT, spaceBefore=0, spaceAfter=0),
    "h1_num": _p("h1_num", fontName="Noto-Bold", fontSize=23, leading=27,
                 textColor=colors.white, alignment=TA_LEFT),
    "h2": _p("h2", keepWithNext=1,  fontName="Noto-Bold", fontSize=12.6, leading=17, textColor=NAVY,
             alignment=TA_LEFT, spaceBefore=13, spaceAfter=5),
    "h3": _p("h3", keepWithNext=1,  fontName="Noto-Bold", fontSize=10.8, leading=15, textColor=TEAL,
             alignment=TA_LEFT, spaceBefore=9, spaceAfter=3),
    "h4": _p("h4", keepWithNext=1,  fontName="Noto-BoldItalic", fontSize=10, leading=14, textColor=ACCENT,
             alignment=TA_LEFT, spaceBefore=7, spaceAfter=2.5),
    "bullet": _p("bullet", leftIndent=11, bulletIndent=2, spaceAfter=2.6),
    "bullet2": _p("bullet2", leftIndent=24, bulletIndent=15, spaceAfter=2.2, fontSize=9.6, leading=14.4),
    "box": _p("box", fontSize=9.8, leading=14.6, backColor=LIGHT, borderColor=RULE,
              borderWidth=0.6, borderPadding=(6, 7, 6, 7), spaceBefore=5, spaceAfter=7),
    "box_warn": _p("box_warn", fontSize=9.8, leading=14.6, backColor=LIGHT2,
                   borderColor=colors.HexColor("#E2C08B"), borderWidth=0.6,
                   borderPadding=(6, 7, 6, 7), spaceBefore=5, spaceAfter=7),
    "box_tip": _p("box_tip", fontSize=9.8, leading=14.6, backColor=LIGHT3,
                  borderColor=colors.HexColor("#A9CFBB"), borderWidth=0.6,
                  borderPadding=(6, 7, 6, 7), spaceBefore=5, spaceAfter=7),
    "formula": _p("formula", fontName="NotoSerif", fontSize=10.4, leading=16,
                  alignment=TA_CENTER, textColor=NAVY, spaceBefore=4, spaceAfter=5),
    "q": _p("q", spaceAfter=4.5),
    "opt": _p("opt", fontSize=9.7, leading=14, spaceAfter=1.2, leftIndent=6),
    "small": _p("small", fontSize=8.4, leading=11.6, textColor=GREY),
    "center": _p("center", alignment=TA_CENTER),
    "right": _p("right", alignment=TA_RIGHT),
    "th": _p("th", fontName="Noto-Bold", fontSize=8.4, leading=11, alignment=TA_CENTER,
             textColor=colors.white),
    "td": _p("td", fontSize=8.5, leading=11.4, alignment=TA_LEFT),
    "tdc": _p("tdc", fontSize=8.5, leading=11.4, alignment=TA_CENTER),
    "cover_t": _p("cover_t", fontName="Noto-Bold", fontSize=30, leading=37,
                  textColor=NAVY, alignment=TA_CENTER),
    "cover_s": _p("cover_s", fontSize=12.5, leading=19, textColor=TEAL, alignment=TA_CENTER),
}


def P(text, style="body"):
    return Paragraph(inline(text), S[style])


def formula(text):
    return Paragraph(inline(text), S["formula"])


def B(text, style="bullet", mark="•"):
    return Paragraph(inline(text), S[style], bulletText=mark)


def box(text, kind="box", title=None):
    st = dict(S[kind].__dict__)
    content = []
    if title:
        content.append(Paragraph(
            inline("<b>%s</b>" % title),
            _p("boxt", fontName="Noto-Bold", fontSize=9.8, leading=14,
               textColor=NAVY if kind != "box_warn" else ACCENT, spaceAfter=2.5)))
    if isinstance(text, list):
        body = [P(t) if isinstance(t, str) else t for t in text]
    else:
        body = [P(text)]
    st2 = ParagraphStyle("boxbody_" + kind, parent=S[kind])
    st2.backColor = None
    st2.borderWidth = 0
    st2.borderPadding = 0
    st2.spaceBefore = 0
    st2.spaceAfter = 0
    content.extend(body)
    t = Table([[content]], colWidths=[None])
    bg = {"box": LIGHT, "box_warn": LIGHT2, "box_tip": LIGHT3}[kind]
    bd = {"box": RULE, "box_warn": colors.HexColor("#E2C08B"),
          "box_tip": colors.HexColor("#A9CFBB")}[kind]
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("BOX", (0, 0), (-1, -1), 0.7, bd),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return [Spacer(1, 3), t, Spacer(1, 8)]


def rule(color=RULE, w=0.7, space=6):
    t = Table([[""]], colWidths=["100%"], rowHeights=[0.1])
    t.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, -1), w, color)]))
    return [Spacer(1, space), t, Spacer(1, space)]


def data_table(rows, widths=None, header=True, align_center=True, fs=8.5):
    """rows: list of list (chuỗi soạn thảo)."""
    data = []
    for r_i, row in enumerate(rows):
        cells = []
        for c in row:
            if isinstance(c, (Paragraph, Table)):
                cells.append(c)
            else:
                st = "th" if (header and r_i == 0) else ("tdc" if align_center else "td")
                if header and r_i == 0:
                    cells.append(Paragraph(inline(c), S["th"]))
                else:
                    cells.append(Paragraph(inline(c), S["td"] if not align_center else S["tdc"]))
        data.append(cells)
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0, hAlign="CENTER")
    style = [
        ("GRID", (0, 0), (-1, -1), 0.5, RULE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3.0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.0),
    ]
    if header:
        style += [("BACKGROUND", (0, 0), (-1, 0), NAVY)]
        for i in range(1, len(data)):
            if i % 2 == 0:
                style.append(("BACKGROUND", (0, i), (-1, i), LIGHT))
    t.setStyle(TableStyle(style))
    return t


class ChapterBand(Table):
    """Dải tiêu đề chương (Table để canh cột, có .title cho mục lục)."""

    def __init__(self, number, title, subtitle=None):
        self.title = title
        self.toc_text = (number + ". " if number else "") + title
        left = [Paragraph(number, S["h1_num"])] if number else [Spacer(1, 1)]
        right = [Paragraph(inline(title), S["h1"])]
        if subtitle:
            right.append(Paragraph(inline(subtitle),
                                   _p("h1s", fontSize=9.2, leading=13,
                                      textColor=colors.HexColor("#BFD4E4"))))
        Table.__init__(self, [[left, right]], colWidths=[20 * mm, None])
        self.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), NAVY),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 9),
            ("RIGHTPADDING", (0, 0), (-1, -1), 10),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ]))
        self.spaceBefore = 2
        self.spaceAfter = 9


def h1(number, title, subtitle=None):
    return [ChapterBand(number, title, subtitle), Spacer(1, 9)]


def h1_raw(number, title, subtitle=None):
    return ChapterBand(number, title, subtitle)


def h2(text):
    return Paragraph(inline(text), S["h2"])


def h2x(text):
    """Tiêu đề mục cấp 2 nhưng KHÔNG đưa vào mục lục/dấu trang."""
    st = _p("h2x", fontName="Noto-Bold", fontSize=11.6, leading=16, textColor=NAVY,
            alignment=TA_LEFT, spaceBefore=12, spaceAfter=5, keepWithNext=1)
    return Paragraph(inline(text), st)


def h3(text):
    return Paragraph(inline(text), S["h3"])


def h4(text):
    return Paragraph(inline(text), S["h4"])


# --------------------------------------------------------------------- template
PAGE_W, PAGE_H = A4
LM, RM, TM, BM = 18 * mm, 16 * mm, 20 * mm, 17 * mm


class Doc(BaseDocTemplate):
    def __init__(self, filename, **kw):
        BaseDocTemplate.__init__(self, filename, pagesize=A4,
                                 leftMargin=LM, rightMargin=RM,
                                 topMargin=TM, bottomMargin=BM,
                                 title="Đề cương ôn tập giữa học kì I – Toán 10 (KNTT)",
                                 author="Tổ Toán – Tin, Trường THPT Hà Huy Tập",
                                 subject="Ôn tập giữa học kì I môn Toán lớp 10 – "
                                         "Chương trình Kết nối tri thức với cuộc sống",
                                 keywords="Toán 10, giữa học kì I, đề cương ôn tập, Kết nối tri thức, "
                                          "mệnh đề, tập hợp, bất phương trình bậc nhất hai ẩn, "
                                          "hệ thức lượng trong tam giác, vectơ",
                                 **kw)
        frame_cover = Frame(LM, BM, PAGE_W - LM - RM, PAGE_H - TM - BM, id="cover")
        frame_body = Frame(LM, BM, PAGE_W - LM - RM, PAGE_H - TM - BM, id="body")
        self.addPageTemplates([
            PageTemplate(id="Cover", frames=[frame_cover], onPage=self._cover_page),
            PageTemplate(id="Body", frames=[frame_body], onPage=self._body_page),
        ])

    # chân trang / đầu trang
    def _body_page(self, canv, doc):
        canv.saveState()
        canv.setFont("Noto", 7.4)
        canv.setFillColor(GREY)
        canv.drawString(LM, PAGE_H - 13 * mm,
                        "Đề cương ôn tập giữa học kì I – Toán 10 – KNTT")
        canv.drawRightString(PAGE_W - RM, PAGE_H - 13 * mm,
                             "Năm học 2026 – 2027")
        canv.setStrokeColor(RULE)
        canv.setLineWidth(0.5)
        canv.line(LM, PAGE_H - 15 * mm, PAGE_W - RM, PAGE_H - 15 * mm)
        canv.line(LM, 13.5 * mm, PAGE_W - RM, 13.5 * mm)
        canv.setFillColor(NAVY)
        canv.setFont("Noto-Bold", 8.6)
        canv.drawCentredString(PAGE_W / 2, 9.6 * mm, "%d" % doc.page)
        canv.restoreState()

    def _cover_page(self, canv, doc):
        canv.saveState()
        canv.setFillColor(NAVY)
        canv.rect(0, PAGE_H - 80 * mm, PAGE_W, 80 * mm, stroke=0, fill=1)
        canv.setFillColor(colors.HexColor("#0E6E6E"))
        canv.rect(0, PAGE_H - 82.5 * mm, PAGE_W, 2.5 * mm, stroke=0, fill=1)
        canv.setFillColor(colors.HexColor("#E8A33D"))
        canv.rect(0, PAGE_H - 83.6 * mm, PAGE_W, 1.1 * mm, stroke=0, fill=1)
        canv.setFillColor(colors.white)
        canv.setFont("Noto-Bold", 11)
        canv.drawCentredString(PAGE_W / 2, PAGE_H - 22 * mm, "TRƯỜNG THPT HÀ HUY TẬP")
        canv.setFont("Noto", 9.4)
        canv.setFillColor(colors.HexColor("#BFD4E4"))
        canv.drawCentredString(PAGE_W / 2, PAGE_H - 28.5 * mm, "TỔ TOÁN – TIN")
        canv.setFont("Noto-Italic", 9)
        canv.drawCentredString(PAGE_W / 2, PAGE_H - 38 * mm,
                               "Năm học 2026 – 2027")
        canv.drawCentredString(PAGE_W / 2, PAGE_H - 44 * mm,
                               "Thời gian làm bài: 90 phút")
        canv.setFillColor(NAVY)
        canv.setFont("Noto-Bold", 8.4)
        canv.drawCentredString(PAGE_W / 2, 20 * mm,
                               "Tài liệu lưu hành nội bộ – dùng cho học sinh khối 10 ôn thi giữa học kì I")
        canv.restoreState()

    # mục lục
    def afterFlowable(self, flowable):
        if isinstance(flowable, ChapterBand):
            key = "ch-%d" % self.page
            self.notify("TOCEntry", (0, flowable.toc_text, self.page))
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(flowable.toc_text, key, level=0)
            self._have_chapter = True
        elif isinstance(flowable, Paragraph) and flowable.style.name == "h2":
            txt = flowable.getPlainText()
            self.notify("TOCEntry", (1, txt, self.page))
            key = "sec-%d-%d" % (self.page, id(flowable) % 10000)
            self.canv.bookmarkPage(key)
            if getattr(self, "_have_chapter", False):
                self.canv.addOutlineEntry(txt, key, level=1)


def toc():
    t = TableOfContents()
    t.levelStyles = [
        _p("toc0", fontName="Noto-Bold", fontSize=9.2, leading=11, textColor=NAVY,
           firstLineIndent=0, leftIndent=0, rightIndent=18, spaceBefore=2.4),
        _p("toc1", fontSize=8.4, leading=9.4, textColor=INK,
           firstLineIndent=0, leftIndent=14, rightIndent=18, spaceBefore=0),
    ]
    t.dotsMinLevel = 0
    return t


# ------------------------------------------------------------ exam components
BADGE = {
    "NB": ("#0E6E6E", "Nhận biết"),
    "TH": ("#B4560F", "Thông hiểu"),
    "VD": ("#8A1C4A", "Vận dụng"),
    "VDC": ("#5B2A86", "Vận dụng cao"),
}


def badge(level):
    """Nhãn mức độ (NB/TH/VD/VDC) dạng chữ nhỏ màu."""
    if not level:
        return ""
    if level not in BADGE:
        return ('<font size="7.4" color="#5B6770"><b>%s</b></font>&nbsp;&nbsp;' % level)
    col, name = BADGE[level]
    return ('<font size="7.4" color="%s"><b>%s · %s</b></font>&nbsp;&nbsp;'
            % (col, level, name))


def question(num, text, level=None, points=None):
    """Khối câu hỏi: 'Câu 3.' + nhãn mức độ + nội dung."""
    head = '<b><font color="#12395B">Câu %s.</font></b> ' % num
    tail = ""
    if points:
        tail = ('&nbsp;<font size="7.6" color="#5B6770">(%s)</font>'
                % points)
    st = _p("qbody", leftIndent=15, firstLineIndent=-15, spaceAfter=4.5)
    return Paragraph(inline(head + badge(level) + text + tail), st)


def options(items, cols=2, indent=15):
    """items: ['A. ...', 'B. ...', ...] -> bảng 2 hoặc 4 cột."""
    n = len(items)
    cols = min(cols, n)
    rows = []
    per = (n + cols - 1) // cols
    for r in range(per):
        row = []
        for c in range(cols):
            k = c * per + r
            row.append(P(items[k], "opt") if k < n else "")
        rows.append(row)
    w = (PAGE_W - LM - RM - indent) / cols
    t = Table(rows, colWidths=[w] * cols, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (indent, 0), (0, -1), indent),
        ("LEFTPADDING", (1, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2),
        ("TOPPADDING", (0, 0), (-1, -1), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
    ]))
    return [Spacer(1, 1), t, Spacer(1, 6)]


def truefalse(stmts, header=True, show=True):
    """stmts: [(mark, text, 'Đ'/'S'), ...] -> bảng có cột Đ/S (show=False: để trống)."""
    rows = []
    if header:
        rows.append([Paragraph("<b>Ý</b>", S["th"]),
                     Paragraph("<b>Mệnh đề</b>", S["th"]),
                     Paragraph("<b>Đ/S</b>", S["th"])])
    for mark, txt, val in stmts:
        rows.append([Paragraph(inline("<b>%s</b>" % mark), S["tdc"]),
                     Paragraph(inline(txt), S["td"]),
                     Paragraph(inline("<b>%s</b>" % val) if show else "&nbsp;", S["tdc"])])
    t = Table(rows, colWidths=[11 * mm, None, 14 * mm], hAlign="CENTER")
    st = [
        ("GRID", (0, 0), (-1, -1), 0.5, RULE),
        ("BACKGROUND", (2, 0), (2, -1), LIGHT),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]
    if header:
        st.append(("BACKGROUND", (0, 0), (-1, 0), NAVY))
        st.append(("BACKGROUND", (0, 1), (1, -1), colors.white))
    t.setStyle(TableStyle(st))
    return [Spacer(1, 2), t, Spacer(1, 5)]


def answer(text, label="Lời giải"):
    """Khối lời giải: nhãn nhỏ, chữ thường, thụt lề nhẹ."""
    head = Paragraph(inline('<font size="8.6" color="#0E6E6E"><b>▸ %s</b></font>'
                            % label),
                     _p("ansh", fontSize=8.6, leading=12, spaceBefore=1, spaceAfter=2))
    body = text if isinstance(text, list) else [P(text)]
    inner = [head] + [P(t, "body_tight") if isinstance(t, str) else t for t in body]
    t = Table([[inner]], colWidths=[None])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F7FAF9")),
        ("LINEBEFORE", (0, 0), (0, -1), 2.2, colors.HexColor("#A9CFBB")),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return [Spacer(1, 1), t, Spacer(1, 7)]


def example(title, body):
    """Ví dụ minh hoạ: tiêu đề đậm + nội dung."""
    return [P('<b>Ví dụ.</b> <i>%s</i>' % title, "body_tight")] + \
           [P(b, "body_tight") if isinstance(b, str) else b for b in
            (body if isinstance(body, list) else [body])]


def steps(items, style="bullet2", mark="–"):
    return [B(t, style, mark) for t in items]


def two_col(left, right, wl=0.5):
    w = PAGE_W - LM - RM
    t = Table([[left, right]], colWidths=[w * wl, w * (1 - wl)])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (0, -1), 0),
        ("LEFTPADDING", (1, 0), (1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))
    return t


# ---------------------------------------------------------------------- ảnh
FIG_DIR = os.path.join(HERE, "assets", "fig")


def figure(name, width_mm, caption=None):
    """Chèn hình (PNG trong assets/fig) kèm chú thích."""
    from reportlab.platypus import Image
    path = os.path.join(FIG_DIR, name)
    img = Image(path)
    ratio = img.imageHeight / float(img.imageWidth)
    img.drawWidth = width_mm * mm
    img.drawHeight = width_mm * mm * ratio
    img.hAlign = "CENTER"
    out = [Spacer(1, 4), img]
    if caption:
        out.append(Paragraph(inline(caption),
                             _p("figcap", fontSize=8.2, leading=11.4, textColor=GREY,
                                alignment=TA_CENTER, spaceBefore=2.5)))
    out.append(Spacer(1, 8))
    return out
