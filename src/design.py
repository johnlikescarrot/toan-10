# -*- coding: utf-8 -*-
"""Hệ thống trình bày (design system) cho đề cương ôn tập — ReportLab.

Toàn bộ tài liệu dùng một họ font duy nhất (DejaVu Sans) vì font này phủ đủ
dấu tiếng Việt và các kí hiệu toán học dùng trong chương trình lớp 10
(∀, ∃, ⇒, ⇔, ∈, ⊂, ∩, ∪, ∅, ℝ, ℕ, √, ∆, α, β, ≤, ≥ ...).
"""
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Flowable, Frame, KeepTogether,
                                NextPageTemplate, PageTemplate, Paragraph, Spacer,
                                Table, TableStyle, PageBreak)

# --------------------------------------------------------------------------
# 1. Bảng màu
# --------------------------------------------------------------------------
NAVY = colors.HexColor('#17324D')
NAVY_SOFT = colors.HexColor('#2E5476')
TEAL = colors.HexColor('#11756F')
TEAL_LIGHT = colors.HexColor('#E7F2F1')
AMBER = colors.HexColor('#9A6B12')
AMBER_LIGHT = colors.HexColor('#FBF2E1')
PLUM = colors.HexColor('#5B4B8A')
PLUM_LIGHT = colors.HexColor('#F0EDF7')
INK = colors.HexColor('#1E2A33')
GREY = colors.HexColor('#5C6B76')
GREY_LIGHT = colors.HexColor('#F1F4F6')
LINE = colors.HexColor('#C9D4DC')
PAPER = colors.HexColor('#FFFFFF')
CREAM = colors.HexColor('#FAFBFC')
RED = colors.HexColor('#A63D40')
GREEN = colors.HexColor('#2F6B3A')

