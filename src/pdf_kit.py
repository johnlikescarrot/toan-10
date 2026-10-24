# -*- coding: utf-8 -*-
"""Bộ công cụ dựng PDF cho đề cương ôn tập Toán 10 (ReportLab, không phụ thuộc mạng).

Cung cấp: đăng ký font tiếng Việt, hệ thống màu/kiểu chữ, các khối nội dung
(hộp ghi nhớ, ví dụ, lỗi thường gặp), bảng biểu và một số hình vẽ minh hoạ
(biểu đồ Ven, trục số, miền nghiệm, tam giác thực tế, hình bình hành).
"""

from __future__ import annotations

import html
import os
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.platypus import (
    BaseDocTemplate,
    Flowable,
    Frame,
    KeepTogether,
    ListFlowable,
    ListItem,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

# --------------------------------------------------------------------------
# 1. Font
# --------------------------------------------------------------------------

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = os.path.join(REPO_ROOT, "assets", "fonts")
FONT_REG = "DejaVuSans"
FONT_BOLD = "DejaVuSans-Bold"
FONT_IT = "DejaVuSans-Oblique"
FONT_BIT = "DejaVuSans-BoldOblique"


def register_fonts() -> None:
    pdfmetrics.registerFont(TTFont(FONT_REG, os.path.join(FONT_DIR, "DejaVuSans.ttf")))
    pdfmetrics.registerFont(TTFont(FONT_BOLD, os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")))
    pdfmetrics.registerFont(TTFont(FONT_IT, os.path.join(FONT_DIR, "DejaVuSans-Oblique.ttf")))
    pdfmetrics.registerFont(TTFont(FONT_BIT, os.path.join(FONT_DIR, "DejaVuSans-BoldOblique.ttf")))
    pdfmetrics.registerFontFamily(
        FONT_REG, normal=FONT_REG, bold=FONT_BOLD, italic=FONT_IT, boldItalic=FONT_BIT
    )


# --------------------------------------------------------------------------
# 2. Màu sắc
# --------------------------------------------------------------------------

INK = colors.HexColor("#1B2430")
MUTED = colors.HexColor("#5A6675")
PRIMARY = colors.HexColor("#0B4F8A")
PRIMARY_DARK = colors.HexColor("#083A66")
PRIMARY_SOFT = colors.HexColor("#EAF1F8")
ACCENT = colors.HexColor("#C2410C")
ACCENT_SOFT = colors.HexColor("#FDEEE6")
GREEN = colors.HexColor("#166534")
GREEN_SOFT = colors.HexColor("#EAF5EE")
AMBER = colors.HexColor("#92400E")
AMBER_SOFT = colors.HexColor("#FDF4E3")
TEAL = colors.HexColor("#0F5F63")
TEAL_SOFT = colors.HexColor("#E7F4F4")
PURPLE = colors.HexColor("#4C1D95")
PURPLE_SOFT = colors.HexColor("#F1ECFB")
BORDER = colors.HexColor("#D3DCE6")
ZEBRA = colors.HexColor("#F6F8FB")
WHITE = colors.white

PAGE_W, PAGE_H = A4
MARGIN_X = 17 * mm
MARGIN_TOP = 21 * mm
MARGIN_BOT = 17 * mm
CONTENT_W = PAGE_W - 2 * MARGIN_X

# --------------------------------------------------------------------------
# 3. Kiểu chữ
# --------------------------------------------------------------------------

register_fonts()

STYLES: dict[str, ParagraphStyle] = {}


def _style(name: str, **kw) -> ParagraphStyle:
    base = dict(
        fontName=FONT_REG,
        fontSize=10,
        leading=15,
        textColor=INK,
        alignment=TA_JUSTIFY,
        spaceBefore=0,
        spaceAfter=0,
        allowWidows=1,
        allowOrphans=1,
        splitLongWords=1,
    )
    base.update(kw)
    STYLES[name] = ParagraphStyle(name, **base)
    return STYLES[name]


_style("body")
_style("body_tight", spaceAfter=2)
_style("lead", fontSize=10.6, leading=16.5, textColor=colors.HexColor("#26313F"))
_style("small", fontSize=8.6, leading=12.4)
_style("tiny", fontSize=7.8, leading=11)
_style("caption", fontSize=8.4, leading=11.5, textColor=MUTED, alignment=TA_CENTER)
_style("bullet", leftIndent=12, bulletIndent=2, spaceAfter=2.6)
_style("bullet_small", leftIndent=12, bulletIndent=2, fontSize=9.2, leading=13.4, spaceAfter=2)
_style("h1", fontName=FONT_BOLD, fontSize=16.5, leading=21, textColor=PRIMARY_DARK,
       alignment=TA_LEFT, spaceBefore=4, spaceAfter=8, keepWithNext=1)
_style("h2", fontName=FONT_BOLD, fontSize=12.8, leading=17, textColor=PRIMARY,
       alignment=TA_LEFT, spaceBefore=10, spaceAfter=5, keepWithNext=1)
_style("h3", fontName=FONT_BOLD, fontSize=10.8, leading=15, textColor=colors.HexColor("#1F3B57"),
       alignment=TA_LEFT, spaceBefore=7, spaceAfter=3, keepWithNext=1)
_style("h4", fontName=FONT_BOLD, fontSize=9.8, leading=13.5, textColor=TEAL,
       alignment=TA_LEFT, spaceBefore=4, spaceAfter=2, keepWithNext=1)
_style("box_title", fontName=FONT_BOLD, fontSize=9.2, leading=12.5, alignment=TA_LEFT)
_style("box_body", fontSize=9.4, leading=13.8, alignment=TA_JUSTIFY)
_style("formula", fontSize=10.6, leading=15.5, alignment=TA_CENTER, textColor=PRIMARY_DARK)
_style("formula_note", fontSize=8.4, leading=11.5, alignment=TA_CENTER, textColor=MUTED)
_style("table_head", fontName=FONT_BOLD, fontSize=8.4, leading=11, textColor=WHITE,
       alignment=TA_CENTER)
_style("table_cell", fontSize=8.6, leading=11.8, alignment=TA_LEFT)
_style("table_cell_c", fontSize=8.6, leading=11.8, alignment=TA_CENTER)
_style("toc0", fontName=FONT_BOLD, fontSize=10.2, leading=17, textColor=PRIMARY_DARK)
_style("toc1", fontSize=9.2, leading=14.4, textColor=INK, leftIndent=12)
_style("toc2", fontSize=8.6, leading=13, textColor=MUTED, leftIndent=26)
_style("question", fontSize=10, leading=15.4, alignment=TA_JUSTIFY)
_style("option", fontSize=9.6, leading=13.6, alignment=TA_LEFT)
_style("answer", fontSize=9.4, leading=14.2, alignment=TA_JUSTIFY)
_style("cover_kicker", fontName=FONT_BOLD, fontSize=9.5, leading=13, textColor=PRIMARY,
       alignment=TA_CENTER)
_style("cover_title", fontName=FONT_BOLD, fontSize=27, leading=33, textColor=PRIMARY_DARK,
       alignment=TA_CENTER)
_style("cover_sub", fontSize=12.5, leading=18, textColor=INK, alignment=TA_CENTER)
_style("cover_note", fontSize=9, leading=13, textColor=MUTED, alignment=TA_CENTER)

# --------------------------------------------------------------------------
# 4. Bộ chuyển đổi ký hiệu: {b}...{/b} -> <b>...</b>, tự động escape < > &
# --------------------------------------------------------------------------

TAG_MAP = {
    "{b}": "<b>", "{/b}": "</b>",
    "{i}": "<i>", "{/i}": "</i>",
    "{u}": "<u>", "{/u}": "</u>",
    "{sup}": "<super>", "{/sup}": "</super>",
    "{sub}": "<sub>", "{/sub}": "</sub>",
    "{br}": "<br/>",
    "{red}": f'<font color="#B91C1C">', "{/red}": "</font>",
    "{blue}": f'<font color="#0B4F8A">', "{/blue}": "</font>",
    "{green}": f'<font color="#166534">', "{/green}": "</font>",
    "{orange}": f'<font color="#C2410C">', "{/orange}": "</font>",
    "{gray}": f'<font color="#5A6675">', "{/gray}": "</font>",
    "{teal}": f'<font color="#0F5F63">', "{/teal}": "</font>",
}


def rt(text: str) -> str:
    """Escape an toàn rồi chuyển các "tag" dạng {b} sang markup của ReportLab."""
    out = html.escape(str(text), quote=False)
    for key, val in TAG_MAP.items():
        out = out.replace(key, val)
    return out


def P(text: str, style: str = "body", **kw) -> Paragraph:
    return Paragraph(rt(text), STYLES[style], **kw)


def SP(h: float = 4) -> Spacer:
    return Spacer(1, h)


def rule(color=BORDER, thickness=0.7, space_before=2, space_after=6) -> Table:
    t = Table([[""]], colWidths=[CONTENT_W], rowHeights=[0.1])
    t.setStyle(TableStyle([
        ("LINEBELOW", (0, 0), (-1, -1), thickness, color),
        ("TOPPADDING", (0, 0), (-1, -1), space_before),
        ("BOTTOMPADDING", (0, 0), (-1, -1), space_after),
    ]))
    return t


def bullets(items, style: str = "bullet", symbol: str = "•") -> ListFlowable:
    return ListFlowable(
        [ListItem(P(it, style), leftIndent=12, value="circle") for it in items],
        bulletType="bullet",
        start=symbol,
        leftIndent=12,
        bulletFontName=FONT_REG,
        bulletFontSize=8,
        bulletColor=PRIMARY,
        spaceBefore=1,
        spaceAfter=3,
    )


def numbered(items, style: str = "body") -> ListFlowable:
    return ListFlowable(
        [ListItem(P(it, style), leftIndent=16) for it in items],
        bulletType="1",
        bulletFormat="%s.",
        leftIndent=16,
        bulletFontName=FONT_BOLD,
        bulletFontSize=9,
        bulletColor=PRIMARY,
        spaceBefore=1,
        spaceAfter=3,
    )


# --------------------------------------------------------------------------
# 5. Tiêu đề có đánh dấu mục lục
# --------------------------------------------------------------------------

def H1(text: str, level: int | None = 0) -> Paragraph:
    p = P(text, "h1")
    if level is not None:
        p._toc_level = level
    return p


def H2(text: str, level: int = 1) -> Paragraph:
    p = P(text, "h2")
    p._toc_level = level
    return p


def H3(text: str) -> Paragraph:
    return P(text, "h3")


def H4(text: str) -> Paragraph:
    return P(text, "h4")


# --------------------------------------------------------------------------
# 6. Hộp nội dung (ghi nhớ / ví dụ / lỗi / mẹo)
# --------------------------------------------------------------------------

BOX_KINDS = {
    "note": ("GHI NHỚ", PRIMARY, PRIMARY_SOFT),
    "example": ("VÍ DỤ MẪU", GREEN, GREEN_SOFT),
    "warn": ("LỖI THƯỜNG GẶP", ACCENT, ACCENT_SOFT),
    "tip": ("MẸO & KINH NGHIỆM", TEAL, TEAL_SOFT),
    "method": ("PHƯƠNG PHÁP", PURPLE, PURPLE_SOFT),
    "exam": ("LƯU Ý KHI LÀM BÀI", AMBER, AMBER_SOFT),
}


def box(kind: str, content, title: str | None = None) -> Table:
    """Hộp nội dung. Mỗi phần tử trong ``content`` là một dòng của bảng để hộp
    có thể ngắt trang khi dài, thay vì đẩy cả khối sang trang sau."""
    default_title, color, bg = BOX_KINDS[kind]
    if title is None:
        title = default_title
    if isinstance(content, str):
        content = [P(content, "box_body")]
    elif not isinstance(content, (list, tuple)):
        content = [content]

    if title:
        head = Paragraph(
            f'<font color="#{color.hexval()[2:]}">{html.escape(title)}</font>', STYLES["box_title"]
        )
        rows = [[head], [SP(2.5)]] + [[item] for item in content]
    else:
        rows = [[item] for item in content]
    t = Table(rows, colWidths=[CONTENT_W], splitByRow=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (0, -1), 2.6, color),
        ("BOX", (0, 0), (-1, -1), 0.5,
         colors.Color(color.red, color.green, color.blue, 0.25)),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, 0), 7),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 8),
        ("TOPPADDING", (0, 1), (-1, -1), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -2), 1),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    # Hộp ngắn: giữ nguyên khối để không bị cắt vụn ở cuối trang.
    try:
        h = t.wrap(CONTENT_W, PAGE_H)[1]
    except Exception:
        h = 0
    if h < 430:
        return KeepTogether([t])
    return t


