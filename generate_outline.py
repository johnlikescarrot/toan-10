# -*- coding: utf-8 -*-
"""Sinh PDF: ĐỀ CƯƠNG ÔN TẬP TOÁN 10 (Kết nối tri thức) - Giữa kì I 2026-2027."""
import html
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle, PageBreak, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

FONTS = '/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('DJV', FONTS + 'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DJV-B', FONTS + 'DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DJV-S', FONTS + 'DejaVuSerif.ttf'))
pdfmetrics.registerFont(TTFont('DJV-S-B', FONTS + 'DejaVuSerif-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DJV-M', FONTS + 'DejaVuSansMono.ttf'))
registerFontFamily('DJV', normal='DJV', bold='DJV-B', italic='DJV', boldItalic='DJV-B')
registerFontFamily('DJV-S', normal='DJV-S', bold='DJV-S-B', italic='DJV-S', boldItalic='DJV-S-B')

# Palette
NAVY = colors.HexColor('#1F3864')
BLUE = colors.HexColor('#2E5FA3')
LBLUE = colors.HexColor('#DCE6F2')
GREY = colors.HexColor('#595959')
GREEN = colors.HexColor('#1E6B3A')
LGREEN = colors.HexColor('#E3F0E7')
AMBER = colors.HexColor('#8A5A00')
LAMBER = colors.HexColor('#FBEFD6')
RED = colors.HexColor('#9E1B1B')
LRED = colors.HexColor('#F7E2E2')

S = {}
S['title'] = ParagraphStyle('title', fontName='DJV-B', fontSize=23, leading=27,
                            textColor=NAVY, alignment=TA_CENTER, spaceAfter=6)
S['subtitle'] = ParagraphStyle('subtitle', fontName='DJV', fontSize=12.5, leading=16,
                               textColor=BLUE, alignment=TA_CENTER, spaceAfter=4)
S['meta'] = ParagraphStyle('meta', fontName='DJV', fontSize=9, leading=13,
                           textColor=GREY, alignment=TA_CENTER, spaceAfter=10)
S['h1'] = ParagraphStyle('h1', fontName='DJV-B', fontSize=15, leading=19,
                         textColor=colors.white, backColor=NAVY, borderPadding=(6, 8, 6, 8),
                         spaceBefore=10, spaceAfter=8)
S['h2'] = ParagraphStyle('h2', fontName='DJV-B', fontSize=12.5, leading=16,
                         textColor=NAVY, spaceBefore=10, spaceAfter=4,
                         borderColor=BLUE, borderWidth=0, leftIndent=0)
S['h3'] = ParagraphStyle('h3', fontName='DJV-B', fontSize=10.5, leading=14,
                         textColor=BLUE, spaceBefore=6, spaceAfter=3)
S['body'] = ParagraphStyle('body', fontName='DJV', fontSize=9.5, leading=13.5,
                           textColor=colors.HexColor('#1a1a1a'), alignment=TA_JUSTIFY,
                           spaceAfter=4)
S['bul'] = ParagraphStyle('bul', parent=S['body'], leftIndent=14, bulletIndent=4, spaceAfter=2.5)
S['sub'] = ParagraphStyle('sub', parent=S['body'], leftIndent=26, spaceAfter=2.5)
S['note'] = ParagraphStyle('note', fontName='DJV', fontSize=9, leading=13,
                           textColor=colors.HexColor('#1a1a1a'), alignment=TA_JUSTIFY,
                           backColor=LAMBER, borderColor=AMBER, borderWidth=0.6,
                           borderPadding=(6, 8, 6, 8), spaceBefore=4, spaceAfter=8)
S['q'] = ParagraphStyle('q', fontName='DJV', fontSize=9.5, leading=13.5,
                        textColor=colors.HexColor('#1a1a1a'), leftIndent=10, spaceAfter=2,
                        spaceBefore=6)
S['opt'] = ParagraphStyle('opt', fontName='DJV', fontSize=9.5, leading=13,
                          textColor=colors.HexColor('#1a1a1a'), leftIndent=30, spaceAfter=1)
S['ans'] = ParagraphStyle('ans', fontName='DJV', fontSize=9.3, leading=13,
                          textColor=colors.HexColor('#1a1a1a'), leftIndent=30, spaceAfter=2,
                          backColor=LGREEN, borderColor=GREEN, borderWidth=0.4,
                          borderPadding=(3, 6, 3, 6))
S['sol'] = ParagraphStyle('sol', fontName='DJV', fontSize=9.2, leading=12.6,
                          textColor=colors.HexColor('#1a1a1a'), leftIndent=16, spaceAfter=1.5,
                          alignment=TA_JUSTIFY)
S['cellh'] = ParagraphStyle('cellh', fontName='DJV-B', fontSize=8.3, leading=10.5,
                            textColor=colors.white, alignment=TA_CENTER)
S['cell'] = ParagraphStyle('cell', fontName='DJV', fontSize=8.2, leading=10.5,
                           textColor=colors.HexColor('#1a1a1a'), alignment=TA_CENTER)
S['cellL'] = ParagraphStyle('cellL', fontName='DJV', fontSize=8.2, leading=10.5,
                            textColor=colors.HexColor('#1a1a1a'), alignment=TA_LEFT)
S['cellB'] = ParagraphStyle('cellB', fontName='DJV-B', fontSize=8.4, leading=10.5,
                            textColor=NAVY, alignment=TA_CENTER)


def fmt(s):
    # nội dung không chứa ký tự & thô (chỉ dùng entity &nbsp;), nên không cần escape &
    s = s.replace('<', '&lt;').replace('>', '&gt;')
    s = s.replace('\n', '<br/>')
    # inline bold token **...**
    parts = s.split('**')
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            out.append('<b>' + p + '</b>')
        else:
            out.append(p)
    return ''.join(out)


def P(style, text):
    return Paragraph(fmt(text), S[style])


def bullet(text):
    return Paragraph('&bull;&nbsp; ' + fmt(text), S['bul'])


story = []