# --------------------------------------------------------------------------
# 2. Font
# --------------------------------------------------------------------------
FONT_DIR = '/usr/share/fonts/truetype/dejavu'
pdfmetrics.registerFont(TTFont('VN', f'{FONT_DIR}/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('VN-Bold', f'{FONT_DIR}/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('VN-Mono', f'{FONT_DIR}/DejaVuSansMono.ttf'))
pdfmetrics.registerFontFamily('VN', normal='VN', bold='VN-Bold',
                              italic='VN', boldItalic='VN-Bold')

PAGE_W, PAGE_H = A4
M_LEFT = M_RIGHT = 19 * mm
M_TOP = 24 * mm
M_BOTTOM = 19 * mm
FRAME_W = PAGE_W - M_LEFT - M_RIGHT          # 172 mm

# --------------------------------------------------------------------------
# 3. Style chữ
# --------------------------------------------------------------------------
def _style(name, **kw):
    base = dict(fontName='VN', fontSize=9.7, leading=14.6, textColor=INK,
                alignment=TA_JUSTIFY, spaceAfter=0, spaceBefore=0)
    base.update(kw)
    return ParagraphStyle(name, **base)


S = {
    'body':      _style('body', spaceAfter=4.5),
    'body_tight': _style('body_tight', spaceAfter=1.5),
    'lead':      _style('lead', fontSize=10.6, leading=16.4, textColor=NAVY,
                        spaceAfter=6),
    'small':     _style('small', fontSize=8.4, leading=12.2, textColor=GREY),
    'tiny':      _style('tiny', fontSize=7.6, leading=10.5, textColor=GREY),
    'bullet':    _style('bullet', spaceAfter=2.6, leftIndent=11, bulletIndent=1),
    'bullet2':   _style('bullet2', spaceAfter=1.8, leftIndent=22, bulletIndent=12,
                        fontSize=9.5, leading=14),
    'num':       _style('num', spaceAfter=2.6, leftIndent=15, bulletIndent=1),
    'h1':        _style('h1', fontName='VN-Bold', fontSize=15, leading=19,
                        textColor=colors.white, alignment=TA_LEFT),
    'h1_num':    _style('h1_num', fontName='VN-Bold', fontSize=19, leading=21,
                        textColor=colors.white, alignment=TA_CENTER),
    'h2':        _style('h2', fontName='VN-Bold', fontSize=12, leading=16,
                        textColor=NAVY, alignment=TA_LEFT, spaceBefore=9,
                        spaceAfter=4, keepWithNext=1),
    'h3':        _style('h3', fontName='VN-Bold', fontSize=10.3, leading=14.4,
                        textColor=TEAL, alignment=TA_LEFT, spaceBefore=6.5,
                        spaceAfter=2.5, keepWithNext=1),
    'h4':        _style('h4', fontName='VN-Bold', fontSize=9.7, leading=13.6,
                        textColor=NAVY_SOFT, spaceBefore=4, spaceAfter=2,
                        keepWithNext=1),
    'eq':        _style('eq', fontName='VN-Bold', fontSize=10.2, leading=15.6,
                        alignment=TA_CENTER, textColor=NAVY, spaceBefore=3,
                        spaceAfter=5),
    'cell':      _style('cell', fontSize=8.6, leading=12.2, alignment=TA_LEFT),
    'cell_c':    _style('cell_c', fontSize=8.6, leading=12.2, alignment=TA_CENTER),
    'cell_b':    _style('cell_b', fontName='VN-Bold', fontSize=8.6, leading=12.2,
                        textColor=colors.white, alignment=TA_CENTER),
    'cell_h':    _style('cell_h', fontName='VN-Bold', fontSize=8.6, leading=12.2,
                        textColor=NAVY, alignment=TA_LEFT),
    'q':         _style('q', spaceAfter=4, leftIndent=0, fontSize=9.8,
                        leading=15),
    'q_tag':     _style('q_tag', fontName='VN-Bold', fontSize=8.2, leading=12,
                        textColor=TEAL, alignment=TA_LEFT),
    'opt':       _style('opt', fontSize=9.6, leading=14.4, alignment=TA_LEFT),
    'box_title': _style('box_title', fontName='VN-Bold', fontSize=9.2,
                        leading=13, alignment=TA_LEFT, spaceAfter=2),
    'box_body':  _style('box_body', fontSize=9.3, leading=14, alignment=TA_JUSTIFY),
    'toc0':      _style('toc0', fontName='VN-Bold', fontSize=9.6, leading=12.9,
                        textColor=NAVY, alignment=TA_LEFT),
    'toc1':      _style('toc1', fontSize=8.7, leading=11.5, textColor=INK,
                        leftIndent=14, alignment=TA_LEFT),
    'cover_kicker': _style('cover_kicker', fontName='VN-Bold', fontSize=9,
                           leading=13, textColor=colors.HexColor('#9FC3C0'),
                           alignment=TA_LEFT),
    'cover_title': _style('cover_title', fontName='VN-Bold', fontSize=27,
                          leading=32, textColor=colors.white, alignment=TA_LEFT),
    'cover_sub': _style('cover_sub', fontSize=11, leading=17,
                        textColor=colors.HexColor('#D7E3EC'), alignment=TA_LEFT),
}


def PS(name, **kw):
    """ParagraphStyle mặc định dùng font VN (tránh lỗi mất dấu tiếng Việt)."""
    kw.setdefault('fontName', 'VN')
    return ParagraphStyle(name, **kw)


def P(text, style='body'):
    return Paragraph(text, S[style])


# --------------------------------------------------------------------------
# 4. Tiêu đề có đánh số, gắn mục lục + bookmark
# --------------------------------------------------------------------------
class Heading(Paragraph):
    """Paragraph biết tự khai báo với mục lục và outline của PDF."""

    def __init__(self, text, style='h2', level=1, toc_text=None, key=None):
        self.toc_level = level
        self.bookmark_key = key or f'h{abs(hash(text))}'
        self.toc_text = toc_text or text
        super().__init__(text, S[style])


class BandHeading(Table):
    """Dải tiêu đề lớn: bảng 2 ô (số thứ tự + tên phần), tự bookmark."""

    toc_level = 0

    def __init__(self, data, **kw):
        super().__init__(data, **kw)
        self.bookmark_key = None
        self.toc_text = ''

    def draw(self):
        if self.bookmark_key:
            try:
                self.canv.bookmarkPage(self.bookmark_key)
            except Exception:
                pass
        super().draw()


def H1(number, title, kicker=None):
    """Dải tiêu đề lớn của một phần: ô số thứ tự + tên phần."""
    left = Paragraph(str(number), S['h1_num'])
    right_cell = []
    if kicker:
        right_cell.append(Paragraph(kicker.upper(), ParagraphStyle(
            'kick', fontName='VN-Bold', fontSize=7.6, leading=11,
            textColor=colors.HexColor('#A8C6D8'))))
    right_cell.append(Paragraph(title, S['h1']))
    t = BandHeading([[left, right_cell]],
                    colWidths=[14 * mm, FRAME_W - 14 * mm])
    t.toc_text = f'{number}. {title}'
    t.bookmark_key = f'h1-{number}'
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), NAVY),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (0, 0), 4),
        ('RIGHTPADDING', (0, 0), (0, 0), 2),
        ('LEFTPADDING', (1, 0), (1, 0), 4),
        ('RIGHTPADDING', (1, 0), (1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LINEAFTER', (0, 0), (0, 0), 0.8, colors.HexColor('#3E6B8C')),
    ]))
    return [Spacer(1, 2), t, Spacer(1, 9)]


