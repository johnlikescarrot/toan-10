#!/usr/bin/env python3
"""Small ReportLab toolkit used to build the Vietnamese Grade 10 review guide."""
from __future__ import annotations

import hashlib
import json
import math
import os
from pathlib import Path
import re
import subprocess
from typing import Iterable, Sequence

import pymupdf
from reportlab.graphics.shapes import ArcPath, Circle, Drawing, Line, Path as GraphicPath, Polygon, Rect, String
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.fonts import addMapping
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Flowable,
    Frame,
    Image,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = Path(__file__).resolve().parents[1]
BUILD_DIR = ROOT / "build" / "guide"
MATH_DIR = BUILD_DIR / "math"
PAGE_W, PAGE_H = A4
LEFT = RIGHT = 17 * mm
TOP = 18 * mm
BOTTOM = 16 * mm
CONTENT_W = PAGE_W - LEFT - RIGHT

NAVY = HexColor("#16324F")
TEAL = HexColor("#0B7A75")
TEAL_DARK = HexColor("#075E5A")
GOLD = HexColor("#E1A62B")
CORAL = HexColor("#C85D4A")
INK = HexColor("#203040")
MUTED = HexColor("#5B6B78")
PALE = HexColor("#F3F7F9")
PALE_TEAL = HexColor("#EAF6F4")
PALE_GOLD = HexColor("#FFF7E3")
PALE_CORAL = HexColor("#FDF0EC")
LINE = HexColor("#CFDCE3")
WHITE = colors.white


