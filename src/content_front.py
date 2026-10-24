# -*- coding: utf-8 -*-
"""Trang bìa, lời nói đầu, mục lục và Phần A (phân tích đề – chiến lược ôn tập)."""

from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.utils import simpleSplit
from reportlab.platypus import NextPageTemplate, PageBreak, Spacer, Table, TableStyle

from pdf_kit import (
    ACCENT, ACCENT_SOFT, AMBER_SOFT, BORDER, CONTENT_W, FONT_BOLD, FONT_REG, GREEN,
    GREEN_SOFT, INK, MUTED, PAGE_H, PAGE_W, PRIMARY, PRIMARY_DARK, PRIMARY_SOFT,
    PURPLE_SOFT, STYLES, TEAL, WHITE, H1, H2, H3, P, SP, box, bullets, formula,
    numbered, rt, rule, tbl,
)

# --------------------------------------------------------------------------
# Trang bìa (vẽ trực tiếp trên canvas)
# --------------------------------------------------------------------------


def _wrap(c, text, x, y, width, font=FONT_REG, size=9, leading=13, color=INK,
          align="left"):
    c.setFont(font, size)
    c.setFillColor(color)
    lines = simpleSplit(text, font, size, width)
    for line in lines:
        if align == "center":
            c.drawCentredString(x + width / 2, y, line)
        elif align == "right":
            c.drawRightString(x + width, y, line)
        else:
            c.drawString(x, y, line)
        y -= leading
    return y