def formula(text, note: str | None = None) -> Table:
    """Khối công thức. ``text`` có thể là chuỗi hoặc danh sách chuỗi (mỗi dòng
    một công thức) – dạng danh sách dễ đọc hơn khi có nhiều công thức."""
    def _keep_spaces(line: str) -> str:
        # Paragraph gộp khoảng trắng liên tiếp; dùng NBSP để giữ căn công thức.
        return re.sub(r"  +", lambda m: "\u00a0" * len(m.group(0)), rt(line))

    if isinstance(text, (list, tuple)):
        body = "<br/>".join(_keep_spaces(line) for line in text)
    else:
        body = _keep_spaces(text)
    cells = [[Paragraph(body, STYLES["formula"])]]
    if note:
        cells.append([P(note, "formula_note")])
    t = Table(cells, colWidths=[CONTENT_W - 6])
    style = [
        ("BOX", (0, 0), (-1, -1), 0.5, BORDER),
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FAFCFF")),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]
    t.setStyle(TableStyle(style))
    outer = Table([[t]], colWidths=[CONTENT_W])
    outer.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return outer


# --------------------------------------------------------------------------
# 7. Bảng biểu
# --------------------------------------------------------------------------

def tbl(rows, widths, header: bool = True, fontsize: float = 8.6, align=None,
        zebra: bool = True, header_bg=PRIMARY, first_col_bold: bool = False,
        row_colors=None, valign="MIDDLE") -> Table:
    """rows: list[list[str | list[str]]]; ô có thể chứa nhiều dòng bằng \\n."""
    cell_style = ParagraphStyle(
        "tc", parent=STYLES["table_cell"], fontSize=fontsize,
        leading=fontsize * 1.36,
    )
    head_style = ParagraphStyle(
        "th", parent=STYLES["table_head"], fontSize=fontsize - 0.2,
        leading=(fontsize - 0.2) * 1.3,
    )
    data = []
    for r_i, row in enumerate(rows):
        out_row = []
        for c_i, cell in enumerate(row):
            if isinstance(cell, (Paragraph, Table, Flowable)):
                out_row.append(cell)
                continue
            st = head_style if (header and r_i == 0) else cell_style
            if align and not (header and r_i == 0):
                st = ParagraphStyle(
                    "tca", parent=st,
                    alignment={"c": TA_CENTER, "l": TA_LEFT, "r": TA_RIGHT}[align[c_i]],
                )
            if first_col_bold and c_i == 0 and r_i > 0:
                st = ParagraphStyle("tcb", parent=st, fontName=FONT_BOLD)
            text = str(cell)
            out_row.append(Paragraph(rt(text), st))
        data.append(out_row)

    t = Table(data, colWidths=widths, repeatRows=1 if header else 0, hAlign="LEFT")
    cmds = [
        ("GRID", (0, 0), (-1, -1), 0.4, BORDER),
        ("VALIGN", (0, 0), (-1, -1), valign),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5),
    ]
    if header:
        cmds += [
            ("BACKGROUND", (0, 0), (-1, 0), header_bg),
            ("LINEBELOW", (0, 0), (-1, 0), 0.8, PRIMARY_DARK),
        ]
    if zebra:
        for i in range(1 if header else 0, len(data)):
            if (i % 2 == 0):
                cmds.append(("BACKGROUND", (0, i), (-1, i), ZEBRA))
    if row_colors:
        for idx, col in row_colors.items():
            cmds.append(("BACKGROUND", (0, idx), (-1, idx), col))
    t.setStyle(TableStyle(cmds))
    return t


