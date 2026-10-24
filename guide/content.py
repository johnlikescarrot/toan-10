#!/usr/bin/env python3
"""Vietnamese content for the Grade 10 midterm-I review guide."""
from __future__ import annotations

from reportlab.lib.units import mm
from reportlab.platypus import Flowable, KeepTogether, PageBreak, Spacer

from guide.pdfguide import (
    CONTENT_W,
    CoverAnchor,
    GuideBuilder,
    PALE_TEAL,
    feasible_region,
    inequality_region,
    number_line,
    parallelogram_diagram,
    triangle_diagram,
    unit_semicircle,
    venn_intersection,
)


def build_story(b: GuideBuilder) -> list[Flowable]:
    story: list[Flowable] = [CoverAnchor(), PageBreak()]
    story += [b.p("Mục lục", "FrontTitle"), b.p(
        "Các mục trong mục lục và thanh bookmark của PDF giúp chuyển nhanh đến từng chuyên đề. "
        "Nếu đọc trên giấy, hãy dùng số trang ở góc dưới.", "Small"
    ), b.toc(), PageBreak()]

    # ------------------------------------------------------------------
    story.append(b.h1("PHẦN I • BẢN ĐỒ BÀI KIỂM TRA & CÁCH DÙNG ĐỀ CƯƠNG"))
    story.append(b.box("Minh bạch về nguồn đề – điều cần biết trước khi học", [
        "Tệp <b>MA TRẬN TOÁN 10 - GIỮA KÌ I.docx</b> do người dùng cung cấp gồm mục tiêu, ma trận và bảng đặc tả; "
        "<b>không có đề thi hoàn chỉnh và không có đáp án chính thức</b>. Vì vậy, đề cương này không gắn nhãn bất kì câu mới nào là “đề gốc”.",
        "Toàn bộ mô tả câu hỏi trong bảng đặc tả được đối chiếu ở Phần IX. Đề 90 phút ở Phần VII là <b>đề luyện tập mới, "
        "được xây dựng đúng số câu, đúng mạch kiến thức và mức độ của ma trận</b>; mọi câu đều có đáp án hoặc lời giải ở Phần VIII.",
    ], "warning"))

    story.append(b.h2("1. Phạm vi theo Kết nối tri thức với cuộc sống"))
    story.append(b.p(
        "Bố cục ôn tập theo <i>Toán 10 – Tập một</i>, bộ <b>Kết nối tri thức với cuộc sống</b>: Bài 1–2 "
        "(Mệnh đề; Tập hợp và các phép toán), Bài 3–4 (Bất phương trình; Hệ bất phương trình bậc nhất hai ẩn), "
        "Bài 5–6 (Giá trị lượng giác; Hệ thức lượng trong tam giác) và <b>chỉ Bài 7</b> (Các khái niệm mở đầu về vectơ). "
        "Các phép cộng vectơ, tích vectơ với một số, tọa độ vectơ và tích vô hướng không được đưa vào trọng tâm vì ma trận chưa yêu cầu."
    ))
    story.append(b.table([
        ["Chuyên đề", "Bài SGK tương ứng", "Trọng tâm phải nắm"],
        ["Mệnh đề và tập hợp", "Bài 1–2", "Mệnh đề, phủ định, kéo theo/đảo/tương đương; ∀, ∃; tập con, khoảng/đoạn; giao, hợp, hiệu, phần bù."],
        ["Bất phương trình bậc nhất hai ẩn", "Bài 3–4", "Nghiệm; biểu diễn miền nghiệm; giao các nửa mặt phẳng; mô hình hóa và bài toán tối ưu."],
        ["Hệ thức lượng trong tam giác", "Bài 5–6", "Giá trị lượng giác của góc 0°–180°; góc bù/phụ; định lí sin, côsin; diện tích; giải tam giác và thực tiễn."],
        ["Vectơ", "Bài 7", "Điểm đầu/cuối, độ dài, giá; cùng phương/hướng; bằng nhau, đối nhau; vectơ-không."],
    ], [39 * mm, 28 * mm, CONTENT_W - 67 * mm]))

    story.append(b.h2("2. Cấu trúc bài kiểm tra 90 phút – 10 điểm"))
    story.append(b.table([
        ["Phần", "Số lượng", "Điểm", "Cách làm hiệu quả"],
        ["I. Trắc nghiệm nhiều phương án", "12 câu", "3,0 (0,25/câu)", "Đọc đúng điều kiện; loại trừ phương án; không để trống."],
        ["II. Trắc nghiệm đúng–sai", "2 câu, mỗi câu 4 ý", "2,0", "Làm độc lập từng ý. Đúng 1/2/3/4 ý được 0,1/0,25/0,5/1,0 điểm cho mỗi câu."],
        ["III. Trả lời ngắn", "4 câu", "2,0 (0,5/câu)", "Tính trên nháp; ghi đúng dạng số, dấu và đơn vị theo yêu cầu."],
        ["IV. Tự luận", "3 câu", "3,0 (1,0/câu)", "Viết công thức/lập luận trước khi thay số; trình bày đủ bước để được điểm thành phần."],
    ], [42 * mm, 31 * mm, 30 * mm, CONTENT_W - 103 * mm]))
    story.append(b.box("Cách đếm số câu trong ma trận", [
        "Có <b>21 câu được đánh số</b> (12 + 2 + 4 + 3). Nếu tách 8 ý đúng–sai thành các lệnh hỏi riêng, "
        "phần trắc nghiệm có 12 + 8 + 4 = <b>24 lệnh hỏi</b>, cộng 3 câu tự luận. Hai cách đếm này không mâu thuẫn."
    ], "note"))

    story.append(b.h2("3. Ma trận rút gọn và định hướng phân bổ thời gian"))
    story.append(b.table([
        ["Mạch kiến thức", "Nhiều phương án", "Đúng–sai", "Trả lời ngắn", "Tự luận", "Tổng điểm"],
        ["Mệnh đề – tập hợp", "4 câu", "1 câu (4 ý)", "2 câu", "1 câu", "4,0"],
        ["Bất phương trình – hệ bất phương trình", "2 câu", "1 câu (4 ý)", "—", "1 câu", "2,5"],
        ["Lượng giác – hệ thức lượng", "4 câu", "—", "2 câu", "1 câu", "3,0"],
        ["Khái niệm vectơ", "2 câu", "—", "—", "—", "0,5"],
    ], [48 * mm, 25 * mm, 26 * mm, 25 * mm, 20 * mm, CONTENT_W - 144 * mm]))
    story.append(b.p(
        "<b>Nhận xét:</b> Mệnh đề–tập hợp chiếm tỉ trọng cao nhất (4 điểm), tiếp theo là lượng giác–hệ thức lượng "
        "(3 điểm). Riêng câu tự luận tối ưu bằng hệ bất phương trình ở mức vận dụng cao cần luyện cả vẽ miền nghiệm "
        "lẫn lập bảng giá trị tại đỉnh."
    ))
    story.append(b.table([
        ["Mốc", "Việc nên làm", "Thời gian gợi ý"],
        ["Bắt đầu", "Đọc lướt, đánh dấu câu chắc chắn; kiểm tra đủ trang và dữ kiện.", "2 phút"],
        ["Phần I", "12 câu nhiều phương án.", "20 phút"],
        ["Phần II", "8 ý đúng–sai; ghi căn cứ ngắn cho ý chưa chắc.", "18 phút"],
        ["Phần III", "4 câu trả lời ngắn; kiểm tra dấu và làm tròn.", "15 phút"],
        ["Phần IV", "3 câu tự luận, ưu tiên câu có thể viết ngay công thức.", "30 phút"],
        ["Kết thúc", "Soát đáp án, biểu đồ, dấu bờ, số 0, đơn vị và phần bù.", "5 phút"],
    ], [25 * mm, CONTENT_W - 50 * mm, 25 * mm]))

    story.append(b.h2("4. Lộ trình 7 ngày và vòng lặp tự sửa lỗi"))
    story.append(b.table([
        ["Ngày", "Nhiệm vụ chính", "Sản phẩm cần có"],
        ["1", "Mệnh đề, phủ định và ∀, ∃.", "1 trang ví dụ–phản ví dụ; làm lại 5 câu đầu Chương I."],
        ["2", "Tập hợp, khoảng/đoạn và các phép toán.", "Sơ đồ Venn/trục số cho mọi phép toán; bài thực tế."],
        ["3", "Miền nghiệm của bất phương trình và hệ.", "Tự vẽ ít nhất 3 hình, ghi rõ bờ và điểm thử."],
        ["4", "Giá trị lượng giác; góc bù/phụ; hằng đẳng thức.", "Bảng giá trị đặc biệt không nhìn tài liệu."],
        ["5", "Định lí sin/côsin, diện tích, giải tam giác.", "Sơ đồ chọn công thức; 2 bài thực tiễn."],
        ["6", "Khái niệm vectơ và ôn lỗi còn sót.", "Hoàn thành checklist; xem lại sổ lỗi."],
        ["7", "Làm Phần VII đúng 90 phút; chấm theo Phần VIII.", "Phiếu thống kê lỗi và thời gian; làm lại câu sai."],
    ], [15 * mm, 77 * mm, CONTENT_W - 92 * mm]))
    story.append(b.box("Vòng lặp 4 bước sau mỗi lần luyện", [
        b.numbered("<b>Đánh dấu:</b> sai kiến thức (K), sai biến đổi (B), đọc nhầm (Đ), hết thời gian (T).", "1.", "BoxBullet"),
        b.numbered("<b>Viết lỗi trong một câu:</b> ví dụ “Quên ∀ đổi thành ∃ khi phủ định”.", "2.", "BoxBullet"),
        b.numbered("<b>Giải lại không nhìn đáp án</b>, rồi nêu quy tắc giúp tránh lỗi.", "3.", "BoxBullet"),
        b.numbered("<b>Làm lại sau 24 giờ và 3 ngày.</b> Chỉ bỏ khỏi sổ lỗi khi đúng hai lần liên tiếp.", "4.", "BoxBullet"),
    ], "tip"))

    story.append(b.h2("5. Checklist trước khi chuyển sang đề luyện tập"))
    for item in [
        "Phủ định được mệnh đề chứa ∀, ∃ và nêu được phản ví dụ khi một mệnh đề sai.",
        "Phân biệt phần tử thuộc tập hợp với tập hợp là tập con; dùng đúng ngoặc ở vô cực.",
        "Tính được giao, hợp, hiệu, phần bù và số tập con; giải bài đếm bằng sơ đồ Venn.",
        "Vẽ đường bờ, chọn điểm thử, tô đúng miền nghiệm; biết khi nào bờ được tính.",
        "Tìm giao điểm các đường bờ và lập bảng giá trị của biểu thức tại các đỉnh miền nghiệm.",
        "Thuộc giá trị lượng giác đặc biệt, dấu trên nửa đường tròn và quan hệ hai góc bù nhau.",
        "Chọn đúng định lí sin/côsin hoặc công thức diện tích theo dữ kiện; kiểm tra đơn vị.",
        "Giải thích cùng phương khác cùng hướng và hai vectơ bằng nhau cần đủ hai điều kiện.",
    ]:
        story.append(b.bullet("☐ " + item))

    # ------------------------------------------------------------------
    story += [PageBreak(), b.h1("PHẦN II • CHƯƠNG I: MỆNH ĐỀ VÀ TẬP HỢP")]
    story.append(b.p(
        "<b>Mục tiêu:</b> nhận diện và lập mệnh đề phủ định; dùng ∀, ∃; diễn đạt điều kiện cần/đủ; "
        "chuyển giữa hai cách cho tập hợp; thao tác thành thạo trên tập hợp và khoảng số; giải bài đếm thực tế."
    ))

    story.append(b.h2("BÀI 1 • MỆNH ĐỀ"))
    story.append(b.h3("1.1. Mệnh đề, mệnh đề chứa biến và phản ví dụ"))
    story.append(b.p(
        "<b>Mệnh đề</b> là một khẳng định có tính đúng hoặc sai, không vừa đúng vừa sai. Câu hỏi, câu mệnh lệnh, "
        "câu cảm thán không phải mệnh đề. Khẳng định chứa biến như $P(n):\,n^2>9$ chưa có tính đúng–sai "
        "cho đến khi thay $n$ bằng một giá trị cụ thể trong tập xác định; đó là <b>mệnh đề chứa biến</b>."
    ))
    story.append(b.table([
        ["Câu", "Có phải mệnh đề?", "Giải thích"],
        ["“9 là số chính phương.”", "Có, đúng", "$9=3^2$."],
        ["“$x+2>5$.”", "Chưa phải", "Đúng hay sai còn phụ thuộc $x$; đây là mệnh đề chứa biến."],
        ["“Bạn đã ôn bài chưa?”", "Không", "Câu hỏi."],
        ["“Mọi số nguyên tố đều lẻ.”", "Có, sai", "$2$ là phản ví dụ."],
    ], [55 * mm, 34 * mm, CONTENT_W - 89 * mm]))
    story.append(b.box("Muốn chứng minh một mệnh đề “mọi …” là sai?", [
        "Chỉ cần <b>một phản ví dụ</b> thuộc tập đang xét nhưng không thỏa mãn kết luận. "
        "Ngược lại, một ví dụ đúng không đủ để khẳng định mệnh đề đúng với mọi trường hợp."
    ], "remember"))

    story.append(b.h3("1.2. Phủ định và hai kí hiệu ∀, ∃"))
    story.append(b.p(
        "Phủ định của mệnh đề $P$, kí hiệu $\\overline P$, đúng khi $P$ sai và sai khi $P$ đúng. "
        "Khi phủ định mệnh đề lượng từ: <b>đổi ∀ thành ∃, đổi ∃ thành ∀, giữ nguyên miền xét và phủ định vị từ</b>."
    ))
    story.extend(b.formula(r"\overline{\forall x\in X,\,P(x)}\ \equiv\ \exists x\in X,\,\overline{P(x)}"))
    story.extend(b.formula(r"\overline{\exists x\in X,\,P(x)}\ \equiv\ \forall x\in X,\,\overline{P(x)}"))
    story.append(b.table([
        ["Mệnh đề ban đầu", "Mệnh đề phủ định đúng"],
        ["$\\forall x\\in\\mathbb R,\\,x^2\\ge0$", "$\\exists x\\in\\mathbb R,\\,x^2<0$"],
        ["$\\exists n\\in\\mathbb Z,\\,n+1=0$", "$\\forall n\\in\\mathbb Z,\\,n+1\\ne0$"],
        ["“Mọi học sinh trong nhóm đều đã nộp bài.”", "“Có ít nhất một học sinh trong nhóm chưa nộp bài.”"],
    ], [CONTENT_W / 2, CONTENT_W / 2]))
    story.append(b.box("Bẫy thường gặp", [
        "Phủ định của “$>$” là “$\\le$”, của “$\\ge$” là “$<$”, của “$=$” là “$\\ne$”. "
        "<b>Không đổi miền</b> $\\mathbb R$ thành miền khác và không chỉ đổi dấu mà quên đổi ∀/∃."
    ], "warning"))

    story.append(b.h3("1.3. Kéo theo, đảo, tương đương; điều kiện cần và đủ"))
    story.append(b.p(
        "Với hai mệnh đề $P,Q$: mệnh đề kéo theo $P\\Rightarrow Q$ chỉ sai khi $P$ đúng mà $Q$ sai. "
        "Mệnh đề đảo của $P\\Rightarrow Q$ là $Q\\Rightarrow P$; mệnh đề đảo <b>không nhất thiết</b> cùng tính đúng–sai với mệnh đề ban đầu."
    ))
    story.append(b.bullet("$P$ là <b>điều kiện đủ</b> để có $Q$: chỉ cần $P$ đúng thì $Q$ đúng."))
    story.append(b.bullet("$Q$ là <b>điều kiện cần</b> để có $P$: muốn $P$ đúng bắt buộc $Q$ phải đúng."))
    story.append(b.bullet("Nếu cả $P\\Rightarrow Q$ và $Q\\Rightarrow P$ đúng thì $P\\Leftrightarrow Q$: $P$ là điều kiện cần và đủ để có $Q$."))
    story.append(b.box("Mẹo diễn đạt không bị đảo chiều", [
        "Trong câu “$P$ là điều kiện cần để có $Q$”, hãy viết $Q\\Rightarrow P$. "
        "Trong câu “$P$ là điều kiện đủ để có $Q$”, viết $P\\Rightarrow Q$. Luôn kiểm tra bằng cách thay một ví dụ cụ thể."
    ], "tip"))

    story.append(b.h3("Ví dụ 1 • Nhận diện, phủ định và dùng phản ví dụ"))
    story.append(b.p("Xét $P:\\ \\forall n\\in\\mathbb N,\\ n^2+n+1$ là số lẻ. Phát biểu $\\overline P$ và xét tính đúng–sai của $P$."))
    story.append(b.p("<b>Bước 1 – Phủ định:</b> đổi ∀ thành ∃, giữ $n\\in\\mathbb N$, phủ định “là số lẻ” thành “không là số lẻ” (tức là số chẵn)."))
    story.extend(b.formula(r"\overline P:\ \exists n\in\mathbb N,\ n^2+n+1\ \text{là số chẵn}."))
    story.append(b.p("<b>Bước 2 – Tìm phản ví dụ:</b> thay $n=1$, ta được $1^2+1+1=3$ (lẻ), chưa kết luận được. Thay $n=2$, được $2^2+2+1=7$ (lẻ). Thay $n=3$, được $9+3+1=13$ (lẻ). Cần lập luận tổng quát, không dừng ở vài ví dụ."))
    story.append(b.p("Vì $n^2+n=n(n+1)$ là tích của hai số nguyên liên tiếp nên luôn chẵn. Do đó $n^2+n+1$ luôn lẻ. Vậy $P$ đúng và $\\overline P$ sai.", "Answer"))
    story.append(b.box("Rút kinh nghiệm", [
        "Phản ví dụ giúp bác bỏ rất nhanh, nhưng nếu chưa tìm thấy thì phải chứng minh. Với biểu thức có $n^2+n$, "
        "nhóm thành $n(n+1)$ là cách kiểm tra tính chẵn/lẻ đáng nhớ."
    ], "note"))

    story.append(b.h3("Ví dụ 2 • Điều kiện cần, đủ và mệnh đề đảo"))
    story.append(b.p("Với số nguyên $n$, đặt $P$: “$n$ chia hết cho 6” và $Q$: “$n$ chia hết cho 3”. Hãy xác định quan hệ và phát biểu bằng điều kiện cần/đủ."))
    story.append(b.p("Ta có $n=6k\\Rightarrow n=3(2k)$ nên $P\\Rightarrow Q$ đúng. Ngược lại, $n=3$ chia hết cho 3 nhưng không chia hết cho 6, nên $Q\\Rightarrow P$ sai."))
    story.append(b.p("Vậy $P$ là điều kiện đủ để có $Q$; $Q$ là điều kiện cần nhưng không đủ để có $P$. Hai mệnh đề không tương đương.", "Answer"))

    story.append(b.h3("Luyện nhanh A • Mệnh đề"))
    for i, text in enumerate([
        "Câu “$x-1=4$” đã là mệnh đề chưa? Vì sao?",
        "Lập phủ định của $P:\\ \\exists x\\in\\mathbb R,\\,2x+1=0$.",
        "Dùng một phản ví dụ để bác bỏ “Bình phương của mọi số thực đều lớn hơn số đó”.",
        "Cho $P\\Rightarrow Q$ đúng. Có thể kết luận $Q\\Rightarrow P$ đúng không?",
        "Phát biểu “$n$ chia hết cho 10 là điều kiện gì để $n$ chia hết cho 5”?",
    ], 1):
        story.append(b.numbered(text, f"{i}."))
    story.append(b.table([
        ["Câu", "Đáp án / căn cứ"],
        ["1", "Chưa; đúng–sai còn phụ thuộc $x$. Đây là mệnh đề chứa biến."],
        ["2", "$\\overline P:\\ \\forall x\\in\\mathbb R,\\,2x+1\\ne0$."],
        ["3", "Chọn $x=1$: $1^2=1$, không lớn hơn 1 (hoặc $x=0$)."],
        ["4", "Không; mệnh đề đảo có thể sai, cần kiểm tra riêng."],
        ["5", "Điều kiện đủ: $n\\ \\vdots\\ 10\\Rightarrow n\\ \\vdots\\ 5$; không phải điều kiện cần (ví dụ $n=5$)."],
    ], [14 * mm, CONTENT_W - 14 * mm]))

    story.append(b.h2("BÀI 2 • TẬP HỢP VÀ CÁC PHÉP TOÁN TRÊN TẬP HỢP"))
    story.append(b.h3("2.1. Hai cách cho tập hợp; phần tử, tập con, tập bằng nhau"))
    story.append(b.bullet("<b>Liệt kê:</b> $A=\\{1;2;3\\}$. Mỗi phần tử chỉ viết một lần, thứ tự không quan trọng."))
    story.append(b.bullet("<b>Nêu tính chất đặc trưng:</b> $A=\\{x\\in\\mathbb N\\mid 0<x<4\\}$."))
    story.append(b.bullet("$a\\in A$: $a$ là một <b>phần tử</b> của $A$. $B\\subset A$: mọi phần tử của $B$ đều thuộc $A$; $B$ là <b>tập con</b> của $A$."))
    story.append(b.bullet("$A=B$ khi $A\\subset B$ và $B\\subset A$. Tập rỗng $\\varnothing$ không có phần tử nào và là tập con của mọi tập hợp."))
    story.append(b.box("Phân biệt ∈ và ⊂ bằng một câu", [
        "$2\\in\\{1;2;3\\}$ vì 2 là phần tử. $\\{2\\}\\subset\\{1;2;3\\}$ vì $\\{2\\}$ là tập hợp chứa một phần tử. "
        "Không viết $2\\subset A$ hay $\\{2\\}\\in A$ trừ khi cấu trúc tập hợp đặc biệt cho phép."
    ], "remember"))
    story.append(b.table([
        ["Kí hiệu", "Tập hợp số", "Lưu ý"],
        ["$\\mathbb N^*$", "Số tự nhiên khác 0", "$1;2;3;\\ldots$"],
        ["$\\mathbb N$", "Số tự nhiên", "$0;1;2;3;\\ldots$"],
        ["$\\mathbb Z$", "Số nguyên", "Gồm số âm, 0 và số dương."],
        ["$\\mathbb Q$", "Số hữu tỉ", "Viết được dưới dạng $a/b$, $a,b\\in\\mathbb Z$, $b\\ne0$."],
        ["$\\mathbb R$", "Số thực", "Gồm hữu tỉ và vô tỉ."],
    ], [24 * mm, 47 * mm, CONTENT_W - 71 * mm]))

    story.append(b.h3("Ví dụ 3 • Chuyển từ tính chất đặc trưng sang liệt kê"))
    story.append(b.p("Viết tập $A=\\{x\\in\\mathbb Z\\mid -2<x\\le3\\}$ và $B=\\{x\\in\\mathbb R\\mid x^2=4\\}$ bằng cách liệt kê."))
    story.append(b.p("Với $A$, chỉ lấy <b>số nguyên</b> lớn hơn $-2$ và nhỏ hơn hoặc bằng $3$: $A=\\{-1;0;1;2;3\\}$. Với $B$, phương trình $x^2=4$ có hai nghiệm thực $x=\\pm2$ nên $B=\\{-2;2\\}$.", "Answer"))
    story.append(b.box("Sai lầm cần tránh", [
        "Miền $\\mathbb Z$ hay $\\mathbb R$ quyết định danh sách nghiệm. Dấu $<$ loại đầu mút, dấu $\\le$ giữ đầu mút. "
        "Đừng quên nghiệm âm của $x^2=a$ với $a>0$."
    ], "warning"))

    story.append(b.h3("2.2. Khoảng, đoạn, nửa khoảng và trục số"))
    story.append(b.table([
        ["Kí hiệu", "Điều kiện tương ứng", "Đầu mút trên trục số"],
        ["$(a;b)$", "$a<x<b$", "Cả hai đầu rỗng."],
        ["$[a;b]$", "$a\\le x\\le b$", "Cả hai đầu đặc."],
        ["$(a;b]$", "$a<x\\le b$", "$a$ rỗng, $b$ đặc."],
        ["$[a;b)$", "$a\\le x<b$", "$a$ đặc, $b$ rỗng."],
        ["$(-\\infty;a)$", "$x<a$", "$a$ rỗng; vô cực luôn dùng ngoặc tròn."],
        ["$[a;+\\infty)$", "$x\\ge a$", "$a$ đặc; vô cực luôn dùng ngoặc tròn."],
        ["$(-\\infty;+\\infty)$", "$x\\in\\mathbb R$", "Toàn bộ trục số."],
    ], [37 * mm, 50 * mm, CONTENT_W - 87 * mm]))
    story.append(number_line(-2, 3, True, False, "Tập hợp [−2; 3)"))
    story.append(b.p("Điểm đặc tại $-2$ nghĩa là $-2$ được lấy; điểm rỗng tại $3$ nghĩa là $3$ không được lấy.", "Caption"))

    story.append(b.h3("2.3. Giao, hợp, hiệu và phần bù"))
    story.append(b.table([
        ["Phép toán", "Định nghĩa", "Cách đọc hình/trục số"],
        ["Giao $A\\cap B$", "$\\{x\\mid x\\in A\\ \\text{và}\\ x\\in B\\}$", "Chỉ phần chung."],
        ["Hợp $A\\cup B$", "$\\{x\\mid x\\in A\\ \\text{hoặc}\\ x\\in B\\}$", "Gom tất cả, phần chung chỉ tính một lần."],
        ["Hiệu $A\\setminus B$", "$\\{x\\mid x\\in A\\ \\text{và}\\ x\\notin B\\}$", "Lấy $A$ rồi bỏ phần thuộc $B$."],
        ["Phần bù $C_E A$", "$E\\setminus A$ khi $A\\subset E$", "Những phần tử của $E$ không thuộc $A$."],
    ], [34 * mm, 75 * mm, CONTENT_W - 109 * mm]))
    story.append(venn_intersection())
    story.append(b.p("Phần tô màu là $A\\cap B$: phần tử phải thuộc đồng thời cả hai tập hợp.", "Caption"))
    story.append(b.box("Quy trình trên trục số", [
        "Vẽ hai tập trên cùng một trục (có thể dùng hai dòng), đánh dấu rõ đầu mút. "
        "<b>Giao:</b> giữ vùng phủ hai lần. <b>Hợp:</b> giữ vùng phủ ít nhất một lần. "
        "Sau cùng mới quyết định đầu mút bằng dấu bất đẳng thức."
    ], "tip"))

    story.append(b.h3("Ví dụ 4 • Bốn phép toán trên khoảng số"))
    story.append(b.p("Cho $A=(-\\infty;2]$, $B=(0;5)$ và $E=\\mathbb R$. Tính $A\\cap B$, $A\\cup B$, $A\\setminus B$, $B\\setminus A$ và $C_E A$."))
    story.append(b.bullet("Giao: phần chung là $0<x\\le2$, nên $A\\cap B=(0;2]$."))
    story.append(b.bullet("Hợp: $A$ phủ đến 2, $B$ nối tiếp đến sát 5, nên $A\\cup B=(-\\infty;5)$."))
    story.append(b.bullet("$A\\setminus B$: từ $A$ bỏ $(0;5)$, còn $(-\\infty;0]$."))
    story.append(b.bullet("$B\\setminus A$: từ $B$ bỏ phần $\\le2$, còn $(2;5)$."))
    story.append(b.bullet("$C_E A=\\mathbb R\\setminus(-\\infty;2]=(2;+\\infty)$.", "BoxBody"))
    story.append(b.p("Kiểm tra đầu mút: $2\\in A$ nhưng $2\\notin B$; $0\\notin B$ nên vẫn thuộc $A\\setminus B$.", "Answer"))

    story.append(b.h3("2.4. Số tập con và bài toán đếm bằng sơ đồ Venn"))
    story.append(b.p(
        "Nếu tập $A$ có $n$ phần tử thì mỗi phần tử có hai lựa chọn: được đưa vào một tập con hoặc không. "
        "Vì vậy $A$ có $2^n$ tập con, tính cả $\\varnothing$ và chính $A$."
    ))
    story.extend(b.formula(r"\text{Số tập con của }A=2^{|A|},\qquad \text{số tập con khác }A=2^{|A|}-1."))
    story.append(b.p(
        "Với hai tập hữu hạn, công thức bao hàm–loại trừ giúp không đếm lặp phần chung:"
    ))
    story.extend(b.formula(r"|A\cup B|=|A|+|B|-|A\cap B|."))
    story.append(b.h3("Ví dụ 5 • Đếm học sinh không tham gia môn nào"))
    story.append(b.p("Một nhóm có 35 bạn. Có 20 bạn chọn bóng đá, 15 bạn chọn cầu lông, trong đó 6 bạn chọn cả hai. Hỏi có bao nhiêu bạn không chọn môn nào?"))
    story.append(b.p("Gọi $A,B$ lần lượt là tập bạn chọn bóng đá và cầu lông. Số bạn chọn ít nhất một môn là $|A\\cup B|=20+15-6=29$. Do đó số bạn không chọn môn nào là $35-29=6$.", "Answer"))
    story.append(b.box("Đừng lấy 20 + 15 = 35 rồi kết luận không có bạn nào ngoài hai môn", [
        "Sáu bạn chọn cả hai đã bị tính hai lần. Luôn trừ $|A\\cap B|$ một lần trước khi xét phần bù."
    ], "warning"))

    story.append(b.h3("Luyện nhanh B • Tập hợp"))
    for i, text in enumerate([
        "Tập $A=\\{1;2;3\\}$ có bao nhiêu tập con? Kể tên hai tập con khác $A$.",
        "Tính $[-1;4)\\cap[2;6]$.",
        "Tính $(-\\infty;3)\\cup[0;5]$.",
        "Cho $E=\\{1;2;3;4;5;6\\}$ và $A$ là tập các số chẵn trong $E$. Tìm $C_E A$.",
        "Lớp có 35 bạn; 20 bạn thích $A$, 15 bạn thích $B$, 6 bạn thích cả hai. Có bao nhiêu bạn không thích môn nào?",
        "Khẳng định $\\varnothing\\subset A$ đúng với mọi tập $A$ không?",
    ], 1):
        story.append(b.numbered(text, f"{i}."))
    story.append(b.table([
        ["Câu", "Đáp án / căn cứ"],
        ["1", "$2^3=8$. Ví dụ: $\\varnothing$, $\\{1\\}$, $\\{2;3\\}$."],
        ["2", "$[2;4)$: giữ 2, không giữ 4."],
        ["3", "$(-\\infty;5]$."],
        ["4", "$C_E A=\\{1;3;5\\}$."],
        ["5", "$35-(20+15-6)=6$ bạn."],
        ["6", "Đúng; tập rỗng là tập con của mọi tập hợp."],
    ], [14 * mm, CONTENT_W - 14 * mm]))

    # ------------------------------------------------------------------
    story += [PageBreak(), b.h1("PHẦN III • CHƯƠNG II: BẤT PHƯƠNG TRÌNH VÀ HỆ BẤT PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN")]
    story.append(b.p(
        "<b>Mục tiêu:</b> nhận dạng đúng bậc và số ẩn; kiểm tra nghiệm; biểu diễn miền nghiệm; "
        "chuyển điều kiện thực tế thành mô hình; tìm giá trị lớn nhất/nhỏ nhất của biểu thức bậc nhất trên miền đa giác."
    ))
    story.append(b.h2("BÀI 3 • BẤT PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN"))
    story.append(b.h3("3.1. Định nghĩa và nghiệm"))
    story.append(b.p(
        "Bất phương trình bậc nhất hai ẩn $x,y$ có một trong các dạng $ax+by+c<0$, $ax+by+c>0$, "
        "$ax+by+c\\le0$, $ax+by+c\\ge0$, trong đó $a,b$ <b>không đồng thời bằng 0</b>. "
        "Cặp $(x_0;y_0)$ là nghiệm nếu thay vào ta được một khẳng định đúng. Tập tất cả các điểm nghiệm trên $Oxy$ là miền nghiệm."
    ))
    story.append(b.table([
        ["Biểu thức", "Có phải BPT bậc nhất hai ẩn?", "Vì sao"],
        ["$2x-y+1\\le0$", "Có", "Bậc nhất, hai ẩn $x,y$."],
        ["$x+3>0$", "Có", "Hệ số của $y$ bằng 0; hệ số của $x$ khác 0."],
        ["$x^2+y<1$", "Không", "Có $x^2$."],
        ["$xy\\ge2$", "Không", "Có tích hai ẩn, không phải bậc nhất."],
    ], [42 * mm, 50 * mm, CONTENT_W - 92 * mm]))

    story.append(b.h3("3.2. Ba bước biểu diễn miền nghiệm"))
    for number, text in [
        ("1.", "<b>Vẽ đường bờ</b> $d:\\ ax+by+c=0$. Tìm hai điểm trên $d$ (thường là giao với hai trục). Bờ nét liền với $\\le,\\ge$; nét đứt với $<,>$."),
        ("2.", "<b>Chọn điểm thử</b> không thuộc $d$, thường là $O(0;0)$ nếu $c\\ne0$. Thay tọa độ vào bất phương trình."),
        ("3.", "<b>Tô miền:</b> nếu điểm thử là nghiệm thì lấy nửa mặt phẳng chứa điểm đó; nếu không thì lấy nửa còn lại. Ghi chú có lấy bờ hay không."),
    ]:
        story.append(b.numbered(text, number))
    story.append(inequality_region())
    story.append(b.p("Ví dụ hình: miền nghiệm của $2x+y-4\\le0$ chứa $O$ và kể cả đường bờ.", "Caption"))
    story.append(b.box("Kiểm tra chéo chỉ trong 10 giây", [
        "Chọn một điểm rõ ràng nằm trong vùng đã tô và một điểm ngoài vùng. Thay lại vào bất phương trình. "
        "Nếu kết quả ngược với hình thì đã tô nhầm nửa mặt phẳng."
    ], "tip"))

    story.append(b.h3("Ví dụ 6 • Từ đường bờ đến miền nghiệm"))
    story.append(b.p("Biểu diễn miền nghiệm của $x-2y+2\\ge0$."))
    story.append(b.p("Đường bờ $d:\\ x-2y+2=0$ đi qua $(-2;0)$ và $(0;1)$. Vì dấu $\\ge$ nên vẽ $d$ nét liền và lấy cả bờ."))
    story.append(b.p("Điểm $O(0;0)$ không thuộc $d$ và $0-2\\cdot0+2=2\\ge0$ (đúng). Vậy miền nghiệm là nửa mặt phẳng bờ $d$ chứa $O$, kể cả $d$.", "Answer"))

    story.append(b.h2("BÀI 4 • HỆ BẤT PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN"))
    story.append(b.h3("4.1. Miền nghiệm của hệ là phần giao"))
    story.append(b.p(
        "Nghiệm của hệ phải thỏa mãn <b>đồng thời</b> mọi bất phương trình. Vì vậy, biểu diễn từng miền nghiệm "
        "trên cùng $Oxy$ rồi lấy phần giao. Nếu miền là đa giác, hãy tìm chính xác các đỉnh bằng cách giải hệ phương trình của hai đường bờ tương ứng."
    ))
    story.append(b.box("Kí hiệu ngoặc nhọn và từ “và”", [
        "Viết $\\begin{cases}x\\ge0\\\\ y\\ge0\\\\ x+y\\le4\\end{cases}$ nghĩa là $x\\ge0$ <b>và</b> $y\\ge0$ <b>và</b> $x+y\\le4$. "
        "Không lấy hợp của ba miền."
    ], "remember"))

    story.append(b.h3("Ví dụ 7 • Miền tam giác và giá trị tại đỉnh"))
    story.append(b.p("Cho hệ $x\\ge0$, $y\\ge0$, $x+y\\le4$. Xác định miền nghiệm và giá trị lớn nhất của $F=2x+3y$ trên miền đó."))
    story.append(b.p("Hai điều kiện $x\\ge0,y\\ge0$ giới hạn ở góc phần tư thứ nhất. Đường $x+y=4$ cắt các trục tại $(4;0),(0;4)$; $O$ thỏa mãn $x+y\\le4$. Miền nghiệm là tam giác có ba đỉnh $(0;0),(4;0),(0;4)$, kể cả biên."))
    story.append(b.table([
        ["Đỉnh (x; y)", "F = 2x + 3y"],
        ["$(0;0)$", "$0$"],
        ["$(4;0)$", "$8$"],
        ["$(0;4)$", "$12$"],
    ], [CONTENT_W / 2, CONTENT_W / 2]))
    story.append(b.p("Vì $F$ là biểu thức bậc nhất trên miền tam giác, giá trị lớn nhất đạt tại một đỉnh. Vậy $F_{\\max}=12$ tại $(0;4)$.", "Answer"))
    story.append(b.box("Vì sao chỉ cần xét đỉnh?", [
        "Trên một miền đa giác lồi, giá trị lớn nhất/nhỏ nhất của biểu thức bậc nhất (nếu có) luôn đạt được tại ít nhất một đỉnh. "
        "Nếu miền không bị chặn, phải kiểm tra thêm: giá trị có thể không tồn tại cực trị hữu hạn."
    ], "note"))

    story.append(b.h3("4.2. Mô hình hóa bài toán thực tiễn"))
    for number, text in [
        ("1.", "<b>Đặt ẩn và đơn vị:</b> ví dụ $x,y$ là số sản phẩm loại A, B; thường $x,y\\ge0$ và có thể nguyên."),
        ("2.", "<b>Dịch từng ràng buộc:</b> “không quá” là $\\le$; “ít nhất” là $\\ge$; “tối đa” là $\\le$."),
        ("3.", "<b>Viết đại lượng mục tiêu:</b> lợi nhuận, chi phí, thời gian… thành $F=ax+by$."),
        ("4.", "<b>Tìm phương án tối ưu</b> rồi kết luận bằng lời, kèm số lượng và đơn vị."),
    ]:
        story.append(b.numbered(text, number))
    story.append(b.box("Đừng bỏ điều kiện tự nhiên", [
        "Số sản phẩm, số học sinh, số chuyến xe không thể âm; nhiều bài còn yêu cầu nguyên. "
        "Sau khi tìm đỉnh, kiểm tra phương án có ý nghĩa thực tế không."
    ], "warning"))

    story.append(b.h3("Luyện nhanh C • Bất phương trình và hệ"))
    for i, text in enumerate([
        "Cặp $(1;2)$ có là nghiệm của $x-y+1\\ge0$ không?",
        "Khi biểu diễn $x+y<2$, đường $x+y=2$ có được tính vào miền nghiệm không?",
        "Nêu hai điểm trên đường bờ của $2x+y-4=0$.",
        "Tìm các đỉnh miền nghiệm của $x\\ge0,y\\ge0,x+y\\le3$.",
        "Với miền ở câu 4, tìm giá trị lớn nhất của $F=x+2y$.",
        "Mỗi quyển vở giá 10 nghìn đồng, mỗi bút giá 5 nghìn đồng. Viết bất phương trình cho việc mua $x$ quyển vở, $y$ bút với không quá 100 nghìn đồng.",
        "Vì sao $xy\\ge0$ không phải bất phương trình bậc nhất hai ẩn?",
        "Nếu điểm thử không thỏa mãn bất phương trình, chọn nửa mặt phẳng nào?",
    ], 1):
        story.append(b.numbered(text, f"{i}."))
    story.append(b.table([
        ["Câu", "Đáp án / căn cứ"],
        ["1", "Có, vì $1-2+1=0\\ge0$."],
        ["2", "Không; dấu $<$ nên bờ nét đứt và bị loại."],
        ["3", "$(2;0)$ và $(0;4)$."],
        ["4", "$(0;0),(3;0),(0;3)$."],
        ["5", "$F_{\\max}=6$ tại $(0;3)$."],
        ["6", "$10x+5y\\le100$ (nghìn đồng), cùng $x,y\\ge0$."],
        ["7", "Có tích $xy$, không thuộc dạng $ax+by+c$."],
        ["8", "Nửa mặt phẳng không chứa điểm thử."],
    ], [14 * mm, CONTENT_W - 14 * mm]))

    # ------------------------------------------------------------------
    story += [PageBreak(), b.h1("PHẦN IV • CHƯƠNG III: HỆ THỨC LƯỢNG TRONG TAM GIÁC")]
    story.append(b.p(
        "<b>Mục tiêu:</b> xác định dấu và giá trị lượng giác của góc từ $0^\\circ$ đến $180^\\circ$; "
        "dùng quan hệ góc bù/phụ và hằng đẳng thức; chọn đúng công thức để giải tam giác và bài toán đo đạc."
    ))
    story.append(b.h2("BÀI 5 • GIÁ TRỊ LƯỢNG GIÁC CỦA MỘT GÓC TỪ 0° ĐẾN 180°"))
    story.append(b.h3("5.1. Định nghĩa bằng nửa đường tròn đơn vị"))
    story.append(b.p(
        "Trên nửa đường tròn đơn vị, lấy điểm $M(x_0;y_0)$ sao cho $\\widehat{xOM}=\\alpha$, $0^\\circ\\le\\alpha\\le180^\\circ$. "
        "Khi đó $\\sin\\alpha=y_0$, $\\cos\\alpha=x_0$, và khi mẫu khác 0:"
    ))
    story.extend(b.formula(r"\tan\alpha=\frac{\sin\alpha}{\cos\alpha}\quad(\cos\alpha\ne0),\qquad \cot\alpha=\frac{\cos\alpha}{\sin\alpha}\quad(\sin\alpha\ne0)."))
    story.append(unit_semicircle())
    story.append(b.p("Tung độ $y_0$ cho sin, hoành độ $x_0$ cho côsin.", "Caption"))
    story.append(b.bullet("Với $0^\\circ<\\alpha<90^\\circ$: sin, côsin, tang, côtang đều dương khi xác định."))
    story.append(b.bullet("Với $90^\\circ<\\alpha<180^\\circ$: $\\sin\\alpha>0$ nhưng $\\cos\\alpha<0$, nên tang và côtang âm."))
    story.append(b.bullet("$\\tan90^\\circ$ không xác định vì $\\cos90^\\circ=0$; $\\cot0^\\circ$ và $\\cot180^\\circ$ không xác định vì sin bằng 0."))

    story.append(b.h3("5.2. Bảng giá trị cần thuộc"))
    story.append(b.table([
        ["Góc", "0°", "30°", "45°", "60°", "90°", "120°", "135°", "150°", "180°"],
        ["sin", "0", "1/2", "√2/2", "√3/2", "1", "√3/2", "√2/2", "1/2", "0"],
        ["cos", "1", "√3/2", "√2/2", "1/2", "0", "−1/2", "−√2/2", "−√3/2", "−1"],
        ["tan", "0", "√3/3", "1", "√3", "—", "−√3", "−1", "−√3/3", "0"],
        ["cot", "—", "√3", "1", "√3/3", "0", "−√3/3", "−1", "−√3", "—"],
    ], [15 * mm] + [(CONTENT_W - 15 * mm) / 9] * 9))
    story.append(b.p("Dấu “—” nghĩa là giá trị không xác định. Có thể suy ra các góc tù bằng quan hệ góc bù thay vì học riêng từng ô.", "Caption"))

    story.append(b.h3("5.3. Hai góc bù nhau, hai góc phụ nhau"))
    story.append(b.table([
        ["Quan hệ", "Công thức", "Ghi nhớ"],
        ["Bù nhau", "$\\sin(180^\\circ-\\alpha)=\\sin\\alpha$", "Sin giữ nguyên."],
        ["Bù nhau", "$\\cos(180^\\circ-\\alpha)=-\\cos\\alpha$", "Côsin đổi dấu."],
        ["Bù nhau", "$\\tan(180^\\circ-\\alpha)=-\\tan\\alpha$; $\\cot(180^\\circ-\\alpha)=-\\cot\\alpha$", "Tang/côtang đổi dấu khi xác định."],
        ["Phụ nhau ($0°\\le\\alpha\\le90°$)", "$\\sin(90^\\circ-\\alpha)=\\cos\\alpha$; $\\cos(90^\\circ-\\alpha)=\\sin\\alpha$", "Sin của góc này bằng côsin góc kia."],
        ["Phụ nhau", "$\\tan(90^\\circ-\\alpha)=\\cot\\alpha$; $\\cot(90^\\circ-\\alpha)=\\tan\\alpha$", "Khi các giá trị xác định."],
    ], [35 * mm, 91 * mm, CONTENT_W - 126 * mm]))

    story.append(b.h3("5.4. Các hằng đẳng thức và cách tìm giá trị còn lại"))
    story.extend(b.formula(r"\sin^2\alpha+\cos^2\alpha=1,\qquad 1+\tan^2\alpha=\frac1{\cos^2\alpha},\qquad 1+\cot^2\alpha=\frac1{\sin^2\alpha}."))
    story.append(b.p(
        "Khai căn phải chọn dấu bằng góc đã cho: nếu $90^\\circ<\\alpha<180^\\circ$ thì $\\sin\\alpha>0$, $\\cos\\alpha<0$. "
        "Sau khi có sin và côsin, tính tang/côtang bằng thương; không dùng máy tính để “đoán” dấu."
    ))
    story.append(b.h3("Ví dụ 8 • Biết côsin của một góc tù"))
    story.append(b.p("Cho $\\cos\\alpha=-3/5$ và $90^\\circ<\\alpha<180^\\circ$. Tính $\\sin\\alpha,\\tan\\alpha,\\cot\\alpha$."))
    story.extend(b.formula(r"\sin^2\alpha=1-\cos^2\alpha=1-\frac9{25}=\frac{16}{25}."))
    story.append(b.p("Vì $\\alpha$ tù nên $\\sin\\alpha>0$, do đó $\\sin\\alpha=4/5$. Suy ra $\\tan\\alpha=(4/5):(-3/5)=-4/3$ và $\\cot\\alpha=-3/4$.", "Answer"))

    story.append(b.h3("Ví dụ 9 • Giá trị biểu thức nhờ góc bù"))
    story.append(b.p("Tính $T=\\sin150^\\circ+\\cos120^\\circ+\\tan135^\\circ$."))
    story.append(b.p("Ta có $\\sin150^\\circ=\\sin30^\\circ=1/2$, $\\cos120^\\circ=-\\cos60^\\circ=-1/2$, $\\tan135^\\circ=-\\tan45^\\circ=-1$. Vậy $T=1/2-1/2-1=-1$.", "Answer"))
    story.append(b.box("Máy tính cầm tay", [
        "Chuyển sang chế độ <b>DEG</b> trước khi tính góc theo độ. Với giá trị gần đúng, chỉ làm tròn ở bước cuối; "
        "với góc đặc biệt, ưu tiên giá trị chính xác có căn."
    ], "tip"))

    story.append(b.h2("BÀI 6 • HỆ THỨC LƯỢNG TRONG TAM GIÁC"))
    story.append(b.p("Quy ước trong $\\triangle ABC$: $a=BC$, $b=CA$, $c=AB$; $R,r$ lần lượt là bán kính đường tròn ngoại tiếp, nội tiếp; $p=(a+b+c)/2$; $S$ là diện tích."))
    story.append(triangle_diagram())
    story.append(b.p("Cạnh $a$ đối diện góc $A$, cạnh $b$ đối diện góc $B$, cạnh $c$ đối diện góc $C$.", "Caption"))

    story.append(b.h3("6.1. Định lí côsin – khi có hai cạnh và góc xen giữa hoặc ba cạnh"))
    story.extend(b.formula(r"a^2=b^2+c^2-2bc\cos A,\qquad \cos A=\frac{b^2+c^2-a^2}{2bc}."))
    story.append(b.p("Viết vòng tròn: $b^2=c^2+a^2-2ca\\cos B$ và $c^2=a^2+b^2-2ab\\cos C$."))
    story.append(b.h3("Ví dụ 10 • Tính cạnh và diện tích"))
    story.append(b.p("Cho $AB=5$, $AC=8$ và $\\widehat A=60^\\circ$. Tính $BC$ và diện tích tam giác."))
    story.extend(b.formula(r"BC^2=8^2+5^2-2\cdot8\cdot5\cdot\cos60^\circ=64+25-40=49."))
    story.append(b.p("Vậy $BC=7$. Diện tích $S=\\frac12\\cdot AB\\cdot AC\\cdot\\sin A=\\frac12\\cdot5\\cdot8\\cdot\\frac{\\sqrt3}{2}=10\\sqrt3$ (đơn vị diện tích).", "Answer"))

    story.append(b.h3("6.2. Định lí sin – cặp cạnh/góc đối diện và bán kính ngoại tiếp"))
    story.extend(b.formula(r"\frac a{\sin A}=\frac b{\sin B}=\frac c{\sin C}=2R."))
    story.append(b.box("Cảnh báo góc khi dùng arcsin", [
        "Từ $\\sin B=k$ có thể có $B$ nhọn hoặc $B=180^\\circ-B$ (tù). Phải dùng tổng ba góc, độ dài cạnh đối diện "
        "và dữ kiện bài toán để chọn nghiệm; không mặc nhiên lấy góc nhọn."
    ], "warning"))
    story.append(b.h3("Ví dụ 11 • Tính cạnh bằng định lí sin"))
    story.append(b.p("Cho $a=8$, $A=30^\\circ$, $B=45^\\circ$. Tính $b$ và $R$."))
    story.extend(b.formula(r"b=\frac{a\sin B}{\sin A}=\frac{8\cdot\frac{\sqrt2}{2}}{\frac12}=8\sqrt2,\qquad R=\frac a{2\sin A}=\frac8{2\cdot\frac12}=8."))
    story.append(b.p("Vậy $b=8\\sqrt2$ và $R=8$ (cùng đơn vị độ dài với $a$).", "Answer"))

    story.append(b.h3("6.3. Bốn công thức diện tích – chọn theo dữ kiện"))
    story.append(b.table([
        ["Dữ kiện nổi bật", "Công thức nên dùng"],
        ["Hai cạnh và góc xen giữa", "$S=\\frac12bc\\sin A=\\frac12ca\\sin B=\\frac12ab\\sin C$."],
        ["Ba cạnh", "Heron: $S=\\sqrt{p(p-a)(p-b)(p-c)}$, $p=(a+b+c)/2$."],
        ["Ba cạnh và $R$", "$S=abc/(4R)$."],
        ["Nửa chu vi và $r$", "$S=pr$."],
        ["Cạnh đáy và chiều cao tương ứng", "$S=\\frac12ah_a$."],
    ], [54 * mm, CONTENT_W - 54 * mm]))
    story.append(b.h3("Ví dụ 12 • Tam giác 13–14–15"))
    story.append(b.p("Tính diện tích tam giác có ba cạnh $13,14,15$ và bán kính đường tròn nội tiếp."))
    story.append(b.p("Nửa chu vi $p=(13+14+15)/2=21$. Áp dụng Heron:"))
    story.extend(b.formula(r"S=\sqrt{21(21-13)(21-14)(21-15)}=\sqrt{21\cdot8\cdot7\cdot6}=\sqrt{7056}=84."))
    story.append(b.p("Từ $S=pr$, suy ra $r=S/p=84/21=4$. Vậy $S=84$ và $r=4$ (đơn vị tương ứng).", "Answer"))

    story.append(b.h3("6.4. Giải tam giác và bài toán thực tiễn"))
    story.append(b.table([
        ["Dữ kiện", "Đường đi gợi ý"],
        ["Hai cạnh + góc xen giữa", "Côsin tìm cạnh thứ ba → côsin hoặc sin tìm góc → tổng góc 180°."],
        ["Ba cạnh", "Côsin tìm góc → tổng góc; Heron nếu cần diện tích."],
        ["Một cạnh + hai góc", "Tổng góc tìm góc còn lại → định lí sin tìm các cạnh."],
        ["Khoảng cách không đo trực tiếp", "Chọn điểm quan sát tạo tam giác; đo hai cạnh/góc hoặc cạnh/hai góc rồi chọn định lí phù hợp."],
    ], [55 * mm, CONTENT_W - 55 * mm]))
    story.append(b.h3("Ví dụ 13 • Khoảng cách qua vật cản"))
    story.append(b.p("Hai điểm $A,B$ bị vật cản ngăn cách. Từ điểm $C$ đo được $CA=7$ km, $CB=9$ km và $\\widehat{ACB}=60^\\circ$. Tính $AB$, làm tròn đến hai chữ số thập phân."))
    story.extend(b.formula(r"AB^2=7^2+9^2-2\cdot7\cdot9\cdot\cos60^\circ=67\quad\Rightarrow\quad AB=\sqrt{67}\approx8{,}19\ \text{km}."))
    story.append(b.p("Kết luận phải có đơn vị và mức làm tròn theo yêu cầu. Hình vẽ chỉ hỗ trợ chọn tam giác; kết quả dựa trên số đo đã cho.", "Answer"))
    story.append(b.box("Bốn lượt kiểm tra sau khi giải tam giác", [
        "① Tổng góc bằng 180°? ② Cạnh lớn hơn có đối diện góc lớn hơn? ③ Ba cạnh thỏa mãn bất đẳng thức tam giác? "
        "④ Đã giữ đúng đơn vị và chỉ làm tròn cuối cùng?"
    ], "remember"))

    story.append(b.h3("Luyện nhanh D • Lượng giác và tam giác"))
    for i, text in enumerate([
        "Tính $\\sin135^\\circ$ và $\\cos135^\\circ$.",
        "Cho $\\sin\\alpha=3/5$, $\\alpha$ tù. Tính $\\cos\\alpha$.",
        "Vì sao $\\tan90^\\circ$ không xác định?",
        "Cho $AB=6,AC=4,\\widehat A=60^\\circ$. Tính $BC^2$.",
        "Cho $a=10,A=30^\\circ$. Tính $R$.",
        "Tính diện tích tam giác có $a=5,b=6,C=30^\\circ$.",
        "Tính diện tích tam giác có ba cạnh $3,4,5$ bằng Heron.",
        "Nếu chỉ biết ba cạnh và cần một góc, nên dùng định lí nào?",
    ], 1):
        story.append(b.numbered(text, f"{i}."))
    story.append(b.table([
        ["Câu", "Đáp án / căn cứ"],
        ["1", "$\\sin135^\\circ=\\sqrt2/2$; $\\cos135^\\circ=-\\sqrt2/2$."],
        ["2", "$\\cos\\alpha=-4/5$ vì góc tù có côsin âm."],
        ["3", "$\\cos90^\\circ=0$ nên thương $\\sin/\\cos$ không xác định."],
        ["4", "$BC^2=6^2+4^2-2\\cdot6\\cdot4\\cdot1/2=28$."],
        ["5", "$2R=a/\\sin A=20$, nên $R=10$."],
        ["6", "$S=\\frac12\\cdot5\\cdot6\\cdot1/2=7{,}5$."],
        ["7", "$p=6$, $S=\\sqrt{6\\cdot3\\cdot2\\cdot1}=6$."],
        ["8", "Định lí côsin dạng $\\cos A=(b^2+c^2-a^2)/(2bc)$."],
    ], [14 * mm, CONTENT_W - 14 * mm]))

    # ------------------------------------------------------------------
    story += [PageBreak(), b.h1("PHẦN V • CHƯƠNG IV: CÁC KHÁI NIỆM MỞ ĐẦU VỀ VECTƠ")]
    story.append(b.p(
        "<b>Phạm vi đúng ma trận:</b> nhận biết và thông hiểu khái niệm vectơ; không đi sâu phép toán vectơ ở các bài sau."
    ))
    story.append(b.h2("BÀI 7 • VECTƠ, GIÁ, PHƯƠNG, HƯỚNG VÀ ĐỘ DÀI"))
    story.append(b.h3("7.1. Vectơ là đoạn thẳng có hướng"))
    story.append(b.bullet("$\\overrightarrow{AB}$ có điểm đầu $A$, điểm cuối $B$. $\\overrightarrow{AB}$ và $\\overrightarrow{BA}$ khác nhau nếu $A\\ne B$."))
    story.append(b.bullet("Độ dài $|\\overrightarrow{AB}|=AB$: khoảng cách giữa điểm đầu và điểm cuối."))
    story.append(b.bullet("Giá của $\\overrightarrow{AB}$ là đường thẳng $AB$ (với $A\\ne B$)."))
    story.append(b.bullet("Vectơ-không $\\overrightarrow 0$ có điểm đầu trùng điểm cuối, độ dài 0. Theo quy ước trong ma trận, vectơ-không cùng phương và cùng hướng với mọi vectơ."))

    story.append(b.h3("7.2. Cùng phương → chưa chắc cùng hướng → chưa chắc bằng nhau"))
    story.append(b.table([
        ["Khái niệm", "Điều kiện", "Điều chưa đủ để kết luận"],
        ["Cùng phương", "Hai giá song song hoặc trùng nhau.", "Chưa biết cùng hướng hay ngược hướng."],
        ["Cùng hướng", "Đã cùng phương và mũi tên chỉ cùng chiều.", "Chưa chắc độ dài bằng nhau."],
        ["Ngược hướng", "Đã cùng phương và mũi tên chỉ ngược chiều.", "Chưa chắc độ dài bằng nhau."],
        ["Bằng nhau", "<b>Cùng hướng và cùng độ dài.</b>", "Chỉ cùng độ dài là chưa đủ."],
        ["Đối nhau", "Ngược hướng và cùng độ dài.", "Hai vectơ đối nhau không bằng nhau nếu khác vectơ-không."],
    ], [31 * mm, 65 * mm, CONTENT_W - 96 * mm]))
    story.append(parallelogram_diagram())
    story.append(b.p("Trong hình bình hành $ABCD$: $\\overrightarrow{AB}=\\overrightarrow{DC}$ và $\\overrightarrow{AD}=\\overrightarrow{BC}$.", "Caption"))

    story.append(b.h3("Ví dụ 14 • Chứng minh hai vectơ bằng nhau"))
    story.append(b.p("Cho hình bình hành $ABCD$. Chứng minh $\\overrightarrow{AB}=\\overrightarrow{DC}$."))
    story.append(b.p("Vì $AB\\parallel DC$ nên hai vectơ cùng phương. Theo thứ tự đỉnh của hình bình hành, $\\overrightarrow{AB}$ và $\\overrightarrow{DC}$ cùng hướng. Mặt khác $AB=DC$ (hai cạnh đối của hình bình hành). Hai vectơ vừa cùng hướng vừa cùng độ dài nên bằng nhau.", "Answer"))
    story.append(b.box("Mẫu trình bày hai điều kiện", [
        "Không chỉ viết “$AB=DC$ nên hai vectơ bằng nhau”. Hãy viết riêng: <b>(1) cùng hướng; (2) cùng độ dài</b>, rồi kết luận."
    ], "tip"))

    story.append(b.h3("Ví dụ 15 • Độ dài không xác định vectơ"))
    story.append(b.p("Cho hai đoạn thẳng $MN=PQ=5$ cm. Có thể kết luận $\\overrightarrow{MN}=\\overrightarrow{PQ}$ không?"))
    story.append(b.p("Không. Ta mới chỉ có cùng độ dài. Nếu hai giá khác phương hoặc hai mũi tên ngược hướng thì hai vectơ không bằng nhau. Cần thêm điều kiện cùng hướng.", "Answer"))

    story.append(b.h3("Luyện nhanh E • Vectơ"))
    for i, text in enumerate([
        "Xác định điểm đầu, điểm cuối của $\\overrightarrow{PQ}$.",
        "Tính $|\\overrightarrow{AA}|$.",
        "Hai vectơ cùng hướng có cùng phương không?",
        "Hai vectơ cùng phương có nhất thiết cùng hướng không?",
        "Trong hình bình hành $ABCD$, điền vectơ bằng $\\overrightarrow{AD}$.",
        "Nêu đủ điều kiện để hai vectơ bằng nhau.",
        "Hai vectơ đối nhau có độ dài như thế nào?",
        "Hình vuông cạnh $a$ có độ dài vectơ đường chéo bằng bao nhiêu?",
    ], 1):
        story.append(b.numbered(text, f"{i}."))
    story.append(b.table([
        ["Câu", "Đáp án / căn cứ"],
        ["1", "Điểm đầu $P$, điểm cuối $Q$."],
        ["2", "$0$; đây là một vectơ-không."],
        ["3", "Có."],
        ["4", "Không; có thể ngược hướng."],
        ["5", "$\\overrightarrow{BC}$."],
        ["6", "Cùng hướng và cùng độ dài."],
        ["7", "Bằng nhau; hai vectơ ngược hướng."],
        ["8", "$a\\sqrt2$."],
    ], [14 * mm, CONTENT_W - 14 * mm]))

    from guide.assessment import add_formula_and_exam
    from guide.solutions import add_solutions
    add_formula_and_exam(b, story)
    add_solutions(b, story)
    return story
