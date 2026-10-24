# -*- coding: utf-8 -*-
"""PHẦN B – Phương pháp giải từng dạng toán thường gặp (kèm ví dụ mẫu)."""
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import CondPageBreak, KeepTogether, PageBreak, Spacer

from pdfkit import (
    BLUE, CONTENT_W, GOLD, NAVY, RED, SectionBanner, TEAL, TINT_BLUE, bullets, callout,
    data_table, method, note, P, S, spacing, tip, warn,
)


def ex(text):
    return P(f"<b>Ví dụ.</b> {text}", "q")


def sol(*parts):
    return callout("Lời giải", list(parts),
                   color=colors.HexColor("#8A99A8"),
                   bg=colors.HexColor("#F7F9FA"), icon="", width=CONTENT_W)


def story():
    st = []
    st.append(CondPageBreak(6.0 * cm))
    st.append(SectionBanner("PHẦN B", "Phương pháp giải các dạng toán thường gặp", GOLD))
    st.append(spacing(0.3))
    st.append(P(
        "17 dạng toán dưới đây bao phủ <b>toàn bộ</b> các câu hỏi có thể xuất hiện trong đề, "
        "sắp xếp theo đúng thứ tự chương. Với mỗi dạng: đọc <i>phương pháp</i> → che <i>lời giải</i> "
        "→ tự làm ví dụ → đối chiếu."))

    st += _dang_menh_de()
    st += _dang_tap_hop()
    st += _dang_bpt()
    st += _dang_luong_giac()
    st += _dang_vecto()
    return st


# ==========================================================================
def _dang_menh_de():
    st = []
    st.append(P("Dạng 1. Nhận diện mệnh đề, mệnh đề chứa biến", "h2"))
    st.append(method([
        P("• Câu <b>khẳng định</b> đúng hoặc sai → mệnh đề.", "small"),
        P("• Câu hỏi, câu cảm thán, câu mệnh lệnh → <b>không</b> phải mệnh đề.", "small"),
        P("• Câu khẳng định có biến chưa gán giá trị → <b>mệnh đề chứa biến</b>.", "small"),
        P("• Mệnh đề chứa kí hiệu ∀ hoặc ∃ (trên một tập xác định) <b>là mệnh đề</b> vì đã xác định "
          "được đúng/sai.", "small"),
    ]))
    st.append(ex("Trong các câu sau, câu nào là mệnh đề? Câu nào là mệnh đề chứa biến? "
                 "Xét tính đúng sai của các mệnh đề.<br/>"
                 "a) “Số 2026 chia hết cho 2.”<br/>"
                 "b) “2n + 1 là số lẻ.”<br/>"
                 "c) “Hãy tính tổng 1 + 2 + … + 100.”<br/>"
                 "d) “∃x ∈ ℝ, x² = −1.”<br/>"
                 "e) “Tam giác đều có ba góc bằng 60°.”"))
    st.append(sol(
        P("a) Là <b>mệnh đề đúng</b> (2026 = 2·1013).", "small"),
        P("b) Là <b>mệnh đề chứa biến</b> P(n): với n = 3 ta được mệnh đề đúng, nhưng bản thân câu "
          "chưa xác định đúng sai vì n chưa được gán giá trị.", "small"),
        P("c) Không phải mệnh đề (câu mệnh lệnh, đề nghị).", "small"),
        P("d) Là <b>mệnh đề sai</b>: với mọi số thực x ta luôn có x² ≥ 0 nên không tồn tại x thoả x² = −1.",
          "small"),
        P("e) Là <b>mệnh đề đúng</b>.", "small"),
    ))

    st.append(P("Dạng 2. Lập mệnh đề phủ định (kể cả mệnh đề có ∀, ∃)", "h2"))
    st.append(method([
        P("<b>Bước 1.</b> Thêm (hoặc bớt) từ “không” / “không phải” trước vị ngữ.", "small"),
        P("<b>Bước 2.</b> Nếu mệnh đề có lượng từ: <b>đổi ∀ thành ∃</b> (và ngược lại), "
          "đồng thời <b>phủ định mệnh đề chứa biến</b> (đổi &lt; thành ≥, = thành ≠, …).", "small"),
        P("<b>Bước 3.</b> Kết luận tính đúng sai: nếu P đúng thì ¬P sai và ngược lại.", "small"),
    ]))
    st.append(warn([
        P("Chỉ phủ định <b>vị ngữ</b>, <b>không</b> phủ định cả câu theo kiểu “Không phải với mọi x…” "
          "rồi giữ nguyên ∀ (sai lượng từ).", "small"),
    ]))
    st.append(ex("Lập mệnh đề phủ định và xét tính đúng sai của mỗi mệnh đề sau:<br/>"
                 "a) P: “∀x ∈ ℝ, x² + 1 &gt; 0”.<br/>"
                 "b) Q: “∃n ∈ ℕ, n² = n + 2”.<br/>"
                 "c) R: “91 là số nguyên tố”."))
    st.append(sol(
        P("a) ¬P: “<b>∃x ∈ ℝ, x² + 1 ≤ 0</b>”. Vì x² + 1 ≥ 1 &gt; 0 với mọi x nên P <b>đúng</b>, "
          "do đó ¬P <b>sai</b>.", "small"),
        P("b) ¬Q: “<b>∀n ∈ ℕ, n² ≠ n + 2</b>”. Với n = 2: 4 = 2 + 2 nên Q <b>đúng</b>, do đó ¬Q <b>sai</b>.",
          "small"),
        P("c) R̄: “<b>91 không phải là số nguyên tố</b>”. Vì 91 = 7·13 nên R <b>sai</b>, do đó R̄ <b>đúng</b>.",
          "small"),
    ))

    st.append(P("Dạng 3. Mệnh đề kéo theo, mệnh đề đảo, điều kiện cần – đủ", "h2"))
    st.append(method([
        P("<b>P ⇒ Q</b> chỉ sai khi P đúng, Q sai.", "small"),
        P("Phát biểu “P là điều kiện <b>đủ</b> để có Q”; “Q là điều kiện <b>cần</b> để có P”.", "small"),
        P("Mệnh đề đảo là <b>Q ⇒ P</b>. Nếu cả hai đều đúng thì <b>P ⇔ Q</b> "
          "(P là điều kiện cần và đủ để có Q).", "small"),
        P("Để chứng minh P ⇒ Q <b>sai</b>, chỉ cần <b>đưa ra một phản ví dụ</b>.", "small"),
    ]))
    st.append(ex("Cho mệnh đề: “Nếu tam giác ABC đều thì tam giác ABC cân”.<br/>"
                 "a) Xét tính đúng sai của mệnh đề.<br/>"
                 "b) Phát biểu mệnh đề trên bằng “điều kiện cần”, “điều kiện đủ”.<br/>"
                 "c) Lập mệnh đề đảo và xét tính đúng sai của nó.<br/>"
                 "d) Hai mệnh đề trên có tương đương không?"))
    st.append(sol(
        P("a) Mệnh đề <b>đúng</b>: tam giác đều có ba cạnh bằng nhau nên có hai cạnh bằng nhau, "
          "tức là tam giác cân.", "small"),
        P("b) “<b>Tam giác ABC đều là điều kiện đủ</b> để tam giác ABC cân”; "
          "“<b>Tam giác ABC cân là điều kiện cần</b> để tam giác ABC đều”.", "small"),
        P("c) Mệnh đề đảo: “Nếu tam giác ABC cân thì tam giác ABC đều”. Mệnh đề này <b>sai</b>: "
          "chẳng hạn tam giác cân tại A với AB = AC = 2, BC = 3 không phải tam giác đều.", "small"),
        P("d) Hai mệnh đề <b>không tương đương</b> vì mệnh đề đảo sai.", "small"),
    ))
    return st


