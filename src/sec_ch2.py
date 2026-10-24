# -*- coding: utf-8 -*-
"""Chương 2 – Bất phương trình và hệ bất phương trình bậc nhất hai ẩn."""
from reportlab.platypus import Paragraph, Spacer

from design import BOX, BULL, EQ, H1, H2, H3, NUM, P, PRACTICE, Spacer, TBL
from figures import FeasibleRegion


def chapter():
    e = []
    e += H1('2', 'Bất phương trình và hệ bất phương trình\nbậc nhất hai ẩn', 'Chương 2  ·  2,50 điểm')
    e += [P('Chương này chỉ có 2,5 điểm nhưng chứa <b>câu phân loại duy nhất</b> của đề (câu 21, '
            '1 điểm). Phần nhận biết – thông hiểu khá dễ, cái khó nằm ở bước chuyển một tình '
            'huống thực tế thành hệ bất phương trình và ở bước kết luận phương án tối ưu.', 'lead')]

    # ======================================================================
    e += [H2('2.1. Bất phương trình bậc nhất hai ẩn')]

    e += [H3('a) Định nghĩa và nghiệm')]
    e += [P('<b>Bất phương trình bậc nhất hai ẩn</b> x, y có dạng tổng quát:')]
    e += EQ('ax + by ≤ c,   ax + by ≥ c,   ax + by &lt; c,   ax + by &gt; c')
    e += [P('trong đó a, b, c là các số thực đã cho, <b>a và b không đồng thời bằng 0</b>, x và y '
            'là hai ẩn.')]
    e += [P('Mỗi cặp số (x₀; y₀) thỏa mãn bất phương trình được gọi là một <b>nghiệm</b>. Tập hợp '
            'tất cả các điểm có tọa độ là nghiệm gọi là <b>miền nghiệm</b> của bất phương trình.')]
    e += [Spacer(1, 2)]

    e += BOX('warn', [
        'Điều kiện “a và b không đồng thời bằng 0” chính là cái để loại phương án trong câu 5. '
        'Ví dụ 0·x + 0·y ≤ 3 không phải bất phương trình bậc nhất hai ẩn.',
        'Bất phương trình <b>không</b> phải bậc nhất hai ẩn khi: có x², y²; có xy; có 1/x, 1/y; '
        'có √x, sin y, …; hoặc hệ số của cả x và y đều bằng 0.'],
        'Nhận diện nhanh')

    e += [H3('b) Quy tắc biểu diễn miền nghiệm')]
    e += [NUM([
        '<b>Vẽ đường thẳng</b> Δ: ax + by = c (đường thẳng này gọi là <b>đường biên</b>). Cách '
        'nhanh: cho x = 0 tìm y, cho y = 0 tìm x, nối hai điểm.',
        '<b>Chọn nét vẽ:</b> nếu bất phương trình có dấu ≤ hoặc ≥ thì vẽ nét <b>liền</b> (miền '
        'nghiệm kể cả bờ); nếu có dấu &lt; hoặc &gt; thì vẽ nét <b>đứt</b> (không kể bờ).',
        '<b>Chọn một điểm thử</b> M không nằm trên Δ — thường chọn gốc tọa độ O(0; 0).',
        '<b>Thay M vào bất phương trình.</b> Nếu được mệnh đề đúng thì miền nghiệm là nửa mặt '
        'phẳng <b>chứa</b> M; nếu sai thì là nửa mặt phẳng <b>không chứa</b> M.',
        '<b>Kết luận:</b> miền nghiệm là nửa mặt phẳng (kể cả hoặc không kể bờ theo bước 2).',
    ])]

    e += BOX('method', [
        '<b>Ví dụ mẫu.</b> Biểu diễn miền nghiệm của bất phương trình 2x + y ≤ 4.',
        '<b>Bước 1.</b> Vẽ đường thẳng 2x + y = 4. Cho x = 0 được y = 4 → điểm A(0; 4); cho y = 0 '
        'được x = 2 → điểm B(2; 0). Nối A, B ta được đường biên.',
        '<b>Bước 2.</b> Dấu ≤ nên vẽ nét <b>liền</b>.',
        '<b>Bước 3.</b> Thử O(0; 0): 2·0 + 0 = 0 ≤ 4, mệnh đề <b>đúng</b>.',
        '<b>Bước 4.</b> Miền nghiệm là nửa mặt phẳng bờ AB <b>chứa gốc O</b>, kể cả bờ — tức miền '
        'nằm về phía gốc tọa độ, phía dưới đường thẳng.'], 'Lời giải mẫu')

    e += BOX('warn', [
        'Không được chọn điểm thử nằm <b>trên</b> đường biên: khi đó hai vế bằng nhau và bạn '
        'không phân biệt được nửa mặt phẳng nào.',
        'Nếu đường biên đi qua gốc O thì phải chọn điểm khác, ví dụ M(1; 0) hoặc M(0; 1).',
        'Kết luận phải nói rõ “kể cả bờ” hay “không kể bờ”, nếu không sẽ mất điểm trình bày.'],
        'Ba lỗi hay mắc')

    # ======================================================================
    e += [H2('2.2. Hệ bất phương trình bậc nhất hai ẩn')]

    e += [H3('a) Khái niệm')]
    e += [P('Hệ bất phương trình bậc nhất hai ẩn là một hệ gồm <b>hai hay nhiều</b> bất phương '
            'trình bậc nhất hai ẩn x, y. Nghiệm của hệ là cặp số (x₀; y₀) đồng thời là nghiệm của '
            '<b>mọi</b> bất phương trình trong hệ; miền nghiệm của hệ là giao các miền nghiệm của '
            'các bất phương trình đó.')]
    e += [P('Vì là giao của các nửa mặt phẳng, miền nghiệm của hệ thường là một <b>đa giác</b> '
            '(tam giác, tứ giác, ngũ giác…) — có thể kể cả biên hoặc không.')]
    e += [Spacer(1, 2)]

    e += [H3('b) Các bước biểu diễn miền nghiệm của hệ')]
    e += [NUM([
        'Với mỗi bất phương trình trong hệ, vẽ đường biên và xác định nửa mặt phẳng nghiệm.',
        'Đánh dấu (gạch chéo phần loại bỏ, hoặc tô phần giữ lại) — cách gạch bỏ thường dễ nhìn hơn.',
        'Phần còn lại <b>không bị gạch</b> là miền nghiệm của hệ.',
        'Xác định tọa độ các đỉnh của miền nghiệm bằng cách giải hệ phương trình tạo bởi hai '
        'đường biên cắt nhau.',
    ])]
    e += [Spacer(1, 2)]

    e += [FeasibleRegion(), Spacer(1, 4)]
    e += BOX('method', [
        '<b>Ví dụ mẫu.</b> Biểu diễn miền nghiệm của hệ: x ≥ 0; y ≥ 0; x + y ≤ 4; 2x + y ≤ 6.',
        '<b>Giải.</b> Hai bất phương trình x ≥ 0, y ≥ 0 cho biết miền nghiệm nằm trong góc phần tư '
        'thứ nhất. Đường x + y = 4 đi qua (4; 0), (0; 4); đường 2x + y = 6 đi qua (3; 0), (0; 6); '
        'cả hai đều lấy phía chứa gốc O. Miền nghiệm là tứ giác O(0; 0), A(3; 0), B(2; 2), '
        'C(0; 4), trong đó B là giao điểm của hai đường: giải x + y = 4 và 2x + y = 6 được x = 2, '
        'y = 2.'], 'Lời giải mẫu')

    e += [H3('c) Bài toán tối ưu (vận dụng cao)')]
    e += [P('Đây là dạng bài chắc chắn xuất hiện ở câu tự luận cuối. Bài toán luôn có dạng: tìm '
            'giá trị lớn nhất (hoặc nhỏ nhất) của biểu thức F = ax + by với (x; y) thuộc miền '
            'nghiệm của một hệ bất phương trình. Quy trình gồm <b>ba bước cố định</b>:')]
    e += [NUM([
        '<b>Đặt ẩn và lập hệ.</b> Gọi x, y là hai đại lượng cần tìm, ghi rõ đơn vị và điều kiện '
        'x ≥ 0, y ≥ 0. Mỗi điều kiện ràng buộc của đề (nguyên liệu, thời gian, vốn…) cho một bất '
        'phương trình. Viết biểu thức mục tiêu F.',
        '<b>Vẽ miền nghiệm</b> và xác định tọa độ các đỉnh của đa giác.',
        '<b>Tính F tại từng đỉnh</b> rồi so sánh. Giá trị lớn nhất (nhỏ nhất) của F trên miền '
        'nghiệm đạt được tại một trong các đỉnh.',
    ])]

    e += BOX('note', [
        '<b>Vì sao chỉ cần thử ở các đỉnh?</b> Trên mỗi cạnh của đa giác, F = ax + by là một hàm '
        'bậc nhất của một biến nên đạt giá trị lớn nhất và nhỏ nhất ở hai đầu mút, tức ở các đỉnh. '
        'Vì vậy chỉ cần thử hữu hạn đỉnh là đủ. Đây là lí do ta không cần khảo sát cả miền.'],
        'Cơ sở toán học')

    e += BOX('method', [
        '<b>Ví dụ mẫu.</b> Một xưởng làm hai loại bánh. Mỗi chiếc bánh loại I cần 0,2 kg bột và '
        '0,1 kg đường; mỗi chiếc loại II cần 0,1 kg bột và 0,2 kg đường. Xưởng có 20 kg bột và '
        '16 kg đường. Tiền lãi mỗi chiếc loại I là 8 nghìn đồng, loại II là 6 nghìn đồng. Hỏi cần '
        'làm bao nhiêu chiếc mỗi loại để lãi lớn nhất?',
        '<b>Bước 1.</b> Gọi x, y lần lượt là số bánh loại I, loại II (x ≥ 0, y ≥ 0). Ràng buộc bột: '
        '0,2x + 0,1y ≤ 20, tức 2x + y ≤ 200. Ràng buộc đường: 0,1x + 0,2y ≤ 16, tức x + 2y ≤ 160. '
        'Hàm mục tiêu F = 8x + 6y (nghìn đồng).',
        '<b>Bước 2.</b> Miền nghiệm là tứ giác O(0; 0), A(100; 0), B(80; 40), C(0; 80). Đỉnh B là '
        'giao của 2x + y = 200 và x + 2y = 160: nhân phương trình thứ hai với 2 được 2x + 4y = 320, '
        'trừ đi được 3y = 120 → y = 40, suy ra x = 80.',
        '<b>Bước 3.</b> F(0; 0) = 0; F(100; 0) = 800; F(80; 40) = 640 + 240 = 880; '
        'F(0; 80) = 480. Vậy lãi lớn nhất là 880 nghìn đồng khi làm <b>80 bánh loại I và 40 bánh '
        'loại II</b>.'], 'Lời giải mẫu')

    e += BOX('warn', [
        'Đặt ẩn mà <b>quên điều kiện</b> x ≥ 0, y ≥ 0 là lỗi mất điểm phổ biến nhất. Số lượng '
        'không thể âm.',
        'Không được kết luận chỉ bằng một đỉnh “có vẻ lớn nhất”. Phải lập bảng giá trị tại '
        '<b>tất cả</b> các đỉnh.',
        'Sau khi giải, hãy đọc lại đề: có yêu cầu nghiệm nguyên không? có yêu cầu tính tổng tiền '
        'không? Câu kết luận phải trả lời đúng câu hỏi của đề.',
        'Nếu miền nghiệm không bị chặn (ví dụ chỉ có x ≥ 0, y ≥ 0) thì F có thể không đạt giá trị '
        'lớn nhất; đề thi giữa kì luôn cho miền bị chặn để tránh trường hợp này.'],
        'Bốn lỗi hay mắc')

    e += PRACTICE([
        'Cặp số (2; −1) có là nghiệm của bất phương trình 3x − y ≥ 5 không?',
        'Nêu cách xác định miền nghiệm của bất phương trình x − 2y &lt; 4 (chỉ rõ nét vẽ và '
        'điểm thử).',
        'Xác định tọa độ các đỉnh của miền nghiệm của hệ: x ≥ 0, y ≥ 0, x + y ≤ 6, 2x + y ≤ 8.',
        'Với miền nghiệm ở bài 3, tìm giá trị lớn nhất của F = 3x + 2y.',
        'Một xưởng may có 120 m vải. Mỗi chiếc áo cần 2 m vải, mỗi chiếc quần cần 3 m vải; '
        'xưởng chỉ nhận may tối đa 50 sản phẩm. Lãi mỗi áo là 50 nghìn đồng, mỗi quần là 80 '
        'nghìn đồng. Lập hệ bất phương trình và xác định phương án lãi lớn nhất.',
    ], '1) Có: 3·2 − (−1) = 7 ≥ 5. '
       '2) Vẽ đường thẳng x − 2y = 4 qua (4; 0) và (0; −2) bằng nét đứt; thử O(0; 0) được '
       '0 &lt; 4 (đúng) nên miền nghiệm là nửa mặt phẳng chứa O, không kể bờ. '
       '3) O(0; 0), (4; 0), (2; 4), (0; 6). '
       '4) F(0; 0) = 0; F(4; 0) = 12; F(2; 4) = 14; F(0; 6) = 12 → lớn nhất bằng 14 tại (2; 4). '
       '5) 2x + 3y ≤ 120, x + y ≤ 50, x ≥ 0, y ≥ 0, F = 50x + 80y. Các đỉnh O(0; 0), (50; 0), '
       '(30; 20), (0; 40); F lần lượt bằng 0; 2 500; 3 100; 3 200 → lãi lớn nhất 3 200 nghìn '
       'đồng khi may 40 quần và không may áo.')
    return e
