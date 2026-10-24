# -*- coding: utf-8 -*-
"""Phần mở đầu: bìa, mục lục, hướng dẫn sử dụng, cấu trúc đề, bảng ma trận."""
from reportlab.lib.units import mm
from reportlab.platypus import NextPageTemplate, PageBreak, Paragraph, Spacer

from design import (AMBER, AMBER_LIGHT, BOX, BOX_STYLE, BULL, CREAM, FRAME_W,
                    GREEN, GREY, GREY_LIGHT, H1, H2, H3, INK, LINE, NAVY, NUM,
                    P, PLUM, RULE, S, TBL, TEAL, TEAL_LIGHT, Heading, flatten, PS)

W = FRAME_W


def cover():
    return [NextPageTemplate('Body'), PageBreak()]


def toc_page(toc):
    out = [Paragraph('Mục lục', S['h2']),
           Spacer(1, 3)]
    story = out + [toc, PageBreak()]
    return story


# --------------------------------------------------------------------------
def how_to_use():
    e = []
    e += [H1('A', 'Cách dùng đề cương này', 'Hướng dẫn')]
    e += [P('Tài liệu được biên soạn theo đúng <b>ma trận đề và bảng đặc tả</b> của Tổ Toán – Tin, '
            'Trường THPT Hà Huy Tập cho kì kiểm tra giữa học kì I năm học 2026–2027. Mọi câu hỏi '
            'trong đề đều bám sát một đơn vị kiến thức và một mức độ nhận thức xác định, nên bạn '
            'có thể dùng tài liệu theo hai cách: <b>học theo chương</b> (Phần 1) hoặc '
            '<b>luyện theo đề</b> (Phần 2 – 3).', 'lead')]

    e += [H2('Bốn phần của tài liệu')]
    e += [TBL(
        ['Phần', 'Nội dung', 'Bạn nên dùng khi nào'],
        [['<b>1</b>', 'Hệ thống lý thuyết 4 chương: định nghĩa, công thức, các dạng toán, '
                      'ví dụ mẫu có lời giải, lỗi thường gặp.',
          'Đang học bài mới hoặc cần lấp lỗ hổng kiến thức.'],
         ['<b>2</b>', 'Đề kiểm tra hoàn chỉnh 21 câu, đúng cấu trúc 4 phần, đúng thang điểm 10.',
          'Khi đã học xong, làm bài trong 90 phút liên tục.'],
         ['<b>3</b>', 'Đáp án và lời giải chi tiết từng câu, từng ý đúng/sai.',
          'Sau khi làm xong đề, để tự chấm và hiểu vì sao sai.'],
         ['<b>4</b>', 'Bảng đáp án nhanh, thang điểm, bảng chẩn đoán lỗi, lộ trình ôn 7 ngày, '
                      'phiếu công thức.',
          'Trước ngày thi 1 tuần và trong buổi cuối cùng.']],
        widths=[0.9, 4.4, 3.2], align=['c', None, None])]
    e += [Spacer(1, 6)]

    e += [H2('Quy ước kí hiệu và nhãn mức độ')]
    e += [BULL([
        '<b>→AB</b> là kí hiệu vectơ có điểm đầu A, điểm góc cuối B (trong vở, bạn viết có mũi tên '
        'trên đầu). <b>|→AB|</b> là độ dài vectơ, tức đoạn thẳng AB.',
        '<b>[NB]</b> Nhận biết – câu hỏi kiểm tra định nghĩa, kí hiệu, nhận dạng. Thường chỉ cần '
        'một bước suy luận.',
        '<b>[TH]</b> Thông hiểu – câu hỏi yêu cầu hiểu bản chất và áp dụng trực tiếp một công thức.',
        '<b>[VD]</b> Vận dụng – phải phối hợp 2–3 bước, thường gắn với tình huống thực tế đơn giản.',
        '<b>[VDC]</b> Vận dụng cao – bài toán tối ưu, phải lập mô hình rồi kết luận.',
        'Mọi kết quả số được làm tròn theo yêu cầu ghi trong câu; nếu không ghi, giữ nguyên '
        'dạng chính xác (căn thức hoặc phân số).',
    ])]

    e += BOX('tip', [
        'Đừng đọc lời giải trước khi làm bài. Sai lầm phổ biến nhất của học sinh khi ôn thi là '
        'đọc lời giải và thấy “hiểu rồi”, nhưng khi vào phòng thi lại không tự tạo ra được bước '
        'đầu tiên. Hãy làm bài bằng giấy, bấm giờ, rồi mới mở Phần 3.'])

    e += [Spacer(1, 2), H2('Cách tính điểm bài kiểm tra')]
    e += [P('Bài kiểm tra gồm 4 phần với tổng 10 điểm. Trong phần trắc nghiệm đúng/sai, điểm của '
            'mỗi câu phụ thuộc số ý đúng, theo đúng quy chế của đề:')]
    e += [TBL(['Số ý đúng trong một câu', '1 ý', '2 ý', '3 ý', '4 ý'],
              [['Điểm được tính', '0,10', '0,25', '0,50', '1,00']],
              widths=[2.6, 1, 1, 1, 1],
              align=[None, 'c', 'c', 'c', 'c'])]
    e += [Spacer(1, 3), P('<i>Hệ quả cần nhớ:</i> một câu đúng/sai 4 ý có giá trị bằng bốn câu '
                          'trắc nghiệm. Nếu bạn chắc chắn 2 ý và chỉ dám khoanh “đúng” cho cả 4 ý, '
                          'bạn có thể mất gần 1 điểm. Hãy phán đoán từng ý độc lập.', 'small')]
    return e


