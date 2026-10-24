#!/usr/bin/env python3
"""Answer key, worked solutions, coverage audit and references."""
from __future__ import annotations

from reportlab.lib.units import mm
from reportlab.platypus import Flowable, PageBreak, Spacer

from guide.pdfguide import CONTENT_W, GuideBuilder, feasible_region


def add_solutions(b: GuideBuilder, story: list[Flowable]) -> None:
    # ------------------------------------------------------------------
    story += [PageBreak(), b.h1("PHẦN VIII • ĐÁP ÁN VÀ LỜI GIẢI CHI TIẾT")]
    story.append(b.box("Cách dùng phần lời giải", [
        "Trước hết tự chấm bằng đáp án nhanh. Với câu sai, che lời giải và làm lại; chỉ đọc từng dòng khi thực sự bí. "
        "Ghi lỗi theo bốn nhóm K (kiến thức), B (biến đổi), Đ (đọc đề), T (thời gian) để ôn lại có mục tiêu."
    ], "tip"))

    story.append(b.h2("8.1. Đáp án nhanh"))
    story.append(b.h3("Phần I – Mỗi câu 0,25 điểm"))
    story.append(b.table([
        ["Câu", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
        ["Đáp án", "C", "A", "B", "D", "B", "A", "D", "C", "A", "D", "B", "C"],
    ], [20 * mm] + [(CONTENT_W - 20 * mm) / 12] * 12))
    story.append(b.h3("Phần II – Đúng–sai"))
    story.append(b.table([
        ["Câu", "a", "b", "c", "d"],
        ["1", "Đúng", "Đúng", "Sai", "Đúng"],
        ["2", "Đúng", "Sai", "Đúng", "Sai"],
    ], [25 * mm] + [(CONTENT_W - 25 * mm) / 4] * 4))
    story.append(b.h3("Phần III – Trả lời ngắn"))
    story.append(b.table([
        ["Câu", "1", "2", "3", "4"],
        ["Đáp số", "32", "8", "−5,5", "7"],
    ], [25 * mm] + [(CONTENT_W - 25 * mm) / 4] * 4))
    story.append(b.p("Phần IV: Câu 1 và Câu 2 xem kết quả cùng thang điểm bên dưới; Câu 3: 20 sản phẩm X, 20 sản phẩm Y, lợi nhuận lớn nhất 14 triệu đồng."))

    story.append(b.h2("8.2. Giải thích Phần I – Trắc nghiệm nhiều phương án"))
    mc_solutions = [
        (1, "C", "“7 là số nguyên tố” là khẳng định đúng, nên là mệnh đề. A là câu hỏi, D là câu mệnh lệnh; B chứa biến $x$ nên chưa có tính đúng–sai khi chưa biết $x$."),
        (2, "A", "Phủ định của $\\forall x\\in\\mathbb R,P(x)$ là $\\exists x\\in\\mathbb R,\\overline{P(x)}$. Phủ định của $x^2+1>0$ là $x^2+1\\le0$."),
        (3, "B", "Các số nguyên thỏa mãn $-2\\le x<2$ là $-2,-1,0,1$. Lấy $-2$ vì dấu $\\le$, không lấy $2$ vì dấu $<$."),
        (4, "D", "Phần tô màu là phần chung của $A$ và $B$, tức $A\\cap B$."),
        (5, "B", "$2x-y+1<0$ có dạng $ax+by+c<0$. A có $x^2$, C có tích $xy$, D là phương trình và có $y^2$."),
        (6, "A", "Cả hai bất phương trình ở A đều bậc nhất với cùng hai ẩn $x,y$. B có $x^2$, C có $xy$, D là hệ phương trình."),
        (7, "D", "Hai góc bù nhau có côsin đối nhau: $\\cos(180^\\circ-\\alpha)=-\\cos\\alpha$."),
        (8, "C", "$\\sin^2\\alpha=1-9/25=16/25$. Vì $\\alpha$ tù nên $\\sin\\alpha>0$, do đó $\\sin\\alpha=4/5$."),
        (9, "A", "Định lí côsin cho cạnh $a$ đối diện góc $A$: $a^2=b^2+c^2-2bc\\cos A$."),
        (10, "D", "$S=\\frac12\\cdot AB\\cdot AC\\cdot\\sin A=\\frac12\\cdot4\\cdot6\\cdot\\frac{\\sqrt3}{2}=6\\sqrt3$."),
        (11, "B", "Theo quy ước trong nội dung kiểm tra, vectơ-không cùng phương và cùng hướng với mọi vectơ. Vectơ-không có độ dài 0."),
        (12, "C", "$\\overrightarrow{AB}$ và $\\overrightarrow{DC}$ cùng hướng, đồng thời $AB=DC$ do hai cạnh đối của hình bình hành. Vậy chúng bằng nhau."),
    ]
    for number, answer, explanation in mc_solutions:
        story.append(b.p(f"<b>Câu {number} — {answer}.</b> {explanation}"))

    story.append(b.h2("8.3. Giải thích Phần II – Đúng–sai"))
    story.append(b.h3("Câu 1 • Tập hợp"))
    story.append(b.bullet("<b>a) Đúng.</b> Phần tử 2 xuất hiện trong $A=\\{1;2;3;4\\}$ nên $2\\in A$."))
    story.append(b.bullet("<b>b) Đúng.</b> Điểm đặc tại $-2$ biểu thị $-2$ được lấy; điểm rỗng tại $3$ biểu thị $3$ bị loại. Đó là $[-2;3)$."))
    story.append(b.bullet("<b>c) Sai.</b> Giao chỉ gồm phần tử chung: $A\\cap B=\\{2;4\\}$. Tập $\\{1;2;3;4;6\\}$ không phải $A\\cap B$."))
    story.append(b.bullet("<b>d) Đúng.</b> $A\\cup B=\\{1;2;3;4;6\\}$. Trong $E=\\{1;2;3;4;5;6\\}$ chỉ còn 5 không thuộc hợp, nên $C_E(A\\cup B)=\\{5\\}$."))

    story.append(b.h3("Câu 2 • Bất phương trình bậc nhất hai ẩn"))
    story.append(b.bullet("<b>a) Đúng.</b> Thay $(1;0)$: $2\\cdot1-0-4=-2\\le0$."))
    story.append(b.bullet("<b>b) Sai.</b> Thay $O(0;0)$: $-4\\le0$, đúng. Vậy miền nghiệm là phía <b>chứa</b> $O$, kể cả $d$ vì dấu $\\le$."))
    story.append(b.bullet("<b>c) Đúng.</b> Thay $M(0;5)$: $2\\cdot0-5-4=-9\\le0$, nên $M$ thuộc miền nghiệm."))
    story.append(b.bullet("<b>d) Sai.</b> “Không vượt quá 4 kg” nghĩa là nhỏ hơn hoặc bằng 4, phải viết $2x+y\\le4$ (cùng $x,y\\ge0$), không phải dấu $<$."))
    story.append(b.box("Tự chấm đúng–sai theo ma trận", [
        "Mỗi câu được tính riêng: đúng 1 ý 0,1 điểm; 2 ý 0,25; 3 ý 0,5; 4 ý 1,0. "
        "Không cộng điểm theo số ý đúng ở cả hai câu rồi mới quy đổi."
    ], "remember"))

    story.append(b.h2("8.4. Lời giải Phần III – Trả lời ngắn"))
    story.append(b.h3("Câu 1 • Đáp số 32"))
    story.append(b.p("Tập có 5 phần tử có $2^5=32$ tập con (bao gồm $\\varnothing$ và chính tập đã cho)."))
    story.append(b.h3("Câu 2 • Đáp số 8"))
    story.append(b.p("Số học sinh chơi ít nhất một môn: $24+17-9=32$. Phải trừ 9 vì nhóm chơi cả hai môn bị đếm hai lần. Số bạn không chơi môn nào: $40-32=8$."))
    story.append(b.h3("Câu 3 • Đáp số −5,5"))
    story.append(b.p("Ta có $\\cos^2\\alpha=1-(3/5)^2=16/25$. Vì $\\alpha$ tù nên $\\cos\\alpha=-4/5$ và $\\tan\\alpha=(3/5):(-4/5)=-3/4$."))
    story.extend(b.formula(r"P=5\left(-\frac45\right)+2\left(-\frac34\right)=-4-\frac32=-\frac{11}{2}=-5{,}5."))
    story.append(b.h3("Câu 4 • Đáp số 7"))
    story.append(b.p("Áp dụng định lí côsin:"))
    story.extend(b.formula(r"BC^2=AC^2+AB^2-2\cdot AC\cdot AB\cdot\cos A=8^2+5^2-2\cdot8\cdot5\cdot\frac12=49."))
    story.append(b.p("Vì $BC>0$ nên $BC=7$."))

    story.append(b.h2("8.5. Lời giải Phần IV – Tự luận"))
    story.append(b.h3("Câu 1 • Phép toán tập hợp (1,0 điểm)"))
    story.append(b.p("a) Liệt kê đúng hai tập:"))
    story.extend(b.formula(r"A=\{2;4;6;8;10\},\qquad B=\{3;6;9\}."))
    story.append(b.p("b) Phần chung chỉ có 6; hợp gom mọi phần tử không lặp; phần bù lấy trong $E$ nhưng ngoài $A$:"))
    story.extend(b.formula(r"A\cap B=\{6\},\qquad A\cup B=\{2;3;4;6;8;9;10\}."))
    story.extend(b.formula(r"C_E A=\{1;3;5;7;9\}."))
    story.append(b.table([
        ["Nội dung", "Điểm gợi ý"],
        ["Liệt kê đúng $A,B$", "0,25"],
        ["Tính đúng $A\\cap B$", "0,25"],
        ["Tính đúng $A\\cup B$", "0,25"],
        ["Tính đúng $C_E A$", "0,25"],
    ], [CONTENT_W - 35 * mm, 35 * mm]))

    story.append(b.h3("Câu 2 • Khoảng cách qua hồ nước (1,0 điểm)"))
    story.append(b.p("Xét tam giác $ABC$, biết hai cạnh $AB=50$ m, $AC=80$ m và góc xen giữa $\\widehat{BAC}=60^\\circ$. Áp dụng định lí côsin cho cạnh $BC$:"))
    story.extend(b.formula(r"BC^2=AB^2+AC^2-2\cdot AB\cdot AC\cdot\cos\widehat{BAC}"))
    story.extend(b.formula(r"=50^2+80^2-2\cdot50\cdot80\cdot\cos60^\circ=2500+6400-4000=4900."))
    story.append(b.p("Vậy $BC=\\sqrt{4900}=70$ m. Khoảng cách giữa hai vị trí $B,C$ là <b>70 mét</b>.", "Answer"))
    story.append(b.table([
        ["Nội dung", "Điểm gợi ý"],
        ["Nêu và viết đúng định lí côsin cho $BC$", "0,40"],
        ["Thay số, tính $BC^2=4900$", "0,35"],
        ["Kết luận $BC=70$ m", "0,25"],
    ], [CONTENT_W - 35 * mm, 35 * mm]))

    story.append(b.h3("Câu 3 • Phương án sản xuất tối ưu (1,0 điểm)"))
    story.append(b.p("a) Từ “tổng số sản phẩm không vượt quá 40” và “tối đa 60 kg nguyên liệu”, ta có mô hình:"))
    story.extend(b.formula(r"\begin{cases}x+y\le40,\\2x+y\le60,\\x\ge0,\ y\ge0,\ x,y\in\mathbb Z,\end{cases}\qquad F=400x+300y\ \text{(nghìn đồng)}."))
    story.append(b.p("b) Trước hết xét miền hình học với $x,y\\ge0$. Đường $x+y=40$ cắt hai trục tại $(40;0),(0;40)$, nhưng $(40;0)$ không thỏa mãn $2x+y\\le60$. Đường $2x+y=60$ cắt trục hoành tại $(30;0)$. Giao của hai đường:"))
    story.extend(b.formula(r"\begin{cases}x+y=40\\2x+y=60\end{cases}\Longleftrightarrow \begin{cases}x=20\\y=20.\end{cases}"))
    story.append(b.p("Do đó miền phương án là tứ giác có bốn đỉnh $(0;0),(30;0),(20;20),(0;40)$, kể cả biên."))
    graph = feasible_region()
    graph.hAlign = "CENTER"
    story.append(graph)
    story.append(b.p("Miền gạch/tô màu thỏa mãn đồng thời hai ràng buộc và $x,y\\ge0$.", "Caption"))
    story.append(b.table([
        ["Đỉnh (x; y)", "F = 400x + 300y (nghìn đồng)", "Lợi nhuận"],
        ["$(0;0)$", "$0$", "0 đồng"],
        ["$(30;0)$", "$12\,000$", "12 triệu đồng"],
        ["$(20;20)$", "$14\,000$", "14 triệu đồng"],
        ["$(0;40)$", "$12\,000$", "12 triệu đồng"],
    ], [40 * mm, 75 * mm, CONTENT_W - 115 * mm]))
    story.append(b.p("Biểu thức bậc nhất $F$ đạt giá trị lớn nhất tại một đỉnh của miền đa giác. Đỉnh $(20;20)$ có tọa độ nguyên nên thỏa mãn điều kiện số sản phẩm. Vậy xưởng cần sản xuất <b>20 sản phẩm X và 20 sản phẩm Y</b>; lợi nhuận lớn nhất là <b>14 000 nghìn đồng = 14 triệu đồng</b>.", "Answer"))
    story.append(b.table([
        ["Nội dung", "Điểm gợi ý"],
        ["Lập đúng hệ ràng buộc và $F$", "0,25"],
        ["Xác định đúng bốn đỉnh của miền phương án", "0,30"],
        ["Thay đủ bốn đỉnh và so sánh giá trị $F$", "0,25"],
        ["Kết luận phương án và lợi nhuận với đơn vị", "0,20"],
    ], [CONTENT_W - 35 * mm, 35 * mm]))

    # ------------------------------------------------------------------
    story += [PageBreak(), b.h1("PHẦN IX • PHỤ LỤC ĐỐI CHIẾU TOÀN BỘ BẢNG ĐẶC TẢ")]
    story.append(b.p(
        "Bảng sau chuẩn hóa chính tả và kí hiệu nhưng giữ đủ yêu cầu của từng mục trong DOCX. "
        "“Vị trí ôn” trỏ đến phần lý thuyết/ví dụ; “Đề luyện” trỏ đến câu tương ứng trong Phần VII. "
        "TN = nhiều phương án; ĐS = đúng–sai; TLN = trả lời ngắn; TL = tự luận."
    ))
    coverage = [
        ["Nguồn", "Yêu cầu trong bảng đặc tả", "Vị trí ôn", "Đề luyện"],
        ["1.1 • TN1", "Nhận biết mệnh đề, mệnh đề phủ định, mệnh đề chứa biến.", "II • Bài 1, mục 1.1–1.2", "TN1"],
        ["1.1 • TN2", "Hiểu ý nghĩa kí hiệu phổ biến ∀ và tồn tại ∃.", "II • mục 1.2", "TN2"],
        ["1.2 • TN3", "Cho tập hợp bằng liệt kê phần tử hoặc nêu tính chất đặc trưng.", "II • mục 2.1, Ví dụ 3", "TN3"],
        ["1.2 • ĐS1a", "Dùng đúng kí hiệu tập hợp; nhận biết các khoảng, đoạn, nửa khoảng và kí hiệu vô cực.", "II • mục 2.1–2.2", "ĐS1a"],
        ["1.2 • ĐS1b", "Biểu diễn khoảng/đoạn trên trục số; lấy ví dụ tập hợp, tập con, hai tập bằng nhau.", "II • mục 2.1–2.2", "ĐS1b"],
        ["1.2 • TLN1", "Tìm số tập con của một tập hợp.", "II • mục 2.4", "TLN1"],
        ["1.3 • TN4", "Dùng biểu đồ Ven để biểu diễn giao hoặc hợp của hai tập hợp.", "II • mục 2.3", "TN4"],
        ["1.3 • ĐS1c, TL1", "Thực hiện giao, hợp và phần bù của một tập con (mức thông hiểu).", "II • Ví dụ 4", "ĐS1c; TL1"],
        ["1.3 • ĐS1d", "Thực hiện các phép toán giao, hợp, phần bù ở mức vận dụng.", "II • Ví dụ 4–5", "ĐS1d"],
        ["1.3 • TLN2", "Giải bài toán thực tế bằng các phép toán tập hợp.", "II • Ví dụ 5", "TLN2"],
        ["2.1 • TN5", "Nhận biết bất phương trình bậc nhất hai ẩn.", "III • mục 3.1", "TN5"],
        ["2.1 • ĐS2a", "Nhận biết nghiệm và miền nghiệm trên mặt phẳng tọa độ.", "III • mục 3.1–3.2", "ĐS2a"],
        ["2.1 • ĐS2b,2c", "Mô tả miền nghiệm của bất phương trình bậc nhất hai ẩn.", "III • mục 3.2, Ví dụ 6", "ĐS2b,2c"],
        ["2.1 • ĐS2d", "Chuyển điều kiện thực tế về bất phương trình bậc nhất hai ẩn.", "III • mục 4.2", "ĐS2d"],
        ["2.2 • TN6", "Nhận biết hệ bất phương trình, nghiệm và miền nghiệm của hệ.", "III • Bài 4, mục 4.1", "TN6"],
        ["2.2 • TL3", "Mô tả miền nghiệm của hệ; tìm giá trị tối ưu trong bài toán thực tiễn.", "III • Ví dụ 7; mục 4.2", "TL3"],
        ["3.1 • TN7", "Nhận biết giá trị lượng giác của góc 0°–180°; quan hệ góc phụ/bù; dùng máy tính cầm tay.", "IV • mục 5.1–5.3", "TN7"],
        ["3.1 • TN8", "Tính các giá trị lượng giác khi biết một trong bốn giá trị.", "IV • mục 5.4, Ví dụ 8", "TN8"],
        ["3.1 • TLN3", "Cho một giá trị lượng giác, tính giá trị của một biểu thức.", "IV • Ví dụ 8–9", "TLN3"],
        ["3.2 • TN9", "Nhận biết định lí côsin, định lí sin và công thức diện tích.", "IV • mục 6.1–6.3", "TN9"],
        ["3.2 • TN10, TLN4", "Dùng hệ thức lượng để tính cạnh, góc, diện tích và ứng dụng đơn giản.", "IV • Ví dụ 10–12", "TN10; TLN4"],
        ["3.2 • TL2", "Giải tam giác và bài thực tiễn như đo khoảng cách khi gặp vật cản.", "IV • mục 6.4, Ví dụ 13", "TL2"],
        ["4.1 • TN11", "Nhận biết vectơ, vectơ-không, độ dài, giá, cùng phương/hướng, bằng nhau.", "V • mục 7.1–7.2", "TN11"],
        ["4.1 • TN12", "Thông hiểu các khái niệm vectơ; chứng minh hai vectơ bằng nhau trong trường hợp đơn giản.", "V • Ví dụ 14–15", "TN12"],
    ]
    story.append(b.table(coverage, [25 * mm, 88 * mm, 39 * mm, CONTENT_W - 152 * mm]))
    story.append(b.box("Kết quả đối chiếu", [
        "Đủ <b>12 TN + 2 câu ĐS (8 ý) + 4 TLN + 3 TL</b>; đủ bốn mạch nội dung và các mức độ nhận thức trong ma trận. "
        "Mọi câu của đề luyện đều có đáp án/lời giải. Các yêu cầu ở phần mục tiêu nhưng không gắn với số câu cụ thể "
        "(mệnh đề đảo, tương đương, điều kiện cần–đủ, vectơ đối nhau…) cũng đã được giải thích và có bài luyện ở các chương."
    ], "tip"))

    story.append(b.h2("9.1. Phiếu tự đánh giá sau khi chấm đề"))
    story.append(b.table([
        ["Mạch", "Câu liên quan", "Điểm tối đa", "Điểm của em", "Hành động tiếp theo"],
        ["Mệnh đề – tập hợp", "TN1–4; ĐS1; TLN1–2; TL1", "4,0", "……", "…………………………"],
        ["Bất phương trình – hệ", "TN5–6; ĐS2; TL3", "2,5", "……", "…………………………"],
        ["Lượng giác – tam giác", "TN7–10; TLN3–4; TL2", "3,0", "……", "…………………………"],
        ["Vectơ", "TN11–12", "0,5", "……", "…………………………"],
    ], [37 * mm, 61 * mm, 23 * mm, 25 * mm, CONTENT_W - 146 * mm]))
    story.append(b.p("Ưu tiên ôn lại mạch có tỉ lệ điểm thấp nhất, sau đó làm lại đúng các câu sai trước khi luyện một đề mới."))

    story.append(b.h2("9.2. Nguồn và căn cứ biên soạn"))
    refs = [
        "<b>[1]</b> Trường THPT Hà Huy Tập, <i>MA TRẬN TOÁN 10 - GIỮA KÌ I.docx</i>, năm học 2026–2027: mục tiêu, hình thức, ma trận và bảng đặc tả (tệp nguồn trong kho lưu trữ).",
        "<b>[2]</b> Bộ Giáo dục và Đào tạo, <i>Chương trình Giáo dục phổ thông 2018 – Chương trình môn Toán</i> "
        "(ban hành kèm Thông tư 32/2018/TT-BGDĐT). Cổng thông tin: <link href='https://rgep.moet.gov.vn/' color='#0B7A75'>rgep.moet.gov.vn</link>.",
        "<b>[3]</b> Hà Huy Khoái (Tổng Chủ biên) và các tác giả, <i>Toán 10 – Tập một</i>, bộ <i>Kết nối tri thức với cuộc sống</i>, "
        "NXB Giáo dục Việt Nam. Mục lục tham khảo: <link href='https://toanmath.com/2022/01/sach-giao-khoa-toan-10-tap-1-ket-noi-tri-thuc-voi-cuoc-song.html' color='#0B7A75'>TOANMATH – SGK Toán 10 tập 1 KNTT</link>.",
        "<b>[4]</b> Nhà xuất bản Giáo dục Việt Nam, <i>Hành trang số</i>, kệ sách điện tử Kết nối tri thức với cuộc sống: "
        "<link href='https://hanhtrangso.nxbgd.vn/sach-dien-tu' color='#0B7A75'>hanhtrangso.nxbgd.vn</link>.",
    ]
    for ref in refs:
        story.append(b.p(ref, "Small"))
    story.append(b.p("Các nguồn trực tuyến được tra cứu ngày 24/10/2026 để kiểm chứng tên bài và phạm vi chương trình. Nội dung toán học, hình minh họa, câu hỏi luyện tập và lời giải trong đề cương được biên soạn lại cho mục đích ôn tập; không sao chép đề thi hoặc đáp án từ nguồn ngoài.", "Small"))
    story.append(b.box("Lời nhắc cuối cùng", [
        "Hiểu quy tắc → tự làm một ví dụ → kiểm tra bằng đáp án → ghi lỗi → làm lại sau một ngày. "
        "Đó là cách biến đề cương này thành năng lực làm bài, thay vì chỉ đọc thuộc lời giải."
    ], "remember"))
