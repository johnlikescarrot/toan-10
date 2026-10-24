# -*- coding: utf-8 -*-
"""Phần 2 – Đề kiểm tra hoàn chỉnh (21 câu)."""
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.units import mm
from reportlab.platypus import Flowable, Paragraph, Spacer, Table, TableStyle

from design import (AMBER, BOX, CREAM, FRAME_W, GREY, GREY_LIGHT, H1, H2, H3,
                    INK, LINE, NAVY, NAVY_SOFT, P, S, TBL, TEAL, TEAL_LIGHT, PS)


# --------------------------------------------------------------------------
# Các khối trình bày riêng của phần đề
# --------------------------------------------------------------------------
def section_band(code, title, meta):
    """Dải tiêu đề nhỏ của từng phần trong đề (I, II, III, IV)."""
    left = Paragraph(f'<b>{code}</b>', PS(
        'pc', fontName='VN-Bold', fontSize=14, leading=16, textColor=colors.white,
        alignment=TA_CENTER))
    mid = Paragraph(f'<b>{title}</b>', PS(
        'pt', fontName='VN-Bold', fontSize=10.2, leading=14, textColor=colors.white,
        alignment=TA_LEFT))
    right = Paragraph(meta, PS(
        'pm', fontSize=7.8, leading=11, textColor=colors.HexColor('#BBD2DE'),
        alignment=TA_CENTER))
    t = Table([[left, mid, right]], colWidths=[10 * mm, FRAME_W - 44 * mm, 34 * mm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), TEAL),
        ('BACKGROUND', (1, 0), (2, 0), NAVY),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (0, 0), 2),
        ('LEFTPADDING', (1, 0), (1, 0), 7),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    return [Spacer(1, 6), t, Spacer(1, 7)]


def mc(num, text, options, tag, level_label, points='0,25'):
    lab = Paragraph(f'<b>Câu {num}.</b>', PS(
        'ql', fontName='VN-Bold', fontSize=9.8, leading=14, textColor=NAVY,
        alignment=TA_LEFT))
    body = Paragraph(text, PS(
        'qb', fontSize=9.8, leading=14.6, textColor=INK, alignment=TA_LEFT))
    meta = Paragraph(f'<font size="7.4" color="#11756F">[{tag}] {level_label}</font>'
                     f'<br/><font size="7.4" color="#7A8A96">{points} điểm</font>',
                     PS('qm', fontSize=7.4, leading=10,
                                    alignment=TA_CENTER))
    head = Table([[lab, body, meta]],
                 colWidths=[18 * mm, FRAME_W - 18 * mm - 25 * mm, 25 * mm])
    head.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (0, 0), 2),
        ('RIGHTPADDING', (1, 0), (1, 0), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    labels = 'ABCD'
    cells = [Paragraph(f'<b>{labels[i]}.</b>&nbsp; {o}', PS(
        f'op{i}', fontSize=9.6, leading=14, textColor=INK, alignment=TA_LEFT,
        leftIndent=0)) for i, o in enumerate(options)]
    grid = Table([[cells[0], cells[1]], [cells[2], cells[3]]],
                 colWidths=[(FRAME_W - 35 * mm) / 2 + 4 * mm,
                            (FRAME_W - 35 * mm) / 2 - 4 * mm])
    grid.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
    ]))
    wrapper = Table([['', grid]], colWidths=[18 * mm, FRAME_W - 18 * mm])
    wrapper.setStyle(TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    return [Spacer(1, 3), head, wrapper, Spacer(1, 6)]


def ds(num, lead, items, points='1,0'):
    """Câu trắc nghiệm đúng/sai với 4 ý a, b, c, d."""
    lab = Paragraph(f'<b>Câu {num}.</b>', PS(
        'dl', fontName='VN-Bold', fontSize=9.8, leading=14, textColor=NAVY))
    body = Paragraph(lead, PS(
        'db', fontSize=9.8, leading=14.6, textColor=INK))
    head = Table([[lab, body]], colWidths=[18 * mm, FRAME_W - 18 * mm])
    head.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    rows = [[Paragraph('<b>Ý</b>', S['cell_c']),
             Paragraph('<b>Khẳng định</b>', S['cell_h']),
             Paragraph('<b>Đúng</b>', S['cell_c']),
             Paragraph('<b>Sai</b>', S['cell_c'])]]
    for i, it in enumerate(items):
        rows.append([
            Paragraph(f'<b>{labels_ds[i]})</b>', S['cell']),
            Paragraph(it, PS('dsi', fontSize=9.5, leading=13.6,
                                         textColor=INK)),
            Paragraph('☐', PS('bx', fontName='VN', fontSize=12,
                                          leading=13, alignment=TA_CENTER,
                                          textColor=GREY)),
            Paragraph('☐', PS('bx2', fontName='VN', fontSize=12,
                                          leading=13, alignment=TA_CENTER,
                                          textColor=GREY)),
        ])
    t = Table(rows, colWidths=[9 * mm, FRAME_W - 37 * mm, 14 * mm, 14 * mm],
              repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), TEAL_LIGHT),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 3.4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.4),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('LINEBELOW', (0, 0), (-1, -1), 0.4, LINE),
        ('BOX', (0, 0), (-1, -1), 0.5, LINE),
        ('LINEAFTER', (1, 0), (1, -1), 0.4, LINE),
        ('LINEAFTER', (2, 0), (2, -1), 0.4, LINE),
    ]))
    tail = Paragraph(f'<font size="7.4" color="#7A8A96">Mỗi ý đúng được tính theo quy chế: '
                     f'1 ý 0,1 · 2 ý 0,25 · 3 ý 0,5 · 4 ý 1,0 điểm.</font>',
                     PS('dt', fontSize=7.4, leading=10,
                                    textColor=GREY, spaceBefore=2))
    return [Spacer(1, 3), head, t, Spacer(1, 2), tail, Spacer(1, 7)]


