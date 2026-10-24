# -*- coding: utf-8 -*-
"""
Bộ công cụ dựng PDF cho Đề cương ôn tập Toán 10 – Giữa kỳ I (năm học 2026-2027).

Cung cấp:
  * Doc        – template PDF (A4 dọc + A4 ngang), đầu trang, chân trang, mục lục tự động.
  * Ctx        – lớp bọc các flowable, có các phương thức trình bày dùng trong toàn bộ tài liệu.
  * Hàm trợ    – esc(), table(), formula(), box(), ...

Yêu cầu: ReportLab và bộ font DejaVu (Sans/Serif/Mono, có bản Oblique/Italic).
"""

import glob
import os

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, CondPageBreak, Flowable, Frame, HRFlowable, KeepTogether,
    NextPageTemplate, PageBreak, PageTemplate, Paragraph, Spacer, Table,
    TableStyle,
)

# --------------------------------------------------------------------------
# 1. FONT
# --------------------------------------------------------------------------

FONT_DIRS = [
    "/usr/share/fonts/truetype/dejavu",
    "/usr/local/lib/python3.11/dist-packages/matplotlib/mpl-data/fonts/ttf",
    "/usr/share/fonts/truetype",
]


def _find_font(*names):
    """Tìm file font theo danh sách tên ưu tiên, trong các thư mục font đã biết."""
    for name in names:
        for folder in FONT_DIRS:
            hits = sorted(glob.glob(os.path.join(folder, name)))
            if hits:
                return hits[0]
    return None


def register_fonts():
    """Đăng ký các font DejaVu (hỗ trợ đầy đủ dấu tiếng Việt)."""
    faces = {
        "DJV": (["DejaVuSans.ttf"], None),
        "DJV-Bold": (["DejaVuSans-Bold.ttf"], None),
        "DJV-Italic": (["DejaVuSans-Oblique.ttf", "DejaVuSerif-Italic.ttf"], None),
        "DJV-BoldItalic": (["DejaVuSans-BoldOblique.ttf", "DejaVuSerif-BoldItalic.ttf"], None),
        "DJV-Serif": (["DejaVuSerif.ttf"], None),
        "DJV-Serif-Bold": (["DejaVuSerif-Bold.ttf"], None),
        "DJV-Mono": (["DejaVuSansMono.ttf"], None),
        "DJV-Mono-Bold": (["DejaVuSansMono-Bold.ttf"], None),
    }
    missing = []
    for alias, (cands, _) in faces.items():
        path = _find_font(*cands)
        if path:
            pdfmetrics.registerFont(TTFont(alias, path))
        else:
            missing.append(alias)
    if missing:
        raise RuntimeError("Không tìm thấy font: %s" % ", ".join(missing))

    pdfmetrics.registerFontFamily(
        "DJV", normal="DJV", bold="DJV-Bold", italic="DJV-Italic",
        boldItalic="DJV-BoldItalic",
    )
    pdfmetrics.registerFontFamily(
        "DJV-Serif", normal="DJV-Serif", bold="DJV-Serif-Bold",
        italic="DJV-Serif", boldItalic="DJV-Serif-Bold",
    )


# --------------------------------------------------------------------------
# 2. MÀU SẮC – BẢNG MÀU
# --------------------------------------------------------------------------

XANH_DAM = colors.HexColor("#16325C")
XANH = colors.HexColor("#1F4E79")
XANH_SANG = colors.HexColor("#2E74B5")
NEN_XANH = colors.HexColor("#EAF1F8")
NEN_XANH_2 = colors.HexColor("#F4F8FC")
XANH_ONG = colors.HexColor("#B9770E")
NEN_ONG = colors.HexColor("#FDF3E3")
XANH_LA = colors.HexColor("#1E6B3A")
NEN_LA = colors.HexColor("#EAF5EE")
XANH_DO = colors.HexColor("#9C2A2A")
NEN_DO = colors.HexColor("#FBEDED")
XAM = colors.HexColor("#555555")
DUONG = colors.HexColor("#C7D3E0")
NEN_BANG = colors.HexColor("#F7F9FB")


# --------------------------------------------------------------------------
# 3. STYLE
# --------------------------------------------------------------------------

