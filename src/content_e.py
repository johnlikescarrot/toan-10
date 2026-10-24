# -*- coding: utf-8 -*-
"""PHẦN E – Đáp số bài tập tự luyện; PHẦN F – Phụ lục (ma trận đáp án, checklist, tài liệu tham khảo)."""

from reportlab.lib.units import mm

from pdf_kit import (
    CONTENT_W as CH, H1, H2, H3, P, SP, box, bullets, formula, numbered, tbl,
)

CAP = "caption"


def _e(num: str, body: str):
    return P("{b}" + str(num) + ".{/b} " + body, "answer")


def part_e() -> list:
    return [
        H1("PHẦN E. ĐÁP SỐ BÀI TẬP TỰ LUYỆN"),
        P("Bài tập tương ứng nằm ở cuối mỗi chương trong Phần B. Hãy làm trước, chỉ mở trang này khi đã "
          "có kết quả của mình – kể cả khi kết quả sai, việc tự tìm chỗ sai học được nhiều hơn là đọc lời "
          "giải."),
        SP(5),

        H2("E.1. Chương I – Mệnh đề và tập hợp"),
        _e("1", "(a) là mệnh đề, {b}đúng{/b}. (b) là mệnh đề, {b}đúng{/b} (x² ≥ 0 với mọi x). "
                "(c) không là mệnh đề (câu cầu khiến). (d) là mệnh đề chứa biến."),
        SP(2),
        _e("2", "Ā: “∃x ∈ ℝ, x² + 2x + 3 ≤ 0”. Vì x² + 2x + 3 = (x + 1)² + 2 ≥ 2 > 0 nên Ā sai, "
                "do đó {b}A đúng{/b}. B̄: “∀n ∈ ℕ, n² + 1 không chia hết cho 4”. Với n chẵn, n² + 1 chia 4 dư 1; "
                "với n lẻ, n² + 1 chia 4 dư 2. Vậy B sai, {b}B̄ đúng{/b}."),
        SP(2),
        _e("3", "A = {0; 1; 2; 3; 4; 5} (vì x² < 30 ⇒ x ≤ 5). B = {−2; −1; 0; 1; 2}."),
        SP(2),
        _e("4", "A ∩ B = (−3; 4]; A ∪ B = (−∞; 7); A \\ B = (−∞; −3]; "
                "C{sub}ℝ{/sub}(A ∪ B) = [7; +∞)."),
        SP(2),
        _e("5", "|A ∪ B| = 30 + 22 − 12 = 40; số bạn không thích môn nào = 45 − 40 = {b}5{/b}."),
        SP(2),
        _e("6", "Có 6 tập con có đúng 1 phần tử; số tập con khác rỗng là 2{sup}6{/sup} − 1 = {b}63{/b}."),
        SP(5),

        H2("E.2. Chương II – Bất phương trình bậc nhất hai ẩn"),
        _e("7", "(a) và (d) là bất phương trình bậc nhất hai ẩn. (b) có x²; (c) có ba ẩn."),
        SP(2),
        _e("8", "(a) Vẽ d: x + 2y = 4 qua (4; 0), (0; 2). Thay O: 0 ≤ 4 đúng ⇒ miền nghiệm là nửa mặt phẳng "
                "bờ d {b}chứa O{/b}, kể cả bờ. (b) Vẽ d: 3x − y = 3 qua (1; 0), (0; −3). Thay O: 0 > 3 sai "
                "⇒ miền nghiệm là nửa mặt phẳng bờ d {b}không chứa O{/b}, {b}không kể bờ{/b} (dấu >)."),
        SP(2),
        _e("9", "Các đỉnh: O(0; 0), (5; 0), (2; 3), (0; 4). Miền nghiệm là tứ giác với bốn đỉnh đó."),
        SP(2),
        _e("10", "F = 2x + 3y tại các đỉnh: 0; 10; {b}13{/b}; 12 ⇒ F lớn nhất bằng {b}13{/b} tại (2; 3)."),
        SP(2),
        _e("11", "Hệ: 0 ≤ x ≤ 50; y ≥ 20; x + y ≤ 80. F = 20x + 15y (nghìn đồng). Các đỉnh và giá trị: "
                 "(0; 20) → 300; (50; 20) → 1300; (50; 30) → {b}1450{/b}; (0; 80) → 1200. Vậy làm "
                 "{b}50 bánh ngọt và 30 bánh mặn{/b} mỗi ngày, lãi lớn nhất {b}1 450 000 đồng{/b}."),
        SP(5),

        H2("E.3. Chương III – Hệ thức lượng trong tam giác"),
        _e("12", "sin 120° = √3/2; cos 150° = −√3/2; tan 135° = −1; cot 120° = −1/√3 = −√3/3."),
        SP(2),
        _e("13", "cos α = −5/13, α tù ⇒ sin α > 0: sin²α = 1 − 25/169 = 144/169 ⇒ sin α = 12/13; "
                 "tan α = (12/13) : (−5/13) = {b}−12/5{/b}."),
        SP(2),
        _e("14", "sin²40° + cos²40° = 1 và sin²50° + cos²50° = 1 (hoặc dùng sin 50° = cos 40°) ⇒ A = {b}2{/b}."),
        SP(2),
        _e("15", "p = 21; S = √(21·8·7·6) = 84; R = abc/(4S) = 2730/336 = {b}8,125{/b}; "
                 "r = S/p = 84/21 = {b}4{/b}."),
        SP(2),
        _e("16", "BC² = 25 + 49 − 2·5·7·(1/2) = 74 − 35 = 39 ⇒ BC = {b}√39 ≈ 6,24{/b}; "
                 "S = ½·5·7·sin 60° = {b}35√3/4 ≈ 15,16{/b}."),
        SP(2),
        _e("17", "A = 180° − 45° − 60° = {b}75°{/b}. Theo định lí sin: b = 8·sin 45°/sin 75° ≈ {b}5,86{/b}; "
                 "c = 8·sin 60°/sin 75° ≈ {b}7,17{/b}."),
        SP(2),
        _e("18", "Gọi P{sub}1{/sub}, P{sub}2{/sub} là hai người, I là hòn đảo. Góc tại P{sub}1{/sub} = 60°, "
                 "tại P{sub}2{/sub} = 45° ⇒ góc tại I = 75°. Cạnh P{sub}1{/sub}P{sub}2{/sub} = 120 m đối diện "
                 "góc I. Khoảng cách P{sub}1{/sub}I (đối diện góc 45°) = 120·sin 45°/sin 75° ≈ "
                 "{b}87,8 m{/b}."),
        SP(5),

        H2("E.4. Chương IV – Vectơ"),
        _e("19", "|{b}AB{/b}| = 4; |{b}AC{/b}| = 4√2 ≈ 5,66; vectơ bằng {b}AB{/b} là {b}DC{/b}."),
        SP(2),
        _e("20", "M là trung điểm BC và tam giác đều cạnh 3 nên AM ⊥ BC và "
                 "AM = √(3² − 1,5²) = 3√3/2 ≈ {b}2,60{/b}. Vậy |{b}AM{/b}| = 3√3/2."),
        SP(2),
        _e("21", "{b}Sai.{/b} {b}AB{/b} và {b}CD{/b} cùng độ dài (vì AB = CD) nhưng {b}ngược hướng{/b} "
                 "(đi từ A đến B ngược chiều với đi từ C đến D), nên chúng là hai vectơ đối nhau. "
                 "Đẳng thức đúng là {b}AB{/b} = {b}DC{/b}."),
        SP(2),
        _e("22", "{b}FO{/b}, {b}OC{/b}, {b}ED{/b} (cùng hướng và cùng độ dài với {b}AB{/b})."),
        SP(6),
        box("tip",
            [P("{b}Cách tự kiểm tra đáp số mà không cần thầy cô:{/b}", "box_body"),
             bullets([
                 "Với bài tập hợp: vẽ lại trục số và kiểm tra {b}ba điểm đại diện{/b} (một điểm trong kết quả, "
                 "một điểm ngoài, một điểm ở đầu mút).",
                 "Với bài lượng giác: bấm máy kiểm tra sin² + cos² = 1 và so sánh dấu.",
                 "Với bài tam giác: kiểm tra {b}bất đẳng thức tam giác{/b} (a + b > c) và tổng ba góc = 180°.",
                 "Với bài tối ưu: thay phương án tìm được vào {b}tất cả{/b} ràng buộc; nếu có ràng buộc bị vi "
                 "phạm thì đã chọn sai miền.",
             ], "bullet_small")]),
    ]