def draw_cover(c, doc):
    c.saveState()
    c.setFillColor(colors.white)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)

    # dải màu phía trên
    band_h = 96 * mm
    c.setFillColor(PRIMARY_DARK)
    c.rect(0, PAGE_H - band_h, PAGE_W, band_h, stroke=0, fill=1)
    c.setFillColor(colors.HexColor("#0E2B47"))
    c.rect(0, PAGE_H - band_h, PAGE_W, 4 * mm, stroke=0, fill=1)
    c.setFillColor(colors.HexColor("#F59E0B"))
    c.rect(0, PAGE_H - band_h - 1.6 * mm, PAGE_W, 1.6 * mm, stroke=0, fill=1)

    _wrap(c, "TRƯỜNG THPT HÀ HUY TẬP  ·  TỔ TOÁN – TIN", 20 * mm, PAGE_H - 24 * mm,
          PAGE_W - 40 * mm, FONT_BOLD, 9, 12, colors.HexColor("#BFD3E8"), "center")
    _wrap(c, "ĐỀ CƯƠNG ÔN TẬP", 20 * mm, PAGE_H - 45 * mm, PAGE_W - 40 * mm,
          FONT_BOLD, 31, 36, WHITE, "center")
    _wrap(c, "GIỮA HỌC KÌ I  ·  NĂM HỌC 2026 – 2027", 20 * mm, PAGE_H - 60 * mm,
          PAGE_W - 40 * mm, FONT_REG, 13.5, 18, colors.HexColor("#DCE9F6"), "center")
    _wrap(c, "MÔN TOÁN  ·  LỚP 10  ·  90 PHÚT", 20 * mm, PAGE_H - 74 * mm,
          PAGE_W - 40 * mm, FONT_BOLD, 9.4, 13, colors.HexColor("#9FC2E2"), "center")

    # tên sách
    y = PAGE_H - band_h - 26 * mm
    _wrap(c, "TOÁN 10", 20 * mm, y, PAGE_W - 40 * mm, FONT_BOLD, 44, 50, PRIMARY, "center")
    _wrap(c, "Bộ sách Kết nối tri thức với cuộc sống", 20 * mm, y - 16 * mm,
          PAGE_W - 40 * mm, FONT_REG, 13, 18, MUTED, "center")

    # ba ô thông tin
    y_boxes = y - 46 * mm
    items = [("24 + 3", "câu hỏi & tự luận"), ("10", "điểm · thang điểm 10"),
             ("7", "ngày ôn tập gợi ý")]
    box_w, gap = 48 * mm, 8 * mm
    total = 3 * box_w + 2 * gap
    x0 = (PAGE_W - total) / 2
    for i, (big, small) in enumerate(items):
        x = x0 + i * (box_w + gap)
        c.setFillColor(colors.HexColor("#F5F8FC"))
        c.setStrokeColor(colors.HexColor("#DCE5EF"))
        c.setLineWidth(0.8)
        c.roundRect(x, y_boxes, box_w, 22 * mm, 3 * mm, stroke=1, fill=1)
        c.setFillColor(PRIMARY)
        c.setFont(FONT_BOLD, 20)
        c.drawCentredString(x + box_w / 2, y_boxes + 11 * mm, big)
        c.setFillColor(MUTED)
        c.setFont(FONT_REG, 7.8)
        c.drawCentredString(x + box_w / 2, y_boxes + 5 * mm, small)

    # thẻ nội dung
    card_x, card_w = 22 * mm, PAGE_W - 44 * mm
    card_top = y_boxes - 12 * mm
    rows = [
        ("Lý thuyết trọng tâm", "4 chương, tóm tắt bằng bảng và công thức"),
        ("12 dạng toán + ví dụ mẫu", "quy trình giải từng bước, kèm lỗi thường gặp"),
        ("ĐỀ MẪU đầy đủ", "12 TN · 2 Đúng–Sai · 4 trả lời ngắn · 3 tự luận"),
        ("Đáp án & lời giải chi tiết", "giải thích vì sao, không chỉ đáp số"),
        ("Tự luyện + phụ lục", "22 bài tập có đáp số, bảng GTLG, mẹo máy tính"),
    ]
    card_h = 12 * mm + len(rows) * 11.5 * mm
    card_y = card_top - card_h
    c.setFillColor(PRIMARY_SOFT)
    c.setStrokeColor(colors.HexColor("#C8D9EA"))
    c.setLineWidth(0.9)
    c.roundRect(card_x, card_y, card_w, card_h, 3 * mm, stroke=1, fill=1)
    c.setFillColor(PRIMARY_DARK)
    c.setFont(FONT_BOLD, 8.6)
    c.drawString(card_x + 7 * mm, card_top - 8 * mm, "TRONG TÀI LIỆU NÀY")
    ry = card_top - 17 * mm
    for title, sub in rows:
        c.setFillColor(GREEN)
        c.setFont(FONT_BOLD, 9.4)
        c.drawString(card_x + 7 * mm, ry, "✓")
        c.setFillColor(INK)
        c.setFont(FONT_BOLD, 8.9)
        c.drawString(card_x + 12 * mm, ry, title)
        c.setFillColor(MUTED)
        c.setFont(FONT_REG, 8.1)
        c.drawString(card_x + 12 * mm + c.stringWidth(title, FONT_BOLD, 8.9) + 3 * mm, ry, "— " + sub)
        ry -= 11.5 * mm

    # chân trang bìa
    _wrap(c, "Biên soạn bám sát Ma trận đề và Bảng đặc tả kiểm tra Giữa kì I – môn Toán, lớp 10, "
            "năm học 2026–2027 (Tổ Toán – Tin). Tài liệu ôn tập, không phải đề thi chính thức.",
          22 * mm, 24 * mm, PAGE_W - 44 * mm, FONT_REG, 7.8, 11, MUTED, "center")
    _wrap(c, "Phiên bản 1.0  ·  10/2026", 22 * mm, 15 * mm, PAGE_W - 44 * mm,
          FONT_REG, 7.8, 10, colors.HexColor("#94A3B8"), "center")
    c.restoreState()


# --------------------------------------------------------------------------
# Lời nói đầu
# --------------------------------------------------------------------------