def register_fonts() -> None:
    font_dir = Path("/usr/share/fonts/truetype/dejavu")
    pdfmetrics.registerFont(TTFont("DV", str(font_dir / "DejaVuSans.ttf")))
    pdfmetrics.registerFont(TTFont("DV-Bold", str(font_dir / "DejaVuSans-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("DV-Mono", str(font_dir / "DejaVuSansMono.ttf")))
    pdfmetrics.registerFontFamily("DV", normal="DV", bold="DV-Bold", italic="DV", boldItalic="DV-Bold")
    addMapping("DV", 0, 0, "DV")
    addMapping("DV", 1, 0, "DV-Bold")
    addMapping("DV", 0, 1, "DV")
    addMapping("DV", 1, 1, "DV-Bold")


register_fonts()


def make_styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    styles: dict[str, ParagraphStyle] = {}
    styles["Body"] = ParagraphStyle(
        "Body", parent=base["BodyText"], fontName="DV", fontSize=9.6,
        leading=14.4, textColor=INK, alignment=TA_JUSTIFY, spaceAfter=5.5,
        allowWidows=0, allowOrphans=0,
    )
    styles["BodyLeft"] = ParagraphStyle("BodyLeft", parent=styles["Body"], alignment=TA_LEFT)
    styles["Small"] = ParagraphStyle(
        "Small", parent=styles["Body"], fontSize=8.2, leading=12.2,
        textColor=MUTED, alignment=TA_LEFT, spaceAfter=4,
    )
    styles["Caption"] = ParagraphStyle(
        "Caption", parent=styles["Small"], fontSize=7.8, leading=11,
        alignment=TA_CENTER, textColor=MUTED, spaceBefore=3, spaceAfter=7,
    )
    styles["H1"] = ParagraphStyle(
        "H1", parent=base["Heading1"], fontName="DV-Bold", fontSize=20,
        leading=25, textColor=NAVY, spaceBefore=3, spaceAfter=11,
        keepWithNext=True,
    )
    styles["FrontTitle"] = ParagraphStyle("FrontTitle", parent=styles["H1"])
    styles["H2"] = ParagraphStyle(
        "H2", parent=base["Heading2"], fontName="DV-Bold", fontSize=13.2,
        leading=17.5, textColor=TEAL_DARK, spaceBefore=12, spaceAfter=6,
        keepWithNext=True,
    )
    styles["H3"] = ParagraphStyle(
        "H3", parent=base["Heading3"], fontName="DV-Bold", fontSize=10.6,
        leading=14.5, textColor=NAVY, spaceBefore=9, spaceAfter=4,
        keepWithNext=True,
    )
    styles["Question"] = ParagraphStyle(
        "Question", parent=styles["BodyLeft"], fontSize=9.5, leading=14.2,
        spaceBefore=7, spaceAfter=4, keepWithNext=True,
    )
    styles["Option"] = ParagraphStyle(
        "Option", parent=styles["BodyLeft"], fontSize=9.1, leading=13.2,
        spaceAfter=0,
    )
    styles["Bullet"] = ParagraphStyle(
        "Bullet", parent=styles["BodyLeft"], leftIndent=14, firstLineIndent=0,
        bulletIndent=2, spaceAfter=3.5,
    )
    styles["BoxTitle"] = ParagraphStyle(
        "BoxTitle", parent=styles["BodyLeft"], fontName="DV-Bold", fontSize=9.7,
        leading=13.5, textColor=NAVY, spaceAfter=4,
    )
    styles["BoxBody"] = ParagraphStyle(
        "BoxBody", parent=styles["BodyLeft"], fontSize=9.1, leading=13.5,
        spaceAfter=4,
    )
    styles["BoxBullet"] = ParagraphStyle(
        "BoxBullet", parent=styles["BoxBody"], leftIndent=13, bulletIndent=2,
        spaceAfter=3,
    )
    styles["Answer"] = ParagraphStyle(
        "Answer", parent=styles["BodyLeft"], fontSize=9.2, leading=13.8,
        textColor=TEAL_DARK, backColor=PALE_TEAL, borderPadding=6,
        spaceBefore=4, spaceAfter=7,
    )
    styles["TableCell"] = ParagraphStyle(
        "TableCell", parent=styles["BodyLeft"], fontSize=8.1, leading=11.3,
        spaceAfter=0,
    )
    styles["TableHead"] = ParagraphStyle(
        "TableHead", parent=styles["TableCell"], fontName="DV-Bold",
        textColor=WHITE, alignment=TA_CENTER, fontSize=8.1, leading=11,
    )
    styles["TableHeadDark"] = ParagraphStyle(
        "TableHeadDark", parent=styles["TableHead"], textColor=NAVY,
    )
    styles["TOC0"] = ParagraphStyle(
        "TOC0", fontName="DV-Bold", fontSize=10.3, leading=16,
        leftIndent=0, firstLineIndent=0, textColor=NAVY, spaceBefore=5,
    )
    styles["TOC1"] = ParagraphStyle(
        "TOC1", fontName="DV", fontSize=8.9, leading=13.5,
        leftIndent=14, firstLineIndent=0, textColor=INK,
    )
    styles["TOC2"] = ParagraphStyle(
        "TOC2", fontName="DV", fontSize=8.2, leading=12.5,
        leftIndent=28, firstLineIndent=0, textColor=MUTED,
    )
    return styles


STYLES = make_styles()


class MathRenderer:
    """Render TeX through MathJax, then rasterize at high resolution for ReportLab."""

    def __init__(self) -> None:
        MATH_DIR.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        cache_modules = ROOT / ".cache" / "npm" / "node_modules"
        if cache_modules.exists():
            env["NODE_PATH"] = str(cache_modules) + (
                os.pathsep + env["NODE_PATH"] if env.get("NODE_PATH") else ""
            )
        self.process = subprocess.Popen(
            ["node", str(ROOT / "guide" / "mathjax_renderer.cjs"), str(MATH_DIR)],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, env=env,
        )
        self.cache: dict[tuple[str, bool], dict] = {}

    def render(self, tex: str, display: bool = False) -> dict:
        key_cache = (tex, display)
        if key_cache in self.cache:
            return self.cache[key_cache]
        digest = hashlib.sha256((tex + "\0" + str(display)).encode("utf-8")).hexdigest()[:20]
        png_path = MATH_DIR / f"{digest}.png"
        meta_path = MATH_DIR / f"{digest}.json"
        if meta_path.exists() and png_path.exists():
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            meta["png"] = str(png_path)
            self.cache[key_cache] = meta
            return meta
        assert self.process.stdin and self.process.stdout
        self.process.stdin.write(json.dumps({"key": digest, "tex": tex, "display": display}) + "\n")
        self.process.stdin.flush()
        response = json.loads(self.process.stdout.readline())
        if "error" in response:
            raise RuntimeError(f"MathJax failed for {tex!r}: {response['error']}")
        svg_path = MATH_DIR / response["file"]
        doc = pymupdf.open(stream=svg_path.read_bytes(), filetype="svg")
        pix = doc[0].get_pixmap(matrix=pymupdf.Matrix(3, 3), alpha=True)
        pix.save(str(png_path))
        doc.close()
        meta = {**response, "png": str(png_path)}
        meta_path.write_text(json.dumps(meta), encoding="utf-8")
        self.cache[key_cache] = meta
        return meta

    @staticmethod
    def dimensions(meta: dict, font_size: float) -> tuple[float, float, float]:
        # MathJax's SVG viewBox uses 1000 units per em. Preserve baseline depth.
        width = meta["viewWidth"] / 1000 * font_size
        height = meta["viewHeight"] / 1000 * font_size
        depth = 0.0
        if meta.get("heightEx"):
            depth = height * meta.get("depthEx", 0) / meta["heightEx"]
        return width, height, depth

    def inline(self, tex: str, font_size: float = 9.6) -> str:
        meta = self.render(tex, False)
        width, height, depth = self.dimensions(meta, font_size)
        return (
            f'<img src="{meta["png"]}" width="{width:.3f}pt" height="{height:.3f}pt" '
            f'valign="{-depth:.3f}pt"/>'
        )

    def display(self, tex: str, font_size: float = 10.5, max_width: float = CONTENT_W - 12) -> Image:
        meta = self.render(tex, True)
        width, height, _ = self.dimensions(meta, font_size)
        scale = min(1.0, max_width / width) if width else 1.0
        image = Image(meta["png"], width=width * scale, height=height * scale)
        image.hAlign = "CENTER"
        return image

    def close(self) -> None:
        if self.process.poll() is None:
            if self.process.stdin:
                self.process.stdin.close()
            self.process.terminate()
            try:
                self.process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                self.process.kill()


MATH_PATTERN = re.compile(r"\$([^$\n]+)\$")


class GuideBuilder:
    def __init__(self) -> None:
        self.math = MathRenderer()
        self.s = STYLES

    def inline_math(self, text: str, font_size: float = 9.6) -> str:
        return MATH_PATTERN.sub(lambda m: self.math.inline(m.group(1), font_size), text)

    def p(self, text: str, style: str = "Body") -> Paragraph:
        return Paragraph(self.inline_math(text, self.s[style].fontSize), self.s[style])

    def bullet(self, text: str, style: str = "Bullet") -> Paragraph:
        return Paragraph(self.inline_math(text, self.s[style].fontSize), self.s[style], bulletText="•")

    def numbered(self, text: str, number: str, style: str = "Bullet") -> Paragraph:
        return Paragraph(self.inline_math(text, self.s[style].fontSize), self.s[style], bulletText=number)

    def formula(self, tex: str, font_size: float = 10.5, max_width: float = CONTENT_W - 12) -> list[Flowable]:
        return [Spacer(1, 2), self.math.display(tex, font_size, max_width), Spacer(1, 6)]

    def h1(self, text: str) -> Paragraph:
        return self.p(text, "H1")

    def h2(self, text: str) -> Paragraph:
        return self.p(text, "H2")

    def h3(self, text: str) -> Paragraph:
        return self.p(text, "H3")

    def box(self, title: str, items: Sequence[str | Flowable], kind: str = "note") -> Table:
        palettes = {
            "note": (PALE, NAVY),
            "tip": (PALE_TEAL, TEAL),
            "warning": (PALE_CORAL, CORAL),
            "remember": (PALE_GOLD, GOLD),
            "example": (PALE, TEAL),
        }
        background, accent = palettes[kind]
        content: list[Flowable] = [self.p(title, "BoxTitle")]
        for item in items:
            if isinstance(item, str):
                content.append(self.p(item, "BoxBody"))
            else:
                content.append(item)
        table = Table([[content]], colWidths=[CONTENT_W], hAlign="LEFT")
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), background),
            ("LINEBEFORE", (0, 0), (0, -1), 3.2, accent),
            ("BOX", (0, 0), (-1, -1), 0.35, LINE),
            ("LEFTPADDING", (0, 0), (-1, -1), 10),
            ("RIGHTPADDING", (0, 0), (-1, -1), 10),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]))
        table.spaceAfter = 8
        return table

    def options(self, options: Sequence[str], columns: int = 2) -> Table:
        if columns == 1:
            rows = [[self.p(option, "Option")] for option in options]
            widths = [CONTENT_W - 8]
        else:
            rows = []
            for i in range(0, len(options), 2):
                row = [self.p(option, "Option") for option in options[i:i + 2]]
                if len(row) == 1:
                    row.append("")
                rows.append(row)
            widths = [(CONTENT_W - 8) / 2] * 2
        table = Table(rows, colWidths=widths, hAlign="LEFT")
        table.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 2),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ]))
        return table

    def table(
        self, data: Sequence[Sequence[str | Flowable]], widths: Sequence[float] | None = None,
        header: bool = True, align: str = "LEFT", font_size: float | None = None,
        compact: bool = False,
    ) -> Table:
        converted: list[list[Flowable | str]] = []
        for r, row in enumerate(data):
            out: list[Flowable | str] = []
            for value in row:
                if isinstance(value, str):
                    out.append(self.p(value, "TableHead" if header and r == 0 else "TableCell"))
                else:
                    out.append(value)
            converted.append(out)
        table = Table(converted, colWidths=widths, repeatRows=1 if header else 0, hAlign="LEFT")
        padding = 2.5 if compact else 5
        commands = [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("GRID", (0, 0), (-1, -1), 0.35, LINE),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),
            ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), padding),
            ("BOTTOMPADDING", (0, 0), (-1, -1), padding),
        ]
        if header:
            commands += [
                ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                ("VALIGN", (0, 0), (-1, 0), "MIDDLE"),
            ]
            for r in range(1, len(data)):
                if r % 2 == 0:
                    commands.append(("BACKGROUND", (0, r), (-1, r), PALE))
        if align:
            commands.append(("ALIGN", (0, 0), (-1, -1), align))
        table.setStyle(TableStyle(commands))
        table.spaceAfter = 7
        return table

    def toc(self) -> TableOfContents:
        toc = TableOfContents()
        toc.levelStyles = [self.s["TOC0"], self.s["TOC1"], self.s["TOC2"]]
        toc.dotsMinLevel = 0
        return toc