# --------------------------------------------------------------------------
# 8. Hình vẽ
# --------------------------------------------------------------------------

class _Fig(Flowable):
    def __init__(self, width, height, caption: str | None = None):
        super().__init__()
        self.width = width
        self.height = height
        self.caption = caption

    CAPTION_H = 13

    def draw(self):
        c = self.canv
        c.saveState()
        if self.caption:
            c.translate(0, self.CAPTION_H)
        self.paint(c)
        c.restoreState()
        if self.caption:
            c.setFont(FONT_REG, 7.6)
            c.setFillColor(MUTED)
            # cho phép xuống dòng khi chú thích dài
            y = 3 + 9 * (len(self._caption_lines()) - 1)
            for line in self._caption_lines():
                c.drawCentredString(self.width / 2, y, line)
                y -= 9

    def _caption_lines(self) -> list:
        if not getattr(self, "_cap_cache", None):
            from reportlab.lib.utils import simpleSplit
            # chú thích được phép rộng hơn hình (vẫn nằm trong khung nội dung)
            wrap_w = max(self.width - 8, min(330, CONTENT_W - 40))
            plain = re.sub(r"\{/?[a-z]+\}", "", self.caption or "")
            self._cap_cache = simpleSplit(plain, FONT_REG, 7.6, wrap_w) or [""]
        return self._cap_cache

    def wrap(self, aw, ah):
        extra = 0
        if self.caption:
            extra = max(self.CAPTION_H, 8 + 9 * len(self._caption_lines()))
        return self.width, self.height + extra


