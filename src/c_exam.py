# -*- coding: utf-8 -*-
"""PHẦN II – ĐỀ THI THAM KHẢO BÁM SÁT MA TRẬN (đủ 24 câu)."""
from kit import *
from kit import _p

MCQ = [
    # (số, mức, nội dung, [4 phương án], đáp án, chủ đề)
    (1, "NB", "Trong các câu sau, câu nào **là** một mệnh đề?",
     ["Bạn có thích học môn Toán không?", "Hà Nội là thủ đô của Việt Nam.",
      "Hãy chăm chỉ học tập nhé!", "$x + 1 > 3$"], "B", "Mệnh đề"),
    (2, "NB", "Mệnh đề “$∀x ∈ ℝ, x^(2) ≥ 0$” được đọc là:",
     ["Tồn tại số thực $x$ sao cho $x^(2) ≥ 0$.", "Mọi số thực $x$ đều có $x^(2) ≥ 0$.",
      "Mọi số thực $x$ đều có $x^(2) < 0$.", "Có đúng một số thực $x$ để $x^(2) ≥ 0$."], "B", "Mệnh đề"),
    (3, "NB", "Cho tập hợp $A = {1; 2; 3; 5; 7}$. Khẳng định nào sau đây **đúng**?",
     ["$4 ∈ A$", "$5 ∈ A$", "$2 ∉ A$", "$7 ∉ A$"], "B", "Tập hợp"),
    (4, "NB", "Cho hai tập hợp $A = {1; 2; 3; 4}$ và $B = {3; 4; 5}$. Tập hợp $A ∩ B$ là:",
     ["${1; 2}$", "${3; 4}$", "${1; 2; 3; 4; 5}$", "${5}$"], "B", "Các phép toán trên tập hợp"),
    (5, "NB", "Bất phương trình nào sau đây là **bất phương trình bậc nhất hai ẩn**?",
     ["$2x + 3y ≤ 5$", "$x^(2) + y > 1$", "$xy − 3 ≥ 0$", "$1/x + y < 2$"], "A",
     "Bất phương trình bậc nhất hai ẩn"),
    (6, "NB", "Hệ nào sau đây là **hệ bất phương trình bậc nhất hai ẩn**?",
     ["$\\{x + y > 1;\\; 2x − y ≤ 3\\}$", "$\\{x^(2) + y > 1;\\; x − y < 0\\}$",
      "$\\{xy ≥ 1;\\; x + y ≤ 2\\}$", "$\\{1/x + y > 1;\\; x − y < 2\\}$"], "A",
     "Hệ bất phương trình bậc nhất hai ẩn"),
    (7, "NB", "Giá trị của $sin 150°$ bằng:",
     ["$−1/2$", "$1/2$", "$√3/2$", "$−√3/2$"], "B", "Giá trị lượng giác"),
    (8, "TH", "Cho góc $α$ thoả mãn $90° < α < 180°$ và $cos α = −3/5$. Giá trị của $sin α$ bằng:",
     ["$4/5$", "$−4/5$", "$16/25$", "$−16/25$"], "A", "Giá trị lượng giác"),
    (9, "NB", "Trong tam giác $ABC$ bất kì (kí hiệu như thường dùng), khẳng định nào sau đây **đúng**?",
     ["$a^(2) = b^(2) + c^(2) + 2bc·cos A$", "$a / sin A = 2R$",
      "$S = a·b·sin C$", "$a^(2) = b^(2) + c^(2) − 2bc·cos B$"], "B", "Hệ thức lượng"),
    (10, "TH", "Cho tam giác $ABC$ có $b = 5$, $c = 8$ và $A = 60°$. Độ dài cạnh $a$ bằng:",
     ["$7$", "$√89$", "$49$", "$√129$"], "A", "Hệ thức lượng"),
    (11, "NB", "Cho hình bình hành $ABCD$. Khẳng định nào sau đây **đúng**?",
     ["$\\v{AB} = \\v{CD}$", "$\\v{AB} = \\v{DC}$", "$\\v{AB} = \\v{BC}$", "$\\v{AC} = \\v{BD}$"], "B",
     "Khái niệm vectơ"),
    (12, "TH", "Cho hình bình hành $ABCD$. Khẳng định nào sau đây **sai**?",
     ["$\\v{AB} = \\v{DC}$", "$\\v{AD} = \\v{BC}$", "$\\v{AC} = \\v{BD}$",
      "$\\v{AB}$ và $\\v{DC}$ cùng hướng"], "C", "Khái niệm vectơ"),
]