class CoverAnchor(Flowable):
    def wrap(self, availWidth, availHeight):
        return 0, 0

    def draw(self):
        pass


class GuideDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str, **kwargs):
        super().__init__(
            filename, pagesize=A4, leftMargin=LEFT, rightMargin=RIGHT,
            topMargin=TOP, bottomMargin=BOTTOM, **kwargs,
        )
        frame = Frame(LEFT, BOTTOM, CONTENT_W, PAGE_H - TOP - BOTTOM, id="body")
        self.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=draw_page)])
        self._heading_counter = 0

    def afterFlowable(self, flowable):
        if not isinstance(flowable, Paragraph):
            return
        level_by_style = {"H1": 0, "H2": 1, "H3": 2}
        level = level_by_style.get(flowable.style.name)
        if level is None:
            return
        text = flowable.getPlainText()
        key = getattr(flowable, "_bookmark_key", None)
        if key is None:
            self._heading_counter += 1
            key = f"heading-{self._heading_counter}"
            flowable._bookmark_key = key
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(text, key, level=level, closed=(level == 0))
        self.notify("TOCEntry", (level, text, self.page, key))


def _paragraph_on_canvas(canvas, text: str, style: ParagraphStyle, x: float, top: float, width: float) -> float:
    p = Paragraph(text, style)
    _, height = p.wrap(width, PAGE_H)
    p.drawOn(canvas, x, top - height)
    return height