# ==========================================================================
def _dang_tap_hop():
    st = []
    st.append(CondPageBreak(10.2 * cm))
    st.append(P("Dạng 4. Xác định tập hợp và tính số tập con", "h2"))
    st.append(method([
        P("• Nếu tập hợp có ít phần tử: <b>liệt kê</b>, mỗi phần tử viết một lần, cách nhau bởi “;”.", "small"),
        P("• Nếu có vô số hoặc rất nhiều phần tử: dùng <b>tính chất đặc trưng</b> "
          "{x ∈ X | tính chất}.", "small"),
        P("• Giải phương trình/bất phương trình trong điều kiện để tìm phần tử (chú ý tập nền ℕ, ℤ, ℚ, ℝ).",
          "small"),
        P("• Tập có n phần tử có <b>2<super>n</super></b> tập con, <b>2<super>n</super> − 1</b> tập con "
          "khác rỗng.", "small"),
    ]))
    st.append(ex("Viết mỗi tập hợp sau bằng cách liệt kê các phần tử và cho biết số phần tử:<br/>"
                 "a) A = {x ∈ ℕ* | x &lt; 10 và x là bội của 3}.<br/>"
                 "b) B = {x ∈ ℤ | −3 ≤ x &lt; 2}.<br/>"
                 "c) C = {x ∈ ℝ | x² − 5x + 6 = 0}.<br/>"
                 "d) D = {x ∈ ℚ | x² = 2}."))
    st.append(sol(
        P("a) Các bội dương của 3 nhỏ hơn 10: 3; 6; 9 ⇒ <b>A = {3; 6; 9}</b>, có <b>3</b> phần tử "
          "(và do đó A có 2³ = <b>8</b> tập con).", "small"),
        P("b) Các số nguyên từ −3 đến 1: <b>B = {−3; −2; −1; 0; 1}</b>, có <b>5</b> phần tử.", "small"),
        P("c) x² − 5x + 6 = 0 ⇔ x = 2 hoặc x = 3 ⇒ <b>C = {2; 3}</b>, có <b>2</b> phần tử.", "small"),
        P("d) Không có số hữu tỉ nào bình phương bằng 2 (vì √2 là số vô tỉ) ⇒ <b>D = ∅</b>, "
          "tập rỗng <b>không có phần tử nào</b> và chỉ có <b>1</b> tập con là chính nó.", "small"),
    ))

    st.append(P("Dạng 5. Xét quan hệ tập con – hai tập hợp bằng nhau", "h2"))
    st.append(method([
        P("Muốn chứng minh <b>A ⊂ B</b>: lấy phần tử x ∈ A bất kì, chứng minh x ∈ B.", "small"),
        P("Muốn chứng minh <b>A = B</b>: chứng minh <b>cả hai</b> chiều A ⊂ B và B ⊂ A.", "small"),
        P("Muốn chứng minh <b>A ⊄ B</b>: chỉ ra <b>một</b> phần tử thuộc A nhưng không thuộc B.", "small"),
        P("Luôn nhớ: <b>∅ ⊂ A</b> với mọi tập A.", "small"),
    ]))
    st.append(ex("Cho A = {x ∈ ℝ | x² − 4 = 0}, B = {−2; 2}, C = {x ∈ ℕ | x &lt; 3}. "
                 "Xác định quan hệ giữa A và B; giữa {1; 2} và C; liệt kê các tập con của {1; 2}."))
    st.append(sol(
        P("Ta có x² − 4 = 0 ⇔ x = ±2 nên A = {−2; 2}. Do đó <b>A = B</b> "
          "(vì A ⊂ B và B ⊂ A).", "small"),
        P("C = {x ∈ ℕ | x &lt; 3} = {0; 1; 2}. Suy ra <b>{1; 2} ⊂ C</b> (và {1; 2} ≠ C vì 0 ∈ C).", "small"),
        P("Các tập con của {1; 2} là: <b>∅, {1}, {2}, {1; 2}</b> – đúng 2² = 4 tập con.", "small"),
    ))

    st.append(P("Dạng 6. Giao, hợp, hiệu của các tập hợp cho bằng cách liệt kê", "h2"))
    st.append(method([
        P("<b>A ∩ B</b>: giữ những phần tử <b>có mặt ở cả A và B</b>.", "small"),
        P("<b>A ∪ B</b>: gộp tất cả, <b>mỗi phần tử chỉ viết một lần</b>.", "small"),
        P("<b>A \\ B</b>: lấy phần tử của A rồi <b>xoá</b> những phần tử thuộc B.", "small"),
        P("<b>B \\ A</b> khác hoàn toàn <b>A \\ B</b> – đọc kĩ đề.", "small"),
    ]))
    st.append(ex("Cho A = {0; 1; 2; 3; 4; 5}, B = {2; 4; 6}, C = {1; 3; 5}. Tìm A ∩ B, A ∪ B, "
                 "A \\ B, B \\ A và (A ∩ B) ∪ C."))
    st.append(sol(
        P("A ∩ B = <b>{2; 4}</b>;   A ∪ B = <b>{0; 1; 2; 3; 4; 5; 6}</b>;", "small"),
        P("A \\ B = <b>{0; 1; 3; 5}</b>;   B \\ A = <b>{6}</b>;", "small"),
        P("(A ∩ B) ∪ C = {2; 4} ∪ {1; 3; 5} = <b>{1; 2; 3; 4; 5}</b>.", "small"),
    ))

    st.append(P("Dạng 7. Giao, hợp, hiệu của các khoảng – đoạn (bài toán trục số)", "h2"))
    st.append(method([
        P("<b>Vẽ trục số</b> cho từng tập hợp (đây là cách chắc chắn nhất, tránh nhầm ngoặc).", "small"),
        P("Giao: phần <b>có đủ mọi đường</b>. Hợp: phần <b>có ít nhất một đường</b>. "
          "Hiệu A \\ B: phần của A <b>nằm ngoài</b> B.", "small"),
        P("Kiểm tra đầu mút: với giao, đầu mút chỉ được lấy nếu nó <b>được lấy ở tất cả</b> các tập; "
          "với hợp, chỉ cần <b>một</b> tập lấy.", "small"),
        P("Phần bù C<sub>ℝ</sub>A = ℝ \\ A: đổi chiều bất đẳng thức và <b>đảo ngoặc</b> "
          "(ngoặc vuông ↔ ngoặc tròn).", "small"),
    ]))
    st.append(ex("Cho A = (−1; 4] và B = [2; 6). Tìm A ∩ B, A ∪ B, A \\ B, B \\ A và phần bù của mỗi "
                 "tập trong ℝ."))
    st.append(sol(
        P("A ∩ B = <b>[2; 4]</b>  (lấy 2 vì B lấy 2, lấy 4 vì A lấy 4).", "small"),
        P("A ∪ B = <b>(−1; 6)</b>  (không lấy −1 vì A bỏ −1; không lấy 6 vì B bỏ 6).", "small"),
        P("A \\ B = <b>(−1; 2)</b>  (phần của A nằm bên trái B, không lấy 2).", "small"),
        P("B \\ A = <b>(4; 6)</b>  (phần của B nằm bên phải A, không lấy 4).", "small"),
        P("C<sub>ℝ</sub>A = ℝ \\ A = <b>(−∞; −1] ∪ (4; +∞)</b>;   "
          "C<sub>ℝ</sub>B = <b>(−∞; 2) ∪ [6; +∞)</b>.", "small"),
    ))

    st.append(P("Dạng 8. Bài toán thực tế dùng biểu đồ Ven", "h2"))
    st.append(method([
        P("Gọi A, B là hai nhóm đối tượng; dùng công thức <b>|A ∪ B| = |A| + |B| − |A ∩ B|</b> "
          "(số phần tử).", "small"),
        P("Số người <b>không</b> thuộc nhóm nào = <b>tổng số − |A ∪ B|</b>.", "small"),
        P("Số người <b>chỉ</b> thuộc A = |A| − |A ∩ B|; chỉ thuộc B = |B| − |A ∩ B|.", "small"),
        P("Nếu xuất hiện ba nhóm, vẽ biểu đồ Ven rồi điền số từ trong ra ngoài.", "small"),
    ]))
    st.append(ex("Lớp 10B có 45 học sinh. Trong đó có 30 học sinh thích môn Toán, 25 học sinh thích "
                 "môn Ngữ văn và 12 học sinh thích cả hai môn. Hỏi:<br/>"
                 "a) Có bao nhiêu học sinh thích ít nhất một trong hai môn?<br/>"
                 "b) Có bao nhiêu học sinh không thích môn nào trong hai môn đó?"))
    st.append(sol(
        P("Gọi A là tập học sinh thích Toán, B là tập học sinh thích Ngữ văn. "
          "Theo đề: |A| = 30, |B| = 25, |A ∩ B| = 12.", "small"),
        P("a) |A ∪ B| = 30 + 25 − 12 = <b>43</b> học sinh thích ít nhất một môn.", "small"),
        P("b) Số học sinh không thích môn nào = 45 − 43 = <b>2</b> học sinh.", "small"),
    ))
    return st