TRUE_FALSE = [
    (13, "Cho tập hợp $A = {x ∈ ℤ \\;|\\; −3 ≤ x ≤ 2}$.",
     [("a)", "Liệt kê các phần tử: $A = {−3; −2; −1; 0; 1; 2}$.", "Đ"),
      ("b)", "Tập hợp $A$ có $5$ phần tử.", "S"),
      ("c)", "Tập hợp $A$ có $64$ tập con.", "Đ"),
      ("d)", "Tập hợp $A$ chứa đúng $2$ số nguyên âm.", "S")],
     "Câu 1a–d"),
    (14, "Cho bất phương trình $2x − y + 3 > 0$ có miền nghiệm là $(P)$ trong mặt phẳng toạ độ $Oxy$.",
     [("a)", "Điểm $O(0; 0)$ thuộc miền nghiệm $(P)$.", "Đ"),
      ("b)", "Điểm $M(2; 8)$ thuộc miền nghiệm $(P)$.", "S"),
      ("c)", "Bờ của miền nghiệm là đường thẳng $2x − y + 3 = 0$, được vẽ bằng nét đứt.", "Đ"),
      ("d)", "Điểm $N(−2; 0)$ thuộc miền nghiệm $(P)$.", "S")],
     "Câu 2a–d"),
]

SHORT = [
    (15, "TH", "Cho góc $α$ thoả mãn $90° < α < 180°$ và $tan α = −2$. "
              "Tính giá trị của biểu thức $P = sin α · cos α$.",
     "$P = −2/5$", "Giá trị lượng giác"),
    (16, "TH", "Cho tam giác $ABC$ có $AB = 5$, $AC = 8$ và $\\widehat{A} = 60°$. "
              "Tính diện tích $S$ của tam giác $ABC$ (làm tròn đến hàng phần trăm).",
     "$S = 10√3 ≈ 17,32$", "Hệ thức lượng"),
]