def draw_cover(canvas, doc) -> None:
    canvas.saveState()
    canvas.setTitle("Đề cương ôn tập Toán 10 – Giữa học kì I – 2026–2027")
    canvas.setAuthor("Tài liệu ôn tập biên soạn theo ma trận Trường THPT Hà Huy Tập")
    canvas.setSubject("Toán 10 Kết nối tri thức: lý thuyết, ví dụ, đề luyện tập và đáp án chi tiết")
    canvas.setKeywords("Toán 10, Kết nối tri thức, giữa học kì 1, mệnh đề, tập hợp, bất phương trình, vectơ")
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    canvas.setFillColor(HexColor("#1D4967"))
    canvas.circle(PAGE_W + 15, PAGE_H - 80, 150, stroke=0, fill=1)
    canvas.setFillColor(TEAL)
    canvas.circle(PAGE_W - 30, 100, 118, stroke=0, fill=1)
    canvas.setStrokeColor(HexColor("#315873"))
    canvas.setLineWidth(0.7)
    for i in range(9):
        y = 72 + i * 18
        canvas.line(38, y, 210, y + 62)

    badge = ParagraphStyle("CoverBadge", fontName="DV-Bold", fontSize=9, leading=12, textColor=GOLD)
    title = ParagraphStyle("CoverTitle", fontName="DV-Bold", fontSize=39, leading=43, textColor=WHITE)
    subtitle = ParagraphStyle("CoverSubtitle", fontName="DV-Bold", fontSize=17, leading=23, textColor=WHITE)
    body = ParagraphStyle("CoverBody", fontName="DV", fontSize=10.2, leading=16, textColor=HexColor("#DCEAF1"))
    small = ParagraphStyle("CoverSmall", fontName="DV", fontSize=8.6, leading=13, textColor=HexColor("#C0D5E0"))
    x = 45
    width = PAGE_W - 100
    _paragraph_on_canvas(canvas, "ÔN TẬP GIỮA HỌC KÌ I  •  NĂM HỌC 2026–2027", badge, x, PAGE_H - 66, width)
    _paragraph_on_canvas(canvas, "TOÁN 10", title, x, PAGE_H - 122, width)
    _paragraph_on_canvas(canvas, "ĐỀ CƯƠNG TRỌNG TÂM<br/>&amp; LUYỆN ĐỀ CÓ LỜI GIẢI", subtitle, x, PAGE_H - 190, width)
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(3)
    canvas.line(x, PAGE_H - 272, x + 82, PAGE_H - 272)
    _paragraph_on_canvas(
        canvas,
        "Mệnh đề và tập hợp  •  Bất phương trình bậc nhất hai ẩn<br/>Hệ thức lượng trong tam giác  •  Khái niệm vectơ",
        body, x, PAGE_H - 303, width,
    )

    # Original geometric motif: Venn diagram, triangle and vector.
    cy = 275
    canvas.setStrokeColor(HexColor("#84C8C1"))
    canvas.setLineWidth(2)
    canvas.circle(90, cy, 43, stroke=1, fill=0)
    canvas.circle(141, cy, 43, stroke=1, fill=0)
    canvas.setFillColor(GOLD)
    canvas.setFont("DV-Bold", 12)
    canvas.drawString(107, cy - 4, "A ∩ B")
    canvas.setStrokeColor(WHITE)
    canvas.setLineWidth(2.2)
    canvas.line(238, 222, 300, 338)
    canvas.line(300, 338, 364, 222)
    canvas.line(364, 222, 238, 222)
    canvas.setFillColor(WHITE)
    canvas.setFont("DV-Bold", 10)
    canvas.drawString(296, 346, "A")
    canvas.drawString(226, 213, "B")
    canvas.drawString(367, 213, "C")
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(3)
    canvas.line(410, 250, 500, 306)
    canvas.setFillColor(GOLD)
    path = canvas.beginPath()
    path.moveTo(500, 306)
    path.lineTo(484, 303)
    path.lineTo(492, 290)
    path.close()
    canvas.drawPath(path, stroke=0, fill=1)

    _paragraph_on_canvas(
        canvas,
        "Lý thuyết dễ tra cứu  •  Ví dụ từng bước  •  Bài luyện có đáp án<br/>Đề 90 phút bám ma trận  •  Lời giải chi tiết  •  Phụ lục đối chiếu đủ nội dung",
        body, x, 158, PAGE_W - 90,
    )
    _paragraph_on_canvas(
        canvas,
        "Bám sát ma trận Trường THPT Hà Huy Tập<br/>Chương trình Toán 10 – Kết nối tri thức với cuộc sống",
        small, x, 89, PAGE_W - 90,
    )
    canvas.restoreState()