class VennFig(_Fig):
    """Hai đường tròn giao nhau, tô phần tương ứng với phép toán tập hợp."""

    def __init__(self, shade="intersection", caption=None, label_a="A", label_b="B"):
        super().__init__(168, 104, caption)
        self.shade = shade
        self.label_a = label_a
        self.label_b = label_b

    def paint(self, c):
        r = 34
        c1x, c2x, cy = 60, 108, 48
        c.setLineWidth(1.1)
        c.setStrokeColor(PRIMARY_DARK)
        c.setFillColor(PRIMARY_SOFT)

        def circle(x):
            p = c.beginPath()
            p.circle(x, cy, r)
            return p

        if self.shade == "union":
            for x in (c1x, c2x):
                c.setFillColor(colors.HexColor("#CFE3F7"))
                c.drawPath(circle(x), stroke=0, fill=1)
        elif self.shade == "intersection":
            c.saveState()
            c.clipPath(circle(c1x), stroke=0, fill=0)
            c.setFillColor(colors.HexColor("#8FC3EC"))
            c.drawPath(circle(c2x), stroke=0, fill=1)
            c.restoreState()
        elif self.shade == "difference":
            c.saveState()
            c.clipPath(circle(c1x), stroke=0, fill=0)
            c.setFillColor(colors.HexColor("#8FC3EC"))
            c.drawPath(circle(c1x), stroke=0, fill=1)
            c.setFillColor(colors.white)
            c.drawPath(circle(c2x), stroke=0, fill=1)
            c.restoreState()

        c.setFillColor(colors.white if self.shade == "intersection" else colors.white)
        c.setStrokeColor(PRIMARY_DARK)
        for x in (c1x, c2x):
            c.drawPath(circle(x), stroke=1, fill=0)

        c.setFont(FONT_BOLD, 10)
        c.setFillColor(PRIMARY_DARK)
        c.drawString(c1x - r - 2, cy + r + 4, self.label_a)
        c.drawString(c2x + r - 6, cy + r + 4, self.label_b)


