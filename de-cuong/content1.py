# -*- coding: utf-8 -*-
"""Nội dung: Bìa, mục lục, hướng dẫn, Chương I (Mệnh đề – Tập hợp)."""

# --------------------------------------------------------------------------
# BÌA + MỤC LỤC + HƯỚNG DẪN
# --------------------------------------------------------------------------
FRONT = [
    ("cover", {
        "school": "TRƯỜNG THPT HÀ HUY TẬP",
        "group": "Tổ Toán – Tin",
    }),

    ("h1", "MỤC LỤC", "Đề cương ôn tập giữa học kì I", "toc"),
    ("toc", [
        ("P.0", "Hướng dẫn sử dụng & cấu trúc đề kiểm tra", "toc0"),
        ("P.1", "Chương I – Mệnh đề và tập hợp", "toc1"),
        ("", "1.1  Mệnh đề, mệnh đề chứa biến", "toc1a"),
        ("", "1.2  Tập hợp và các phép toán trên tập hợp", "toc1b"),
        ("P.2", "Chương II – Bất phương trình và hệ bất phương trình bậc nhất hai ẩn", "toc2"),
        ("", "2.1  Bất phương trình bậc nhất hai ẩn", "toc2a"),
        ("", "2.2  Hệ bất phương trình và bài toán tối ưu", "toc2b"),
        ("P.3", "Chương III – Hệ thức lượng trong tam giác", "toc3"),
        ("", "3.1  Giá trị lượng giác của một góc từ 0° đến 180°", "toc3a"),
        ("", "3.2  Định lí côsin, định lí sin và diện tích tam giác", "toc3b"),
        ("P.4", "Chương IV – Vectơ (Bài 7: Các khái niệm mở đầu)", "toc4"),
        ("P.5", "ĐỀ THAM KHẢO SỐ 1 (cấu trúc 100% theo ma trận)", "toc5"),
        ("P.6", "ĐÁP ÁN VÀ LỜI GIẢI CHI TIẾT", "toc6"),
        ("", "Đáp án trắc nghiệm & trả lời ngắn", "toc6a"),
        ("", "Lời giải chi tiết – Phần I: Trắc nghiệm", "toc6b"),
        ("", "Lời giải chi tiết – Phần II: Đúng – Sai", "toc6c"),
        ("", "Lời giải chi tiết – Phần III: Trả lời ngắn", "toc6d"),
        ("", "Lời giải chi tiết – Phần IV: Tự luận", "toc6e"),
        ("P.7", "PHỤ LỤC – Bảng công thức, lỗi thường gặp, chiến lược phòng thi", "toc7"),
    ]),
]

