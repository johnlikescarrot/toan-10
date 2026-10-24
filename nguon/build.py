# -*- coding: utf-8 -*-
"""Render the Vietnamese revision guide (đề cương) to PDF with ReportLab."""
import os, re, sys, glob
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, PageBreak, KeepTogether,
                                NextPageTemplate, Flowable, HRFlowable)
from reportlab.platypus.tableofcontents import TableOfContents

HERE = os.path.dirname(os.path.abspath(__file__))
FD = '/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('Body', FD + 'DejaVuSerif.ttf'))
pdfmetrics.registerFont(TTFont('Body-Bold', FD + 'DejaVuSerif-Bold.ttf'))
pdfmetrics.registerFont(TTFont('UI', FD + 'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('UI-Bold', FD + 'DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Mono', FD + 'DejaVuSansMono.ttf'))
pdfmetrics.registerFontFamily('Body', normal='Body', bold='Body-Bold',
                              italic='Body', boldItalic='Body-Bold')
pdfmetrics.registerFontFamily('UI', normal='UI', bold='UI-Bold',
                              italic='UI', boldItalic='UI-Bold')

# ---------------------------------------------------------------- palette
NAVY   = colors.HexColor('#152C54')
BLUE   = colors.HexColor('#1F4E9C')
BLUE_L = colors.HexColor('#EAF1FA')
BLUE_B = colors.HexColor('#B7CBE6')
RED    = colors.HexColor('#A61B1B')
RED_L  = colors.HexColor('#FBEDED')
GREEN  = colors.HexColor('#1B5E20')
GREEN_L= colors.HexColor('#ECF6EC')
GREEN_B= colors.HexColor('#A5CCA5')
AMBER  = colors.HexColor('#8A5A00')
AMBER_L= colors.HexColor('#FFF7E6')
AMBER_B= colors.HexColor('#EBC98A')
GREY   = colors.HexColor('#5A5A5A')
GREY_L = colors.HexColor('#F3F3F1')
GREY_B = colors.HexColor('#CFCFCB')
TEAL   = colors.HexColor('#0F5A5A')
TEAL_L = colors.HexColor('#E8F4F4')

PAGE_W, PAGE_H = A4
LM = RM = 1.9 * cm
TM = 2.05 * cm
BM = 1.75 * cm

# ---------------------------------------------------------------- styles
S = {}
def st(name, **kw):
    S[name] = ParagraphStyle(name, **kw)

base = dict(fontName='Body', fontSize=9.7, leading=14.6, textColor=colors.HexColor('#1A1A1A'),
            alignment=TA_JUSTIFY, spaceAfter=3, hyphenationLang='vi')

st('Body', **base)
st('BodyC', parent=S['Body'], alignment=TA_CENTER)
st('H1', fontName='UI-Bold', fontSize=17.5, leading=21, textColor=NAVY,
   spaceBefore=0, spaceAfter=2, alignment=TA_LEFT)
st('H1sub', fontName='UI', fontSize=9, leading=13, textColor=RED, spaceAfter=10)
st('H2', fontName='UI-Bold', fontSize=13, leading=17, textColor=colors.white,
   keepWithNext=1,
   backColor=NAVY, borderPadding=(5, 7, 6, 7), spaceBefore=13, spaceAfter=9,
   alignment=TA_LEFT, leftIndent=0)
st('H3', fontName='UI-Bold', fontSize=11, leading=15, textColor=BLUE,
   keepWithNext=1,
   spaceBefore=11, spaceAfter=5, alignment=TA_LEFT,
   borderPadding=(0, 0, 0, 0))
st('H4', fontName='UI-Bold', fontSize=9.6, leading=13.5, textColor=NAVY,
   keepWithNext=1,
   backColor=BLUE_L, borderPadding=(3.5, 6, 3.5, 6), spaceBefore=8, spaceAfter=4,
   alignment=TA_LEFT)
st('Bar', fontName='UI-Bold', fontSize=9.4, leading=13, textColor=colors.white,
   keepWithNext=1,
   backColor=TEAL, borderPadding=(3.5, 6, 3.5, 6), spaceBefore=8, spaceAfter=5,
   alignment=TA_LEFT)
st('Bullet', parent=S['Body'], leftIndent=15, bulletIndent=4, spaceAfter=2.6,
   alignment=TA_JUSTIFY, bulletFontName='UI', bulletFontSize=9,
   bulletColor=BLUE)
st('Num', parent=S['Body'], leftIndent=17, bulletIndent=2, spaceAfter=2.6,
   bulletFontName='UI', bulletFontSize=9, bulletColor=RED)
st('Note', parent=S['Body'], fontSize=9.4, leading=14, backColor=BLUE_L,
   borderColor=BLUE_B, borderWidth=0.6, borderPadding=(5, 7, 5, 7),
   spaceBefore=5, spaceAfter=7, leftIndent=0, rightIndent=0)
st('Warn', parent=S['Note'], backColor=AMBER_L, borderColor=AMBER_B, textColor=AMBER)
st('Key', parent=S['Note'], backColor=GREEN_L, borderColor=GREEN_B, textColor=colors.HexColor('#12300F'))
st('Teal', parent=S['Note'], backColor=TEAL_L, borderColor=colors.HexColor('#8FC0C0'), textColor=colors.HexColor('#0B3B3B'))
st('MathBox', fontName='UI', fontSize=11, leading=18, alignment=TA_CENTER,
   textColor=NAVY, backColor=GREY_L, borderPadding=(5, 4, 5, 4), spaceBefore=4, spaceAfter=7)
st('MathInline', fontName='UI', fontSize=9.7, leading=14.6, textColor=colors.HexColor('#10305C'))
st('Q', parent=S['Body'], spaceBefore=6, spaceAfter=2, leftIndent=0,
   alignment=TA_JUSTIFY)
st('QC', parent=S['Body'], spaceBefore=5, spaceAfter=1)
st('Opt', parent=S['Body'], fontSize=9.5, leading=13.6, alignment=TA_LEFT, spaceAfter=0)
st('Sol', parent=S['Body'], fontSize=9.4, leading=14, textColor=colors.HexColor('#222222'),
   leftIndent=10, spaceAfter=2)
st('Small', fontName='UI', fontSize=7.8, leading=11, textColor=GREY, alignment=TA_LEFT)
st('TableH', fontName='UI-Bold', fontSize=8.2, leading=10.6, textColor=colors.white,
   alignment=TA_CENTER)
st('TableCell', fontName='UI', fontSize=8.2, leading=11, alignment=TA_LEFT)
st('TableCellC', fontName='UI', fontSize=8.2, leading=11, alignment=TA_CENTER)
st('Section', fontName='UI-Bold', fontSize=8.8, leading=12, textColor=NAVY,
   alignment=TA_LEFT)
st('CoverK', fontName='UI-Bold', fontSize=10.5, leading=15, textColor=RED, alignment=TA_CENTER)
st('CoverT', fontName='UI-Bold', fontSize=26, leading=32, textColor=NAVY, alignment=TA_CENTER)
st('CoverS', fontName='UI', fontSize=12.5, leading=19, textColor=colors.HexColor('#333333'), alignment=TA_CENTER)
st('TOC1', fontName='UI-Bold', fontSize=10.2, leading=16, textColor=NAVY, spaceBefore=6)
st('TOC2', fontName='UI', fontSize=9.2, leading=14.5, textColor=colors.HexColor('#222222'), leftIndent=16)

FONT_UI = 'UI'

# ---------------------------------------------------------------- inline markup
def inline(t):
    """**bold**  @@accent-blue@@  ##accent-red##  %%green%%  ~~ui-blue~~"""
    t = t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    t = re.sub(r'\*\*(.+?)\*\*', r'<font name="UI-Bold">\1</font>', t)
    t = re.sub(r'@@(.+?)@@', r'<font name="UI-Bold" color="#1F4E9C">\1</font>', t)
    t = re.sub(r'##(.+?)##', r'<font name="UI-Bold" color="#A61B1B">\1</font>', t)
    t = re.sub(r'%%(.+?)%%', r'<font name="UI-Bold" color="#1B5E20">\1</font>', t)
    t = re.sub(r'~~(.+?)~~', r'<font name="UI" color="#10305C">\1</font>', t)
    t = t.replace('*', '')
    # glyphs missing from DejaVu Serif (and Serif-Bold) -> force DejaVu Sans
    for ch in '∅∖✔✘✦⋮⋯☐☑':
        if ch in t:
            t = t.replace(ch, '<font name="UI" face="UI">%s</font>' % ch)
    return t


def P(text, style='Body'):
    return Paragraph(inline(text), S[style])


# ---------------------------------------------------------------- doc template
class Doc(BaseDocTemplate):
    def __init__(self, fn, **kw):
        BaseDocTemplate.__init__(self, fn, pagesize=A4,
                                 leftMargin=LM, rightMargin=RM,
                                 topMargin=TM, bottomMargin=BM,
                                 title='Đề cương ôn tập Giữa học kì I - Toán 10 (Kết nối tri thức) - NH 2026-2027',
                                 author='Tổ Toán - Tin, Trường THPT Hà Huy Tập',
                                 subject='Đề cương ôn tập giữa học kì I môn Toán lớp 10',
                                 creator='ReportLab',
                                 keywords='đề cương ôn tập, toán 10, giữa học kì 1, kết nối tri thức, 2026-2027, mệnh đề, tập hợp, bất phương trình bậc nhất hai ẩn, hệ thức lượng, vectơ',
                                 **kw)
        fw = PAGE_W - LM - RM
        cover = Frame(LM, BM, fw, PAGE_H - BM - TM, id='cover',
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        body = Frame(LM, BM, fw, PAGE_H - BM - TM, id='body',
                     leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id='Cover', frames=[cover], onPage=self.cover_page),
            PageTemplate(id='Body', frames=[body], onPage=self.body_page),
        ])
        self._toc_seen = set()

    def handle_documentBegin(self):
        self._toc_seen = set()
        BaseDocTemplate.handle_documentBegin(self)

    # ---- page furniture -------------------------------------------------
    def cover_page(self, c, doc):
        c.saveState()
        c.setFillColor(NAVY)
        c.rect(0, PAGE_H - 1.05 * cm, PAGE_W, 1.05 * cm, stroke=0, fill=1)
        c.setFillColor(RED)
        c.rect(0, PAGE_H - 1.25 * cm, PAGE_W, 0.2 * cm, stroke=0, fill=1)
        c.setFillColor(NAVY)
        c.rect(0, 0, PAGE_W, 0.85 * cm, stroke=0, fill=1)
        c.setFont('UI', 8)
        c.setFillColor(colors.white)
        c.drawCentredString(PAGE_W / 2, 0.32 * cm,
                            'Tài liệu lưu hành nội bộ - Tổ Toán - Tin, Trường THPT Hà Huy Tập')
        c.restoreState()

    def body_page(self, c, doc):
        c.saveState()
        # header
        c.setStrokeColor(BLUE_B)
        c.setLineWidth(0.7)
        c.line(LM, PAGE_H - TM + 0.55 * cm, PAGE_W - RM, PAGE_H - TM + 0.55 * cm)
        c.setFont('UI', 7.6)
        c.setFillColor(GREY)
        c.drawString(LM, PAGE_H - TM + 0.72 * cm,
                     'ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I  •  TOÁN 10  •  KẾT NỐI TRI THỨC VỚI CUỘC SỐNG')
        c.drawRightString(PAGE_W - RM, PAGE_H - TM + 0.72 * cm, 'NĂM HỌC 2026 - 2027')
        # footer
        c.line(LM, BM - 0.42 * cm, PAGE_W - RM, BM - 0.42 * cm)
        c.setFont('UI-Bold', 8.2)
        c.setFillColor(NAVY)
        c.drawCentredString(PAGE_W / 2, BM - 0.92 * cm, 'Trang %d' % (doc.page - 1))
        c.restoreState()

    # ---- bookmarks + TOC ------------------------------------------------
    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph):
            name = flowable.style.name
            if name in ('H1', 'H2'):
                level = 0 if name == 'H1' else 1
                text = flowable.getPlainText()
                if text in self._toc_seen or text.strip().upper() == 'MỤC LỤC':
                    return
                self._toc_seen.add(text)
                key = 'sec%d' % id(flowable)
                self.canv.bookmarkPage(key)
                self.canv.addOutlineEntry(text, key, level=level, closed=False)
                link = '<a href="#%s" color="#1A1A1A">%s</a>' % (key, text)
                self.notify('TOCEntry', (level, link, self.page, key))