class NumberLineFig(_Fig):
    """Trục số với các đoạn/khoảng tô màu theo từng hàng."""

    def __init__(self, rows, xmin, xmax, caption=None, width=430):
        super().__init__(width, 42 + 24 * len(rows), caption)
        self.rows = rows  # list of dict(start, end, label, color, closed_left, closed_right)
        self.xmin = xmin
        self.xmax = xmax

    def paint(self, c):
        width = self.width
        left, right = 46, width - 18
        span = self.xmax - self.xmin
        axis_y = 22
        row0_y = axis_y + 26

        def X(v):
            return left + (v - self.xmin) / span * (right - left)

        # trục
        c.setStrokeColor(colors.HexColor("#6B7280"))
        c.setLineWidth(0.9)
        c.line(left - 12, axis_y, right + 12, axis_y)
        p = c.beginPath()
        p.moveTo(right + 12, axis_y)
        p.lineTo(right + 5, axis_y + 3)
        p.lineTo(right + 5, axis_y - 3)
        p.close()
        c.setFillColor(colors.HexColor("#6B7280"))
        c.drawPath(p, stroke=0, fill=1)
        c.setFont(FONT_REG, 7.6)
        c.setFillColor(MUTED)
        c.drawRightString(left - 15, axis_y - 3, "x")

        for i, row in enumerate(self.rows):
            y = row0_y + 20 * (len(self.rows) - 1 - i)
            x1, x2 = X(row["start"]), X(row["end"])
            col = row.get("color", PRIMARY)
            c.setStrokeColor(col)
            c.setLineWidth(3.2)
            c.line(x1, y, x2, y)
            # đầu mút
            for xv, closed in ((x1, row.get("closed_left", True)),
                               (x2, row.get("closed_right", False))):
                c.setLineWidth(1.3)
                if closed:
                    c.setFillColor(col)
                    c.circle(xv, y, 2.2, stroke=1, fill=1)
                else:
                    c.setFillColor(colors.white)
                    c.circle(xv, y, 2.2, stroke=1, fill=1)
            c.setFont(FONT_BOLD, 8)
            c.setFillColor(INK)
            c.drawRightString(left - 10, y - 2.8, row.get("label", ""))

        # nhãn giá trị các đầu mút (dưới trục, so le hai mức để không đè nhau)
        c.setFont(FONT_REG, 6.6)
        c.setFillColor(MUTED)
        seen = {}
        for row in self.rows:
            for k, xv in ((0, row["start"]), (1, row["end"])):
                key = round(xv, 3)
                if key in seen:
                    continue
                seen[key] = 1
                yoff = -11 if (int(abs(key) * 7) % 2 == 0) else -18
                c.drawCentredString(X(xv), axis_y + yoff, f"{xv:g}")

        # vạch chia quanh 0
        c.setStrokeColor(colors.HexColor("#9CA3AF"))
        c.setLineWidth(0.6)


