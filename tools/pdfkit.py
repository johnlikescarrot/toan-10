# -*- coding: utf-8 -*-
"""Bộ công cụ dựng PDF cho đề cương (ReportLab Platypus).

Cung cấp: đăng ký font, bảng màu, các style, và một số flowable tuỳ biến
(hộp ghi nhớ, hộp công thức, banner chương, bảng số liệu, hình vẽ).
"""
from __future__ import annotations

import os
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Flowable, KeepTogether, Paragraph, Spacer, Table, TableStyle,
)
from reportlab.platypus.flowables import HRFlowable

ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = ROOT / "assets" / "fonts"

# --------------------------------------------------------------------------
# Xử lý markup an toàn: cho phép viết "<", ">" trong công thức toán
# --------------------------------------------------------------------------
import re as _re

_TAG_RE = _re.compile(
    r"</?(?:b|i|u|s|br|sub|super|font|span|link|a|img)(?:\s[^<>]*)?/?>",
    _re.IGNORECASE,
)
_ENT_RE = _re.compile(r"&(?!#?\w+;)")


def esc(text: str) -> str:
    """Escape ký tự <, >, & nhưng giữ nguyên các thẻ định dạng hợp lệ."""
    if not isinstance(text, str):
        return text
    out, pos = [], 0
    for m in _TAG_RE.finditer(text):
        out.append(_esc_plain(text[pos:m.start()]))
        out.append(m.group(0))
        pos = m.end()
    out.append(_esc_plain(text[pos:]))
    return "".join(out)


def _esc_plain(s: str) -> str:
    s = _ENT_RE.sub("&amp;", s)
    return s.replace("<", "&lt;").replace(">", "&gt;")


# --------------------------------------------------------------------------
# Font
# --------------------------------------------------------------------------
FONT = "DejaVu"
FONT_B = "DejaVu-Bold"
FONT_I = "DejaVu-Oblique"
FONT_BI = "DejaVu-BoldOblique"
FONT_MONO = "DejaVu-Mono"


def register_fonts() -> None:
    mapping = {
        FONT: "DejaVuSans.ttf",
        FONT_B: "DejaVuSans-Bold.ttf",
        FONT_I: "DejaVuSans-Oblique.ttf",
        FONT_BI: "DejaVuSans-BoldOblique.ttf",
        FONT_MONO: "DejaVuSansMono.ttf",
    }
    for alias, fname in mapping.items():
        path = FONT_DIR / fname
        if not path.exists():  # pragma: no cover
            raise SystemExit(f"Thiếu font: {path}")
        pdfmetrics.registerFont(TTFont(alias, str(path)))
    pdfmetrics.registerFontFamily(
        FONT, normal=FONT, bold=FONT_B, italic=FONT_I, boldItalic=FONT_BI
    )


# --------------------------------------------------------------------------
# Bảng màu
# --------------------------------------------------------------------------
NAVY = colors.HexColor("#12355B")
BLUE = colors.HexColor("#1F4E79")
TEAL = colors.HexColor("#0E6E6B")
GOLD = colors.HexColor("#9C6500")
RED = colors.HexColor("#A33E30")
GREEN = colors.HexColor("#2E6B3E")
PURPLE = colors.HexColor("#5B3E90")

INK = colors.HexColor("#1A1A1A")
GREY = colors.HexColor("#5A6672")
LIGHT = colors.HexColor("#F4F6F8")
LINE = colors.HexColor("#C9D2DB")
TINT_BLUE = colors.HexColor("#EAF1F8")
TINT_GREEN = colors.HexColor("#EAF4EC")
TINT_GOLD = colors.HexColor("#FBF3DF")
TINT_RED = colors.HexColor("#FBECEA")
TINT_PURPLE = colors.HexColor("#F1EDF9")

PAGE_W, PAGE_H = A4
MARGIN_L = MARGIN_R = 1.9 * cm
MARGIN_T = 1.9 * cm
MARGIN_B = 1.8 * cm
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R