def H2(text):
    return Heading(text, 'h2', level=1)


def H3(text):
    return Paragraph(text, S['h3'])


def H4(text):
    return Paragraph(text, S['h4'])


# --------------------------------------------------------------------------
# 5. Danh sách
# --------------------------------------------------------------------------
def BULL(items, style='bullet', mark='•'):
    out = []
    for it in items:
        if isinstance(it, str):
            out.append(Paragraph(it, S[style], bulletText=mark))
        else:                       # tuple (text, sub-items)
            head, subs = it
            out.append(Paragraph(head, S[style], bulletText=mark))
            for sb in subs:
                out.append(Paragraph(sb, S['bullet2'], bulletText='–'))
    out.append(Spacer(1, 2.5))
    return out


def NUM(items, start=1):
    out = []
    for i, it in enumerate(items, start):
        out.append(Paragraph(it, S['num'], bulletText=f'{i}.'))
    out.append(Spacer(1, 2.5))
    return out


def EQ(text, note=None):
    out = [Paragraph(text, S['eq'])]
    if note:
        out.append(Paragraph(note, S['small']))
    return out


# --------------------------------------------------------------------------
# 6. Bảng
# --------------------------------------------------------------------------
def TBL(header, rows, widths=None, align=None, zebra=True, font_size=8.6,
        header_bg=NAVY, first_col_bold=False):
    """Bảng dữ liệu. widths: list tỉ lệ (sẽ tự co theo bề rộng khung)."""
    n = len(header)
    if widths is None:
        widths = [1] * n
    total = sum(widths)
    col_w = [FRAME_W * w / total for w in widths]

    body_style = ParagraphStyle('cellx', parent=S['cell'], fontSize=font_size,
                                leading=font_size * 1.42)
    center_style = ParagraphStyle('cellxc', parent=S['cell_c'],
                                  fontSize=font_size, leading=font_size * 1.42)
    bold_style = ParagraphStyle('cellxb', parent=S['cell'], fontSize=font_size,
                                leading=font_size * 1.42, fontName='VN-Bold',
                                textColor=NAVY)
    head_style = ParagraphStyle('cellxh', parent=S['cell_b'],
                                fontSize=font_size, leading=font_size * 1.4)

    def wrap(v, st):
        return v if isinstance(v, Flowable) else Paragraph(str(v), st)

    data = [[wrap(h, head_style) for h in header]]
    for r in rows:
        row = []
        for j, v in enumerate(r):
            st = body_style
            if align and j < len(align) and align[j] == 'c':
                st = center_style
            elif first_col_bold and j == 0:
                st = bold_style
            row.append(wrap(v, st))
        data.append(row)

    t = Table(data, colWidths=col_w, repeatRows=1, hAlign='LEFT')
    cmds = [
        ('BACKGROUND', (0, 0), (-1, 0), header_bg),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 4.2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4.2),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('LINEBELOW', (0, 0), (-1, -1), 0.4, LINE),
        ('BOX', (0, 0), (-1, -1), 0.6, LINE),
        ('LINEBELOW', (0, 0), (-1, 0), 0.8, NAVY),
    ]
    if zebra:
        for i in range(1, len(data)):
            if i % 2 == 0:
                cmds.append(('BACKGROUND', (0, i), (-1, i), CREAM))
    t.setStyle(TableStyle(cmds))
    return t