# --------------------------------------------------------------------------
# PHẦN 0 – HƯỚNG DẪN
# --------------------------------------------------------------------------
PART0 = [
    ("h1", "HƯỚNG DẪN SỬ DỤNG & CẤU TRÚC ĐỀ", "Phần 0", "toc0"),

    ("lead", "Tài liệu này được biên soạn **bám sát 100% Ma trận và Bảng đặc tả** đề kiểm tra "
             "giữa học kì I môn Toán 10 (năm học 2026 – 2027) của Tổ Toán – Tin, Trường THPT Hà Huy Tập. "
             "Mọi đơn vị kiến thức, mọi mức độ nhận thức và mọi dạng câu hỏi xuất hiện trong ma trận "
             "đều được trình bày lại thành lý thuyết – phương pháp – ví dụ – bài tập có lời giải."),

    ("box", "Lưu ý quan trọng về tài liệu gốc", [
        "Văn bản gốc của nhà trường (tệp **“MA TRẬN TOÁN 10 – GIỮA KÌ I.docx”)** là **ma trận đề** kèm "
        "**bảng đặc tả** – nghĩa là nó quy định **kiến thức nào được hỏi, ở mức độ nào, bao nhiêu câu, "
        "bao nhiêu điểm**, chứ **không chứa nội dung câu hỏi cụ thể**.",
        "Vì vậy tài liệu này được biên soạn theo hướng: **bám đúng 100%** các đơn vị kiến thức và mức "
        "độ trong ma trận, rồi **xây dựng Đề tham khảo số 1** (Phần 5) có cấu trúc, số câu, dạng câu và "
        "phân bố điểm **trùng khớp hoàn toàn** với ma trận; toàn bộ **21 câu** của đề đều có **đáp án và "
        "lời giải chi tiết** ở Phần 6.",
        "Như vậy, khi đề chính thức được công bố, các em sẽ gặp **đúng những dạng câu** đã luyện ở đây – "
        "chỉ khác con số.",
    ]),
    ("h2", "Cấu trúc đề kiểm tra (theo ma trận của nhà trường)"),
    ("p", "Đề kiểm tra gồm **4 phần**, tổng **10,0 điểm**, thời gian làm bài **90 phút**:"
          ),
    ("table",
     ["Phần", "Hình thức", "Số câu", "Điểm", "Ghi chú"],
     [
         ["I", "Trắc nghiệm nhiều phương án lựa chọn", "12", "3,0", "Mỗi câu đúng 0,25 điểm"],
         ["II", "Trắc nghiệm đúng – sai", "2", "2,0", "Mỗi câu 4 ý, thang điểm lũy tiến"],
         ["III", "Trắc nghiệm trả lời ngắn", "4", "2,0", "Mỗi câu đúng 0,5 điểm"],
         ["IV", "Tự luận", "3", "3,0", "1,0 điểm/câu"],
         ["", "**Tổng**", "**21**", "**10,0**", "90 phút"],
     ],
     [1.3, 5.4, 1.4, 1.2, 3.3],
     ["c", "l", "c", "c", "l"]),

    ("box", "Thang điểm câu Đúng – Sai (rất quan trọng)", [
        "Với mỗi câu đúng – sai gồm 4 ý a), b), c), d), điểm được tính **lũy tiến** theo số ý đúng:",
        "__Đúng 1 ý → 0,1 điểm  •  Đúng 2 ý → 0,25 điểm  •  Đúng 3 ý → 0,5 điểm  •  Đúng 4 ý → 1,0 điểm__",
        "**Chiến lược:** chỉ cần chắc chắn **3/4 ý** là đã có 0,5 điểm – gấp đôi một câu trắc nghiệm thường. "
        "Vì vậy đừng bỏ trống câu đúng – sai, hãy phán đoán từng ý một cách độc lập. "
        "Tuyệt đối không \"đoán bừa\" cả 4 ý theo một chiều, vì xác suất sai toàn bộ là rất cao.",
    ]),

    ("h2", "Phân bố nội dung và mức độ theo ma trận"),
    ("table",
     ["Chương / Bài", "Nhận biết", "Thông hiểu", "Vận dụng", "Vận dụng cao", "Tổng điểm"],
     [
         ["1.1  Mệnh đề", "2", "–", "–", "–", "0,5"],
         ["1.2  Tập hợp", "1 + 1 ý ĐS + 1 TLN", "1 ý ĐS", "–", "–", "1,25"],
         ["1.3  Các phép toán trên tập hợp", "1 + 1 ý ĐS", "1 ý ĐS", "1 TLN + 1 TL", "–", "2,25"],
         ["2.1  Bất phương trình bậc nhất hai ẩn", "1 + 1 ý ĐS", "2 ý ĐS", "1 ý ĐS", "–", "1,25"],
         ["2.2  Hệ bất phương trình bậc nhất hai ẩn", "1", "–", "–", "1 TL", "1,25"],
         ["3.1  Giá trị lượng giác của một góc", "1", "1", "1 TLN", "–", "1,0"],
         ["3.2  Hệ thức lượng trong tam giác", "2", "1 + 1 TLN", "1 TL", "–", "2,0"],
         ["4.1  Khái niệm vectơ", "1", "1", "–", "–", "0,5"],
     ],
     [5.0, 1.7, 1.5, 1.5, 1.4, 1.3],
     ["l", "c", "c", "c", "c", "c"]),

    ("note", "Bảng trên được tổng hợp trực tiếp từ ma trận đề gốc; tổng điểm theo từng dòng khớp với "
             "cột \"Điểm\" của ma trận (phần tự luận được tính vào dòng tương ứng)."),

    ("h2", "Cách dùng tài liệu để ôn tập hiệu quả"),
    ("num", [
        "**Bước 1 – Nắm khung lý thuyết.** Đọc phần lý thuyết của mỗi chương, học thuộc các khung "
        "\"Ghi nhớ\". Đây là phần chiếm trọn 5,0 điểm nhận biết – thông hiểu.",
        "**Bước 2 – Luyện theo dạng.** Mỗi chương đều có mục **Các dạng toán thường gặp** kèm ví dụ mẫu "
        "có lời giải từng bước. Hãy tự làm lại ví dụ trước khi đọc lời giải.",
        "**Bước 3 – Làm đề tham khảo.** Đề tham khảo ở Phần 5 được thiết kế **đúng 100% cấu trúc ma trận** "
        "(12 + 2 + 4 + 3 câu, đúng phân bố mức độ). Hãy bấm đồng hồ 90 phút và làm nghiêm túc.",
        "**Bước 4 – Chấm và sửa.** Đối chiếu Phần 6. Với mỗi câu sai, ghi lại **nguyên nhân sai** "
        "vào sổ tay lỗi (sai kiến thức / sai kĩ năng tính / đọc sai đề / bấm máy sai).",
        "**Bước 5 – Ôn bảng lỗi.** Trước ngày thi 1 – 2 hôm, chỉ cần đọc Phụ lục và sổ tay lỗi.",
    ]),

    ("box", "Những lỗi khiến học sinh mất điểm nhiều nhất", [
        "**Mất điểm oan ở câu Đúng – Sai** vì đọc lướt: sai một chữ \"không\" là đảo ngược cả mệnh đề.",
        "**Quên điều kiện khi bình phương** hai vế của phương trình, hoặc nhân hai vế với số âm mà "
        "không đổi chiều bất phương trình.",
        "**Nhầm ngoặc** khi viết khoảng, đoạn: __(−∞; a)__ khác __(−∞; a]__; **(2; 3)** là một khoảng, "
        "còn **{2; 3}** là tập hai phần tử.",
        "**Nhầm sin và cos của hai góc bù nhau:** bù nhau thì **sin bằng nhau**, **côsin đối nhau**.",
        "**Nhầm vectơ với đoạn thẳng:** AB^{→} và BA^{→} là hai vectơ **ngược hướng**, "
        "không bằng nhau.",
    ]),
]


