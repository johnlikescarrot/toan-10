# -*- coding: utf-8 -*-
"""Chương 4 – Vectơ (khái niệm vectơ)."""
from reportlab.platypus import Paragraph, Spacer

from design import BOX, BULL, EQ, H1, H2, H3, P, PRACTICE, TBL


def chapter():
    e = []
    e += H1('4', 'Vectơ', 'Chương 4  ·  0,50 điểm')
    e += [P('Chỉ 2 câu trắc nghiệm (0,5 điểm) nhưng đây là <b>điểm chắc chắn lấy được</b>: toàn bộ '
            'nội dung kiểm tra là định nghĩa và nhận dạng. Chỉ cần phân biệt được bốn cặp khái '
            'niệm “cùng phương – cùng hướng – bằng nhau – đối nhau” là đủ.', 'lead')]

    e += [H2('4.1. Khái niệm vectơ')]

    e += [H3('a) Định nghĩa và kí hiệu')]
    e += [P('<b>Vectơ</b> là một đoạn thẳng có hướng, tức là đã chỉ rõ điểm đầu và điểm cuối. '
            'Vectơ có điểm đầu A, điểm cuối B được kí hiệu là <b>→AB</b> (trong vở viết có mũi tên '
            'trên đầu). Vectơ còn được kí hiệu bằng một chữ in thường có mũi tên, ví dụ →a, →x.')]
    e += [P('<b>Độ dài vectơ</b> →AB, kí hiệu |→AB|, là độ dài đoạn thẳng AB. Như vậy '
            '|→AB| = AB ≥ 0 và |→AB| = |→BA|.')]
    e += [Spacer(1, 2)]

    e += [H3('b) Giá của vectơ')]
    e += [P('<b>Giá</b> của vectơ →AB là đường thẳng đi qua hai điểm A và B. Hai vectơ được gọi là '
            '<b>cùng phương</b> nếu giá của chúng song song hoặc trùng nhau.')]
    e += [P('Nếu hai vectơ cùng phương thì chúng hoặc <b>cùng hướng</b>, hoặc <b>ngược hướng</b>. '
            'Về hình: hai vectơ cùng phương cùng hướng khi mũi tên “chĩa về cùng một phía” của '
            'đường thẳng chứa chúng.')]
    e += [Spacer(1, 2)]

    e += BOX('formula', [
        ('eq', 'Cùng phương: giá song song hoặc trùng nhau'),
        ('eq', 'Cùng hướng  ⇒  cùng phương   (nhưng ngược lại thì không đúng)'),
        ('eq', '→AB = →CD   ⇔   →AB và →CD cùng hướng và |→AB| = |→CD|'),
        ('eq', '→AB và →CD đối nhau  ⇔  →AB = −→CD  ⇔  cùng độ dài, ngược hướng'),
        'Đẳng thức vectơ đòi hỏi <b>hai</b> điều kiện cùng lúc: cùng hướng và cùng độ dài.'],
        'Bốn quan hệ giữa hai vectơ')

    e += [H3('c) Vectơ bằng nhau, vectơ đối nhau')]
    e += [P('Hai vectơ <b>bằng nhau</b> nếu chúng cùng hướng và có cùng độ dài. Kí hiệu →AB = →CD. '
            'Hai vectơ <b>đối nhau</b> nếu chúng cùng độ dài và ngược hướng; vectơ đối của →a kí '
            'hiệu là −→a.')]
    e += [P('Lưu ý quan trọng: hai vectơ bằng nhau <b>không</b> bắt buộc phải có cùng điểm đầu và '
            'điểm cuối. Với mỗi vectơ →a cho trước và mỗi điểm O cho trước, tồn tại <b>duy nhất</b> '
            'một điểm M sao cho →OM = →a.')]
    e += [Spacer(1, 2)]

    e += [H3('d) Vectơ – không')]
    e += [P('<b>Vectơ – không</b>, kí hiệu →0, là vectơ có điểm đầu và điểm cuối trùng nhau: '
            '→AA = →BB = →0. Vectơ – không có độ dài bằng 0.')]
    e += [P('Quy ước đặc biệt cần nhớ: <b>vectơ – không cùng phương và cùng hướng với mọi '
            'vectơ</b>. Đây là chi tiết luôn được hỏi trong đề để kiểm tra học sinh có thuộc quy '
            'ước hay không.')]
    e += [Spacer(1, 2)]

    e += BOX('warn', [
        '“Cùng phương” <b>không</b> suy ra “cùng hướng”. Ví dụ ABCD là hình bình hành thì →AB và '
        '→CD cùng phương nhưng <b>ngược hướng</b>.',
        '“Cùng độ dài” <b>không</b> suy ra “bằng nhau”. Hai vectơ có thể cùng độ dài mà ngược '
        'hướng, hoặc không cùng phương.',
        'Đừng nhầm độ dài vectơ |→AB| với vectơ →AB: một cái là <b>số</b>, một cái là '
        '<b>đoạn thẳng có hướng</b>.',
        'Đừng nhầm →AB và →BA: chúng cùng độ dài, cùng phương nhưng ngược hướng, tức là đối nhau '
        'chứ không bằng nhau.'],
        'Bốn cái bẫy')

    e += [H3('e) Dạng toán thường gặp')]
    e += [P('<b>Dạng 1. Nhận dạng khái niệm.</b> Đọc từng khẳng định, kiểm tra điều kiện “cùng '
            'hướng” và điều kiện “cùng độ dài” một cách tách bạch. Nếu một khẳng định chỉ kiểm tra '
            'được một điều kiện thì nó thường sai.')]
    e += [P('<b>Dạng 2. Xác định vectơ từ hình cho trước.</b> Với hình bình hành ABCD: '
            '→AB = →DC (cùng hướng, cùng độ dài — đối cạnh thứ nhất), →AD = →BC (đối cạnh thứ hai), '
            '→AB và →CD đối nhau, →BC và →CB đối nhau.')]
    e += [P('<b>Dạng 3. Chứng minh hai vectơ bằng nhau.</b> Chỉ ra tứ giác tạo bởi bốn điểm là '
            'hình bình hành (hoặc trung điểm chung, hoặc phép tịnh tiến), rồi suy ra cặp cạnh đối '
            'song song và bằng nhau, kết hợp đúng chiều mũi tên.')]
    e += [Spacer(1, 2)]

    e += BOX('method', [
        '<b>Ví dụ mẫu.</b> Cho hình bình hành ABCD tâm O. Xác định các vectơ bằng →AB, các vectơ '
        'đối của →OA, và các cặp vectơ cùng phương với →AB.',
        '<b>Giải.</b> Vì ABCD là hình bình hành nên AB song song và bằng DC, và mũi tên A→B cùng '
        'chiều với D→C, do đó →AB = →DC. Các vectơ bằng →AB chỉ có →DC.',
        'Vectơ đối của →OA là →AO (cùng độ dài, ngược hướng). Ngoài ra vì O là trung điểm AC nên '
        '→OA và →OC cũng đối nhau.',
        'Các vectơ cùng phương với →AB gồm →AB, →BA, →DC, →CD (giá là đường thẳng AB); nếu kể cả '
        'vectơ – không thì thêm →0 (quy ước cùng phương với mọi vectơ).'], 'Lời giải mẫu')

    e += PRACTICE([
        'Cho hình vuông ABCD tâm O. Kể tên các vectơ (khác →0) có điểm đầu và điểm cuối là các '
        'điểm A, B, C, D, O. Có tất cả bao nhiêu vectơ như vậy?',
        'Cho ba điểm A, B, C phân biệt và thẳng hàng. Có bao nhiêu vectơ khác →0 có điểm đầu và '
        'điểm cuối thuộc tập {A, B, C}?',
        'Cho tứ giác ABCD có →AB = →DC. Tứ giác ABCD là hình gì? Vì sao?',
        'Cho tam giác đều ABC cạnh a. Tính |→AB|, |→BC|, |→AC| và chỉ ra một cặp vectơ đối nhau.',
    ], '1) Với 5 điểm phân biệt, số vectơ khác →0 là 5·4 = 20. '
       '2) 3·2 = 6 vectơ: →AB, →BA, →AC, →CA, →BC, →CB. '
       '3) ABCD là hình bình hành: →AB = →DC nghĩa là AB song song, bằng DC và cùng chiều, nên '
       'AB // DC và AB = DC — đúng dấu hiệu nhận biết hình bình hành. '
       '4) Cả ba độ dài đều bằng a; cặp vectơ đối nhau: →AB và →BA (hoặc →BC và →CB, →CA và →AC).')
    return e