# ---------------------------------------------------------------- builders
CW = PAGE_W - LM - RM
BLANK_ROW = 26


def two_col_options(items):
    """items: list of strings like 'a) ...' -> 2x2 table."""
    cells = [[Paragraph(inline(x), S['Opt']) for x in items[i:i + 2]] for i in range(0, len(items), 2)]
    while len(cells[-1]) < 2:
        cells[-1].append(Paragraph('', S['Opt']))
    t = Table(cells, colWidths=[CW * 0.5 - 2, CW * 0.5 - 2])
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 1.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5),
    ]))
    return t


def make_table(rows, widths=None, header=True, zebra=True, align=None, fs=None):
    """rows: list of list of str (first row = header)."""
    ncol = max(len(r) for r in rows)
    rows = [r + [''] * (ncol - len(r)) for r in rows]
    data = []
    for i, r in enumerate(rows):
        line = []
        for j, cell in enumerate(r):
            style = 'TableH' if (i == 0 and header) else ('TableCellC' if (align and align[j] == 'c') else 'TableCell')
            line.append(Paragraph(inline(cell), S[style]))
        data.append(line)
    if widths is None:
        widths = [CW / ncol] * ncol
    else:
        tot = sum(widths)
        widths = [w / tot * CW for w in widths]
    blanks = [18] * len(data)
    for i in range(1 if header else 0, len(data)):
        if all(r[j].strip() == '' for j in range(1, ncol)):
            blanks[i] = 21
    if header and len(data) > 1 and all(rows[i][j].strip() == '' for i in range(1, len(rows)) for j in range(ncol)):
        t = Table(data, colWidths=widths, repeatRows=1,
                  rowHeights=[None] + [BLANK_ROW] * (len(data) - 1))
        t.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('GRID', (0, 0), (-1, -1), 0.5, GREY_B),
            ('BACKGROUND', (0, 0), (-1, 0), NAVY),
            ('LEFTPADDING', (0, 0), (-1, -1), 4), ('RIGHTPADDING', (0, 0), (-1, -1), 4),
            ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]))
        return t
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0,
              rowHeights=blanks if any(h == 21 for h in blanks) else None)
    cmds = [
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.45, GREY_B),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
    ]
    if header:
        cmds += [('BACKGROUND', (0, 0), (-1, 0), NAVY)]
    if zebra:
        for i in range(1 if header else 0, len(data)):
            if (i % 2) == 0:
                cmds.append(('BACKGROUND', (0, i), (-1, i), GREY_L))
    t.setStyle(TableStyle(cmds))
    return t


