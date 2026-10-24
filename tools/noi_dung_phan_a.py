# -*- coding: utf-8 -*-
"""
Nội dung Phần A (thông tin chung, cấu trúc đề, cách ôn tập) và
Phần B (kiến thức nền tảng & dạng bài theo 4 chương của chương trình
Toán 10 "Kết nối tri thức").

Nguồn: MA TRẬN TOÁN 10 - GIỮA KÌ I.docx (ma trận + bảng đặc tả).
"""

from reportlab.lib import colors
from reportlab.lib.units import mm

W = 498.0          # bề rộng vùng nội dung A4 dọc (pt)
WL = 756.0         # bề rộng vùng nội dung A4 ngang (pt)


# ==========================================================================
# PHẦN A – THÔNG TIN CHUNG, CẤU TRÚC ĐỀ VÀ CÁCH ÔN TẬP
# ==========================================================================

def phan_a(ctx):
    ctx.h1("PHẦN A. THÔNG TIN CHUNG, CẤU TRÚC ĐỀ VÀ CÁCH ÔN TẬP")

    ctx.h2("A.1. Mục tiêu và đối tượng sử dụng")
    ctx.p(
        "Đề cương này được biên soạn từ tài liệu gốc <b>“MA TRẬN TOÁN 10 - GIỮA KÌ I.docx”</b> "
        "(ma trận đề kiểm tra và bảng đặc tả của Trường THPT Hà Huy Tập – Tổ Toán-Tin), bám sát "
        "chương trình Toán lớp 10 của bộ sách <b>“Kết nối tri thức”</b> (Bài 1 đến Bài 7 của tập 1). "
        "Mục tiêu của tài liệu gồm ba tầng:"
    )
    ctx.numbered([
        "<b>Ôn luyện kiến thức:</b> hệ thống hóa toàn bộ kiến thức Toán 10 đến giữa học kỳ I "
        "(mệnh đề, tập hợp, bất phương trình và hệ bất phương trình bậc nhất hai ẩn, hệ thức "
        "lượng trong tam giác, khái niệm vectơ) theo đúng cấu trúc đơn vị kiến thức của ma trận.",
        "<b>Rèn kỹ năng giải bài:</b> mỗi chương có các dạng bài toán điển hình kèm lời giải mẫu, "
        "lỗi thường gặp và bài tập tự luyện có đáp án.",
        "<b>Đồng thời là bộ đề và bộ đáp án:</b> Phần C và Phần D trình bày <b>đầy đủ 21 câu hỏi "
        "kèm đáp án</b> của bài kiểm tra giữa học kỳ I năm học 2026-2027, đúng theo ma trận và bảng "
        "đặc tả (12 câu trắc nghiệm chọn phương án, 2 câu trắc nghiệm đúng sai, 4 câu trả lời ngắn, "
        "3 câu tự luận).",
    ])
    ctx.box("Đối tượng sử dụng", [
        "Học sinh lớp 10 (môn Toán, chương trình “Kết nối tri thức”) tự học trước khi kiểm tra.",
        "Giáo viên Toán dùng làm đề cương ôn tập, làm bài mẫu trên lớp và đối chiếu khi chấm điểm.",
        "Tổ Toán-Tin sử dụng làm tài liệu sinh hoạt chuyên môn và cơ sở ra đề đề thi đểu.",
    ], kind="grey")

    ctx.h2("A.2. Cấu trúc bài kiểm tra giữa học kỳ I năm học 2026-2027")
    ctx.p(
        "Bài kiểm tra viết trong <b>90 phút</b>, tổng điểm <b>10,0</b>, gồm 21 câu hỏi chia làm "
        "4 phần. Cấu trúc này được giữ nguyên trong toàn bộ Phần C và Phần D của đề cương này."
    )
    ctx.table(
        [
            ["Phần", "Dạng câu hỏi", "Số câu", "Điểm mỗi câu", "Thành tiền", "Cách làm bài được quy định"],
            ["I", "Trắc nghiệm nhiều phương án lựa chọn", "12", "0,25", "3,0",
             "Chọn một phương án đúng nhất (A, B, C hoặc D) ở mỗi câu."],
            ["II", "Trắc nghiệm đúng sai", "2", "0,1 / 0,25 / 0,5 / 1,0", "2,0",
             "Mỗi câu gồm 4 ý. Điểm của câu tính theo số ý đúng: đúng 1 ý – 0,1 điểm; "
             "đúng 2 ý – 0,25 điểm; đúng 3 ý – 0,5 điểm; đúng 4 ý – 1,0 điểm."],
            ["III", "Trắc nghiệm trả lời ngắn", "4", "0,5", "2,0",
             "Ghi kết quả hoặc lời giải ngắn gọn, không cần trình bày dài."],
            ["IV", "Tự luận", "3", "1,0", "3,0",
             "Trình bày đầy đủ lập luận, nêu rõ các bước và công thức sử dụng."],
            ["", "TỔNG", "21", "", "10,0", ""],
        ],
        widths=[42, 150, 44, 78, 50, W - 364],
        align=["c", "l", "c", "c", "c", "l"],
    )
    ctx.caption("Bảng 1. Cấu trúc bài kiểm tra giữa học kỳ I môn Toán 10 năm học 2026-2027.")

    ctx.h2("A.3. Ma trận đề kiểm tra (nguyên bản theo tài liệu nguồn)")
    ctx.p(
        "Bảng dưới đây được trích nguyên vẹn từ tài liệu nguồn. Vì có 19 cột nên được trình bày "
        "trên trang khổ ngang. Các chữ viết tắt: <b>NB</b> – nhận biết; <b>TH</b> – thông hiểu; "
        "<b>VD</b> – vận dụng; <b>VDC</b> – vận dụng cao; <b>TN</b> – trắc nghiệm; "
        "<b>TL</b> – tự luận."
    )
    ctx.to_landscape()
    ctx.p("<b>Bảng 2. Ma trận đề kiểm tra giữa kỳ I năm học 2026-2027 (nguyên bản).</b>")

    def _mtx(tt, nk, dv, mid, cuoi):
        """Gộp một dòng của ma trận: 3 cột đầu + 12 cột giữa + 4 cột cuối."""
        assert len(mid) == 12 and len(cuoi) == 4
        return [tt, nk, dv] + list(mid) + list(cuoi)

    _theo_dong = [
        _mtx("1", "Mệnh đề. Tập hợp.", "1.1. Mệnh đề",
             [2, "", "", "", "", "", "", "", "", "", "", ""],
             ["2", "", "0,5", ""]),
        _mtx("", "", "1.2. Tập hợp",
             [1, "", "", 1, 1, "", "", 1, "", "", "", ""],
             ["4", "", "1,25", ""]),
        _mtx("", "", "1.3. Các phép toán trên tập hợp",
             [1, "", "", 1, 1, 1, "", 1, 1, 1, "", ""],
             ["4", "1", "1,25", "1,0"]),
        _mtx("2", "Bất phương trình và hệ bất phương trình bậc nhất hai ẩn",
             "2.1. Bất phương trình bậc nhất hai ẩn",
             [1, "", "", 1, 2, 1, "", 1, "", "", "", ""],
             ["5", "", "1,25", ""]),
        _mtx("", "", "2.2. Hệ bất phương trình bậc nhất hai ẩn",
             [1, "", "", 1, "", "", "", "", "", "", "", 1],
             ["1", "1", "0,25", "1,0"]),
        _mtx("3", "Hệ thức lượng trong tam giác.",
             "3.1. Giá trị lượng giác của một góc từ 0° đến 180°.",
             [1, 1, "", "", "", "", "", "", 1, "", "", ""],
             ["3", "", "1,0", ""]),
        _mtx("", "", "3.2. Hệ thức lượng trong tam giác",
             [1, 1, "", "", "", "", "", "", 1, "", 1, ""],
             ["3", "1", "1,0", "1,0"]),
        _mtx("4", "Vectơ", "4.1. Khái niệm vectơ",
             [1, 1, "", "", "", "", "", "", "", "", "", ""],
             ["2", "", "0,5", ""]),
        _mtx("Tổng", "", "",
             [9, 3, 0, 2, 4, 2, "", 2, 2, 1, 1, 1],
             ["24", "3", "7,0", "3,0"]),
    ]
    ctx.table(
        [["TT", "Nội dung kiến thức", "Đơn vị kiến thức",
          "TN chọn PA: NB", "TN chọn PA: TH", "TN chọn PA: VD",
          "ĐS: NB", "ĐS: TH", "ĐS: VD",
          "TLN: NB", "TLN: TH", "TLN: VD",
          "TL: TH", "TL: VD", "TL: VDC",
          "Số câu TN", "Số câu TL", "Điểm TN", "Điểm TL"]] + _theo_dong,
        widths=[30, 108, 96, 34, 34, 34, 30, 30, 30, 30, 30, 30, 30, 30, 32, 40, 40, 36, 34],
        align=["c", "l", "l", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c",
               "c", "c", "c", "c"],
    )
    ctx.caption("Bảng 2 (nguyên bản). Kết quả: 24 câu trắc nghiệm – 7,0 điểm; 3 câu tự luận – 3,0 điểm.")

    ctx.h2("A.4. Bảng đặc tả (nguyên bản theo tài liệu nguồn)")
    ctx.p(
        "Bảng đặc tả cho biết từng câu hỏi kiểm tra nội dung gì và ở mức độ nào. Đây là bản "
        "“khoá” để đối chiếu khi xây dựng đề: mọi câu hỏi ở Phần C đều bám theo bảng này."
    )
    ctx.p("<b>Bảng 3. Bảng đặc tả đề kiểm tra giữa kỳ I năm học 2026-2027 (nguyên bản).</b>")
    ctx.table(
        [
            ["TT", "Nội dung kiến thức", "Đơn vị kiến thức",
             "Mức độ kiến thức, kỹ năng cần kiểm tra đánh giá",
             "NB", "TH", "VD", "VDC"],
            ["1", "Mệnh đề. Tập hợp.", "1.1. Mệnh đề",
             "<b>Nhận biết:</b> Câu 1. Biết thế nào là một mệnh đề, mệnh đề phủ định, mệnh đề "
             "chứa biến. Câu 2. Biết ý nghĩa kí hiệu phổ biến (∀) và kí hiệu tồn tại (∃).",
             "2", "", "", ""],
            ["", "", "1.2. Tập hợp",
             "<b>Nhận biết:</b> Câu 3. Biết cho tập hợp bằng cách liệt kê các phần tử của tập hợp "
             "hoặc chỉ ra tính chất đặc trưng của các phần tử của tập hợp; Câu 1a (ĐS) – sử dụng "
             "đúng các kí hiệu ∈; sử dụng đúng các kí hiệu (a;b); [a;b]; (a;b]; [a;b); (–∞;a); "
             "(–∞;a]; (a;+∞); [a;+∞); (–∞;+∞). <b>Thông hiểu:</b> Câu 1b. Biểu diễn được các khoảng, "
             "đoạn trên trục số; lấy được ví dụ về tập hợp, tập hợp con, tập hợp bằng nhau; "
             "Câu 1 (TLN): tìm số tập hợp con của 1 tập hợp.",
             "1+1", "1+1", "", ""],
            ["", "", "1.3. Các phép toán trên tập hợp",
             "<b>Nhận biết:</b> Câu 4. Biết dùng biểu đồ Ven để biểu diễn giao của hai tập hợp, "
             "hợp của hai tập hợp. <b>Thông hiểu:</b> Câu 1c, Câu 1 (TL) – thực hiện được các phép "
             "toán giao của hai tập hợp, hợp của hai tập hợp, phần bù của một tập con. "
             "<b>Vận dụng:</b> Câu 1d – thực hiện được các phép toán giao, hợp, phần bù của một "
             "tập con; Câu 2 (TLN) – bài toán thực tế các phép toán tập hợp.",
             "1", "1+1TL", "1+1", ""],
            ["2", "Bất phương trình và hệ bất phương trình bậc nhất hai ẩn",
             "2.1. Bất phương trình bậc nhất hai ẩn",
             "<b>Nhận biết:</b> Câu 5. Nhận biết được bất phương trình bậc nhất hai ẩn; Câu 2a – "
             "nhận biết được nghiệm và miền nghiệm của bất phương trình bậc nhất hai ẩn trên mặt "
             "phẳng tọa độ. <b>Thông hiểu:</b> Câu 2b, 2c – mô tả được miền nghiệm của bất phương "
             "trình bậc nhất hai ẩn trên mặt phẳng tọa độ. <b>Vận dụng:</b> Câu 2d – chuyển được "
             "các điều kiện của bài toán thực tế về dạng bất phương trình bậc nhất hai ẩn.",
             "1+1", "2", "1", ""],
            ["", "", "2.2. Hệ bất phương trình bậc nhất hai ẩn",
             "<b>Nhận biết:</b> Câu 6. Nhận biết được hệ bất phương trình bậc nhất hai ẩn; nhận biết "
             "được nghiệm và miền nghiệm của hệ bất phương trình bậc nhất hai ẩn trên mặt phẳng "
             "tọa độ. <b>Vận dụng cao:</b> Câu 3 (TL) – mô tả được miền nghiệm của hệ bất phương "
             "trình bậc nhất hai ẩn trên mặt phẳng tọa độ; tìm giá trị tối ưu của bài toán tìm "
             "phương án tối ưu.",
             "1", "", "", "1 TL"],
            ["3", "Hệ thức lượng trong tam giác.",
             "3.1. Giá trị lượng giác của một góc từ 0° đến 180°.",
             "<b>Nhận biết:</b> Câu 7. Nhận biết được giá trị lượng giác của một góc từ 0° đến 180°; "
             "nhận biết được hệ thức liên hệ giữa các giá trị lượng giác của các góc phụ nhau, bù "
             "nhau; tính được giá trị lượng giác (đúng hoặc gần đúng) của một góc từ 0° đến 180° "
             "bằng máy tính cầm tay. <b>Thông hiểu:</b> Câu 8. Tính được giá trị lượng giác của một "
             "góc khi biết 1 trong 4 giá trị lượng giác của nó. <b>Vận dụng:</b> Câu 3 (TLN) – cho biết "
             "1 giá trị lượng giác, tính giá trị của 1 biểu thức.",
             "1", "1", "1", ""],
            ["", "", "3.2. Hệ thức lượng trong tam giác",
             "<b>Nhận biết:</b> Câu 9. Nhận biết các hệ thức lượng cơ bản trong tam giác: định lí "
             "côsin, định lí sin, công thức tính diện tích tam giác. <b>Thông hiểu:</b> Câu 10 TN, "
             "Câu 4 (TLN) – sử dụng được các hệ thức lượng cơ bản trong tam giác để tính các cạnh, "
             "các góc chưa biết và diện tích tam giác, ứng dụng giải bài toán thực tiễn. "
             "<b>Vận dụng:</b> Câu 2 (TL) – mô tả được cách giải tam giác và vận dụng được vào việc "
             "giải một số bài toán có nội dung thực tiễn (ví dụ: xác định khoảng cách giữa hai địa "
             "điểm khi gặp vật cản, xác định chiều cao của vật khi không thể đo trực tiếp…).",
             "2", "1+1TLN", "1 (TL)", ""],
            ["4", "Vectơ", "4.1. Khái niệm vectơ",
             "<b>Nhận biết:</b> Câu 11. Biết các khái niệm và tính chất vectơ, vectơ-không, độ dài "
             "vectơ, hai vectơ cùng phương, cùng hướng, hai vectơ bằng nhau; biết được vectơ-không "
             "cùng phương và cùng hướng với mọi vectơ. <b>Thông hiểu:</b> Câu 12. Hiểu được khái "
             "niệm và đặc điểm của các vectơ, vectơ-không, độ dài vectơ, hai vectơ cùng phương, hai "
             "vectơ bằng nhau; chứng minh được hai vectơ bằng nhau trong một số trường hợp đơn giản.",
             "1", "1", "", ""],
        ],
        widths=[28, 92, 92, 388, 40, 40, 40, 36],
        align=["c", "l", "l", "l", "c", "c", "c", "c"],
    )
    ctx.caption("Bảng 3 (nguyên bản). Bảng đặc tả đầy đủ 21 câu hỏi với mức độ nhận thức tương ứng.")
    ctx.to_portrait()

    ctx.h2("A.5. Bảng đối chiếu: câu hỏi của đề với đơn vị kiến thức")
    ctx.p(
        "Bảng dưới đây là “bản dịch” từ bảng đặc tả sang đề thi cụ thể ở Phần C, giúp thầy cô "
        "kiểm tra nhanh rằng mọi câu hỏi đều có mặt trong đề và đúng mức độ."
    )
    ctx.table(
        [
            ["Câu trong đề", "Phần", "Đơn vị kiến thức", "Mức độ", "Nội dung kiểm tra (rút gọn từ bảng đặc tả)"],
            ["Câu 1", "I – TN chọn PA", "1.1. Mệnh đề", "Nhận biết",
             "Mệnh đề, mệnh đề chứa biến."],
            ["Câu 2", "I – TN chọn PA", "1.1. Mệnh đề", "Nhận biết",
             "Ý nghĩa kí hiệu phổ biến (∀) và kí hiệu tồn tại (∃)."],
            ["Câu 3", "I – TN chọn PA", "1.2. Tập hợp", "Nhận biết",
             "Cách cho tập hợp bằng liệt kê phần tử hoặc nêu tính chất đặc trưng."],
            ["Câu 4", "I – TN chọn PA", "1.3. Các phép toán trên tập hợp", "Nhận biết",
             "Biểu đồ Ven biểu diễn giao và hợp của hai tập hợp."],
            ["Câu 5", "I – TN chọn PA", "2.1. Bất phương trình bậc nhất hai ẩn", "Nhận biết",
             "Nhận biết bất phương trình bậc nhất hai ẩn; nghiệm và miền nghiệm của nó."],
            ["Câu 6", "I – TN chọn PA", "2.2. Hệ bất phương trình bậc nhất hai ẩn", "Nhận biết",
             "Nhận biết hệ bất phương trình bậc nhất hai ẩn; nghiệm và miền nghiệm của hệ."],
            ["Câu 7", "I – TN chọn PA", "3.1. Giá trị lượng giác của góc 0° đến 180°", "Nhận biết",
             "Giá trị lượng giác của góc trong [0°; 180°]; quan hệ giữa góc bù nhau."],
            ["Câu 8", "I – TN chọn PA", "3.1. Giá trị lượng giác của góc 0° đến 180°", "Thông hiểu",
             "Tính giá trị lượng giác của một góc khi biết một trong bốn giá trị lượng giác của nó."],
            ["Câu 9", "I – TN chọn PA", "3.2. Hệ thức lượng trong tam giác", "Nhận biết",
             "Định lí côsin, định lí sin, công thức tính diện tích tam giác."],
            ["Câu 10", "I – TN chọn PA", "3.2. Hệ thức lượng trong tam giác", "Thông hiểu",
             "Tính cạnh, góc chưa biết bằng các hệ thức lượng."],
            ["Câu 11", "I – TN chọn PA", "4.1. Khái niệm vectơ", "Nhận biết",
             "Vectơ, vectơ-không, độ dài vectơ, vectơ cùng phương, cùng hướng, bằng nhau."],
            ["Câu 12", "I – TN chọn PA", "4.1. Khái niệm vectơ", "Thông hiểu",
             "Chứng minh hai vectơ bằng nhau trong trường hợp đơn giản."],
            ["Câu 13", "II – Đúng sai", "1.2. Tập hợp; 1.3. Các phép toán", "NB, TH, VD",
             "4 ý: kí hiệu ∈; tập hợp con và tập hợp bằng nhau; khoảng – đoạn; tập rỗng."],
            ["Câu 14", "II – Đúng sai", "2.1; 2.2", "NB, TH, VD",
             "4 ý: bất phương trình bậc nhất hai ẩn; miền nghiệm; nghiệm của hệ; hình học của hệ."],
            ["Câu 15", "III – Trả lời ngắn", "1.2. Tập hợp", "Thông hiểu",
             "Tìm số tập hợp con của một tập hợp."],
            ["Câu 16", "III – Trả lời ngắn", "1.3. Các phép toán trên tập hợp", "Vận dụng",
             "Bài toán thực tế các phép toán trên tập hợp."],
            ["Câu 17", "III – Trả lời ngắn", "3.1. Giá trị lượng giác của góc 0° đến 180°", "Vận dụng",
             "Cho biết một giá trị lượng giác, tính giá trị của một biểu thức."],
            ["Câu 18", "III – Trả lời ngắn", "3.2. Hệ thức lượng trong tam giác", "Thông hiểu",
             "Dùng định lí côsin và công thức diện tích để tính diện tích tam giác."],
            ["Câu 19", "IV – Tự luận", "1.3. Các phép toán trên tập hợp", "MĐ2 (1,0 đ)",
             "Thực hiện các phép toán giao, hợp, phần bù của một tập con."],
            ["Câu 20", "IV – Tự luận", "3.2. Hệ thức lượng trong tam giác", "MĐ2 (1,0 đ)",
             "Giải tam giác và vận dụng vào bài toán thực tiễn (mức đơn giản)."],
            ["Câu 21", "IV – Tự luận", "2.2. Hệ bất phương trình bậc nhất hai ẩn", "MĐ3 (1,0 đ)",
             "Mô tả miền nghiệm của hệ bất phương trình và tìm giá trị tối ưu."],
        ],
        widths=[66, 96, 150, 78, W - 390],
        align=["c", "l", "l", "c", "l"],
    )
    ctx.caption("Bảng 4. Đối chiếu 21 câu hỏi của đề với bảng đặc tả của tài liệu nguồn.")

    ctx.h2("A.6. Ghi chú về các điểm chưa thống nhất trong tài liệu nguồn")
    ctx.p(
        "Khi đối chiếu ma trận (Bảng 2) với phần “Hình thức” của tài liệu gốc, phát hiện vài chỗ "
        "chưa khớp nhau. Đề cương này giữ nguyên các bảng gốc để thầy cô tiếp tục sử dụng, đồng thời "
        "đề xuất cách hiểu nhất quán như sau:"
    )
    ctx.table(
        [
            ["Vấn đề quan sát được", "Cách hiểu thống nhất áp dụng trong đề cương"],
            ["Phần “Hình thức” ghi: 12 câu trắc nghiệm chọn phương án (3 điểm), 2 câu đúng sai "
             "(2 điểm), 4 câu trả lời ngắn (2 điểm), 3 câu tự luận (3 điểm) – tổng 21 câu, 10 điểm.",
             "Lấy phần “Hình thức” làm chuẩn: <b>21 câu – 10,0 điểm – 90 phút</b>. Mọi câu hỏi "
             "trong Phần C đều bám theo chuẩn này."],
            ["Ở cột “TN chọn PA”, tổng theo hàng là 9 câu nhận biết + 4 câu thông hiểu + 1 câu "
             "vận dụng = 14, trong khi tổng ghi ở dòng “Tổng” là 9 + 3 + 0 = 12.",
             "Lấy <b>12 câu</b> của phần “Hình thức”. Bốn câu thừa được san vào các câu hiện có "
             "(xem Câu 5, 8, 10, 12 có thêm ý kiểm tra tương ứng)."],
            ["Ở các cột “Đúng sai”, tổng theo hàng cho 10 ý, trong khi tổng ghi là 2 + 4 + 2 = 8 ý.",
             "Mỗi câu đúng sai có <b>4 ý</b> (Câu 13 và Câu 14), tổng 8 ý – khớp với cách tính "
             "điểm “đúng 1 ý 0,1 … đúng 4 ý 1,0”."],
            ["Cột “Số câu TN” ghi tổng 24 trong khi đề thực tế có 18 câu trắc nghiệm.",
             "24 là tổng số ý/câu hỏi liệt kê ở bảng đặc tả (bao gồm các ý của câu đúng sai và "
             "các câu tự luận). Số câu làm bài vẫn là 18 câu trắc nghiệm + 3 câu tự luận."],
        ],
        widths=[280, W - 280],
        align=["l", "l"],
    )
    ctx.caption("Bảng 5. Các điểm cần hiệu chỉnh trong ma trận của tài liệu nguồn.")

    ctx.h2("A.7. Lộ trình ôn tập gợi ý (8 tuần)")
    ctx.table(
        [
            ["Tuần", "Nội dung trọng tâm", "Việc cần làm", "Câu hỏi tự kiểm tra (Phần C)"],
            ["1", "Chương 1 – Mệnh đề (Bài 1)",
             "Học thuộc khái niệm; làm hết dạng bài VD1–VD3 và 8 bài tự luyện của Chương 1.",
             "Câu 1, 2, 13"],
            ["2", "Chương 1 – Tập hợp (Bài 2)",
             "Tập hợp con, kí hiệu khoảng/đoạn, biểu đồ Ven; VD4–VD7.",
             "Câu 3, 4, 15, 16, 19"],
            ["3", "Chương 2 – Bất phương trình (Bài 3)",
             "Cách tìm nghiệm, miền nghiệm trên mặt phẳng tọa độ; bài toán thực tế.",
             "Câu 5, 14"],
            ["4", "Chương 2 – Hệ bất phương trình (Bài 4)",
             "Giao của các miền nghiệm; bài toán tối ưu.",
             "Câu 14, 21"],
            ["5", "Chương 3 – Giá trị lượng giác (Bài 5)",
             "Bảng giá trị lượng giác; quan hệ giữa góc bù nhau; tính bằng máy tính cầm tay.",
             "Câu 7, 8, 17"],
            ["6", "Chương 3 – Hệ thức lượng (Bài 6)",
             "Định lí côsin, định lí sin, diện tích, giải tam giác; bài toán thực tế.",
             "Câu 9, 10, 18, 20"],
            ["7", "Chương 4 – Vectơ (Bài 7)",
             "Khái niệm vectơ, vectơ-không, cùng phương, cùng hướng, bằng nhau.",
             "Câu 11, 12"],
            ["8", "Ôn toàn bộ và kỹ năng làm bài",
             "Làm trọn đề 21 câu trong 90 phút; xem lại phần sai; dùng Phiếu tự đánh giá (Phần E).",
             "Toàn bộ Câu 1–21"],
        ],
        widths=[36, 130, 200, W - 366],
        align=["c", "l", "l", "l"],
    )
    ctx.caption("Bảng 6. Lộ trình ôn tập gợi ý theo tuần.")

    ctx.h2("A.8. Phương pháp ôn tập hiệu quả")
    ctx.numbered([
        "<b>Đọc – Gạch – Kể lại.</b> Mỗi mục lý thuyết trong Phần B: đọc, gạch công thức, đóng sách "
        "kể lại bằng lời. Kể lại được thì đã hiểu.",
        "<b>Ví dụ mẫu trước, tự làm sau.</b> Đọc kỹ lời giải mẫu (mỗi dạng bài đều có), che đáp án, "
        "tự làm lại rồi mới soát.",
        "<b>Nguyên tắc “3 phút”.</b> Một câu trắc nghiệm bị bỏ trống quá 3 phút thì chuyển sang câu "
        "khác, đánh dấu lại và quay về sau. Trong 90 phút, 21 câu trung bình 4 phút/câu.",
        "<b>Ưu tiên chỗ yếu.</b> Dùng Phiếu tự đánh giá ở Phần E: mỗi mục có ba mức (tốt – cần ôn – "
        "chưa làm được). Ôn theo thứ tự “chưa làm được” → “cần ôn” → “tốt”.",
        "<b>Chấm điểm ngay.</b> Sau mỗi lần làm đề, chấm theo bảng đáp án ở Phần D và ghi điểm từng "
        "phần vào Phiếu tự đánh giá. Sai ở đâu thì ôn lại đúng mục đó.",
    ])
    ctx.box("Quy ước kí hiệu dùng trong tài liệu", [
        "Vectơ được kí hiệu bằng chữ in nghiêng đậm (a, b, c…) hoặc bằng cặp điểm: <b>vectơ AB</b> "
        "(đọc là “vectơ A B”), để tiện đọc khi in.",
        "Các kí hiệu dùng chung: ∀ (phổ biến), ∃ (tồn tại), ∈ (thuộc), ⊂ (là tập con của), "
        "⊆ (là tập con hoặc bằng), ∅ (tập rỗng), ≠ (không bằng), ≤ (nhỏ hơn hoặc bằng), "
        "≥ (lớn hơn hoặc bằng), ∠ (góc), ⊥ (vuông góc).",
    ], kind="grey")