# --------------------------------------------------------------------------
# Styles
# --------------------------------------------------------------------------
def build_styles() -> dict[str, ParagraphStyle]:
    s: dict[str, ParagraphStyle] = {}

    s["body"] = ParagraphStyle(
        "body", fontName=FONT, fontSize=10.2, leading=15.4,
        alignment=TA_JUSTIFY, textColor=INK, spaceAfter=4,
    )
    s["body_c"] = ParagraphStyle("body_c", parent=s["body"], alignment=TA_CENTER)
    s["small"] = ParagraphStyle(
        "small", parent=s["body"], fontSize=8.6, leading=12.2, textColor=GREY
    )
    s["caption"] = ParagraphStyle(
        "caption", parent=s["body"], fontSize=8.4, leading=11.5,
        alignment=TA_CENTER, textColor=GREY, spaceBefore=2, spaceAfter=8,
    )
    s["bullet"] = ParagraphStyle(
        "bullet", parent=s["body"], leftIndent=13, bulletIndent=3,
        spaceAfter=2.5, alignment=TA_JUSTIFY,
    )
    s["bullet2"] = ParagraphStyle(
        "bullet2", parent=s["bullet"], leftIndent=27, bulletIndent=16,
        fontSize=9.9, leading=14.6,
    )
    s["h1"] = ParagraphStyle(
        "h1", fontName=FONT_B, fontSize=15.5, leading=20, textColor=colors.white,
    )
    s["h1_sub"] = ParagraphStyle(
        "h1_sub", fontName=FONT_I, fontSize=9.4, leading=13,
        textColor=colors.HexColor("#DCE6F2"),
    )
    s["h2"] = ParagraphStyle(
        "h2", fontName=FONT_B, fontSize=12.2, leading=17, textColor=NAVY,
        spaceBefore=13, spaceAfter=5,
    )
    s["h3"] = ParagraphStyle(
        "h3", fontName=FONT_B, fontSize=10.6, leading=15, textColor=TEAL,
        spaceBefore=9, spaceAfter=3,
    )
    s["h4"] = ParagraphStyle(
        "h4", fontName=FONT_B, fontSize=10.0, leading=14, textColor=INK,
        spaceBefore=6, spaceAfter=2,
    )
    s["formula"] = ParagraphStyle(
        "formula", fontName=FONT, fontSize=10.2, leading=16,
        alignment=TA_CENTER, textColor=INK, spaceBefore=3, spaceAfter=3,
    )
    s["cell"] = ParagraphStyle(
        "cell", fontName=FONT, fontSize=8.7, leading=11.8, textColor=INK,
    )
    s["cell_c"] = ParagraphStyle("cell_c", parent=s["cell"], alignment=TA_CENTER)
    s["cell_h"] = ParagraphStyle(
        "cell_h", fontName=FONT_B, fontSize=8.6, leading=11.5,
        alignment=TA_CENTER, textColor=colors.white,
    )
    s["cell_l"] = ParagraphStyle("cell_l", parent=s["cell"], alignment=TA_LEFT)
    s["q"] = ParagraphStyle(
        "q", fontName=FONT, fontSize=10.2, leading=15.2, textColor=INK,
        alignment=TA_JUSTIFY, spaceBefore=5, spaceAfter=2,
    )
    s["opt"] = ParagraphStyle(
        "opt", fontName=FONT, fontSize=9.9, leading=13.6, textColor=INK,
        leftIndent=16, bulletIndent=4, spaceAfter=1,
    )
    s["toc1"] = ParagraphStyle(
        "toc1", fontName=FONT_B, fontSize=9.7, leading=12.2, textColor=NAVY,
        spaceBefore=1.6,
    )
    s["toc2"] = ParagraphStyle(
        "toc2", fontName=FONT, fontSize=8.9, leading=10.6, textColor=INK,
        leftIndent=18, firstLineIndent=-2,
    )
    s["toc3"] = ParagraphStyle(
        "toc3", fontName=FONT, fontSize=9.0, leading=13, textColor=GREY,
        leftIndent=34,
    )
    return s


STY: dict[str, ParagraphStyle] = {}


def S(name) -> ParagraphStyle:
    if isinstance(name, ParagraphStyle):
        return name
    return STY[name]


class Heading(Paragraph):
    """Đoạn tiêu đề, có thể tự đăng ký vào mục lục và bookmark PDF."""

    def __init__(self, text, style, level=0, toc_text=None):
        super().__init__(esc(text), S(style))
        self.toc_level = level
        self.toc_text = toc_text if toc_text is not None else strip_tags(text)

    def _notoc(self):
        self.toc_text = None
        return self


_LEVELS = {"h1": 0, "h2": 1, "h3": 2}


