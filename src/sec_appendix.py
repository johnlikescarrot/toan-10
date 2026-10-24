# -*- coding: utf-8 -*-
"""Phần 4 – Bảng đáp án, chẩn đoán lỗi, lộ trình ôn tập, phiếu công thức."""
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, Spacer

from design import (AMBER, AMBER_LIGHT, BOX, BULL, CREAM, FRAME_W, GREEN, GREY,
                    H1, H2, H3, INK, LINE, NAVY, NUM, P, PLUM, RULE, TBL, TEAL,
                    TEAL_LIGHT, PS)


def appendix():
    e = []
    e += H1('IV', 'Tra cứu nhanh và lộ trình ôn tập', 'Phần 4  ·  Dùng trước ngày thi')
    e += [P('Phần này để dùng trong hai ngày cuối: tra đáp án trong 30 giây, tự chẩn đoán lỗ hổng, '
            'và ôn lại toàn bộ công thức trên một vài trang.', 'lead')]

    # ------------------------------------------------------------------
    e += [H2('D.1. Bảng đáp án')]
    e += [TBL(['Câu', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
              [['Đáp án', 'B', 'C', 'A', 'C', 'B', 'B', 'C', 'A', 'B', 'A', 'B', 'B']],
              widths=[1.5] + [0.72] * 12,
              align=[None] + ['c'] * 12, font_size=8.4)]
    e += [Spacer(1, 4)]
    e += [TBL(['Câu', '13', '14', '15', '16', '17', '18'],
              [['Đáp án', 'a) Đ · b) Đ · c) Đ · d) S', 'a) Đ · b) Đ · c) S · d) S',
                '2', '7', '√3/2', 'S = 6']],
              widths=[1.1, 2.5, 2.5, 0.7, 0.7, 1.0, 1.0],
              align=[None] + ['c'] * 6, font_size=8.2)]
    e += [Spacer(1, 4)]
    e += [TBL(['Câu', 'Nội dung', 'Kết quả'],
              [['19', 'A ∩ B;  A ∪ C;  C<sub>ℝ</sub>B',
                '(0; 2);  (−∞; 2);  (−∞; 0]'],
               ['20', 'Khoảng cách AC', '50√6 ≈ 122,5 m'],
               ['21', 'Số sản phẩm mỗi loại', '40 loại I và 20 loại II · lãi 22 triệu đồng']],
              widths=[0.7, 3.2, 4.6], align=['c', None, None])]
    e += [Spacer(1, 6)]

    # ------------------------------------------------------------------
    e += [H2('D.2. Thang điểm tự chấm')]
    e += [P('Chấm theo đúng quy chế của đề rồi đối chiếu bảng dưới đây. Mốc điểm quan trọng nhất '
            'không phải là 10 mà là <b>6,5</b>: từ mức này trở lên, bạn đã nắm được toàn bộ kiến '
            'thức nền của học kì.')]
    e += [TBL(['Khoảng điểm', 'Mức độ', 'Việc cần làm ngay'],
              [['9,0 – 10', 'Xuất sắc', 'Ôn kĩ câu 21 và các bài tối ưu; luyện tốc độ để không '
                'mất điểm trình bày.'],
               ['7,5 – 8,9', 'Tốt', 'Rà lại các câu đúng/sai (dễ mất 0,5 mỗi ý) và phần tự luận '
                'trình bày.'],
               ['6,5 – 7,4', 'Trung bình khá', 'Học lại chương 3 (công thức diện tích, định lí '
                'sin – côsin) và luyện lại câu 19, 20.'],
               ['5,0 – 6,4', 'Trung bình', 'Quay lại Phần 1 của cả bốn chương; làm lại toàn bộ đề '
                'sau 3 ngày.'],
               ['Dưới 5,0', 'Cần củng cố', 'Bắt đầu từ chương 1: mệnh đề, tập hợp là gốc của mọi '
                'câu khác. Học theo lộ trình 7 ngày ở mục D.5.']],
              widths=[1.3, 1.5, 5.4], align=['c', None, None])]
    e += [Spacer(1, 6)]

    e += [Spacer(1, 8), H2('D.3. Biểu điểm chi tiết phần tự luận')]
    e += [P('Dùng bảng này để tự chấm phần tự luận một cách khách quan, thay vì chỉ so kết quả '
            'cuối. Điểm được chia theo bước làm, đúng như cách chấm của giáo viên.')]
    e += [TBL(['Câu', 'Bước', 'Điểm'],
              [['19', 'Viết đúng A, B, C dưới dạng khoảng / nửa khoảng', '0,25'],
               ['', 'Tìm đúng A ∩ B = (0; 2)', '0,25'],
               ['', 'Tìm đúng A ∪ C = (−∞; 2)', '0,25'],
               ['', 'Tìm đúng C<sub>ℝ</sub>B = (−∞; 0]', '0,25'],
               ['20', 'Tính đúng góc C = 45°', '0,25'],
               ['', 'Chọn và viết đúng định lí sin cho cạnh AC', '0,25'],
               ['', 'Thay số, tính đúng AC = 50√6', '0,25'],
               ['', 'Kết luận có đơn vị và làm tròn đúng 122,5 m', '0,25'],
               ['21', 'Đặt ẩn, nêu điều kiện x ≥ 0, y ≥ 0', '0,25'],
               ['', 'Lập đúng hệ bất phương trình và hàm mục tiêu', '0,25'],
               ['', 'Xác định đúng bốn đỉnh của miền nghiệm', '0,25'],
               ['', 'Tính F tại các đỉnh và kết luận đúng phương án', '0,25']],
              widths=[0.7, 5.6, 0.9], align=['c', None, 'c'], font_size=8.4)]
    e += [Spacer(1, 6)]

    e += [Spacer(1, 6)]

    # ------------------------------------------------------------------
    e += [H2('D.4. Bảng chẩn đoán lỗi')]
    e += [P('Sau khi chấm, hãy điền vào bảng này. Cột “số câu sai” giúp bạn nhận ra lỗ hổng nằm ở '
            'kiến thức hay ở kĩ năng trình bày — hai loại lỗi này cần hai cách sửa khác nhau.')]
    rows = []
    diag = [
        ('Nhận diện mệnh đề, phủ định, ∀ – ∃', '1, 2', 'Nhầm câu hỏi / mệnh lệnh là mệnh đề; '
         'quên đổi lượng từ khi phủ định'),
        ('Tập con, tập hợp bằng nhau, số tập con', '3, 13a', 'Quên tập rỗng; nhầm 2ⁿ với n²'),
        ('Giao, hợp, hiệu, phần bù', '4, 13b–d, 15, 19', 'Lấy sai đầu mút; quên trừ phần giao'),
        ('Bài toán đếm bằng biểu đồ Ven', '16', 'Không trừ phần giao nên đếm trùng'),
        ('Bất phương trình bậc nhất hai ẩn', '5, 14', 'Không kiểm tra “a, b không đồng thời '
         'bằng 0”; nhầm nét liền / nét đứt'),
        ('Hệ bất phương trình, bài toán tối ưu', '6, 21', 'Quên x ≥ 0, y ≥ 0; không thử đủ đỉnh'),
        ('Giá trị lượng giác, góc bù', '7, 8, 17', 'Sai dấu khi góc tù; bỏ qua điều kiện góc'),
        ('Định lí côsin, định lí sin', '9, 10, 20', 'Chọn sai định lí; quên lấy căn bậc hai'),
        ('Công thức diện tích tam giác', '18', 'Nhầm p với chu vi; quên chia 2'),
        ('Khái niệm vectơ', '11, 12', 'Đồng nhất “cùng phương” với “cùng hướng”'),
    ]
    for name, qs, why in diag:
        rows.append([name, qs, why, '', ''])
    e += [TBL(['Đơn vị kiến thức', 'Câu', 'Lỗi thường gặp', 'Số câu sai', 'Ôn lại ở'],
              rows,
              widths=[2.5, 1.15, 3.05, 1.0, 1.0],
              align=[None, 'c', None, 'c', 'c'], font_size=8.2)]
    e += [Spacer(1, 5)]

    # ------------------------------------------------------------------
    e += [H2('D.5. Lộ trình ôn tập 7 ngày')]
    e += [P('Lộ trình dưới đây giả định bạn có khoảng 90 phút mỗi ngày. Nếu có ít thời gian hơn, '
            'hãy giữ nguyên thứ tự nhưng gộp ngày 1–2 và ngày 5–6.')]
    e += [TBL(['Ngày', 'Nội dung', 'Sản phẩm cần đạt'],
              [['<b>1</b>', 'Chương 1: mệnh đề (định nghĩa, phủ định, kéo theo, tương đương, '
                'điều kiện cần – đủ). Làm câu 1, 2, 13.', 'Viết lại được 3 mệnh đề và phủ định '
                'của chúng không cần nhìn sách.'],
               ['<b>2</b>', 'Chương 1: tập hợp và các phép toán. Làm câu 3, 4, 15, 16, 19.',
                'Vẽ trục số và tìm đúng giao, hợp, hiệu của 3 cặp khoảng bất kì.'],
               ['<b>3</b>', 'Chương 2: bất phương trình, hệ bất phương trình, bài toán tối ưu. '
                'Làm câu 5, 6, 14, 21.', 'Trình bày trọn vẹn một bài tối ưu trong 12 phút.'],
               ['<b>4</b>', 'Chương 3: giá trị lượng giác, góc bù, hệ thức cơ bản. Học thuộc bảng '
                'giá trị đặc biệt. Làm câu 7, 8, 17.', 'Điền bảng giá trị đặc biệt trong 3 phút, '
                'không sai ô nào.'],
               ['<b>5</b>', 'Chương 3: định lí côsin, định lí sin, diện tích, giải tam giác. '
                'Làm câu 9, 10, 18, 20.', 'Giải được một tam giác khi biết hai cạnh và góc xen '
                'giữa trong 5 phút.'],
               ['<b>6</b>', 'Chương 4: khái niệm vectơ. Làm câu 11, 12. Sau đó làm lại toàn bộ đề '
                'trong 90 phút.', 'Điểm lần hai cao hơn lần một ít nhất 1,5 điểm.'],
               ['<b>7</b>', 'Chỉ ôn phiếu công thức (mục D.6) và bảng chẩn đoán lỗi. Không làm đề '
                'mới.', 'Đọc lại đúng những dòng mình đã đánh dấu sai.']],
              widths=[0.7, 4.4, 3.1], align=['c', None, None], font_size=8.4)]
    e += [Spacer(1, 6)]

    # ------------------------------------------------------------------
    e += [H2('D.6. Phiếu công thức')]

    e += [H3('Chương 1 – Mệnh đề và tập hợp')]
    e += [TBL(['Nội dung', 'Công thức / cách viết'],
              [['Phủ định ∀, ∃', '¬(∀x, P(x)) = ∃x, ¬P(x)   ·   ¬(∃x, P(x)) = ∀x, ¬P(x)'],
               ['Số tập con', 'tập có n phần tử → 2ⁿ tập con'],
               ['Giao, hợp', 'A ∩ B = {x | x ∈ A và x ∈ B}   ·   A ∪ B = {x | x ∈ A hoặc x ∈ B}'],
               ['Hiệu, phần bù', 'A \\ B = {x | x ∈ A và x ∉ B}   ·   C<sub>ℝ</sub>B = ℝ \\ B'],
               ['Công thức đếm', '|A ∪ B| = |A| + |B| − |A ∩ B|'],
               ['Ngoặc', '( ) không lấy đầu mút · [ ] lấy đầu mút · ∞ luôn đi với ( )']],
              widths=[1.6, 6.3], font_size=8.4)]
    e += [Spacer(1, 5)]

    e += [H3('Chương 2 – Bất phương trình bậc nhất hai ẩn')]
    e += [TBL(['Nội dung', 'Cách làm'],
              [['Dạng tổng quát', 'ax + by ≤ c (a, b không đồng thời bằng 0)'],
               ['Vẽ miền nghiệm', 'vẽ Δ: ax + by = c → nét liền nếu có dấu ≤, ≥; nét đứt nếu &lt;, '
                '&gt; → thử điểm O(0; 0) → kết luận'],
               ['Miền nghiệm của hệ', 'giao các miền nghiệm; thường là một đa giác'],
               ['Bài toán tối ưu', 'lập hệ → tìm các đỉnh → tính F tại từng đỉnh → chọn max/min']],
              widths=[1.6, 6.3], font_size=8.4)]
    e += [Spacer(1, 5)]

    e += [H3('Chương 3 – Hệ thức lượng trong tam giác')]
    e += [TBL(['Nội dung', 'Công thức'],
              [['Hệ thức cơ bản', 'sin²α + cos²α = 1 · tan α = sin α/cos α · '
                '1 + tan²α = 1/cos²α'],
               ['Góc bù', 'sin(180° − α) = sin α · cos(180° − α) = −cos α · '
                'tan(180° − α) = −tan α'],
               ['Định lí côsin', 'a² = b² + c² − 2bc·cos A'],
               ['Hệ quả', 'cos A = (b² + c² − a²)/(2bc)'],
               ['Định lí sin', 'a/sin A = b/sin B = c/sin C = 2R'],
               ['Diện tích', 'S = ½ah<sub>a</sub> = ½ab sin C = abc/(4R) = pr = '
                '√(p(p−a)(p−b)(p−c))'],
               ['Trung tuyến', 'm<sub>a</sub>² = (2b² + 2c² − a²)/4']],
              widths=[1.6, 6.3], font_size=8.4)]
    e += [Spacer(1, 5)]

    e += [H3('Chương 4 – Vectơ')]
    e += [TBL(['Nội dung', 'Cách viết'],
              [['Vectơ, độ dài', '→AB; |→AB| = AB'],
               ['Cùng phương', 'giá song song hoặc trùng nhau'],
               ['Bằng nhau', 'cùng hướng <b>và</b> cùng độ dài'],
               ['Đối nhau', 'cùng độ dài, ngược hướng: →AB = −→BA'],
               ['Vectơ – không', '→0 = →AA, độ dài 0, cùng phương và cùng hướng với mọi vectơ']],
              widths=[1.6, 6.3], font_size=8.4)]

    e += [Spacer(1, 8)]
    e += BOX('tip', [
        'Trước khi vào phòng thi, chỉ cần đọc ba thứ: <b>bảng đáp án D.1</b> để tự tin, '
        '<b>bảng chẩn đoán D.4</b> để nhớ lỗi của chính mình, và <b>phiếu công thức D.6</b> để '
        'không quên công thức nào.',
        'Trong phòng thi, hãy làm đúng thứ tự: câu dễ trước, câu đúng/sai đánh dấu từng ý, bài '
        'tối ưu để cuối. Và luôn kiểm tra lại các đầu mút của khoảng — đó là nơi mất điểm nhiều '
        'nhất của học sinh lớp 10.'],
        'Lời nhắn cuối')
    return e
