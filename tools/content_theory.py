# -*- coding: utf-8 -*-
"""PHẦN A – Tóm tắt lý thuyết trọng tâm (4 chương)."""
from reportlab.lib.units import cm
from reportlab.platypus import CondPageBreak, KeepTogether, PageBreak, Spacer

from pdfkit import (
    BLUE, CONTENT_W, ChapterBanner, GOLD, NAVY, RED, SectionBanner, TEAL,
    TINT_BLUE, TINT_GOLD, bullets, callout, data_table, key_table, method,
    note, P, S, side, spacing, tip, warn,
)
from pdfkit import Table, TableStyle
from reportlab.lib import colors
import figures

from build_pdf import chapter


def story():
    st = []
    st.append(CondPageBreak(12.5 * cm))
    st.append(SectionBanner("PHẦN A", "Tóm tắt lý thuyết trọng tâm", TEAL))
    st.append(spacing(0.3))
    st.append(P(
        "Phần này cô đọng toàn bộ lý thuyết của 4 chương có trong đề. Mỗi mục gồm: "
        "<b>định nghĩa – tính chất – công thức</b> và những lưu ý dễ mất điểm. "
        "Các em nên học theo đúng thứ tự vì kiến thức được xây dựng liên tục."))

    st += _ch1()
    st += _ch2()
    st += _ch3()
    st += _ch4()
    return st