# ============ COVER / HEADER ============
story.append(P('title', 'ĐỀ CƯƠNG ÔN TẬP TOÁN LỚP 10'))
story.append(P('subtitle', 'Chương trình "Kết nối tri thức" &nbsp;•&nbsp; Kiểm tra giữa kì I, năm học 2026–2027'))
story.append(Spacer(1, 2))
story.append(P('meta', 'TRƯỜNG THPT HÀ HUY TẬP &nbsp;•&nbsp; TỔ TOÁN-TIN &nbsp;•&nbsp; MÔN: TOÁN 10 &nbsp;•&nbsp; THỜI GIAN LÀM BÀI: 90 PHÚT'))
story.append(Spacer(1, 6))
story.append(P('note',
    'Lưu ý: Tệp "MA TRẬN TOÁN 10 - GIÙA KÌ I.docx" là đề kiểm tra giữa kì I, bao gồm mục tiêu, hình thức '
    'và bảng đặc tả đề kiểm tra (chi tiết 21 câu: 12 trắc nghiệm nhiều phương án, 2 đúng-sai, '
    '4 trả lời ngắn, 3 tự luận). Đề cương ôn tập này được biên soạn theo đúng cấu trúc và nội dung đó: '
    'phần 1 tóm tắt cấu trúc đề kiểm tra, phần 2 tóm tắt lý thuyết trọng tâm của 4 chương, '
    'phần 3 đưa ra bộ đề ôn tập đầy đủ (đủ 21 câu theo đúng số lượng và dạng) kèm đầy đủ đáp án và lời giải chi tiết.'))
story.append(PageBreak())

# ============ PHẦN I: CẤU TRÚC ĐỀ KIỂM TRA ============
story.append(P('h1', 'PHẦN I — CẤU TRÚC ĐỀ KIỂM TRA GIỮA KÌ I'))

story.append(P('h3', '1. Mục tiêu'))
story.append(P('body', 'Kiểm tra kiến thức đại số và hình học đến hết giữa học kỳ 1 lớp 10, thuộc 4 chương:'))
story.append(bullet('**Chương 1.** Mệnh đề và tập hợp (1.1 Mệnh đề; 1.2 Tập hợp; 1.3 Các phép toán trên tập hợp).'))
story.append(bullet('**Chương 2.** Bất phương trình và hệ bất phương trình bậc nhất hai ẩn.'))
story.append(bullet('**Chương 3.** Hệ thức lượng trong tam giác.'))
story.append(bullet('**Chương 4.** Vectơ (khái niệm vectơ).'))
story.append(P('body',
    'Yêu cầu học sinh thành thạo các kỹ năng: nhận biết và xét tính đúng-sai của mệnh đề; lập mệnh đề phủ định, '
    'đảo, tương đương; sử dụng kí hiệu ∀, ∃; thực hiện các phép toán giao, hợp, hiệu, phần bù trên tập hợp; '
    'biểu diễn miền nghiệm của bất phương trình và hệ bất phương trình bậc nhất hai ẩn trên mặt phẳng tọa độ; '
    'tính giá trị lượng giác của góc từ 0° đến 180°; vận dụng định lí sin, định lí cosin và công thức diện tích để giải tam giác; '
    'nắm vững các khái niệm và tính chất của vectơ.'))

story.append(P('h3', '2. Hình thức thi và thang điểm'))
tbl_struct = [
    [P('cellh', 'Phần'), P('cellh', 'Dạng bài'), P('cellh', 'Số câu'), P('cellh', 'Điểm')],
    [P('cellL', 'I'), P('cellL', 'Trắc nghiệm nhiều phương án lựa chọn'), P('cell', '12'), P('cell', '3')],
    [P('cellL', 'II'), P('cellL', 'Trắc nghiệm đúng sai (mỗi câu 4 ý)'), P('cell', '2'), P('cell', '2')],
    [P('cellL', 'III'), P('cellL', 'Trắc nghiệm trả lời ngắn'), P('cell', '4'), P('cell', '2')],
    [P('cellL', 'IV'), P('cellL', 'Tự luận'), P('cell', '3'), P('cell', '3')],
    [P('cellB', 'TỔNG'), P('cellL', ''), P('cellB', '21'), P('cellB', '10')],
]
t = Table(tbl_struct, colWidths=[1.9*cm, 7.9*cm, 2.2*cm, 2.0*cm])
t.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), BLUE),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, LBLUE]),
    ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#B9C7DA')),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#E7EEF7')),
]))
story.append(t)
story.append(Spacer(1, 4))
story.append(P('body',
    'Thang điểm trắc nghiệm đúng sai: đúng 1 ý = 0,1 điểm; đúng 2 ý = 0,25; đúng 3 ý = 0,5; đúng 4 ý = 1,0 điểm. '
    'Thời gian làm bài: 90 phút.'))

