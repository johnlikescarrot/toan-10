# -*- coding: utf-8 -*-
"""Phần mở đầu: lời dẫn, cách dùng tài liệu, cấu trúc đề, lộ trình ôn tập."""
from reportlab.lib.units import cm
from reportlab.platypus import CondPageBreak, PageBreak, Paragraph, Spacer

from pdfkit import (
    CONTENT_W, SectionBanner, callout, data_table, key_table, note, P, S,
    spacing, tip, warn, GOLD, NAVY, RED, TEAL, TINT_BLUE, TINT_GOLD, BLUE,
    method, bullets,
)


def story():
    st = []

    # ------------------------------------------------------------------
    st.append(SectionBanner("PHẦN MỞ ĐẦU", "Hướng dẫn sử dụng tài liệu", NAVY))
    st.append(spacing(0.35))

    st.append(P(
        "Tài liệu này được biên soạn để giúp các em học sinh lớp 10 <b>hệ thống hoá toàn bộ "
        "kiến thức</b> của nửa đầu học kì I theo bộ sách <i>Kết nối tri thức với cuộc sống</i>, "
        "đồng thời <b>luyện tập đúng cấu trúc</b> của bài kiểm tra giữa học kì I năm học 2026 – 2027. "
        "Nội dung bám sát ma trận và bảng đặc tả đề kiểm tra do Tổ Toán – Tin xây dựng: "
        "4 chương (mệnh đề – tập hợp; bất phương trình bậc nhất hai ẩn; hệ thức lượng trong tam giác; "
        "khái niệm vectơ) với 24 câu/ý trắc nghiệm và 3 câu tự luận trong 90 phút."))

    st.append(note([
        P(
            "<b>Về nguồn gốc đề bài.</b> Tệp gốc <i>“MA TRẬN TOÁN 10 – GIỮA KÌ I.docx”</i> chỉ gồm "
            "<b>ma trận</b> và <b>bảng đặc tả</b> (mô tả mức độ, số câu, dạng câu cho từng đơn vị kiến thức), "
            "không kèm nội dung câu hỏi cụ thể. Vì vậy tài liệu này: (1) tái hiện <b>nguyên văn</b> ma trận "
            "và đặc tả ở Phần E; (2) biên soạn <b>đề luyện tập số 1</b> bám chính xác từng ô của ma trận "
            "(đúng số câu, đúng mức độ Nhận biết – Thông hiểu – Vận dụng – Vận dụng cao, đúng dạng câu mà "
            "đặc tả yêu cầu); (3) cung cấp lời giải chi tiết cho <b>100% câu hỏi</b>. Khi thầy cô công bố đề "
            "chính thức, các em dùng cấu trúc và phương pháp trong tài liệu để xử lý là có thể bao quát "
            "toàn bộ các dạng sẽ ra.", "small")],
        color=BLUE, bg=TINT_BLUE, title="Lưu ý quan trọng", icon="i"))

    st.append(spacing(0.25))
    st.append(P("Bốn bước sử dụng tài liệu hiệu quả", "h3"))
    st.extend(bullets([
        "<b>Bước 1 – Đọc lý thuyết (Phần A).</b> Đọc kĩ, tự viết lại công thức vào vở mà không nhìn tài liệu. "
        "Mỗi hộp <font color='#0E6E6B'><b>★ Ghi nhớ</b></font> là nội dung <i>buộc phải thuộc</i>.",
        "<b>Bước 2 – Học phương pháp (Phần B).</b> Với mỗi dạng toán: đọc phương pháp, che lời giải của ví dụ mẫu, "
        "tự làm trước rồi mới đối chiếu.",
        "<b>Bước 3 – Làm đề luyện (Phần C).</b> Bấm đồng hồ đúng 90 phút, không xem đáp án. Ghi lại các câu "
        "chưa chắc chắn để soát lại.",
        "<b>Bước 4 – Chữa lỗi (Phần D).</b> Đối chiếu lời giải, đánh dấu lỗi vào sổ tay và làm lại các câu sai "
        "sau 2 ngày.",
    ], bullet="▸"))

    st.append(spacing(0.1))
    st.append(P("Chú thích các biểu tượng trong tài liệu", "h3"))
    legend = data_table(
        ["Biểu tượng", "Ý nghĩa", "Cách dùng"],
        [
            ["<font color='#0E6E6B'><b>★ Ghi nhớ</b></font>",
             "Định nghĩa, định lí, công thức bắt buộc thuộc lòng",
             "Học thuộc nguyên văn, viết lại được khi không nhìn sách"],
            ["<font color='#5B3E90'><b>◆ Phương pháp giải</b></font>",
             "Quy trình từng bước để xử lý một dạng toán",
             "Áp dụng theo đúng thứ tự, không bỏ bước kiểm tra"],
            ["<font color='#9C6500'><b>✦ Mẹo / Kinh nghiệm</b></font>",
             "Thủ thuật làm nhanh, cách loại trừ đáp án",
             "Dùng khi làm trắc nghiệm để tiết kiệm thời gian"],
            ["<font color='#A33E30'><b>⚠ Lỗi thường gặp</b></font>",
             "Sai sót phổ biến trong bài kiểm tra",
             "Đọc trước khi làm bài để tránh mất điểm oan"],
        ],
        widths=[4.3 * cm, 5.9 * cm, 7.1 * cm],
        align_center_cols=[0],
    )
    st.append(legend)

    # ------------------------------------------------------------------
    st.append(CondPageBreak(10.2 * cm))
    st.append(P("Cấu trúc đề kiểm tra giữa học kì I", "h2"))
    st.append(P(
        "Đề gồm 4 phần, tổng 10,0 điểm, thời gian 90 phút. Phần trắc nghiệm chiếm 7,0 điểm "
        "(24 câu/ý), phần tự luận chiếm 3,0 điểm (3 câu)."))

    struct = data_table(
        ["Phần", "Dạng câu hỏi", "Số câu", "Điểm / câu", "Tổng điểm", "Ghi chú"],
        [
            ["I", "Trắc nghiệm nhiều phương án lựa chọn", "12", "0,25", "3,0",
             "Chọn 1 trong 4 phương án A, B, C, D"],
            ["II", "Trắc nghiệm đúng – sai", "2 câu<br/>(8 ý)", "Theo số ý đúng", "2,0",
             "Mỗi câu 4 ý; đúng 1 ý 0,1 – 2 ý 0,25 – 3 ý 0,5 – 4 ý 1,0 điểm"],
            ["III", "Trắc nghiệm trả lời ngắn", "4", "0,5", "2,0", "Chỉ ghi đáp số vào ô trả lời"],
            ["IV", "Tự luận", "3", "1,0", "3,0",
             "Trình bày lời giải: tập hợp; hệ thức lượng thực tế; tối ưu hoá"],
            ["", "<b>Tổng cộng</b>", "<b>21 câu (24 ý)</b>", "", "<b>10,0</b>", "<b>90 phút</b>"],
        ],
        widths=[1.2 * cm, 5.4 * cm, 2.1 * cm, 2.2 * cm, 1.9 * cm, 4.5 * cm],
        align_center_cols=[0, 2, 3, 4],
    )
    st.append(struct)

    st.append(spacing(0.2))
    st.append(P("Phân bố nội dung và điểm số theo chương", "h3"))
    st.append(P(
        "Bảng dưới đây được tổng hợp trực tiếp từ ma trận đề. Các em dùng bảng này để quyết định "
        "phân bổ thời gian ôn tập: chương nào nhiều điểm thì ôn kĩ hơn."))

    dist = data_table(
        ["Chương", "Nội dung", "Số câu TN", "Điểm TN", "Số câu TL", "Điểm TL", "Tổng điểm", "Tỉ lệ"],
        [
            ["1", "Mệnh đề. Tập hợp", "10", "3,0", "1", "1,0", "4,0", "40%"],
            ["2", "Bất phương trình, hệ bất phương trình bậc nhất hai ẩn", "6", "1,5", "1", "1,0", "2,5", "25%"],
            ["3", "Hệ thức lượng trong tam giác", "6", "2,0", "1", "1,0", "3,0", "30%"],
            ["4", "Vectơ (khái niệm vectơ)", "2", "0,5", "0", "0", "0,5", "5%"],
            ["", "<b>Cộng</b>", "<b>24</b>", "<b>7,0</b>", "<b>3</b>", "<b>3,0</b>", "<b>10,0</b>", "<b>100%</b>"],
        ],
        widths=[1.3 * cm, 6.3 * cm, 1.9 * cm, 1.7 * cm, 1.8 * cm, 1.6 * cm, 1.8 * cm, 1.4 * cm],
        align_center_cols=[0, 2, 3, 4, 5, 6, 7],
    )
    st.append(dist)

    st.append(spacing(0.25))
    st.append(P("Ma trận mức độ nhận thức", "h3"))
    st.append(P(
        "Đề được thiết kế theo 4 mức độ. Lưu ý: <b>không có câu Nhận biết nào ở phần tự luận</b>, và "
        "<b>chỉ có duy nhất 1 câu Vận dụng cao</b> (câu 3 tự luận) – đây là câu phân loại học sinh."))

    level = data_table(
        ["Mức độ", "Nhận biết", "Thông hiểu", "Vận dụng", "Vận dụng cao", "Tổng"],
        [
            ["Trắc nghiệm chọn phương án", "9", "3", "0", "0", "12"],
            ["Trắc nghiệm đúng – sai (số ý)", "2", "4", "2", "0", "8"],
            ["Trắc nghiệm trả lời ngắn", "0", "2", "2", "0", "4"],
            ["Tự luận", "0", "1", "1", "1", "3"],
            ["<b>Tổng điểm</b>", "<b>~3,5</b>", "<b>~3,5</b>", "<b>~2,0</b>", "<b>1,0</b>", "<b>10,0</b>"],
        ],
        widths=[5.6 * cm, 2.5 * cm, 2.5 * cm, 2.5 * cm, 2.6 * cm, 1.6 * cm],
        align_center_cols=[1, 2, 3, 4, 5],
    )
    st.append(level)

    st.append(spacing(0.2))
    st.append(tip([
        P("Khoảng 70% số điểm (≈ 7,0 điểm) nằm ở mức Nhận biết – Thông hiểu. Nghĩa là "
          "<b>chỉ cần nắm chắc định nghĩa, công thức và kĩ năng cơ bản là đã có thể đạt điểm khá</b>. "
          "Đừng dành quá nhiều thời gian cho câu Vận dụng cao khi còn câu dễ chưa làm xong.")]))

    # ------------------------------------------------------------------
    st.append(CondPageBreak(10.2 * cm))
    st.append(P("Chiến lược phân bổ 90 phút làm bài", "h2"))
    st.append(P(
        "Một lỗi rất phổ biến là làm bài theo thứ tự và “sa lầy” ở một câu khó. Hãy chia thời gian "
        "theo bảng dưới đây và bám sát đồng hồ."))

    time_tbl = data_table(
        ["Giai đoạn", "Thời gian", "Nội dung", "Mục tiêu"],
        [
            ["1", "0 – 5 phút", "Đọc lướt toàn đề, ghi chú câu dễ / câu khó", "Nắm “bản đồ” đề, tránh bỏ sót trang"],
            ["2", "5 – 45 phút", "Làm 12 câu trắc nghiệm chọn phương án", "Tối đa 3 phút/câu; câu nào quá 4 phút thì bỏ lại"],
            ["3", "45 – 60 phút", "Làm 2 câu đúng – sai (8 ý)", "Đọc kĩ từng ý; ghi rõ Đ/S, không bỏ trống ý nào"],
            ["4", "60 – 70 phút", "Làm 4 câu trả lời ngắn", "Chỉ ghi đáp số, kiểm tra lại đơn vị và dấu"],
            ["5", "70 – 88 phút", "Làm 3 câu tự luận", "Trình bày rõ bước; câu tập hợp và hệ thức lượng ưu tiên làm trước"],
            ["6", "88 – 90 phút", "Rà soát", "Kiểm tra phiếu trả lời, các ý bỏ trống, đơn vị đo"],
        ],
        widths=[1.5 * cm, 2.6 * cm, 6.6 * cm, 6.6 * cm],
        align_center_cols=[0, 1],
    )
    st.append(time_tbl)

    st.append(spacing(0.3))
    st.append(P("Lộ trình ôn tập 7 ngày", "h2"))
    st.append(P(
        "Nếu các em bắt đầu ôn muộn, hãy theo lộ trình cấp tốc dưới đây. Nếu còn nhiều thời gian, "
        "mỗi ngày có thể giãn ra gấp đôi."))

    roadmap = data_table(
        ["Ngày", "Nội dung trọng tâm", "Việc cần làm", "Mục tiêu kiểm tra"],
        [
            ["1", "Mệnh đề (1.1)", "Học Phần A.1.1 + Dạng 1, 2, 3",
             "Viết được phủ định của mệnh đề ∀, ∃"],
            ["2", "Tập hợp và các phép toán (1.2, 1.3)", "Học Phần A.1.2 – 1.3 + Dạng 4 → 8",
             "Tìm giao, hợp, hiệu của hai khoảng; đếm số tập con"],
            ["3", "Bất phương trình bậc nhất hai ẩn (2.1)", "Học Phần A.2.1 + Dạng 9, 10",
             "Biểu diễn đúng miền nghiệm (nét liền/nét đứt, kể bờ hay không)"],
            ["4", "Hệ bất phương trình – bài toán tối ưu (2.2)", "Học Phần A.2.2 + Dạng 11, 12",
             "Lập được hệ bất phương trình từ đề bài thực tế"],
            ["5", "Giá trị lượng giác (3.1)", "Học Phần A.3.1 + Dạng 13",
             "Thuộc bảng giá trị đặc biệt; tính GTLG khi biết một giá trị"],
            ["6", "Hệ thức lượng trong tam giác (3.2)", "Học Phần A.3.2 + Dạng 14 → 16",
             "Giải tam giác; tính khoảng cách, chiều cao thực tế"],
            ["7", "Vectơ (4.1) + Làm đề", "Học Phần A.4.1 + Dạng 17, sau đó làm Phần C trong 90 phút",
             "Tự chấm điểm, chữa lỗi bằng Phần D"],
        ],
        widths=[1.2 * cm, 4.4 * cm, 6.4 * cm, 5.3 * cm],
        align_center_cols=[0],
    )
    st.append(roadmap)

    st.append(spacing(0.25))
    st.append(warn([
        P("Ba lỗi khiến học sinh mất điểm nhiều nhất trong bài kiểm tra này:", "body"),
        P("(1) Nhầm <b>ngoặc tròn</b> và <b>ngoặc vuông</b> khi tìm giao/hợp các khoảng (mất 0,5 – 1,0 điểm).", "small"),
        P("(2) Quên <b>đổi dấu cos khi góc tù</b> (90° < α < 180°) – câu hỏi này gần như chắc chắn xuất hiện.", "small"),
        P("(3) Khi biểu diễn miền nghiệm, vẽ <b>nét liền</b> cho bất phương trình <b>không có dấu bằng</b> (<, >).", "small"),
    ]))

    return st