# ==========================================================================
def _dang_bpt():
    st = []
    st.append(CondPageBreak(10.2 * cm))
    st.append(P("Dạng 9. Nhận diện bất phương trình bậc nhất hai ẩn, kiểm tra nghiệm", "h2"))
    st.append(method([
        P("Bất phương trình phải có dạng <b>ax + by ≤ c</b> (hoặc ≥, &lt;, &gt;) với <b>a, b không "
          "đồng thời bằng 0</b>.", "small"),
        P("Loại các bất phương trình: có ẩn bậc 2 (x², y², xy), có ẩn ở mẫu, có <b>ba ẩn</b> trở lên, "
          "hoặc có căn thức của ẩn.", "small"),
        P("Kiểm tra nghiệm: <b>thay số</b> vào bất phương trình, nếu được khẳng định đúng thì là nghiệm.",
          "small"),
        P("Điểm nằm <b>trên đường bờ</b> vẫn là nghiệm khi bất phương trình có dấu “=” (≤, ≥).", "small"),
    ]))
    st.append(ex("a) Trong các bất phương trình sau, bất phương trình nào là bất phương trình bậc nhất "
                 "hai ẩn? (1) 2x + 5y &lt; 3;  (2) x² + y ≥ 1;  (3) 3/x − y ≤ 0;  (4) x + y − 2z &gt; 1;  "
                 "(5) 4x ≥ 7.<br/>"
                 "b) Cho bất phương trình 3x − 2y ≤ 6. Trong các cặp số (0; 0), (2; 0), (3; 0), (1; −2), "
                 "cặp nào là nghiệm?"))
    st.append(sol(
        P("a) <b>(1)</b> và <b>(5)</b> là bất phương trình bậc nhất hai ẩn. "
          "(5) có dạng 4x + 0y ≥ 7, vẫn hợp lệ vì b = 0 nhưng a = 4 ≠ 0. "
          "(2) có ẩn bậc hai; (3) có ẩn ở mẫu; (4) có ba ẩn.", "small"),
        P("b) Thay lần lượt:", "small"),
        P("• (0; 0): 3·0 − 2·0 = 0 ≤ 6 → <b>là nghiệm</b>.", "small"),
        P("• (2; 0): 6 − 0 = 6 ≤ 6 → <b>là nghiệm</b> (điểm nằm trên đường bờ).", "small"),
        P("• (3; 0): 9 &gt; 6 → không là nghiệm.", "small"),
        P("• (1; −2): 3 + 4 = 7 &gt; 6 → không là nghiệm.", "small"),
    ))

    st.append(P("Dạng 10. Biểu diễn miền nghiệm của bất phương trình bậc nhất hai ẩn", "h2"))
    st.append(method([
        P("<b>Bước 1.</b> Vẽ bờ d: ax + by = c qua hai điểm dễ tìm (giao với Ox, Oy).", "small"),
        P("<b>Bước 2.</b> Thử điểm M ∉ d (ưu tiên O(0; 0)).", "small"),
        P("<b>Bước 3.</b> Kết luận: miền nghiệm là nửa mặt phẳng bờ d <b>chứa M</b> nếu thay M thoả mãn, "
          "<b>không chứa M</b> nếu không thoả mãn.", "small"),
        P("<b>Bước 4.</b> Có dấu “=” (≤, ≥) → <b>kể cả bờ</b>, vẽ bờ <b>nét liền</b>; "
          "không có dấu “=” (&lt;, &gt;) → <b>không kể bờ</b>, vẽ bờ <b>nét đứt</b>.", "small"),
    ]))
    st.append(ex("Biểu diễn miền nghiệm của bất phương trình x + 2y &gt; 4."))
    st.append(sol(
        P("Vẽ đường thẳng d: x + 2y = 4, đi qua hai điểm (0; 2) và (4; 0). Vì bất phương trình có dấu "
          "“&gt;” nên bờ d được vẽ <b>nét đứt</b> (không kể bờ).", "small"),
        P("Chọn O(0; 0): 0 + 2·0 = 0 &gt; 4 là <b>sai</b>, nên O không thuộc miền nghiệm.", "small"),
        P("Vậy miền nghiệm là <b>nửa mặt phẳng bờ d, không chứa O, không kể bờ d</b> "
          "(phần nằm phía trên – bên phải đường thẳng).", "small"),
    ))

    st.append(P("Dạng 11. Biểu diễn miền nghiệm của hệ bất phương trình", "h2"))
    st.append(method([
        P("Vẽ lần lượt các đường bờ, với mỗi bất phương trình <b>gạch bỏ</b> phần không phải miền nghiệm.",
          "small"),
        P("Phần <b>không bị gạch</b> là miền nghiệm của hệ – thường là một đa giác.", "small"),
        P("Xác định toạ độ các <b>đỉnh</b> bằng cách giải hệ phương trình tạo bởi hai đường bờ cắt nhau.",
          "small"),
        P("Đừng quên hai ràng buộc <b>x ≥ 0, y ≥ 0</b> nếu bài toán có ý nghĩa số lượng.", "small"),
    ]))
    st.append(ex("Biểu diễn miền nghiệm của hệ bất phương trình: x + y ≤ 4; x ≥ 0; y ≥ 0."))
    st.append(sol(
        P("Vẽ d₁: x + y = 4 qua (4; 0) và (0; 4); miền nghiệm của x + y ≤ 4 là nửa mặt phẳng chứa O "
          "(kể cả bờ).", "small"),
        P("x ≥ 0 là nửa mặt phẳng bên phải trục Oy; y ≥ 0 là nửa mặt phẳng phía trên trục Ox.", "small"),
        P("Miền nghiệm là <b>tam giác OAB</b> với O(0; 0), A(4; 0), B(0; 4), <b>kể cả biên</b>.", "small"),
    ))

    st.append(P("Dạng 12. Bài toán tối ưu – tìm giá trị lớn nhất, nhỏ nhất", "h2"))
    st.append(method([
        P("<b>Bước 1.</b> Đặt ẩn x, y (kèm điều kiện x ≥ 0, y ≥ 0 nếu là số lượng).", "small"),
        P("<b>Bước 2.</b> Lập hệ bất phương trình từ các ràng buộc của đề.", "small"),
        P("<b>Bước 3.</b> Vẽ miền nghiệm, tìm toạ độ các đỉnh của đa giác.", "small"),
        P("<b>Bước 4.</b> Tính giá trị biểu thức mục tiêu F tại từng đỉnh, chọn lớn nhất / nhỏ nhất.",
          "small"),
        P("<b>Bước 5.</b> Kết luận bằng lời văn, có đơn vị, kiểm tra x, y có nguyên không.", "small"),
    ]))
    st.append(ex("Một gia đình có 10 ha đất và 240 giờ công để trồng đậu và ngô. Mỗi ha đậu cần 20 giờ "
                 "công, mỗi ha ngô cần 30 giờ công; lợi nhuận thu được là 3 triệu đồng/ha đậu và "
                 "4 triệu đồng/ha ngô. Hỏi cần trồng bao nhiêu ha mỗi loại để lợi nhuận lớn nhất?"))
    st.append(sol(
        P("Gọi x, y (ha) lần lượt là diện tích trồng đậu và ngô, x ≥ 0, y ≥ 0.", "small"),
        P("Ràng buộc: x + y ≤ 10 (đất) và 20x + 30y ≤ 240, tức <b>2x + 3y ≤ 24</b> (giờ công).", "small"),
        P("Hệ: x + y ≤ 10; 2x + 3y ≤ 24; x ≥ 0; y ≥ 0. Lợi nhuận F = 3x + 4y (triệu đồng).", "small"),
        P("Miền nghiệm là tứ giác với các đỉnh O(0; 0), A(10; 0), B(6; 4), C(0; 8) "
          "(B là giao của x + y = 10 và 2x + 3y = 24).", "small"),
        P("F(O) = 0; F(A) = 30; F(B) = 3·6 + 4·4 = <b>34</b>; F(C) = 32.", "small"),
        P("Vậy lợi nhuận lớn nhất là <b>34 triệu đồng</b>, đạt khi trồng <b>6 ha đậu và 4 ha ngô</b>.",
          "small"),
    ))
    return st