def draw_header_footer(canvas, doc) -> None:
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.5)
    canvas.line(LEFT, PAGE_H - 11 * mm, PAGE_W - RIGHT, PAGE_H - 11 * mm)
    canvas.setFillColor(MUTED)
    canvas.setFont("DV-Bold", 7.4)
    canvas.drawString(LEFT, PAGE_H - 8.5 * mm, "TOÁN 10  •  ÔN TẬP GIỮA HỌC KÌ I")
    canvas.setFont("DV", 7.4)
    canvas.drawRightString(PAGE_W - RIGHT, PAGE_H - 8.5 * mm, "KẾT NỐI TRI THỨC  •  2026–2027")
    canvas.line(LEFT, 10.5 * mm, PAGE_W - RIGHT, 10.5 * mm)
    canvas.setFont("DV", 7.3)
    canvas.drawString(LEFT, 7 * mm, "Lý thuyết – Ví dụ – Luyện tập – Đáp án")
    canvas.setFont("DV-Bold", 7.5)
    canvas.drawRightString(PAGE_W - RIGHT, 7 * mm, f"TRANG {canvas.getPageNumber()}")
    canvas.restoreState()


def draw_page(canvas, doc) -> None:
    if canvas.getPageNumber() == 1:
        draw_cover(canvas, doc)
    else:
        draw_header_footer(canvas, doc)


