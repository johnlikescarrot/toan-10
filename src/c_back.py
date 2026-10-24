# -*- coding: utf-8 -*-
"""PHẦN IV – Ma trận, đặc tả tóm tắt, phân tích và kế hoạch ôn tập."""
from kit import *
from kit import _p


def matrix():
    s = []
    s += h1("07", "MA TRẬN, ĐẶC TẢ VÀ KẾ HOẠCH ÔN TẬP",
            "Số hoá lại văn bản gốc của Tổ Toán – Tin thành các bảng dùng được khi ôn thi")

    s.append(h2("7.1. Hình thức và cấu trúc đề kiểm tra"))
    s.append(data_table([
        ["Phần", "Số câu", "Điểm", "Ghi chú về cách tính điểm"],
        ["Trắc nghiệm nhiều phương án lựa chọn", "12", "3,0", "mỗi câu đúng 0,25 điểm"],
        ["Trắc nghiệm đúng – sai", "2", "2,0", "đúng 1 ý 0,1 – đúng 2 ý 0,25 – đúng 3 ý 0,5 – đúng 4 ý 1,0"],
        ["Trắc nghiệm trả lời ngắn", "4", "2,0", "mỗi câu 0,5 điểm, chỉ ghi kết quả"],
        ["Tự luận", "3", "3,0", "mỗi câu 1,0 điểm, trình bày đầy đủ các bước"],
        ["<b>Tổng</b>", "<b>24 câu</b>", "<b>10,0</b>", "thời gian làm bài 90 phút"],
    ], widths=[66 * mm, 22 * mm, 18 * mm, None], align_center=False))

    s.append(h2("7.2. Ma trận theo nội dung kiến thức"))
    s.append(P("Bảng dưới đây tóm tắt ma trận của đề kiểm tra (số câu và điểm theo từng đơn vị kiến thức). "
               "Cột “TN” gộp cả ba hình thức trắc nghiệm, trong đó hai câu đúng–sai (mỗi câu 4 ý) nằm ở mục 1.2–1.3 và 2.1."))
    rows = [["TT", "Nội dung", "Đơn vị kiến thức", "TN (câu)", "Tự luận (câu)", "Điểm TN", "Điểm TL"],
            ["1", "Mệnh đề. Tập hợp.", "1.1. Mệnh đề", "2", "–", "0,50", "–"],
            ["", "", "1.2. Tập hợp", "4 (có 1 câu ĐS)", "–", "1,25", "–"],
            ["", "", "1.3. Các phép toán trên tập hợp", "4 (có 1 câu ĐS)", "1", "1,25", "1,00"],
            ["2", "Bất phương trình và hệ bất phương trình bậc nhất hai ẩn",
             "2.1. Bất phương trình bậc nhất hai ẩn", "5 (có 1 câu ĐS)", "–", "1,25", "–"],
            ["", "", "2.2. Hệ bất phương trình bậc nhất hai ẩn", "1", "1", "0,25", "1,00"],
            ["3", "Hệ thức lượng trong tam giác",
             "3.1. Giá trị lượng giác của một góc từ $0°$ đến $180°$", "3", "–", "1,00", "–"],
            ["", "", "3.2. Hệ thức lượng trong tam giác", "3", "1", "1,00", "1,00"],
            ["4", "Vectơ", "4.1. Khái niệm vectơ", "2", "–", "0,50", "–"],
            ["<b>Tổng</b>", "", "", "<b>24</b>", "<b>3</b>", "<b>7,00</b>", "<b>3,00</b>"]]
    s.append(data_table(rows, widths=[12 * mm, 46 * mm, None, 22 * mm, 20 * mm, 17 * mm, 17 * mm],
                        align_center=True))

    s.append(h2("7.3. Bảng đặc tả tóm tắt: mỗi đơn vị kiến thức cần đạt gì?"))
    rows = [["Đơn vị kiến thức", "Mức độ", "Yêu cầu cần đạt (theo đặc tả)", "Câu trong đề mẫu"],
            ["1.1. Mệnh đề", "NB",
             "Biết thế nào là mệnh đề, mệnh đề phủ định, mệnh đề chứa biến; biết ý nghĩa kí hiệu $∀$, $∃$", "Câu 1, 2"],
            ["1.2. Tập hợp", "NB",
             "Cho tập hợp bằng cách liệt kê hoặc chỉ ra tính chất đặc trưng; dùng đúng các kí hiệu $∈, ∉, ⊂, ⊄, ∅$; "
             "dùng đúng các kí hiệu khoảng, đoạn, nửa khoảng", "Câu 3; câu 13a"],
            ["1.2. Tập hợp", "TH – VD",
             "Biểu diễn khoảng, đoạn trên trục số; lấy ví dụ về tập con, hai tập hợp bằng nhau; **tìm số tập con** "
             "của một tập hợp hữu hạn", "Câu 13b–d"],
            ["1.3. Các phép toán trên tập hợp", "NB – TH",
             "Dùng biểu đồ Ven biểu diễn giao, hợp; thực hiện được phép giao, hợp, phần bù của một tập con", "Câu 4"],
            ["1.3. Các phép toán trên tập hợp", "TH – VD",
             "Vận dụng các phép toán tập hợp vào bài toán thực tế (đếm số phần tử)", "Câu 19"],
            ["2.1. Bất phương trình bậc nhất hai ẩn", "NB",
             "Nhận biết bất phương trình bậc nhất hai ẩn; nhận biết nghiệm và miền nghiệm", "Câu 5; câu 14a"],
            ["2.1. Bất phương trình bậc nhất hai ẩn", "TH – VD",
             "Mô tả miền nghiệm trên mặt phẳng toạ độ; chuyển điều kiện thực tế về bất phương trình bậc nhất hai ẩn",
             "Câu 5, 6; câu 14b–d"],
            ["2.2. Hệ bất phương trình bậc nhất hai ẩn", "NB – VDC",
             "Nhận biết hệ bất phương trình bậc nhất hai ẩn; mô tả miền nghiệm; **tìm phương án tối ưu**", "Câu 6; câu 21"],
            ["3.1. Giá trị lượng giác $0°$–$180°$", "NB – VD",
             "Nhận biết giá trị lượng giác của một góc; hệ thức giữa hai góc phụ nhau, bù nhau; tính bằng máy tính; "
             "tính giá trị lượng giác khi biết một giá trị lượng giác của góc", "Câu 7, 8; câu 15"],
            ["3.2. Hệ thức lượng trong tam giác", "NB – VD",
             "Nhận biết định lí côsin, định lí sin, công thức diện tích; tính cạnh, góc, diện tích; "
             "giải bài toán thực tiễn (khoảng cách, chiều cao)", "Câu 9, 10; câu 16; câu 20"],
            ["4.1. Khái niệm vectơ", "NB – TH",
             "Biết khái niệm vectơ, vectơ – không, độ dài, cùng phương, cùng hướng, bằng nhau; chứng minh hai vectơ "
             "bằng nhau trong trường hợp đơn giản", "Câu 11, 12"]]
    s.append(data_table(rows, widths=[44 * mm, 20 * mm, None, 26 * mm], align_center=False))
    s.extend(box(["**Phân bố mức độ (theo đặc tả):** Nhận biết ≈ 40% – Thông hiểu ≈ 30% – Vận dụng ≈ 20% – "
                  "Vận dụng cao ≈ 10%. Nghĩa là **7 điểm đầu tiên** thuộc về phần hiểu và nhớ định nghĩa, công thức. "
                  "Đừng dồn sức cho câu khó khi còn để mất điểm ở phần nhận biết."],
                 kind="box_warn", title="Nhận xét quan trọng"))

    s.append(h2("7.4. Đối chiếu đề tham khảo với ma trận"))
    from c_exam import exam_matrix
    s.extend(exam_matrix())

    s.append(h2("7.5. Kế hoạch ôn tập 7 ngày"))
    rows = [["Ngày", "Nội dung", "Việc cần làm", "Thời gian"],
            ["1", "Mệnh đề (mục 1.1)", "Học định nghĩa; lập bảng phủ định của $∀$, $∃$; làm câu 1, 2 + 10 ví dụ tự đặt", "60–75 phút"],
            ["2", "Tập hợp và các phép toán (1.2, 1.3)", "Vẽ trục số cho ít nhất 8 khoảng/đoạn; làm câu 3, 4, câu 13, câu 19", "75 phút"],
            ["3", "Bất phương trình bậc nhất hai ẩn (2.1)", "Luyện 5 bài vẽ miền nghiệm; học thuộc 3 bước; làm câu 5, câu 14", "75 phút"],
            ["4", "Hệ bất phương trình – bài toán tối ưu (2.2)", "Làm lại ví dụ trong tài liệu; giải 3 bài tối ưu tương tự; làm câu 6, câu 21", "90 phút"],
            ["5", "Giá trị lượng giác (3.1)", "Học bảng giá trị đặc biệt; luyện dạng “cho một giá trị, tính biểu thức”; làm câu 7, 8, câu 15", "75 phút"],
            ["6", "Hệ thức lượng trong tam giác (3.2)", "Viết lại 5 công thức diện tích; luyện 3 bài toán thực tiễn; làm câu 9, 10, câu 16, câu 20", "90 phút"],
            ["7", "Vectơ (4.1) + tổng ôn", "Ôn khái niệm vectơ; **làm trọn đề Phần II trong 90 phút**, chấm và chữa theo Phần III", "90 + 60 phút"]]
    s.append(data_table(rows, widths=[12 * mm, 45 * mm, None, 24 * mm], align_center=False))

    s.append(h2("7.6. Chiến lược làm bài trong 90 phút"))
    s.extend(steps([
        "**0–5 phút:** đọc lướt toàn đề, đánh dấu câu quen thuộc. Ghi ngay đáp án những câu chắc chắn vào phiếu.",
        "**5–35 phút:** làm 12 câu trắc nghiệm chọn đáp án. Mục tiêu 3 điểm tuyệt đối – đây là phần dễ lấy điểm nhất.",
        "**35–55 phút:** làm 2 câu đúng–sai và 4 câu trả lời ngắn. Với câu đúng–sai, xét từng ý độc lập, "
        "đừng suy diễn “ý a đúng nên ý b sai”.",
        "**55–85 phút:** làm 3 câu tự luận theo thứ tự dễ → khó (câu 19 → câu 20 → câu 21). Trình bày từng bước, ghi kết luận.",
        "**85–90 phút:** rà lại phiếu trả lời, kiểm tra đơn vị, dấu của giá trị lượng giác và các đầu mút của khoảng.",
    ]))
    s.extend(box(["**Ba lỗi mất điểm nhiều nhất** (rút ra từ chính đặc tả của đề):",
                  "1. Quên **đổi dấu** khi dùng hai góc bù nhau ($cos$, $tan$, $cot$ đổi dấu).",
                  "2. Nhầm **đầu mút** khi tìm giao/hợp/phần bù của các khoảng, đoạn.",
                  "3. Bỏ sót **đỉnh của đa giác** trong bài toán tối ưu – đặc biệt là giao điểm của hai đường biên."],
                 kind="box_warn", title="Checklist trước khi nộp bài"))

    s.append(h2("7.7. Trang công thức cần nhớ"))
    s.append(h3("Đại số"))
    s.append(formula("$A ∩ B = {x \\;|\\; x ∈ A$ và $x ∈ B}$ ; $A ∪ B = {x \\;|\\; x ∈ A$ hoặc $x ∈ B}$ ; "
                     "$A \\setminus B = {x \\;|\\; x ∈ A$ và $x ∉ B}$"))
    s.append(formula("$|A ∪ B| = |A| + |B| − |A ∩ B|$ ; số tập con của tập $n$ phần tử $= 2^(n)$"))
    s.append(formula("$P ⇒ Q$ chỉ sai khi $P$ đúng, $Q$ sai ; $\\overline{∀x ∈ X, P(x)} = ∃x ∈ X, \\overline{P}(x)$"))
    s.append(h3("Lượng giác"))
    s.append(formula("$sin^(2) α + cos^(2) α = 1$ ; $tan α = sin α/cos α$ ; $1 + tan^(2) α = 1/cos^(2) α$"))
    s.append(formula("$sin(180° − α) = sin α$ ; $cos(180° − α) = −cos α$ ; $tan(180° − α) = −tan α$"))
    s.append(h3("Hệ thức lượng trong tam giác"))
    s.append(formula("$a^(2) = b^(2) + c^(2) − 2bc·cos A$ ; $cos A = (b^(2) + c^(2) − a^(2)) / (2bc)$"))
    s.append(formula("$a/sin A = b/sin B = c/sin C = 2R$"))
    s.append(formula("$S = ½ah_a = ½ab·sin C = abc/(4R) = pr = √(p(p−a)(p−b)(p−c))$"))
    s.append(h3("Vectơ"))
    s.append(formula("$\\v{AB} + \\v{BC} = \\v{AC}$ ; $\\v{AB} − \\v{AC} = \\v{CB}$ ; $\\v{AB} + \\v{AD} = \\v{AC}$ (hình bình hành)"))
    s.append(formula("$I$ trung điểm $AB$: $\\v{IA} + \\v{IB} = \\v{0}$, $\\v{MA} + \\v{MB} = 2\\v{MI}$ ; "
                     "$G$ trọng tâm: $\\v{GA} + \\v{GB} + \\v{GC} = \\v{0}$, $\\v{MA} + \\v{MB} + \\v{MC} = 3\\v{MG}$"))
    s.append(formula("$A, B, C$ thẳng hàng $⇔ \\v{AB} = k\\v{AC}$ ; $\\v{AB} = (x_B − x_A;\\; y_B − y_A)$ ; "
                     "$\\v{a} · \\v{b} = x_1 x_2 + y_1 y_2$"))

    s.append(h2("7.8. Bảng tra cứu: mỗi mục của đề cương ứng với bài nào trong SGK KNTT"))
    s.append(data_table([
        ["Mục trong đề cương", "Bài trong SGK Toán 10 – Kết nối tri thức"],
        ["1.1. Mệnh đề", "Bài 1. Mệnh đề (Chương I)"],
        ["1.2. Tập hợp", "Bài 2. Tập hợp và các phép toán trên tập hợp (Chương I)"],
        ["1.3. Các phép toán trên tập hợp", "Bài 2. Tập hợp và các phép toán trên tập hợp (Chương I)"],
        ["2.1. Bất phương trình bậc nhất hai ẩn", "Bài 3. Bất phương trình bậc nhất hai ẩn (Chương II)"],
        ["2.2. Hệ bất phương trình bậc nhất hai ẩn", "Bài 4. Hệ bất phương trình bậc nhất hai ẩn (Chương II)"],
        ["3.1. Giá trị lượng giác của một góc từ $0°$ đến $180°$", "Bài 5 (Chương III)"],
        ["3.2. Hệ thức lượng trong tam giác", "Bài 6. Hệ thức lượng trong tam giác (Chương III)"],
        ["4.1. Các khái niệm mở đầu về vectơ", "Bài 7. Các khái niệm mở đầu (Chương IV)"],
        ["4.2 → 4.5 (mở rộng, học trước cho học kì I)", "Bài 8 → Bài 11 (Chương IV)"],
    ], widths=[78 * mm, None], align_center=False))

    s.extend(rule(NAVY, 1.0, 10))
    s.append(Paragraph(inline("<b>Lời kết.</b> Đề kiểm tra giữa học kì I không khó nếu nắm chắc bốn nhóm nội dung: "
                              "mệnh đề – tập hợp, bất phương trình bậc nhất hai ẩn, hệ thức lượng trong tam giác và "
                              "khái niệm vectơ. Hãy học theo ma trận, luyện theo đặc tả và luôn tự kiểm tra bằng "
                              "một đề bấm giờ. Chúc các em làm bài tốt."),
                       _p("end", fontSize=10, leading=15.5, textColor=NAVY, spaceBefore=4)))
    return s
