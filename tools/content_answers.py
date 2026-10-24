# -*- coding: utf-8 -*-
"""PHẦN D – Đáp án và lời giải chi tiết."""
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import CondPageBreak, KeepTogether, PageBreak, Table, TableStyle

import figures
from pdfkit import (
    BLUE, CONTENT_W, GOLD, GREEN, NAVY, RED, SectionBanner, TEAL, TINT_BLUE,
    bullets, callout, data_table, key_table, note, P, S, spacing, tip, warn, LINE,
)
from reportlab.lib.styles import ParagraphStyle


def ans_chip(letter):
    return (f'<font name="DejaVu-Bold" color="#2E6B3E">'
            f'<b>Đáp án: {letter}</b></font>')


def giai(num, letter, *parts):
    """Một câu trắc nghiệm: đáp án + lời giải."""
    head = P(f"<b>Câu {num}.</b>  " + ans_chip(letter), "q")
    body = callout("", list(parts), color=colors.HexColor("#8A99A8"),
                   bg=colors.HexColor("#F7F9FA"), icon="", width=CONTENT_W)
    return [head, body]


def story():
    st = []
    st.append(PageBreak())
    st.append(SectionBanner("PHẦN D", "Đáp án và lời giải chi tiết", NAVY))
    st.append(spacing(0.3))
    st.append(P(
        "Các em hãy tự làm hết đề trước khi xem phần này. Khi chữa bài, đừng chỉ so đáp án: "
        "hãy đọc cả phần <b>giải thích vì sao các phương án khác sai</b> – đó là cách tránh lặp lại lỗi "
        "trong lần kiểm tra thật."))

    # ---------------- đáp án nhanh ----------------
    st.append(P("1. Đáp án nhanh", "h2"))
    st.append(P("Phần I. Trắc nghiệm nhiều phương án lựa chọn", "h3"))
    st.append(key_table([(f"Câu {i+1}", a) for i, a in enumerate(
        ["C", "D", "C", "B", "A", "A", "C", "B", "A", "A", "C", "B"])], cols=6))

    st.append(spacing(0.2))
    st.append(P("Phần II. Trắc nghiệm đúng – sai", "h3"))
    ds = data_table(
        ["Câu", "Ý a", "Ý b", "Ý c", "Ý d", "Điểm tối đa"],
        [["Câu 1", "<b>Đ</b>", "<b>S</b>", "<b>S</b>", "<b>Đ</b>", "1,0"],
         ["Câu 2", "<b>S</b>", "<b>Đ</b>", "<b>S</b>", "<b>Đ</b>", "1,0"]],
        widths=[2.6 * cm, 2.6 * cm, 2.6 * cm, 2.6 * cm, 2.6 * cm, 3.4 * cm],
        align_center_cols=[0, 1, 2, 3, 4, 5])
    st.append(ds)

    st.append(spacing(0.2))
    st.append(P("Phần III. Trắc nghiệm trả lời ngắn", "h3"))
    st.append(key_table([("Câu 1", "32"), ("Câu 2", "5"), ("Câu 3", "−3"), ("Câu 4", "60")], cols=4))

    st.append(spacing(0.15))
    st.append(note([
        P("Phần IV (tự luận): đáp số lần lượt là "
          "<b>a) (1; 3)  b) [−2; 5]  c) [−2; 1]  d) (−∞; −2) ∪ [3; +∞)</b>; "
          "<b>≈ 72,1 km</b>; <b>40 áo và 20 quần, lãi 2 200 000 đồng</b>.", "small")],
        color=BLUE, bg=TINT_BLUE, title="Đáp số phần tự luận", icon="i"))

    # ---------------- giải chi tiết I ----------------
    st.append(CondPageBreak(10.2 * cm))
    st.append(P("2. Lời giải chi tiết – Phần I (trắc nghiệm nhiều phương án)", "h2"))

    st += giai(1, "C",
               P("• A sai: “x + 1 &gt; 2” chứa biến x chưa được gán giá trị nên là <b>mệnh đề chứa biến</b>.", "small"),
               P("• B sai: câu cảm thán, không khẳng định đúng/sai.", "small"),
               P("• <b>C đúng</b>: “17 là số nguyên tố” là câu khẳng định và là khẳng định <b>đúng</b> "
                 "(17 chỉ chia hết cho 1 và chính nó), nên là mệnh đề.", "small"),
               P("• D sai: câu hỏi, không phải mệnh đề.", "small"))

    st += giai(2, "D",
               P("<b>Quy tắc:</b> phủ định của “∀x ∈ X, P(x)” là “∃x ∈ X, ¬P(x)”. ", "small"),
               P("Ở đây X = ℝ, P(x) là “x² + x + 1 &gt; 0”, nên ¬P(x) là “x² + x + 1 ≤ 0”. "
                 "Vậy mệnh đề phủ định là <b>∃x ∈ ℝ, x² + x + 1 ≤ 0</b>.", "small"),
               P("• A sai vì giữ nguyên lượng từ ∀ và đổi &gt; thành &lt; (mất dấu “=”).", "small"),
               P("• B sai vì giữ nguyên ∀ (không đổi lượng từ).", "small"),
               P("• C sai vì không phủ định vị ngữ (vẫn là &gt; 0).", "small"),
               P("<i>Kiểm tra thêm:</i> x² + x + 1 = (x + 1/2)² + 3/4 &gt; 0 với mọi x nên P đúng, "
                 "suy ra mệnh đề phủ định phải <b>sai</b> – phù hợp với phương án D "
                 "(vì không tồn tại x để x² + x + 1 ≤ 0).", "small"))

    st += giai(3, "C",
               P("Giải phương trình: x² − 3x + 2 = 0 ⇔ (x − 1)(x − 2) = 0 ⇔ x = 1 hoặc x = 2.", "small"),
               P("Cả hai nghiệm đều là số thực nên <b>A = {1; 2}</b>.", "small"),
               P("• A, D sai vì chứa số −2 không là nghiệm; B sai vì viết sai dấu ngoặc "
                 "(dùng ngoặc đơn là kí hiệu một khoảng của ℝ, không phải tập liệt kê).", "small"))

    st += giai(4, "B",
               P("Vùng tô màu là <b>phần chung</b> của hai hình tròn biểu diễn A và B, "
                 "tức là tập hợp các phần tử vừa thuộc A vừa thuộc B.", "small"),
               P("Theo định nghĩa, đó chính là giao: <b>A ∩ B</b>.", "small"),
               P("• A sai: A ∪ B là toàn bộ hai hình tròn. • C sai: A \\ B là phần của A nằm ngoài B. "
                 "• D sai: B \\ A là phần của B nằm ngoài A.", "small"))

    st += giai(5, "A",
               P("<b>2x + 3y &lt; 5</b> có dạng ax + by &lt; c với a = 2, b = 3, c = 5; "
                 "a và b không đồng thời bằng 0 nên là bất phương trình bậc nhất hai ẩn.", "small"),
               P("• B sai vì chứa x² (ẩn bậc hai). • C sai vì có ẩn ở mẫu (1/y). "
                 "• D sai vì có ba ẩn x, y, z.", "small"))

    st += giai(6, "A",
               P("Hệ A gồm hai bất phương trình bậc nhất hai ẩn (x + y &gt; 1 và 2x − y ≤ 3).", "small"),
               P("• B có x²; C có 1/x; D có ba ẩn z. Chỉ <b>hệ A</b> thoả mãn định nghĩa.", "small"))

    st += giai(7, "C",
               P("Với 90° &lt; α &lt; 180° (góc tù): <b>sin α &gt; 0</b>, còn "
                 "<b>cos α &lt; 0, tan α &lt; 0, cot α &lt; 0</b>.", "small"),
               P("Vì thế A sai (sin dương), B sai (cos âm), D sai (cot âm), chỉ <b>C đúng</b>.", "small"),
               P("<i>Ví dụ kiểm chứng:</i> α = 120° ⇒ sin = √3/2 &gt; 0, cos = −1/2 &lt; 0, "
                 "tan = −√3 &lt; 0.", "small"))

    st += giai(8, "B",
               P("Từ sin²α + cos²α = 1: cos²α = 1 − (3/5)² = 1 − 9/25 = 16/25 ⇒ cos α = ±4/5.", "small"),
               P("Vì 90° &lt; α &lt; 180° nên cos α &lt; 0. Do đó <b>cos α = −4/5</b>.", "small"),
               P("• A sai vì chọn sai dấu. • C sai vì đảo ngược tử và mẫu. "
                 "• D sai vì nhầm với tan α.", "small"))

    st += giai(9, "A",
               P("Theo định lí côsin: bình phương một cạnh bằng tổng bình phương hai cạnh kia "
                 "<b>trừ</b> hai lần tích của chúng nhân với cosin góc xen giữa. Cạnh a đối diện góc A nên:",
                 "small"),
               P("<b>a² = b² + c² − 2bc·cos A</b>.", "formula"),
               P("• B sai vì dấu “+”. • C sai vì thiếu hệ số 2. • D sai vì dùng góc B thay cho góc A.", "small"))

    st += giai(10, "A",
               P("Áp dụng định lí côsin với góc A = 60° xen giữa hai cạnh AB = 5 và AC = 8:", "small"),
               P("BC² = AB² + AC² − 2·AB·AC·cos A = 25 + 64 − 2·5·8·(1/2) = 89 − 40 = 49.", "small"),
               P("Suy ra <b>BC = √49 = 7</b>.", "small"),
               P("• B sai vì quên trừ (√89). • D sai vì cộng thay vì trừ. "
                 "• C sai vì quên khai căn.", "small"))

    st += giai(11, "C",
               P("Khẳng định <b>C sai</b>: hai vectơ cùng phương có thể <b>cùng hướng</b> hoặc "
                 "<b>ngược hướng</b>. Chẳng hạn trong hình bình hành ABCD, AB và CD cùng phương "
                 "nhưng ngược hướng.", "small"),
               P("• A, B đúng theo tính chất đặc biệt của vectơ – không. • D đúng theo định nghĩa độ dài.", "small"))

    st += giai(12, "B",
               P("Trong hình bình hành ABCD: hai cạnh AB và DC <b>song song, bằng nhau</b> và "
                 "<b>cùng hướng</b> (cùng chiều từ trái sang phải trên hình). Do đó <b>AB = DC</b>.", "small"),
               P("• A sai: AB và CD <b>ngược hướng</b> (cùng độ dài nhưng khác hướng nên không bằng nhau).",
                 "small"),
               P("• C sai: AB và BC không cùng phương. • D sai: AC và BD là hai đường chéo, "
                 "không cùng phương (trừ trường hợp đặc biệt).", "small"))

    # ---------------- giải chi tiết II ----------------
    st.append(CondPageBreak(10.2 * cm))
    st.append(P("3. Lời giải chi tiết – Phần II (đúng – sai)", "h2"))
    st.append(P(
        "Với dạng câu này, các em nên xử lý từng ý độc lập: một ý sai <b>không</b> ảnh hưởng đến các ý "
        "khác. Hãy ghi rõ Đ/S ra nháp trước khi tô, và <b>không bỏ trống</b> ý nào.", "small"))

    st.append(P("Câu 1. Cho A = (−∞; 3] và B = [−2; 5)", "h3"))
    c1 = data_table(
        ["Ý", "Mệnh đề", "Kết luận", "Giải thích"],
        [["a", "3 ∈ (−∞; 3)", "<b>Sai</b>",
          "Tập (−∞; 3) <b>không lấy</b> điểm 3 (ngoặc tròn), nên 3 ∉ (−∞; 3). "
          "Lưu ý 3 ∈ (−∞; 3] là đúng."],
         ["b", "Trục số: đoạn nối −2 và 5, tô đậm −2, để trống 5", "<b>Đúng</b>",
          "B = [−2; 5): lấy −2 (ngoặc vuông) và không lấy 5 (ngoặc tròn). Phát biểu mô tả đúng."],
         ["c", "A ∩ B = (−2; 3]", "<b>Sai</b>",
          "A ∩ B = [−2; 3] vì −2 ∈ B (B lấy −2) và 3 ∈ A (A lấy 3). Mệnh đề đã bỏ sót đầu mút −2 "
          "và dùng sai ngoặc tại 3."],
         ["d", "ℝ \\ B = (−∞; −2) ∪ [5; +∞)", "<b>Đúng</b>",
          "Phần bù của [−2; 5) trong ℝ là phần còn lại: bỏ đoạn [−2; 5), tức là "
          "(−∞; −2) ∪ [5; +∞). Đúng cả về ngoặc."]],
        widths=[1.0 * cm, 4.6 * cm, 1.9 * cm, 9.3 * cm], align_center_cols=[0, 2])
    st.append(c1)

    st.append(spacing(0.2))
    st.append(P("Câu 2. Cho bất phương trình 2x − y ≤ 3 (1)", "h3"))
    c2 = data_table(
        ["Ý", "Mệnh đề", "Kết luận", "Giải thích"],
        [["a", "(1; −2) là một nghiệm của (1)", "<b>Sai</b>",
          "Thay x = 1, y = −2: 2·1 − (−2) = 4 &gt; 3, không thoả mãn. Cần chú ý dấu khi trừ số âm."],
         ["b", "O(0; 0) thuộc miền nghiệm", "<b>Đúng</b>",
          "Thay x = y = 0: 0 − 0 = 0 ≤ 3, thoả mãn nên O là nghiệm, do đó O thuộc miền nghiệm."],
         ["c", "Miền nghiệm là nửa mặt phẳng bờ d không chứa O (kể cả bờ)", "<b>Sai</b>",
          "Vì O là nghiệm nên miền nghiệm là nửa mặt phẳng bờ d <b>chứa</b> O (kể cả bờ d vì có dấu ≤)."],
         ["d", "2x + y ≤ 3 mô tả điều kiện của x, y", "<b>Đúng</b>",
          "Mỗi sản phẩm loại I cần 2 giờ, loại II cần 1 giờ, tổng không vượt quá 3 giờ ⇒ "
          "2x + y ≤ 3 (và thực tế còn cần x ≥ 0, y ≥ 0)."]],
        widths=[1.0 * cm, 4.6 * cm, 1.9 * cm, 9.3 * cm], align_center_cols=[0, 2])
    st.append(c2)

    st.append(spacing(0.2))
    st.append(warn([
        P("Nếu chỉ đúng 1 ý, các em vẫn được 0,1 điểm – <b>đừng bỏ trống</b>. Nhưng cũng đừng đoán bừa: "
          "hãy thay số/kiểm tra bằng phản ví dụ, mỗi ý chỉ mất khoảng 30 giây.", "small")]))

    # ---------------- giải chi tiết III ----------------
    st.append(CondPageBreak(10.2 * cm))
    st.append(P("4. Lời giải chi tiết – Phần III (trả lời ngắn)", "h2"))

    st.append(P("<b>Câu 1.</b> Số tập con của A = {1; 2; 3; 4; 5}  →  <b>32</b>", "q"))
    st.append(callout("", [
        P("Tập hợp A có n = 5 phần tử. Mỗi tập con được tạo bằng cách <b>quyết định lấy hoặc không lấy</b> "
          "từng phần tử, nên có 2·2·2·2·2 = 2⁵ = <b>32</b> tập con (kể cả tập rỗng ∅ và chính A).", "small"),
        P("Nếu đề hỏi “số tập con <b>khác rỗng</b>” thì đáp số là 32 − 1 = 31; "
          "“số tập con có đúng 1 phần tử” là 5.", "small"),
    ], color=colors.HexColor("#8A99A8"), bg=colors.HexColor("#F7F9FA"), icon=""))

    st.append(P("<b>Câu 2.</b> Số học sinh không tham gia câu lạc bộ nào  →  <b>5</b>", "q"))
    st.append(callout("", [
        P("Gọi A là tập học sinh tham gia CLB Toán, B là tập học sinh tham gia CLB Tin học. "
          "Ta có |A| = 25, |B| = 20, |A ∩ B| = 10.", "small"),
        P("Số học sinh tham gia ít nhất một CLB: |A ∪ B| = 25 + 20 − 10 = 35.", "small"),
        P("Số học sinh không tham gia CLB nào: 40 − 35 = <b>5</b> học sinh.", "small"),
    ], color=colors.HexColor("#8A99A8"), bg=colors.HexColor("#F7F9FA"), icon=""))

    st.append(P("<b>Câu 3.</b> Giá trị của P = 5cos α + 1  →  <b>−3</b>", "q"))
    st.append(callout("", [
        P("Từ sin²α + cos²α = 1: cos²α = 1 − 9/25 = 16/25 ⇒ cos α = ±4/5.", "small"),
        P("Vì 90° &lt; α &lt; 180° (góc tù) nên cos α &lt; 0 ⇒ <b>cos α = −4/5</b>.", "small"),
        P("Do đó P = 5·(−4/5) + 1 = −4 + 1 = <b>−3</b>.", "small"),
    ], color=colors.HexColor("#8A99A8"), bg=colors.HexColor("#F7F9FA"), icon=""))

    st.append(P("<b>Câu 4.</b> Số đo góc A  →  <b>60°</b>", "q"))
    st.append(callout("", [
        P("Dùng hệ quả định lí côsin với góc A (đối diện cạnh BC = 7, hai cạnh kề là AB = 5, AC = 8):",
          "small"),
        P("cos A = (AB² + AC² − BC²)/(2·AB·AC) = (25 + 64 − 49)/(2·5·8) = 40/80 = 1/2.", "small"),
        P("Vậy <b>A = 60°</b>. (Có thể kiểm tra nhanh bằng máy tính: shift + cos 0,5 = 60°.)", "small"),
    ], color=colors.HexColor("#8A99A8"), bg=colors.HexColor("#F7F9FA"), icon=""))

    # ---------------- giải chi tiết IV ----------------
    st.append(CondPageBreak(10.2 * cm))
    st.append(P("5. Lời giải chi tiết – Phần IV (tự luận)", "h2"))
    st.append(P("Phần này chấm theo <b>thang điểm từng bước</b>. Ngay cả khi kết quả cuối sai, "
                "các em vẫn được điểm ở những bước đúng – vì thế hãy trình bày đủ bước.", "small"))

    # câu 1
    st.append(KeepTogether([
        P("Câu 1 (1,0 điểm). Cho A = [−2; 3) và B = (1; 5]", "h3"),
        callout("", [
        P("<b>a) A ∩ B = (1; 3).</b>  <font color='#5A6672'>(0,25 đ)</font>", "small"),
        P("Phần chung: từ 1 đến 3. Không lấy 1 vì B dùng ngoặc tròn; không lấy 3 vì A dùng ngoặc tròn.",
          "small"),
        P("<b>b) A ∪ B = [−2; 5].</b>  <font color='#5A6672'>(0,25 đ)</font>", "small"),
        P("Gộp hai tập: lấy −2 (A lấy) và lấy 5 (B lấy).", "small"),
        P("<b>c) A \\ B = [−2; 1].</b>  <font color='#5A6672'>(0,25 đ)</font>", "small"),
        P("Phần của A không thuộc B là đoạn từ −2 đến 1; 1 ∉ B (B bỏ 1) nên 1 vẫn thuộc A \\ B.",
          "small"),
        P("<b>d) C<sub>ℝ</sub>A = ℝ \\ A = (−∞; −2) ∪ [3; +∞).</b>  "
          "<font color='#5A6672'>(0,25 đ)</font>", "small"),
        P("Phần bù đảo ngoặc: A lấy −2 nên phần bù bỏ −2 (ngoặc tròn); A bỏ 3 nên phần bù lấy 3 "
          "(ngoặc vuông).", "small"),
        ], color=colors.HexColor("#8A99A8"), bg=colors.HexColor("#F7F9FA"),
                icon=""),
    ]))

    st.append(spacing(0.1))
    st.append(warn([
        P("Ba lỗi làm mất điểm câu này: (1) quên dấu “=” ở đầu mút; (2) viết A ∪ B = (−2; 5) "
          "(nhầm ngoặc); (3) tính A \\ B thành (−∞; 1] hoặc [−2; 1).", "small")]))

    # câu 2
    st.append(CondPageBreak(10.2 * cm))
    st.append(KeepTogether([
        P("Câu 2 (1,0 điểm). Hai tàu thuỷ rời bến C theo hai hướng tạo với nhau góc 60°", "h3"),
        callout("", [
        P("<b>Bước 1 – Quãng đường mỗi tàu đi được sau 2 giờ</b>  <font color='#5A6672'>(0,25 đ)</font>",
          "small"),
        P("Tàu thứ nhất: CA = 30·2 = 60 (km). Tàu thứ hai: CB = 40·2 = 80 (km).", "small"),
        P("<b>Bước 2 – Áp dụng định lí côsin cho tam giác ABC</b>  "
          "<font color='#5A6672'>(0,25 đ)</font>", "small"),
        P("AB² = CA² + CB² − 2·CA·CB·cos 60°", "formula"),
        P("AB² = 60² + 80² − 2·60·80·(1/2) = 3600 + 6400 − 4800 = 5200.  "
          "<font color='#5A6672'>(0,25 đ)</font>", "small"),
        P("<b>Bước 3 – Kết luận</b>  <font color='#5A6672'>(0,25 đ)</font>", "small"),
        P("AB = √5200 = 20√13 ≈ <b>72,1 (km)</b>.", "small"),
        P("<b>Vậy sau 2 giờ, hai tàu cách nhau khoảng 72,1 km.</b>", "small"),
        ], color=colors.HexColor("#8A99A8"), bg=colors.HexColor("#F7F9FA"),
                icon=""),
        tip([
            P("Có thể trình bày bằng tam giác vuông/định lí côsin đều được. Điểm quan trọng là phải "
              "<b>tính đúng quãng đường trước</b> rồi mới áp dụng công thức – nhiều bạn dùng nhầm "
              "30 và 40 (vận tốc) thay vì 60 và 80 (quãng đường).", "small")]),
    ]))

    # câu 3
    st.append(spacing(0.15))
    st.append(KeepTogether([
        P("Câu 3 (1,0 điểm). Bài toán tối ưu – xưởng may", "h3"),
        callout("", [
        P("<b>Bước 1 – Đặt ẩn và lập hệ bất phương trình</b>  "
          "<font color='#5A6672'>(0,25 đ)</font>", "small"),
        P("Gọi x là số áo, y là số quần cần may (x ≥ 0, y ≥ 0 là các số tự nhiên).", "small"),
        P("Vải: 2x + y ≤ 100.   Giờ công: x + 2y ≤ 80.", "small"),
        P("Hệ bất phương trình: <b>2x + y ≤ 100;  x + 2y ≤ 80;  x ≥ 0;  y ≥ 0.</b>", "small"),
        P("Tiền lãi (nghìn đồng): <b>F = 40x + 30y</b>.", "small"),
        P("<b>Bước 2 – Miền nghiệm và các đỉnh</b>  <font color='#5A6672'>(0,25 đ)</font>", "small"),
        P("Miền nghiệm là tứ giác OABC với O(0; 0), A(50; 0), B(40; 20), C(0; 40); "
          "B là giao điểm của hai đường thẳng 2x + y = 100 và x + 2y = 80 (giải hệ được x = 40, y = 20).",
          "small"),
        figures.feasible_region(width=CONTENT_W - 90, height=196),
        P("<b>Bước 3 – Tính F tại các đỉnh</b>  <font color='#5A6672'>(0,25 đ)</font>", "small"),
        P("F(O) = 0;   F(A) = 40·50 = 2000;   F(B) = 40·40 + 30·20 = 2200;   F(C) = 30·40 = 1200.",
          "small"),
        P("Giá trị lớn nhất là <b>F = 2200</b> tại <b>B(40; 20)</b>.", "small"),
        P("<b>Bước 4 – Kết luận</b>  <font color='#5A6672'>(0,25 đ)</font>", "small"),
        P("Xưởng cần may <b>40 chiếc áo và 20 chiếc quần</b>, khi đó tiền lãi lớn nhất là "
          "2 200 nghìn đồng, tức <b>2 200 000 đồng</b>.", "small"),
        ], color=colors.HexColor("#8A99A8"), bg=colors.HexColor("#F7F9FA"),
                icon=""),
    ]))

    st.append(spacing(0.05))
    st.append(warn([
        P("Nhiều học sinh chỉ thử tại A(50; 0) – cho lãi 2 000 – và kết luận ngay. Hãy nhớ: "
          "<b>phải tính F tại tất cả các đỉnh</b> rồi mới so sánh.", "small")]))

    return st