# --------------------------------------------------------------------------
# 7. Hộp gọi chú ý
# --------------------------------------------------------------------------
BOX_STYLE = {
    # kind: (màu viền, màu nền, màu chữ tiêu đề, nhãn mặc định)
    'note':    (TEAL, TEAL_LIGHT, TEAL, 'GHI NHỚ'),
    'warn':    (AMBER, AMBER_LIGHT, AMBER, 'CẨN THẬN'),
    'tip':     (GREEN, colors.HexColor('#EEF6EC'), GREEN, 'MẸO LÀM BÀI'),
    'formula': (PLUM, PLUM_LIGHT, PLUM, 'CÔNG THỨC'),
    'method':  (NAVY_SOFT, colors.HexColor('#EDF2F7'), NAVY, 'PHƯƠNG PHÁP'),
}


def BOX(kind, content, title=None):
    border, bg, ink, label = BOX_STYLE[kind]
    head = title or label
    show_head = head.strip().lower() != label.strip().lower()
    inner = [Paragraph(
        f'<font color="{ink.hexval()}"><b>{label}</b></font>'
        + (f' &nbsp;·&nbsp; <b>{head}</b>' if show_head else ''),
        ParagraphStyle('bxh', fontName='VN-Bold', fontSize=8, leading=11.6,
                       textColor=ink, spaceAfter=3))]
    for c in content:
        if isinstance(c, str):
            inner.append(Paragraph(c, S['box_body']))
        elif isinstance(c, tuple) and c[0] == 'eq':
            inner.append(Paragraph(c[1], ParagraphStyle(
                'bxq', fontName='VN-Bold', fontSize=9.8, leading=15,
                alignment=TA_CENTER, textColor=NAVY, spaceBefore=2,
                spaceAfter=3)))
        elif isinstance(c, list):
            inner.extend(c)
        else:
            inner.append(c)
    t = Table([['', inner]], colWidths=[2.6 * mm, FRAME_W - 2.6 * mm],
              hAlign='LEFT')
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), border),
        ('BACKGROUND', (1, 0), (1, 0), bg),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (0, 0), 0),
        ('RIGHTPADDING', (0, 0), (0, 0), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (1, 0), (1, 0), 9),
        ('RIGHTPADDING', (1, 0), (1, 0), 9),
    ]))
    return [Spacer(1, 3), t, Spacer(1, 5)]


# --------------------------------------------------------------------------
# 8. Khối câu hỏi / lời giải
# --------------------------------------------------------------------------
def OPTIONS(opts, cols=2):
    """opts: list 4 chuỗi (chưa có nhãn A/B/C/D)."""
    labels = 'ABCD'
    cells = [Paragraph(f'<b>{labels[i]}.</b>&nbsp; {o}', S['opt'])
             for i, o in enumerate(opts)]
    if cols == 2:
        data = [cells[0:2], cells[2:4]]
        widths = [FRAME_W * 0.5 - 4 * mm, FRAME_W * 0.5 - 4 * mm]
    else:
        data = [[c] for c in cells]
        widths = [FRAME_W - 8 * mm]
    t = Table(data, colWidths=widths, hAlign='LEFT')
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 1.2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.2),
    ]))
    return t


