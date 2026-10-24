# -*- coding: utf-8 -*-
"""Phần 3 – Đáp án và lời giải chi tiết."""
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.units import mm
from reportlab.platypus import KeepTogether, Paragraph, Spacer, Table, TableStyle

from design import (AMBER, BOX, CREAM, FRAME_W, GREEN, GREY, H1, H2, H3, INK,
                    LINE, NAVY, P, PLUM, RULE, S, TBL, TEAL, TEAL_LIGHT, PS)


def _chip(text, bg=TEAL, fg=colors.white, size=9.4):
    return Paragraph(f'<b>{text}</b>', PS(
        'chip', fontName='VN-Bold', fontSize=size, leading=size + 2.6,
        textColor=fg, alignment=TA_CENTER))


def sol_mc(num, answer, blocks, why_wrong=None):
    """Thẻ lời giải một câu trắc nghiệm."""
    head = [_chip(f'Câu {num}', NAVY)] + [_chip(f'Đáp án {answer}', TEAL)]
    head_t = Table([head], colWidths=[18 * mm, 30 * mm], hAlign='LEFT')
    head_t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), NAVY),
        ('BACKGROUND', (1, 0), (1, 0), TEAL),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 3.4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.4),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    inner = [head_t, Spacer(1, 4)]
    for b in blocks:
        if isinstance(b, str):
            inner.append(Paragraph(b, S['body']))
        elif isinstance(b, list):
            inner.extend(b)
        else:
            inner.append(b)
    t = Table([['', inner]], colWidths=[1.6 * mm, FRAME_W - 1.6 * mm], hAlign='LEFT')
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), TEAL),
        ('BACKGROUND', (1, 0), (1, 0), colors.white),
        ('BOX', (1, 0), (1, 0), 0.6, LINE),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (0, 0), 0),
        ('RIGHTPADDING', (0, 0), (0, 0), 0),
        ('LEFTPADDING', (1, 0), (1, 0), 9),
        ('RIGHTPADDING', (1, 0), (1, 0), 9),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
    ]))
    out = [t]
    if why_wrong:
        out.append(Paragraph(why_wrong, PS(
            'ww', fontSize=8.4, leading=12.4, textColor=GREY, spaceBefore=3,
            leftIndent=2)))
    return [Spacer(1, 6), KeepTogether(out), Spacer(1, 4)]


def sol_ds(num, verdicts, notes, intro=None):
    """Lời giải câu đúng/sai: bảng ý – kết luận – giải thích."""
    rows = []
    for i, (v, n) in enumerate(zip(verdicts, notes)):
        color = GREEN if v == 'Đ' else '#A63D40'
        rows.append([
            Paragraph(f'<b>{labels[i]})</b>', S['cell']),
            Paragraph(f'<b><font color="{color}">{v}</font></b>', S['cell_c']),
            Paragraph(n, PS('sdn', fontSize=8.9, leading=13.2,
                                        textColor=INK)),
        ])
    t = Table(rows, colWidths=[8 * mm, 11 * mm, FRAME_W - 19 * mm])
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('LINEBELOW', (0, 0), (-1, -1), 0.4, LINE),
        ('BOX', (0, 0), (-1, -1), 0.5, LINE),
        ('BACKGROUND', (1, 0), (1, -1), CREAM),
    ]))
    head = Table([[_chip(f'Câu {num}', NAVY),
                   _chip('Đáp án: ' + ' · '.join(f'{labels[i]}) {v}'
                                                  for i, v in enumerate(verdicts)),
                   TEAL, size=8.6)]],
                 colWidths=[18 * mm, FRAME_W - 18 * mm], hAlign='LEFT')
    head.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), NAVY),
        ('BACKGROUND', (1, 0), (1, 0), TEAL),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 3.4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.4),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
    ]))
    out = [Spacer(1, 6), head, Spacer(1, 5), t]
    if intro:
        out += [Spacer(1, 4), Paragraph(intro, PS(
            'dsintro', fontSize=8.6, leading=12.8, textColor=GREY))]
    out += [Spacer(1, 9)]
    return out