# ---------- Original vector diagrams ----------

def _arrow(d: Drawing, x1, y1, x2, y2, color=NAVY, width=1.8) -> None:
    d.add(Line(x1, y1, x2, y2, strokeColor=color, strokeWidth=width))
    angle = math.atan2(y2 - y1, x2 - x1)
    size = 6
    p1 = (x2 - size * math.cos(angle - 0.55), y2 - size * math.sin(angle - 0.55))
    p2 = (x2 - size * math.cos(angle + 0.55), y2 - size * math.sin(angle + 0.55))
    d.add(Polygon([x2, y2, p1[0], p1[1], p2[0], p2[1]], fillColor=color, strokeColor=color))


def venn_intersection() -> Drawing:
    d = Drawing(235, 135)
    d.add(Rect(5, 10, 225, 115, rx=5, ry=5, fillColor=PALE, strokeColor=LINE, strokeWidth=0.8))
    d.add(String(15, 112, "E", fontName="DV-Bold", fontSize=10, fillColor=NAVY))
    left, right, cy, r = 85, 145, 65, 45
    lens = ArcPath()
    theta = math.degrees(math.acos((right - left) / (2 * r)))
    lens.addArc(left, cy, r, -theta, theta, moveTo=True, reverse=True)
    lens.addArc(right, cy, r, 180 - theta, 180 + theta, moveTo=False, reverse=True)
    lens.closePath()
    lens.fillColor = GOLD
    lens.strokeColor = None
    d.add(lens)
    d.add(Circle(left, cy, r, fillColor=None, strokeColor=TEAL, strokeWidth=1.8))
    d.add(Circle(right, cy, r, fillColor=None, strokeColor=NAVY, strokeWidth=1.8))
    d.add(String(55, 70, "A", fontName="DV-Bold", fontSize=12, fillColor=TEAL_DARK))
    d.add(String(170, 70, "B", fontName="DV-Bold", fontSize=12, fillColor=NAVY))
    d.add(String(108, 60, "?", fontName="DV-Bold", fontSize=12, fillColor=NAVY))
    return d


def number_line(start=-2, end=3, left_closed=True, right_closed=False, label="") -> Drawing:
    d = Drawing(330, 72)
    lo, hi = start - 1.5, end + 1.5
    x0, x1, y = 24, 306, 33
    def sx(value):
        return x0 + (value - lo) / (hi - lo) * (x1 - x0)
    _arrow(d, x0 - 6, y, x1 + 7, y, MUTED, 1.1)
    xa, xb = sx(start), sx(end)
    d.add(Line(xa, y, xb, y, strokeColor=TEAL, strokeWidth=4))
    for value, closed in [(start, left_closed), (end, right_closed)]:
        x = sx(value)
        d.add(Line(x, y - 6, x, y + 6, strokeColor=NAVY, strokeWidth=0.8))
        d.add(Circle(x, y, 4, fillColor=TEAL if closed else WHITE, strokeColor=TEAL, strokeWidth=1.5))
        d.add(String(x, y - 20, str(value).replace("-", "−"), fontName="DV", fontSize=9, fillColor=INK, textAnchor="middle"))
    if label:
        d.add(String((xa + xb) / 2, 57, label, fontName="DV-Bold", fontSize=10, fillColor=NAVY, textAnchor="middle"))
    return d