# ==========================================================================
# CHƯƠNG 1
# ==========================================================================
def _ch1():
    st = []
    st += chapter("1", "Mệnh đề và tập hợp",
                  "Mệnh đề • Tập hợp • Các phép toán trên tập hợp", NAVY)

    st.append(P(
        "Đây là chương <b>chiếm nhiều điểm nhất</b> trong đề (4,0/10 điểm, gồm cả 1 câu tự luận). "
        "Kiến thức không khó nhưng đòi hỏi sự chính xác tuyệt đối về kí hiệu – đặc biệt là "
        "ngoặc tròn/ngoặc vuông khi làm việc với các khoảng, đoạn."))

    # ---------------- 1.1 ----------------
    st.append(P("1.1. Mệnh đề. Mệnh đề chứa biến", "h2"))

    st.append(P("<b>a) Mệnh đề</b>", "h3"))
    st.append(P(
        "<b>Mệnh đề</b> (gọi tắt là <i>mệnh đề</i>) là một câu khẳng định <b>đúng</b> hoặc <b>sai</b>. "
        "Một câu không thể vừa đúng vừa sai, cũng không thể không đúng cũng không sai."))
    st.append(P(
        "Người ta dùng chữ cái in hoa P, Q, R, … để kí hiệu mệnh đề. Mệnh đề đúng có giá trị chân lí "
        "là <b>Đ</b> (đúng), mệnh đề sai có giá trị chân lí là <b>S</b> (sai)."))

    st.append(note([
        P("Những câu <b>không phải</b> mệnh đề:", "small"),
        P("• Câu hỏi: “Bạn có thích học Toán không?”", "small"),
        P("• Câu cảm thán: “Ôi, đẹp quá!”", "small"),
        P("• Câu mệnh lệnh, đề nghị: “Hãy nộp bài”, “Cho tôi xin quyển vở”.", "small"),
        P("• Câu chứa biến chưa được gán giá trị: “x + 1 &gt; 2”, “n là số chẵn”.", "small"),
    ], title="Phân biệt mệnh đề với các câu khác", icon="★"))

    st.append(P("<b>b) Mệnh đề chứa biến</b>", "h3"))
    st.append(P(
        "Câu khẳng định chứa một hay nhiều biến nhận giá trị trong một tập hợp nào đó mà "
        "<b>bản thân câu đó chưa xác định được đúng hay sai</b> gọi là <b>mệnh đề chứa biến</b>."))
    st.append(P(
        "Ví dụ: P(x): “x &gt; 3” với x là số thực. Ta có P(4) là mệnh đề <b>đúng</b>, P(1) là mệnh đề "
        "<b>sai</b>. Như vậy, mỗi giá trị cụ thể của biến biến mệnh đề chứa biến thành một mệnh đề."))

    st.append(P("<b>c) Mệnh đề phủ định</b>", "h3"))
    st.append(P(
        "Mệnh đề phủ định của mệnh đề P, kí hiệu là <b>¬P</b> (đọc là “không P”; khi viết tay, các em có "
        "thể viết P kèm một gạch ngang ở trên đầu), là mệnh đề khẳng định P không xảy ra. Để lập mệnh đề "
        "phủ định, ta thêm (hoặc bớt) từ “không”, “không phải” vào trước vị ngữ của mệnh đề."))
    st.append(P(
        "Tính chất: <b>P đúng thì ¬P sai; P sai thì ¬P đúng.</b> Do đó phủ định của phủ định "
        "chính là mệnh đề ban đầu."))
    st.append(P(
        "Ví dụ: P: “5 là số nguyên tố” (đúng) ⇒ ¬P: “5 không phải là số nguyên tố” (sai)."))

    st.append(P("<b>d) Mệnh đề kéo theo</b>", "h3"))
    st.append(P(
        "Mệnh đề “Nếu P thì Q” được gọi là <b>mệnh đề kéo theo</b>, kí hiệu <b>P ⇒ Q</b>. "
        "Mệnh đề P ⇒ Q chỉ <b>sai khi P đúng và Q sai</b>; đúng trong mọi trường hợp còn lại."))

    truth = data_table(
        ["P", "Q", "P ⇒ Q"],
        [["Đúng", "Đúng", "<b>Đúng</b>"],
         ["Đúng", "Sai", "<font color='#A33E30'><b>Sai</b></font>"],
         ["Sai", "Đúng", "<b>Đúng</b>"],
         ["Sai", "Sai", "<b>Đúng</b>"]],
        widths=[3.0 * cm, 3.0 * cm, 3.0 * cm], align_center_cols=[0, 1, 2])
    st.append(KeepTogether([
        P("Bảng giá trị chân lí của mệnh đề kéo theo:", "small"),
        truth,
        P("Chỉ có <b>một</b> trường hợp mệnh đề kéo theo sai: <i>giả thiết đúng nhưng kết luận sai</i>.",
          "caption"),
    ]))

    st.append(P(
        "Với mệnh đề P ⇒ Q ta có các cách phát biểu tương đương: “P kéo theo Q”, “P suy ra Q”, "
        "“Nếu P thì Q”, “P là điều kiện đủ để có Q”, “Q là điều kiện cần để có P”."))
    st.append(note([
        P("• <b>P là điều kiện đủ</b> để có Q (có P là đủ để có Q).", "small"),
        P("• <b>Q là điều kiện cần</b> để có P (muốn có P thì cần có Q).", "small"),
    ], color=GOLD, bg=TINT_GOLD, title="Điều kiện cần – điều kiện đủ", icon="★"))

    st.append(P("<b>e) Mệnh đề đảo. Mệnh đề tương đương</b>", "h3"))
    st.append(P(
        "Mệnh đề <b>Q ⇒ P</b> gọi là <b>mệnh đề đảo</b> của mệnh đề P ⇒ Q. "
        "Nếu cả P ⇒ Q và Q ⇒ P đều đúng thì ta nói P và Q là hai mệnh đề <b>tương đương</b>, "
        "kí hiệu <b>P ⇔ Q</b> (đọc là “P khi và chỉ khi Q”, “P nếu và chỉ nếu Q”, "
        "“P là điều kiện cần và đủ để có Q”)."))
    st.append(warn([
        P("Mệnh đề P ⇒ Q đúng <b>không</b> suy ra được mệnh đề đảo Q ⇒ P đúng. "
          "Ví dụ: “Nếu tứ giác ABCD là hình vuông thì ABCD là hình chữ nhật” là mệnh đề đúng, "
          "nhưng mệnh đề đảo “Nếu ABCD là hình chữ nhật thì ABCD là hình vuông” là mệnh đề <b>sai</b>. "
          "Đây là bẫy rất hay xuất hiện trong câu hỏi trắc nghiệm.", "small")]))

    st.append(P("<b>f) Kí hiệu ∀ và ∃</b>", "h3"))
    sym = data_table(
        ["Kí hiệu", "Cách đọc", "Ý nghĩa", "Mệnh đề phủ định"],
        [["<b>∀</b>", "với mọi, với tất cả", "Mệnh đề đúng khi <b>mọi</b> phần tử đều thoả mãn",
          "∃ (đổi ∀ thành ∃, lấy phủ định vị ngữ)"],
         ["<b>∃</b>", "tồn tại, có ít nhất một", "Mệnh đề đúng khi <b>có ít nhất một</b> phần tử thoả mãn",
          "∀ (đổi ∃ thành ∀, lấy phủ định vị ngữ)"]],
        widths=[1.6 * cm, 3.4 * cm, 5.3 * cm, 6.5 * cm], align_center_cols=[0])
    st.append(sym)

    st.append(spacing(0.15))
    st.append(note([
        P("<b>Quy tắc phủ định mệnh đề có kí hiệu:</b>", "small"),
        P("Phủ định của “∀x ∈ X, P(x)” là “∃x ∈ X, ¬P(x)”.", "small"),
        P("Phủ định của “∃x ∈ X, P(x)” là “∀x ∈ X, ¬P(x)”.", "small"),
        P("Nói cách khác: <b>đổi lượng từ (∀ ↔ ∃) và phủ định mệnh đề chứa biến</b>.", "small"),
    ], title="Công thức phủ định – câu hỏi gần như chắc chắn có trong đề", icon="★"))

    st.append(P(
        "Ví dụ: P: “∀x ∈ ℝ, x² ≥ 0” (đúng) ⇒ ¬P: “∃x ∈ ℝ, x² &lt; 0” (sai). "
        "Q: “∃n ∈ ℕ, n² = 4” (đúng) ⇒ ¬Q: “∀n ∈ ℕ, n² ≠ 4” (sai)."))

    # ---------------- 1.2 ----------------
    st.append(CondPageBreak(10.2 * cm))
    st.append(P("1.2. Tập hợp", "h2"))

    st.append(P("<b>a) Tập hợp và phần tử</b>", "h3"))
    st.append(P(
        "Tập hợp là một khái niệm cơ bản của toán học, không có định nghĩa. Các đối tượng trong "
        "tập hợp gọi là <b>phần tử</b> của tập hợp. Nếu a là phần tử của tập hợp A, ta viết "
        "<b>a ∈ A</b> (đọc: “a thuộc A”); nếu không, viết <b>a ∉ A</b> (đọc: “a không thuộc A”)."))

    st.append(P("<b>b) Hai cách xác định một tập hợp</b>", "h3"))
    st.extend(bullets([
        "<b>Liệt kê các phần tử</b>: A = {1; 2; 3; 4; 5}. Các phần tử ngăn cách bởi dấu “;”. "
        "Mỗi phần tử chỉ liệt kê một lần, thứ tự không quan trọng.",
        "<b>Chỉ ra tính chất đặc trưng</b>: A = {x ∈ ℕ | x &lt; 6}, đọc là “tập hợp các số tự nhiên x "
        "sao cho x &lt; 6”. Dấu “|” đọc là “sao cho” hoặc “thoả mãn”.",
    ], bullet="▸"))

    st.append(note([
        P("Khi một tập hợp có <b>rất nhiều</b> phần tử, ta <b>không được</b> dùng dấu “…” trong bài kiểm tra "
          "nếu chưa chỉ rõ quy luật; hãy dùng cách chỉ ra tính chất đặc trưng.", "small"),
    ], color=BLUE, bg=TINT_BLUE, title="Lưu ý", icon="★"))

    st.append(P("<b>c) Tập hợp rỗng</b>", "h3"))
    st.append(P(
        "<b>Tập hợp rỗng</b>, kí hiệu <b>∅</b>, là tập hợp không có phần tử nào. "
        "Một tập hợp không phải tập rỗng nếu nó có ít nhất một phần tử."))
    st.append(P("Ví dụ: A = {x ∈ ℝ | x² + 1 = 0} = ∅ (vì x² + 1 &gt; 0 với mọi x)."))
    st.append(warn([
        P("Không được viết ∅ = {0} hay ∅ = {∅}. Tập hợp {0} có <b>một</b> phần tử là số 0.",
          "small")]))

    st.append(P("<b>d) Tập hợp con</b>", "h3"))
    st.append(P(
        "Tập hợp A được gọi là <b>tập con</b> của tập hợp B nếu mọi phần tử của A đều là phần tử của B, "
        "kí hiệu <b>A ⊂ B</b> (đọc: “A là tập con của B”, “A chứa trong B”, “B chứa A”)."))
    st.append(P(
        "A ⊂ B ⇔ (∀x, x ∈ A ⇒ x ∈ B). Nếu A không phải tập con của B, ta viết A ⊄ B."))

    st.append(note([
        P("Với mọi tập hợp A, ta luôn có:", "small"),
        P("• <b>∅ ⊂ A</b> và <b>A ⊂ A</b> (tập rỗng là con của mọi tập, mọi tập là con của chính nó).", "small"),
        P("• Nếu A ⊂ B và B ⊂ C thì <b>A ⊂ C</b> (tính chất bắc cầu).", "small"),
        P("• Tập hợp có n phần tử (n ≥ 1) có <b>2<super>n</super></b> tập con, trong đó có "
          "<b>2<super>n</super> − 1</b> tập con khác rỗng.", "small"),
        P("• A ⊂ B và B ⊂ A ⇔ A = B (hai tập hợp bằng nhau).", "small"),
    ], title="Tính chất tập con và số tập con", icon="★"))

    st.append(P(
        "Ví dụ: A = {1; 2; 3} có 2³ = 8 tập con là: ∅, {1}, {2}, {3}, {1; 2}, {1; 3}, {2; 3}, {1; 2; 3}."))

    st.append(P("<b>e) Hai tập hợp bằng nhau</b>", "h3"))
    st.append(P(
        "Hai tập hợp A và B gọi là <b>bằng nhau</b> nếu mỗi phần tử của A là phần tử của B và ngược lại, "
        "tức là <b>A ⊂ B và B ⊂ A</b>. Khi đó ta viết A = B."))
    st.append(tip([
        P("Thứ tự liệt kê và việc lặp lại phần tử không làm thay đổi tập hợp: "
          "{1; 2; 3} = {3; 1; 2} = {1; 1; 2; 3}. Nhưng <b>(1; 2) ≠ [1; 2]</b> – đây là hai tập con "
          "khác nhau của ℝ (xem mục 1.3).", "small")]))

    # ---------------- 1.3 ----------------
    st.append(CondPageBreak(10.2 * cm))
    st.append(P("1.3. Các tập con thường dùng của ℝ và các phép toán trên tập hợp", "h2"))

    st.append(P("<b>a) Các tập con thường dùng của ℝ</b>", "h3"))
    st.append(P(
        "Cho a, b là hai số thực với a &lt; b. Ta có các tập hợp sau (gọi chung là <b>khoảng</b>, "
        "<b>đoạn</b>, <b>nửa khoảng</b>):"))

    intervals = data_table(
        ["Kí hiệu", "Tên gọi", "Tập hợp tương ứng", "Trên trục số"],
        [["(a; b)", "khoảng", "{x ∈ ℝ | a &lt; x &lt; b}", "bỏ cả hai đầu mút"],
         ["[a; b]", "đoạn", "{x ∈ ℝ | a ≤ x ≤ b}", "lấy cả hai đầu mút"],
         ["(a; b]", "nửa khoảng", "{x ∈ ℝ | a &lt; x ≤ b}", "bỏ a, lấy b"],
         ["[a; b)", "nửa khoảng", "{x ∈ ℝ | a ≤ x &lt; b}", "lấy a, bỏ b"],
         ["(−∞; a)", "khoảng", "{x ∈ ℝ | x &lt; a}", "tia trái, bỏ a"],
         ["(−∞; a]", "nửa khoảng", "{x ∈ ℝ | x ≤ a}", "tia trái, lấy a"],
         ["(a; +∞)", "khoảng", "{x ∈ ℝ | x &gt; a}", "tia phải, bỏ a"],
         ["[a; +∞)", "nửa khoảng", "{x ∈ ℝ | x ≥ a}", "tia phải, lấy a"],
         ["(−∞; +∞)", "khoảng", "ℝ", "toàn bộ trục số"]],
        widths=[2.4 * cm, 2.6 * cm, 5.4 * cm, 6.4 * cm], align_center_cols=[0, 1])
    st.append(intervals)

    st.append(spacing(0.15))
    st.append(note([
        P("• Luôn dùng <b>ngoặc tròn</b> cho −∞ và +∞ (không bao giờ viết [−∞; a] hay [a; +∞]).", "small"),
        P("• Ngoặc <b>vuông</b> ⇔ <b>có dấu “=”</b> ⇔ điểm đó <b>thuộc</b> tập hợp (trên trục số: chấm đặc).", "small"),
        P("• Ngoặc <b>tròn</b> ⇔ <b>không có dấu “=”</b> ⇔ điểm đó <b>không thuộc</b> tập hợp (trên trục số: chấm rỗng).", "small"),
    ], title="Quy tắc ngoặc tròn – ngoặc vuông", icon="★"))

    st.append(KeepTogether([
        P("Ví dụ biểu diễn trên trục số:", "small"),
        figures.number_line(
            width=CONTENT_W - 10, height=98,
            marks=[(-4, "−4"), (-1, "−1"), (0, "0"), (1, "1"), (2, "2"), (3, "3"), (4.5, "4,5")],
            intervals=[
                (-1, 3, True, False, BLUE, "[−1; 3)", 0),
                (2, None, True, None, RED, "[2; +∞)", 1),
                (None, 0, None, False, TEAL, "(−∞; 0)", 2),
            ],
            xmin=-4.6, xmax=5.0,
            caption="Hình A.1. Ba tập hợp số biểu diễn trên trục số (chấm đặc = lấy, chấm rỗng = bỏ)"),
    ]))

    st.append(KeepTogether([P("<b>b) Giao của hai tập hợp</b>", "h3"), side([
        P("Tập hợp gồm các phần tử <b>vừa thuộc A vừa thuộc B</b> gọi là giao của A và B, "
          "kí hiệu <b>A ∩ B</b>.", "small"),
        P("<b>A ∩ B = {x | x ∈ A và x ∈ B}</b>", "formula"),
        P("Ví dụ: A = {1; 2; 3}, B = {2; 3; 4} ⇒ A ∩ B = {2; 3}.", "small"),
        P("Quy tắc nhớ: <b>giao</b> là phần <b>chung</b> – muốn thuộc giao phải thoả mãn "
          "<b>tất cả</b> các tập.", "small"),
    ], figures.venn_intersection(width=215, height=118), text_ratio=0.615)]))

    st.append(KeepTogether([P("<b>c) Hợp của hai tập hợp</b>", "h3"), side([
        P("Tập hợp gồm các phần tử <b>thuộc A hoặc thuộc B</b> (thuộc ít nhất một trong hai tập) "
          "gọi là hợp của A và B, kí hiệu <b>A ∪ B</b>.", "small"),
        P("<b>A ∪ B = {x | x ∈ A hoặc x ∈ B}</b>", "formula"),
        P("Ví dụ: A = {1; 2; 3}, B = {2; 3; 4} ⇒ A ∪ B = {1; 2; 3; 4}.", "small"),
        P("Quy tắc nhớ: <b>hợp</b> là <b>tất cả</b> – chỉ cần thoả mãn <b>một</b> trong các tập.", "small"),
    ], figures.venn_union(width=215, height=118), text_ratio=0.615)]))

    st.append(P("<b>d) Hiệu và phần bù của hai tập hợp</b>", "h3"))
    st.append(side([
        P("Tập hợp gồm các phần tử <b>thuộc A nhưng không thuộc B</b> gọi là hiệu của A và B, "
          "kí hiệu <b>A \\ B</b>.", "small"),
        P("<b>A \\ B = {x | x ∈ A và x ∉ B}</b>", "formula"),
        P("Đặc biệt, khi <b>B ⊂ A</b> thì A \\ B được gọi là <b>phần bù của B trong A</b>, "
          "kí hiệu <b>C<sub>A</sub>B</b>. Vậy C<sub>A</sub>B = A \\ B (chỉ định nghĩa khi B ⊂ A).",
          "small"),
        P("Ví dụ: A = {1; 2; 3}, B = {2; 3; 4} ⇒ A \\ B = {1}; B \\ A = {4}.", "small"),
    ], figures.venn_difference(width=215, height=118), text_ratio=0.615))

    st.append(spacing(0.2))
    st.append(KeepTogether([note([
        P("• <b>Giao</b> → lấy phần <b>chung</b> (phải thoả mãn <i>tất cả</i>).", "small"),
        P("• <b>Hợp</b> → lấy <b>tất cả</b> (chỉ cần thoả mãn <i>một</i>).", "small"),
        P("• <b>Hiệu A \\ B</b> → lấy phần của A, <b>bỏ đi</b> phần nằm trong B.", "small"),
        P("• <b>Phần bù</b> C<sub>A</sub>B chính là A \\ B, với điều kiện B ⊂ A.", "small"),
        P("Với mọi tập A, B: A ∩ B ⊂ A ⊂ A ∪ B và A ∩ B ⊂ B ⊂ A ∪ B.", "small"),
    ], title="Phân biệt bốn phép toán – dễ nhầm nhất", icon="★"), spacing(0.15)]))

    st.append(P("<b>e) Quy trình tìm giao – hợp – hiệu của các khoảng, đoạn</b>", "h3"))
    st.append(method([
        P("<b>Bước 1.</b> Vẽ tất cả các tập hợp đã cho lên <b>cùng một trục số</b>, mỗi tập một dòng, "
          "dùng chấm đặc cho đầu mút lấy được và chấm rỗng cho đầu mút không lấy được.", "small"),
        P("<b>Bước 2.</b> Với <b>giao</b>: giữ lại những đoạn có <b>đủ tất cả</b> các đường "
          "(kể cả các đường giới hạn bởi nửa đường thẳng).", "small"),
        P("<b>Bước 3.</b> Với <b>hợp</b>: giữ lại những đoạn có <b>ít nhất một</b> đường.", "small"),
        P("<b>Bước 4.</b> Với <b>hiệu A \\ B</b>: giữ phần của A nằm <b>ngoài</b> B.", "small"),
        P("<b>Bước 5.</b> Đọc kết quả và <b>kiểm tra lại ngoặc</b> ở hai đầu mút: đầu mút thuộc kết quả "
          "khi nó thuộc <i>tất cả</i> các tập tham gia (với giao) hoặc thuộc tập nguồn (với hiệu).", "small"),
    ]))

    st.append(P(
        "Ví dụ: Cho A = [−2; 3) và B = (1; 5]. Khi đó A ∩ B = (1; 3), A ∪ B = [−2; 5], "
        "A \\ B = [−2; 1], B \\ A = [3; 5]. Hãy tự kiểm tra bằng cách vẽ trục số."))

    return st