class FeasibleFig(_Fig):
    """Miền nghiệm của hệ bất phương trình (đa giác lồi) trên hệ trục Oxy."""

    def __init__(self, lines, vertices, xmax, ymax, caption=None,
                 vertex_labels=None, width=250, height=200, x0=0, y0=0):
        super().__init__(width, height, caption)
        self.lines = lines  # list of (A,B,C) cho Ax+By=C
        self.vertices = vertices
        self.xmax = xmax
        self.ymax = ymax
        self.vertex_labels = vertex_labels or []
        self.x0, self.y0 = x0, y0

    @staticmethod
    def _step(span):
        raw = span / 8.0
        for cand in (1, 2, 2.5, 5, 10, 20, 25, 50):
            if raw <= cand:
                return cand
        return 100

    def paint(self, c):
        left, bottom = 34, 24
        right, top = self.width - 16, self.height - 16
        sx = (right - left) / (self.xmax - self.x0)
        sy = (top - bottom) / (self.ymax - self.y0)

        def X(v):
            return left + (v - self.x0) * sx

        def Y(v):
            return bottom + (v - self.y0) * sy

        step_x = self._step(self.xmax - self.x0)
        step_y = self._step(self.ymax - self.y0)

        # lưới mảnh
        c.setStrokeColor(colors.HexColor("#E8EDF3"))
        c.setLineWidth(0.4)
        gx = self.x0
        while gx <= self.xmax + 1e-9:
            c.line(X(gx), bottom, X(gx), top)
            gx += step_x
        gy = self.y0
        while gy <= self.ymax + 1e-9:
            c.line(left, Y(gy), right, Y(gy))
            gy += step_y

        # miền nghiệm
        p = c.beginPath()
        p.moveTo(X(self.vertices[0][0]), Y(self.vertices[0][1]))
        for v in self.vertices[1:]:
            p.lineTo(X(v[0]), Y(v[1]))
        p.close()
        c.setFillColor(colors.HexColor("#BFD8EE"))
        c.setStrokeColor(PRIMARY)
        c.setLineWidth(1.0)
        c.drawPath(p, stroke=1, fill=1)

        # đường biên (cắt trong khung hình)
        for (A, B, C) in self.lines:
            pts = []
            if abs(B) > 1e-12:
                for x in (self.x0, self.xmax):
                    y = (C - A * x) / B
                    if self.y0 - 1e-9 <= y <= self.ymax + 1e-9:
                        pts.append((x, y))
            if abs(A) > 1e-12:
                for y in (self.y0, self.ymax):
                    x = (C - B * y) / A
                    if self.x0 - 1e-9 <= x <= self.xmax + 1e-9:
                        pts.append((x, y))
            uniq = []
            for pt in pts:
                if not any(abs(pt[0] - q[0]) < 1e-6 and abs(pt[1] - q[1]) < 1e-6 for q in uniq):
                    uniq.append(pt)
            if len(uniq) >= 2:
                c.setStrokeColor(PRIMARY_DARK)
                c.setLineWidth(0.9)
                c.line(X(uniq[0][0]), Y(uniq[0][1]), X(uniq[1][0]), Y(uniq[1][1]))

        # trục toạ độ
        c.setStrokeColor(INK)
        c.setLineWidth(0.9)
        if self.y0 <= 0 <= self.ymax:
            c.line(left, Y(0), right + 4, Y(0))
            c.setFont(FONT_REG, 7.4)
            c.setFillColor(INK)
            c.drawRightString(right + 3, Y(0) - 9, "x")
        if self.x0 <= 0 <= self.xmax:
            c.line(X(0), bottom, X(0), top + 4)
            c.setFont(FONT_REG, 7.4)
            c.setFillColor(INK)
            c.drawString(X(0) + 4, top, "y")
        c.setFont(FONT_REG, 7)
        c.setFillColor(MUTED)
        c.drawString(X(0) - 9, Y(0) - 10, "O")

        # vạch chia
        c.setFont(FONT_REG, 6.4)
        c.setFillColor(MUTED)
        gx = self.x0
        while gx <= self.xmax + 1e-9:
            if abs(gx) > 1e-9:
                c.drawCentredString(X(gx), Y(0) - 8, f"{gx:g}")
            gx += step_x
        gy = self.y0
        while gy <= self.ymax + 1e-9:
            if abs(gy) > 1e-9:
                c.drawRightString(X(0) - 3, Y(gy) - 2, f"{gy:g}")
            gy += step_y

        # đỉnh
        for idx, (vx, vy) in enumerate(self.vertices):
            c.setFillColor(ACCENT)
            c.circle(X(vx), Y(vy), 2.2, stroke=0, fill=1)
            label = self.vertex_labels[idx] if idx < len(self.vertex_labels) else ""
            if label:
                c.setFont(FONT_BOLD, 7.4)
                c.setFillColor(ACCENT)
                c.drawString(X(vx) + 5, Y(vy) + 6, label)