# --------------------------------------------------------------------------
# CHƯƠNG I
# --------------------------------------------------------------------------
PART1 = [
    ("h1", "CHƯƠNG I – MỆNH ĐỀ VÀ TẬP HỢP", "Phần 1", "toc1"),
    ("lead", "Đây là chương **mở đầu** của chương trình Toán 10 và cũng là chương \"dễ ăn điểm\" nhất "
             "trong đề: chỉ cần hiểu đúng khái niệm là làm được. Trong ma trận, chương này chiếm "
             "**khoảng 4,0 điểm** (mệnh đề + tập hợp + các phép toán + 1 câu tự luận)."),

    ("h2", "1.1  Mệnh đề. Mệnh đề chứa biến"),
    ("mark", "toc1a"),

    ("h3", "1. Mệnh đề là gì?"),
    ("p", "**Mệnh đề** là một câu khẳng định mà tính đúng – sai của nó phải xác định được một cách "
          "khách quan. Một mệnh đề chỉ có thể **đúng** hoặc **sai**, không thể vừa đúng vừa sai."),
    ("p", "Mệnh đề đúng được gọi là **mệnh đề đúng**, mệnh đề sai được gọi là **mệnh đề sai**."),
    ("table",
     ["Câu", "Là mệnh đề?", "Vì sao"],
     [
         ["\"5 là số nguyên tố\"", "Có – đúng", "Khẳng định có tính đúng/sai xác định"],
         ["\"2 + 3 = 6\"", "Có – sai", "Vẫn là mệnh đề dù nội dung sai"],
         ["\"Hôm nay trời đẹp quá!\"", "Không", "Câu cảm thán, không khẳng định"],
         ["\"Bạn có đi học không?\"", "Không", "Câu hỏi"],
         ["\"Hãy làm bài tập đi!\"", "Không", "Câu mệnh lệnh"],
         ["\"x + 1 > 3\"", "Không (chưa xác định)", "Có chứa biến – là **mệnh đề chứa biến**"],
     ],
     [5.6, 2.6, 7.4],
     ["l", "l", "l"]),

    ("h3", "2. Mệnh đề chứa biến"),
    ("p", "Mệnh đề chứa biến là câu khẳng định có chứa **một hay nhiều biến**, mà với mỗi giá trị cụ thể "
          "của biến ta được một mệnh đề."),
    ("p", "Ví dụ: P(x) : \"x^{2} − 3x + 2 = 0\" là mệnh đề chứa biến x. Với x = 1 ta được "
          "\"1 − 3 + 2 = 0\" (đúng); với x = 3 ta được \"9 − 9 + 2 = 0\" (sai)."),

    ("h3", "3. Mệnh đề phủ định"),
    ("p", "**Mệnh đề phủ định** của mệnh đề P, kí hiệu @P (đọc là \"không P\"), là mệnh đề "
          "có nội dung **trái ngược** với P. Đặc điểm quan trọng:"),
    ("eq", "P đúng  ⇔  @P sai;     P sai  ⇔  @P đúng"),

    ("box", "Cách lập mệnh đề phủ định nhanh", [
        "Thêm (hoặc bớt) chữ **\"không\"** (hoặc \"không phải\") vào **trước vị ngữ** của câu, "
        "giữ nguyên phần còn lại.",
        "Ví dụ: P: \"3 là số nguyên tố\" → @P: \"3 **không phải** là số nguyên tố\".",
        "Nếu trong câu có **\"và\"** thì phủ định thành **\"hoặc\"**, có **\"hoặc\"** thì thành **\"và\"**, "
        "có **\"mọi\"/\"tất cả\"** thì thành **\"có một\"/\"tồn tại\"**, và ngược lại.",
        "Cẩn thận với **\"không\"** đã có sẵn trong câu: phủ định của \"x không chia hết cho 2\" là "
        "\"x chia hết cho 2\", **không** phải \"x không không chia hết cho 2\".",
    ]),

    ("h3", "4. Mệnh đề kéo theo. Mệnh đề đảo. Mệnh đề tương đương"),
    ("p", "Cho hai mệnh đề P và Q. Mệnh đề **\"Nếu P thì Q\"** được gọi là **mệnh đề kéo theo**, "
          "kí hiệu **P ⇒ Q**."),
    ("p", "Mệnh đề kéo theo P ⇒ Q chỉ **sai** khi **P đúng và Q sai**; trong mọi trường hợp còn lại "
          "nó đều **đúng**."),
    ("table",
     ["P", "Q", "P ⇒ Q"],
     [
         ["Đúng", "Đúng", "**Đúng**"],
         ["Đúng", "Sai", "**Sai**"],
         ["Sai", "Đúng", "**Đúng**"],
         ["Sai", "Sai", "**Đúng**"],
     ],
     [5, 5, 6],
     ["c", "c", "c"]),
    ("p", "Từ mệnh đề P ⇒ Q ta lập được mệnh đề **đảo** là **Q ⇒ P**. Mệnh đề đảo **không** nhất thiết "
          "đúng khi mệnh đề ban đầu đúng."),
    ("p", "Nếu cả **P ⇒ Q** và **Q ⇒ P** đều đúng thì ta nói P và Q **tương đương** nhau, kí hiệu "
          "**P ⇔ Q** (đọc: \"P khi và chỉ khi Q\", \"P nếu và chỉ nếu Q\")."),
    ("box", "Điều kiện cần – điều kiện đủ – điều kiện cần và đủ", [
        "Với mệnh đề **P ⇒ Q** (\"Nếu P thì Q\", \"P kéo theo Q\"):",
        "•  **P** là **điều kiện đủ** để có **Q** (có P là đủ để có Q).",
        "•  **Q** là **điều kiện cần** để có **P** (muốn có P thì ắt phải có Q).",
        "Với mệnh đề **P ⇔ Q**: **P** là **điều kiện cần và đủ** để có **Q**.",
        "__Mẹo nhớ:__ \"đủ\" đứng trước mũi tên, \"cần\" đứng sau mũi tên. "
        "Ví dụ: \"Tam giác ABC cân và có một góc 60° ⇒ ABC đều\". "
        "Điều kiện **đủ** là \"cân và có một góc 60°\"; điều kiện **cần** là \"ABC đều\".",
    ]),

    ("h3", "5. Kí hiệu ∀ và ∃"),
    ("table",
     ["Kí hiệu", "Đọc là", "Nghĩa"],
     [
         ["∀x ∈ X, P(x)", "với mọi x thuộc X, P(x)", "P(x) đúng với **tất cả** x trong X"],
         ["∃x ∈ X, P(x)", "tồn tại x thuộc X, P(x)", "có **ít nhất một** x trong X để P(x) đúng"],
     ],
     [3.6, 5.4, 7.4],
     ["l", "l", "l"]),

    ("box", "Phủ định mệnh đề chứa ∀, ∃ (dạng câu hỏi rất hay gặp)", [
        "Phủ định của **∀x ∈ X, P(x)**  là  **∃x ∈ X, @P(x)** (P gạch ngang, tức \"không P(x)\", với mọi x).",
        "Phủ định của **∃x ∈ X, P(x)**  là  **∀x ∈ X, @P(x)** (với mọi x, P(x) sai).",
        "Nói cách khác: **đổi ∀ thành ∃** (và ngược lại) rồi **phủ định phần thân**.",
        "Ví dụ: P: \"∀x ∈ ℝ, x^{2} ≥ 0\" → @P: \"∃x ∈ ℝ, x^{2} < 0\".",
        "Ví dụ: Q: \"∃n ∈ ℕ, n chia hết cho 3\" → @Q: \"∀n ∈ ℕ, n **không** chia hết cho 3\".",
    ]),

    ("h2", "Các dạng toán thường gặp – Mệnh đề"),

    ("h3", "Dạng 1. Nhận biết mệnh đề, mệnh đề chứa biến"),
    ("p", "**Phương pháp:** kiểm tra hai điều kiện – (i) là **câu khẳng định**; (ii) tính đúng/sai "
          "**xác định được**. Câu hỏi, câu cảm thán, câu mệnh lệnh ⇒ **không** phải mệnh đề. "
          "Câu có chứa biến chưa gán giá trị ⇒ **mệnh đề chứa biến**, không phải mệnh đề."),
    ("box", "Ví dụ mẫu", [
        "**Ví dụ.** Trong các câu sau, câu nào là mệnh đề, câu nào là mệnh đề chứa biến?",
        "a) \"Số 2026 chia hết cho 2\".   b) \"n là số chẵn\".   c) \"Học Toán rất thú vị!\".",
        "**Giải.** a) Là mệnh đề (đúng, vì 2026 = 2·1013). b) Là mệnh đề chứa biến n. "
        "c) Là câu cảm thán ⇒ không phải mệnh đề.",
    ]),

    ("h3", "Dạng 2. Xét tính đúng – sai của mệnh đề"),
    ("p", "**Phương pháp:** với mệnh đề chứa ∀, phải kiểm tra **tất cả** (hoặc chứng minh); "
          "để bác bỏ một mệnh đề ∀, chỉ cần **chỉ ra một phản ví dụ**. Với mệnh đề chứa ∃, để chứng minh "
          "đúng chỉ cần **tìm một giá trị**; để bác bỏ phải chứng minh không có giá trị nào."),
    ("box", "Ví dụ mẫu", [
        "**Ví dụ.** Xét tính đúng – sai: a) \"∀n ∈ ℕ, n^{2} + n chia hết cho 2\"; "
        "b) \"∃x ∈ ℝ, x^{2} + 1 = 0\".",
        "**Giải.** a) **Đúng**, vì n^{2} + n = n(n + 1) là tích hai số tự nhiên liên tiếp nên luôn có "
        "một số chẵn. b) **Sai**, vì x^{2} ≥ 0 nên x^{2} + 1 ≥ 1 > 0 với mọi x.",
    ]),

    ("h3", "Dạng 3. Lập mệnh đề phủ định"),
    ("p", "**Phương pháp:** xác định đúng \"phần khẳng định\" của câu rồi phủ định phần đó. "
          "Với mệnh đề chứa ∀/∃, áp dụng quy tắc đổi lượng từ ở khung trên."),
    ("box", "Ví dụ mẫu", [
        "**Ví dụ.** Lập mệnh đề phủ định của: a) P: \"∀x ∈ ℝ, x^{2} − 2x + 2 > 0\"; "
        "b) Q: \"∃x ∈ ℚ, x^{2} = 2\".",
        "**Giải.** a) @P: \"∃x ∈ ℝ, x^{2} − 2x + 2 ≤ 0\" (mệnh đề này **sai**, vì "
        "x^{2} − 2x + 2 = (x − 1)^{2} + 1 > 0). b) @Q: \"∀x ∈ ℚ, x^{2} ≠ 2\" "
        "(mệnh đề này **đúng**, vì √2 là số vô tỉ).",
    ]),

    ("h3", "Dạng 4. Mệnh đề kéo theo, mệnh đề đảo, điều kiện cần – đủ"),
    ("p", "**Phương pháp:** phát biểu lại dưới dạng \"Nếu P thì Q\", sau đó xác định đâu là giả thiết P "
          "và đâu là kết luận Q. Nhớ: **P là điều kiện đủ, Q là điều kiện cần**."),
    ("box", "Ví dụ mẫu", [
        "**Ví dụ.** Cho định lí: \"Nếu một tứ giác là hình thoi thì hai đường chéo của nó vuông góc "
        "với nhau\". Phát biểu định lí dưới dạng điều kiện cần, điều kiện đủ.",
        "**Giải.** – Điều kiện **đủ** để hai đường chéo của tứ giác vuông góc với nhau là tứ giác đó "
        "là hình thoi. – Điều kiện **cần** để một tứ giác là hình thoi là hai đường chéo của nó vuông "
        "góc với nhau.",
        "__Lưu ý:__ mệnh đề đảo \"Nếu tứ giác có hai đường chéo vuông góc thì nó là hình thoi\" là "
        "**sai** (phản ví dụ: tứ giác có hai đường chéo vuông góc nhưng không phải hình thoi). Do đó "
        "định lí trên **không** thể phát biểu dạng \"khi và chỉ khi\".",
    ]),

    ("note", "Tổng kết mục 1.1: trong đề kiểm tra, dạng 1 và dạng 3 xuất hiện ở mức **nhận biết** "
             "(2 câu trắc nghiệm), dạng 2 và 4 ở mức **thông hiểu**."),

    ("h2", "1.2  Tập hợp"),
    ("mark", "toc1b"),

    ("h3", "1. Cách xác định một tập hợp"),
    ("p", "Một tập hợp được xác định bằng một trong hai cách:"),
    ("num", [
        "**Liệt kê các phần tử** của tập hợp, mỗi phần tử viết một lần, cách nhau bởi dấu \";\" "
        "(hoặc dấu \",\"). Ví dụ: A = {1; 2; 3; 5; 8}.",
        "**Chỉ ra tính chất đặc trưng** cho các phần tử của tập hợp. "
        "Ví dụ: B = {n ∈ ℕ | n là ước của 12} = {1; 2; 3; 4; 6; 12}.",
    ]),
    ("p", "Kí hiệu **a ∈ A** (a thuộc A, a là phần tử của A); **a ∉ A** (a không thuộc A). "
          "Số phần tử của tập hợp A kí hiệu là **n(A)**."),

    ("h3", "2. Tập hợp rỗng"),
    ("p", "**Tập hợp rỗng**, kí hiệu **∅**, là tập hợp **không chứa phần tử nào**. "
          "Một tập hợp chỉ có thể là rỗng hoặc chứa ít nhất một phần tử."),
    ("note", "Tập rỗng **không** viết là {∅}. Kí hiệu {∅} là tập hợp **có một phần tử** là tập rỗng, "
             "và n(∅) = 0 còn n({∅}) = 1."),

    ("h3", "3. Tập hợp con. Hai tập hợp bằng nhau"),
    ("p", "**A là tập con của B** (kí hiệu A ⊂ B, đọc là \"A chứa trong B\"), nếu **mọi phần tử của A "
          "đều là phần tử của B**."),
    ("eq", "A ⊂ B  ⇔  (∀x, x ∈ A ⇒ x ∈ B)"),
    ("p", "**Hai tập hợp bằng nhau** khi mỗi phần tử của tập này đều là phần tử của tập kia:"),
    ("eq", "A = B  ⇔  (A ⊂ B và B ⊂ A)"),
    ("box", "Ba tính chất của quan hệ tập con", [
        "**A ⊂ A** với mọi tập hợp A.",
        "**∅ ⊂ A** với mọi tập hợp A.",
        "Nếu **A ⊂ B** và **B ⊂ C** thì **A ⊂ C**.",
        "__Số tập con:__ nếu tập A có **n** phần tử thì A có tất cả **2^{n}** tập con (kể cả ∅ và chính A). "
        "Đặc biệt: số tập con **khác rỗng** là 2^{n} − 1; số tập con **có đúng k phần tử** là "
        "tổ hợp chập k của n.",
    ]),

    ("h3", "4. Các tập hợp số"),
    ("table",
     ["Kí hiệu", "Tên gọi", "Mô tả"],
     [
         ["ℕ*", "Tập số tự nhiên khác 0", "{1; 2; 3; 4; …}"],
         ["ℕ", "Tập số tự nhiên", "{0; 1; 2; 3; …}"],
         ["ℤ", "Tập số nguyên", "{…; −2; −1; 0; 1; 2; …}"],
         ["ℚ", "Tập số hữu tỉ", "Số viết được dạng a/b với a, b ∈ ℤ, b ≠ 0"],
         ["ℝ", "Tập số thực", "Toàn bộ trục số (gồm cả số vô tỉ như √2, π)"],
     ],
     [1.8, 4.6, 10],
     ["c", "l", "l"]),
    ("p", "Quan hệ bao hàm giữa các tập số: **ℕ* ⊂ ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ**."),

    ("h3", "5. Các khoảng, đoạn, nửa khoảng"),
    ("p", "Cho hai số thực a, b với **a < b**. Ta có bảng kí hiệu sau – học thuộc để không nhầm ngoặc:"),
    ("table",
     ["Tập hợp", "Kí hiệu", "Mô tả", "Trục số"],
     [
         ["{x ∈ ℝ | a < x < b}", "(a; b)", "**khoảng** (a; b)", "hai đầu **đều không lấy**"],
         ["{x ∈ ℝ | a ≤ x ≤ b}", "[a; b]", "**đoạn** [a; b]", "hai đầu **đều lấy**"],
         ["{x ∈ ℝ | a < x ≤ b}", "(a; b]", "**nửa khoảng**", "trái không lấy, phải lấy"],
         ["{x ∈ ℝ | a ≤ x < b}", "[a; b)", "**nửa khoảng**", "trái lấy, phải không lấy"],
         ["{x ∈ ℝ | x > a}", "(a; +∞)", "**khoảng**", "đầu a không lấy"],
         ["{x ∈ ℝ | x ≥ a}", "[a; +∞)", "**nửa khoảng**", "đầu a lấy"],
         ["{x ∈ ℝ | x < a}", "(−∞; a)", "**khoảng**", "đầu a không lấy"],
         ["{x ∈ ℝ | x ≤ a}", "(−∞; a]", "**nửa khoảng**", "đầu a lấy"],
         ["ℝ", "(−∞; +∞)", "cả trục số", "lấy toàn bộ"],
     ],
     [4.6, 2.6, 4.4, 5.0],
     ["l", "c", "l", "l"]),
    ("note", "__Mẹo nhớ ngoặc:__ ngoặc **tròn ( )** luôn đi với dấu **<  >** (không lấy đầu mút), "
             "ngoặc **vuông [ ]** luôn đi với dấu **≤ ≥** (lấy đầu mút). "
             "Kí hiệu **+∞** và **−∞** không phải là số nên **luôn** đi với ngoặc tròn."),

    ("img", "assets/truc-so.png", 12.5,
     "Hình 1. Biểu diễn A = [−3; 2), B = [1; +∞) và giao của chúng trên trục số"),

    ("h2", "1.3  Các phép toán trên tập hợp"),
    ("mark", "toc1c"),

    ("h3", "1. Giao của hai tập hợp"),
    ("p", "**Giao** của hai tập hợp A và B là tập hợp gồm các phần tử **vừa thuộc A, vừa thuộc B**:"),
    ("eq", "A ∩ B = {x | x ∈ A **và** x ∈ B}"),
    ("p", "Đọc là \"A giao B\". Điều kiện để x thuộc A ∩ B: x phải thỏa **đồng thời** cả hai.")

    ,
    ("h3", "2. Hợp của hai tập hợp"),
    ("p", "**Hợp** của hai tập hợp A và B là tập hợp gồm các phần tử **thuộc A hoặc thuộc B** "
          "(hoặc thuộc cả hai):"),
    ("eq", "A ∪ B = {x | x ∈ A **hoặc** x ∈ B}"),
    ("p", "Đọc là \"A hợp B\". Lưu ý trong toán học, chữ \"hoặc\" ở đây **không loại trừ**: "
          "một phần tử thuộc cả A và B vẫn thuộc A ∪ B."),

    ("h3", "3. Hiệu và phần bù của hai tập hợp"),
    ("p", "**Hiệu** của A và B, kí hiệu **A \\ B**, là tập hợp gồm các phần tử **thuộc A nhưng không "
          "thuộc B**:"),
    ("eq", "A \\ B = {x | x ∈ A **và** x ∉ B}"),
    ("p", "Nếu **B ⊂ A** thì **A \\ B** được gọi là **phần bù của B trong A**, kí hiệu **C_{A}B**."),
    ("box", "Phân biệt nhanh bằng biểu đồ Ven", [
        "**A ∩ B**: chỉ lấy phần **chồng lên nhau** của hai vòng tròn.",
        "**A ∪ B**: lấy **toàn bộ** cả hai vòng tròn.",
        "**A \\ B**: lấy phần của A **nằm ngoài** B (\"A mà không có B\").",
        "**C_{A}B** (với B ⊂ A): phần của A nằm **ngoài** B – chính là A \\ B.",
    ]),
    ("img", "assets/ven.png", 13.6,
     "Hình 2. Biểu đồ Ven của A ∩ B (phần tô đậm) và A ∪ B"),

    ("h3", "4. Cách tìm giao, hợp, hiệu bằng trục số"),
    ("p", "Với các tập là khoảng, đoạn, nửa khoảng, cách nhanh và chính xác nhất là **vẽ trục số**:"),
    ("num", [
        "Vẽ trục số, biểu diễn tập A bằng một **đoạn tô đậm** ở dòng trên cùng (dùng ngoặc tròn/vuông "
        "cho đầu mút).",
        "Biểu diễn tập B bằng một đoạn tô đậm ở **dòng thứ hai**.",
        "Nhìn theo **phương thẳng đứng**, đọc kết quả:",
    ]),
    ("bullets", [
        "**Giao A ∩ B** = chỗ mà **cả hai dòng cùng tô đậm**.",
        "**Hợp A ∪ B** = chỗ mà **ít nhất một dòng tô đậm**.",
        "**Hiệu A \\ B** = chỗ **chỉ có dòng A tô đậm** (và dòng B không tô).",
    ]),
    ("box", "Ba lỗi cực kì thường gặp khi làm phép toán trên tập hợp", [
        "**1. Nhầm (a; b) với [a; b].** Ví dụ A = (1; 3] và B = [3; 5) thì A ∩ B = **∅**, "
        "vì 3 không thuộc A. Nếu viết A ∩ B = {3} là **sai**.",
        "**2. Quên chiều của bất phương trình khi tập cho bởi điều kiện.** "
        "Tập {x | 2x − 1 < 5} phải rút gọn thành {x | x < 3} = (−∞; 3) **trước khi** làm phép toán.",
        "**3. Lẫn A \\ B với B \\ A.** Phép hiệu **không** có tính giao hoán: "
        "A \\ B ≠ B \\ A nói chung.",
    ]),

    ("h2", "Các dạng toán thường gặp – Tập hợp"),

    ("h3", "Dạng 1. Viết tập hợp bằng cách liệt kê"),
    ("box", "Ví dụ mẫu", [
        "**Ví dụ.** Viết các tập hợp sau bằng cách liệt kê phần tử: "
        "a) A = {x ∈ ℕ | x < 5};   b) B = {x ∈ ℤ | −3 ≤ x < 2};   c) C = {x ∈ ℝ | x^{2} − 3x + 2 = 0}.",
        "**Giải.** a) A = {0; 1; 2; 3; 4}. — Lưu ý **x ∈ ℕ** nên có số **0**.",
        "b) B = {−3; −2; −1; 0; 1}. — Lưu ý **x ∈ ℤ** nên có số âm, nhưng x < 2 nên **không** có 2.",
        "c) C = {1; 2}. — Giải phương trình: x^{2} − 3x + 2 = 0 ⇔ x = 1 hoặc x = 2.",
    ]),

    ("h3", "Dạng 2. Xác định tập con và số tập con"),
    ("box", "Ví dụ mẫu", [
        "**Ví dụ.** Cho tập A = {1; 2; 3}. Liệt kê các tập con của A và kiểm tra công thức.",
        "**Giải.** A có 3 phần tử nên có 2^{3} = 8 tập con: ∅; {1}; {2}; {3}; {1; 2}; {1; 3}; {2; 3}; "
        "{1; 2; 3}. Số tập con khác rỗng là 7.",
        "__Áp dụng thi:__ với câu trả lời ngắn \"tìm số tập con\", chỉ cần đếm số phần tử n của tập rồi "
        "tính 2^{n}. Nếu đề hỏi tập con có đúng 2 phần tử thì đáp án là C(n; 2) = n(n − 1)/2.",
    ]),

    ("h3", "Dạng 3. Tìm giao, hợp, hiệu của các khoảng – đoạn"),
    ("box", "Ví dụ mẫu", [
        "**Ví dụ.** Cho A = [−3; 2) và B = [1; +∞). Tìm A ∩ B, A ∪ B, A \\ B, B \\ A và C_{ℝ}A.",
        "**Giải.** Vẽ trục số (Hình 1):",
        "• **A ∩ B** = [1; 2) — phần cả hai cùng tô.",
        "• **A ∪ B** = [−3; +∞) — phần ít nhất một tập tô.",
        "• **A \\ B** = [−3; 1) — phần của A nằm ngoài B.",
        "• **B \\ A** = [2; +∞) — phần của B nằm ngoài A.",
        "• **C_{ℝ}A** = (−∞; −3) ∪ [2; +∞) — phần bù của A trong ℝ (điểm 2 vẫn bị loại vì 2 ∉ A).",
    ]),

    ("h3", "Dạng 4. Toán thực tế dùng phép toán tập hợp"),
    ("p", "Đây là dạng bài **chắc chắn** xuất hiện ở câu trả lời ngắn thứ hai. Công thức cốt lõi:"),
    ("eq", "n(A ∪ B) = n(A) + n(B) − n(A ∩ B)"),
    ("p", "Công thức này đúng cho **mọi** hai tập hợp hữu hạn, kể cả khi chúng rời nhau "
          "(khi đó n(A ∩ B) = 0)."),
    ("box", "Ví dụ mẫu", [
        "**Ví dụ.** Lớp 10A có 40 học sinh. Trong đó có 25 học sinh thích môn Toán, 20 học sinh thích "
        "môn Văn, 10 học sinh thích cả hai môn. Hỏi có bao nhiêu học sinh **không** thích môn nào?",
        "**Giải.** Gọi A là tập học sinh thích Toán, B là tập học sinh thích Văn. "
        "Số học sinh thích ít nhất một môn: n(A ∪ B) = 25 + 20 − 10 = **35**.",
        "Số học sinh không thích môn nào: 40 − 35 = **5** học sinh.",
        "__Kiểm tra lại bằng sơ đồ:__ chỉ thích Toán = 25 − 10 = 15; chỉ thích Văn = 20 − 10 = 10; "
        "thích cả hai = 10. Tổng = 15 + 10 + 10 = 35 ✔.",
    ]),
    ("h3", "Dạng 5. Tìm tham số để A ∩ B = ∅ hoặc A ⊂ B"),
    ("p", "**Phương pháp:** vẽ trục số, biểu diễn hai tập theo tham số m, rồi **so sánh các đầu mút**. "
          "Đây là dạng khó nhất của chương, thường ở mức vận dụng."),
    ("box", "Ví dụ mẫu", [
        "**Ví dụ.** Cho A = (m; m + 2) và B = (−1; 3). Tìm m để A ⊂ B.",
        "**Giải.** A là khoảng có độ dài 2. Điều kiện A ⊂ B: "
        "**m ≥ −1** và **m + 2 ≤ 3**, tức **−1 ≤ m ≤ 1**. Vậy m ∈ [−1; 1].",
        "__Cẩn thận:__ nếu A không phải khoảng (ví dụ A = (m; m + 2) luôn khác rỗng vì 2 > 0), "
        "còn với A = [m; m] thì A = {m} luôn khác rỗng. Riêng A = (m; m) = ∅ nên ∅ ⊂ B luôn đúng "
        "với mọi m.",
    ]),
]