def unit_semicircle() -> Drawing:
    d = Drawing(310, 180)
    ox, oy, r = 155, 40, 105
    d.add(Line(ox - 130, oy, ox + 130, oy, strokeColor=MUTED, strokeWidth=1))
    _arrow(d, ox, oy - 10, ox, oy + 135, MUTED, 1)
    path = ArcPath()
    path.addArc(ox, oy, r, 0, 180, moveTo=True)
    path.strokeColor = NAVY
    path.strokeWidth = 1.8
    path.fillColor = None
    d.add(path)
    d.add(Line(ox - r, oy, ox + r, oy, strokeColor=NAVY, strokeWidth=1.2))
    alpha = math.radians(125)
    mx, my = ox + r * math.cos(alpha), oy + r * math.sin(alpha)
    d.add(Line(ox, oy, mx, my, strokeColor=TEAL, strokeWidth=1.8))
    d.add(Line(mx, oy, mx, my, strokeColor=GOLD, strokeWidth=1, strokeDashArray=[3, 3]))
    d.add(Circle(mx, my, 3, fillColor=TEAL, strokeColor=TEAL))
    d.add(String(mx - 5, my + 9, "M(x₀; y₀)", fontName="DV-Bold", fontSize=9, fillColor=NAVY, textAnchor="middle"))
    d.add(String(mx - 5, oy - 15, "x₀ = cos α", fontName="DV", fontSize=8.5, fillColor=INK, textAnchor="middle"))
    d.add(String(mx + 14, (my + oy) / 2, "y₀ = sin α", fontName="DV", fontSize=8.5, fillColor=INK))
    d.add(String(ox + 35, oy + 12, "α", fontName="DV-Bold", fontSize=11, fillColor=CORAL))
    d.add(String(ox + r - 5, oy - 15, "1", fontName="DV", fontSize=8, fillColor=MUTED))
    d.add(String(ox - r - 5, oy - 15, "−1", fontName="DV", fontSize=8, fillColor=MUTED))
    d.add(String(ox + 125, oy - 15, "x", fontName="DV-Bold", fontSize=9, fillColor=MUTED))
    d.add(String(ox + 7, oy + 128, "y", fontName="DV-Bold", fontSize=9, fillColor=MUTED))
    d.add(String(ox + 5, oy - 15, "O", fontName="DV", fontSize=8, fillColor=MUTED))
    return d


def inequality_region() -> Drawing:
    d = Drawing(300, 220)
    left, bottom, scale = 48, 28, 31
    def pt(x, y):
        return left + (x + 1) * scale, bottom + (y + 1) * scale
    for v in range(-1, 6):
        x, _ = pt(v, 0)
        _, y = pt(0, v)
        d.add(Line(x, bottom, x, bottom + 6 * scale, strokeColor=HexColor("#E7EEF1"), strokeWidth=0.5))
        d.add(Line(left, y, left + 6 * scale, y, strokeColor=HexColor("#E7EEF1"), strokeWidth=0.5))
    region = [pt(-1, -1), pt(5, -1), pt(0, 4), pt(-1, 5)]
    d.add(Polygon([c for p in region for c in p], fillColor=HexColor("#CDEBE5"), strokeColor=None))
    _arrow(d, *pt(-1, 0), *pt(5.25, 0), MUTED, 1)
    _arrow(d, *pt(0, -1), *pt(0, 5.25), MUTED, 1)
    d.add(Line(*pt(-1, 5), *pt(5, -1), strokeColor=NAVY, strokeWidth=1.8))
    for x, y, name in [(0, 0, "O"), (2, 0, "2"), (0, 4, "4")]:
        px, py = pt(x, y)
        d.add(Circle(px, py, 2.6, fillColor=CORAL if name == "O" else NAVY, strokeColor=None))
        d.add(String(px + 5, py + 5, name, fontName="DV", fontSize=8, fillColor=INK))
    d.add(String(*pt(4.8, -0.4), "x", fontName="DV-Bold", fontSize=9, fillColor=MUTED))
    d.add(String(*pt(0.15, 4.85), "y", fontName="DV-Bold", fontSize=9, fillColor=MUTED))
    d.add(String(*pt(2.1, 2.55), "2x + y = 4", fontName="DV-Bold", fontSize=8.5, fillColor=NAVY))
    d.add(String(*pt(0.15, 1.05), "Miền nghiệm", fontName="DV-Bold", fontSize=8.5, fillColor=TEAL_DARK))
    return d