story.append(PageBreak())
story.append(P('h3', '3. Bảng đặc tả đề kiểm tra (tóm tắt)'))
tbl_spec = [
    [P('cellh', 'Câu'), P('cellh', 'Đơn vị kiến thức'), P('cellh', 'Nội dung / mức độ'), P('cellh', 'Mức độ nhận thức')],
    [P('cellB', 'C1'), P('cellL', '1.1 Mệnh đề'), P('cellL', 'Mệnh đề, mệnh đề phủ định, mệnh đề chứa biến'), P('cell', 'Nhận biết')],
    [P('cellB', 'C2'), P('cellL', '1.1 Mệnh đề'), P('cellL', 'Kí hiệu ∀ (với mọi) và ∃ (tồn tại)'), P('cell', 'Nhận biết')],
    [P('cellB', 'C3'), P('cellL', '1.2 Tập hợp'), P('cellL', 'Cho tập hợp bằng liệt kê hoặc tính chất đặc trưng'), P('cell', 'Nhận biết')],
    [P('cellB', 'C4'), P('cellL', '1.3 Phép toán trên tập hợp'), P('cellL', 'Biểu diễn giao, hợp của hai tập hợp (biểu đồ Ven)'), P('cell', 'Nhận biết')],
    [P('cellB', 'C5'), P('cellL', '2.1 BPT bậc nhất hai ẩn'), P('cellL', 'Nhận biết bất phương trình bậc nhất hai ẩn'), P('cell', 'Nhận biết')],
    [P('cellB', 'C6'), P('cellL', '2.2 Hệ BPT bậc nhất hai ẩn'), P('cellL', 'Nhận biết hệ bất phương trình bậc nhất hai ẩn'), P('cell', 'Nhận biết')],
    [P('cellB', 'C7'), P('cellL', '3.1 GT lượng giác'), P('cellL', 'GT lượng giác của góc từ 0° đến 180°'), P('cell', 'Nhận biết')],
    [P('cellB', 'C8'), P('cellL', '3.1 GT lượng giác'), P('cellL', 'Tính GT lượng giác khi biết 1 trong 4 GT'), P('cell', 'Thông hiểu')],
    [P('cellB', 'C9'), P('cellL', '3.2 Hệ thức lượng'), P('cellL', 'Nhận biết định lí côsin, định lí sin, diện tích'), P('cell', 'Nhận biết')],
    [P('cellB', 'C10'), P('cellL', '3.2 Hệ thức lượng'), P('cellL', 'Tính cạnh, góc, diện tích tam giác'), P('cell', 'Vận dụng')],
    [P('cellB', 'C11'), P('cellL', '4.1 Vectơ'), P('cellL', 'Các khái niệm vectơ, vectơ-không, cùng phương, bằng nhau'), P('cell', 'Nhận biết')],
    [P('cellB', 'C12'), P('cellL', '4.1 Vectơ'), P('cellL', 'Chứng minh hai vectơ bằng nhau (trường hợp đơn giản)'), P('cell', 'Thông hiểu')],
    [P('cellB', '1a'), P('cellL', '1.2 Tập hợp'), P('cellL', 'Kí hiệu khoảng, đoạn, nửa khoảng trên trục số'), P('cell', 'Nhận biết')],
    [P('cellB', '2a'), P('cellL', '2.1 BPT bậc nhất hai ẩn'), P('cellL', 'Nghiệm và miền nghiệm trên mặt phẳng tọa độ'), P('cell', 'Nhận biết')],
    [P('cellB', '1–4'), P('cellL', '1.2, 1.3, 3.1, 3.2'), P('cellL', 'Trả lời ngắn: tập hợp con; bài toán thực tế; GT lượng giác; giải tam giác'), P('cell', 'Vận dụng')],
    [P('cellB', '1–3'), P('cellL', '1.3; 3.2; 2.2'), P('cellL', 'Tự luận: phép toán tập hợp; hệ thức lượng thực tế; hệ BPT thực tế'), P('cell', 'Vận dụng')],
]
t = Table(tbl_spec, colWidths=[1.3*cm, 3.9*cm, 7.5*cm, 2.6*cm], repeatRows=1)
t.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), BLUE),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, LBLUE]),
    ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#B9C7DA')),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 2.5), ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
]))
story.append(t)
story.append(PageBreak())

# ============ PHẦN II: TÓM TẮT LÝ THUYẾT ============
story.append(P('h1', 'PHẦN II — TÓM TẮT LÝ THUYẾT TRỌNG TÂM'))

# ---- Chapter 1 ----
story.append(P('h2', 'CHƯƠNG 1. MỆNH ĐỀ VÀ TẬP HỢP'))
story.append(P('h3', '1.1. Mệnh đề'))
story.append(bullet('**Mệnh đề** là khẳng định có tính đúng hoặc sai (không thể vừa đúng vừa sai). Kí hiệu P, Q, R... Những câu hỏi, cảm thán, cầu khiến không phải mệnh đề.'))
story.append(bullet('**Mệnh đề chứa biến** là mệnh đề chưa xác định được đúng-sai, cần giá trị cụ thể của biến; kí hiệu P(x), P(n).'))
story.append(bullet('**Mệnh đề phủ định** của P là mệnh đề trái ngược với P, kí hiệu ¬P (thêm "không / không phải").'))
story.append(bullet('**Mệnh đề kéo theo** "Nếu P thì Q" kí hiệu P ⇒ Q; P là giả thiết (điều kiện đủ), Q là kết luận (điều kiện cần). P ⇒ Q chỉ sai khi P đúng và Q sai.'))
story.append(bullet('**Mệnh đề đảo** của P ⇒ Q là Q ⇒ P (chưa chắc đúng). **Mệnh đề tương đương** P ⇔ Q đúng khi cả P ⇒ Q và Q ⇒ P đều đúng (điều kiện cần và đủ).'))
story.append(bullet('**Kí hiệu ∀** (với mọi) và **∃** (tồn tại): phủ định của "∀x∈X, P(x)" là "∃x∈X, ¬P(x)"; phủ định của "∃x∈X, P(x)" là "∀x∈X, ¬P(x)".'))

story.append(P('h3', '1.2. Tập hợp'))
story.append(bullet('**Tập hợp** gồm các đối tượng xác định được; phần tử a ∈ S, a ∉ S; số phần tử kí hiệu n(S). **Tập rỗng** kí hiệu ∅.'))
story.append(bullet('Mô tả tập hợp bằng 2 cách: **liệt kê** phần tử hoặc **tính chất đặc trưng** (kí hiệu {x ∈ X | tính chất}).'))
story.append(bullet('**Tập con**: T ⊂ S nếu mọi phần tử của T đều thuộc S. Tập rỗng là tập con của mọi tập hợp. **Hai tập bằng nhau**: S = T khi S ⊂ T và T ⊂ S.'))
story.append(bullet('**Các tập số**: N = {0; 1; 2; ...}; Z = {...; -2; -1; 0; 1; 2; ...}; Q (hữu tỉ); R (thực). Quan hệ: N ⊂ Z ⊂ Q ⊂ R.'))
story.append(P('body', '**Khoảng, đoạn, nửa khoảng trên trục số:**'))
story.append(bullet('(a; b) = {x ∈ R | a < x < b};   [a; b] = {x ∈ R | a ≤ x ≤ b};   [a; b) = {x ∈ R | a ≤ x < b};   (a; b] = {x ∈ R | a < x ≤ b}.'))
story.append(bullet('(a; +∞) = {x ∈ R | x > a};  [a; +∞) = {x ∈ R | x ≥ a};  (−∞; b) = {x ∈ R | x < b};  (−∞; b] = {x ∈ R | x ≤ b};  (−∞; +∞) = R.'))

story.append(P('h3', '1.3. Các phép toán trên tập hợp'))
story.append(bullet('**Giao:** S ∩ T = {x | x ∈ S và x ∈ T}.'))
story.append(bullet('**Hợp:** S ∪ T = {x | x ∈ S hoặc x ∈ T}.'))
story.append(bullet('**Hiệu:** S \ T = {x | x ∈ S và x ∉ T}. Nếu T ⊂ S thì S \ T là **phần bù** của T trong S, kí hiệu C_S T; đặc biệt C_S S = ∅.'))
story.append(bullet('Biểu diễn các phép toán bằng **biểu đồ Ven**. Công thức: n(S ∪ T) = n(S) + n(T) − n(S ∩ T); số tập con của tập có n phần tử là 2^n.'))