def part_f() -> list:
    return [
        H1("PHẦN F. PHỤ LỤC"),
        H2("F.1. Bảng ma trận – đáp án đối chiếu"),
        P("Dùng bảng này để kiểm tra đề mẫu đã phủ đủ ma trận hay chưa (cột “Câu” khớp với Phần C)."),
        SP(2),
        tbl([
            ["Đơn vị kiến thức", "Mức", "Câu trong đề mẫu", "Đáp án"],
            ["1.1. Mệnh đề", "NB", "I.1", "B"],
            ["1.1. Mệnh đề (phủ định ∀, ∃)", "NB", "I.2", "B"],
            ["1.2. Tập hợp (liệt kê)", "NB", "I.3", "A"],
            ["1.2. Tập hợp (kí hiệu, số tập con)", "NB, TH", "II.1a, II.1b; III.1", "Đ, Đ; 32"],
            ["1.3. Phép toán trên tập hợp", "NB", "I.4", "B"],
            ["1.3. Phép toán – biểu diễn trục số", "TH, VD", "II.1c, II.1d; IV.1", "S, Đ; xem D.5"],
            ["1.3. Bài toán thực tế tập hợp", "VD", "III.2", "5"],
            ["2.1. Bất phương trình bậc nhất hai ẩn", "NB", "I.5; II.2a", "B; Đ"],
            ["2.1. Nghiệm – miền nghiệm", "NB, TH", "I.6; II.2b, II.2c, II.2d", "C; S, Đ, S"],
            ["2.2. Hệ bất phương trình", "NB", "IV.3a", "xem D.5"],
            ["2.2. Bài toán tối ưu", "VDC", "IV.3b, IV.3c", "160 triệu đồng"],
            ["3.1. Giá trị lượng giác", "NB", "I.7", "B"],
            ["3.1. GTLG khi biết một giá trị", "TH", "I.8", "A"],
            ["3.1. Tính giá trị biểu thức lượng giác", "VD", "III.3", "−7/5"],
            ["3.2. Định lí côsin, sin, diện tích", "NB", "I.9", "B"],
            ["3.2. Giải tam giác", "TH", "I.10; III.4", "A; 6√3"],
            ["3.2. Bài toán thực tiễn", "VD", "IV.2", "≈ 27,5 m"],
            ["4.1. Khái niệm vectơ", "NB", "I.11", "B"],
            ["4.1. Vectơ bằng nhau", "TH", "I.12", "B"],
        ], widths=[62 * mm, 18 * mm, CH - 62 * mm - 18 * mm - 44 * mm, 44 * mm],
            fontsize=8.0, align=["l", "c", "l", "l"]),
        SP(3),
        box("note",
            [P("Cấu trúc điểm của đề mẫu: Phần I 3,0 + Phần II 2,0 + Phần III 2,0 + Phần IV 3,0 = "
               "{b}10,0 điểm{/b}. Số câu trắc nghiệm: 12 + 2 (Đúng – Sai) + 4 = {b}18 câu{/b}, tương ứng "
               "24 “câu/ý” theo cách đếm của ma trận (mỗi câu Đúng – Sai gồm 4 ý, được tính là 4 đơn vị).",
               "box_body")]),
        SP(5),

        H2("F.2. Danh mục kiến thức – kĩ năng cần đạt"),
        P("Trước khi vào phòng thi, hãy tự đánh dấu ô “Đạt” cho từng dòng. Ô nào chưa đạt là ô cần ôn lại."),
        SP(2),
        tbl([
            ["#", "Kĩ năng", "Đạt"],
            ["1", "Nhận biết mệnh đề, mệnh đề chứa biến; phát biểu mệnh đề phủ định (kể cả ∀, ∃)", "☐"],
            ["2", "Phát biểu mệnh đề kéo theo, mệnh đề đảo; dùng đúng “điều kiện cần”, “điều kiện đủ”", "☐"],
            ["3", "Viết tập hợp bằng liệt kê và bằng tính chất đặc trưng; dùng đúng ∈, ∉, ⊂, ⊄", "☐"],
            ["4", "Đọc – viết đúng khoảng, đoạn, nửa khoảng; biểu diễn trên trục số", "☐"],
            ["5", "Thực hiện giao, hợp, hiệu, phần bù; giải bài toán đếm bằng biểu đồ Ven", "☐"],
            ["6", "Nhận biết bất phương trình bậc nhất hai ẩn; kiểm tra một cặp số là nghiệm", "☐"],
            ["7", "Biểu diễn miền nghiệm của bất phương trình và của hệ bất phương trình", "☐"],
            ["8", "Chuyển bài toán thực tế thành hệ bất phương trình; tìm phương án tối ưu", "☐"],
            ["9", "Thuộc bảng giá trị lượng giác của các góc đặc biệt; tính GTLG của góc 0°–180°", "☐"],
            ["10", "Dùng quan hệ hai góc bù nhau, hai góc phụ nhau; dùng sin²α + cos²α = 1", "☐"],
            ["11", "Tính GTLG còn lại khi biết một giá trị; tính giá trị biểu thức lượng giác", "☐"],
            ["12", "Dùng định lí côsin, định lí sin, công thức diện tích để giải tam giác", "☐"],
            ["13", "Giải bài toán thực tế: khoảng cách có vật cản, chiều cao vật", "☐"],
            ["14", "Nhận biết vectơ, độ dài, giá, cùng phương, cùng hướng, bằng nhau, đối nhau, vectơ – không", "☐"],
        ], widths=[10 * mm, CH - 10 * mm - 16 * mm, 16 * mm], fontsize=8.2,
            align=["c", "l", "c"]),
        SP(5),

        H2("F.3. Những điều cần mang và lưu ý trong phòng thi"),
        bullets([
            "{b}Dụng cụ:{/b} bút, thước kẻ, compa (để vẽ đường tròn/venn nếu cần), máy tính cầm tay được phép, "
            "giấy nháp. Không mang tài liệu.",
            "{b}Thời gian:{/b} 90 phút. Ghi giờ bắt đầu lên nháp và kiểm tra tiến độ sau mỗi 20 phút.",
            "{b}Đọc đề hai lần{/b} với câu hỏi về dấu (≤ hay <), về “lấy cả bờ hay không”, về đơn vị.",
            "{b}Không bỏ trống{/b} câu nào; câu khó làm sau, câu dễ làm trước.",
            "{b}Tự luận:{/b} viết công thức trước khi thay số; kết luận rõ ràng; ghi đơn vị. Nếu sai số, "
            "làm tròn theo yêu cầu của đề (thường 1 chữ số thập phân).",
            "{b}Nộp bài:{/b} kiểm tra lại phiếu trả lời đã tô đủ, không tô hai đáp án một câu.",
        ]),
        SP(5),

        H2("F.4. Nguồn tài liệu"),
        bullets([
            "Ma trận đề và Bảng đặc tả kiểm tra Giữa kì I – môn Toán, lớp 10, năm học 2026–2027, "
            "Tổ Toán – Tin, Trường THPT Hà Huy Tập (tệp {i}MA TRẬN TOÁN 10 - GIỮA KÌ I.docx{/i}).",
            "Sách giáo khoa {i}Toán 10{/i}, bộ {i}Kết nối tri thức với cuộc sống{/i} – Chương I, II, III, IV.",
            "Sách bài tập {i}Toán 10{/i} (cùng bộ sách) – phần bài tập tương ứng bốn chương.",
            "Tài liệu này là {b}tài liệu ôn tập{/b} do học sinh/giáo viên tự biên soạn, không phải ấn phẩm "
            "chính thức của nhà xuất bản hay của trường.",
            "Cấu trúc đề mẫu (số câu, số điểm, mức độ, dạng câu) được lấy từ ma trận; {b}đề bài và đáp án do "
            "tài liệu này biên soạn{/b} để phục vụ việc tự ôn tập.",
        ]),
        SP(8),
        H2("F.5. Ghi chú về cách biên soạn"),
        P("Đề mẫu trong Phần C được dựng {b}bám sát từng dòng{/b} của bảng đặc tả: mỗi yêu cầu cần đạt ứng với "
          "ít nhất một câu, đúng mức độ nhận thức (NB/TH/VD/VDC) và đúng dạng câu (lựa chọn, Đúng – Sai, "
          "trả lời ngắn, tự luận). Số câu và điểm từng phần khớp mục II của ma trận (12 – 2 – 4 – 3; "
          "3,0 – 2,0 – 2,0 – 3,0)."),
        P("Mọi đáp số đã được {b}kiểm tra lại bằng tính toán độc lập{/b} (kể cả các giá trị làm tròn). Nếu "
          "phát hiện sai sót, hãy đối chiếu với sách giáo khoa và báo lại để chỉnh sửa – một tài liệu ôn tập "
          "chỉ có giá trị khi nó chính xác."),
        SP(4),
        H3("Quy ước viết tắt dùng trong tài liệu"),
        tbl([
            ["Viết tắt", "Nghĩa", "Viết tắt", "Nghĩa"],
            ["NB", "Nhận biết", "TN", "Trắc nghiệm"],
            ["TH", "Thông hiểu", "TL", "Tự luận"],
            ["VD", "Vận dụng", "ĐS", "Đúng – Sai"],
            ["VDC", "Vận dụng cao", "TLN", "Trả lời ngắn"],
            ["GTLG", "Giá trị lượng giác", "BPT", "Bất phương trình"],
            ["H.1 – H.10", "Hình minh hoạ (đánh số liên tục trong tài liệu)", "SGK", "Sách giáo khoa"],
        ], widths=[22 * mm, 60 * mm, 22 * mm, CH - 104 * mm], fontsize=8.2,
            align=["c", "l", "c", "l"], zebra=False),
        SP(8),
        box("tip",
            [P("{b}Lời cuối.{/b} Kiến thức giữa kì I không nhiều: bốn chương, khoảng mười hai dạng toán, "
               "một bảng công thức. Điều quyết định điểm số không phải là học thêm dạng mới sát ngày thi, "
               "mà là {b}làm đúng những dạng đã biết{/b} và {b}không mất điểm vì bất cẩn{/b}. Chúc bạn ôn tập "
               "hiệu quả và làm bài thật tốt.", "box_body")]),
    ]