def feasible_region() -> Drawing:
    d = Drawing(350, 255)
    left, bottom, sx, sy = 48, 33, 4.2, 2.85
    def pt(x, y):
        return left + x * sx, bottom + y * sy
    for x in range(0, 61, 10):
        px, _ = pt(x, 0)
        d.add(Line(px, bottom, px, bottom + 60 * sy, strokeColor=HexColor("#E7EEF1"), strokeWidth=0.45))
        d.add(String(px, bottom - 13, str(x), fontName="DV", fontSize=7.5, fillColor=MUTED, textAnchor="middle"))
    for y in range(0, 61, 10):
        _, py = pt(0, y)
        d.add(Line(left, py, left + 60 * sx, py, strokeColor=HexColor("#E7EEF1"), strokeWidth=0.45))
        d.add(String(left - 10, py - 2, str(y), fontName="DV", fontSize=7.5, fillColor=MUTED, textAnchor="end"))
    vertices = [(0, 0), (30, 0), (20, 20), (0, 40)]
    d.add(Polygon([c for x, y in vertices for c in pt(x, y)], fillColor=HexColor("#CDEBE5"), strokeColor=TEAL, strokeWidth=1.1))
    d.add(Line(*pt(0, 40), *pt(40, 0), strokeColor=NAVY, strokeWidth=1.5))
    d.add(Line(*pt(0, 60), *pt(30, 0), strokeColor=CORAL, strokeWidth=1.5))
    _arrow(d, *pt(0, 0), *pt(63, 0), MUTED, 1)
    _arrow(d, *pt(0, 0), *pt(0, 63), MUTED, 1)
    for x, y in vertices:
        px, py = pt(x, y)
        d.add(Circle(px, py, 3, fillColor=GOLD, strokeColor=NAVY, strokeWidth=0.7))
        d.add(String(px + 5, py + 5, f"({x}; {y})", fontName="DV-Bold", fontSize=7.6, fillColor=NAVY))
    d.add(String(*pt(24, 28), "x + y = 40", fontName="DV", fontSize=8, fillColor=NAVY))
    d.add(String(*pt(7, 51), "2x + y = 60", fontName="DV", fontSize=8, fillColor=CORAL))
    d.add(String(*pt(60, -3), "x", fontName="DV-Bold", fontSize=9, fillColor=MUTED))
    d.add(String(*pt(2, 60), "y", fontName="DV-Bold", fontSize=9, fillColor=MUTED))
    return d


def parallelogram_diagram() -> Drawing:
    d = Drawing(280, 155)
    A, B, C, D = (55, 30), (220, 30), (250, 120), (85, 120)
    d.add(Polygon([*A, *B, *C, *D], fillColor=PALE, strokeColor=NAVY, strokeWidth=1.5))
    _arrow(d, A[0] + 25, A[1], B[0] - 25, B[1], TEAL, 2.2)
    _arrow(d, D[0] + 25, D[1], C[0] - 25, C[1], TEAL, 2.2)
    for (x, y), label, dx, dy in [(A, "A", -12, -14), (B, "B", 5, -14), (C, "C", 5, 4), (D, "D", -14, 4)]:
        d.add(String(x + dx, y + dy, label, fontName="DV-Bold", fontSize=10, fillColor=NAVY))
    d.add(String(132, 10, "vectơ AB", fontName="DV", fontSize=8, fillColor=TEAL_DARK, textAnchor="middle"))
    d.add(String(170, 128, "vectơ DC", fontName="DV", fontSize=8, fillColor=TEAL_DARK, textAnchor="middle"))
    return d


def triangle_diagram(practical=False) -> Drawing:
    d = Drawing(300, 175)
    A, B, C = (145, 145), (45, 30), (255, 30)
    d.add(Polygon([*A, *B, *C], fillColor=PALE_TEAL if practical else PALE, strokeColor=NAVY, strokeWidth=1.5))
    for (x, y), label, dx, dy in [(A, "A", -4, 8), (B, "B", -14, -12), (C, "C", 6, -12)]:
        d.add(String(x + dx, y + dy, label, fontName="DV-Bold", fontSize=10, fillColor=NAVY))
    if practical:
        d.add(String(82, 92, "50 m", fontName="DV-Bold", fontSize=9, fillColor=TEAL_DARK, textAnchor="middle"))
        d.add(String(210, 92, "80 m", fontName="DV-Bold", fontSize=9, fillColor=TEAL_DARK, textAnchor="middle"))
        d.add(String(150, 12, "BC = ?", fontName="DV-Bold", fontSize=9, fillColor=CORAL, textAnchor="middle"))
        d.add(String(148, 126, "60°", fontName="DV-Bold", fontSize=9, fillColor=CORAL, textAnchor="middle"))
    else:
        d.add(String(150, 12, "a = BC", fontName="DV", fontSize=9, fillColor=INK, textAnchor="middle"))
        d.add(String(82, 92, "c = AB", fontName="DV", fontSize=9, fillColor=INK, textAnchor="middle"))
        d.add(String(210, 92, "b = CA", fontName="DV", fontSize=9, fillColor=INK, textAnchor="middle"))
        d.add(String(148, 126, "A", fontName="DV-Bold", fontSize=9, fillColor=CORAL, textAnchor="middle"))
    return d