# ---- Chapter 2 ----
story.append(P('h2', 'CHƯƠNG 2. BẤT PHƯƠNG TRÌNH VÀ HỆ BẤT PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN'))
story.append(P('h3', '2.1. Bất phương trình bậc nhất hai ẩn'))
story.append(bullet('**Dạng tổng quát:** ax + by ≤ c (hay ≥, <, >); với a, b, c là các số thực cho trước, a và b **không đồng thời bằng 0**; x, y là ẩn.'))
story.append(bullet('**Nghiệm:** cặp số (x0; y0) thỏa mãn bất đẳng thức. BPT bậc nhất hai ẩn luôn có **vô số nghiệm**.'))
story.append(bullet('**Miền nghiệm:** trên mặt phẳng Oxy, đường thẳng d: ax + by = c chia mặt phẳng thành hai nửa mặt phẳng; một nửa mặt phẳng (không kể bờ) là miền nghiệm.'))
story.append(P('body', '**Cách biểu diễn miền nghiệm của BPT ax + by ≤ c:**'))
story.append(bullet('Bước 1: Vẽ đường thẳng d: ax + by = c.'))
story.append(bullet('Bước 2: Lấy điểm M0(x0; y0) không thuộc d (thường lấy O(0;0) nếu c ≠ 0; hoặc (1;0), (0;1) nếu c = 0).'))
story.append(bullet('Bước 3: Tính a·x0 + b·y0 và so sánh với c.'))
story.append(bullet('Bước 4: Nếu a·x0 + b·y0 < c thì nửa mặt phẳng bờ d chứa M0 là miền nghiệm; ngược lại là nửa mặt phẳng không chứa M0. Với "<" hoặc ">" thì bờ d được vẽ nét đứt.'))

story.append(P('h3', '2.2. Hệ bất phương trình bậc nhất hai ẩn'))
story.append(bullet('**Miền nghiệm của hệ** là giao của các miền nghiệm của các BPT trong hệ.'))
story.append(bullet('**Cách vẽ:** trên cùng mặt phẳng, xác định miền nghiệm từng BPT rồi gạch bỏ phần không thỏa mãn; miền còn lại là miền nghiệm của hệ.'))
story.append(bullet('**Ứng dụng (bài toán tối ưu):** miền nghiệm là đa giác A1A2...An; tìm GT lớn nhất / nhỏ nhất của F(x; y) = mx + ny bằng cách tính F tại tọa độ các đỉnh, rồi so sánh.'))

# ---- Chapter 3 ----
story.append(P('h2', 'CHƯƠNG 3. HỆ THỨC LƯỢNG TRONG TAM GIÁC'))
story.append(P('h3', '3.1. Giá trị lượng giác của một góc từ 0° đến 180°'))
story.append(bullet('Trên **nửa đường tròn đơn vị** (tâm O, bán kính 1), với điểm M(x0; y0) sao cho góc xO M = α (0° ≤ α ≤ 180°):'))
story.append(P('sub', 'sin α = y0;  cos α = x0;  tan α = y0/x0 (α ≠ 90°);  cot α = x0/y0 (α ≠ 0°, 180°).'))
story.append(bullet('tan α = sin α/cos α;  cot α = cos α/sin α;  tan α = 1/cot α.'))
story.append(P('body', '**Bảng giá trị lượng giác của các góc đặc biệt:**'))
tbl_trig = [
    [P('cellh', 'α'), P('cellh', '0°'), P('cellh', '30°'), P('cellh', '45°'), P('cellh', '60°'), P('cellh', '90°'), P('cellh', '120°'), P('cellh', '135°'), P('cellh', '150°'), P('cellh', '180°')],
    [P('cellh', 'sin'), P('cell', '0'), P('cell', '1/2'), P('cell', '√2/2'), P('cell', '√3/2'), P('cell', '1'), P('cell', '√3/2'), P('cell', '√2/2'), P('cell', '1/2'), P('cell', '0')],
    [P('cellh', 'cos'), P('cell', '1'), P('cell', '√3/2'), P('cell', '√2/2'), P('cell', '1/2'), P('cell', '0'), P('cell', '−1/2'), P('cell', '−√2/2'), P('cell', '−√3/2'), P('cell', '−1')],
    [P('cellh', 'tan'), P('cell', '0'), P('cell', '√3/3'), P('cell', '1'), P('cell', '√3'), P('cell', '—'), P('cell', '−√3'), P('cell', '−1'), P('cell', '−√3/3'), P('cell', '0')],
    [P('cellh', 'cot'), P('cell', '—'), P('cell', '√3'), P('cell', '1'), P('cell', '√3/3'), P('cell', '—'), P('cell', '−√3/3'), P('cell', '−1'), P('cell', '−√3'), P('cell', '—')],
]
t = Table(tbl_trig, colWidths=[1.5*cm]*10, repeatRows=1)
t.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), NAVY),
    ('BACKGROUND', (0, 1), (0, -1), BLUE),
    ('ROWBACKGROUNDS', (1, 1), (-1, -1), [colors.white, LBLUE]),
    ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#B9C7DA')),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 2.5), ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
]))
story.append(t)
story.append(Spacer(1, 3))
story.append(bullet('**Hai góc bù nhau** α và 180° − α: sin(180° − α) = sin α; cos(180° − α) = −cos α; tan(180° − α) = −tan α; cot(180° − α) = −cot α.'))
story.append(bullet('**Hai góc phụ nhau** (α + β = 90°): sin α = cos β, cos α = sin β, tan α = cot β.'))