def sol_short(num, answer, blocks, points='0,5'):
    head = Table([[_chip(f'Câu {num}', NAVY),
                   _chip(f'Kết quả: {answer}', TEAL)]],
                 colWidths=[18 * mm, FRAME_W - 18 * mm], hAlign='LEFT')
    head.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), NAVY),
        ('BACKGROUND', (1, 0), (1, 0), TEAL),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 3.4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.4),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
    ]))
    inner = [Paragraph(b, S['body']) if isinstance(b, str) else b for b in blocks]
    t = Table([['', inner]], colWidths=[1.6 * mm, FRAME_W - 1.6 * mm], hAlign='LEFT')
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), TEAL),
        ('BOX', (1, 0), (1, 0), 0.6, LINE),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (0, 0), 0),
        ('RIGHTPADDING', (0, 0), (0, 0), 0),
        ('LEFTPADDING', (1, 0), (1, 0), 9),
        ('RIGHTPADDING', (1, 0), (1, 0), 9),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
    ]))
    return [Spacer(1, 6), KeepTogether([head, Spacer(1, 5), t]), Spacer(1, 4)]


labels = 'abcd'

STEP_STYLE = PS('step', fontSize=9.4, leading=14.4, textColor=INK,
                            leftIndent=16, bulletIndent=2, spaceAfter=3)
WHY = PS('why', fontSize=8.5, leading=12.6, textColor=GREY,
                     spaceBefore=2, spaceAfter=2)


def steps(items):
    return [Paragraph(s, STEP_STYLE, bulletText=f'{i}.')
            for i, s in enumerate(items, 1)]