def preface() -> list:
    out = [
        H1("Lời nói đầu"),
        P("Tài liệu này dành cho học sinh lớp 10 đang ôn tập {b}Giữa học kì I{/b} theo bộ sách "
          "{b}Kết nối tri thức với cuộc sống{/b}. Nội dung được biên soạn bám sát {b}Ma trận đề{/b} và "
          "{b}Bảng đặc tả{/b} kiểm tra Giữa kì I năm học 2026–2027 của Tổ Toán – Tin, Trường THPT Hà Huy Tập "
          "(tệp nguồn: {i}“MA TRẬN TOÁN 10 - GIỮA KÌ I.docx”{/i}).", "lead"),
        SP(3),
        P("Mục tiêu của tài liệu gồm bốn việc: {b}(1){/b} giúp bạn nắm chắc phần lý thuyết cốt lõi của bốn "
          "chương; {b}(2){/b} nhận diện được các dạng toán thường gặp và quy trình giải từng dạng; "
          "{b}(3){/b} luyện tập trên một đề mẫu có cấu trúc, độ khó và cách cho điểm giống đề thật; "
          "{b}(4){/b} tự chấm – tự đánh giá để biết mình cần quay lại phần nào."),
        SP(4),
        H2("Một điều bạn cần biết về nguồn tài liệu"),
        P("Tệp gốc là {b}ma trận đề và bảng đặc tả{/b} — tức là bản thiết kế của đề kiểm tra: nó quy định "
          "kiểm tra đơn vị kiến thức nào, ở mức độ nào, bằng dạng câu gì, bao nhiêu điểm. Tệp {b}không chứa "
          "đề bài và đáp án{/b}. Vì vậy, để có một “đề kiểm tra kèm đáp án” đúng như bạn yêu cầu, tài liệu "
          "dựng một {b}ĐỀ MẪU hoàn chỉnh{/b} tuân thủ đúng khung của ma trận:"),
        SP(2),
        bullets([
            "{b}12 câu{/b} trắc nghiệm nhiều lựa chọn – 3,0 điểm (0,25 điểm/câu);",
            "{b}2 câu{/b} trắc nghiệm Đúng – Sai, mỗi câu 4 ý – 2,0 điểm (chấm theo số ý đúng: 1 ý 0,1; "
            "2 ý 0,25; 3 ý 0,5; 4 ý 1,0);",
            "{b}4 câu{/b} trắc nghiệm trả lời ngắn – 2,0 điểm (0,5 điểm/câu);",
            "{b}3 câu{/b} tự luận – 3,0 điểm; thời gian 90 phút.",
        ]),
        SP(2),
        P("Mỗi câu trong đề mẫu được ánh xạ một–một tới một dòng trong bảng đặc tả (xem {b}Bảng A.3{/b}); "
          "nhờ vậy bạn ôn đúng trọng tâm, không lan man. Toàn bộ {b}27 câu{/b} đều có đáp án và lời giải "
          "chi tiết ở {b}Phần D{/b}, kèm thang điểm và hướng dẫn chấm phần tự luận."),
        SP(3),
        box("warn",
            "Nếu thầy cô đã phát đề chính thức, hãy dùng Phần B–E để ôn và luyện, rồi đối chiếu đề thật "
            "với cấu trúc ở Bảng A.1 để biết phần nào cần tập trung. Đề mẫu trong tài liệu là đề luyện, "
            "{b}không phải đề thi{/b}.",
            title="LƯU Ý VỀ TÍNH TRUNG THỰC"),
        SP(4),
        H2("Cách dùng tài liệu trong 7 ngày"),
        tbl([
            ["Bước", "Việc cần làm", "Thời gian"],
            ["1", "Đọc Phần A để biết đề gồm những gì và phân bổ thời gian làm bài.", "15 phút"],
            ["2", "Học lý thuyết + dạng toán của mỗi chương trong Phần B, làm lại ví dụ mẫu "
                  "{i}trước khi{/i} xem lời giải.", "4–5 giờ (chia 4 buổi)"],
            ["3", "Làm trọn đề mẫu Phần C trong 90 phút, đúng giờ, không mở tài liệu.", "90 phút"],
            ["4", "Tự chấm theo Phần D, ghi lại các câu sai và đọc lại đúng dạng toán đó.", "45 phút"],
            ["5", "Làm bài tự luyện Phần E, ưu tiên nhóm đã sai nhiều.", "60 phút"],
            ["6", "Học lại bảng công thức (B.5) và các lỗi thường gặp; làm lại câu từng sai.", "30 phút"],
        ], widths=[14 * mm, CONTENT_W - 14 * mm - 34 * mm, 34 * mm], align=["c", "l", "c"]),
        SP(4),
        H2("Quy ước kí hiệu trong tài liệu"),
        bullets([
            "{b}Vectơ{/b} được in đậm: {b}AB{/b} là vectơ có điểm đầu A, điểm cuối B; |{b}AB{/b}| là độ dài "
            "đoạn thẳng AB. Cách viết này tương đương với mũi tên trên đầu trong sách giáo khoa.",
            "{b}Tập hợp số{/b}: ℕ (số tự nhiên), ℕ* (số tự nhiên khác 0), ℤ (số nguyên), ℚ (số hữu tỉ), "
            "ℝ (số thực); ∅ là tập rỗng.",
            "{b}Khoảng – đoạn{/b}: (a; b) không lấy hai đầu mút; [a; b] lấy cả hai; [a; b) và (a; b] lấy một đầu. "
            "Dấu “;” dùng để phân biệt với dấu thập phân.",
            "{b}Đ{/b} = Đúng, {b}S{/b} = Sai (phần trắc nghiệm Đúng – Sai).",
            "Góc được đo bằng độ; 0° ≤ α ≤ 180°.",
        ]),
        SP(3),
        P("{i}Tài liệu được soạn cho việc tự học: mọi công thức đều có ví dụ đi kèm, mọi dạng toán đều có "
          "quy trình và lỗi thường gặp. Nếu một chỗ nào chưa rõ, hãy ghi lại rồi hỏi thầy cô – đó là cách "
          "ôn tập hiệu quả nhất.{/i}", "small"),
        SP(6),
        H2("Ba câu hỏi để bắt đầu đúng chỗ"),
        P("Trước khi đọc tiếp, hãy tự trả lời (ghi ra giấy, mất 2 phút):"),
        SP(2),
        tbl([
            ["Câu hỏi", "Nếu câu trả lời là …", "Thì bắt đầu từ …"],
            ["1. Chương nào mình thấy khó nhất?", "Chương I / II / III / IV",
             "Phần B tương ứng: B.1 / B.2 / B.3 / B.4"],
            ["2. Mình mất điểm vì không nhớ công thức hay vì không biết làm?",
             "Không nhớ công thức", "B.5 – Bảng công thức cần nhớ"],
            ["", "Không biết cách làm", "Các dạng toán trong Phần B (mỗi dạng có quy trình 3–4 bước)"],
            ["3. Mình đã làm thử đề chưa?", "Chưa", "Phần C – làm ngay đề mẫu để biết mình đang ở đâu"],
            ["", "Rồi, và sai nhiều", "Phần D – chấm kĩ, đọc lại dạng toán tương ứng"],
        ], widths=[52 * mm, 44 * mm, CONTENT_W - 96 * mm], fontsize=8.3,
            align=["l", "l", "l"]),
        SP(3),
        box("tip",
            [P("{b}Nguyên tắc ôn tập hiệu quả nhất:{/b} {b}làm bài trước, đọc lời giải sau{/b}. Đọc lời giải "
               "mà không tự làm giống như xem người khác bơi – bạn hiểu, nhưng bạn chưa bơi được.", "box_body")]),
    ]
    return out