def strip_tags(markup: str) -> str:
    out, depth = [], 0
    for ch in markup:
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth -= 1
        elif depth == 0:
            out.append(ch)
    return " ".join("".join(out).split())


def P(text: str, style: str = "body", **kw) -> Paragraph:
    if isinstance(style, str) and style in _LEVELS:
        h = Heading(text, style, level=_LEVELS[style])
        if _LEVELS[style] > 1:      # h3 không đưa vào mục lục
            h.toc_text = None
        return h
    return Paragraph(esc(text), S(style), **kw)


def bullets(items, style: str = "bullet", bullet: str = "•") -> list[Paragraph]:
    return [Paragraph(esc(t), S(style), bulletText=bullet) for t in items]


def numbered(items, style: str = "bullet") -> list[Paragraph]:
    out = []
    for i, t in enumerate(items, 1):
        out.append(Paragraph(esc(t), S(style), bulletText=f"{i}."))
    return out


# --------------------------------------------------------------------------
# Flowable tuỳ biến
# --------------------------------------------------------------------------
class Rule(Flowable):
    """Đường kẻ ngang mảnh."""

    def __init__(self, width=CONTENT_W, color=LINE, thickness=0.6, space=3):
        super().__init__()
        self.width, self.color = width, color
        self.thickness, self.space = thickness, space
        self.height = thickness + 2 * space

    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, self.space, self.width, self.space)


def callout(title: str, body: list, color=TEAL, bg=TINT_GREEN,
            icon: str = "", width=CONTENT_W) -> Table:
    """Hộp ghi nhớ / công thức với thanh màu bên trái."""
    head = ""
    if title:
        head = (
            f'<font name="{FONT_B}" size="9.6" color="{color.hexval().replace("0x", "#")}">'
            f"{icon + ' ' if icon else ''}{title}</font>"
        )
    inner = []
    if head:
        inner.append(Paragraph(head, ParagraphStyle("h", fontName=FONT, fontSize=9.6,
                                                    leading=13, spaceAfter=3)))
    inner.extend(body)
    t = Table([[inner]], colWidths=[width])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (0, -1), 2.6, color),
        ("BOX", (0, 0), (-1, -1), 0.4, color),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return t


def note(body, color=BLUE, bg=TINT_BLUE, title="Ghi nhớ", icon="★") -> Table:
    return callout(title, body, color=color, bg=bg, icon=icon)


def warn(body, title="Lỗi thường gặp", icon="⚠") -> Table:
    return callout(title, body, color=RED, bg=TINT_RED, icon=icon)


def tip(body, title="Mẹo / Kinh nghiệm", icon="✦") -> Table:
    return callout(title, body, color=GOLD, bg=TINT_GOLD, icon=icon)


def method(body, title="Phương pháp giải", icon="◆") -> Table:
    return callout(title, body, color=PURPLE, bg=TINT_PURPLE, icon=icon)


class ChapterBanner(Flowable):
    """Banner đầu chương: khối màu đặc, số chương lớn, tiêu đề."""

    def __init__(self, number: str, title: str, subtitle: str = "",
                 color=NAVY, width=CONTENT_W, height=2.55 * cm):
        super().__init__()
        self.number, self.title, self.subtitle = number, title, subtitle
        self.color, self.width, self.height = color, width, height
        self.toc_text = f"Chương {number}. {title}"
        self.toc_level = 0

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        h, w = self.height, self.width
        c.setFillColor(self.color)
        c.roundRect(0, 0, w, h, 4, stroke=0, fill=1)
        # ô số chương
        c.setFillColor(colors.Color(1, 1, 1, alpha=0.13))
        c.roundRect(0.45 * cm, 0.36 * cm, 1.85 * cm, h - 0.72 * cm, 3, stroke=0, fill=1)
        c.setFillColor(colors.white)
        c.setFont(FONT_B, 9)
        c.drawCentredString(1.375 * cm, h - 0.75 * cm, "CHƯƠNG")
        c.setFont(FONT_B, 26)
        c.drawCentredString(1.375 * cm, 0.78 * cm, self.number)
        # tiêu đề
        c.setFillColor(colors.white)
        c.setFont(FONT_B, 15)
        c.drawString(2.75 * cm, h - 1.05 * cm, self.title)
        if self.subtitle:
            c.setFillColor(colors.Color(1, 1, 1, alpha=0.82))
            c.setFont(FONT_I, 9.2)
            c.drawString(2.78 * cm, 0.72 * cm, self.subtitle)