def build_styles():
    st = {}

    def add(name, **kw):
        st[name] = ParagraphStyle(name, **kw)

    add("body", fontName="DJV", fontSize=10, leading=15, alignment=TA_JUSTIFY,
        spaceAfter=5, textColor=colors.HexColor("#1A1A1A"))
    add("body_c", parent=st["body"], alignment=TA_CENTER)
    add("body_j", parent=st["body"], alignment=TA_JUSTIFY)

    add("h1", fontName="DJV-Bold", fontSize=16, leading=21, textColor=XANH_DAM,
        spaceBefore=14, spaceAfter=9)
    add("h2", fontName="DJV-Bold", fontSize=12.5, leading=17, textColor=XANH,
        spaceBefore=11, spaceAfter=6)
    add("h3", fontName="DJV-Bold", fontSize=11, leading=15, textColor=colors.black,
        spaceBefore=8, spaceAfter=4)
    add("h4", fontName="DJV-Bold", fontSize=10, leading=14, textColor=XANH_SANG,
        spaceBefore=6, spaceAfter=3)

    add("bullet", parent=st["body"], leftIndent=13, bulletIndent=3, spaceAfter=3)
    add("bullet2", parent=st["body"], leftIndent=26, bulletIndent=16,
        fontSize=9.5, leading=14, spaceAfter=2)
    add("num", parent=st["body"], leftIndent=16, bulletIndent=3, spaceAfter=3)

    add("formula", fontName="DJV", fontSize=10.5, leading=16, alignment=TA_CENTER,
        textColor=colors.HexColor("#0F2B46"))
    add("formula_small", parent=st["formula"], fontSize=9.5, leading=14)

    add("cell", fontName="DJV", fontSize=8.6, leading=11.6, alignment=TA_LEFT,
        spaceAfter=0)
    add("cell_c", parent=st["cell"], alignment=TA_CENTER)
    add("cell_head", parent=st["cell"], fontName="DJV-Bold", alignment=TA_CENTER,
        textColor=colors.white)
    add("cell_head_l", parent=st["cell"], fontName="DJV-Bold", alignment=TA_LEFT,
        textColor=colors.white)

    add("box_t", fontName="DJV-Bold", fontSize=9.8, leading=14,
        textColor=colors.HexColor("#0F2B46"))
    add("box_b", fontName="DJV", fontSize=9.4, leading=13.6, alignment=TA_JUSTIFY,
        spaceAfter=2)

    add("cover_t", fontName="DJV-Bold", fontSize=25, leading=32, alignment=TA_CENTER,
        textColor=XANH_DAM)
    add("cover_s", fontName="DJV", fontSize=13.5, leading=20, alignment=TA_CENTER,
        textColor=XANH)
    add("cover_k", fontName="DJV-Bold", fontSize=10.5, leading=16, alignment=TA_CENTER,
        textColor=colors.white)
    add("cover_v", fontName="DJV", fontSize=10.5, leading=16, alignment=TA_LEFT,
        textColor=colors.HexColor("#1A1A1A"))

    add("toc1", fontName="DJV-Bold", fontSize=10.5, leading=16, spaceBefore=6)
    add("toc2", fontName="DJV", fontSize=9.6, leading=14, leftIndent=16)
    add("toc3", fontName="DJV", fontSize=9.2, leading=13, leftIndent=32,
        textColor=colors.HexColor("#333333"))

    add("small", fontName="DJV", fontSize=8.6, leading=12, alignment=TA_JUSTIFY,
        textColor=XAM)
    add("cap", fontName="DJV-Italic", fontSize=8.8, leading=12, alignment=TA_CENTER,
        textColor=XAM, spaceBefore=3, spaceAfter=8)
    add("q", fontName="DJV", fontSize=10.2, leading=15.2, alignment=TA_JUSTIFY,
        spaceAfter=3, leftIndent=0)
    add("q_opt", parent=st["q"], leftIndent=16)
    add("note_ref", fontName="DJV", fontSize=9.4, leading=13.6, alignment=TA_JUSTIFY)
    return st


# --------------------------------------------------------------------------
# 4. TIỆN ÍCH
# --------------------------------------------------------------------------