# ==========================================================================
def part():
    e = []
    e += H1('III', 'Đáp án và lời giải chi tiết', 'Phần 3  ·  21 câu')
    e += [P('Mỗi câu được trình bày theo cùng một cấu trúc: <b>đáp án</b> → <b>lập luận</b> → '
            '<b>vì sao các phương án khác sai</b> (với câu trắc nghiệm). Với câu tự luận, lời '
            'giải được chia thành các bước đúng như cách trình bày trong bài thi để bạn đối chiếu '
            'được điểm từng phần.', 'lead')]

    # ------------------------------------------------------------------
    e += [H2('C.1. Trắc nghiệm nhiều phương án lựa chọn (câu 1 – 12)')]

    e += sol_mc(1, 'B', [
        'Mệnh đề là câu khẳng định có tính đúng hoặc sai xác định. Câu B khẳng định “số 2026 '
        'chia hết cho 3” — ta kiểm tra được: 2 + 0 + 2 + 6 = 10 không chia hết cho 3, nên đây là '
        'mệnh đề <b>sai</b>. Tuy sai, nó vẫn là mệnh đề.',
    ], 'A là câu mệnh lệnh, C là câu hỏi, D là câu cảm thán — cả ba đều không có tính đúng/sai. '
       'Lưu ý: đề có thể đưa ra một mệnh đề sai; “sai” không có nghĩa là “không phải mệnh đề”.')

    e += sol_mc(2, 'C', [
        'Mệnh đề P có dạng “∀x ∈ ℝ, P(x)” với P(x) là “x² + 1 &gt; 0”. Phủ định phải đổi '
        '<b>∀ thành ∃</b> và phủ định vế sau: “x² + 1 &gt; 0” phủ định là “x² + 1 ≤ 0”. '
        'Vậy mệnh đề phủ định là <b>∃x ∈ ℝ, x² + 1 ≤ 0</b>.',
    ], 'A và B vẫn dùng ∀ nên chưa phải phủ định. D giữ nguyên vế sau nên chỉ đổi lượng từ, '
       'không phủ định nội dung. Hãy nhớ: phải đổi <i>cả hai</i> chỗ.')

    e += sol_mc(3, 'A', [
        'Ước của 6 (trong ℕ) là các số tự nhiên chia hết 6: 1; 2; 3; 6. Vậy A = {1; 2; 3; 6}.',
    ], 'B thiếu 6; C thêm 0 (0 không phải ước của 6 vì không có số nguyên nào nhân với 0 bằng 6); '
       'D bỏ sót 1. Khi liệt kê, hãy kiểm tra từng số từ 1 đến chính nó.')

    e += sol_mc(4, 'C', [
        'A ∩ B gồm các phần tử vừa thuộc A vừa thuộc B. So sánh A = {1; 2; 3; 4} và '
        'B = {3; 4; 5}, phần tử chung là 3 và 4. Vậy A ∩ B = {3; 4}.',
    ], 'A là A \\ B; D là A ∪ B; B là B \\ A. Ba phép toán này rất dễ lẫn — hãy đọc kĩ kí hiệu.')

    e += sol_mc(5, 'B', [
        'Bất phương trình bậc nhất hai ẩn có dạng ax + by ≤ c (hoặc ≥, &lt;, &gt;) với a, b '
        'không đồng thời bằng 0. Phương án 2x − 3y ≥ 1 có a = 2, b = −3, c = 1, thỏa mãn.',
    ], 'A có x² (bậc hai); C có xy (tích hai ẩn); D có 1/x (ẩn ở mẫu).')

    e += sol_mc(6, 'B', [
        'Cả hai bất phương trình 2x − y ≤ 4 và x + 3y ≥ 0 đều là bậc nhất hai ẩn, nên hệ là hệ '
        'bất phương trình bậc nhất hai ẩn.',
    ], 'A chứa x²; C chứa 1/x; D chứa tích x·y. Chỉ cần <b>một</b> bất phương trình trong hệ '
       'không phải bậc nhất hai ẩn là cả hệ bị loại.')

    e += sol_mc(7, 'C', [
        'Áp dụng công thức hai góc bù nhau: sin(180° − α) = sin α. Với α = 45°: '
        '180° − 45° = 135°, nên sin 135° = sin 45° = √2/2.',
    ], 'A sai vì sin 120° = sin 60° (dấu dương), không phải −sin 60°. B sai vì cos 150° = −cos 30°. '
       'D sai vì tan 120° = −tan 60°. Quy tắc: <b>sin giữ nguyên, cos và tan đổi dấu</b>.')

    e += sol_mc(8, 'A', [
        'Dùng hệ thức cơ bản: sin²α + cos²α = 1 ⇒ cos²α = 1 − (3/5)² = 1 − 9/25 = 16/25. '
        'Vì 0° &lt; α &lt; 90° nên cos α &gt; 0, suy ra cos α = 4/5.',
    ], 'B sai vì chọn nhầm dấu (góc nhọn thì cos dương). C sai vì lấy nhầm 5 − 3. '
       'D sai vì quên khai căn, dừng lại ở cos²α.')

    e += sol_mc(9, 'B', [
        'Định lí côsin trong tam giác ABC: a² = b² + c² − 2bc·cos A, với a = BC, b = CA, c = AB.',
    ], 'A sai dấu (+ thay vì −); C thiếu hệ số 2; D dùng sin thay vì cos. Mẹo kiểm tra: khi '
       'A = 90° thì cos A = 0 và công thức phải trở về Pythagore a² = b² + c² — chỉ có B thỏa mãn.')

    e += sol_mc(10, 'A', [
        'Áp dụng định lí côsin với góc xen giữa A: '
        'BC² = AB² + AC² − 2·AB·AC·cos A = 5² + 8² − 2·5·8·cos 60° = 25 + 64 − 80·(1/2) '
        '= 89 − 40 = 49. Vậy BC = √49 = 7.',
    ], 'B là BC² chứ không phải BC; C là kết quả của phép tính sai dấu (cộng thay vì trừ, cho '
       '129); D cũng là BC². Câu này kiểm tra đúng thói quen: <b>tính xong phải lấy căn</b>.')

    e += sol_mc(11, 'B', [
        'Hai vectơ cùng hướng thì giá của chúng song song hoặc trùng nhau, tức là cùng phương. '
        'Vậy khẳng định “cùng hướng ⇒ cùng phương” đúng.',
    ], 'A sai: hai vectơ cùng phương có thể ngược hướng (ví dụ →AB và →CD trong hình bình hành). '
       'C sai: cùng độ dài nhưng khác hướng thì không bằng nhau. D sai: hai vectơ đối nhau thì '
       '<b>ngược</b> hướng.')

    e += sol_mc(12, 'B', [
        'Trong hình bình hành ABCD, hai cạnh AB và DC song song và bằng nhau. Đi từ A đến B và '
        'đi từ D đến C là cùng một chiều, nên →AB và →DC cùng hướng và cùng độ dài. '
        'Vậy →AB = →DC.',
    ], 'A sai vì →AB và →CD ngược hướng (đó là hai vectơ đối nhau). C sai vì →CB ngược hướng '
       'với →AD (→AD = →BC). D sai vì →AB và →BC không cùng phương. Hãy vẽ hình và đánh mũi tên '
       'trước khi chọn.')

    # ------------------------------------------------------------------
    e += [H2('C.2. Trắc nghiệm đúng – sai (câu 13 – 14)')]

    e += sol_ds(13, ['Đ', 'Đ', 'Đ', 'S'], [
        'Tập A có 3 phần tử nên số tập con là 2³ = 8, gồm ∅, ba tập một phần tử, ba tập hai phần '
        'tử và chính A. <b>Đúng.</b>',
        'A ⊂ B nghĩa là mọi phần tử của A đều thuộc B, nên phần chung của A và B chính là A. '
        '<b>Đúng.</b>',
        'A \\ B = A có nghĩa là khi bỏ khỏi A các phần tử thuộc B, A không mất gì — tức A và B '
        'không có phần tử chung. Vậy A ∩ B = ∅. <b>Đúng.</b>',
        'Phần bù của (1; 4] là tập các số thực <b>không</b> thuộc (1; 4], tức là x ≤ 1 hoặc '
        'x &gt; 4. Vậy phải là (−∞; 1] ∪ (4; +∞). Khẳng định trong đề dùng (−∞; 1) — thiếu điểm '
        '1 — và [4; +∞) — lấy nhầm điểm 4. <b>Sai.</b>',
    ], intro='<b>Phân tích:</b> hai ý đầu kiểm tra định nghĩa cơ bản; ý c kiểm tra suy luận; ý d là '
             'ý “bẫy” về đầu mút, cần xét riêng từng điểm 1 và 4.')

    e += sol_ds(14, ['Đ', 'Đ', 'S', 'S'], [
        'Thay x = 1, y = 2 vào: 2·1 + 2 = 4 ≤ 4, đúng. Vậy (1; 2) là nghiệm. <b>Đúng.</b>',
        'Với x = 0 thì y = 4 → điểm (0; 4). Với y = 0 thì x = 2 → điểm (2; 0). '
        '<b>Đúng.</b>',
        'Bất phương trình có dấu ≤ nên miền nghiệm <b>kể cả</b> đường biên. <b>Sai.</b>',
        'Thay M(1; 3): 2·1 + 3 = 5 &gt; 4, không thỏa mãn. Vậy M không thuộc miền nghiệm. '
        '<b>Sai.</b>',
    ], intro='<b>Phân tích:</b> ba ý đầu là kiến thức trực tiếp về nghiệm và miền nghiệm; ý d kiểm '
             'tra kĩ năng thay số. Chỉ cần thay đúng một phép tính là kết luận được.')

    # ------------------------------------------------------------------
    e += [H2('C.3. Trắc nghiệm trả lời ngắn (câu 15 – 18)')]

    e += sol_short(15, '2', [
        Paragraph('Liệt kê phần tử của hai tập hợp:', S['body']),
        *steps([
            'A = {x ∈ ℤ | −2 ≤ x ≤ 3} = {−2; −1; 0; 1; 2; 3} — lấy cả hai đầu mút vì có dấu ≤.',
            'B = {x ∈ ℤ | 1 &lt; x &lt; 5} = {2; 3; 4} — không lấy 1 và 5 vì dấu &lt;.',
            'A ∩ B = {2; 3}, vậy số phần tử là <b>2</b>.',
        ]),
        Paragraph('Có thể giải nhanh mà không cần liệt kê: A ∩ B = {x ∈ ℤ | 1 &lt; x ≤ 3} vì phải '
                  'đồng thời ≥ −2, ≤ 3 và &gt; 1, &lt; 5; các số nguyên thỏa mãn là 2 và 3.', S['small']),
    ])

    e += sol_short(16, '7', [
        Paragraph('Gọi A là tập học sinh tham gia CLB Toán, B là tập học sinh tham gia CLB Tin học. '
                  'Ta có |A| = 25, |B| = 18, |A ∩ B| = 10.', S['body']),
        *steps([
            'Số học sinh tham gia ít nhất một CLB: |A ∪ B| = |A| + |B| − |A ∩ B| = 25 + 18 − 10 = 33.',
            'Số học sinh không tham gia CLB nào: 40 − 33 = <b>7</b>.',
        ]),
        Paragraph('Vì sao phải trừ |A ∩ B|? Vì 10 bạn tham gia cả hai đã được đếm hai lần (một lần '
                  'trong 25, một lần trong 18). Đây chính là công thức đếm của chương 1.', S['small']),
    ])

    e += sol_short(17, '√3/2', [
        *steps([
            'sin²α = 1 − cos²α = 1 − (−1/2)² = 1 − 1/4 = 3/4.',
            'Vì 90° &lt; α &lt; 180° (góc tù) nên sin α &gt; 0. Do đó sin α = √3/2.',
        ]),
        Paragraph('Nếu đề cho góc nhọn thì sin vẫn dương, nhưng nếu đề cho cos dương và sin âm thì '
                  'phải chọn dấu âm — luôn xét điều kiện góc trước khi kết luận.', S['small']),
    ])

    e += sol_short(18, 'S = 6', [
        *steps([
            'Kiểm tra: 3² + 4² = 9 + 16 = 25 = 5², nên tam giác ABC vuông tại A (định lí Pythagore '
            'đảo).',
            'Diện tích tam giác vuông: S = (1/2)·AB·AC = (1/2)·3·4 = <b>6</b>.',
        ]),
        Paragraph('Cách khác dùng Heron: p = (3 + 4 + 5)/2 = 6, '
                  'S = √(6·3·2·1) = √36 = 6. Cả hai cách đều cho cùng kết quả — hãy chọn cách '
                  'nhanh hơn khi làm bài.', S['small']),
    ])

    # ------------------------------------------------------------------
    e += [H2('C.4. Tự luận (câu 19 – 21)')]

    # Câu 19
    e += [H3('Câu 19 (1,0 điểm) – Giao, hợp, phần bù của các khoảng')]
    e += [P('<b>Đề.</b> Cho A = {x ∈ ℝ | −3 ≤ x &lt; 2}, B = {x ∈ ℝ | x &gt; 0}, '
            'C = {x ∈ ℝ | x ≤ 1}. Tìm A ∩ B, A ∪ C và C<sub>ℝ</sub>B.')]
    e += [P('<b>Bước 1. Viết các tập dưới dạng khoảng, nửa khoảng.</b>')]
    e += [Paragraph('A = [−3; 2) — lấy −3, không lấy 2;   B = (0; +∞);   C = (−∞; 1].',
                    PS('eqx', fontName='VN-Bold', fontSize=9.4, leading=14,
                                   textColor=NAVY, leftIndent=12, spaceAfter=4))]
    e += [P('<b>Bước 2. Tìm A ∩ B.</b> Phần tử phải vừa thuộc A (từ −3 đến dưới 2) vừa thuộc B '
            '(lớn hơn 0). Phần chung là các số lớn hơn 0 và nhỏ hơn 2, không lấy 0 (vì 0 ∉ B) và '
            'không lấy 2 (vì 2 ∉ A):')]
    e += [Paragraph('A ∩ B = (0; 2).', PS(
        'eqx2', fontName='VN-Bold', fontSize=10, leading=15, textColor=TEAL,
        leftIndent=12, spaceAfter=4))]
    e += [P('<b>Bước 3. Tìm A ∪ C.</b> Hợp gồm mọi số thuộc A hoặc thuộc C. Tập A phủ đoạn '
            '[−3; 2), tập C phủ (−∞; 1]. Hợp của chúng phủ toàn bộ phía trái cho đến sát 2, và vì '
            '−3 &gt; −∞ nên không có “lỗ hổng” nào:')]
    e += [Paragraph('A ∪ C = (−∞; 2).', PS(
        'eqx3', fontName='VN-Bold', fontSize=10, leading=15, textColor=TEAL,
        leftIndent=12, spaceAfter=4))]
    e += [P('<b>Bước 4. Tìm C<sub>ℝ</sub>B.</b> B = (0; +∞) nên phần bù là các số thực không lớn '
            'hơn 0, tức là x ≤ 0:')]
    e += [Paragraph('C<sub>ℝ</sub>B = (−∞; 0].', PS(
        'eqx4', fontName='VN-Bold', fontSize=10, leading=15, textColor=TEAL,
        leftIndent=12, spaceAfter=4))]
    e += BOX('warn', [
        'Điểm 0 <b>thuộc</b> phần bù vì 0 ∉ B= (0; +∞). Vì thế kết quả phải là (−∞; 0] chứ không '
        'phải (−∞; 0). Rất nhiều bạn mất 0,25 điểm chỉ vì dấu ngoặc này.',
        'Với A ∪ C, đừng viết [−3; 2) ∪ (−∞; 1] rồi để nguyên — phải rút gọn thành (−∞; 2).'],
        'Chỗ dễ mất điểm')

    # Câu 20
    e += [H3('Câu 20 (1,0 điểm) – Giải tam giác, ứng dụng thực tế')]
    e += [P('<b>Đề.</b> A và B cách nhau 100 m trên bờ biển, C là vị trí con tàu. Biết '
            'góc BAC = 75°, góc ABC = 60°. Tính AC.')]
    e += [P('<b>Bước 1. Tính góc thứ ba của tam giác ABC.</b> Tổng ba góc bằng 180° nên')]
    e += [Paragraph('góc ACB = 180° − 75° − 60° = 45°.', PS(
        'eqx5', fontName='VN-Bold', fontSize=9.6, leading=14, textColor=NAVY,
        leftIndent=12, spaceAfter=4))]
    e += [P('<b>Bước 2. Chọn định lí sin.</b> Ta biết cạnh AB = 100 m và góc đối diện với nó là '
            'góc C = 45°; cần tìm cạnh AC, đối diện với góc B = 60°. Cặp cạnh – góc đối diện đã '
            'đủ, nên dùng định lí sin:')]
    e += [Paragraph('AC / sin B = AB / sin C   ⇒   AC = AB · sin B / sin C.',
                    PS('eqx6', fontName='VN-Bold', fontSize=9.6, leading=14,
                                   textColor=NAVY, leftIndent=12, spaceAfter=4))]
    e += [P('<b>Bước 3. Thay số.</b>')]
    e += [Paragraph('AC = 100 · sin 60° / sin 45° = 100 · (√3/2)/(√2/2) = 100·√3/√2 = 50√6 '
                    '≈ 122,5 (m).', PS(
                        'eqx7', fontName='VN-Bold', fontSize=9.6, leading=14,
                        textColor=TEAL, leftIndent=12, spaceAfter=4))]
    e += [P('<b>Kết luận.</b> Khoảng cách từ A đến tàu xấp xỉ <b>122,5 m</b>.')]
    e += BOX('note', [
        'Vì sao không dùng định lí côsin? Vì định lí côsin cần biết hai cạnh và góc xen giữa, hoặc '
        'ba cạnh. Ở đây ta chỉ biết một cạnh, nên định lí sin là lựa chọn duy nhất.',
        'Kỹ năng bấm máy: tính 100 × sin60 ÷ sin45, kết quả 122,474…, làm tròn đến hàng phần mười '
        'là 122,5. Hãy đặt chế độ máy ở DEG.'],
        'Ghi nhớ')

    # Câu 21
    e += [H3('Câu 21 (1,0 điểm) – Bài toán tối ưu')]
    e += [P('<b>Đề.</b> Sản phẩm I cần 2 giờ máy và 1 giờ nhân công; sản phẩm II cần 1 giờ máy và '
            '2 giờ nhân công. Tối đa 100 giờ máy, 80 giờ nhân công mỗi tuần. Lãi 400 nghìn đồng '
            'cho mỗi sản phẩm I, 300 nghìn đồng cho mỗi sản phẩm II. Tìm phương án lãi lớn nhất.')]
    e += [P('<b>Bước 1. Đặt ẩn và lập hệ bất phương trình.</b> Gọi x, y lần lượt là số sản phẩm '
            'loại I và loại II sản xuất trong một tuần (x ≥ 0, y ≥ 0, đơn vị: sản phẩm).')]
    e += [Paragraph('Ràng buộc giờ máy: 2x + y ≤ 100.    Ràng buộc giờ nhân công: x + 2y ≤ 80.',
                    PS('eqx8', fontName='VN-Bold', fontSize=9.4, leading=14,
                                   textColor=NAVY, leftIndent=12, spaceAfter=4))]
    e += [P('Hàm mục tiêu (tiền lãi, đơn vị nghìn đồng): F(x; y) = 400x + 300y.')]
    e += [P('<b>Bước 2. Xác định miền nghiệm và các đỉnh.</b> Miền nghiệm là tứ giác OABC với:')]
    e += [TBL(['Đỉnh', 'Cách xác định', 'Tọa độ'],
              [['O', 'gốc tọa độ', '(0; 0)'],
               ['A', 'giao của 2x + y = 100 với trục Ox (y = 0) → x = 50', '(50; 0)'],
               ['B', 'giao của 2x + y = 100 và x + 2y = 80', '(40; 20)'],
               ['C', 'giao của x + 2y = 80 với trục Oy (x = 0) → y = 40', '(0; 40)']],
              widths=[0.8, 5.6, 1.4], align=['c', None, 'c'])]
    e += [Spacer(1, 3), P('Tìm B: từ 2x + y = 100 suy ra y = 100 − 2x. Thay vào x + 2y = 80 được '
                          'x + 2(100 − 2x) = 80 ⇒ x + 200 − 4x = 80 ⇒ 3x = 120 ⇒ x = 40, '
                          'y = 100 − 80 = 20.')]
    e += [P('<b>Bước 3. Tính F tại bốn đỉnh và so sánh.</b>')]
    e += [TBL(['Đỉnh', 'O(0; 0)', 'A(50; 0)', 'B(40; 20)', 'C(0; 40)'],
              [['F = 400x + 300y', '0', '20 000', '<b>22 000</b>', '12 000']],
              widths=[2.2, 1.2, 1.2, 1.2, 1.2],
              align=[None, 'c', 'c', 'c', 'c'])]
    e += [Spacer(1, 4), P('<b>Kết luận.</b> Giá trị lớn nhất của F là 22 000 (nghìn đồng), đạt '
                          'tại x = 40, y = 20. Vậy mỗi tuần xưởng nên sản xuất <b>40 sản phẩm loại '
                          'I và 20 sản phẩm loại II</b>, khi đó tiền lãi lớn nhất là '
                          '<b>22 triệu đồng</b>.')]
    e += [P('<b>Kiểm tra lại.</b> Giờ máy: 2·40 + 20 = 100 (vừa đủ). Giờ nhân công: 40 + 2·20 = 80 '
            '(vừa đủ). Cả hai ràng buộc đều được dùng hết — dấu hiệu cho thấy lời giải hợp lí, vì '
            'tăng sản phẩm nào cũng sẽ vi phạm một ràng buộc.')]
    e += BOX('warn', [
        'Nếu quên điều kiện x ≥ 0, y ≥ 0, miền nghiệm sẽ không bị chặn và bài toán không có giá '
        'trị lớn nhất — mất 0,25 điểm trình bày.',
        'Nếu chỉ thử hai đỉnh A và C (bỏ qua B), bạn sẽ chọn sai phương án (A cho 20 000 &lt; '
        '22 000). Phải thử <b>tất cả</b> các đỉnh.',
        'Câu kết luận phải nêu đủ: số lượng từng loại <b>và</b> giá trị tiền lãi.'],
        'Ba lỗi làm mất điểm')
    return e