def big_table(rows, widths=None, header_rows=1, align=None, fs='TableCell'):
    """Table with possibly 2 header rows; a row whose first cell starts with
    '~' becomes a merged section row."""
    ncol = max(len(r) for r in rows)
    rows = [r + [''] * (ncol - len(r)) for r in rows]
    data = []
    spans = []
    for i, r in enumerate(rows):
        line = []
        section = r[0].startswith('~')
        for j, cell in enumerate(r):
            if section:
                sty = 'Section'
            else:
                sty = 'TableH' if i < header_rows else fs
            c = cell[1:].strip() if (section and j == 0) else cell
            if section and j == 0:
                c = c.replace('~', '')
            line.append(Paragraph(inline(c), S[sty]))
        data.append(line)
        if section:
            spans.append(i)
    ncol = max(len(r) for r in rows)
    if widths is None:
        widths = [CW / ncol] * ncol
    else:
        tot = sum(widths)
        widths = [w / tot * CW for w in widths]
    t = Table(data, colWidths=widths, repeatRows=header_rows)
    cmds = [('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('GRID', (0, 0), (-1, -1), 0.45, GREY_B),
            ('LEFTPADDING', (0, 0), (-1, -1), 4), ('RIGHTPADDING', (0, 0), (-1, -1), 4),
            ('TOPPADDING', (0, 0), (-1, -1), 3.2), ('BOTTOMPADDING', (0, 0), (-1, -1), 3.2),
            ('BACKGROUND', (0, 0), (-1, header_rows - 1), NAVY)]
    for i in range(header_rows, len(data)):
        if (i - header_rows) % 2 == 1 and i not in spans:
            cmds.append(('BACKGROUND', (0, i), (-1, i), GREY_L))
    for i in spans:
        cmds += [('SPAN', (0, i), (-1, i)),
                 ('BACKGROUND', (0, i), (-1, i), BLUE_L)]
    t.setStyle(TableStyle(cmds))
    return t


# ---------------------------------------------------------------- parser
def build_story(text):
    story = []
    lines = text.split('\n')
    i = 0
    n = len(lines)
    pending_opts = []
    while i < n:
        raw = lines[i]
        line = raw.rstrip()
        s = line.strip()
        i += 1
        if not s:
            continue
        if s.startswith('//'):
            continue
        if s == '#PAGE':
            story.append(PageBreak()); continue
        if s == '#COVER':
            story.append(NextPageTemplate('Body')); story.append(PageBreak()); continue
        if s == '#TOC':
            toc = TableOfContents()
            toc.levelStyles = [S['TOC1'], S['TOC2']]
            toc.dotsMinLevel = 0
            story.append(toc)
            story.append(Spacer(1, 6))
            continue
        if s.startswith('#H1 '):
            story.append(Spacer(1, 2))
            story.append(Paragraph(inline(s[4:]), S['H1']))
            story.append(HRFlowable(width='100%', thickness=2, color=RED, spaceBefore=2, spaceAfter=9))
            continue
        if s.startswith('#H2 '):
            story.append(Paragraph(inline(s[4:]), S['H2']))
            continue
        if s.startswith('#H3 '):
            story.append(Paragraph(inline(s[4:]), S['H3']))
            continue
        if s.startswith('#H4 '):
            story.append(Paragraph(inline(s[4:]), S['H4']))
            continue
        if s.startswith('#BAR '):
            story.append(Paragraph(inline(s[5:]), S['Bar']))
            continue
        if s.startswith('#M '):
            story.append(Paragraph(inline(s[3:]), S['MathBox']))
            continue
        if s.startswith('#MATHBLOCK'):
            block = []
            while i < n and lines[i].strip() != '#ENDM':
                block.append(lines[i].strip()); i += 1
            i += 1
            body = '<br/>'.join(inline(x) for x in block)
            story.append(Paragraph(body, ParagraphStyle(
                'MB', parent=S['MathBox'], leading=19)))
            continue
        if s.startswith('#P '):
            story.append(Paragraph(inline(s[3:]), S['Body'])); continue
        if s.startswith('#PC '):
            story.append(Paragraph(inline(s[3:]), S['BodyC'])); continue
        if s.startswith('#B '):
            story.append(Paragraph(inline(s[3:]), S['Bullet'], bulletText='•')); continue
        if s.startswith('#D '):   # dash bullet
            story.append(Paragraph(inline(s[3:]), S['Bullet'], bulletText='–')); continue
        if s.startswith('#N '):
            story.append(Paragraph(inline(s[3:]), S['Num'], bulletText='')); continue
        if s.startswith('#S '):
            story.append(Paragraph(inline(s[3:]), S['Sol'])); continue
        if s.startswith('#SM '):
            story.append(Paragraph(inline(s[3:]), S['Small'])); continue
        if s.startswith('#NOTE '):
            story.append(Paragraph(inline(s[6:]), S['Note'])); continue
        if s.startswith('#WARN '):
            story.append(Paragraph(inline(s[6:]), S['Warn'])); continue
        if s.startswith('#KEY '):
            story.append(Paragraph(inline(s[5:]), S['Key'])); continue
        if s.startswith('#TEAL '):
            story.append(Paragraph(inline(s[6:]), S['Teal'])); continue
        if s.startswith('#Q '):
            block = [Paragraph(inline(s[3:]), S['QC'])]
            opts = []
            j = i
            while j < n and lines[j].strip().startswith('#O '):
                opts.append(lines[j].strip()[3:]); j += 1
            i = j
            if opts:
                block.append(two_col_options(opts))
            story.append(KeepTogether(block))
            continue
        if s.startswith('#O ') or s.startswith('#O2 '):
            items = []
            if s.startswith('#O '):
                items.append(s[3:])
            else:
                items.append(s[4:])
            while i < n and lines[i].strip().startswith('#O '):
                items.append(lines[i].strip()[3:]); i += 1
            story.append(two_col_options(items))
            continue
        if s.startswith('#SP '):
            story.append(Spacer(1, float(s[4:]))); continue
        if s.startswith('#LINE'):
            story.append(HRFlowable(width='100%', thickness=0.6, color=GREY_B,
                                    spaceBefore=4, spaceAfter=4)); continue
        if s.startswith('#TABLE'):
            rows = []
            while i < n and not lines[i].strip().startswith('#ENDTABLE'):
                rl = lines[i].strip()
                if rl and not rl.startswith('//'):
                    rows.append([c.strip() for c in rl.split('|')])
                i += 1
            i += 1
            story.append(make_table(rows))
            story.append(Spacer(1, 6))
            continue
        if s.startswith('#BIGTABLE'):
            spec = s[len('#BIGTABLE'):].strip()
            hr = 1
            wid = None
            if spec:
                if '|' in spec:
                    a, b = spec.split('|', 1)
                    hr = int(a.strip()) if a.strip() else 1
                    wid = [float(x) for x in b.split(',')]
                else:
                    hr = int(spec)
            rows = []
            while i < n and not lines[i].strip().startswith('#ENDBIGTABLE'):
                rl = lines[i].strip()
                if rl and not rl.startswith('//'):
                    rows.append([c.strip() for c in rl.split('|')])
                i += 1
            i += 1
            story.append(big_table(rows, widths=wid, header_rows=hr))
            story.append(Spacer(1, 6))
            continue
        # default paragraph
        story.append(Paragraph(inline(s), S['Body']))
    return story


def main():
    src = os.path.join(HERE, 'content')
    parts = sorted(glob.glob(os.path.join(src, '*.txt')))
    text = '\n'.join(open(p, encoding='utf-8').read() for p in parts)
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'de-cuong.pdf')
    doc = Doc(out)
    story = build_story(text)
    doc.multiBuild(story)
    print('OK ->', out, doc.page, 'pages')


if __name__ == '__main__':
    main()