labels_ds = 'abcd'


class AnswerLine(Flowable):
    """Dòng “Trả lời: ..........” cho câu trả lời ngắn."""

    def __init__(self, label='Trả lời:', width=None):
        super().__init__()
        self.label = label
        self.width = width or FRAME_W
        self.height = 8 * mm

    def draw(self):
        c = self.canv
        c.setFont('VN-Bold', 9)
        c.setFillColor(NAVY)
        c.drawString(0, 2 * mm, self.label)
        x0 = pdfmetrics_width(self.label, 'VN-Bold', 9) + 2.5 * mm
        c.setStrokeColor(GREY)
        c.setLineWidth(0.5)
        c.setDash(1, 2)
        c.line(x0, 1.6 * mm, self.width - 4 * mm, 1.6 * mm)
        c.setDash()


def pdfmetrics_width(text, font, size):
    from reportlab.pdfbase.pdfmetrics import stringWidth
    return stringWidth(text, font, size)


def tln(num, text, tag, level_label, unit='', points='0,5'):
    lab = Paragraph(f'<b>Câu {num}.</b>', PS(
        'tl', fontName='VN-Bold', fontSize=9.8, leading=14, textColor=NAVY))
    inner = [Paragraph(text, PS('tb', fontSize=9.8, leading=14.6,
                                            textColor=INK))]
    meta = f'<font size="7.4" color="#11756F">[{tag}] {level_label}</font> &nbsp;·&nbsp; ' \
           f'<font size="7.4" color="#7A8A96">{points} điểm</font>'
    if unit:
        meta += f'<br/><font size="7.2" color="#96A5AF">{unit}</font>'
    inner.append(Spacer(1, 1.5))
    inner.append(Paragraph(meta, PS('tm', fontSize=7.4, leading=10.4)))
    inner.append(AnswerLine())
    t = Table([[lab, inner]], colWidths=[17 * mm, FRAME_W - 17 * mm])
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    return [Spacer(1, 3), t, Spacer(1, 6)]


def essay(num, text, points_label, work_lines=4):
    lab = Paragraph(f'<b>Câu {num}.</b>', PS(
        'el', fontName='VN-Bold', fontSize=9.9, leading=14.4, textColor=NAVY))
    inner = [Paragraph(text, PS('eb', fontSize=9.9, leading=15,
                                            textColor=INK))]
    inner.append(Spacer(1, 2))
    inner.append(Paragraph(f'<font size="7.4" color="#7A8A96">{points_label}</font>',
                           PS('em', fontSize=7.4, leading=10)))
    t = Table([[lab, inner]], colWidths=[17 * mm, FRAME_W - 17 * mm])
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    return [Spacer(1, 6), t, Spacer(1, 4)]


