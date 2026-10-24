#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
md2pdf.py — Bộ dựng PDF cho "Đề cương ôn tập Giữa học kì I – Toán 10 (KNTT)".

Nội dung được viết trong content.md bằng một tập cú pháp Markdown rút gọn,
sau đó được chuyển thành PDF bằng ReportLab (không cần LaTeX/pandoc).

Cú pháp nội dung (content.md)
-----------------------------
# Tiêu đề chương            -> dải màu (Band) + mục lục cấp 1
## Mục                      -> mục lục cấp 2
### Mục nhỏ                 -> mục lục cấp 3
Đoạn văn                    -> đoạn văn căn đều
- gạch đầu dòng             -> danh sách (thụt lề 2 dấu cách = cấp 2)
1. mục đánh số             -> danh sách đánh số
> nội dung                  -> hộp ghi chú (xanh)
!> nội dung                 -> hộp cảnh báo (hổ phách)
+> nội dung                 -> hộp "chốt ý / kết quả" (xanh lá)
| a | b |                   -> bảng (hàng thứ hai là |---|---| để bật kiểu tiêu đề)
$...$                       -> công thức (chỉ để đánh dấu, in như chữ thường)
**đậm**, *nghiêng*, `mã`
[[pagebreak]]  [[toc]]  [[lp]]  [[venn:both|A ∩ B]]
"""

import os
import re
import html
import sys

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, Flowable, NextPageTemplate, CondPageBreak,
)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.platypus.flowables import HRFlowable

# --------------------------------------------------------------------------
# Đường dẫn & phông chữ
# --------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
MPL_DIR = None
try:  # phông nghiêng lấy từ gói matplotlib (DejaVu Serif Italic)
    import matplotlib
    MPL_DIR = os.path.join(os.path.dirname(matplotlib.__file__), "mpl-data", "fonts", "ttf")
except Exception:  # pragma: no cover
    MPL_DIR = FONT_DIR

FONTS = {
    "Body": os.path.join(FONT_DIR, "DejaVuSerif.ttf"),
    "Body-Bold": os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf"),
    "Body-Italic": os.path.join(MPL_DIR, "DejaVuSerif-Italic.ttf"),
    "Body-BoldItalic": os.path.join(MPL_DIR, "DejaVuSerif-BoldItalic.ttf"),
    "Head": os.path.join(FONT_DIR, "DejaVuSans.ttf"),
    "Head-Bold": os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf"),
    "Head-Oblique": os.path.join(MPL_DIR, "DejaVuSans-Oblique.ttf"),
    "Mono": os.path.join(FONT_DIR, "DejaVuSansMono.ttf"),
    "Vec": os.path.join(FONT_DIR, "DejaVuSans.ttf"),
    "Vec-Bold": os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf"),
}

for name, path in FONTS.items():
    if os.path.exists(path):
        pdfmetrics.registerFont(TTFont(name, path))
    else:  # phông dự phòng
        pdfmetrics.registerFont(TTFont(name, FONTS["Body"]))

registerFontFamily("Body", normal="Body", bold="Body-Bold",
                   italic="Body-Italic", boldItalic="Body-BoldItalic")
registerFontFamily("Head", normal="Head", bold="Head-Bold",
                   italic="Head-Oblique", boldItalic="Head-Bold")
registerFontFamily("Mono", normal="Mono", bold="Mono", italic="Mono", boldItalic="Mono")
registerFontFamily("Vec", normal="Vec", bold="Vec-Bold", italic="Vec", boldItalic="Vec-Bold")

# Ký tự không có trong DejaVuSerif -> in bằng DejaVuSans
FALLBACK_CHARS = {}


def update_fallbacks(text):
    """Ký tự nào thiếu ở bất kỳ mặt chữ serif nào thì in bằng DejaVuSans."""
    from fontTools.ttLib import TTFont
    maps = []
    for key in ("Body", "Body-Bold", "Body-Italic"):
        try:
            maps.append(TTFont(FONTS[key]).getBestCmap())
        except Exception:
            pass
    global FALLBACK_CHARS
    FALLBACK_CHARS = {}
    for ch in sorted(set(text)):
        if ord(ch) < 128 or ch in "\n\t":
            continue
        if any(ord(ch) not in cm for cm in maps):
            FALLBACK_CHARS[ch] = "Vec"

# --------------------------------------------------------------------------
# Bảng màu
# --------------------------------------------------------------------------
INK = colors.HexColor("#1b2430")
INK_SOFT = colors.HexColor("#41505f")
NAVY = colors.HexColor("#12305c")
BLUE = colors.HexColor("#1d4ed8")
BLUE_L = colors.HexColor("#eaf0fd")
TEAL = colors.HexColor("#0f766e")
TEAL_L = colors.HexColor("#e6f4f1")
AMBER = colors.HexColor("#b45309")
AMBER_L = colors.HexColor("#fdf1de")
GREEN = colors.HexColor("#166534")
GREEN_L = colors.HexColor("#eaf5ec")
LINE = colors.HexColor("#cfd8e3")
PAPER = colors.HexColor("#f7f9fc")
WHITE = colors.white

PAGE_W, PAGE_H = A4
LM, RM, TM, BM = 19 * mm, 18 * mm, 22 * mm, 19 * mm
CONTENT_W = PAGE_W - LM - RM

# --------------------------------------------------------------------------
# Kiểu đoạn văn
# --------------------------------------------------------------------------
STY = {}
STY["body"] = ParagraphStyle(
    "body", fontName="Body", fontSize=10.2, leading=15.6, textColor=INK,
    alignment=TA_JUSTIFY, spaceAfter=4.6, spaceBefore=0, splitLongWords=0,
    bulletFontName="Body", bulletFontSize=10.2,
)
STY["lead"] = ParagraphStyle(
    "lead", parent=STY["body"], fontSize=10.8, leading=16.6, textColor=INK_SOFT,
    spaceAfter=8,
)
STY["h2"] = ParagraphStyle(
    "h2", fontName="Head-Bold", fontSize=13.2, leading=17, textColor=NAVY,
    spaceBefore=15, spaceAfter=2, keepWithNext=1,
)
STY["h3"] = ParagraphStyle(
    "h3", fontName="Head-Bold", fontSize=10.9, leading=14.6, textColor=BLUE,
    spaceBefore=10, spaceAfter=3.5, keepWithNext=1,
)
STY["h4"] = ParagraphStyle(
    "h4", fontName="Head-Bold", fontSize=9.9, leading=13.4, textColor=TEAL,
    spaceBefore=8, spaceAfter=2.5, keepWithNext=1,
)
STY["bullet"] = ParagraphStyle(
    "bullet", parent=STY["body"], leftIndent=13, bulletIndent=2,
    spaceAfter=2.6, alignment=TA_LEFT,
)
STY["bullet2"] = ParagraphStyle(
    "bullet2", parent=STY["bullet"], leftIndent=27, bulletIndent=15,
)
STY["num"] = ParagraphStyle(
    "num", parent=STY["body"], leftIndent=17, spaceAfter=2.6, alignment=TA_LEFT,
)
STY["box"] = ParagraphStyle(
    "box", parent=STY["body"], fontSize=9.8, leading=14.8, alignment=TA_LEFT,
    spaceAfter=2.4,
)
STY["boxb"] = ParagraphStyle(
    "boxb", parent=STY["box"], fontName="Body-Bold", textColor=NAVY,
    spaceAfter=3,
)
STY["th"] = ParagraphStyle(
    "th", fontName="Head-Bold", fontSize=8.9, leading=12, textColor=WHITE,
    alignment=TA_CENTER,
)
STY["td"] = ParagraphStyle(
    "td", fontName="Head", fontSize=8.7, leading=12.4, textColor=INK,
    alignment=TA_LEFT,
)
STY["tdc"] = ParagraphStyle("tdc", parent=STY["td"], alignment=TA_CENTER)
STY["q"] = ParagraphStyle(
    "q", parent=STY["body"], alignment=TA_LEFT, spaceAfter=1.6,
    leftIndent=15, firstLineIndent=-15,
)
STY["opt"] = ParagraphStyle(
    "opt", parent=STY["body"], alignment=TA_LEFT, spaceAfter=1.2,
    leftIndent=30, firstLineIndent=-15, fontSize=10.0, leading=15.0,
)
STY["stmt"] = ParagraphStyle(
    "stmt", parent=STY["body"], alignment=TA_LEFT, leftIndent=17,
    firstLineIndent=-17, spaceAfter=2.2, fontSize=10.0, leading=15.0,
)
STY["optc"] = ParagraphStyle(
    "optc", parent=STY["body"], alignment=TA_LEFT, spaceAfter=0,
    fontSize=9.9, leading=14.4, textColor=INK,
)
STY["sol"] = ParagraphStyle(
    "sol", parent=STY["body"], fontSize=9.9, leading=15.0, spaceAfter=3.4,
)
STY["cap"] = ParagraphStyle(
    "cap", fontName="Head-Oblique", fontSize=8.4, leading=11.5,
    textColor=INK_SOFT, alignment=TA_CENTER, spaceAfter=8, spaceBefore=2,
)
STY["toc0"] = ParagraphStyle(
    "toc0", fontName="Head-Bold", fontSize=10.6, leading=16,
    textColor=NAVY, spaceBefore=7,
)
STY["toc1"] = ParagraphStyle(
    "toc1", fontName="Head", fontSize=9.6, leading=14,
    textColor=INK, leftIndent=13, firstLineIndent=0,
)
STY["toc2"] = ParagraphStyle(
    "toc2", fontName="Head", fontSize=9.0, leading=13,
    textColor=INK_SOFT, leftIndent=26, firstLineIndent=0,
)

# --------------------------------------------------------------------------
# Tiện ích văn bản
# --------------------------------------------------------------------------
def esc(s):
    return html.escape(s, quote=False)


def inline(s):
    """Chuyển cú pháp nội tuyến sang thẻ của ReportLab."""
    s = esc(s)
    # chỉ số dưới kiểu Unicode: d₁ -> d<sub>1</sub>
    s = re.sub(r"([A-Za-z])([\u2080-\u2089]+)",
               lambda m: m.group(1) + "<sub>" + "".join(
                   "0123456789"[ord(c) - 0x2080] for c in m.group(2)) + "</sub>", s)
    for ch, fnt in FALLBACK_CHARS.items():
        s = s.replace(ch, '<font name="%s">%s</font>' % (fnt, ch))
    s = re.sub(r"\\v\{([^{}]*)\}", lambda m: '<font name="Vec">%s\u20d7</font>' % m.group(1), s)
    s = re.sub(r"`([^`]+)`", r'<font name="Mono" size="9">\1</font>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", s)
    s = s.replace("$", "").replace("\\|", "|")
    return s


def P(text, style="body", **kw):
    return Paragraph(inline(text), STY[style], **kw)


# --------------------------------------------------------------------------
# Flowable: dải tiêu đề chương
# --------------------------------------------------------------------------
class Band(Flowable):
    """Dải màu đậm chứa tiêu đề chương (mục lục cấp 1)."""

    def __init__(self, num, title, sub=None, color=NAVY):
        Flowable.__init__(self)
        self.num, self.title, self.sub = num, title, sub
        self.color = color
        self.toc_text = (("%s. " % num) if num else "") + title
        self.width = CONTENT_W
        self.height = 21 * mm if sub else 17 * mm

    def wrap(self, aw, ah):
        self.width = aw
        return aw, self.height

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        c.saveState()
        c.setFillColor(self.color)
        c.roundRect(0, 0, w, h, 2.2 * mm, stroke=0, fill=1)
        # vệt sáng bên trái
        c.setFillColor(colors.Color(1, 1, 1, alpha=0.16))
        c.roundRect(0, 0, 4.4 * mm, h, 2.2 * mm, stroke=0, fill=1)
        c.setFillColor(WHITE)
        x = 8.4 * mm
        if self.num:
            c.setFont("Head-Bold", 20)
            c.drawString(x, h - 11.4 * mm, str(self.num))
            x += 12.6 * mm
            c.setStrokeColor(colors.Color(1, 1, 1, alpha=0.45))
            c.setLineWidth(0.8)
            c.line(x - 4.6 * mm, 5.6 * mm, x - 4.6 * mm, h - 5.6 * mm)
        c.setFont("Head-Bold", 15.2)
        c.drawString(x, h - (11.8 * mm if self.sub else 10.8 * mm), self.title)
        if self.sub:
            c.setFont("Head", 9.1)
            c.setFillColor(colors.Color(1, 1, 1, alpha=0.86))
            c.drawString(x, 4.6 * mm, self.sub)
        c.restoreState()


class HRule(Flowable):
    """Đường kẻ mảnh, có thể kèm nhãn nhỏ ở giữa."""

    def __init__(self, w=None, color=LINE, thickness=0.7, pad=3.4, label=None):
        Flowable.__init__(self)
        self._w, self.color, self.t, self.pad = w, color, thickness, pad
        self.label = label

    def wrap(self, aw, ah):
        self.width = self._w or aw
        return self.width, self.t + 2 * self.pad

    def draw(self):
        c = self.canv
        c.saveState()
        c.setStrokeColor(self.color)
        c.setLineWidth(self.t)
        y = self.pad
        if self.label:
            c.setFont("Head-Bold", 8)
            tw = c.stringWidth(self.label, "Head-Bold", 8)
            c.drawString(0, y + 2.2, self.label)
            x0 = tw + 6
            c.line(x0, y, self.width, y)
        else:
            c.line(0, y, self.width, y)
        c.restoreState()


# --------------------------------------------------------------------------
# Flowable: biểu đồ Ven
# --------------------------------------------------------------------------
class Venn(Flowable):
    """Hai đường tròn A, B; tô vùng: both | either | left | right | none."""

    def __init__(self, mode="both", label=None, size=34 * mm, color=BLUE):
        Flowable.__init__(self)
        self.mode = mode
        self.label = label
        self.size = size
        self.color = color

    def wrap(self, aw, ah):
        self.width = self.size
        self.height = self.size * 0.74 + (5 * mm if self.label else 0)
        return self.width, self.height

    def draw(self):
        c = self.canv
        r = self.size * 0.27
        cx1, cy = self.size * 0.33, self.height - (5 * mm if self.label else 0) - r
        cx2 = self.size * 0.67
        fill = colors.Color(self.color.red, self.color.green, self.color.blue, alpha=0.30)
        c.saveState()
        paths = {}
        for i, cx in enumerate((cx1, cx2)):
            p = c.beginPath()
            p.circle(cx, cy, r)
            paths[i] = p

        def paint(paths_to_fill, col):
            for p in paths_to_fill:
                c.setFillColor(col)
                c.drawPath(p, stroke=0, fill=1)

        if self.mode == "either":
            paint([paths[0], paths[1]], fill)
        elif self.mode == "both":
            c.saveState()
            c.clipPath(paths[0], stroke=0, fill=0)
            paint([paths[1]], fill)
            c.restoreState()
        elif self.mode == "left":
            paint([paths[0]], fill)
            paint([paths[1]], colors.white)
        elif self.mode == "right":
            paint([paths[1]], fill)
            paint([paths[0]], colors.white)

        for cx in (cx1, cx2):
            c.setStrokeColor(colors.HexColor("#334155"))
            c.setLineWidth(1.0)
            c.circle(cx, cy, r, stroke=1, fill=0)
        c.setFont("Body-Italic", 10)
        c.setFillColor(INK)
        c.drawCentredString(cx1 - r - 5.4, cy - 3.2, "A")
        c.drawCentredString(cx2 + r + 5.4, cy - 3.2, "B")
        if self.label:
            c.setFont("Head", 8)
            c.setFillColor(INK_SOFT)
            c.drawCentredString(self.width / 2, 0.6 * mm, self.label)
        c.restoreState()


class VennRow(Flowable):
    """Bốn biểu đồ Ven cạnh nhau: giao, hợp, hiệu, phần bù."""

    ITEMS = [
        ("both", "A ∩ B"),
        ("either", "A ∪ B"),
        ("left", "A \\ B"),
        ("right", "B \\ A"),
    ]

    def __init__(self, w=CONTENT_W):
        Flowable.__init__(self)
        self.width = w
        self.height = 33 * mm

    def wrap(self, aw, ah):
        self.width = min(self.width, aw)
        return self.width, self.height

    def draw(self):
        c = self.canv
        slot = self.width / 4.0
        r = slot * 0.185
        cy = 16.5 * mm
        fill = colors.Color(0.11, 0.31, 0.85, alpha=0.28)
        for i, (mode, lab) in enumerate(self.ITEMS):
            cx1 = i * slot + slot / 2 - r * 0.62
            cx2 = i * slot + slot / 2 + r * 0.62
            p1, p2 = c.beginPath(), c.beginPath()
            p1.circle(cx1, cy, r)
            p2.circle(cx2, cy, r)
            c.saveState()
            if mode == "either":
                for p in (p1, p2):
                    c.setFillColor(fill)
                    c.drawPath(p, stroke=0, fill=1)
            elif mode == "both":
                c.saveState()
                c.clipPath(p1, stroke=0, fill=0)
                c.setFillColor(fill)
                c.drawPath(p2, stroke=0, fill=1)
                c.restoreState()
            elif mode == "left":
                c.setFillColor(fill)
                c.drawPath(p1, stroke=0, fill=1)
                c.setFillColor(colors.white)
                c.drawPath(p2, stroke=0, fill=1)
            elif mode == "right":
                c.setFillColor(fill)
                c.drawPath(p2, stroke=0, fill=1)
                c.setFillColor(colors.white)
                c.drawPath(p1, stroke=0, fill=1)
            c.setStrokeColor(colors.HexColor("#334155"))
            c.setLineWidth(0.9)
            for p in (p1, p2):
                c.drawPath(p, stroke=1, fill=0)
            c.setFillColor(INK)
            c.setFont("Head-Bold", 9)
            c.drawCentredString(i * slot + slot / 2, 2.2 * mm, lab)
            c.restoreState()


# --------------------------------------------------------------------------
# Flowable: hình minh hoạ miền nghiệm bài toán quy hoạch (Câu 24)
# --------------------------------------------------------------------------
class LPPlot(Flowable):
    """Miền nghiệm của hệ: 2x + y <= 100, x + 2y <= 80, x >= 0, y >= 0."""

    RED = colors.HexColor("#b91c1c")
    GRN = colors.HexColor("#047857")

    def __init__(self, w=120 * mm, h=76 * mm):
        Flowable.__init__(self)
        self.width, self.height = w, h

    def wrap(self, aw, ah):
        return min(self.width, aw), self.height

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        ox, oy = 15 * mm, 12 * mm
        s = min((w - ox - 7 * mm) / 55.0, (h - oy - 8 * mm) / 46.0)
        X = lambda v: ox + v * s
        Y = lambda v: oy + v * s

        c.saveState()
        # lưới nhẹ
        c.setStrokeColor(colors.HexColor("#e8edf4"))
        c.setLineWidth(0.5)
        for v in range(0, 56, 5):
            c.line(X(v), Y(0), X(v), Y(44))
        for v in range(0, 46, 5):
            c.line(X(0), Y(v), X(55), Y(v))
        # miền nghiệm
        pts = [(0, 0), (50, 0), (40, 20), (0, 40)]
        p = c.beginPath()
        p.moveTo(X(pts[0][0]), Y(pts[0][1]))
        for q in pts[1:]:
            p.lineTo(X(q[0]), Y(q[1]))
        p.close()
        c.setFillColor(colors.Color(0.11, 0.31, 0.85, alpha=0.15))
        c.setStrokeColor(BLUE)
        c.setLineWidth(1.2)
        c.drawPath(p, stroke=1, fill=1)

        # vùng vẽ (cắt phần đường thẳng tràn ra ngoài)
        c.saveState()
        clip = c.beginPath()
        clip.rect(X(0) - 0.6, Y(0) - 0.6, X(55) - X(0) + 1.2, Y(44) - Y(0) + 1.2)
        c.clipPath(clip, stroke=0, fill=0)
        c.setLineWidth(1.5)
        c.setStrokeColor(self.RED)
        c.line(X(0), Y(100), X(52), Y(-4))
        c.setStrokeColor(self.GRN)
        c.line(X(0), Y(40), X(56), Y(8))
        c.restoreState()

        # trục
        c.setStrokeColor(INK)
        c.setLineWidth(0.9)
        c.line(X(0), Y(0), X(55), Y(0))
        c.line(X(0), Y(0), X(0), Y(44))
        c.setFillColor(INK_SOFT)
        c.setFont("Head", 7.6)
        c.drawRightString(X(0) - 2.6, Y(0) - 3.2, "O")
        c.drawString(X(55) + 1.2, Y(0) - 2.6, "x")
        c.drawString(X(0) + 1.8, Y(44) + 1.4, "y")
        for v in (10, 20, 30, 40, 50):
            c.setStrokeColor(INK_SOFT)
            c.setLineWidth(0.7)
            c.line(X(v), Y(0) - 1.4, X(v), Y(0) + 1.4)
            c.drawCentredString(X(v), Y(0) - 7.2, str(v))
        for v in (10, 20, 30, 40):
            c.line(X(0) - 1.4, Y(v), X(0) + 1.4, Y(v))
            c.drawRightString(X(0) - 3.0, Y(v) - 2.4, str(v))
        # nhãn đỉnh
        c.setFont("Head-Bold", 7.4)
        c.setFillColor(NAVY)
        c.drawString(X(50) + 2.0, Y(0) + 2.8, "(50; 0)")
        c.drawString(X(40) + 2.4, Y(20) + 2.4, "(40; 20)")
        c.drawString(X(0) + 2.6, Y(40) + 1.8, "(0; 40)")
        # chú giải
        lx, ly = X(28.5), Y(35.0)
        c.setFillColor(colors.white)
        c.setStrokeColor(LINE)
        c.setLineWidth(0.6)
        c.roundRect(lx, ly, 25.0 * mm, 9.6 * mm, 1.2 * mm, stroke=1, fill=1)
        c.setFont("Head", 6.9)
        for i, (col, txt) in enumerate([(self.RED, "d\u2081: 2x + y = 100"),
                                        (self.GRN, "d\u2082: x + 2y = 80")]):
            yy = ly + 6.0 * mm - i * 3.7 * mm
            c.setStrokeColor(col)
            c.setLineWidth(1.8)
            c.line(lx + 2.2 * mm, yy + 1.1, lx + 6.2 * mm, yy + 1.1)
            c.setFillColor(INK)
            c.drawString(lx + 7.2 * mm, yy, txt)
        c.restoreState()


# --------------------------------------------------------------------------
# Hộp gọi chú
# --------------------------------------------------------------------------
BOX_STYLE = {
    "note": (BLUE_L, BLUE, "Ghi nhớ"),
    "warn": (AMBER_L, AMBER, "Lưu ý"),
    "key": (GREEN_L, GREEN, "Chốt ý"),
    "info": (PAPER, LINE, ""),
}


def make_box(paras, kind="note", title=None):
    bg, border, def_title = BOX_STYLE[kind]
    inner = []
    t = title if title is not None else def_title
    if t:
        st = ParagraphStyle("bt", parent=STY["boxb"], textColor=border)
        inner.append(Paragraph(inline(t), st))
    inner.extend(paras)
    tb = Table([[inner]], colWidths=[CONTENT_W])
    tb.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (0, -1), 2.6, border),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return [Spacer(1, 3), tb, Spacer(1, 7)]


def make_table(rows):
    """rows: list of list of str; dòng 0 là tiêu đề."""
    ncol = max(len(r) for r in rows)
    rows = [r + [""] * (ncol - len(r)) for r in rows]
    data = []
    for i, r in enumerate(rows):
        st = "th" if i == 0 else "td"
        data.append([Paragraph(inline(c), STY[st]) if c else Paragraph("", STY[st])
                     for c in r])
    # độ rộng cột: cột đầu rộng hơn
    if ncol == 1:
        widths = [CONTENT_W]
    else:
        first = CONTENT_W * (0.36 if ncol <= 3 else 0.26)
        rest = (CONTENT_W - first) / (ncol - 1)
        widths = [first] + [rest] * (ncol - 1)
    tb = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("GRID", (0, 0), (-1, -1), 0.5, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4.2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.2),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            style.append(("BACKGROUND", (0, i), (-1, i), PAPER))
    tb.setStyle(TableStyle(style))
    try:
        _, th = tb.wrap(CONTENT_W, 10000)
    except Exception:
        th = 0
    body = KeepTogether([tb]) if th < 200 * mm else tb
    return [Spacer(1, 2), body, Spacer(1, 8)]


# --------------------------------------------------------------------------
# Bộ phân tích nội dung
# --------------------------------------------------------------------------
SPECIAL = ("|", "#", ">", "!>", "+>", "- ", "[[")


def _nb(story, need):
    """Chèn ngắt trang có điều kiện, trừ khi mục vừa mới bắt đầu trang/dải tiêu đề."""
    if not story:
        return
    if isinstance(story[-1], Band):
        return
    if isinstance(story[-1], Spacer) and len(story) > 1 and isinstance(story[-2], Band):
        return
    story.append(CondPageBreak(need))


def parse(text):
    """Sinh danh sách flowable từ nội dung Markdown rút gọn."""
    story = []
    lines = text.split("\n")
    i, n = 0, len(lines)
    while i < n:
        raw = lines[i]
        s = raw.strip()

        if not s:
            i += 1
            continue

        # ---- lệnh đặc biệt
        if s == "[[pagebreak]]":
            story.append(PageBreak())
            i += 1
            continue
        if s == "[[toc]]":
            story.append(("TOC",))
            i += 1
            continue
        if s == "[[lp]]":
            story.append(Spacer(1, 4))
            story.append(LPPlot())
            i += 1
            continue
        if s.startswith("[[vennrow]]"):
            story.append(Spacer(1, 4))
            story.append(VennRow())
            story.append(Spacer(1, 8))
            i += 1
            continue
        m = re.match(r"\[\[venn:([a-z]+)(?:\|(.*?))?\]\]", s)
        if m:
            story.append(Spacer(1, 3))
            story.append(Venn(m.group(1), m.group(2)))
            story.append(Spacer(1, 7))
            i += 1
            continue
        m = re.match(r"\[\[lpfig(?:\|(.*?))?\]\]", s)
        if m:
            story.append(Spacer(1, 4))
            story.append(LPPlot())
            if m.group(1):
                story.append(Paragraph(inline(m.group(1)), STY["cap"]))
            i += 1
            continue

        # ---- tiêu đề
        if s.startswith("#"):
            level = len(s) - len(s.lstrip("#"))
            title = s[level:].strip()
            if level == 1:
                num, _, rest = title.partition("|")
                story.append(Spacer(1, 2))
                story.append(Band(num.strip() or None, rest.strip() or num.strip()))
                story.append(Spacer(1, 9))
            elif level == 2:
                _nb(story, 40 * mm)
                story.append(TocParagraph(inline(title), STY["h2"], 1))
                story.append(HRule(color=LINE, thickness=0.6, pad=2.6))
                story.append(Spacer(1, 4))
            elif level == 3:
                # chỉ đưa vào mục lục các tiểu mục có số hiệu (2.1.1, ...)
                _nb(story, 24 * mm)
                lvl = 2 if re.match(r"^\d+(\.\d+)+", title) else None
                if lvl is None:
                    story.append(Paragraph(inline(title), STY["h3"]))
                else:
                    story.append(TocParagraph(inline(title), STY["h3"], lvl))
            else:
                story.append(Paragraph(inline(title), STY["h4"]))
            i += 1
            continue

        # ---- hộp
        if s.startswith("!>") or s.startswith("+>") or s.startswith(">"):
            kind = "warn" if s.startswith("!>") else ("key" if s.startswith("+>") else "note")
            buf, i = [], i
            while i < n:
                ls = lines[i].strip()
                if ls[:2] in ("!>", "+>") or (ls.startswith("> ") or ls == ">"):
                    buf.append(ls[2:].strip())
                    i += 1
                else:
                    break
            # dòng đầu hoàn toàn in đậm -> tiêu đề của hộp
            title = None
            if buf and re.fullmatch(r"\*\*[^*]+\*\*", buf[0]):
                title = buf[0][2:-2]
                buf = buf[1:]
            # gom thành đoạn, dòng trống phân tách
            paras, cur = [], []
            for b in buf:
                if b == "":
                    if cur:
                        paras.append(" ".join(cur))
                        cur = []
                else:
                    cur.append(b)
            if cur:
                paras.append(" ".join(cur))
            story.extend(make_box([Paragraph(inline(p), STY["box"]) for p in paras], kind, title))
            continue

        # ---- hàng phương án trắc nghiệm (2 cột × 2 dòng)
        if s.startswith("@opts "):
            body = s[len("@opts "):]
            parts = [p.strip() for p in body.split("|")]
            while len(parts) < 4:
                parts.append("")
            data = [[Paragraph(inline(parts[0]), STY["optc"]),
                     Paragraph(inline(parts[1]), STY["optc"])],
                    [Paragraph(inline(parts[2]), STY["optc"]),
                     Paragraph(inline(parts[3]), STY["optc"])]]
            tb = Table(data, colWidths=[CONTENT_W / 2.0] * 2, hAlign="LEFT")
            tb.setStyle(TableStyle([
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 16),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 1.4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.4),
            ]))
            story.append(tb)
            story.append(Spacer(1, 3.6))
            i += 1
            continue

        # ---- hàng phương án 4 cột (phương án ngắn)
        if s.startswith("@opts4 "):
            parts = [p.strip() for p in s[len("@opts4 "):].split("|")]
            while len(parts) < 4:
                parts.append("")
            data = [[Paragraph(inline(p), STY["optc"]) for p in parts]]
            tb = Table(data, colWidths=[CONTENT_W / 4.0] * 4, hAlign="LEFT")
            tb.setStyle(TableStyle([
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                ("TOPPADDING", (0, 0), (-1, -1), 1.4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3.4),
            ]))
            story.append(tb)
            i += 1
            continue

        # ---- bảng
        if s.startswith("|") and s.endswith("|"):
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                line = lines[i].strip()
                line = line[1:] if line.startswith("|") else line
                line = line[:-1] if line.endswith("|") and not line.endswith("\\|") else line
                cells = [c.strip().replace("\\|", "|")
                         for c in re.split(r"(?<!\\)\|", line)]
                if not all(re.fullmatch(r":?-{2,}:?", c or "-") for c in cells):
                    rows.append(cells)
                i += 1
            story.extend(make_table(rows))
            continue

        # ---- danh sách
        if s.startswith("- "):
            while i < n and lines[i].strip().startswith("- "):
                item = lines[i].strip()[2:].strip()
                indented = len(lines[i]) - len(lines[i].lstrip())
                st = "bullet2" if indented >= 2 else "bullet"
                story.append(Paragraph(inline(item), STY[st], bulletText="•" if indented < 2 else "–"))
                i += 1
            story.append(Spacer(1, 3))
            continue

        m = re.match(r"^(\d{1,2})[.)]\s+(.*)$", s)
        if m and not s.startswith("|"):
            num = m.group(1)
            body = m.group(2)
            # gom các dòng nối tiếp (không phải dòng đánh số mới)
            i += 1
            while i < n and lines[i].strip() and not re.match(r"^(\d{1,2})[.)]\s", lines[i].strip()) \
                    and not lines[i].strip().startswith(SPECIAL):
                body += " " + lines[i].strip()
                i += 1
            story.append(Paragraph(inline(body), STY["num"], bulletText=num + "."))
            continue

        # ---- dòng khẳng định a) b) c) d)
        if re.match(r"^[a-d]\)\s", s):
            buf = [s]
            i += 1
            while i < n and lines[i].strip() and not lines[i].strip().startswith(SPECIAL) \
                    and not re.match(r"^([a-d]\)|\d{1,2}[.)])\s", lines[i].strip()):
                buf.append(lines[i].strip())
                i += 1
            story.append(Paragraph(inline(" ".join(buf)), STY["stmt"]))
            continue

        # ---- đoạn văn
        buf = [s]
        i += 1
        while i < n and lines[i].strip() and not lines[i].strip().startswith(SPECIAL) \
                and not re.match(r"^\d{1,2}[.)]\s", lines[i].strip()):
            buf.append(lines[i].strip())
            i += 1
        story.append(Paragraph(inline(" ".join(buf)), STY["body"]))
    return story


# --------------------------------------------------------------------------
# Khung trang, đầu trang, chân trang
# --------------------------------------------------------------------------
RUNNING = "Đề cương ôn tập Giữa học kì I – Toán 10"


def cover_page(canv, doc):
    c = canv
    c.saveState()
    # nền trên
    c.setFillColor(NAVY)
    c.rect(0, PAGE_H - 128 * mm, PAGE_W, 128 * mm, stroke=0, fill=1)
    c.setFillColor(colors.Color(1, 1, 1, alpha=0.05))
    c.circle(PAGE_W - 22 * mm, PAGE_H - 24 * mm, 46 * mm, stroke=0, fill=1)
    c.circle(16 * mm, PAGE_H - 118 * mm, 30 * mm, stroke=0, fill=1)
    # dải màu
    c.setFillColor(colors.HexColor("#f2b705"))
    c.rect(0, PAGE_H - 130.6 * mm, PAGE_W, 2.6 * mm, stroke=0, fill=1)
    c.setFillColor(TEAL)
    c.rect(0, PAGE_H - 132.6 * mm, PAGE_W, 2.0 * mm, stroke=0, fill=1)

    x = LM
    c.setFillColor(colors.Color(1, 1, 1, alpha=0.80))
    c.setFont("Head-Bold", 9.2)
    c.drawString(x, PAGE_H - 30 * mm, "BỘ SÁCH KẾT NỐI TRI THỨC VỚI CUỘC SỐNG")
    c.setFont("Head", 9.2)
    c.drawString(x, PAGE_H - 36 * mm, "Chương trình Giáo dục phổ thông 2018 · Môn Toán")

    c.setFillColor(WHITE)
    c.setFont("Head-Bold", 33)
    c.drawString(x, PAGE_H - 58 * mm, "ĐỀ CƯƠNG ÔN TẬP")
    c.setFont("Head-Bold", 27)
    c.drawString(x, PAGE_H - 72 * mm, "GIỮA HỌC KÌ I")
    c.setFont("Head-Bold", 19)
    c.setFillColor(colors.HexColor("#ffd166"))
    c.drawString(x, PAGE_H - 85 * mm, "TOÁN 10")
    c.setFillColor(colors.Color(1, 1, 1, alpha=0.92))
    c.setFont("Head", 12)
    c.drawString(x, PAGE_H - 96 * mm, "Tóm tắt lý thuyết · Bộ câu hỏi bám sát ma trận · Lời giải chi tiết")

    c.setFillColor(colors.Color(1, 1, 1, alpha=0.75))
    c.setFont("Head", 9)
    c.drawString(x, PAGE_H - 112 * mm, "Năm học 2026 – 2027  ·  Thời gian 90 phút  ·  Thang điểm 10")

    # khối nội dung
    y0 = PAGE_H - 170 * mm
    c.setFillColor(INK)
    c.setFont("Head-Bold", 13.6)
    c.drawString(LM, y0, "Trong tài liệu này có gì?")
    items = [
        ("1", "Cấu trúc đề & kế hoạch ôn tập", "Bảng phân bố câu hỏi, thang điểm, lộ trình 7 ngày."),
        ("2", "Kiến thức trọng tâm 4 chương", "Mệnh đề – Tập hợp · Bất phương trình · Hệ thức lượng · Vectơ."),
        ("3", "Đề tham khảo 24 câu", "Đúng cấu trúc: 12 TN · 2 Đúng–Sai · 4 Trả lời ngắn · 3 Tự luận."),
        ("4", "Đáp án & lời giải chi tiết", "Giải từng câu kèm nhận xét, cách bấm máy tính."),
        ("5", "Bài tập tự luyện & phụ lục", "12 bài tự luyện, bảng công thức, checklist trước thi."),
    ]
    y = y0 - 9 * mm
    for num, t1, t2 in items:
        c.setFillColor(BLUE)
        c.roundRect(LM, y - 3.2 * mm, 7 * mm, 7 * mm, 1.6 * mm, stroke=0, fill=1)
        c.setFillColor(WHITE)
        c.setFont("Head-Bold", 9.6)
        c.drawCentredString(LM + 3.5 * mm, y - 1.2 * mm, num)
        c.setFillColor(INK)
        c.setFont("Head-Bold", 10.4)
        c.drawString(LM + 10 * mm, y, t1)
        c.setFillColor(INK_SOFT)
        c.setFont("Head", 9.2)
        c.drawString(LM + 10 * mm, y - 5.2 * mm, t2)
        y -= 15.4 * mm

    # chân trang bìa
    c.setStrokeColor(LINE)
    c.setLineWidth(0.8)
    c.line(LM, 30 * mm, PAGE_W - RM, 30 * mm)
    c.setFillColor(INK_SOFT)
    c.setFont("Head", 8.6)
    c.drawString(LM, 22 * mm, "Biên soạn bám sát Ma trận & Bản đặc tả đề kiểm tra Giữa kì I – môn Toán, lớp 10")
    c.drawString(LM, 17 * mm, "của Tổ Toán – Tin, Trường THPT Hà Huy Tập, năm học 2026 – 2027.")
    c.setFont("Head-Bold", 8.6)
    c.setFillColor(BLUE)
    c.drawRightString(PAGE_W - RM, 22 * mm, "Tài liệu ôn tập")
    c.restoreState()


def body_page(canv, doc):
    c = canv
    c.saveState()
    # đầu trang
    c.setFont("Head", 7.8)
    c.setFillColor(INK_SOFT)
    c.drawString(LM, PAGE_H - 12.4 * mm, RUNNING)
    c.drawRightString(PAGE_W - RM, PAGE_H - 12.4 * mm, "Năm học 2026 – 2027")
    c.setStrokeColor(LINE)
    c.setLineWidth(0.6)
    c.line(LM, PAGE_H - 14.6 * mm, PAGE_W - RM, PAGE_H - 14.6 * mm)
    # chân trang
    c.line(LM, 14.2 * mm, PAGE_W - RM, 14.2 * mm)
    c.setFont("Head", 7.8)
    c.drawString(LM, 9.4 * mm, "Tổ Toán – Tin · THPT Hà Huy Tập")
    c.setFillColor(NAVY)
    c.setFont("Head-Bold", 8.4)
    c.drawRightString(PAGE_W - RM, 9.2 * mm, "Trang %d" % canv.getPageNumber())
    c.restoreState()


class Doc(BaseDocTemplate):
    def __init__(self, filename, **kw):
        BaseDocTemplate.__init__(self, filename, pagesize=A4,
                                 leftMargin=LM, rightMargin=RM,
                                 topMargin=TM, bottomMargin=BM,
                                 title="Đề cương ôn tập Giữa học kì I – Toán 10 (KNTT)",
                                 author="Tài liệu ôn tập Toán 10",
                                 subject="Ôn tập giữa học kì I – Toán 10 – Kết nối tri thức – 2026–2027",
                                 creator="md2pdf.py (ReportLab)",
                                 **kw)
        frame_cover = Frame(LM, BM, CONTENT_W, PAGE_H - TM - BM, id="cover",
                            leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        frame_body = Frame(LM, BM, CONTENT_W, PAGE_H - TM - BM, id="body",
                           leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[frame_cover], onPage=cover_page),
            PageTemplate(id="body", frames=[frame_body], onPage=body_page),
        ])

    _outline_level = -1

    def _outline(self, text, level):
        # cấp outline phải tăng dần từng bậc một
        lvl = min(level, self._outline_level + 1)
        lvl = max(lvl, 0)
        self._outline_level = lvl
        key = "e%d" % id(text) if isinstance(text, str) else "e"
        key = "d%d_%d" % (self.page, abs(hash((text, level))) % 10 ** 9)
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(text, key, level=lvl, closed=False)

    def afterFlowable(self, flowable):
        if isinstance(flowable, Band):
            self._outline(flowable.toc_text, 0)
            self.notify("TOCEntry", (0, flowable.toc_text, self.page))
        elif isinstance(flowable, Paragraph) and getattr(flowable, "_toc_entry", None):
            level, text = flowable._toc_entry
            self._outline(text, level)
            self.notify("TOCEntry", (level, text, self.page))


class TocParagraph(Paragraph):
    """Paragraph có đăng ký mục lục."""

    def __init__(self, text, style, toc_level):
        Paragraph.__init__(self, text, style)
        self._toc_entry = (toc_level, re.sub(r"<[^>]+>", "", text))


# --------------------------------------------------------------------------
# Dựng tài liệu
# --------------------------------------------------------------------------
def build(md_path, out_path):
    with open(md_path, encoding="utf-8") as f:
        text = f.read()

    update_fallbacks(text)
    story = [NextPageTemplate("body"), PageBreak()]

    toc = TableOfContents()
    toc.levelStyles = [STY["toc0"], STY["toc1"], STY["toc2"]]
    toc.dotsMinLevel = 0

    blocks = parse(text)
    # thay các placeholder ("TOC",) và nhãn mục lục
    fixed = []
    for b in blocks:
        if isinstance(b, tuple) and b and b[0] == "TOC":
            fixed.append(Paragraph("MỤC LỤC", ParagraphStyle(
                "toch", fontName="Head-Bold", fontSize=18, leading=22,
                textColor=NAVY, spaceAfter=10)))
            fixed.append(HRule(color=LINE, thickness=1.0, pad=4))
            fixed.append(Spacer(1, 8))
            fixed.append(toc)
            fixed.append(PageBreak())
        else:
            fixed.append(b)

    doc = Doc(out_path)
    doc.multiBuild(story + fixed)
    return out_path


if __name__ == "__main__":
    md = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "content.md")
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "..", "DE-CUONG.pdf")
    build(md, out)
    print("Đã tạo:", os.path.abspath(out))