def esc(t):
    """Escape & < > để đưa vào Paragraph."""
    if t is None:
        return ""
    return (str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def _auto(t):
    """Cho phép các thẻ ReportLab cơ bản (<b>, <i>, <br/>, <super>, <sub>) đi qua."""
    return t


# --------------------------------------------------------------------------
# 5. TEMPLATE PDF
# --------------------------------------------------------------------------

class NumberedCanvas:
    """Canvas dựng sẵn – chỉ giữ để tương thích; số trang được in trong onPage."""

    def __init__(self, *args, **kwargs):
        from reportlab.pdfgen import canvas as _canvas
        self._canvas = _canvas.Canvas(*args, **kwargs)

    def __getattr__(self, name):
        return getattr(self.__dict__["_canvas"], name)


class Doc(BaseDocTemplate):
    """Template chính: A4 dọc + A4 ngang, mục lục tự sinh."""

    def __init__(self, filename, **kw):
        BaseDocTemplate.__init__(self, filename, **kw)
        self.styles = build_styles()
        self._toc_entries = []
        self._seen = set()
        self.toc_level = 0
        self.total_pages = None      # được cập nhật ở lượt dựng thứ hai
        self.skip_toc = {"MỤC LỤC"}

        pw, ph = A4
        lw, lh = landscape(A4)

        self.frame_portrait = Frame(
            17 * mm, 16 * mm, pw - 34 * mm, ph - 16 * mm - 20 * mm,
            id="fp", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
        )
        self.frame_land = Frame(
            14 * mm, 14 * mm, lw - 28 * mm, lh - 14 * mm - 18 * mm,
            id="fl", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
        )

        self.addPageTemplates([
            PageTemplate(id="portrait", frames=[self.frame_portrait],
                         pagesize=A4, onPage=self._deco_portrait),
            PageTemplate(id="landscape", frames=[self.frame_land],
                         pagesize=landscape(A4), onPage=self._deco_landscape),
        ])

    # -- trang trang trí ----------------------------------------------------
    def _deco_portrait(self, canv, doc):
        canv.saveState()
        w, h = A4
        canv.setStrokeColor(XANH_DAM)
        canv.setLineWidth(1.1)
        canv.line(17 * mm, h - 14 * mm, w - 17 * mm, h - 14 * mm)
        canv.setFont("DJV", 7.6)
        canv.setFillColor(XAM)
        canv.drawString(17 * mm, h - 11.6 * mm,
                        "ĐỀ CƯƠNG ÔN TẬP TOÁN 10 – GIỮA HỌC KỲ I  |  NĂM HỌC 2026-2027")
        canv.drawRightString(w - 17 * mm, h - 11.6 * mm, "SGD: TRƯỜNG THPT HÀ HUY TẬP – TỔ TOÁN-TIN")
        canv.setStrokeColor(DUONG)
        canv.setLineWidth(0.6)
        canv.line(17 * mm, 13.6 * mm, w - 17 * mm, 13.6 * mm)
        canv.setFont("DJV", 7.6)
        canv.setFillColor(XAM)
        canv.drawString(17 * mm, 9.6 * mm,
                        "Chương trình Toán 10 – “Kết nối tri thức”  |  Dựa trên ma trận đề kiểm tra")
        self._so_trang(canv, doc, w, 17 * mm)
        canv.restoreState()

    def _so_trang(self, canv, doc, w, right=17 * mm):
        """In số trang ở chân trang: 'Trang x' hoặc 'Trang x / y'."""
        n = getattr(doc, "page", 1)
        tot = getattr(doc, "total_pages", None)
        txt = "Trang %d" % n if not tot else "Trang %d / %d" % (n, tot)
        canv.setFont("DJV", 7.6)
        canv.setFillColor(XAM)
        canv.drawRightString(w - right, 9.6 * mm, txt)

    def _deco_landscape(self, canv, doc):
        canv.saveState()
        w, h = landscape(A4)
        canv.setStrokeColor(XANH_DAM)
        canv.setLineWidth(1.1)
        canv.line(14 * mm, h - 12 * mm, w - 14 * mm, h - 12 * mm)
        canv.setFont("DJV", 7.6)
        canv.setFillColor(XAM)
        canv.drawString(14 * mm, h - 9.8 * mm,
                        "ĐỀ CƯƠNG ÔN TẬP TOÁN 10 – GIỮA HỌC KỲ I  |  NĂM HỌC 2026-2027")
        canv.drawRightString(w - 14 * mm, h - 9.8 * mm, "Tài liệu gốc: MA TRẬN TOÁN 10 - GIỮA KÌ I")
        canv.setStrokeColor(DUONG)
        canv.setLineWidth(0.6)
        canv.line(14 * mm, 12.4 * mm, w - 14 * mm, 12.4 * mm)
        canv.setFont("DJV", 7.6)
        canv.setFillColor(XAM)
        canv.drawString(14 * mm, 8.4 * mm, "Chương trình Toán 10 – “Kết nối tri thức”")
        self._so_trang(canv, doc, w, 14 * mm)
        canv.restoreState()

    # -- mục lục ------------------------------------------------------------
    def build(self, *args, **kw):
        """Mỗi lượt dựng lại (multiBuild chạy nhiều lượt) phải bỏ bộ nhớ đệ quy."""
        self._seen = set()
        return BaseDocTemplate.build(self, *args, **kw)

    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph):
            style = flowable.style.name
            if style == "h1":
                level, text = 0, flowable.getPlainText()
            elif style == "h2":
                level, text = 1, flowable.getPlainText()
            else:
                return
            if text.strip() in self.skip_toc:
                return
            key = "%s|%s" % (level, text)
            if key in self._seen:
                return
            self._seen.add(key)
            self.notify("TOCEntry", (level, text, self.page))