# --------------------------------------------------------------------------
def part():
    e = []
    e += H1('II', 'Đề kiểm tra giữa học kì I', 'Phần 2  ·  Đề chính thức')
    e += [P('Đề gồm 21 câu, làm trong <b>90 phút</b>. Cấu trúc và thang điểm bám đúng ma trận: '
            '12 câu trắc nghiệm (3,0 điểm), 2 câu đúng/sai (2,0 điểm), 4 câu trả lời ngắn '
            '(2,0 điểm) và 3 câu tự luận (3,0 điểm). Hãy chuẩn bị giấy nháp, bút và máy tính cầm '
            'tay; không xem Phần 3 trước khi hết giờ.', 'lead')]

    e += [TBL(['Thông tin', 'Nội dung'],
              [['Môn', 'Toán – Lớp 10'],
               ['Chương trình', 'Kết nối tri thức với cuộc sống'],
               ['Thời gian', '90 phút (không kể thời gian phát đề)'],
               ['Hình thức', 'Trắc nghiệm khách quan kết hợp tự luận'],
               ['Phạm vi', 'Chương 1, 2, 3 và bài 1 của chương 4 (khái niệm vectơ)'],
               ['Dụng cụ được dùng', 'Bút, thước kẻ, compa, máy tính cầm tay']],
              widths=[1.5, 6.4], first_col_bold=True)]
    e += [Spacer(1, 4)]

    e += BOX('tip', [
        '<b>Phân bổ 90 phút:</b> 30 phút cho 12 câu trắc nghiệm (trung bình 2,5 phút/câu), '
        '15 phút cho 2 câu đúng/sai, 15 phút cho 4 câu trả lời ngắn, 30 phút cho 3 câu tự luận.',
        'Làm câu dễ trước. Câu 21 (tối ưu) nên để cuối cùng vì dù sao cũng chỉ 1 điểm.',
        'Với câu đúng/sai, hãy đánh dấu ngay khi chắc chắn và để lại các ý còn do dự để quay lại.'],
        'Chiến lược làm bài')

    # ------------------------------------------------------------------
    e += section_band('I', 'TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN', '12 câu · 3,0 điểm<br/>0,25 điểm/câu')

    e += mc(1, 'Trong các câu sau, câu nào là một <b>mệnh đề</b>?',
            ['Hãy tính tổng 2 + 3.',
             'Số 2026 chia hết cho 3.',
             'Bạn có thích học môn Toán không?',
             'Ôi, hôm nay trời đẹp quá!'],
            'NB', 'Nhận biết · Mệnh đề')

    e += mc(2, 'Mệnh đề nào sau đây là <b>mệnh đề phủ định</b> của mệnh đề '
               'P: “∀x ∈ ℝ, x² + 1 &gt; 0”?',
            ['∀x ∈ ℝ, x² + 1 &lt; 0.',
             '∀x ∈ ℝ, x² + 1 ≤ 0.',
             '∃x ∈ ℝ, x² + 1 ≤ 0.',
             '∃x ∈ ℝ, x² + 1 &gt; 0.'],
            'NB', 'Nhận biết · Mệnh đề')

    e += mc(3, 'Cho tập hợp A = {x ∈ ℕ | x là ước của 6}. Tập hợp A viết dưới dạng '
               '<b>liệt kê</b> các phần tử là',
            ['A = {1; 2; 3; 6}.',
             'A = {1; 2; 3}.',
             'A = {0; 1; 2; 3; 6}.',
             'A = {2; 3; 6}.'],
            'NB', 'Nhận biết · Tập hợp')

    e += mc(4, 'Cho hai tập hợp A = {1; 2; 3; 4} và B = {3; 4; 5}. Tập hợp A ∩ B là',
            ['{1; 2}.', '{5}.', '{3; 4}.', '{1; 2; 3; 4; 5}.'],
            'NB', 'Nhận biết · Phép toán tập hợp')

    e += mc(5, 'Trong các bất phương trình sau, bất phương trình nào là <b>bất phương trình '
               'bậc nhất hai ẩn</b>?',
            ['x² + y ≤ 2.', '2x − 3y ≥ 1.', 'xy + x &gt; 0.', '1/x + y ≤ 3.'],
            'NB', 'Nhận biết · Bất phương trình bậc nhất hai ẩn')

    e += mc(6, 'Hệ bất phương trình nào sau đây là <b>hệ bất phương trình bậc nhất hai ẩn</b>?',
            ['{ x + y &gt; 1 ; x² − y ≤ 3 }.',
             '{ 2x − y ≤ 4 ; x + 3y ≥ 0 }.',
             '{ x + y &gt; 1 ; 1/x − y &lt; 2 }.',
             '{ x·y ≥ 1 ; x − y &lt; 0 }.'],
            'NB', 'Nhận biết · Hệ bất phương trình')

    e += mc(7, 'Trong các đẳng thức sau, đẳng thức nào <b>đúng</b>?',
            ['sin 120° = −sin 60°.', 'cos 150° = cos 30°.',
             'sin 135° = sin 45°.', 'tan 120° = tan 60°.'],
            'NB', 'Nhận biết · Giá trị lượng giác')

    e += mc(8, 'Cho sin α = 3/5 với 0° &lt; α &lt; 90°. Giá trị của cos α bằng',
            ['4/5.', '−4/5.', '2/5.', '16/25.'],
            'TH', 'Thông hiểu · Giá trị lượng giác')

    e += mc(9, 'Cho tam giác ABC có BC = a, CA = b, AB = c. Khẳng định nào sau đây <b>đúng</b>?',
            ['a² = b² + c² + 2bc·cos A.', 'a² = b² + c² − 2bc·cos A.',
             'a² = b² + c² − bc·cos A.', 'a² = b² + c² + 2bc·sin A.'],
            'NB', 'Nhận biết · Định lí côsin')

    e += mc(10, 'Cho tam giác ABC có AB = 5, AC = 8 và góc BAC = 60°. Độ dài cạnh BC bằng',
             ['7.', '129.', '√129.', '49.'],
             'TH', 'Thông hiểu · Định lí côsin')

    e += mc(11, 'Khẳng định nào sau đây là <b>đúng</b>?',
             ['Hai vectơ cùng phương thì cùng hướng.',
              'Hai vectơ cùng hướng thì cùng phương.',
              'Hai vectơ có cùng độ dài thì bằng nhau.',
              'Hai vectơ đối nhau thì cùng hướng.'],
             'NB', 'Nhận biết · Khái niệm vectơ')

    e += mc(12, 'Cho hình bình hành ABCD. Khẳng định nào sau đây là <b>đúng</b>?',
             ['→AB = →CD.', '→AB = →DC.', '→AD = →CB.', '→AB = →BC.'],
             'TH', 'Thông hiểu · Hai vectơ bằng nhau')

    # ------------------------------------------------------------------
    e += section_band('II', 'TRẮC NGHIỆM ĐÚNG – SAI', '2 câu · 2,0 điểm<br/>4 ý mỗi câu')

    e += [P('Với mỗi câu, hãy đánh dấu ☐ vào cột <b>Đúng</b> hoặc <b>Sai</b> cho từng ý. Điểm '
            'của câu phụ thuộc số ý đúng: 1 ý 0,1 · 2 ý 0,25 · 3 ý 0,5 · 4 ý 1,0 điểm.', 'small')]
    e += ds(13, 'Cho các tập hợp A, B khác rỗng, đều là tập con của ℝ.', [
        'Tập hợp A = {1; 2; 3} có đúng 8 tập con.',
        'Nếu A ⊂ B thì A ∩ B = A.',
        'Nếu A \\ B = A thì A ∩ B = ∅.',
        'Phần bù của nửa khoảng (1; 4] trong ℝ là (−∞; 1) ∪ [4; +∞).',
    ])
    e += [Paragraph('<font size="7.4" color="#7A8A96">Câu 13 · [NB–TH–VD] · '
                    'Tập hợp và các phép toán trên tập hợp</font>',
                    PS('c13', fontSize=7.4, leading=10))]
    e += [Spacer(1, 10)]

    e += ds(14, 'Cho bất phương trình 2x + y ≤ 4 (1).', [
        'Cặp số (1; 2) là một nghiệm của bất phương trình (1).',
        'Đường thẳng 2x + y = 4 đi qua hai điểm (0; 4) và (2; 0).',
        'Miền nghiệm của (1) là nửa mặt phẳng bờ là đường thẳng 2x + y = 4, '
        '<b>không kể</b> bờ.',
        'Điểm M(1; 3) thuộc miền nghiệm của (1).',
    ])
    e += [Paragraph('<font size="7.4" color="#7A8A96">Câu 14 · [NB–TH–VD] · '
                    'Bất phương trình và hệ bất phương trình bậc nhất hai ẩn</font>',
                    PS('c14', fontSize=7.4, leading=10))]

    # ------------------------------------------------------------------
    e += section_band('III', 'TRẮC NGHIỆM TRẢ LỜI NGẮN', '4 câu · 2,0 điểm<br/>0,5 điểm/câu')

    e += [P('Mỗi câu chỉ cần ghi <b>kết quả</b> (một số, một biểu thức hoặc một tập hợp) vào chỗ '
            'trống. Không cần trình bày lời giải.', 'small')]

    e += tln(15, 'Cho hai tập hợp A = {x ∈ ℤ | −2 ≤ x ≤ 3} và B = {x ∈ ℤ | 1 &lt; x &lt; 5}. '
                 'Số phần tử của tập hợp A ∩ B bằng bao nhiêu?',
             'NB–TH', 'Nhận biết – Thông hiểu', 'Chương 1 · Tập hợp')

    e += tln(16, 'Lớp 10A có 40 học sinh, trong đó có 25 bạn tham gia câu lạc bộ Toán, 18 bạn '
                 'tham gia câu lạc bộ Tin học và 10 bạn tham gia cả hai câu lạc bộ. Có bao nhiêu '
                 'học sinh của lớp <b>không</b> tham gia câu lạc bộ nào?',
             'VD', 'Vận dụng', 'Chương 1 · Phép toán tập hợp')

    e += tln(17, 'Cho góc α thỏa mãn 90° &lt; α &lt; 180° và cos α = −1/2. Tính sin α '
                 '(ghi kết quả dạng chính xác).',
             'TH', 'Thông hiểu', 'Chương 3 · Giá trị lượng giác')

    e += tln(18, 'Cho tam giác ABC có AB = 3, AC = 4 và BC = 5. Tính diện tích S của tam giác ABC.',
             'TH', 'Thông hiểu', 'Chương 3 · Hệ thức lượng trong tam giác')

    # ------------------------------------------------------------------
    e += section_band('IV', 'TỰ LUẬN', '3 câu · 3,0 điểm<br/>1,0 điểm/câu')

    e += [P('Trình bày đầy đủ các bước. Điểm trình bày được tính trong từng câu, nên hãy viết '
            'rõ: đặt vấn đề → biến đổi → kết luận.', 'small')]

    e += essay(19, '<b>(1,0 điểm)</b> Cho các tập hợp A = {x ∈ ℝ | −3 ≤ x &lt; 2}, '
                   'B = {x ∈ ℝ | x &gt; 0} và C = {x ∈ ℝ | x ≤ 1}. '
                   'Tìm A ∩ B, A ∪ C và phần bù C<sub>ℝ</sub>B.',
                 'Vận dụng · Chương 1 · Giao, hợp, phần bù của các khoảng và nửa khoảng')

    e += essay(20, '<b>(1,0 điểm)</b> Từ hai vị trí A và B trên bờ biển cách nhau 100 m, người '
                   'ta quan sát một con tàu ở vị trí C trên biển. Người ta đo được góc '
                   'BAC = 75° và góc ABC = 60°. Tính khoảng cách từ A đến tàu (làm tròn đến '
                   'hàng phần mười của mét).',
                 'Vận dụng · Chương 3 · Giải tam giác, định lí sin')

    e += essay(21, '<b>(1,0 điểm)</b> Một xưởng sản xuất hai loại sản phẩm I và II. Mỗi sản phẩm '
                   'loại I cần 2 giờ gia công máy và 1 giờ nhân công; mỗi sản phẩm loại II cần '
                   '1 giờ gia công máy và 2 giờ nhân công. Mỗi tuần xưởng có tối đa 100 giờ máy '
                   'và 80 giờ nhân công. Tiền lãi mỗi sản phẩm loại I là 400 nghìn đồng, mỗi sản '
                   'phẩm loại II là 300 nghìn đồng. Hỏi mỗi tuần xưởng cần sản xuất bao nhiêu sản '
                   'phẩm mỗi loại để tiền lãi lớn nhất?',
                 'Vận dụng cao · Chương 2 · Hệ bất phương trình và bài toán tối ưu')

    e += [Spacer(1, 6)]
    e += BOX('note', [
        'Hết phần đề. Trước khi đối chiếu đáp án, hãy tự ghi lại: (1) số câu bạn làm được chắc '
        'chắn, (2) số câu bạn đoán, (3) số câu bạn bỏ trống. Ba con số này quan trọng hơn điểm '
        'số, vì chúng cho biết lỗ hổng nằm ở đâu.'])
    return e
