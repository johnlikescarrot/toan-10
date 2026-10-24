# -*- coding: utf-8 -*-
"""Chương 3 – Hệ thức lượng trong tam giác."""
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, Spacer

from design import BOX, BULL, EQ, H1, H2, H3, NUM, P, PRACTICE, Spacer, TBL
from figures import TriangleFigure


def chapter():
    e = []
    e += H1('3', 'Hệ thức lượng trong tam giác', 'Chương 3  ·  3,00 điểm')
    e += [P('Đây là chương nặng nhất về công thức: bốn công thức diện tích, hai định lí, thêm bán '
            'kính ngoại tiếp và nội tiếp. Nhưng đề chỉ hỏi ở mức áp dụng trực tiếp và một bài '
            'toán thực tế, nên chiến lược đúng là <b>thuộc bảng giá trị đặc biệt</b> và '
            '<b>biết chọn đúng công thức</b> cho từng kiểu dữ kiện.', 'lead')]

    # ======================================================================
    e += [H2('3.1. Giá trị lượng giác của một góc từ 0° đến 180°')]

    e += [H3('a) Định nghĩa')]
    e += [P('Trong mặt phẳng tọa độ Oxy, lấy nửa đường tròn đơn vị (bán kính 1, nằm phía trên trục '
            'hoành). Với góc α (0° ≤ α ≤ 180°), lấy điểm M trên nửa đường tròn sao cho '
            'xOM = α, giả sử M(x₀; y₀). Khi đó:')]
    e += EQ('sin α = y₀,    cos α = x₀,    tan α = y₀/x₀ (x₀ ≠ 0),    cot α = x₀/y₀ (y₀ ≠ 0)')
    e += [P('Nhờ cách định nghĩa này, giá trị lượng giác được mở rộng cho góc tù, điều mà tỉ số '
            'lượng giác trong tam giác vuông (lớp 9) không làm được.')]
    e += [Spacer(1, 2)]

    e += [H3('b) Bảng giá trị lượng giác của các góc đặc biệt')]
    e += [TBL(['α', '0°', '30°', '45°', '60°', '90°', '120°', '135°', '150°', '180°'],
              [['sin α', '0', '1/2', '√2/2', '√3/2', '1', '√3/2', '√2/2', '1/2', '0'],
               ['cos α', '1', '√3/2', '√2/2', '1/2', '0', '−1/2', '−√2/2', '−√3/2', '−1'],
               ['tan α', '0', '√3/3', '1', '√3', '║', '−√3', '−1', '−√3/3', '0'],
               ['cot α', '║', '√3', '1', '√3/3', '0', '−√3/3', '−1', '−√3', '║']],
              widths=[0.9, 0.55, 0.62, 0.62, 0.62, 0.55, 0.7, 0.72, 0.72, 0.72],
              align=['c'] * 10, font_size=8.2)]
    e += [Spacer(1, 3), P('Kí hiệu ║ nghĩa là giá trị không xác định (tan 90° và cot 0°, cot 180° '
                          'không tồn tại).', 'small')]
    e += [Spacer(1, 2)]

    e += [H3('c) Hai góc bù nhau và các hệ thức cơ bản')]
    e += [P('Với hai góc bù nhau α và 180° − α, tung độ của điểm M giữ nguyên còn hoành độ đổi '
            'dấu, do đó:')]
    e += EQ('sin(180° − α) = sin α,    cos(180° − α) = −cos α')
    e += EQ('tan(180° − α) = −tan α,    cot(180° − α) = −cot α')
    e += [P('Nói gọn: <b>sin giữ nguyên, cos và tan, cot đổi dấu</b>. Nhờ đó chỉ cần nhớ bảng '
            'đến 90° là suy ra được mọi góc tù.')]
    e += [Spacer(1, 2)]

    e += BOX('formula', [
        ('eq', 'sin²α + cos²α = 1'),
        ('eq', 'tan α = sin α / cos α   (cos α ≠ 0)'),
        ('eq', 'cot α = cos α / sin α   (sin α ≠ 0)'),
        ('eq', 'tan α · cot α = 1   (sin α ≠ 0, cos α ≠ 0)'),
        ('eq', '1 + tan²α = 1/cos²α,    1 + cot²α = 1/sin²α'),
        'Ba công thức cuối là dạng “nâng cao” nhưng cực nhanh khi phải tính tan, cot từ sin, cos.'],
        'Bốn hệ thức lượng giác cơ bản')

    e += [H3('d) Dạng toán: tính giá trị lượng giác khi biết một giá trị')]
    e += [P('Đây là câu trả lời ngắn số 3 của đề. Quy trình luôn gồm ba bước: dùng '
            'sin²α + cos²α = 1 để tìm giá trị còn thiếu (chú ý <b>dấu</b> phụ thuộc góc nhọn hay '
            'góc tù) → tính tan, cot nếu cần → thay vào biểu thức.')]
    e += [Spacer(1, 2)]

    e += BOX('method', [
        '<b>Ví dụ mẫu.</b> Cho cos α = −3/5 với 90° &lt; α &lt; 180°. Tính sin α, tan α và giá trị '
        'biểu thức P = (sin α + 2cos α)/(1 − sin α).',
        '<b>Bước 1.</b> sin²α = 1 − cos²α = 1 − 9/25 = 16/25, suy ra sin α = ±4/5. Vì '
        '90° &lt; α &lt; 180° nên sin α &gt; 0, chọn sin α = 4/5.',
        '<b>Bước 2.</b> tan α = sin α / cos α = (4/5)/(−3/5) = −4/3.',
        '<b>Bước 3.</b> P = (4/5 + 2·(−3/5))/(1 − 4/5) = (4/5 − 6/5)/(1/5) = (−2/5)/(1/5) = −2.'],
        'Lời giải mẫu')

    e += BOX('warn', [
        'Bỏ qua điều kiện của góc là lỗi nặng nhất. sin²α = 16/25 cho <b>hai</b> nghiệm ±4/5; '
        'chỉ điều kiện góc mới quyết định dấu.',
        'Góc tù (90° &lt; α &lt; 180°) thì sin dương, cos âm, tan âm, cot âm.',
        'Với góc nhọn thì cả bốn giá trị đều dương.',
        'Không được viết sin α = −4/5 rồi “bỏ dấu trừ vì sin luôn dương” — sin chỉ luôn dương khi '
        'α ∈ (0°; 180°), và đó chính là lí do phải xét điều kiện.'],
        'Lỗi dấu')

    # ======================================================================
    e += [H2('3.2. Hệ thức lượng trong tam giác')]

    e += [P('Xét tam giác ABC có BC = a, CA = b, AB = c; R là bán kính đường tròn ngoại tiếp, '
            'r là bán kính đường tròn nội tiếp, p = (a + b + c)/2 là nửa chu vi, S là diện tích.')]

    e += [TriangleFigure(), Spacer(1, 3)]

    e += [H3('a) Định lí côsin')]
    e += EQ('a² = b² + c² − 2bc·cos A')
    e += [P('và tương tự với các cạnh còn lại. Hệ quả dùng để <b>tìm góc</b> khi biết ba cạnh:')]
    e += EQ('cos A = (b² + c² − a²)/(2bc)')
    e += BOX('tip', [
        'Dùng định lí côsin khi biết <b>hai cạnh và góc xen giữa</b> (tìm cạnh thứ ba) hoặc biết '
        '<b>ba cạnh</b> (tìm góc). Trong tam giác vuông, khi A = 90° thì cos A = 0 và công thức '
        'trở về định lí Pythagore — dấu hiệu để nhớ công thức: có dấu <b>trừ</b>.'],
        'Khi nào dùng')

    e += [H3('b) Định lí sin')]
    e += EQ('a/sin A = b/sin B = c/sin C = 2R')
    e += [P('Dùng khi biết một cạnh và góc đối diện của nó, cần tìm cạnh hoặc góc khác; hoặc khi '
            'cần tính bán kính đường tròn ngoại tiếp.')]

    e += [H3('c) Bốn công thức tính diện tích tam giác')]
    e += [TBL(['Công thức', 'Dùng khi biết'],
              [['S = (1/2)·a·h<sub>a</sub>', 'một cạnh và đường cao tương ứng'],
               ['S = (1/2)·ab·sin C = (1/2)·bc·sin A = (1/2)·ca·sin B',
                'hai cạnh và góc xen giữa'],
               ['S = abc/(4R)', 'ba cạnh và bán kính đường tròn ngoại tiếp'],
               ['S = p·r', 'ba cạnh (để tính p) và bán kính đường tròn nội tiếp'],
               ['S = √(p(p − a)(p − b)(p − c))  (công thức Heron)', 'ba cạnh']],
              widths=[5.2, 3.3])]
    e += [Spacer(1, 3)]

    e += [H3('d) Độ dài đường trung tuyến')]
    e += EQ('m<sub>a</sub>² = (2b² + 2c² − a²)/4')
    e += [P('với m<sub>a</sub> là độ dài đường trung tuyến kẻ từ đỉnh A.')]
    e += [Spacer(1, 2)]

    e += [H3('e) Giải tam giác và bài toán thực tế')]
    e += [P('<b>Giải tam giác</b> là tìm các yếu tố còn lại (cạnh, góc) khi biết một số yếu tố '
            'xác định tam giác. Ba tình huống thường gặp:')]
    e += [BULL([
        'Biết <b>hai cạnh và góc xen giữa</b> → dùng định lí côsin tìm cạnh thứ ba, rồi định lí '
        'sin (hoặc côsin) tìm góc.',
        'Biết <b>ba cạnh</b> → dùng hệ quả định lí côsin tìm góc (nên tìm góc lớn nhất trước để '
        'biết tam giác tù hay nhọn).',
        'Biết <b>một cạnh và hai góc</b> → tính góc thứ ba, rồi dùng định lí sin tìm hai cạnh còn '
        'lại.',
    ])]

    e += BOX('method', [
        '<b>Ví dụ mẫu 1 (đo khoảng cách).</b> Để đo khoảng cách từ A đến C trên bờ hồ bị vật cản, '
        'người ta chọn B sao cho đo được AB = 40 m, góc BAC = 70°, góc ABC = 55°. Tính AC.',
        '<b>Giải.</b> Góc C = 180° − 70° − 55° = 55°. Vậy tam giác ABC cân tại A (vì B = C = 55°) '
        'nên AC = AB = 40 m. Nếu muốn dùng công thức: AC = AB·sin B / sin C = 40·sin55°/sin55° = 40 '
        '(m).'], 'Lời giải mẫu')

    e += BOX('method', [
        '<b>Ví dụ mẫu 2 (đo chiều cao).</b> Từ hai điểm A, B trên mặt đất cách nhau 20 m và thẳng '
        'hàng với chân cột, người ta đo góc nâng của đỉnh cột lần lượt là 30° và 45° (B gần cột '
        'hơn). Tính chiều cao cột.',
        '<b>Giải.</b> Gọi H là chân cột, C là đỉnh cột, h = CH. Trong tam giác vuông CBH: '
        'tan45° = h/BH ⇒ BH = h. Trong tam giác vuông CAH: tan30° = h/AH = h/(h + 20) ⇒ '
        'h + 20 = h√3 ⇒ h(√3 − 1) = 20 ⇒ h = 20/(√3 − 1) = 10(√3 + 1) ≈ <b>27,3 m</b>.'],
        'Lời giải mẫu')

    e += BOX('warn', [
        'Chọn sai công thức là lỗi tốn thời gian nhất. Hãy tự hỏi: “Tôi đang biết cạnh nào, góc '
        'nào, và góc đó có <b>xen giữa</b> hai cạnh không?”',
        'Định lí sin cần cặp <b>cạnh – góc đối diện</b>. Dùng sin với góc kề là sai.',
        'Khi dùng định lí côsin để tìm góc, nếu cos A &lt; 0 thì góc A tù — nhiều bạn bấm máy ra '
        'kết quả âm rồi lấy trị tuyệt đối, dẫn đến sai.',
        'Bài toán thực tế: nhớ đổi đơn vị và làm tròn đúng yêu cầu; nếu đề không nói, ghi kèm '
        'đơn vị đo.'],
        'Bốn lỗi hay mắc')

    e += PRACTICE([
        'Cho sin α = 1/3 với 90° &lt; α &lt; 180°. Tính cos α và tan α.',
        'Tính giá trị của biểu thức A = 2sin 30° + 3cos 45° − tan 60°.',
        'Cho tam giác ABC có a = 7, b = 8, c = 5. Tính cos A và suy ra số đo góc A.',
        'Cho tam giác ABC có a = 6, góc B = 45°, góc C = 60°. Tính cạnh b (làm tròn đến hàng '
        'phần trăm).',
        'Cho tam giác ABC có AB = 4, AC = 6 và góc A = 120°. Tính BC và diện tích tam giác.',
        'Cho tam giác đều cạnh a. Tính bán kính đường tròn ngoại tiếp R, bán kính đường tròn nội '
        'tiếp r và diện tích S theo a.',
    ], '1) cos α = −2√2/3; tan α = −√2/4. '
       '2) A = 1 + 3√2/2 − √3 ≈ 1,39. '
       '3) cos A = (64 + 25 − 49)/(2·8·5) = 1/2 → A = 60°. '
       '4) Góc A = 75°; b = 6·sin45°/sin75° ≈ 4,39. '
       '5) BC² = 16 + 36 − 2·4·6·cos120° = 76 → BC = 2√19 ≈ 8,72; S = ½·4·6·sin120° = 6√3 ≈ 10,39. '
       '6) R = a/√3; r = a/(2√3); S = a²√3/4.')
    e += PRACTICE([
        'Một cột cờ thẳng đứng cao h mét. Từ điểm A cách chân cột 12 m, góc nâng của đỉnh cột là '
        '40°. Tính h (làm tròn đến hàng phần mười).',
        'Cho tam giác ABC có góc A = 120°, b = 5, c = 7. Tính cạnh a, diện tích S và bán kính '
        'đường tròn ngoại tiếp R.',
        'Chứng minh rằng trong mọi tam giác ABC ta luôn có a = 2R·sin A, từ đó giải thích vì sao '
        'cạnh lớn nhất đối diện với góc lớn nhất.',
    ], '7) h = 12·tan 40° ≈ 10,1 m. '
       '8) a² = 25 + 49 − 2·5·7·cos 120° = 109 → a ≈ 10,44; S = ½·5·7·sin 120° = 35√3/4 ≈ 15,16; '
       'R = a/(2sin A) = 10,44/(2·sin 120°) ≈ 6,03. '
       '9) Theo định lí sin, a/sin A = 2R nên a = 2R·sin A. Vì 2R không đổi, cạnh a lớn nhất khi '
       'sin A lớn nhất; với 0° &lt; A &lt; 180° thì sin A đạt giá trị lớn nhất bằng 1 tại A = 90° '
       'và tăng trên (0°; 90°], nên góc càng lớn (trong miền này) thì cạnh đối diện càng lớn.',
       title='Bài tập tự luyện (tiếp)')
    return e