# --------------------------------------------------------------------------
def exam_structure():
    e = []
    e += [H1('B', 'Cấu trúc đề và phân bố điểm', 'Bản đồ đề thi')]
    e += [P('Bảng dưới đây tái hiện đúng phần <b>Hình thức</b> và <b>Ma trận</b> của đề gốc, '
            'kèm cột chỉ rõ câu nào trong đề ở Phần 2 ứng với dòng nào của ma trận.', 'lead')]

    e += [H2('B.1. Bốn phần của đề')]
    e += [TBL(['Phần', 'Dạng câu hỏi', 'Số câu', 'Điểm', 'Câu trong tài liệu'],
              [['I', 'Trắc nghiệm nhiều phương án lựa chọn', '12', '3,0', 'Câu 1 – 12'],
               ['II', 'Trắc nghiệm đúng / sai (4 ý mỗi câu)', '2', '2,0', 'Câu 13 – 14'],
               ['III', 'Trắc nghiệm trả lời ngắn', '4', '2,0', 'Câu 15 – 18'],
               ['IV', 'Tự luận', '3', '3,0', 'Câu 19 – 21'],
               ['<b>Tổng</b>', 'Thời gian: 90 phút', '<b>21</b>', '<b>10,0</b>', '']],
              widths=[0.7, 4.2, 0.9, 0.8, 1.9],
              align=['c', None, 'c', 'c', 'c'])]
    e += [Spacer(1, 6)]

    e += [H2('B.2. Ma trận phân bố câu hỏi theo chương')]
    e += [TBL(['Chương', 'Đơn vị kiến thức', 'TN', 'ĐS', 'TLN', 'TL', 'Điểm'],
              [['<b>1</b>', '1.1. Mệnh đề', '2', '–', '–', '–', '0,50'],
               ['', '1.2. Tập hợp', '1', '1a–b', '1', '–', '1,25'],
               ['', '1.3. Các phép toán trên tập hợp', '1', '1c–d', '1', '19', '2,25'],
               ['<b>2</b>', '2.1. Bất phương trình bậc nhất hai ẩn', '1', '2a–c', '–', '–', '1,00'],
               ['', '2.2. Hệ bất phương trình bậc nhất hai ẩn', '1', '2d', '–', '21', '1,50'],
               ['<b>3</b>', '3.1. Giá trị lượng giác của góc 0° – 180°', '2', '–', '3', '–', '1,00'],
               ['', '3.2. Hệ thức lượng trong tam giác', '2', '–', '4', '20', '2,00'],
               ['<b>4</b>', '4.1. Khái niệm vectơ', '2', '–', '–', '–', '0,50'],
               ['<b>Tổng</b>', '24 lượt câu hỏi trên 21 câu', '12', '2', '4', '3', '<b>10,0</b>']],
              widths=[1.0, 4.1, 0.6, 0.9, 0.7, 0.7, 0.8],
              align=['c', None, 'c', 'c', 'c', 'c', 'c'])]
    e += [Spacer(1, 3), P('Ghi chú: <b>TN</b> = trắc nghiệm chọn phương án, <b>ĐS</b> = đúng/sai, '
                          '<b>TLN</b> = trả lời ngắn, <b>TL</b> = tự luận. Hai câu đúng/sai được '
                          'tính theo từng ý nên một câu có thể xuất hiện ở hai đơn vị kiến thức; '
                          'con số “24 lượt” là tổng số ý/câu con, không phải số câu.', 'small')]
    e += [Spacer(1, 6)]

    e += [H2('B.3. Bản đồ câu hỏi → mức độ nhận thức')]
    e += [TBL(['Mức độ', 'Câu hỏi trong đề', 'Số điểm', 'Nhận xét chiến lược'],
              [['Nhận biết', '1–7, 9, 11 (trắc nghiệm); 13a; 14a–b', '3,00',
                'Chiếm gần một phần ba số điểm và là phần “phải lấy trọn” — mất điểm ở đây là '
                'mất điểm dễ nhất.'],
               ['Thông hiểu', '8, 10, 12; 13b–c; 14c; 15; 17; 18', '3,00',
                'Đòi hỏi thuộc công thức và thay số chính xác; cần luyện tốc độ.'],
               ['Vận dụng', '13d; 14d; 16; 19; 20', '3,00',
                'Bài toán thực tế và hai câu tự luận; điểm nằm ở các bước trình bày.'],
               ['Vận dụng cao', '21', '1,00',
                'Bài toán tối ưu hệ bất phương trình; hầu như luôn là câu phân loại.']],
              widths=[1.1, 3.2, 0.8, 4.0])]
    e += [Spacer(1, 4)]

    e += BOX('note', [
        'Cấu trúc này giải thích vì sao <b>không được bỏ chương nào</b>. Chương 1 chiếm 4 điểm, '
        'chương 3 chiếm 3,0 điểm, chương 2 chiếm 2,5 điểm và chương 4 chỉ 0,5 điểm nhưng lại là '
        'phần dễ lấy điểm nhất. Chiến lược hợp lí: giữ chắc chương 1 và 4, luyện kĩ chương 3, '
        'dành thời gian cuối cho bài tối ưu ở chương 2.'])
    e += [Spacer(1, 4), H2('B.4. Năm sai lầm tốn điểm nhất, theo thứ tự tần suất')]
    e += [P('Danh sách dưới đây được rút ra từ chính cấu trúc của đề: mỗi lỗi đều gắn với một '
            'dạng câu cụ thể, nên bạn có thể kiểm tra lại ngay sau khi làm xong đề ở Phần 2.')]
    e += [TBL(['#', 'Sai lầm', 'Câu dễ mắc', 'Cách phòng tránh'],
              [['1', 'Lấy sai đầu mút khi tìm giao, hợp, hiệu các khoảng',
                '4, 15, 19', 'Hỏi lại với từng đầu mút: điểm đó có thuộc tập không?'],
               ['2', 'Bỏ qua điều kiện của góc khi tính giá trị lượng giác',
                '8, 17', 'Viết điều kiện góc ra giấy trước khi chọn dấu.'],
               ['3', 'Quên điều kiện x ≥ 0, y ≥ 0 trong bài toán tối ưu',
                '21', 'Bắt đầu mọi lời giải bằng câu “gọi x, y là … (x ≥ 0, y ≥ 0)”.'],
               ['4', 'Không thử đủ các đỉnh của miền nghiệm',
                '21', 'Kẻ bảng giá trị F tại <i>tất cả</i> các đỉnh rồi mới kết luận.'],
               ['5', 'Nhầm “cùng phương” với “cùng hướng”',
                '11, 12', 'Vẽ hình và đánh mũi tên trước khi so sánh hai vectơ.']],
              widths=[0.5, 3.0, 1.3, 3.4], align=['c', None, 'c', None])]
    e += [Spacer(1, 6)]


    e += [Spacer(1, 6), H2('B.5. Đối chiếu với sách giáo khoa Kết nối tri thức')]
    e += [P('Ma trận của trường chỉ ghi tên đơn vị kiến thức, không ghi số bài. Bảng dưới đây đối '
            'chiếu từng đơn vị kiến thức với bài học tương ứng trong sách Kết nối tri thức – '
            'Toán 10, tập 1, để bạn tra cứu nhanh khi cần đọc lại lí thuyết gốc.')]
    e += [TBL(['Đơn vị kiến thức', 'Bài trong sách KNTT', 'Câu trong đề'],
              [['1.1. Mệnh đề', 'Bài 1. Mệnh đề', '1, 2'],
               ['1.2. Tập hợp', 'Bài 2. Tập hợp và các phép toán trên tập hợp (phần 1)', '3, 13a, 15'],
               ['1.3. Các phép toán trên tập hợp',
                'Bài 2. Tập hợp và các phép toán trên tập hợp (phần 2)', '4, 13b–d, 16, 19'],
               ['2.1. Bất phương trình bậc nhất hai ẩn',
                'Bài 3. Bất phương trình bậc nhất hai ẩn', '5, 14'],
               ['2.2. Hệ bất phương trình bậc nhất hai ẩn',
                'Bài 4. Hệ bất phương trình bậc nhất hai ẩn', '6, 21'],
               ['3.1. Giá trị lượng giác của góc 0° – 180°',
                'Bài 5. Giá trị lượng giác của một góc từ 0° đến 180°', '7, 8, 17'],
               ['3.2. Hệ thức lượng trong tam giác', 'Bài 6. Hệ thức lượng trong tam giác',
                '9, 10, 18, 20'],
               ['4.1. Khái niệm vectơ', 'Bài 7. Các khái niệm mở đầu (về vectơ)', '11, 12']],
              widths=[2.5, 4.0, 1.6])]
    e += [Spacer(1, 6)]

    e += [H2('B.6. Những nội dung nằm ngoài phạm vi kiểm tra')]
    e += [P('Biết rõ phần nào <b>không</b> thi cũng quan trọng như biết phần nào thi: nó giúp bạn '
            'không mất thời gian vào những bài sẽ không xuất hiện. Theo ma trận, các nội dung sau '
            'thuộc chương trình học kì I nhưng <b>không</b> có trong đề giữa kì:')]
    e += [BULL([
        'Tổng và hiệu của hai vectơ, tích của một vectơ với một số (Bài 8, 9) — chỉ thi học kì.',
        'Vectơ trong mặt phẳng tọa độ và tích vô hướng của hai vectơ (Bài 10, 11).',
        'Bất phương trình bậc hai một ẩn và ứng dụng của hệ bất phương trình trong quy hoạch '
        'tuyến tính ở mức nâng cao hơn.',
        'Các bài toán chứng minh bất đẳng thức, tìm giá trị lớn nhất – nhỏ nhất bằng đại số.',
    ])]
    e += BOX('tip', [
        'Nếu bạn đang ôn muộn: bỏ qua hoàn toàn Bài 8 – 11 ở chương 4, chỉ học Bài 7. Đây là '
        'khoản tiết kiệm thời gian lớn nhất trong toàn bộ kế hoạch ôn tập, vì chương 4 chỉ chiếm '
        '0,5 điểm và phần được thi nằm gọn trong một bài.'])

    e += [Spacer(1, 8), H2('B.7. Ghi chú về cách biên soạn đề ở Phần 2')]
    e += [P('Tài liệu gốc “MA TRẬN ĐỀ KIỂM TRA GIỮA KÌ I NĂM HỌC 2026-2027 – MÔN TOÁN, LỚP 10” '
            'gồm phần mục tiêu, hình thức, ma trận phân bố câu hỏi và bảng đặc tả mức độ nhận '
            'thức. Văn bản này <b>không</b> chứa đề bài cụ thể: bảng đặc tả chỉ mô tả yêu cầu cần '
            'kiểm tra của từng câu (ví dụ “Câu 3: biết cho tập hợp bằng cách liệt kê…”).')]
    e += [P('Vì vậy đề ở Phần 2 được biên soạn lại đúng theo bảng đặc tả đó: mỗi câu giữ nguyên '
            'vị trí, đơn vị kiến thức và mức độ nhận thức mà ma trận quy định, chỉ thay phần nội '
            'dung số cụ thể. Nhờ vậy cấu trúc, thang điểm và độ khó của đề vẫn trùng khớp với đề '
            'chính thức, còn nội dung thì luôn có sẵn để luyện tập.')]
    e += BOX('note', [
        '<b>Đối chiếu nhanh:</b> mỗi câu trong đề đều có nhãn [NB], [TH], [VD], [VDC] và tên đơn '
        'vị kiến thức in bên cạnh. Bạn có thể so trực tiếp với cột “Đơn vị kiến thức” và “Mức độ” '
        'trong bảng B.2, B.3 để thấy đề bám ma trận đến mức nào.',
        '<b>Về điểm số:</b> tổng điểm của 21 câu là 10,0; 12 câu trắc nghiệm × 0,25 = 3,0; '
        '2 câu đúng/sai × 1,0 = 2,0; 4 câu trả lời ngắn × 0,5 = 2,0; 3 câu tự luận × 1,0 = 3,0.'],
        'Minh bạch nguồn')
    return e
