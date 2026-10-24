# -*- coding: utf-8 -*-
"""Chương 1 – Mệnh đề và tập hợp."""
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, Spacer

from design import (BOX, BULL, EQ, H1, H2, H3, NUM, P, PRACTICE, RULE,
                    TBL, TEAL, TEAL_LIGHT, flatten, PS)
from figures import NumberLine, Venn


def chapter():
    e = []
    e += H1('1', 'Mệnh đề và tập hợp', 'Chương 1  ·  4,00 điểm')
    e += [P('Đây là chương “ăn điểm” của đề: 4 trong 10 điểm, và phần lớn ở mức nhận biết – '
            'thông hiểu. Cái khó duy nhất của chương là <b>kí hiệu</b>: chỉ cần viết sai một dấu '
            'ngoặc là mất điểm cả câu. Hãy học chương này bằng cách viết lại kí hiệu ra giấy '
            'nhiều lần, không chỉ đọc.', 'lead')]

    # ======================================================================
    e += [H2('1.1. Mệnh đề')]

    e += [H3('a) Mệnh đề là gì?')]
    e += [P('<b>Mệnh đề</b> là một câu khẳng định mà tính đúng hoặc sai của nó có thể xác định '
            'được. Một mệnh đề chỉ có thể đúng hoặc sai, không thể vừa đúng vừa sai.')]
    e += [TBL(['Câu', 'Là mệnh đề?', 'Vì sao'],
              [['“Số 2026 chia hết cho 3.”', '<b>Có</b> (sai)',
                'Là câu khẳng định, kiểm tra được: 2 + 0 + 2 + 6 = 10 không chia hết cho 3, '
                'nên mệnh đề này <b>sai</b> — nhưng nó vẫn là mệnh đề.'],
               ['“Hà Nội là thủ đô của Việt Nam.”', '<b>Có</b> (đúng)', 'Khẳng định kiểm chứng được.'],
               ['“Hôm nay trời đẹp quá!”', 'Không', 'Câu cảm thán, không có tính đúng/sai.'],
               ['“Bạn đã làm bài tập chưa?”', 'Không', 'Câu hỏi.'],
               ['“Hãy nộp bài đúng giờ!”', 'Không', 'Câu mệnh lệnh.'],
               ['“x + 3 &gt; 7”', 'Không', 'Chứa biến x, chưa xác định được đúng/sai. Đây là '
                '<b>mệnh đề chứa biến</b>: với x = 5 thì đúng, với x = 1 thì sai.']],
              widths=[3.1, 1.3, 4.1])]
    e += [Spacer(1, 4)]

    e += BOX('warn', [
        'Ba loại câu <b>không</b> phải mệnh đề mà đề thi luôn đưa vào để “bẫy”: câu hỏi, câu '
        'mệnh lệnh/cảm thán, và câu chứa biến chưa gán giá trị. Khi đọc đề, hãy tự hỏi: '
        '“Câu này có trả lời được <i>đúng</i> hoặc <i>sai</i> ngay bây giờ không?”'], 'Ba cái bẫy')

    e += [H3('b) Mệnh đề phủ định')]
    e += [P('Kí hiệu mệnh đề là P. Mệnh đề phủ định của P được kí hiệu là <b>¬P</b> '
            '(trong vở viết là P có gạch ngang trên đầu), đọc là “không P”; nó đúng khi P sai '
            'và sai khi P đúng.')]
    e += [TBL(['Mệnh đề P', 'Mệnh đề phủ định ¬P'],
              [['“Số 5 là số nguyên tố.”', '“Số 5 không phải là số nguyên tố.”'],
               ['“Tổng ba góc của một tam giác bằng 180°.”',
                '“Tổng ba góc của một tam giác không bằng 180°.”'],
               ['“∀x ∈ ℝ, x² ≥ 0.” (đúng)', '“∃x ∈ ℝ, x² &lt; 0.” (sai)'],
               ['“∃n ∈ ℕ, n là số nguyên tố chẵn.” (đúng, n = 2)',
                '“∀n ∈ ℕ, n không là số nguyên tố chẵn.” (sai)']],
              widths=[4.2, 4.3])]
    e += [Spacer(1, 3)]

    e += BOX('formula', [
        ('eq', 'Phủ định của “∀x ∈ X, P(x)” là “∃x ∈ X, ¬P(x)”'),
        ('eq', 'Phủ định của “∃x ∈ X, P(x)” là “∀x ∈ X, ¬P(x)”'),
        'Nói gọn: <b>đổi ∀ thành ∃, đổi ∃ thành ∀, rồi phủ định phần khẳng định phía sau</b>.'],
        'Phủ định mệnh đề chứa kí hiệu ∀, ∃')

    e += [P('<i>Ví dụ.</i> Phủ định mệnh đề “Mọi số tự nhiên đều chia hết cho 1”. Kết quả: '
            '“Tồn tại số tự nhiên không chia hết cho 1” — một mệnh đề sai, đúng như mong đợi vì '
            'mệnh đề gốc đúng.', 'small')]

    e += [H3('c) Mệnh đề kéo theo, mệnh đề đảo, mệnh đề tương đương')]
    e += [TBL(['Khái niệm', 'Cách viết', 'Cách đọc', 'Tính đúng sai'],
              [['Kéo theo', 'P ⇒ Q', '“Nếu P thì Q”, “P suy ra Q”',
                'Chỉ <b>sai</b> khi P đúng mà Q sai.'],
               ['Đảo', 'Q ⇒ P', 'Mệnh đề đảo của P ⇒ Q',
                'Không nhất thiết cùng tính đúng sai với P ⇒ Q.'],
               ['Tương đương', 'P ⇔ Q', '“P khi và chỉ khi Q”, “P nếu và chỉ nếu Q”',
                'Đúng khi P và Q <b>cùng</b> đúng hoặc <b>cùng</b> sai, tức P ⇒ Q và Q ⇒ P đều đúng.']],
              widths=[1.3, 1.2, 2.9, 3.1])]
    e += [Spacer(1, 4)]

    e += BOX('note', [
        '<b>P là điều kiện đủ để có Q</b> — có P là đủ để kết luận Q (nhưng có Q chưa chắc có P).',
        '<b>Q là điều kiện cần để có P</b> — muốn có P thì buộc phải có Q (không có Q thì không '
        'có P).',
        '<b>P ⇔ Q</b>: P là điều kiện <b>cần và đủ</b> của Q (và ngược lại).',
        'Mẹo nhớ: “cần” đứng sau “đủ” trong câu “P đủ, Q cần”.'],
        'Điều kiện cần – điều kiện đủ')

    e += [P('<i>Ví dụ.</i> Cho mệnh đề “Nếu tam giác ABC có hai góc bằng 60° thì ABC là tam giác '
            'đều”. Khi đó “tam giác ABC có hai góc bằng 60°” là <b>điều kiện đủ</b> để ABC đều; '
            '“ABC là tam giác đều” là <b>điều kiện cần</b> để ABC có hai góc bằng 60°. Mệnh đề '
            'đảo “Nếu ABC đều thì ABC có hai góc bằng 60°” cũng đúng, nên ta có mệnh đề tương '
            'đương: “ABC đều ⇔ ABC có hai góc bằng 60°”.', 'small')]

    e += [H3('d) Các dạng toán thường gặp')]
    e += [P('<b>Dạng 1. Nhận diện mệnh đề.</b> Kiểm tra câu đó có phải câu khẳng định có tính '
            'đúng/sai xác định hay không. Loại ngay câu hỏi, câu cảm thán, câu mệnh lệnh, câu '
            'chứa biến tự do.')]
    e += [P('<b>Dạng 2. Lập mệnh đề phủ định.</b> Với mệnh đề thường: thêm “không” hoặc “không '
            'phải” đúng chỗ. Với mệnh đề có ∀, ∃: đổi lượng từ rồi phủ định phần sau.')]
    e += [P('<b>Dạng 3. Xét tính đúng sai.</b> Với mệnh đề “∀”: chỉ cần <b>một</b> phản ví dụ là '
            'đủ kết luận sai. Với mệnh đề “∃”: chỉ cần <b>một</b> ví dụ đúng là đủ kết luận đúng.')]
    e += [P('<b>Dạng 4. Phát biểu điều kiện cần, điều kiện đủ.</b> Từ “P ⇒ Q” đọc thành: “P là '
            'điều kiện đủ để có Q”, hoặc “Q là điều kiện cần để có P”.')]
    e += [Spacer(1, 3)]

    e += BOX('method', [
        '<b>Ví dụ mẫu.</b> Cho mệnh đề P: “∃x ∈ ℤ, x² = 9”. Xét tính đúng sai và lập mệnh đề phủ định.',
        '<b>Giải.</b> Với x = 3 ∈ ℤ ta có 3² = 9, nên P <b>đúng</b>. Vì P dùng lượng từ ∃ nên phủ '
        'định dùng ∀ và phủ định vế sau: “∀x ∈ ℤ, x² ≠ 9”. Mệnh đề này sai (vì x = 3 là phản ví dụ) '
        '— phù hợp với quy luật: phủ định của mệnh đề đúng là mệnh đề sai.'], 'Lời giải mẫu')

    e += BOX('warn', [
        'Sai lầm thường gặp: phủ định “x² = 9” thành “x² = −9”. Phủ định của một đẳng thức là '
        'việc dùng dấu <b>≠</b>, không phải đổi dấu hai vế.',
        'Sai lầm thứ hai: viết “∀x ∈ ℤ, x² ≠ 9” thành “∀x ∈ ℤ, x² &lt; 9”. Đây là phủ định sai '
        'logic.'], 'Lỗi hay mắc')

    # ======================================================================
    e += [H2('1.2. Tập hợp')]

    e += [H3('a) Hai cách xác định tập hợp')]
    e += [P('<b>Cách 1 — liệt kê phần tử:</b> A = {1; 2; 3; 5; 8}. Dùng khi tập hữu hạn và ít '
            'phần tử; các phần tử ngăn cách bởi dấu chấm phẩy.')]
    e += [P('<b>Cách 2 — chỉ ra tính chất đặc trưng:</b> A = {n ∈ ℕ | n là ước của 12}. Đọc là '
            '“tập hợp các số tự nhiên n sao cho n là ước của 12”. Phần trước dấu “|” cho biết '
            'phần tử lấy từ đâu, phần sau là điều kiện.')]
    e += [Spacer(1, 2)]

    e += [H3('b) Tập con, tập hợp bằng nhau, tập rỗng')]
    e += [BULL([
        '<b>A ⊂ B</b> (A là tập con của B) khi mọi phần tử của A đều thuộc B. Khi đó B chứa A, '
        'kí hiệu B ⊃ A.',
        '<b>A = B</b> khi A ⊂ B và B ⊂ A, tức hai tập có đúng cùng các phần tử.',
        '<b>Tập rỗng ∅</b> là tập không có phần tử nào. Quy ước: ∅ là tập con của <b>mọi</b> tập '
        'hợp, kể cả chính nó.',
        '<b>Số tập con</b> của một tập có n phần tử là <b>2ⁿ</b> (kể cả ∅ và chính tập đó). Số '
        '<b>tập con khác rỗng</b> là 2ⁿ − 1; số tập con có đúng k phần tử là C(n, k).',
    ])]
    e += BOX('formula', [
        ('eq', 'A ⊂ B  ⇔  (x ∈ A ⇒ x ∈ B)'),
        ('eq', 'Số tập con của A có n phần tử:  2ⁿ'),
        'Ví dụ: A = {1; 2; 3} có 2³ = 8 tập con: ∅, {1}, {2}, {3}, {1;2}, {1;3}, {2;3}, {1;2;3}.'],
        'Công thức cần nhớ')

    e += [H3('c) Các tập số và các khoảng – đoạn')]
    e += [TBL(['Kí hiệu', 'Tên gọi', 'Gồm các số thực'],
              [['ℕ', 'Số tự nhiên', '0; 1; 2; 3; …'],
               ['ℕ*', 'Số tự nhiên khác 0', '1; 2; 3; …'],
               ['ℤ', 'Số nguyên', '…; −2; −1; 0; 1; 2; …'],
               ['ℚ', 'Số hữu tỉ', 'các số viết được dạng a/b với a, b ∈ ℤ, b ≠ 0'],
               ['ℝ', 'Số thực', 'toàn bộ trục số'],
               ['(a; b)', 'Khoảng', 'a &lt; x &lt; b — <b>không</b> lấy hai đầu mút'],
               ['[a; b]', 'Đoạn', 'a ≤ x ≤ b — lấy <b>cả</b> hai đầu mút'],
               ['[a; b)', 'Nửa khoảng', 'a ≤ x &lt; b — lấy a, không lấy b'],
               ['(a; b]', 'Nửa khoảng', 'a &lt; x ≤ b — không lấy a, lấy b']],
              widths=[1.1, 1.8, 5.6])]
    e += [Spacer(1, 3)]
    e += [P('Với dấu ∞, luôn dùng ngoặc tròn vì ∞ không phải một số: (−∞; a), (−∞; a], '
            '(a; +∞), [a; +∞), (−∞; +∞) = ℝ.', 'small')]

    e += BOX('warn', [
        'Ngoặc tròn <b>(</b> = “không lấy”, ngoặc vuông <b>[</b> = “lấy”. Một chỗ duy nhất luôn '
        'dùng ngoặc tròn là phía có dấu ∞.',
        'Khi biểu diễn trên trục số: ngoặc tròn vẽ <b>dấu chấm rỗng</b> (khoanh tròn), ngoặc '
        'vuông vẽ <b>dấu chấm đặc</b> (tô đen). Phần thuộc tập được tô đậm hoặc gạch chéo.'],
        'Quy tắc ngoặc')

    e += [H3('d) Dạng toán: đếm phần tử, xét quan hệ tập con')]
    e += [P('<b>Ví dụ mẫu.</b> Cho A = {x ∈ ℤ | −2 ≤ x &lt; 3}. Viết A bằng cách liệt kê và cho '
            'biết A có bao nhiêu tập con.')]
    e += [P('<b>Giải.</b> Các số nguyên x thỏa −2 ≤ x &lt; 3 là −2; −1; 0; 1; 2, vậy '
            'A = {−2; −1; 0; 1; 2}, có 5 phần tử. Số tập con là 2⁵ = 32.')]
    e += BOX('warn', [
        'Khi đếm phần tử của một khoảng, hãy viết ra giấy dãy số rồi đếm, đừng tính nhẩm. '
        'Khoảng [a; b] với a, b nguyên có b − a + 1 phần tử; nửa khoảng [a; b) có b − a phần tử.'],
        'Lỗi đếm thiếu một phần tử')

    # ======================================================================
    e += [H2('1.3. Các phép toán trên tập hợp')]

    e += [TBL(['Phép toán', 'Kí hiệu', 'Định nghĩa', 'Đọc là'],
              [['Giao', 'A ∩ B', '{x | x ∈ A <b>và</b> x ∈ B}', '“A giao B” — phần chung'],
               ['Hợp', 'A ∪ B', '{x | x ∈ A <b>hoặc</b> x ∈ B}', '“A hợp B” — gộp cả hai'],
               ['Hiệu', 'A \\ B', '{x | x ∈ A <b>và</b> x ∉ B}', '“A trừ B” — bỏ phần thuộc B'],
               ['Phần bù', 'C<sub>ℝ</sub>B', 'ℝ \\ B (chỉ dùng khi B ⊂ ℝ)',
                '“phần bù của B trong ℝ”']],
              widths=[1.2, 1.2, 3.6, 2.5])]
    e += [Spacer(1, 4)]

    e += BOX('formula', [
        ('eq', 'A ∩ B ⊂ A ⊂ A ∪ B   và   A ∩ B ⊂ B ⊂ A ∪ B'),
        ('eq', 'A \\ B = A ∩ C<sub>ℝ</sub>B'),
        ('eq', '|A ∪ B| = |A| + |B| − |A ∩ B|'),
        'Công thức cuối là công thức <b>đếm</b> dùng cho bài toán thực tế (câu 16 của đề).'],
        'Các hệ thức cần nhớ')

    e += [H3('a) Cách tìm giao, hợp, hiệu của các khoảng')]
    e += [NUM([
        '<b>Vẽ trục số</b> và biểu diễn từng tập: tô phần thuộc tập, dùng chấm rỗng/đặc cho đầu mút.',
        '<b>Giao</b> = phần bị tô <b>hai lần</b> (phần chung). <b>Hợp</b> = phần được tô ít nhất '
        'một lần. <b>Hiệu A \\ B</b> = phần tô của A mà không bị tô bởi B.',
        '<b>Đọc kết quả</b> từ trái sang phải, kiểm tra lại từng đầu mút: đầu mút đó có thuộc kết '
        'quả không?',
    ])]
    e += [Spacer(1, 4), NumberLine(), Spacer(1, 5)]
    e += [P('<b>Ví dụ mẫu.</b> Cho A = [−2; 3) và B = (1; 5]. Tìm A ∩ B, A ∪ B, A \\ B, C<sub>ℝ</sub>B.')]
    e += [P('<b>Giải.</b> A ∩ B = (1; 3) — chỉ lấy phần chung, hai đầu 1 và 3 đều không thuộc A '
            'hoặc B nên dùng ngoặc tròn. A ∪ B = [−2; 5] — phủ kín từ −2 đến 5, lấy cả hai đầu. '
            'A \\ B = [−2; 1] — phần của A nằm bên trái B, lấy cả điểm 1 vì 1 ∉ B. '
            'C<sub>ℝ</sub>B = (−∞; 1] ∪ (5; +∞) — bù của (1; 5] là mọi số ≤ 1 hoặc &gt; 5.')]
    e += [Spacer(1, 3)]

    e += BOX('warn', [
        'Sai lầm phổ biến nhất của cả chương: lấy sai đầu mút. Hãy tự hỏi với từng đầu mút a: '
        '“a có thuộc A không? a có thuộc B không?” rồi mới quyết định ngoặc.',
        'Với phép <b>hiệu</b> A \\ B, hãy nhớ: những điểm thuộc B nhưng nằm ngoài A thì không ảnh '
        'hưởng gì; những điểm vừa thuộc A vừa thuộc B thì bị loại.',
        'Không được viết C<sub>ℝ</sub>B khi B không phải tập con của ℝ (ví dụ không viết '
        'C<sub>ℕ</sub>A).'], 'Ba lỗi mất điểm')

    e += [H3('b) Biểu đồ Ven và bài toán đếm')]
    e += [P('Biểu đồ Ven biểu diễn tập hợp bằng các đường cong khép kín. Phần chung của hai vòng '
            'tròn là A ∩ B; toàn bộ vùng bên trong hai vòng là A ∪ B; phần thuộc A nhưng ngoài B '
            'là A \\ B. Với bài toán “mỗi học sinh có thể chọn nhiều hoạt động”, hãy điền số vào '
            'từng miền, bắt đầu từ miền giao, rồi mới suy ra các miền còn lại.')]
    e += [Spacer(1, 4), Venn(), Spacer(1, 5)]
    e += [P('<b>Ví dụ mẫu.</b> Lớp 10A có 40 học sinh. Có 25 bạn tham gia câu lạc bộ Toán, 18 bạn '
            'tham gia câu lạc bộ Tin, 10 bạn tham gia cả hai. Hỏi có bao nhiêu bạn không tham gia '
            'câu lạc bộ nào?')]
    e += [P('<b>Giải.</b> Gọi A, B là tập học sinh tham gia CLB Toán, Tin. Số bạn tham gia ít nhất '
            'một CLB là |A ∪ B| = 25 + 18 − 10 = 33. Vậy số bạn không tham gia CLB nào là '
            '40 − 33 = <b>7</b>.')]
    e += [Spacer(1, 2)]

    e += BOX('tip', [
        'Với bài toán có ba nhóm (Toán, Lí, Hóa), hãy điền vào biểu đồ Ven từ trong ra ngoài: '
        'miền ba nhóm trước, rồi đến từng miền hai nhóm (nhớ trừ phần đã điền), cuối cùng mới '
        'đến miền một nhóm. Đây là cách chắc chắn không bị đếm trùng.'],
        'Mẹo với bài toán ba tập hợp')

    e += PRACTICE([
        'Lập mệnh đề phủ định của mệnh đề “∀x ∈ ℝ, x² − 2x + 2 &gt; 0” và cho biết mệnh đề phủ '
        'định đúng hay sai.',
        'Cho A = {−1; 0; 1; 2; 3} và B = {x ∈ ℤ | |x| ≤ 2}. Tìm A ∩ B, A ∪ B và A \\ B.',
        'Cho A = (−∞; 4] và B = (2; +∞). Tìm A ∩ B, A ∪ B và C<sub>ℝ</sub>A.',
        'Tập hợp X = {1; 2; 3; 4; 5} có bao nhiêu tập con có đúng hai phần tử?',
        'Lớp 10B có 35 học sinh, trong đó 20 bạn thích bóng đá, 15 bạn thích bóng rổ và 8 bạn '
        'thích cả hai môn. Có bao nhiêu bạn không thích môn nào trong hai môn đó?',
        'Cho mệnh đề “Nếu số nguyên n chia hết cho 6 thì n chia hết cho 3”. Phát biểu mệnh đề '
        'này bằng “điều kiện cần” và “điều kiện đủ”.',
    ], '1) “∃x ∈ ℝ, x² − 2x + 2 ≤ 0” — sai, vì x² − 2x + 2 = (x − 1)² + 1 &gt; 0 với mọi x. '
       '2) A ∩ B = {−1; 0; 1; 2}; A ∪ B = {−2; −1; 0; 1; 2; 3}; A \\ B = {3}. '
       '3) A ∩ B = (2; 4]; A ∪ B = ℝ; C<sub>ℝ</sub>A = (4; +∞). '
       '4) 10 tập (tổ hợp chập 2 của 5). '
       '5) 35 − (20 + 15 − 8) = 8 bạn. '
       '6) “n chia hết cho 6” là điều kiện đủ để n chia hết cho 3; “n chia hết cho 3” là điều '
       'kiện cần để n chia hết cho 6.')
    return e