# ==========================================================================
# CHƯƠNG 2
# ==========================================================================
def _ch2():
    st = []
    st += chapter("2", "Bất phương trình và hệ bất phương trình bậc nhất hai ẩn",
                  "Miền nghiệm • Biểu diễn hình học • Bài toán tối ưu", TEAL)

    st.append(P(
        "Chương này chiếm 2,5 điểm, trong đó câu tự luận số 3 là câu <b>Vận dụng cao</b> duy nhất của đề. "
        "Phần lớn điểm nằm ở kĩ năng <b>biểu diễn miền nghiệm</b> và <b>chuyển bài toán thực tế thành hệ bất phương trình</b>."))

    # ---------------- 2.1 ----------------
    st.append(P("2.1. Bất phương trình bậc nhất hai ẩn", "h2"))

    st.append(P("<b>a) Định nghĩa</b>", "h3"))
    st.append(P(
        "<b>Bất phương trình bậc nhất hai ẩn</b> x, y là bất phương trình có một trong các dạng sau:"))
    st.append(P("<b>ax + by ≤ c,  ax + by ≥ c,  ax + by &lt; c,  ax + by &gt; c</b>", "formula"))
    st.append(P(
        "trong đó a, b, c là những số thực đã cho, <b>a và b không đồng thời bằng 0</b> "
        "(tức là a² + b² &gt; 0), còn x và y là các ẩn số."))

    st.append(note([
        P("Cặp số (x<sub>0</sub>; y<sub>0</sub>) được gọi là <b>một nghiệm</b> của bất phương trình nếu "
          "thay x = x<sub>0</sub>, y = y<sub>0</sub> vào bất phương trình ta được một khẳng định đúng.", "small"),
        P("<b>Miền nghiệm</b> của bất phương trình là tập hợp tất cả các điểm có toạ độ là nghiệm "
          "của bất phương trình đó trong mặt phẳng toạ độ Oxy.", "small"),
    ], title="Nghiệm và miền nghiệm", icon="★"))

    st.append(P(
        "Ví dụ: Với bất phương trình 2x + y ≤ 4: cặp (1; 1) có 2·1 + 1 = 3 ≤ 4 nên là nghiệm; "
        "cặp (3; 0) có 2·3 + 0 = 6 &gt; 4 nên không là nghiệm; cặp (2; 0) có 4 ≤ 4 nên là nghiệm "
        "(điểm nằm ngay trên đường bờ vẫn là nghiệm vì có dấu “=”)."))

    st.append(P("<b>b) Quy tắc biểu diễn miền nghiệm</b>", "h3"))
    st.append(method([
        P("<b>Bước 1.</b> Vẽ đường thẳng <b>d: ax + by = c</b> trên mặt phẳng toạ độ Oxy "
          "(chỉ cần xác định hai điểm: cho x = 0 tìm y, cho y = 0 tìm x).", "small"),
        P("<b>Bước 2.</b> Chọn một điểm <b>M(x<sub>0</sub>; y<sub>0</sub>) không nằm trên d</b> "
          "– thường chọn gốc toạ độ O(0; 0) nếu O ∉ d.", "small"),
        P("<b>Bước 3.</b> Tính giá trị ax<sub>0</sub> + by<sub>0</sub> rồi so sánh với c:", "small"),
        P("   • Nếu ax<sub>0</sub> + by<sub>0</sub> &lt; c thì <b>miền nghiệm là nửa mặt phẳng bờ d chứa M</b>.", "small"),
        P("   • Nếu ax<sub>0</sub> + by<sub>0</sub> &gt; c thì <b>miền nghiệm là nửa mặt phẳng bờ d không chứa M</b>.", "small"),
        P("<b>Bước 4.</b> <b>Tô đậm</b> miền nghiệm và kết luận: nếu bất phương trình có dấu ≤ hoặc ≥ "
          "(có dấu “=”) thì <b>kể cả bờ d</b> (vẽ nét liền); nếu là &lt; hoặc &gt; thì <b>không kể bờ</b> "
          "(vẽ nét đứt).", "small"),
    ]))

    st.append(spacing(0.1))
    st.append(KeepTogether([
        P("Ví dụ: Biểu diễn miền nghiệm của bất phương trình 2x − y ≤ 3.", "h4"),
        P("Vẽ d: 2x − y = 3 qua hai điểm (0; −3) và (3; 3). Chọn O(0; 0): 2·0 − 0 = 0 &lt; 3, "
          "vậy miền nghiệm là nửa mặt phẳng bờ d <b>chứa O</b>, kể cả bờ d (vẽ nét liền).", "small"),
        figures.half_plane(width=CONTENT_W - 30, height=225),
    ]))

    st.append(warn([
        P("Lỗi 1: vẽ <b>nét liền</b> cho bất phương trình &lt; hoặc &gt;. Quy tắc: <i>có dấu “=” thì liền, "
          "không có dấu “=” thì đứt</i>.", "small"),
        P("Lỗi 2: kết luận ngược miền. Hãy luôn <b>thay điểm thử</b> chứ đừng đoán theo dấu của hệ số.", "small"),
        P("Lỗi 3: chọn điểm thử nằm <b>trên</b> đường thẳng d (không kết luận được gì).", "small"),
    ]))

    # ---------------- 2.2 ----------------
    st.append(CondPageBreak(10.2 * cm))
    st.append(P("2.2. Hệ bất phương trình bậc nhất hai ẩn", "h2"))

    st.append(P("<b>a) Định nghĩa</b>", "h3"))
    st.append(P(
        "<b>Hệ bất phương trình bậc nhất hai ẩn</b> x, y gồm một số bất phương trình bậc nhất hai ẩn "
        "x, y mà ta phải tìm các nghiệm chung của chúng. Mỗi nghiệm chung được gọi là một "
        "<b>nghiệm của hệ</b>; tập hợp các điểm biểu diễn nghiệm của hệ gọi là <b>miền nghiệm của hệ</b>."))
    st.append(P("Ví dụ một hệ bất phương trình bậc nhất hai ẩn:"))
    st.append(P("<b>{ 2x + y ≤ 100;  x + 2y ≤ 80;  x ≥ 0;  y ≥ 0 }</b>", "formula"))

    st.append(note([
        P("Miền nghiệm của hệ là <b>giao</b> của các miền nghiệm của từng bất phương trình trong hệ.", "small"),
        P("Miền nghiệm thường là một <b>đa giác</b> (tam giác, tứ giác, ngũ giác…) kể cả biên, "
          "hoặc là <b>tập rỗng</b> nếu các miền không có phần chung.", "small"),
        P("Để biểu diễn: vẽ từng đường thẳng bờ, gạch bỏ nửa mặt phẳng <b>không</b> là miền nghiệm "
          "của từng bất phương trình; phần còn lại (không bị gạch) là miền nghiệm của hệ.", "small"),
    ], title="Cách biểu diễn miền nghiệm của hệ", icon="★"))

    st.append(P("<b>b) Bài toán tối ưu (tìm giá trị lớn nhất, nhỏ nhất)</b>", "h3"))
    st.append(P(
        "Rất nhiều bài toán thực tế dẫn đến việc tìm giá trị lớn nhất hoặc nhỏ nhất của biểu thức "
        "<b>F = ax + by</b> với (x; y) thoả mãn một hệ bất phương trình bậc nhất hai ẩn. "
        "Người ta chứng minh được kết quả quan trọng sau:"))

    st.append(callout("Định lí (điểm cực trị của hàm bậc nhất trên đa giác)", [
        P("Nếu miền nghiệm của hệ là một <b>đa giác lồi</b> (kể cả biên) thì biểu thức "
          "<b>F = ax + by</b> đạt giá trị lớn nhất và giá trị nhỏ nhất tại một trong các <b>đỉnh</b> "
          "của đa giác đó.", "small"),
        P("Do đó chỉ cần tính F tại tất cả các đỉnh rồi so sánh – không cần xét mọi điểm của miền.",
          "small"),
    ], color=NAVY, bg=TINT_BLUE, icon="◆"))

    st.append(spacing(0.1))
    st.append(P("<b>c) Quy trình giải một bài toán thực tế bằng hệ bất phương trình</b>", "h3"))
    st.append(method([
        P("<b>Bước 1 – Đặt ẩn.</b> Gọi x, y là các đại lượng cần tìm (số sản phẩm, số kg, số ha, "
          "số giờ…). Luôn kèm điều kiện <b>x ≥ 0, y ≥ 0</b> nếu chúng là số lượng.", "small"),
        P("<b>Bước 2 – Lập hệ bất phương trình.</b> Dịch từng điều kiện ràng buộc của đề bài "
          "(nguồn nguyên liệu, thời gian, khối lượng, diện tích…) thành một bất phương trình bậc nhất "
          "hai ẩn. Chú ý từ khoá: “không vượt quá”, “tối đa” → <b>≤</b>; “ít nhất”, “tối thiểu” → <b>≥</b>.", "small"),
        P("<b>Bước 3 – Xác định miền nghiệm</b> và toạ độ các đỉnh của đa giác.", "small"),
        P("<b>Bước 4 – Viết biểu thức mục tiêu</b> F (lợi nhuận, chi phí, quãng đường…) theo x, y; "
          "tính F tại từng đỉnh.", "small"),
        P("<b>Bước 5 – Kết luận.</b> So sánh các giá trị, chọn phương án cho F lớn nhất (hoặc nhỏ nhất), "
          "<b>trả lời bằng lời văn có đơn vị</b> và kiểm tra x, y có phải số tự nhiên không.", "small"),
    ]))

    st.append(warn([
        P("Sai sót hay gặp: quên điều kiện <b>x ≥ 0, y ≥ 0</b>; nhầm “không vượt quá” thành dấu ≥; "
          "tính F tại đỉnh nhưng <b>quên kết luận theo câu hỏi</b> (ví dụ hỏi “số áo, số quần” nhưng "
          "chỉ ghi giá trị lớn nhất của F).", "small"),
    ]))

    return st