def QUESTION(num, text, opts=None, tag=None, cols=2):
    """Một câu trắc nghiệm: số câu + nhãn năng lực + nội dung + phương án."""
    parts = []
    tag_html = ''
    if tag:
        tag_html = (f'<font color="{TEAL.hexval()}" size="7.6">'
                    f'&nbsp;&nbsp;[{tag}]</font>')
    parts.append(Paragraph(f'<b>Câu {num}.</b>&nbsp; {text}{tag_html}', S['q']))
    if opts:
        parts.append(OPTIONS(opts, cols=cols))
    parts.append(Spacer(1, 4))
    return parts


def SOL(num, blocks):
    """Lời giải của một câu: tiêu đề nhỏ + nội dung."""
    out = [Paragraph(f'<font color="{TEAL.hexval()}"><b> Câu {num}.</b></font>',
                     ParagraphStyle('soln', fontName='VN-Bold', fontSize=9.4,
                                    leading=13, textColor=TEAL, spaceBefore=6,
                                    spaceAfter=2))]
    for b in blocks:
        if isinstance(b, str):
            out.append(Paragraph(b, S['body']))
        elif isinstance(b, list):
            out.extend(b)
        else:
            out.append(b)
    out.append(Spacer(1, 4))
    return out


def RULE(color=LINE, space_before=6, space_after=6, thickness=0.6):
    t = Table([['']], colWidths=[FRAME_W], rowHeights=[0.1])
    t.setStyle(TableStyle([('LINEABOVE', (0, 0), (-1, -1), thickness, color)]))
    return [Spacer(1, space_before), t, Spacer(1, space_after)]


# --------------------------------------------------------------------------
# 9. Khung trang
# --------------------------------------------------------------------------


def _wrap(text, font, size, max_width):
    """Ngắt dòng đơn giản theo bề rộng chữ (dùng cho vẽ canvas)."""
    words = text.split()
    lines, cur = [], ''
    for w in words:
        trial = (cur + ' ' + w).strip()
        if pdfmetrics.stringWidth(trial, font, size) <= max_width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