# --------------------------------------------------------------------------
# Mục lục
# --------------------------------------------------------------------------

def toc_page() -> list:
    from reportlab.platypus.tableofcontents import TableOfContents
    t = TableOfContents()
    t.levelStyles = [STYLES["toc0"], STYLES["toc1"], STYLES["toc2"]]
    t.dotsMinLevel = 0
    return [
        H1("Mục lục"),
        P("Các mục được đánh số theo phần; số trang ghi bên phải.", "small"),
        SP(8),
        t,
        SP(10),
        box("tip",
            "Muốn ôn nhanh trước giờ kiểm tra? Đọc {b}B.5 – Bảng công thức cần nhớ{/b}, "
            "{b}A.6 – Các lỗi mất điểm{/b} và {b}D.1 – Đáp án nhanh{/b}.",
            title="GỢI Ý ĐỌC NHANH"),
    ]


# --------------------------------------------------------------------------
# PHẦN A
# --------------------------------------------------------------------------

def part_a() -> list:
    out = [
        H1("PHẦN A. PHÂN TÍCH ĐỀ VÀ CHIẾN LƯỢC ÔN TẬP"),
        P("Phần này trả lời bốn câu hỏi: đề gồm những gì? kiến thức nào chiếm nhiều điểm nhất? "
          "90 phút nên chia thế nào? và bảy ngày trước kì thi nên học gì mỗi ngày?"),
        SP(6),

        H2("A.1. Cấu trúc đề kiểm tra"),
        P("Theo mục {b}II. HÌNH THỨC{/b} của ma trận, đề gồm bốn phần với tổng 24 câu trắc nghiệm và "
          "3 câu tự luận, thang điểm 10, thời gian 90 phút:"),
        SP(2),
        tbl([
            ["Phần", "Dạng câu", "Số câu", "Điểm", "Thời gian"],
            ["I", "Trắc nghiệm nhiều phương án lựa chọn (A, B, C, D)", "12", "3,0", "22 phút"],
            ["II", "Trắc nghiệm Đúng – Sai (mỗi câu 4 ý)", "2", "2,0", "15 phút"],
            ["III", "Trắc nghiệm trả lời ngắn (điền kết quả)", "4", "2,0", "15 phút"],
            ["IV", "Tự luận (trình bày lời giải)", "3", "3,0", "33 phút"],
            ["", "Rà soát, kiểm tra lại bài", "—", "—", "5 phút"],
            ["Tổng", "24 câu TN + 3 câu TL", "27", "10,0", "90 phút"],
        ], widths=[16 * mm, CONTENT_W - 16 * mm - 18 * mm - 18 * mm - 34 * mm, 18 * mm, 18 * mm, 34 * mm],
            align=["c", "l", "c", "c", "c"],
            row_colors={6: PRIMARY_SOFT}),
        SP(3),
        box("note",
            [P("Cách chấm phần {b}Đúng – Sai{/b} (theo ma trận): đúng 1 ý được 0,1 điểm; đúng 2 ý được "
               "0,25; đúng 3 ý được 0,5; đúng cả 4 ý được 1,0. Vì vậy {b}khoanh bừa cả 4 ý là lỗ{/b}: "
               "xác suất đúng cả 4 chỉ 1/16, còn “đúng 3 ý” cũng rất khó. Hãy phân tích từng ý.", "box_body")]),

        SP(6),
        H2("A.2. Ma trận nội dung rút gọn: điểm nằm ở đâu?"),
        P("Bảng dưới đây tóm tắt ma trận gốc. Cột “TN” là số câu/ý trắc nghiệm, cột “TL” là số câu tự luận."),
        SP(2),
        tbl([
            ["Chủ đề", "Đơn vị kiến thức", "Mức độ", "TN", "TL", "Điểm"],
            ["1. Mệnh đề. Tập hợp", "1.1. Mệnh đề", "NB", "2", "—", "0,5"],
            ["", "1.2. Tập hợp", "NB, TH", "4", "—", "1,25"],
            ["", "1.3. Các phép toán trên tập hợp", "NB, TH, VD", "4", "1", "2,25"],
            ["2. Bất phương trình và hệ bất phương trình bậc nhất hai ẩn",
             "2.1. Bất phương trình bậc nhất hai ẩn", "NB, TH, VD", "5", "—", "1,25"],
            ["", "2.2. Hệ bất phương trình bậc nhất hai ẩn", "NB, VDC", "1", "1", "1,25"],
            ["3. Hệ thức lượng trong tam giác", "3.1. Giá trị lượng giác của góc 0°–180°",
             "NB, TH, VD", "3", "—", "1,0"],
            ["", "3.2. Hệ thức lượng trong tam giác", "NB, TH, VD", "3", "1", "2,0"],
            ["4. Vectơ", "4.1. Khái niệm vectơ", "NB, TH", "2", "—", "0,5"],
            ["Tổng", "", "", "24", "3", "10,0"],
        ], widths=[42 * mm, CONTENT_W - 42 * mm - 26 * mm - 12 * mm - 12 * mm - 16 * mm,
                   26 * mm, 12 * mm, 12 * mm, 16 * mm],
            fontsize=8.1, align=["l", "l", "c", "c", "c", "c"],
            row_colors={9: PRIMARY_SOFT}),
        SP(3),
        P("{b}Nhận xét quan trọng.{/b} Ba vùng chiếm điểm nhiều nhất là: phép toán trên tập hợp (2,25 điểm), "
          "hệ thức lượng trong tam giác (2,0 điểm) và bất phương trình bậc nhất hai ẩn (1,25 điểm). "
          "Chương I và Chương II chiếm khoảng {b}6,5/10 điểm{/b} nhưng chủ yếu ở mức nhận biết – thông hiểu, "
          "tức là {b}dễ lấy điểm nếu nhớ đúng định nghĩa và quy tắc{/b}. Câu khó nhất (vận dụng cao) nằm ở "
          "bài toán tối ưu của hệ bất phương trình. Chiến lược hợp lý: {b}ăn chắc 6,5 điểm đầu{/b}, "
          "giữ chắc phần lượng giác, rồi mới đầu tư vào câu tối ưu."),
        SP(6),

        H2("A.3. Bảng đặc tả được hiện thực hoá trong đề mẫu"),
        P("Mỗi dòng dưới đây là một yêu cầu của bảng đặc tả và câu hỏi tương ứng trong {b}Phần C{/b}. "
          "Khi ôn, bạn có thể đối chiếu ngược: làm sai câu nào → tra bảng → biết ngay phải ôn dạng nào."),
        SP(2),
        tbl([
            ["Đơn vị kiến thức", "Yêu cầu cần đạt (theo đặc tả)", "Câu trong đề mẫu", "Mức"],
            ["1.1. Mệnh đề", "Nhận biết mệnh đề, mệnh đề phủ định; ý nghĩa ∀, ∃",
             "I.1, I.2", "NB"],
            ["1.2. Tập hợp", "Liệt kê phần tử; dùng kí hiệu khoảng, đoạn; số tập con",
             "I.3; II.1a; III.1", "NB, TH"],
            ["1.3. Phép toán trên tập hợp",
             "Giao, hợp, hiệu, phần bù; biểu diễn trên trục số; bài toán thực tế",
             "I.4; II.1b–d; III.2; IV.1", "NB, TH, VD"],
            ["2.1. Bất phương trình bậc nhất hai ẩn",
             "Nhận biết BPT; nghiệm và miền nghiệm; mô tả miền nghiệm; chuyển điều kiện thực tế",
             "I.5; II.2a–d", "NB, TH, VD"],
            ["2.2. Hệ bất phương trình bậc nhất hai ẩn",
             "Miền nghiệm của hệ; tìm phương án tối ưu", "I.6; IV.3", "NB, VDC"],
            ["3.1. Giá trị lượng giác",
             "GTLG của góc 0°–180°; hai góc bù nhau; tính GTLG khi biết một giá trị",
             "I.7, I.8; III.3", "NB, TH, VD"],
            ["3.2. Hệ thức lượng trong tam giác",
             "Định lí côsin, định lí sin, công thức diện tích; giải tam giác; bài toán thực tế",
             "I.9, I.10; III.4; IV.2", "NB, TH, VD"],
            ["4.1. Khái niệm vectơ",
             "Vectơ, độ dài, cùng phương – cùng hướng; hai vectơ bằng nhau",
             "I.11, I.12", "NB, TH"],
        ], widths=[38 * mm, CONTENT_W - 38 * mm - 38 * mm - 16 * mm, 38 * mm, 16 * mm],
            fontsize=8.1, align=["l", "l", "l", "c"]),
        SP(3),
        P("Ghi chú: “I” = Phần I (trắc nghiệm lựa chọn), “II” = Phần II (Đúng – Sai), "
          "“III” = Phần III (trả lời ngắn), “IV” = Phần IV (tự luận)."),
        SP(6),

        H2("A.4. Chiến lược làm bài trong 90 phút"),
        P("Điểm số không tỉ lệ với số câu làm được mà tỉ lệ với số câu {b}đúng{/b}. Hãy đi theo ba vòng:"),
        SP(2),
        tbl([
            ["Vòng", "Thời gian", "Việc làm", "Mục tiêu"],
            ["1. Lấy điểm chắc", "0–22 phút", "Làm 12 câu trắc nghiệm lựa chọn. Câu nào quá 90 giây "
             "thì đánh dấu, bỏ qua.", "9–12 câu đúng"],
            ["2. Xử lý Đúng – Sai", "22–37 phút", "Với mỗi câu, đọc kĩ từng ý; loại ý hiển nhiên sai "
             "trước, rồi kiểm tra bằng phản ví dụ.", "≥ 6/8 ý đúng"],
            ["3. Trả lời ngắn", "37–52 phút", "Tính ra giấy nháp, ghi đúng dạng (phân số, căn, số thập "
             "phân theo yêu cầu).", "3–4 câu đúng"],
            ["4. Tự luận", "52–85 phút", "Trình bày theo cấu trúc: đặt vấn đề – công thức – thay số – "
             "kết luận. Câu tối ưu làm sau cùng.", "2,0–3,0 điểm"],
            ["5. Rà soát", "85–90 phút", "Kiểm tra phiếu trả lời, đơn vị, dấu của cos, dấu ngoặc của "
             "tập hợp.", "Tránh mất điểm vô ích"],
        ], widths=[30 * mm, 26 * mm, CONTENT_W - 30 * mm - 26 * mm - 32 * mm, 32 * mm],
            fontsize=8.2, align=["l", "c", "l", "l"]),
        SP(3),
        box("exam",
            [P("Ba thói quen cứu điểm:", "box_body"),
             bullets([
                 "Câu nào {b}không chắc{/b}: loại hai phương án sai rõ ràng rồi mới chọn, đừng bỏ trống.",
                 "Với câu trả lời ngắn: viết lại đề bằng kí hiệu trước khi tính – phần lớn lỗi là lỗi "
                 "{i}đọc sai đề{/i}, không phải lỗi tính.",
                 "Câu tự luận: {b}không bao giờ{/b} bỏ trống. Viết công thức đúng đã có điểm; mất 1 phút "
                 "ghi công thức rẻ hơn mất 0,25 điểm.",
             ], "bullet_small")]),

        SP(6),
        H2("A.5. Kế hoạch ôn tập 7 ngày"),
        tbl([
            ["Ngày", "Nội dung", "Việc cụ thể", "Thời lượng"],
            ["1", "Chương I – Mệnh đề", "Học B.1.1, làm Dạng 1–3; tự phát biểu 10 mệnh đề và phủ định", "60–75′"],
            ["2", "Chương I – Tập hợp", "Học B.1.1 (tập hợp), làm Dạng 4–6; vẽ trục số cho 5 ví dụ", "75–90′"],
            ["3", "Chương II – BPT", "Học B.2, làm Dạng 1–2; vẽ miền nghiệm của 4 bất phương trình", "75–90′"],
            ["4", "Chương II – Tối ưu", "Làm Dạng 3–4; giải lại bài toán tối ưu trong đề mẫu", "60–75′"],
            ["5", "Chương III – Lượng giác", "Học bảng GTLG, làm Dạng 1–3; học thuộc bảng góc đặc biệt", "75–90′"],
            ["6", "Chương III – Tam giác + Vectơ", "Làm Dạng 4–7 và B.4; vẽ hình, ghi công thức", "75–90′"],
            ["7", "Tổng duyệt", "Làm trọn đề mẫu 90′, chấm, đọc lời giải các câu sai, làm lại", "150′"],
        ], widths=[12 * mm, 42 * mm, CONTENT_W - 12 * mm - 42 * mm - 24 * mm, 24 * mm],
            fontsize=8.2, align=["c", "l", "l", "c"]),
        SP(3),
        P("{i}Nếu chỉ còn 2 ngày: ngày 1 học B.5 (công thức) + làm đề mẫu; ngày 2 chữa kĩ các câu sai và "
          "làm lại đúng những câu đó. Đừng học thêm dạng mới sát ngày thi.{/i}", "small"),

        SP(6),
        H2("A.6. Mười lỗi mất điểm phổ biến"),
        tbl([
            ["#", "Lỗi", "Cách tránh"],
            ["1", "Viết [a; b] khi đề cho a < x < b", "Đọc kĩ dấu: {b}<{/b} → ngoặc tròn; {b}≤{/b} → ngoặc vuông."],
            ["2", "Tính A \\ B nhưng lấy cả phần tử thuộc B", "A \\ B = {x ∈ A và x ∉ B}: {b}lấy của A, bỏ của B{/b}."],
            ["3", "Nhầm phần bù C{sub}ℝ{/sub}A với A \\ B", "Phần bù chỉ xác định khi A ⊂ ℝ; kết quả gồm {b}phía ngoài{/b} A."],
            ["4", "Quên đổi chiều/giữ nguyên dấu khi biểu diễn miền nghiệm", "Thử điểm O(0;0): nếu thỏa thì tô nửa mặt phẳng {b}chứa O{/b}."],
            ["5", "Dùng định lí côsin với góc không xen giữa hai cạnh", "a² = b² + c² − 2bc·cos{b}A{/b} – góc A phải {b}đối diện{/b} cạnh a."],
            ["6", "Bỏ dấu âm của cos khi góc tù", "90° < α < 180° ⇒ cos α < 0, tan α < 0. Kiểm tra lại dấu trước khi kết luận."],
            ["7", "Nhầm sin(180° − α) = −sin α", "Hai góc bù: {b}sin bằng nhau{/b}, cos, tan, cot {b}đổi dấu{/b}."],
            ["8", "Đổi đơn vị độ – radian lẫn lộn khi bấm máy", "Máy phải ở chế độ {b}DEG{/b} (hiện chữ D trên màn hình)."],
            ["9", "Cho hai vectơ bằng nhau chỉ vì cùng độ dài", "Bằng nhau cần {b}cùng hướng{/b} và cùng độ dài."],
            ["10", "Kết luận bài tối ưu mà không thử {b}tất cả{/b} đỉnh", "Liệt kê đủ các đỉnh của miền, lập bảng giá trị F rồi so sánh."],
        ], widths=[8 * mm, 66 * mm, CONTENT_W - 8 * mm - 66 * mm],
            fontsize=8.2, align=["c", "l", "l"]),
    ]
    return out


def front_matter() -> list:
    return [
        NextPageTemplate("content"),
        PageBreak(),
        *preface(),
        PageBreak(),
        *toc_page(),
        PageBreak(),
        *part_a(),
        PageBreak(),
    ]