class HeightFig(_Fig):
    """Sơ đồ đo chiều cao gián tiếp: A, B trên mặt đất, C chân tháp, T đỉnh."""

    def __init__(self, caption=None, width=330, height=178):
        super().__init__(width, height, caption)

    def paint(self, c):
        from math import atan, degrees
        base = 30
        h = 104
        cx = 262
        ax = cx - int(round(h / 0.5774))   # tan 30°
        bx = cx - int(round(h / 1.7321))   # tan 60°
        ttop = base + h
        c.setStrokeColor(colors.HexColor("#CBD5E1"))
        c.setLineWidth(1.2)
        c.line(10, base, self.width - 12, base)
        c.setStrokeColor(PRIMARY_DARK)
        c.setLineWidth(1)
        c.line(ax, base, cx, base)
        c.line(ax, base, cx, ttop)
        c.line(bx, base, cx, ttop)
        c.setFillColor(colors.HexColor("#E8EEF6"))
        c.rect(cx, base, 12, ttop - base, stroke=1, fill=1)
        c.setStrokeColor(PRIMARY_DARK)
        c.setLineWidth(0.7)
        c.line(cx - 7, base, cx - 7, base + 7)
        c.line(cx - 7, base + 7, cx, base + 7)
        # góc nâng (dùng atan để vẽ đúng độ lớn)
        ang_a = degrees(atan(h / (cx - ax)))
        ang_b = degrees(atan(h / (cx - bx)))
        c.setStrokeColor(ACCENT)
        c.setLineWidth(0.9)
        c.arc(ax - 30, base - 30, ax + 30, base + 30, 0, ang_a)
        c.arc(bx - 30, base - 30, bx + 30, base + 30, ang_b, 180 - ang_b)
        c.setFont(FONT_BOLD, 9)
        c.setFillColor(INK)
        c.drawString(ax - 11, base - 12, "A")
        c.drawString(bx - 10, base - 12, "B")
        c.drawString(cx + 15, base - 4, "C")
        c.drawString(cx + 2, ttop + 3, "T")
        c.setFont(FONT_BOLD, 7.8)
        c.setFillColor(ACCENT)
        c.drawCentredString((ax + bx) / 2, base - 13, "30 m")
        c.setFont(FONT_REG, 7.4)
        c.setFillColor(ACCENT)
        c.drawCentredString((bx + cx) / 2, base - 13, "x")
        c.setFont(FONT_REG, 7.4)
        c.setFillColor(MUTED)
        c.drawString(ax + 14, base + 5, f"{ang_a:.0f}°")
        c.drawRightString(bx - 6, base + 5, f"{ang_b:.0f}°")
        c.setFont(FONT_REG, 7.4)
        c.setFillColor(PRIMARY_DARK)
        c.drawString(cx + 16, (base + ttop) / 2, "h")
        c.setFont(FONT_REG, 6.8)
        c.setFillColor(MUTED)
        c.drawString(18, base + h / 2, "mặt đất")