class Doc(BaseDocTemplate):
    def __init__(self, filename, **kw):
        super().__init__(filename, pagesize=A4,
                         leftMargin=M_LEFT, rightMargin=M_RIGHT,
                         topMargin=M_TOP, bottomMargin=M_BOTTOM, **kw)
        frame_cover = Frame(0, 0, PAGE_W, PAGE_H, id='cover',
                            leftPadding=0, rightPadding=0,
                            topPadding=0, bottomPadding=0)
        frame_body = Frame(M_LEFT, M_BOTTOM, FRAME_W,
                           PAGE_H - M_TOP - M_BOTTOM, id='body',
                           leftPadding=0, rightPadding=0,
                           topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id='Cover', frames=[frame_cover], onPage=self._cover),
            PageTemplate(id='Body', frames=[frame_body], onPage=self._decorate),
        ])
        self._toc_entries = []

    # -- trang bìa: vẽ hoàn toàn trên canvas
    def _cover(self, canv, doc):
        canv.saveState()
        canv.setFillColor(colors.white)
        canv.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)

        band_h = 160 * mm
        canv.setFillColor(NAVY)
        canv.rect(0, PAGE_H - band_h, PAGE_W, band_h, stroke=0, fill=1)
        canv.setFillColor(TEAL)
        canv.rect(0, PAGE_H - band_h - 2.2 * mm, PAGE_W, 2.2 * mm,
                  stroke=0, fill=1)

        x, right = 22 * mm, PAGE_W - 22 * mm

        # ---- dải nhận diện
        canv.setFillColor(colors.HexColor('#8CBFBA'))
        canv.setFont('VN-Bold', 8.2)
        canv.drawString(x, PAGE_H - 26 * mm,
                        'TRƯỜNG THPT HÀ HUY TẬP   ·   TỔ TOÁN – TIN')
        canv.drawRightString(right, PAGE_H - 26 * mm, 'TÀI LIỆU ÔN THI')
        canv.setStrokeColor(colors.HexColor('#3B5F7C'))
        canv.setLineWidth(0.7)
        canv.line(x, PAGE_H - 30 * mm, right, PAGE_H - 30 * mm)

        # ---- tiêu đề
        canv.setFillColor(colors.white)
        canv.setFont('VN-Bold', 40)
        canv.drawString(x - 1 * mm, PAGE_H - 53 * mm, 'ĐỀ CƯƠNG')
        canv.setFont('VN-Bold', 25)
        canv.drawString(x, PAGE_H - 68 * mm, 'ÔN TẬP GIỮA HỌC KÌ I')
        canv.setFillColor(colors.HexColor('#E8C57A'))
        canv.setFont('VN-Bold', 14)
        canv.drawString(x, PAGE_H - 82 * mm, 'MÔN TOÁN  ·  LỚP 10')
        canv.setFillColor(colors.HexColor('#BFD3E0'))
        canv.setFont('VN', 11)
        canv.drawString(x, PAGE_H - 92 * mm,
                        'Năm học 2026 – 2027   ·   Thời gian làm bài: 90 phút')

        # ---- nhãn chương trình
        chip_w, chip_h, chip_y = 98 * mm, 9.4 * mm, PAGE_H - 110 * mm
        canv.setFillColor(colors.HexColor('#20465F'))
        canv.roundRect(x, chip_y, chip_w, chip_h, 1.6 * mm, stroke=0, fill=1)
        canv.setFillColor(colors.HexColor('#7FD1C8'))
        canv.roundRect(x, chip_y, 1.7 * mm, chip_h, 0.8 * mm, stroke=0, fill=1)
        canv.setFillColor(colors.HexColor('#DCEAE6'))
        canv.setFont('VN', 9)
        canv.drawString(x + 4.8 * mm, chip_y + 3.2 * mm,
                        'Chương trình Kết nối tri thức với cuộc sống')

        # ---- 4 chương
        canv.setFillColor(colors.HexColor('#9DB9CC'))
        canv.setFont('VN-Bold', 7.6)
        canv.drawString(x, PAGE_H - 122 * mm, 'PHẠM VI KIẾN THỨC')
        chaps = [('01', 'Mệnh đề và tập hợp'),
                 ('02', 'Bất phương trình bậc nhất hai ẩn'),
                 ('03', 'Hệ thức lượng trong tam giác'),
                 ('04', 'Vectơ')]
        col_w = (right - x) / 4
        for i, (num, name) in enumerate(chaps):
            cx = x + i * col_w
            canv.setFillColor(colors.HexColor('#E8C57A'))
            canv.setFont('VN-Bold', 10.5)
            canv.drawString(cx, PAGE_H - 130.5 * mm, num)
            canv.setFillColor(colors.HexColor('#D6E2EB'))
            canv.setFont('VN', 7.4)
            yy = PAGE_H - 135.5 * mm
            for line in _wrap(name, 'VN', 7.4, col_w - 4 * mm):
                canv.drawString(cx, yy, line)
                yy -= 3.3 * mm
            if i:
                canv.setStrokeColor(colors.HexColor('#33566F'))
                canv.line(cx - 3.2 * mm, PAGE_H - 131 * mm, cx - 3.2 * mm,
                          PAGE_H - 142 * mm)

        # ---- thẻ số liệu
        canv.setFillColor(TEAL)
        canv.setFont('VN-Bold', 8)
        canv.drawString(x, 124 * mm, 'TÀI LIỆU GỒM')

        cards = [('04', 'CHƯƠNG', ['Tóm tắt lý thuyết, công thức', 'và phương pháp từng dạng']),
                 ('21', 'CÂU HỎI', ['Đề kiểm tra đầy đủ, đúng', 'ma trận và bảng đặc tả']),
                 ('27', 'LỜI GIẢI', ['Chi tiết 21 câu và từng ý', 'đúng – sai, kèm lý do'])]
        gap = 6 * mm
        card_w = (right - x - 2 * gap) / 3
        card_h, card_top = 34 * mm, 119 * mm
        for i, (num, label, desc) in enumerate(cards):
            cx = x + i * (card_w + gap)
            cy = card_top - card_h
            canv.setFillColor(colors.HexColor('#F7F9FA'))
            canv.setStrokeColor(colors.HexColor('#DCE4EA'))
            canv.setLineWidth(0.6)
            canv.roundRect(cx, cy, card_w, card_h, 2 * mm, stroke=1, fill=1)
            canv.setFillColor(TEAL)
            canv.rect(cx, cy, 1.4 * mm, card_h, stroke=0, fill=1)
            canv.setFillColor(NAVY)
            canv.setFont('VN-Bold', 19)
            canv.drawString(cx + 5.5 * mm, cy + card_h - 12 * mm, num)
            canv.setFillColor(TEAL)
            canv.setFont('VN-Bold', 7.2)
            canv.drawString(cx + 5.5 * mm, cy + card_h - 17.5 * mm, label)
            canv.setFillColor(GREY)
            canv.setFont('VN', 7.2)
            dy = cy + card_h - 23 * mm
            for line in desc:
                canv.drawString(cx + 5.5 * mm, dy, line)
                dy -= 3.4 * mm

        # ---- hộp cách dùng
        note_top, note_h = 73 * mm, 40 * mm
        canv.setFillColor(colors.HexColor('#FBF2E1'))
        canv.roundRect(x, note_top - note_h, right - x, note_h, 2 * mm,
                       stroke=0, fill=1)
        canv.setFillColor(AMBER)
        canv.roundRect(x, note_top - note_h, 1.5 * mm, note_h, 0.7 * mm,
                       stroke=0, fill=1)
        canv.setFillColor(colors.HexColor('#7A5410'))
        canv.setFont('VN-Bold', 8)
        canv.drawString(x + 6 * mm, note_top - 7.5 * mm, 'CÁCH DÙNG TÀI LIỆU')
        canv.setFillColor(colors.HexColor('#54452C'))
        canv.setFont('VN', 8)
        body = ('Bước 1 – Hệ thống lý thuyết ở Phần 1: mỗi chương gồm kiến thức trọng tâm, '
                'bảng công thức, các dạng toán thường gặp kèm ví dụ mẫu và lỗi hay mắc. '
                'Bước 2 – Tự làm Phần 2 trong đúng 90 phút, không xem đáp án. '
                'Bước 3 – Đối chiếu Phần 3, ghi lại từng lỗi vào bảng chẩn đoán ở Phần 4. '
                'Bước 4 – Ôn lại theo lộ trình 7 ngày và bảng công thức cuối tài liệu.')
        yy = note_top - 13 * mm
        for line in _wrap(body, 'VN', 8, right - x - 13 * mm):
            canv.drawString(x + 6 * mm, yy, line)
            yy -= 4.0 * mm

        # ---- chân bìa
        canv.setStrokeColor(LINE)
        canv.setLineWidth(0.6)
        canv.line(x, 22 * mm, right, 22 * mm)
        canv.setFillColor(GREY)
        canv.setFont('VN', 7)
        canv.drawString(x, 17 * mm,
                        'Nguồn: “MA TRẬN ĐỀ KIỂM TRA GIỮA KÌ I NĂM HỌC 2026-2027 – MÔN TOÁN, LỚP 10”')
        canv.drawRightString(right, 17 * mm, 'Trường THPT Hà Huy Tập')
        canv.restoreState()

    # -- trang nội dung
    def _decorate(self, canv, doc):
        canv.saveState()
        # header
        canv.setStrokeColor(LINE)
        canv.setLineWidth(0.5)
        canv.line(M_LEFT, PAGE_H - 15.5 * mm, PAGE_W - M_RIGHT, PAGE_H - 15.5 * mm)
        canv.setFont('VN-Bold', 7.3)
        canv.setFillColor(NAVY)
        canv.drawString(M_LEFT, PAGE_H - 13.4 * mm,
                        'ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I  ·  TOÁN 10')
        canv.setFont('VN', 7.3)
        canv.setFillColor(GREY)
        canv.drawRightString(PAGE_W - M_RIGHT, PAGE_H - 13.4 * mm,
                             'Chương trình Kết nối tri thức  ·  Năm học 2026–2027')
        # footer
        canv.line(M_LEFT, 13.5 * mm, PAGE_W - M_RIGHT, 13.5 * mm)
        canv.setFont('VN', 7.3)
        canv.setFillColor(GREY)
        canv.drawString(M_LEFT, 10 * mm,
                        'Đề cương ôn tập Toán 10 – Giữa học kì I')
        canv.setFont('VN-Bold', 8.2)
        canv.setFillColor(NAVY)
        canv.drawRightString(PAGE_W - M_RIGHT, 10 * mm, f'{doc.page}')
        canv.setFillColor(TEAL)
        canv.rect(PAGE_W - M_RIGHT - 12 * mm, 13.0 * mm, 12 * mm, 0.7 * mm,
                  stroke=0, fill=1)
        canv.restoreState()

    def afterFlowable(self, flowable):
        if not isinstance(flowable, (Heading, BandHeading)):
            return
        key = flowable.bookmark_key
        if not key:
            return
        if isinstance(flowable, Heading):
            try:
                self.canv.bookmarkPage(key)
            except Exception:
                pass
        # tránh nhảy cấp outline (PDF không cho phép)
        level = flowable.toc_level
        last = getattr(self, '_outline_level', -1)
        if level > last + 1:
            level = last + 1
        self._outline_level = level
        try:
            self.canv.addOutlineEntry(flowable.toc_text, key, level=level,
                                      closed=False)
        except Exception:
            pass
        self.notify('TOCEntry',
                    (flowable.toc_level, flowable.toc_text, self.page, key))