story.append(P('h3', '3.2. Hệ thức lượng trong tam giác'))
story.append(bullet('Ký hiệu: a, b, c là độ dài các cạnh đối diện với các đỉnh A, B, C; p = (a + b + c)/2 (nửa chu vi); S là diện tích; R, r là bán kính đường tròn ngoại tiếp, nội tiếp.'))
story.append(bullet('**Định lí Côsin:** a² = b² + c² − 2bc·cos A;  b² = c² + a² − 2ca·cos B;  c² = a² + b² − 2ab·cos C.'))
story.append(P('sub', 'Hệ quả: cos A = (b² + c² − a²)/(2bc); cos B = (a² + c² − b²)/(2ac); cos C = (a² + b² − c²)/(2ab).'))
story.append(bullet('**Định lí Sin:** a/sin A = b/sin B = c/sin C = 2R (R là bán kính đường tròn ngoại tiếp).'))
story.append(bullet('**Diện tích:** S = (1/2)·a·h_a;  S = (1/2)·bc·sin A = (1/2)·ca·sin B = (1/2)·ab·sin C;  S = abc/(4R);  S = p·r.'))
story.append(bullet('**Giải tam giác:** (i) biết 2 cạnh và góc xen giữa → dùng định lí cosin; (ii) biết 3 cạnh → dùng định lí cosin (kiểm tra bất đẳng thức tam giác); (iii) biết 1 cạnh và 2 góc kề → dùng định lí sin.'))

# ---- Chapter 4 ----
story.append(P('h2', 'CHƯƠNG 4. VECTƠ'))
story.append(P('h3', '4.1. Khái niệm vectơ'))
story.append(P('note', 'Trong phần này, ký hiệu **in đậm** (ví dụ **AB**, **a**, **0**) là vectơ.'))
story.append(bullet('**Vectơ** là đoạn thẳng có hướng (có điểm đầu và điểm cuối). Kí hiệu **AB** (vectơ AB) hoặc **a**.'))
story.append(bullet('**Độ dài vectơ** là khoảng cách giữa điểm đầu và điểm cuối; kí hiệu |**AB**|. **Giá của vectơ** là đường thẳng đi qua điểm đầu và điểm cuối.'))
story.append(bullet('Hai vectơ **cùng phương** khi giá của chúng song song hoặc trùng nhau; hai vectơ cùng phương thì hoặc **cùng hướng** hoặc **ngược hướng**.'))
story.append(bullet('Hai vectơ **bằng nhau** (**AB** = **CD**) khi có cùng độ dài và cùng hướng. Hai vectơ **đối nhau** khi ngược hướng và cùng độ dài: **a** = −**b**.'))
story.append(bullet('**Vectơ-không** kí hiệu **0** có độ dài bằng 0; vectơ-không cùng phương và cùng hướng với mọi vectơ.'))
story.append(bullet('**Quy tắc ba điểm:** **AB** + **BC** = **AC**. **Quy tắc hình bình hành:** **AB** + **AD** = **AC** (ABCD là hình bình hành).'))
story.append(bullet('**Hiệu hai vectơ:** **AB** = **OB** − **OA**. **Tích vectơ với số thực k:** k·**a** cùng hướng (k > 0) hoặc ngược hướng (k < 0) với **a**, độ dài bằng |k|·|**a**|.'))
story.append(bullet('Ba điểm A, B, C **thẳng hàng** khi và chỉ khi **AB** và **AC** cùng phương. Vectơ trong mặt phẳng tọa độ: **u** = x·**i** + y·**j**, tọa độ (x; y).'))
story.append(PageBreak())

# ============ PHẦN III: ĐỀ ÔN TẬP ============
story.append(P('h1', 'PHẦN III — ĐỀ ÔN TẬP (CÂU HỎI VÀ ĐÁP ÁN)'))
story.append(P('body',
    'Bộ đề gồm đầy đủ 21 câu theo đúng cấu trúc đề kiểm tra: 12 câu trắc nghiệm nhiều phương án, '
    '2 câu đúng-sai, 4 câu trả lời ngắn và 3 câu tự luận. Mỗi câu được ghi rõ chương/đơn vị kiến thức và kèm đáp án / lời giải chi tiết.'))