def exam():
    s = []
    s += h1("05", "ĐỀ THI THAM KHẢO BÁM SÁT MA TRẬN",
            "Cấu trúc: 12 câu trắc nghiệm – 3 điểm • 2 câu đúng/sai – 2 điểm • 4 câu trả lời ngắn – 2 điểm • 3 câu tự luận – 3 điểm")

    s.extend(box(["**Hướng dẫn làm bài.** Thời gian 90 phút. Phần trắc nghiệm chọn phương án: mỗi câu đúng 0,25 điểm. "
                  "Phần đúng/sai: đúng 1 ý 0,1 – đúng 2 ý 0,25 – đúng 3 ý 0,5 – đúng 4 ý 1,0 điểm. "
                  "Phần trả lời ngắn và tự luận: trình bày rõ các bước, ghi đơn vị và làm tròn theo yêu cầu.",
                  "Đề được biên soạn **bám sát bảng đặc tả** của đề kiểm tra giữa học kì I (xem Phần IV), "
                  "đủ 24 câu theo đúng cấu trúc và mức độ nhận thức."],
                 kind="box_warn", title="Trước khi làm bài"))

    # ------------------------------------------------ phần I
    s.append(h2("PHẦN I. TRẮC NGHIỆM CHỌN PHƯƠNG ÁN (12 câu – 3,0 điểm)"))
    for num, lvl, text, opts, _, topic in MCQ:
        block = [question(num, text, lvl, "0,25 điểm")]
        block += options(["<b>%s.</b> %s" % (chr(65 + i), o) for i, o in enumerate(opts)], cols=2)
        s.append(KeepTogether(block))

    # ------------------------------------------------ phần II
    s.append(h2("PHẦN II. TRẮC NGHIỆM ĐÚNG – SAI (2 câu – 2,0 điểm)"))
    s.append(P("Với mỗi câu, hãy xác định mỗi ý (a), (b), (c), (d) là **đúng** hay **sai**, "
               "ghi **Đ** hoặc **S** vào ô tương ứng."))
    for num, lead, stmts, _ in TRUE_FALSE:
        s.append(question(num, lead, "NB – TH – VD", "1,0 điểm"))
        s.extend(truefalse(stmts, show=False))

    # ------------------------------------------------ phần III
    s.append(h2("PHẦN III. TRẮC NGHIỆM TRẢ LỜI NGẮN (4 câu – 2,0 điểm)"))
    s.append(P("Mỗi câu trả lời đúng được 0,5 điểm. Chỉ ghi kết quả (số hoặc biểu thức) vào ô trả lời, không cần trình bày."))
    for num, lvl, text, _, topic in SHORT:
        s.append(question(num, text, lvl, "0,5 điểm"))
        s.append(Spacer(1, 3))

    # ------------------------------------------------ phần IV
    s.append(h2("PHẦN IV. TỰ LUẬN (3 câu – 3,0 điểm)"))
    s.append(question(19, "Cho hai tập hợp $A = {x ∈ ℝ \\;|\\; −3 ≤ x < 5}$ và $B = {x ∈ ℝ \\;|\\; x ≥ 1}$. "
                         "Hãy xác định các tập hợp $A ∩ B$, $A ∪ B$, $A \\setminus B$ và $C_ℝ B$.", "TH",
                      "1,0 điểm"))
    s.append(Spacer(1, 4))
    s.append(question(20, "Từ hai vị trí $A$ và $B$ cách nhau $80$ m trên bờ biển, người ta quan sát một hòn đảo tại "
                         "điểm $C$. Biết $\\widehat{BAC} = 75°$ và $\\widehat{ABC} = 60°$. "
                         "Hãy tính khoảng cách từ $A$ đến đảo và khoảng cách từ $B$ đến đảo "
                         "(làm tròn đến hàng phần trăm).", "VD", "1,0 điểm"))
    s.append(Spacer(1, 4))
    s.append(question(21, "Một nông trại có kế hoạch trồng cà rốt và khoai tây trên diện tích $8$ ha. "
                         "Chi phí trồng cà rốt là $20$ triệu đồng/ha, khoai tây là $30$ triệu đồng/ha, "
                         "tổng vốn đầu tư không vượt quá $180$ triệu đồng. "
                         "Lợi nhuận thu được là $30$ triệu đồng/ha cà rốt và $40$ triệu đồng/ha khoai tây. "
                         "Hỏi nông trại cần trồng mỗi loại trên bao nhiêu ha để lợi nhuận lớn nhất? "
                         "Tính lợi nhuận lớn nhất đó.", "VDC", "1,0 điểm"))
    s.append(Spacer(1, 10))
    s.extend(rule(NAVY, 1.2, 2))
    s.append(P("<i>Hết</i>", "center"))
    return s


def exam_matrix():
    """Bảng tổng hợp ma trận 24 câu của đề tham khảo."""
    s = []
    s.append(h4("Bảng đối chiếu 24 câu của đề tham khảo với ma trận"))
    rows = [["Phần", "Câu", "Nội dung kiến thức", "Mức độ", "Điểm"]]
    for num, lvl, text, opts, ans, topic in MCQ:
        rows.append(["TN chọn đáp án", str(num), topic, lvl, "0,25"])
    rows.append(["TN đúng – sai", "13", "Tập hợp, số tập con", "NB–TH", "1,0"])
    rows.append(["TN đúng – sai", "14", "Miền nghiệm bất phương trình bậc nhất hai ẩn", "NB–TH–VD", "1,0"])
    rows.append(["TN trả lời ngắn", "15", "Giá trị lượng giác (cho $tan$, tính biểu thức)", "TH", "0,5"])
    rows.append(["TN trả lời ngắn", "16", "Diện tích tam giác", "TH", "0,5"])
    rows.append(["Tự luận", "19", "Giao, hợp, hiệu, phần bù của các tập con của $ℝ$", "TH", "1,0"])
    rows.append(["Tự luận", "20", "Định lí sin – bài toán thực tiễn", "VD", "1,0"])
    rows.append(["Tự luận", "21", "Hệ bất phương trình – bài toán tối ưu", "VDC", "1,0"])
    rows.append(["<b>Tổng</b>", "<b>24 câu</b>", "", "", "<b>10,0</b>"])
    s.append(data_table(rows, widths=[34 * mm, 18 * mm, None, 24 * mm, 18 * mm], align_center=False))
    return s