# ==========================================================================
# CHƯƠNG 3
# ==========================================================================
def _ch3():
    st = []
    st += chapter("3", "Hệ thức lượng trong tam giác",
                  "Giá trị lượng giác • Định lí côsin, định lí sin • Diện tích tam giác", TEAL)

    st.append(P(
        "Chương này chiếm 3,0 điểm, gồm 6 câu trắc nghiệm và 1 câu tự luận thực tế. "
        "Đây là chương “dễ ăn điểm” nhất nếu thuộc bảng giá trị lượng giác và 3 công thức gốc."))

    # ---------------- 3.1 ----------------
    st.append(P("3.1. Giá trị lượng giác của một góc từ 0° đến 180°", "h2"))

    st.append(P("<b>a) Định nghĩa</b>", "h3"))
    st.append(P(
        "Trong mặt phẳng toạ độ Oxy, ta xét nửa đường tròn đơn vị (nửa đường tròn tâm O, bán kính 1) "
        "nằm phía trên trục Ox. Với mỗi góc α (0° ≤ α ≤ 180°), có duy nhất điểm M trên nửa đường tròn "
        "sao cho góc xOM = α. Giả sử M có toạ độ (x<sub>0</sub>; y<sub>0</sub>). Khi đó:"))
    st.append(P("<b>sin α = y<sub>0</sub>;   cos α = x<sub>0</sub>;   "
                "tan α = y<sub>0</sub>/x<sub>0</sub> (x<sub>0</sub> ≠ 0);   "
                "cot α = x<sub>0</sub>/y<sub>0</sub> (y<sub>0</sub> ≠ 0)</b>", "formula"))
    st.append(P(
        "Các số sin α, cos α, tan α, cot α gọi là <b>các giá trị lượng giác</b> của góc α."))

    st.append(note([
        P("Với mọi góc α (0° ≤ α ≤ 180°), ta luôn có:", "small"),
        P("• <b>0 ≤ sin α ≤ 1</b> (sin α luôn <b>không âm</b>).", "small"),
        P("• <b>−1 ≤ cos α ≤ 1</b>.", "small"),
        P("• sin α và cos α <b>không đồng thời bằng 0</b>.", "small"),
    ], title="Miền giá trị cần nhớ", icon="★"))

    st.append(P("<b>b) Dấu của các giá trị lượng giác</b>", "h3"))
    sign = data_table(
        ["Góc α", "sin α", "cos α", "tan α", "cot α"],
        [["α = 0°", "0", "1", "0", "không xác định"],
         ["0° &lt; α &lt; 90° (góc nhọn)", "+", "+", "+", "+"],
         ["α = 90°", "1", "0", "không xác định", "0"],
         ["90° &lt; α &lt; 180° (góc tù)", "+", "−", "−", "−"],
         ["α = 180°", "0", "−1", "0", "không xác định"]],
        widths=[5.2 * cm, 2.6 * cm, 2.6 * cm, 2.9 * cm, 3.5 * cm], align_center_cols=[0, 1, 2, 3, 4])
    st.append(sign)

    st.append(spacing(0.15))
    st.append(tip([
        P("<b>Mẹo nhớ:</b> khi góc là góc tù (lớn hơn 90°, nhỏ hơn 180°) thì <b>chỉ có sin dương</b>, "
          "còn cos, tan, cot đều <b>âm</b>. Đây là kiến thức được hỏi trực tiếp ở câu trắc nghiệm "
          "và là chìa khoá để chọn dấu khi tính giá trị lượng giác.", "small")]))

    st.append(P("<b>c) Bảng giá trị lượng giác của các góc đặc biệt</b>", "h3"))
    special = data_table(
        ["α", "0°", "30°", "45°", "60°", "90°", "120°", "135°", "150°", "180°"],
        [["<b>sin α</b>", "0", "1/2", "√2/2", "√3/2", "1", "√3/2", "√2/2", "1/2", "0"],
         ["<b>cos α</b>", "1", "√3/2", "√2/2", "1/2", "0", "−1/2", "−√2/2", "−√3/2", "−1"],
         ["<b>tan α</b>", "0", "√3/3", "1", "√3", "‖", "−√3", "−1", "−√3/3", "0"],
         ["<b>cot α</b>", "‖", "√3", "1", "√3/3", "0", "−√3/3", "−1", "−√3", "‖"]],
        widths=[2.0 * cm] + [1.72 * cm] * 9, align_center_cols=list(range(10)),
        font_size=8.2)
    st.append(special)
    st.append(P("Kí hiệu “‖” chỉ giá trị <b>không xác định</b> (tan 90°, cot 0°, cot 180°).", "caption"))

    st.append(spacing(0.15))
    st.append(note([
        P("Hai góc <b>bù nhau</b> (có tổng bằng 180°), tức là α và 180° − α:", "small"),
        P("• <b>sin(180° − α) = sin α</b>  (sin “giữ nguyên”)", "small"),
        P("• <b>cos(180° − α) = −cos α</b>  (cos “đổi dấu”)", "small"),
        P("• <b>tan(180° − α) = −tan α</b>;  <b>cot(180° − α) = −cot α</b>", "small"),
        P("Hai góc <b>phụ nhau</b> (tổng bằng 90°), tức là α và 90° − α:", "small"),
        P("• <b>sin(90° − α) = cos α</b>;  <b>cos(90° − α) = sin α</b>;  "
          "<b>tan(90° − α) = cot α</b>;  <b>cot(90° − α) = tan α</b>.", "small"),
    ], title="Hai góc bù nhau – hai góc phụ nhau", icon="★"))

    st.append(P(
        "Ví dụ: sin 120° = sin 60° = √3/2; cos 135° = −cos 45° = −√2/2; "
        "tan 150° = −tan 30° = −√3/3; cot 135° = −cot 45° = −1."))

    st.append(P("<b>d) Các hệ thức lượng giác cơ bản</b>", "h3"))
    st.append(callout("Bốn hệ thức cơ bản (với điều kiện các biểu thức xác định)", [
        P("<b>sin²α + cos²α = 1</b>", "formula"),
        P("<b>tan α · cot α = 1</b>", "formula"),
        P("<b>1 + tan²α = 1/cos²α</b>", "formula"),
        P("<b>1 + cot²α = 1/sin²α</b>", "formula"),
    ], color=TEAL, bg=colors.HexColor("#EAF4EC"), icon="★"))

    st.append(P("<b>e) Tính giá trị lượng giác khi biết một giá trị</b>", "h3"))
    st.append(method([
        P("<b>Bước 1.</b> Dùng <b>sin²α + cos²α = 1</b> để tìm sin α (nếu biết cos α) hoặc cos α "
          "(nếu biết sin α).", "small"),
        P("<b>Bước 2.</b> Xác định <b>dấu</b> dựa vào khoảng của α (góc nhọn: mọi giá trị dương; "
          "góc tù: sin dương, cos âm, tan và cot âm).", "small"),
        P("<b>Bước 3.</b> Tính tan α = sin α / cos α và cot α = cos α / sin α nếu đề yêu cầu.", "small"),
        P("<b>Bước 4.</b> Thay vào biểu thức cần tính và rút gọn.", "small"),
    ]))
    st.append(P(
        "Ví dụ: Cho sin α = 3/5 với 90° &lt; α &lt; 180°. Ta có cos²α = 1 − 9/25 = 16/25 ⇒ "
        "cos α = ±4/5. Vì α là góc tù nên cos α &lt; 0, do đó <b>cos α = −4/5</b>; suy ra "
        "tan α = −3/4, cot α = −4/3."))

    # ---------------- 3.2 ----------------
    st.append(CondPageBreak(10.2 * cm))
    st.append(P("3.2. Hệ thức lượng trong tam giác", "h2"))
    st.append(P(
        "Xét tam giác ABC có các cạnh <b>BC = a, CA = b, AB = c</b>; R là bán kính đường tròn ngoại tiếp, "
        "r là bán kính đường tròn nội tiếp, p = (a + b + c)/2 là nửa chu vi, S là diện tích, "
        "m<sub>a</sub> là độ dài đường trung tuyến kẻ từ A."))
    st.append(figures.triangle_labels(width=CONTENT_W - 40, height=170))

    st.append(P("<b>a) Định lí côsin</b>", "h3"))
    st.append(callout("Định lí côsin", [
        P("<b>a² = b² + c² − 2bc·cos A</b>", "formula"),
        P("<b>b² = c² + a² − 2ca·cos B</b>", "formula"),
        P("<b>c² = a² + b² − 2ab·cos C</b>", "formula"),
        P("Hệ quả (dùng để tính góc khi biết ba cạnh):", "small"),
        P("<b>cos A = (b² + c² − a²) / (2bc)</b>", "formula"),
        P("<b>cos B = (c² + a² − b²) / (2ca)</b>;   <b>cos C = (a² + b² − c²) / (2ab)</b>", "formula"),
    ], color=NAVY, bg=TINT_BLUE, icon="★"))

    st.append(P(
        "Nhận xét: nếu A = 90° thì cos A = 0 và ta được <b>a² = b² + c²</b> – chính là định lí Pythagore. "
        "Nếu A là góc tù thì cos A &lt; 0 nên a² &gt; b² + c² (cạnh đối diện góc tù là cạnh lớn nhất)."))

    st.append(P("<b>b) Định lí sin</b>", "h3"))
    st.append(callout("Định lí sin", [
        P("<b>a/sin A = b/sin B = c/sin C = 2R</b>", "formula"),
        P("Từ đó: <b>a = 2R·sin A, b = 2R·sin B, c = 2R·sin C</b> và <b>R = a/(2 sin A)</b>.", "small"),
    ], color=TEAL, bg=colors.HexColor("#EAF4EC"), icon="★"))

    st.append(P("<b>c) Công thức tính diện tích tam giác</b>", "h3"))
    st.append(callout("Năm công thức diện tích", [
        P("<b>S = (1/2)·a·h<sub>a</sub></b>   (h<sub>a</sub> là đường cao kẻ từ A)", "formula"),
        P("<b>S = (1/2)·a·b·sin C = (1/2)·b·c·sin A = (1/2)·c·a·sin B</b>", "formula"),
        P("<b>S = abc / (4R)</b>", "formula"),
        P("<b>S = p·r</b>   (p là nửa chu vi)", "formula"),
        P("<b>S = √(p(p − a)(p − b)(p − c))</b>   (công thức Heron)", "formula"),
    ], color=GOLD, bg=TINT_GOLD, icon="★"))

    st.append(P("<b>d) Công thức đường trung tuyến</b>", "h3"))
    st.append(P("<b>m<sub>a</sub></b><super>2</super><b> = (b² + c²)/2 − a²/4</b>", "formula"))
    st.append(P("<b>m<sub>b</sub></b><super>2</super><b> = (c² + a²)/2 − b²/4</b>;   "
                "<b>m<sub>c</sub></b><super>2</super><b> = (a² + b²)/2 − c²/4</b>", "formula"))

    st.append(P("<b>e) Định lí tổng ba góc và hệ quả</b>", "h3"))
    st.append(P(
        "Trong tam giác ABC: <b>A + B + C = 180°</b>. Do đó sin(A + B) = sin C, cos(A + B) = −cos C. "
        "Trong tam giác, <b>cạnh đối diện góc lớn hơn thì lớn hơn</b> và ngược lại: "
        "a &gt; b ⇔ A &gt; B."))

    st.append(P("<b>f) Giải tam giác và ứng dụng thực tiễn</b>", "h3"))
    st.append(P(
        "<b>Giải tam giác</b> là tìm các yếu tố còn lại (cạnh, góc, diện tích) khi biết một số yếu tố "
        "xác định của tam giác. Bốn tình huống thường gặp:"))
    st.append(data_table(
        ["Biết", "Công cụ nên dùng"],
        [["Ba cạnh a, b, c", "Định lí côsin (tính góc) → công thức Heron (diện tích)"],
         ["Hai cạnh và góc xen giữa (b, c, A)", "Định lí côsin (tính a) → định lí sin (tính góc)"],
         ["Một cạnh và hai góc (a, B, C)", "Tính góc còn lại (A = 180° − B − C) → định lí sin"],
         ["Hai cạnh và góc không xen giữa", "Định lí sin, chú ý có thể có 1 hoặc 2 nghiệm hình"]],
        widths=[6.4 * cm, 10.4 * cm]))

    st.append(spacing(0.2))
    st.append(note([
        P("Trong bài toán thực tế, hãy làm theo 3 bước:", "small"),
        P("<b>(1)</b> Vẽ hình, đặt tên các điểm và <b>chuyển dữ kiện thành các yếu tố của tam giác</b> "
          "(cạnh – góc).", "small"),
        P("<b>(2)</b> Chọn công cụ: định lí côsin khi biết 2 cạnh + góc xen giữa hoặc 3 cạnh; "
          "định lí sin khi biết 1 cạnh + góc đối diện.", "small"),
        P("<b>(3)</b> Tính toán, <b>làm tròn theo yêu cầu</b> và trả lời có đơn vị (m, km, °…).", "small"),
    ], title="Kĩ năng giải bài toán thực tiễn", icon="◆"))

    st.append(P("<b>g) Ba trường hợp tam giác đặc biệt (dùng để tính nhanh)</b>", "h3"))
    st.append(data_table(
        ["Loại tam giác", "Hệ thức rút gọn", "Ghi nhớ"],
        [["<b>Vuông tại A</b> (A = 90°)",
          "a² = b² + c²;  S = (1/2)·b·c;  R = a/2",
          "Định lí Pythagore; cạnh huyền là đường kính đường tròn ngoại tiếp"],
         ["<b>Đều cạnh a</b>",
          "S = a²√3/4;  R = a/√3 = a√3/3;  r = a√3/6;  h = a√3/2",
          "Mọi góc bằng 60°; trọng tâm trùng trực tâm, tâm nội – ngoại tiếp"],
         ["<b>Cân tại A</b> (AB = AC = b)",
          "a = 2b·sin(A/2);  S = (1/2)·b²·sin A",
          "Hai góc ở đáy bằng nhau: B = C = (180° − A)/2"]],
        widths=[4.2 * cm, 6.4 * cm, 6.2 * cm], font_size=8.4))
    st.append(P("Ba trường hợp này xuất hiện rất nhiều trong bài toán thực tiễn: cột cờ – bóng nắng "
                "thường tạo tam giác vuông, mái nhà – tháp chuông thường tạo tam giác cân.", "caption"))

    st.append(tip([
        P("Với bài toán tính <b>khoảng cách giữa hai điểm</b> mà không đo trực tiếp được (có vật cản), "
          "ta chọn một điểm thứ ba nhìn thấy cả hai điểm, đo khoảng cách tới chúng và góc tạo bởi "
          "hai hướng nhìn → dùng <b>định lí côsin</b>.", "small"),
        P("Với bài toán tính <b>chiều cao</b> của vật, đo hai góc nâng từ hai vị trí cách nhau một "
          "khoảng đã biết → lập tam giác và dùng <b>định lí sin</b>.", "small"),
    ]))

    return st