# ==========================================================================
def _dang_luong_giac():
    st = []
    st.append(CondPageBreak(10.2 * cm))
    st.append(P("Dạng 13. Giá trị lượng giác của một góc từ 0° đến 180°", "h2"))
    st.append(method([
        P("Góc đặc biệt (30°, 45°, 60°, …) và góc bù: dùng <b>sin bù, cos đối dấu</b>.", "small"),
        P("Biết một giá trị lượng giác: dùng <b>sin²α + cos²α = 1</b> rồi <b>xét dấu</b> theo khoảng của α.",
          "small"),
        P("Rút gọn biểu thức: đưa về sin²α + cos²α = 1, hoặc chia cả tử và mẫu cho cos α (hoặc sin α) "
          "để xuất hiện tan α, cot α.", "small"),
        P("Nếu α là góc tù (90° &lt; α &lt; 180°): sin α &gt; 0, còn cos α, tan α, cot α đều <b>âm</b>.",
          "small"),
    ]))
    st.append(ex("a) Tính sin 120°, cos 135°, tan 150°, cot 120°.<br/>"
                 "b) Cho cos α = −1/3 với 90° &lt; α &lt; 180°. Tính sin α, tan α, cot α.<br/>"
                 "c) Với cos α = −1/3 như trên, tính P = 2sin²α + 3cos²α."))
    st.append(sol(
        P("a) sin 120° = sin 60° = <b>√3/2</b>;  cos 135° = −cos 45° = <b>−√2/2</b>;", "small"),
        P("tan 150° = −tan 30° = <b>−√3/3</b>;  "
          "cot 120° = cos 120°/sin 120° = (−1/2)/(√3/2) = <b>−√3/3</b>.", "small"),
        P("b) sin²α = 1 − cos²α = 1 − 1/9 = 8/9 ⇒ sin α = ±2√2/3. Vì 90° &lt; α &lt; 180° nên sin α &gt; 0, "
          "do đó <b>sin α = 2√2/3</b>. Suy ra tan α = sin α/cos α = <b>−2√2</b>, "
          "cot α = 1/tan α = <b>−√2/4</b>.", "small"),
        P("c) P = 2sin²α + 3cos²α = 2(sin²α + cos²α) + cos²α = 2 + 1/9 = <b>19/9</b>. "
          "(Kĩ thuật: tách 3cos²α = 2cos²α + cos²α để dùng hệ thức cơ bản.)", "small"),
    ))

    st.append(P("Dạng 14. Định lí côsin – tính cạnh, góc, trung tuyến, diện tích", "h2"))
    st.append(method([
        P("Biết 2 cạnh và góc xen giữa → tính cạnh thứ ba bằng <b>định lí côsin</b>.", "small"),
        P("Biết 3 cạnh → tính góc bằng <b>hệ quả định lí côsin</b> (chọn góc có mẫu số “đẹp” để tính nhanh).",
          "small"),
        P("Diện tích: dùng <b>S = (1/2)ab sin C</b> nếu biết góc; dùng <b>Heron</b> nếu biết 3 cạnh.", "small"),
        P("Trung tuyến: <b>m<sub>a</sub>² = (b² + c²)/2 − a²/4</b>.", "small"),
    ]))
    st.append(ex("Cho tam giác ABC có a = 7, b = 8, c = 5. Tính góc A, góc B (làm tròn đến độ), "
                 "diện tích S, bán kính R, r và độ dài trung tuyến m<sub>a</sub>."))
    st.append(sol(
        P("cos A = (b² + c² − a²)/(2bc) = (64 + 25 − 49)/(2·8·5) = 40/80 = 1/2 ⇒ <b>A = 60°</b>.", "small"),
        P("cos B = (c² + a² − b²)/(2ca) = (25 + 49 − 64)/(2·5·7) = 10/70 = 1/7 ⇒ "
          "<b>B ≈ 81°47′</b>. Suy ra C ≈ 38°13′.", "small"),
        P("S = (1/2)·b·c·sin A = (1/2)·8·5·(√3/2) = <b>10√3 ≈ 17,32</b>. "
          "Kiểm tra bằng Heron: p = 10, S = √(10·3·2·5) = √300 = 10√3 ✓", "small"),
        P("R = a/(2 sin A) = 7/(2·(√3/2)) = 7/√3 = <b>7√3/3 ≈ 4,04</b>;  "
          "r = S/p = 10√3/10 = <b>√3 ≈ 1,73</b>.", "small"),
        P("m<sub>a</sub>² = (b² + c²)/2 − a²/4 = 89/2 − 49/4 = (178 − 49)/4 = 129/4 ⇒ "
          "<b>m<sub>a</sub> = √129/2 ≈ 5,68</b>.", "small"),
    ))

    st.append(P("Dạng 15. Định lí sin và công thức diện tích", "h2"))
    st.append(method([
        P("Biết 1 cạnh và góc <b>đối diện</b> cạnh đó → tính R, hoặc tính cạnh khác qua "
          "<b>a/sin A = b/sin B</b>.", "small"),
        P("Biết 2 góc → góc thứ ba = 180° − tổng hai góc.", "small"),
        P("Chọn công thức diện tích phù hợp với dữ kiện: có góc → dùng (1/2)ab sin C; có R → abc/(4R); "
          "có r → pr; có 3 cạnh → Heron.", "small"),
    ]))
    st.append(ex("Cho tam giác ABC có A = 60°, B = 45° và b = 4. Tính a, c, R và diện tích S."))
    st.append(sol(
        P("C = 180° − 60° − 45° = <b>75°</b>.", "small"),
        P("Theo định lí sin: a = b·sin A/sin B = 4·(√3/2)/(√2/2) = 4√3/√2 = <b>2√6 ≈ 4,90</b>.", "small"),
        P("c = b·sin C/sin B = 4·sin 75°/(√2/2). Với sin 75° = (√6 + √2)/4, ta được "
          "c = <b>2(√3 + 1) ≈ 5,46</b>.", "small"),
        P("R = b/(2 sin B) = 4/(2·(√2/2)) = 4/√2 = <b>2√2 ≈ 2,83</b>.", "small"),
        P("S = (1/2)·b·c·sin A = (1/2)·4·2(√3 + 1)·(√3/2) = <b>2√3(√3 + 1) = 6 + 2√3 ≈ 9,46</b>.",
          "small"),
    ))

    st.append(P("Dạng 16. Bài toán thực tiễn: khoảng cách và chiều cao", "h2"))
    st.append(method([
        P("<b>Vẽ hình</b> và xác định tam giác chứa đại lượng cần tìm.", "small"),
        P("Biết 2 cạnh + góc xen giữa (hoặc 3 cạnh) → <b>định lí côsin</b>.", "small"),
        P("Biết 1 cạnh + góc đối diện, hoặc 2 góc → <b>định lí sin</b>.", "small"),
        P("Với bài toán chiều cao: dùng góc nâng, lập phương trình theo chiều cao h rồi giải.", "small"),
        P("<b>Làm tròn</b> theo yêu cầu và ghi đơn vị.", "small"),
    ]))
    st.append(ex("Từ hai điểm A và B trên mặt đất, cách nhau 50 m và cùng nằm trên đường thẳng nối tới "
                 "chân C của một cột cờ, người ta đo được góc nâng của đỉnh cột từ A là 30° và từ B là "
                 "45° (A xa cột hơn B). Tính chiều cao của cột cờ."))
    st.append(sol(
        P("Gọi h là chiều cao cột cờ. Trong tam giác vuông tại C:", "small"),
        P("• Từ B: tan 45° = h/BC ⇒ BC = h.", "small"),
        P("• Từ A: tan 30° = h/AC ⇒ AC = h/tan 30° = h√3.", "small"),
        P("Vì A, B, C thẳng hàng và B nằm giữa A và C: AB = AC − BC = h√3 − h = h(√3 − 1).", "small"),
        P("Do đó h(√3 − 1) = 50 ⇒ h = 50/(√3 − 1) = 50(√3 + 1)/2 = <b>25(√3 + 1) ≈ 68,3 m</b>.", "small"),
    ))
    st.append(tip([
        P("Với bài toán “hai tàu rời bến theo hai hướng tạo với nhau một góc”, hãy tính quãng đường "
          "mỗi tàu đi được trước (v = s/t ⇒ s = v·t), sau đó áp dụng <b>định lí côsin</b> cho tam giác "
          "tạo bởi hai vị trí và bến.", "small")]))
    return st