class ParallelogramFig(_Fig):
    def __init__(self, caption=None, width=190, height=96):
        super().__init__(width, height, caption)

    def paint(self, c):
        A, B, C, D = (22, 26), (128, 26), (160, 74), (54, 74)
        c.setStrokeColor(PRIMARY_DARK)
        c.setLineWidth(1.0)
        c.setFillColor(colors.HexColor("#EDF3FA"))
        p = c.beginPath()
        p.moveTo(*A); p.lineTo(*B); p.lineTo(*C); p.lineTo(*D); p.close()
        c.drawPath(p, stroke=1, fill=1)
        c.setFont(FONT_BOLD, 9)
        c.setFillColor(INK)
        for label, (x, y) in {"A": A, "B": B, "C": C, "D": D}.items():
            dx = -12 if label in "AD" else 4
            c.drawString(x + dx, y + (4 if label in "AB" else -2), label)


# --------------------------------------------------------------------------
# 9. Khung trang, trang bìa, tài liệu
# --------------------------------------------------------------------------

DOC_TITLE = "Đề cương ôn tập Giữa kì I – Toán 10"


def _footer(c: pdfcanvas.Canvas, doc):
    if doc.page == 1:  # trang bìa không đánh số
        return
    c.saveState()
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.6)
    c.line(MARGIN_X, MARGIN_BOT - 6 * mm, PAGE_W - MARGIN_X, MARGIN_BOT - 6 * mm)
    c.setFont(FONT_REG, 7.4)
    c.setFillColor(MUTED)
    c.drawString(MARGIN_X, MARGIN_BOT - 10.5 * mm, DOC_TITLE)
    total = getattr(doc, "_total_pages", None) or "?"
    c.drawRightString(PAGE_W - MARGIN_X, MARGIN_BOT - 10.5 * mm, f"Trang {doc.page}/{total}")
    c.restoreState()


def _header(c: pdfcanvas.Canvas, doc):
    c.saveState()
    c.setFont(FONT_BOLD, 7.2)
    c.setFillColor(colors.HexColor("#8A97A6"))
    c.drawString(MARGIN_X, PAGE_H - 13 * mm, "TOÁN 10 · KẾT NỐI TRI THỨC VỚI CUỘC SỐNG")
    c.drawRightString(PAGE_W - MARGIN_X, PAGE_H - 13 * mm, "GIỮA HỌC KÌ I · 2026–2027")
    c.setStrokeColor(colors.HexColor("#E2E8F0"))
    c.setLineWidth(0.5)
    c.line(MARGIN_X, PAGE_H - 14.6 * mm, PAGE_W - MARGIN_X, PAGE_H - 14.6 * mm)
    c.restoreState()


class GuideDoc(BaseDocTemplate):
    def __init__(self, filename, **kw):
        super().__init__(filename, pagesize=A4, **kw)
        self._seq = 0

    def afterFlowable(self, flowable):
        level = getattr(flowable, "_toc_level", None)
        if level is None:
            return
        text = flowable.getPlainText()
        self.notify("TOCEntry", (level, text, self.page))
        key = f"h{self._seq}"
        self._seq += 1
        self.canv.bookmarkPage(key)
        try:
            self.canv.addOutlineEntry(text, key, level=level, closed=(level > 0))
        except Exception:
            pass


def build_doc(path: str) -> GuideDoc:
    doc = GuideDoc(
        path,
        leftMargin=MARGIN_X,
        rightMargin=MARGIN_X,
        topMargin=MARGIN_TOP,
        bottomMargin=MARGIN_BOT,
        title="Đề cương ôn tập Giữa học kì I – Toán 10 (Kết nối tri thức)",
        author="Biên soạn từ Ma trận đề kiểm tra Giữa kì I 2026–2027",
        subject="Toán 10 – Mệnh đề, tập hợp; bất phương trình bậc nhất hai ẩn; hệ thức lượng; vectơ",
    )
    cover_frame = Frame(MARGIN_X, MARGIN_BOT, CONTENT_W, PAGE_H - MARGIN_TOP - MARGIN_BOT,
                        id="cover", leftPadding=0, rightPadding=0,
                        topPadding=0, bottomPadding=0)
    content_frame = Frame(MARGIN_X, MARGIN_BOT, CONTENT_W,
                          PAGE_H - MARGIN_TOP - MARGIN_BOT, id="content",
                          leftPadding=0, rightPadding=0,
                          topPadding=0, bottomPadding=0)
    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[cover_frame]),
        PageTemplate(id="content", frames=[content_frame],
                     onPage=_header, onPageEnd=None),
    ])
    # footer chạy cả hai loại trang
    for pt in doc.pageTemplates:
        pt.onPageEnd = _footer
    return doc