# --------------------------------------------------------------------------
# 6. LỚP BỌC NỘI DUNG
# --------------------------------------------------------------------------

class Ctx:
    """Cung cấp các phương thức trình bày dùng xuyên suốt tài liệu."""

    def __init__(self, doc):
        self.doc = doc
        self.st = doc.styles
        self.story = []

    # -- hàm cơ bản --------------------------------------------------------
    def add(self, flowable):
        self.story.append(flowable)
        return flowable

    def sp(self, h=4):
        return self.add(Spacer(1, h))

    def p(self, text, style="body"):
        return self.add(Paragraph(text, self.st[style]))

    def h1(self, text):
        self.add(Paragraph(text, self.st["h1"]))
        self.add(HRFlowable(width="100%", thickness=1.1, color=XANH_SANG,
                            spaceBefore=1, spaceAfter=7))

    def h2(self, text):
        return self.add(Paragraph(text, self.st["h2"]))

    def h3(self, text):
        return self.add(Paragraph(text, self.st["h3"]))

    def h4(self, text):
        return self.add(Paragraph(text, self.st["h4"]))

    def bullets(self, items, style="bullet", bullet="•"):
        for it in items:
            self.add(Paragraph(it, self.st[style], bulletText=bullet))
        return self

    def numbered(self, items, style="num"):
        for i, it in enumerate(items, 1):
            self.add(Paragraph(it, self.st[style], bulletText="%d." % i))
        return self

    def caption(self, text):
        return self.add(Paragraph(text, self.st["cap"]))

    def hr(self, color=DUONG, space=4):
        return self.add(HRFlowable(width="100%", thickness=0.7, color=color,
                                   spaceBefore=space, spaceAfter=space))

    def page_break(self):
        return self.add(PageBreak())

    def to_landscape(self):
        self.add(NextPageTemplate("landscape"))
        self.add(PageBreak())

    def to_portrait(self):
        self.add(NextPageTemplate("portrait"))
        self.add(PageBreak())

    # -- khối nội dung ------------------------------------------------------
    def formula(self, lines, bg=NEN_XANH, border=XANH_SANG, small=False):
        """Khung công thức canh giữa."""
        sty = "formula_small" if small else "formula"
        if isinstance(lines, str):
            lines = [lines]
        inner = [[Paragraph(l, self.st[sty])] for l in lines]
        t = Table(inner, colWidths=[self._content_width()])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), bg),
            ("BOX", (0, 0), (-1, -1), 0.8, border),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ]))
        self.add(t)
        self.sp(5)
        return t

    def _content_width(self):
        f = self.doc.frame_portrait
        return f.width

    def box(self, title, lines, kind="info"):
        """Khối lưu ý / ví dụ / đáp án."""
        pal = {
            "info": (NEN_XANH, XANH_SANG, XANH_DAM),
            "warn": (NEN_ONG, XANH_ONG, colors.HexColor("#7A4E00")),
            "ans": (NEN_LA, XANH_LA, XANH_LA),
            "err": (NEN_DO, XANH_DO, XANH_DO),
            "grey": (NEN_BANG, DUONG, colors.HexColor("#333333")),
        }
        bg, border, tcol = pal.get(kind, pal["info"])
        rows = []
        if title:
            rows.append([Paragraph("<b><font color='%s'>%s</font></b>"
                                   % (tcol.hexval(), title), self.st["box_t"])])
        for ln in lines:
            if isinstance(ln, (list, tuple)):
                rows.append([Paragraph("".join(ln), self.st["box_b"])])
            else:
                rows.append([Paragraph(ln, self.st["box_b"])])
        t = Table(rows, colWidths=[self._content_width()])
        st = [
            ("BACKGROUND", (0, 0), (-1, -1), bg),
            ("BOX", (0, 0), (-1, -1), 0.9, border),
            ("LEFTPADDING", (0, 0), (-1, -1), 9),
            ("RIGHTPADDING", (0, 0), (-1, -1), 9),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ]
        if title:
            st.append(("LINEBELOW", (0, 0), (0, 0), 0.9, border))
            st.append(("SPAN", (0, 0), (0, 0)))
            st.append(("BOTTOMPADDING", (0, 0), (0, 0), 2))
        t.setStyle(TableStyle(st))
        self.add(t)
        self.sp(6)
        return t

    def table(self, data, widths, header=1, align=None, small=8.6,
              head_bg=XANH, zebra=True, valign="TOP", repeat=1):
        """Bảng dữ liệu; mỗi ô là chuỗi (đã cho phép thẻ ReportLab)."""
        rows = []
        for ri, row in enumerate(data):
            out = []
            for ci, cell in enumerate(row):
                if cell is None:
                    cell = ""
                sty = "cell"
                if ri < header:
                    sty = "cell_head"
                    if align and align[ci] == "l":
                        sty = "cell_head_l"
                else:
                    if align and align[ci] == "c":
                        sty = "cell_c"
                if isinstance(cell, Paragraph):
                    out.append(cell)
                else:
                    out.append(Paragraph(str(cell), self.st[sty]))
            rows.append(out)
        t = Table(rows, colWidths=widths, repeatRows=repeat if header else 0)
        cmds = [
            ("GRID", (0, 0), (-1, -1), 0.5, DUONG),
            ("VALIGN", (0, 0), (-1, -1), valign),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ]
        if header:
            cmds += [
                ("BACKGROUND", (0, 0), (-1, header - 1), head_bg),
                ("VALIGN", (0, header - 1), (-1, header - 1), "MIDDLE"),
            ]
            if zebra:
                for i in range(header, len(rows)):
                    if (i - header) % 2 == 1:
                        cmds.append(("BACKGROUND", (0, i), (-1, i), NEN_BANG))
        t.setStyle(TableStyle(cmds))
        self.add(t)
        self.sp(6)
        return t

    def question(self, num, text, options=None, points=None, note=None):
        """Khối câu hỏi của đề thi."""
        head = "<b>Câu %s.</b> %s" % (num, text)
        if points:
            head += "  <font color='#555555' size='8.6'>[%s]</font>" % points
        block = [Paragraph(head, self.st["q"])]
        if note:
            block.append(Paragraph("<i>%s</i>" % note, self.st["note_ref"]))
        for opt in (options or []):
            block.append(Paragraph(opt, self.st["q_opt"]))
        return self.add(KeepTogether(block))

    def answer(self, title, lines, kind="ans"):
        return self.box(title, lines, kind=kind)


# --------------------------------------------------------------------------
# 7. TIỆN ÍCH KIỂM TRA
# --------------------------------------------------------------------------

def build_doc(filename, title="", author=""):
    """Tạo template PDF chuẩn cho tài liệu."""
    return Doc(filename, title=title, author=author,
               leftMargin=17 * mm, rightMargin=17 * mm,
               topMargin=20 * mm, bottomMargin=16 * mm)
