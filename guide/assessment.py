#!/usr/bin/env python3
"""Formula sheet and the complete matrix-aligned practice examination."""
from __future__ import annotations

from reportlab.lib.units import mm
from reportlab.platypus import Flowable, KeepTogether, PageBreak, Spacer

from guide.pdfguide import CONTENT_W, GuideBuilder, number_line, parallelogram_diagram, triangle_diagram, venn_intersection


def _center(flowable):
    flowable.hAlign = "CENTER"
    return flowable


def _mc(b: GuideBuilder, story: list[Flowable], number: int, text: str, options: list[str], columns=2, diagram=None):
    block: list[Flowable] = [b.p(f"<b>Câu {number}.</b> {text}", "Question")]
    if diagram is not None:
        block.append(_center(diagram))
    block.append(b.options(options, columns))
    story.append(KeepTogether(block))


def add_formula_and_exam(b: GuideBuilder, story: list[Flowable]) -> None:
    # ------------------------------------------------------------------
    story += [PageBreak(), b.h1("PHẦN VI • PHIẾU CÔNG THỨC & QUY TẮC RA QUYẾT ĐỊNH")]
    story.append(b.p("Chỉ dùng phiếu này để ôn lần cuối. Khi luyện đề, hãy tự viết lại công thức từ trí nhớ rồi mới tra cứu."))

    story.append(b.h2("6.1. Mệnh đề và tập hợp"))
    story.append(b.table([
        ["Tình huống", "Công thức / quy tắc"],
        ["Phủ định lượng từ", "$\\overline{\\forall x,P(x)}\\equiv\\exists x,\\overline{P(x)}$; $\\overline{\\exists x,P(x)}\\equiv\\forall x,\\overline{P(x)}$."],
        ["Kéo theo", "$P\\Rightarrow Q$: $P$ đủ cho $Q$; $Q$ cần cho $P$."],
        ["Tương đương", "$P\\Leftrightarrow Q$ khi cả hai chiều kéo theo đều đúng."],
        ["Số tập con", "Tập có $n$ phần tử có $2^n$ tập con."],
        ["Đếm hợp", "$|A\\cup B|=|A|+|B|-|A\\cap B|$."],
        ["Phần bù", "$C_E A=E\\setminus A$ với $A\\subset E$."],
    ], [43 * mm, CONTENT_W - 43 * mm], compact=True))

    story.append(b.h2("6.2. Bất phương trình bậc nhất hai ẩn"))
    story.append(b.table([
        ["Bước", "Phải làm", "Tự kiểm tra"],
        ["Đường bờ", "Vẽ $ax+by+c=0$ qua hai điểm.", "Nét liền cho $\\le,\\ge$; nét đứt cho $<,>$."],
        ["Điểm thử", "Thay một điểm không thuộc bờ, thường là $O$.", "Đúng → lấy phía chứa điểm; sai → lấy phía còn lại."],
        ["Hệ", "Lấy giao của mọi miền nghiệm.", "Mọi điểm được chọn phải thỏa mãn tất cả bất phương trình."],
        ["Tối ưu", "Tìm đỉnh, thay vào $F=ax+by$, so sánh.", "Miền có bị chặn? Phương án có nguyên/đúng đơn vị không?"],
    ], [25 * mm, 80 * mm, CONTENT_W - 105 * mm], compact=True))

    story.append(b.h2("6.3. Lượng giác và tam giác"))
    story.append(b.table([
        ["Chủ đề", "Công thức"],
        ["Hằng đẳng thức", "$\\sin^2\\alpha+\\cos^2\\alpha=1$; $\\tan\\alpha=\\sin\\alpha/\\cos\\alpha$; $\\cot\\alpha=\\cos\\alpha/\\sin\\alpha$."],
        ["Góc bù", "$\\sin(180^\\circ-\\alpha)=\\sin\\alpha$; cos, tan, cot đổi dấu khi xác định."],
        ["Định lí côsin", "$a^2=b^2+c^2-2bc\\cos A$."],
        ["Định lí sin", "$a/\\sin A=b/\\sin B=c/\\sin C=2R$."],
        ["Diện tích", "$S=\\frac12bc\\sin A=\\frac{abc}{4R}=pr=\\sqrt{p(p-a)(p-b)(p-c)}$."],
        ["Nửa chu vi", "$p=(a+b+c)/2$; cạnh $a=BC,b=CA,c=AB$."],
    ], [38 * mm, CONTENT_W - 38 * mm], compact=True))

    story.append(b.h2("6.4. Vectơ: chuỗi kiểm tra không bỏ sót điều kiện"))
    story.append(b.box("Trước khi kết luận", [
        "<b>Cùng phương?</b> Xét giá song song hoặc trùng. → <b>Cùng hướng hay ngược hướng?</b> Nhìn mũi tên. "
        "→ <b>Độ dài có bằng nhau?</b> Nếu cùng hướng + cùng độ dài thì hai vectơ bằng nhau; nếu ngược hướng + cùng độ dài thì đối nhau.",
        "$|\\overrightarrow{AB}|=AB$; $\\overrightarrow{AA}=\\overrightarrow0$; vectơ-không cùng phương và cùng hướng với mọi vectơ theo quy ước của ma trận."
    ], "remember"))

    # ------------------------------------------------------------------
    story += [PageBreak(), b.h1("PHẦN VII • ĐỀ LUYỆN TẬP BÁM SÁT MA TRẬN")]
    story.append(b.box("Đề luyện tập do tài liệu xây dựng – không phải đề gốc của nhà trường", [
        "Thời gian: <b>90 phút</b>. Tổng: <b>10 điểm</b>. Hãy làm trong một lượt, không xem Phần VIII cho đến khi kết thúc. "
        "Cấu trúc, mạch kiến thức và mức độ được đối chiếu ở Phần IX."
    ], "note"))
    story.append(b.table([
        ["TRƯỜNG THPT HÀ HUY TẬP", "ĐỀ LUYỆN TẬP GIỮA HỌC KÌ I"],
        ["Tổ Toán – Tin", "Môn: TOÁN 10 • Năm học 2026–2027"],
        ["Họ và tên: …………………………………", "Lớp: ……… • Thời gian: 90 phút"],
    ], [CONTENT_W / 2, CONTENT_W / 2], header=False))

    story.append(b.h2("PHẦN I • TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN (3,0 ĐIỂM)"))
    story.append(b.p("Chọn <b>một</b> phương án đúng trong mỗi câu. Mỗi câu 0,25 điểm.", "Small"))
    _mc(b, story, 1, "Khẳng định nào sau đây là một <b>mệnh đề</b>?", [
        "A. “Bạn đã làm bài chưa?”", "B. “$x+3=7$.”", "C. “7 là số nguyên tố.”", "D. “Hãy đọc kĩ đề!”"
    ])
    _mc(b, story, 2, "Phủ định của mệnh đề $P:\\ \\forall x\\in\\mathbb R,\\,x^2+1>0$ là", [
        "A. $\\exists x\\in\\mathbb R,\\,x^2+1\\le0$", "B. $\\forall x\\in\\mathbb R,\\,x^2+1\\le0$",
        "C. $\\exists x\\in\\mathbb R,\\,x^2+1>0$", "D. $\\forall x\\notin\\mathbb R,\\,x^2+1\\le0$"
    ], columns=1)
    _mc(b, story, 3, "Tập hợp $A=\\{x\\in\\mathbb Z\\mid -2\\le x<2\\}$ được viết bằng cách liệt kê là", [
        "A. $\\{-1;0;1;2\\}$", "B. $\\{-2;-1;0;1\\}$", "C. $\\{-2;-1;0;1;2\\}$", "D. $\\{-2;-1;0\\}$"
    ], columns=1)
    _mc(b, story, 4, "Phần tô màu trong biểu đồ Ven sau biểu diễn tập hợp nào?", [
        "A. $A\\cup B$", "B. $A\\setminus B$", "C. $C_E(A\\cap B)$", "D. $A\\cap B$"
    ], diagram=venn_intersection())
    _mc(b, story, 5, "Bất phương trình nào sau đây là bất phương trình bậc nhất hai ẩn $x,y$?", [
        "A. $x^2+y\\ge0$", "B. $2x-y+1<0$", "C. $xy\\le4$", "D. $x+y^2=3$"
    ])
    _mc(b, story, 6, "Hệ nào sau đây là hệ bất phương trình bậc nhất hai ẩn?", [
        "A. $\\begin{cases}x+y\\ge1\\\\2x-y<3\\end{cases}$", "B. $\\begin{cases}x^2+y\\ge0\\\\x-y\\le1\\end{cases}$",
        "C. $\\begin{cases}xy>0\\\\x+y\\le2\\end{cases}$", "D. $\\begin{cases}x+y=1\\\\2x-y=3\\end{cases}$"
    ], columns=1)
    _mc(b, story, 7, "Với mọi góc $\\alpha$ trong phạm vi đang học, $\\cos(180^\\circ-\\alpha)$ bằng", [
        "A. $\\cos\\alpha$", "B. $\\sin\\alpha$", "C. $-\\sin\\alpha$", "D. $-\\cos\\alpha$"
    ])
    _mc(b, story, 8, "Cho $\\cos\\alpha=-3/5$ và $90^\\circ<\\alpha<180^\\circ$. Giá trị của $\\sin\\alpha$ là", [
        "A. $-4/5$", "B. $3/5$", "C. $4/5$", "D. $16/25$"
    ])
    _mc(b, story, 9, "Trong tam giác $ABC$ với $a=BC,b=CA,c=AB$, định lí côsin phát biểu đúng là", [
        "A. $a^2=b^2+c^2-2bc\\cos A$", "B. $a^2=b^2+c^2+2bc\\cos A$",
        "C. $a^2=b^2+c^2-2bc\\sin A$", "D. $a^2=b^2+c^2-bc\\cos A$"
    ], columns=1)
    _mc(b, story, 10, "Tam giác $ABC$ có $AB=4$, $AC=6$ và $\\widehat A=60^\\circ$. Diện tích tam giác bằng", [
        "A. $12$", "B. $6$", "C. $12\\sqrt3$", "D. $6\\sqrt3$"
    ])
    _mc(b, story, 11, "Khẳng định đúng về vectơ-không là", [
        "A. Vectơ-không có độ dài bằng 1.", "B. Vectơ-không cùng phương và cùng hướng với mọi vectơ.",
        "C. Vectơ-không không cùng phương với vectơ nào.", "D. Với mọi $A,B$, $\\overrightarrow{AB}=\\overrightarrow{BA}$."
    ], columns=1)
    _mc(b, story, 12, "Cho hình bình hành $ABCD$. Khẳng định nào sau đây đúng?", [
        "A. $\\overrightarrow{AB}=\\overrightarrow{CD}$", "B. $\\overrightarrow{AD}=\\overrightarrow{CB}$",
        "C. $\\overrightarrow{AB}=\\overrightarrow{DC}$", "D. $\\overrightarrow{AC}=\\overrightarrow{BD}$"
    ], columns=2, diagram=parallelogram_diagram())

    story.append(b.h2("PHẦN II • TRẮC NGHIỆM ĐÚNG–SAI (2,0 ĐIỂM)"))
    story.append(b.p(
        "Trong mỗi câu, chọn đúng hoặc sai cho từng ý. Điểm mỗi câu: đúng 1 ý 0,1; đúng 2 ý 0,25; đúng 3 ý 0,5; đúng 4 ý 1,0.",
        "Small"
    ))
    story.append(b.p("<b>Câu 1.</b> Cho $A=\\{1;2;3;4\\}$, $B=\\{2;4;6\\}$ và $E=\\{1;2;3;4;5;6\\}$. Xét tính đúng–sai của các khẳng định sau.", "Question"))
    story.append(b.table([
        ["Ý", "Khẳng định", "Đúng", "Sai"],
        ["a", "$2\\in A$.", "☐", "☐"],
        ["b", "Hình dưới đây biểu diễn đúng tập hợp $[-2;3)$ trên trục số.", "☐", "☐"],
        ["c", "$A\\cap B=\\{1;2;3;4;6\\}$.", "☐", "☐"],
        ["d", "$C_E(A\\cup B)=\\{5\\}$.", "☐", "☐"],
    ], [12 * mm, CONTENT_W - 42 * mm, 15 * mm, 15 * mm]))
    story.append(_center(number_line(-2, 3, True, False, "Hình dùng cho Câu 1b")))

    story.append(b.p("<b>Câu 2.</b> Cho bất phương trình $2x-y-4\\le0$ và đường thẳng $d:\\ 2x-y-4=0$. Xét tính đúng–sai của các khẳng định sau.", "Question"))
    story.append(b.table([
        ["Ý", "Khẳng định", "Đúng", "Sai"],
        ["a", "$(1;0)$ là một nghiệm của bất phương trình đã cho.", "☐", "☐"],
        ["b", "Miền nghiệm là nửa mặt phẳng bờ $d$ <b>không</b> chứa $O(0;0)$, kể cả $d$.", "☐", "☐"],
        ["c", "Điểm $M(0;5)$ thuộc miền nghiệm của bất phương trình.", "☐", "☐"],
        ["d", "Mỗi sản phẩm X cần 2 kg nguyên liệu, mỗi sản phẩm Y cần 1 kg. Nếu tổng khối lượng <b>không vượt quá</b> 4 kg thì ràng buộc là $2x+y<4$ với $x,y$ lần lượt là số sản phẩm X, Y.", "☐", "☐"],
    ], [12 * mm, CONTENT_W - 42 * mm, 15 * mm, 15 * mm]))

    story.append(b.h2("PHẦN III • TRẢ LỜI NGẮN (2,0 ĐIỂM)"))
    story.append(b.p("Mỗi câu 0,5 điểm. Chỉ ghi kết quả cuối cùng theo yêu cầu.", "Small"))
    story.append(b.p("<b>Câu 1.</b> Một tập hợp có 5 phần tử. Hỏi tập hợp đó có bao nhiêu tập con? <b>Đáp số:</b> ………………………", "Question"))
    story.append(b.p("<b>Câu 2.</b> Một lớp có 40 học sinh. Có 24 bạn chơi bóng đá, 17 bạn chơi cầu lông và 9 bạn chơi cả hai môn. Hỏi có bao nhiêu bạn không chơi môn nào trong hai môn trên? <b>Đáp số:</b> ………………………", "Question"))
    story.append(b.p("<b>Câu 3.</b> Cho $\\sin\\alpha=3/5$ và $90^\\circ<\\alpha<180^\\circ$. Tính $P=5\\cos\\alpha+2\\tan\\alpha$, viết kết quả dưới dạng số thập phân. <b>Đáp số:</b> ………………………", "Question"))
    story.append(b.p("<b>Câu 4.</b> Tam giác $ABC$ có $AB=5$, $AC=8$ và $\\widehat A=60^\\circ$. Tính độ dài cạnh $BC$. <b>Đáp số:</b> ………………………", "Question"))

    story.append(b.h2("PHẦN IV • TỰ LUẬN (3,0 ĐIỂM)"))
    story.append(b.p("<b>Câu 1 (1,0 điểm).</b> Cho $E=\\{1;2;3;4;5;6;7;8;9;10\\}$, $A$ là tập các số chẵn thuộc $E$ và $B$ là tập các số chia hết cho 3 thuộc $E$.", "Question"))
    story.append(b.p("a) Liệt kê các phần tử của $A,B$. &nbsp;&nbsp; b) Tính $A\\cap B$, $A\\cup B$ và $C_E A$."))
    story.append(b.p("<b>Câu 2 (1,0 điểm).</b> Hai vị trí $B,C$ bị hồ nước ngăn cách. Người ta chọn điểm $A$, đo được $AB=50$ m, $AC=80$ m và $\\widehat{BAC}=60^\\circ$. Tính khoảng cách $BC$.", "Question"))
    story.append(_center(triangle_diagram(practical=True)))
    story.append(b.p("<b>Câu 3 (1,0 điểm).</b> Một xưởng sản xuất hai loại sản phẩm X và Y. Gọi $x,y$ lần lượt là số sản phẩm X, Y ($x,y$ nguyên không âm). Tổng số sản phẩm không vượt quá 40; lượng nguyên liệu cho mỗi sản phẩm X, Y lần lượt là 2 kg và 1 kg, với tối đa 60 kg nguyên liệu. Lợi nhuận mỗi sản phẩm X, Y lần lượt là 400 nghìn đồng và 300 nghìn đồng.", "Question"))
    story.append(b.p("a) Viết hệ bất phương trình biểu thị các ràng buộc và biểu thức lợi nhuận $F$ (nghìn đồng).<br/>b) Xác định các đỉnh của miền phương án và tìm phương án để lợi nhuận lớn nhất. Tính lợi nhuận đó."))
    story.append(b.box("Dừng lại trước khi chấm", [
        "Đã điền đủ 12 lựa chọn và 8 ý đúng–sai? Đã ghi 4 đáp số? Tự luận đã có công thức, thay số, kết luận và đơn vị? "
        "Chỉ mở Phần VIII sau khi hoàn tất soát bài."
    ], "tip"))