# ==========================================================================
# CHƯƠNG 4
# ==========================================================================
def _ch4():
    st = []
    st += chapter("4", "Vectơ", "Khái niệm vectơ • Phương, hướng • Hai vectơ bằng nhau", TEAL)

    st.append(P(
        "Chương này chỉ chiếm 0,5 điểm (2 câu trắc nghiệm mức Nhận biết – Thông hiểu), "
        "nhưng kiến thức rất dễ học và chắc chắn có trong đề. Chỉ cần nắm vững phần khái niệm là đủ."))

    st.append(P("4.1. Khái niệm vectơ", "h2"))

    st.append(P("<b>a) Định nghĩa</b>", "h3"))
    st.append(P(
        "<b>Vectơ</b> là một đoạn thẳng có hướng. Vectơ có điểm đầu A và điểm cuối B được kí hiệu là "
        "<b>AB</b> (trong tài liệu này vectơ được in đậm; khi viết tay các em dùng mũi tên "
        "AB có dấu → ở trên), đọc là “vectơ AB”."))
    st.append(P(
        "Đường thẳng đi qua A và B gọi là <b>giá</b> của vectơ AB. "
        "<b>Độ dài</b> của vectơ AB, kí hiệu <b>|AB|</b>, là độ dài đoạn thẳng AB: |AB| = AB."))
    st.append(P(
        "Vectơ có điểm đầu trùng điểm cuối, kí hiệu <b>AA</b> (hoặc 0), gọi là <b>vectơ – không</b>."))

    st.append(note([
        P("• <b>Độ dài vectơ là một số không âm</b>: |AB| ≥ 0 và |AA| = 0.", "small"),
        P("• Độ dài vectơ là độ dài đoạn thẳng, nên <b>không phụ thuộc hướng</b>: |AB| = |BA|.", "small"),
        P("• Vectơ – không có độ dài bằng 0, giá không xác định.", "small"),
    ], title="Độ dài và vectơ – không", icon="★"))

    st.append(P("<b>b) Hai vectơ cùng phương, cùng hướng</b>", "h3"))
    st.append(P(
        "Hai vectơ được gọi là <b>cùng phương</b> nếu giá của chúng song song với nhau hoặc trùng nhau."))
    st.append(P(
        "Nếu hai vectơ cùng phương thì chúng chỉ có thể <b>cùng hướng</b> hoặc <b>ngược hướng</b>. "
        "Hai vectơ được gọi là <b>cùng hướng</b> nếu chúng cùng phương và cùng chỉ về một phía; "
        "ngược lại gọi là <b>ngược hướng</b>."))
    st.append(note([
        P("Từ một điểm O bất kì, chỉ có <b>duy nhất một</b> vectơ cùng hướng và có độ dài bằng "
          "vectơ AB cho trước, và <b>duy nhất một</b> vectơ ngược hướng có độ dài bằng |AB|.", "small"),
        P("<b>Ba điểm A, B, C thẳng hàng</b> ⇔ hai vectơ AB và AC <b>cùng phương</b>.", "small"),
    ], color=BLUE, bg=TINT_BLUE, title="Tính chất", icon="★"))

    st.append(P("<b>c) Hai vectơ bằng nhau</b>", "h3"))
    st.append(P(
        "Hai vectơ <b>AB</b> và <b>CD</b> được gọi là <b>bằng nhau</b>, kí hiệu <b>AB = CD</b>, "
        "nếu chúng <b>cùng hướng</b> và <b>cùng độ dài</b>."))
    st.append(P(
        "Chú ý: hai vectơ bằng nhau thì phải cùng hướng – vì thế khi viết AB = DC (chứ không phải CD) "
        "trong hình bình hành ABCD, ta cần kiểm tra hướng của chúng. "
        "Vectơ <b>BA</b> gọi là vectơ <b>đối</b> của vectơ AB: cùng độ dài, ngược hướng."))

    st.append(P("<b>d) Vectơ – không</b>", "h3"))
    st.append(note([
        P("• Vectơ – không có độ dài bằng 0: |0| = 0.", "small"),
        P("• <b>Vectơ – không cùng phương và cùng hướng với mọi vectơ.</b>", "small"),
        P("• Mọi vectơ – không đều bằng nhau: AA = BB = 0.", "small"),
    ], title="Bốn tính chất của vectơ – không (rất hay được hỏi)", icon="★"))

    st.append(KeepTogether([
        figures.parallelogram(width=CONTENT_W - 60, height=140,
                             caption="Hình A.2. Hình bình hành ABCD: AB = DC và AD = BC"),
        P("Trong hình bình hành ABCD (đỉnh theo thứ tự A, B, C, D) ta có "
          "<b>AB = DC</b>, <b>AD = BC</b>; AB và CD là hai vectơ <b>ngược hướng</b> "
          "nhưng <b>bằng nhau về độ dài</b>.", "small"),
    ]))

    st.append(warn([
        P("Ba khẳng định <b>sai</b> học sinh hay chọn nhầm:", "small"),
        P("(1) “Hai vectơ cùng phương thì cùng hướng” – <b>sai</b> (có thể ngược hướng).", "small"),
        P("(2) “Hai vectơ cùng độ dài thì bằng nhau” – <b>sai</b> (còn phải cùng hướng).", "small"),
        P("(3) “Vectơ – không không cùng phương với vectơ nào” – <b>sai</b> (nó cùng phương với mọi vectơ).",
          "small"),
    ]))

    return st