# ---- A. TRẮC NGHIỆM ----
story.append(P('h2', 'A. TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN (12 CÂU)'))
mcq = [
 ('Câu 1 (CHƯƠNG 1 — 1.1 Mệnh đề). Câu sau đây là một mệnh đề:',
  ['A. Họ sẽ học tập sau giờ học.', 'B. Bao giờ các bạn đi học?',
   'C. Hãy làm bài tập ngay!', 'D. Số 7 là số nguyên tố.'], 'D',
  'A là câu cảm thán/khẳng định chưa xác định tính đúng-sai; B là câu hỏi; C là câu cầu khiến — đều không phải mệnh đề. D là khẳng định có tính đúng-sai → là mệnh đề (đúng).'),
 ('Câu 2 (CHƯƠNG 1 — 1.1 Mệnh đề). Kí hiệu "∀" và "∃" được hiểu là:',
  ['A. ∀: với mọi; ∃: tồn tại', 'B. ∀: tồn tại; ∃: với mọi',
   'C. ∀: và; ∃: hoặc', 'D. ∀: không; ∃: không phải'], 'A',
  'Theo chương trình: ∀ đọc là "với mọi"; ∃ đọc là "có một" hoặc "tồn tại".'),
 ('Câu 3 (CHƯƠNG 1 — 1.2 Tập hợp). Tập hợp các số tự nhiên chia hết cho 3 và nhỏ hơn 20 có số phần tử là:',
  ['A. 6', 'B. 7', 'C. 8', 'D. 9'], 'B',
  'A = {0; 3; 6; 9; 12; 15; 18} (0 ∈ N, 0 chia hết cho 3 và 0 < 20) → n(A) = 7.'),
 ('Câu 4 (CHƯƠNG 1 — 1.3 Phép toán trên tập hợp). Cho A = {1; 2; 3; 4; 5} và B = {2; 4; 6}. Tập A ∩ B bằng:',
  ['A. {2; 4}', 'B. {1; 3; 5}', 'C. {2; 4; 6}', 'D. {1; 2; 3; 4; 5; 6}'], 'A',
  'A ∩ B là tập các phần tử thuộc cả A và B → {2; 4}.'),
 ('Câu 5 (CHƯƠNG 2 — 2.1 BPT bậc nhất hai ẩn). Bất phương trình nào sau là bất phương trình bậc nhất hai ẩn?',
  ['A. x² + y² ≤ 4', 'B. xy ≥ 1', 'C. 2x + 3y > 5', 'D. y³ − 2 ≤ 0'], 'C',
  'BPT bậc nhất hai ẩn có dạng ax + by ≤ c (a, b không cùng bằng 0). A bậc hai; B bậc hai; D chỉ có một ẩn và bậc ba.'),
 ('Câu 6 (CHƯƠNG 2 — 2.2 Hệ BPT bậc nhất hai ẩn). Hệ nào sau là hệ bất phương trình bậc nhất hai ẩn?',
  ['A. { x² + y ≤ 1; x − y ≥ 0 }', 'B. { 2x + y ≤ 3; 2x − y ≥ 1 }',
   'C. { xy ≥ 0; x + y ≤ 2 }', 'D. { x² − y ≤ 2; x + y ≥ 0 }'], 'B',
  'Hệ BPT bậc nhất hai ẩn gồm các BPT bậc nhất hai ẩn. A, C, D chứa biểu thức bậc hai (x², xy) → không phải.'),
 ('Câu 7 (CHƯƠNG 3 — 3.1 GT lượng giác). sin 150° bằng:',
  ['A. −1/2', 'B. 1/2', 'C. √3/2', 'D. √2/2'], 'B',
  '150° + 30° = 180° (góc bù): sin 150° = sin 30° = 1/2.'),
 ('Câu 8 (CHƯƠNG 3 — 3.1 GT lượng giác). Biết cos α = 1/2 và α là góc nhọn. Tính tan α:',
  ['A. √3/3', 'B. 1/2', 'C. √3', 'D. √3/2'], 'C',
  'cos α = 1/2, α nhọn → α = 60° → tan 60° = √3.'),
 ('Câu 9 (CHƯƠNG 3 — 3.2 Hệ thức lượng). Trong tam giác ABC, công thức nào sau đây đúng?',
  ['A. a² = b² + c² + 2bc·cos A', 'B. a² = b² + c² − 2bc·cos A',
   'C. a/sin A = b/cos B', 'D. S = (a + b + c)'], 'B',
  'Định lí Côsin: a² = b² + c² − 2bc·cos A (A). C sai vì dùng cos B; D sai (S ≠ a + b + c).'),
 ('Câu 10 (CHƯƠNG 3 — 3.2 Hệ thức lượng). Cho tam giác ABC có A = 60°, b = 2, c = 3. Tính a:',
  ['A. √5', 'B. √6', 'C. √7', 'D. √8'], 'C',
  'a² = b² + c² − 2bc·cos A = 4 + 9 − 2·2·3·(1/2) = 13 − 6 = 7 → a = √7.'),
 ('Câu 11 (CHƯƠNG 4 — 4.1 Vectơ). Phát biểu nào sau đây SAI về vectơ?',
  ['A. Vectơ-không cùng phương và cùng hướng với mọi vectơ.',
   'B. Hai vectơ cùng phương thì hoặc cùng hướng hoặc ngược hướng.',
   'C. Giá của vectơ AB là đường thẳng AB.',
   'D. Hai vectơ có cùng độ dài thì bằng nhau.'], 'D',
  'Hai vectơ bằng nhau phải vừa cùng độ dài vừa cùng hướng; chỉ cùng độ dài chưa đủ (có thể ngược hướng). A, B, C đều đúng.'),
 ('Câu 12 (CHƯƠNG 4 — 4.1 Vectơ). Cho hình bình hành ABCD. Ta có:',
  ['A. **AB** = **BC**', 'B. **AB** = **DC**', 'C. **AC** = **BD**', 'D. **AB** = **AD**'], 'B',
  'Trong hình bình hành ABCD: **AB** ∥ **DC** và AB = DC, cùng hướng → **AB** = **DC**.'),
]
for qtext, opts, ans, sol in mcq:
    story.append(P('q', qtext))
    for o in opts:
        story.append(P('opt', o))
    story.append(P('ans', 'Đáp án: **' + ans + '**.'))
    story.append(P('sol', 'Giải: ' + sol))
    story.append(Spacer(1, 2))

# ---- B. ĐÚNG SAI ----
story.append(P('h2', 'B. TRẮC NGHIỆM ĐÚNG SAI (2 CÂU)'))
tf = [
 ('Câu 1a (CHƯƠNG 1 — 1.2 Tập hợp). Xét các phát biểu:',
  ['a) Tập (2; 5) gồm các số thực lớn hơn 2 và nhỏ hơn 5.',
   'b) Đoạn [−1; 3] gồm các số thực x thỏa −1 ≤ x ≤ 3.',
   'c) Tập rỗng là tập con của mọi tập hợp.',
   'd) Tập {0} là tập rỗng.'], ['a', 'b', 'c'],
  'a, b, c đúng; d sai. Tập {0} có một phần tử là số 0, không phải tập rỗng (tập rỗng ∅ không có phần tử nào).'),
 ('Câu 2a (CHƯƠNG 2 — 2.1 BPT bậc nhất hai ẩn). Xét bất phương trình 2x + y ≤ 4.',
  ['a) (1; 2) là nghiệm.',
   'b) (0; 0) là nghiệm.',
   'c) Miền nghiệm là nửa mặt phẳng bờ d: 2x + y = 4 chứa gốc tọa độ O.',
   'd) (3; 0) thuộc miền nghiệm.'], ['a', 'b', 'c'],
  'a: 2·1 + 2 = 4 ≤ 4 (đúng). b: 0 ≤ 4 (đúng). c: tại O, 2·0 + 0 = 0 ≤ 4 → O thuộc miền nghiệm (đúng). d: 2·3 + 0 = 6 > 4 → sai.'),
]
for qtext, stmts, correct, sol in tf:
    story.append(P('q', qtext))
    for s in stmts:
        story.append(P('opt', s))
    story.append(P('ans', 'Đáp án: các ý đúng là **' + ', '.join(correct) + '**.'))
    story.append(P('sol', 'Lý giải: ' + sol))
    story.append(Spacer(1, 2))
story.append(P('note', 'Lưu ý: mỗi câu đúng-sai có 4 ý; thang điểm: đúng 1 ý = 0,1; đúng 2 ý = 0,25; đúng 3 ý = 0,5; đúng 4 ý = 1,0 điểm.'))
story.append(PageBreak())