# ==========================================================================
def _dang_vecto():
    st = []
    st.append(CondPageBreak(10.2 * cm))
    st.append(P("Dạng 17. Khái niệm vectơ: phương, hướng, độ dài, hai vectơ bằng nhau", "h2"))
    st.append(method([
        P("Xét <b>giá</b> (đường thẳng chứa vectơ) để kết luận <b>cùng phương</b> "
          "(giá song song hoặc trùng nhau).", "small"),
        P("Trên cùng một phương, xét chiều mũi tên để phân biệt <b>cùng hướng</b> / <b>ngược hướng</b>.",
          "small"),
        P("<b>Bằng nhau</b> ⇔ <b>cùng hướng</b> và <b>cùng độ dài</b> (thiếu một điều kiện là sai).", "small"),
        P("Vectơ <b>đối</b> của AB là BA: cùng độ dài, ngược hướng.", "small"),
        P("Nhớ: vectơ – không cùng phương, cùng hướng với <b>mọi</b> vectơ và có độ dài bằng 0.", "small"),
    ]))
    st.append(ex("Cho hình bình hành ABCD tâm O (đỉnh theo thứ tự A, B, C, D). Xét tính đúng sai của "
                 "các khẳng định sau:<br/>"
                 "a) AB = CD.   b) AB = DC.   c) |AB| = |CD|.   d) BO = OD.   "
                 "e) Hai vectơ AB và CD cùng phương."))
    st.append(sol(
        P("a) <b>Sai</b>: AB và CD có cùng độ dài nhưng <b>ngược hướng</b> (AB hướng từ A tới B, "
          "CD hướng từ C tới D – ngược chiều trên hai cạnh song song).", "small"),
        P("b) <b>Đúng</b>: AB và DC cùng hướng (đều “đi sang phải” trong hình bình hành) và cùng độ dài "
          "vì AB = DC (hai cạnh đối).", "small"),
        P("c) <b>Đúng</b>: độ dài vectơ là độ dài đoạn thẳng, |AB| = |CD| = AB.", "small"),
        P("d) <b>Đúng</b>: O là trung điểm của BD nên BO và OD cùng hướng, cùng độ dài.", "small"),
        P("e) <b>Đúng</b>: giá của AB và CD là hai đường thẳng song song (chứa hai cạnh đối của hình "
          "bình hành) nên hai vectơ cùng phương.", "small"),
    ))
    st.append(warn([
        P("Câu a và câu e là cặp dễ nhầm: <b>cùng phương</b> chỉ cần giá song song/trùng, còn "
          "<b>bằng nhau</b> cần thêm <b>cùng hướng</b>.", "small"),
    ]))

    st.append(spacing(0.2))
    st.append(P("Bảng tra nhanh: gặp đề bài như thế này thì làm gì?", "h2"))
    st.append(P("Khi đọc một câu hỏi trong đề, hãy dùng bảng dưới đây để xác định ngay dạng toán và "
                "công cụ cần dùng – tiết kiệm thời gian định hướng.", "small"))
    st.append(data_table(
        ["Đề bài cho / hỏi", "Dạng", "Công cụ"],
        [["“Câu nào là mệnh đề / mệnh đề chứa biến”", "1", "Định nghĩa mệnh đề (câu khẳng định đúng–sai)"],
         ["“Mệnh đề phủ định của … là”", "2", "Đổi ∀ ↔ ∃, phủ định vị ngữ"],
         ["“Điều kiện cần / điều kiện đủ / mệnh đề đảo”", "3", "P ⇒ Q, Q ⇒ P, bảng chân trị"],
         ["“Viết tập hợp bằng cách liệt kê / số tập con”", "4", "Giải phương trình, 2<super>n</super>"],
         ["“Tìm A ∩ B, A ∪ B, A \\ B” (liệt kê)", "6", "So phần tử; lưu ý thứ tự hiệu"],
         ["“Tìm A ∩ B, A ∪ B” với khoảng, đoạn", "7", "Vẽ trục số, kiểm tra ngoặc ở đầu mút"],
         ["“Lớp có … thích … , bao nhiêu em không …”", "8", "|A ∪ B| = |A| + |B| − |A ∩ B|"],
         ["“Biểu diễn miền nghiệm của bất phương trình”", "10", "Vẽ bờ d, thử điểm, xét nét liền/đứt"],
         ["“Biểu diễn miền nghiệm của hệ”", "11", "Giao các miền, tìm đỉnh"],
         ["“Để lãi lớn nhất / chi phí nhỏ nhất …”", "12", "Lập hệ, tính F tại các đỉnh"],
         ["“Cho sin α (hoặc cos α), tính …”", "13", "sin²α + cos²α = 1, xét dấu theo khoảng"],
         ["“Tính cạnh / góc / diện tích / trung tuyến”", "14 – 15", "Định lí côsin, định lí sin, công thức S"],
         ["“Khoảng cách hai điểm / chiều cao vật”", "16", "Vẽ tam giác, chọn côsin hay sin"],
         ["“Vectơ nào bằng nhau / cùng phương / cùng hướng”", "17", "Xét giá, chiều, độ dài"]],
        widths=[8.6 * cm, 1.9 * cm, 6.3 * cm], align_center_cols=[1], font_size=8.2))

    st.append(spacing(0.2))
    st.append(note([
        P("Bảng tra này chỉ giúp <b>định hướng trong 10 giây đầu</b> khi đọc đề. Việc thành thạo vẫn "
          "phải đến từ luyện tập: hãy làm lại đề ở Phần C hai lần (lần 1 không giới hạn thời gian, "
          "lần 2 bấm đúng 90 phút).", "small"),
        P("Nếu một câu không nhận ra dạng sau 30 giây, hãy <b>đánh dấu và đi tiếp</b> – "
          "quay lại khi đã làm xong các câu chắc chắn.", "small"),
    ], color=BLUE, bg=TINT_BLUE, title="Cách dùng bảng tra hiệu quả", icon="i"))
    return st