class SectionBanner(Flowable):
    """Dải tiêu đề phần (PHẦN A, PHẦN B...)."""

    def __init__(self, kicker: str, title: str, color=TEAL, width=CONTENT_W,
                 height=1.9 * cm):
        super().__init__()
        self.kicker, self.title, self.color = kicker, title, color
        self.width, self.height = width, height
        self.toc_text = title
        self.toc_level = 0

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        h, w = self.height, self.width
        c.setFillColor(self.color)
        c.roundRect(0, 0, w, h, 4, stroke=0, fill=1)
        c.setFillColor(colors.Color(1, 1, 1, alpha=0.85))
        c.setFont(FONT_B, 9.5)
        c.drawString(0.7 * cm, h - 0.72 * cm, self.kicker)
        c.setFillColor(colors.white)
        c.setFont(FONT_B, 16)
        c.drawString(0.7 * cm, 0.55 * cm, self.title)


def data_table(header, rows, widths, align_center_cols=None, header_bg=NAVY,
               zebra=True, font_size=8.7, valign="MIDDLE") -> Table:
    """Bảng dữ liệu có header màu, kẻ mảnh, sọc xen kẽ."""
    align_center_cols = set(align_center_cols or [])
    cell_l = ParagraphStyle("cl", fontName=FONT, fontSize=font_size,
                            leading=font_size * 1.38, textColor=INK)
    cell_c = ParagraphStyle("cc", parent=cell_l, alignment=TA_CENTER)
    head_s = ParagraphStyle("hh", fontName=FONT_B, fontSize=font_size - 0.1,
                            leading=(font_size - 0.1) * 1.35,
                            alignment=TA_CENTER, textColor=colors.white)

    def wrap_cell(v, i):
        if isinstance(v, (Paragraph, Table, Flowable)):
            return v
        txt = "" if v is None else esc(str(v))
        return Paragraph(txt, cell_c if i in align_center_cols else cell_l)

    data = [[Paragraph(esc(h), head_s) for h in header]]
    for r in rows:
        data.append([wrap_cell(v, i) for i, v in enumerate(r)])

    t = Table(data, colWidths=widths, repeatRows=1)
    cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), header_bg),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.45, LINE),
        ("VALIGN", (0, 0), (-1, -1), valign),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3.2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.2),
    ]
    if zebra:
        for i in range(1, len(data)):
            if i % 2 == 0:
                cmds.append(("BACKGROUND", (0, i), (-1, i), LIGHT))
    t.setStyle(TableStyle(cmds))
    return t


def answer_chip(letter: str, ok: bool = True) -> str:
    """Trả về markup cho một đáp án được tô."""
    color = "#2E6B3E" if ok else "#A33E30"
    return f'<font name="{FONT_B}" color="{color}">{letter}</font>'


def key_table(pairs, cols=6, width=CONTENT_W, color=TEAL) -> Table:
    """Bảng đáp án nhanh: pairs = [(câu, đáp án), ...]."""
    per = max(1, cols)
    rows = []
    for i in range(0, len(pairs), per):
        chunk = pairs[i:i + per]
        row = []
        for q, a in chunk:
            row.append(Paragraph(
                esc(f'<font name="{FONT_B}" size="8.4">{q}</font> '
                    f'<font name="{FONT_B}" color="{color.hexval().replace("0x", "#")}">{a}</font>'),
                ParagraphStyle("k", fontName=FONT, fontSize=9.2, leading=13, alignment=TA_CENTER)))
        while len(row) < per:
            row.append("")
        rows.append(row)
    t = Table(rows, colWidths=[width / per] * per)
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.45, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("BACKGROUND", (0, 0), (-1, -1), colors.white),
    ]))
    return t


def side(flow_text, figure, text_ratio=0.60, width=CONTENT_W, valign="TOP",
         gap=0.35 * cm) -> Table:
    """Đặt khối nội dung bên trái và hình vẽ bên phải."""
    w1 = (width - gap) * text_ratio
    w2 = width - gap - w1
    t = Table([[list(flow_text), figure]], colWidths=[w1, w2])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), valign),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return t


def spacing(h: float = 0.25) -> Spacer:
    return Spacer(1, h * cm)