# ---- C. TRẢ LỜI NGẮN ----
story.append(P('h2', 'C. TRẮC NGHIỆM TRẢ LỜI NGẮN (4 CÂU)'))
short = [
 ('Câu 1 (CHƯƠNG 1 — 1.2/1.3 Tập hợp). Tập hợp A có 4 phần tử. Hỏi A có bao nhiêu tập con?',
  'Số tập con của tập hợp có n phần tử là 2^n. Với n = 4 → 2⁴ = 16. Vậy A có 16 tập con (trong đó có A và ∅).'),
 ('Câu 2 (CHƯƠNG 1 — 1.3 Phép toán trên tập hợp). Trong một lớp có 35 học sinh; 25 em thích bóng đá (tập A), 20 em thích bóng rổ (tập B), 10 em thích cả hai. Hỏi có bao nhiêu em chỉ thích bóng đá?',
  'Số em chỉ thích bóng đá = |A| − |A ∩ B| = 25 − 10 = 15 (em). (Kiểm tra: |A ∪ B| = 25 + 20 − 10 = 35, đúng với tổng số học sinh.)'),
 ('Câu 3 (CHƯƠNG 3 — 3.1 GT lượng giác). Biết sin α = 1/2, với 0° ≤ α ≤ 180°. Tính cos α và tan α.',
  'sin α = 1/2 trên [0°; 180°] cho hai giá trị: α = 30° hoặc α = 150°.\n'
  '• Với α = 30°: cos 30° = √3/2; tan 30° = √3/3.\n'
  '• Với α = 150°: cos 150° = −√3/2; tan 150° = −√3/3.'),
 ('Câu 4 (CHƯƠNG 3 — 3.2 Hệ thức lượng). Cho tam giác ABC có A = 60°, b = 2, c = 3. Tính diện tích S và cạnh a.',
  'S = (1/2)·b·c·sin A = (1/2)·2·3·(√3/2) = 3√3/2.\n'
  'a = √(b² + c² − 2bc·cos A) = √(4 + 9 − 2·2·3·(1/2)) = √(13 − 6) = √7.\n'
  'Vậy S = 3√3/2 và a = √7.'),
]
for qtext, sol in short:
    story.append(P('q', qtext))
    story.append(P('ans', 'Đáp án / lời giải:'))
    story.append(P('sol', sol))
    story.append(Spacer(1, 2))

# ---- D. TỰ LUẬN ----
story.append(P('h2', 'D. TỰ LUẬN (3 CÂU)'))
essay = [
 ('Câu 1 (CHƯƠNG 1 — 1.3 Phép toán trên tập hợp).',
  'Cho các tập hợp: A = {x ∈ Z | −2 ≤ x < 5};  B = {x ∈ Z | x là số chẵn, −2 ≤ x ≤ 4}.\n'
  'Tìm A ∩ B, A ∪ B và phần bù của B trong A (kí hiệu C_A B).',
  'Ta liệt kê: A = {−2; −1; 0; 1; 2; 3; 4}; B = {−2; 0; 2; 4}.\n'
  '• A ∩ B = {−2; 0; 2; 4}.\n'
  '• A ∪ B = A = {−2; −1; 0; 1; 2; 3; 4}.\n'
  '• Vì B ⊂ A nên C_A B = A \ B = {−1; 1; 3}.\n'
  'Vậy A ∩ B = {−2; 0; 2; 4}; A ∪ B = {−2; −1; 0; 1; 2; 3; 4}; C_A B = {−1; 1; 3}.'),
 ('Câu 2 (CHƯƠNG 3 — 3.2 Hệ thức lượng trong tam giác, ứng dụng thực tiễn).',
  'Từ điểm A, người ta quan sát thấy hai địa điểm B và C nằm về hai phía của một vật cản. Biết AB = 200 m, '
  'góc BAC = 60° và góc ABC = 30°. Tính khoảng cách BC, độ dài AC và diện tích tam giác ABC.',
  'Trong tam giác ABC: C = 180° − A − B = 180° − 60° − 30° = 90°.\n'
  'Theo định lí sin: BC/sin A = AB/sin C → BC = AB·sin A/sin C = 200·(√3/2)/1 = 100√3 ≈ 173,2 m.\n'
  'AC = AB·sin B/sin C = 200·(1/2)/1 = 100 m.\n'
  'Diện tích: S = (1/2)·BC·AC = (1/2)·100√3·100 = 5000√3 ≈ 8660 m².\n'
  'Vậy BC ≈ 173,2 m; AC = 100 m; S ≈ 8660 m².'),
 ('Câu 3 (CHƯƠNG 2 — 2.2 Hệ BPT bậc nhất hai ẩn, ứng dụng thực tiễn).',
  'Một công ty sản xuất bàn và ghế. Mỗi bàn cần 2 giờ gia công và 1 m² gỗ; mỗi ghế cần 1 giờ gia công và 1 m² gỗ. '
  'Mỗi ngày công ty có 16 giờ gia công và 12 m² gỗ. Lợi nhuận mỗi bàn là 80.000 đồng, mỗi ghế là 50.000 đồng. '
  'Tìm số bàn, số ghế cần sản xuất để lợi nhuận cao nhất.',
  'Gọi x, y là số bàn, số ghế sản xuất. Hệ BPT:\n'
  '  2x + y ≤ 16  (giờ gia công)\n'
  '  x + y ≤ 12   (gỗ)\n'
  '  x ≥ 0; y ≥ 0.\n'
  'Miền nghiệm là tứ giác với các đỉnh: O(0;0), M(0;12), N(4;8), P(8;0).\n'
  'Lợi nhuận P = 80x + 50y (nghìn đồng). Tính tại các đỉnh:\n'
  '  O: 0;  M: 600;  N: 80·4 + 50·8 = 720;  P: 640.\n'
  'GT lớn nhất là 720 (nghìn đồng) tại N(4; 8).\n'
  'Vậy sản xuất 4 bàn và 8 ghế thì lợi nhuận cao nhất là 720.000 đồng.'),
]
for title, question, sol in essay:
    story.append(P('q', title))
    story.append(P('q', question))
    story.append(P('ans', 'Lời giải:'))
    story.append(P('sol', sol))
    story.append(Spacer(1, 3))
story.append(PageBreak())