# --------------------------------------------------------------------------
# Bổ sung cuối chương I: sơ đồ tư duy + bài tập tự luyện
# --------------------------------------------------------------------------
PART1_EXTRA = [
    ("h2", "Sơ đồ tư duy chương I"),
    ("p", "Hãy học theo sơ đồ: từ **hai khái niệm gốc** là __mệnh đề__ và __tập hợp__ mà mọi dạng bài "
          "đều được suy ra."),
    ("table",
     ["Nhánh lớn", "Các nhánh con", "Dạng bài tương ứng"],
     [
         ["**Mệnh đề**",
          "khái niệm • phủ định • chứa biến • kéo theo/đảo/tương đương • ∀, ∃",
          "Nhận biết mệnh đề; phủ định; điều kiện cần – đủ; xét đúng sai"],
         ["**Tập hợp**",
          "liệt kê / tính chất đặc trưng • tập con • tập bằng nhau • tập rỗng • khoảng – đoạn",
          "Viết tập hợp; số tập con; biểu diễn trên trục số"],
         ["**Phép toán**",
          "giao ∩ • hợp ∪ • hiệu \\ • phần bù C_{A}B",
          "Tìm giao, hợp, hiệu; bài toán thực tế n(A ∪ B)"],
     ],
     [3.4, 7.6, 5.6],
     ["l", "l", "l"]),

    ("h2", "Bài tập tự luyện chương I"),
    ("p", "Làm trước, rồi mới xem đáp số ở cuối mục. Mỗi bài tương ứng một dạng vừa học."),
    ("bullets", [
        "**Bài 1.** Trong các câu sau, câu nào là mệnh đề? "
        "a) \"17 là số nguyên tố\".  b) \"2n là số chẵn\".  c) \"Đẹp quá!\".  d) \"5 − 3 = 1\".",
        "**Bài 2.** Lập mệnh đề phủ định của: a) P: \"∀x ∈ ℝ, x^{2} + x + 1 > 0\"; "
        "b) Q: \"∃n ∈ ℕ, n^{2} = n\".",
        "**Bài 3.** Cho định lí \"Nếu tứ giác ABCD là hình chữ nhật thì nó có hai đường chéo bằng "
        "nhau\". Phát biểu dưới dạng điều kiện cần, điều kiện đủ.",
        "**Bài 4.** Viết các tập hợp sau bằng cách liệt kê: "
        "a) A = {x ∈ ℕ | x ≤ 6};  b) B = {x ∈ ℤ | −2 ≤ x < 3};  c) C = {x ∈ ℝ | x^{2} − 5x + 6 = 0}.",
        "**Bài 5.** Cho A = {a; b; c}. Liệt kê các tập con của A và cho biết A có bao nhiêu tập con.",
        "**Bài 6.** Cho A = [−4; 3) và B = (0; 5]. Tìm A ∩ B, A ∪ B, A \\ B, B \\ A.",
        "**Bài 7.** Lớp 10B có 38 học sinh; 22 em tham gia câu lạc bộ Toán, 16 em tham gia câu lạc bộ "
        "Tiếng Anh, 8 em tham gia cả hai. Hỏi có bao nhiêu em không tham gia câu lạc bộ nào?",
        "**Bài 8.** Cho A = [m; m + 3] và B = (1; 6). Tìm m để A ⊂ B.",
    ]),
    ("box", "Đáp số và gợi ý", [
        "**Bài 1.** a) Là mệnh đề (đúng).  b) Là **mệnh đề chứa biến** (chưa gán n).  "
        "c) Không (câu cảm thán).  d) Là mệnh đề (sai).",
        "**Bài 2.** a) @P: \"∃x ∈ ℝ, x^{2} + x + 1 ≤ 0\" (mệnh đề này **sai**, vì "
        "x^{2} + x + 1 = (x + ½)^{2} + ¾ > 0).  b) @Q: \"∀n ∈ ℕ, n^{2} ≠ n\" (__sai__, vì n = 0 và n = 1 "
        "đều thỏa n^{2} = n).",
        "**Bài 3.** Điều kiện **đủ** để tứ giác ABCD có hai đường chéo bằng nhau là ABCD là hình chữ "
        "nhật. Điều kiện **cần** để ABCD là hình chữ nhật là nó có hai đường chéo bằng nhau.",
        "**Bài 4.** a) A = {0; 1; 2; 3; 4; 5; 6}.  b) B = {−2; −1; 0; 1; 2}.  "
        "c) C = {2; 3} (vì x^{2} − 5x + 6 = 0 ⇔ x = 2 hoặc x = 3).",
        "**Bài 5.** 8 tập con: ∅; {a}; {b}; {c}; {a; b}; {a; c}; {b; c}; {a; b; c}.",
        "**Bài 6.** A ∩ B = **(0; 3)**;  A ∪ B = **[−4; 5]**;  A \\ B = **[−4; 0]**;  "
        "B \\ A = **[3; 5]**. __(Kiểm tra: 0 ∈ A và 0 ∉ B nên 0 ∈ A \\ B; 3 ∉ A nên 3 ∈ B \\ A.)__",
        "**Bài 7.** n(A ∪ B) = 22 + 16 − 8 = **30** ⇒ số em không tham gia câu lạc bộ nào: "
        "38 − 30 = **8** (em).",
        "**Bài 8.** Cần **m ≥ 1** và **m + 3 ≤ 6** ⇒ **1 ≤ m ≤ 3**.",
    ]),
]