def toc_styles():
    return [S['toc0'], S['toc1']]


# --------------------------------------------------------------------------
# 10. Tiện ích
# --------------------------------------------------------------------------
def flatten(seq):
    """Làm phẳng danh sách lồng nhau (các helper trả về list flowable)."""
    out = []
    for x in seq:
        if isinstance(x, (list, tuple)) and not isinstance(x, Flowable):
            out.extend(flatten(x))
        elif x is not None:
            out.append(x)
    return out


def page_break():
    return [PageBreak()]


def PRACTICE(items, answers, title='Bài tập tự luyện'):
    """Khối bài tập tự luyện + đáp án ngắn ở cuối mỗi chương."""
    q_style = PS('pq', fontSize=9.3, leading=14.2, textColor=INK,
                 leftIndent=16, bulletIndent=2, spaceAfter=3)
    out = [Spacer(1, 4), Paragraph(title, S['h2']), Spacer(1, 1)]
    for i, it in enumerate(items, 1):
        out.append(Paragraph(it, q_style, bulletText=f'{i}.'))
    out.append(Spacer(1, 5))
    ans = [Paragraph('<b>Đáp án.</b>', PS(
        'ansh', fontName='VN-Bold', fontSize=8.2, leading=11, textColor=TEAL,
        spaceAfter=2))]
    ans.append(Paragraph(answers, PS('ansb', fontSize=8.4, leading=12.4,
                                     textColor=GREY)))
    t = Table([['', ans]], colWidths=[1.6 * mm, FRAME_W - 1.6 * mm], hAlign='LEFT')
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), TEAL),
        ('BACKGROUND', (1, 0), (1, 0), colors.HexColor('#F4F8F8')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (0, 0), 0),
        ('RIGHTPADDING', (0, 0), (0, 0), 0),
        ('LEFTPADDING', (1, 0), (1, 0), 8),
        ('RIGHTPADDING', (1, 0), (1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    out.append(t)
    return [KeepTogether([out[0]])] + out[1:-1] + [KeepTogether([out[-1]])]