# ============ PHẦN IV ============
story.append(P('h1', 'PHẦN IV — LƯU Ý ÔN TẬP VÀ KẾ HOẠCH ÔN TẬP'))
story.append(P('h3', '1. Những sai lầm thường gặp'))
story.append(bullet('Mệnh đề: phân biệt rõ mệnh đề, mệnh đề chứa biến; phủ định đổi "không/không phải"; P ⇒ Q chỉ sai khi P đúng và Q sai.'))
story.append(bullet('Tập hợp: tập rỗng ∅ ≠ {0}; tập {0} có 1 phần tử; dấu ngoặc ( ) và [ ] quyết định đầu mút thuộc hay không thuộc.'))
story.append(bullet('BPT bậc nhất hai ẩn: chỉ có 2 ẩn và bậc nhất; kiểm tra a, b không đồng thời bằng 0; với "<", ">" bờ d cần vẽ nét đứt.'))
story.append(bullet('GT lượng giác: góc bù có sin bằng nhau, cos/tan/cot đối nhau; máy tính chỉ cho giá trị x ≤ 90° khi biết sin x.'))
story.append(bullet('Định lí sin/cosin: ghép đúng cạnh với góc đối diện; kiểm tra bất đẳng thức tam giác khi biết 3 cạnh.'))
story.append(bullet('Vectơ: cùng độ dài chưa đủ để bằng nhau (cần cùng hướng); vectơ-không cùng phương, cùng hướng với mọi vectơ.'))

story.append(P('h3', '2. Kế hoạch ôn tập (gợi ý 7 ngày)'))
tbl_plan = [
    [P('cellh', 'Ngày'), P('cellh', 'Nội dung ôn tập'), P('cellh', 'Mục tiêu')],
    [P('cellL', '1'), P('cellL', 'Chương 1: mệnh đề (phủ định, kéo theo, đảo, tương đương, ∀/∃)'), P('cellL', 'Nhận biết, TH')],
    [P('cellL', '2'), P('cellL', 'Chương 1: tập hợp và phép toán (giao, hợp, hiệu, phần bù, Ven)'), P('cellL', 'Vận dụng')],
    [P('cellL', '3'), P('cellL', 'Chương 2: BPT và hệ BPT bậc nhất hai ẩn (miền nghiệm, tối ưu)'), P('cellL', 'Vận dụng')],
    [P('cellL', '4'), P('cellL', 'Chương 3.1: GT lượng giác góc 0°–180°, bảng GT đặc biệt, góc bù/phụ'), P('cellL', 'Nhận biết, TH')],
    [P('cellL', '5'), P('cellL', 'Chương 3.2: định lí sin, cosin, diện tích, giải tam giác'), P('cellL', 'Vận dụng')],
    [P('cellL', '6'), P('cellL', 'Chương 4: vectơ (khái niệm, tính chất, quy tắc ba điểm, hình bình hành)'), P('cellL', 'Nhận biết, TH')],
    [P('cellL', '7'), P('cellL', 'Luyện tập toàn diện (đề ôn tập phần III) và tổng kết lại công thức'), P('cellL', 'Tổng hợp')],
]
t = Table(tbl_plan, colWidths=[1.6*cm, 11.0*cm, 3.2*cm], repeatRows=1)
t.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), BLUE),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, LBLUE]),
    ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#B9C7DA')),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 3.5), ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
]))
story.append(t)
story.append(Spacer(1, 8))
story.append(P('h3', '3. Công thức cần nhớ (tóm tắt nhanh)'))
story.append(bullet('Phủ định: ¬P trái ngược P;  (∀x, P(x)) phủ định = ∃x, ¬P(x);  (∃x, P(x)) phủ định = ∀x, ¬P(x).'))
story.append(bullet('Giao ∩, hợp ∪, hiệu \\, phần bù C_S T = S \\ T; n(S ∪ T) = n(S) + n(T) − n(S ∩ T); số tập con = 2^n.'))
story.append(bullet('BPT bậc nhất hai ẩn: ax + by ≤ c; miền nghiệm là một nửa mặt phẳng bờ d: ax + by = c.'))
story.append(bullet('sin(180° − α) = sin α;  cos(180° − α) = −cos α;  tan(180° − α) = −tan α.'))
story.append(bullet('a² = b² + c² − 2bc·cos A;  a/sin A = b/sin B = c/sin C = 2R;  S = (1/2)bc·sin A = abc/(4R).'))
story.append(bullet('**AB** + **BC** = **AC**;  **AB** = **OB** − **OA**;  A, B, C thẳng hàng ⇔ **AB** ∥ **AC**.'))
story.append(Spacer(1, 10))
story.append(P('note',
    'Đề cương ôn tập này được biên soạn theo chương trình Toán 10 "Kết nối tri thức", bám sát mục tiêu, hình thức '
    'và bảng đặc tả của đề kiểm tra giữa kì I năm học 2026–2027 (TRƯỜNG THPT HÀ HUY TẬP). '
    'Chúc các em ôn tập hiệu quả và đạt kết quả cao trong kỳ kiểm tra!'))


# ============ BUILD ============
def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('DJV', 7.5)
    canvas.setFillColor(GREY)
    canvas.drawString(2*cm, A4[1] - 1.1*cm, 'ĐỀ CƯƠNG ÔN TẬP TOÁN 10 — Kết nối tri thức — Giữa kì I 2026–2027')
    canvas.drawRightString(A4[0] - 2*cm, A4[1] - 1.1*cm, 'THPT Hà Huy Tập')
    canvas.setStrokeColor(colors.HexColor('#B9C7DA'))
    canvas.setLineWidth(0.5)
    canvas.line(2*cm, A4[1] - 1.25*cm, A4[0] - 2*cm, A4[1] - 1.25*cm)
    canvas.line(2*cm, 1.35*cm, A4[0] - 2*cm, 1.35*cm)
    canvas.drawCentredString(A4[0]/2, 0.95*cm, 'Trang %d' % doc.page)
    canvas.restoreState()


OUT = '/home/user/toan-10/ĐỀ CƯƠNG ÔN TẬP TOÁN 10 - GIỮA KÌ I (2026-2027).pdf'
doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=2*cm, rightMargin=2*cm,
                      topMargin=1.8*cm, bottomMargin=1.7*cm,
                      title='Đề cương ôn tập Toán 10 - Kết nối tri thức - Giữa kì I 2026-2027',
                      author='THPT Hà Huy Tập - Tổ Toán-Tin')
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='main')
doc.addPageTemplates([PageTemplate(id='page', frames=[frame], onPage=header_footer)])
doc.build(story)
print('OK ->', OUT)
