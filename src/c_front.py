# -*- coding: utf-8 -*-
"""Bìa, lời nói đầu và mục lục."""
from kit import *
from kit import _p


def cover():
    s = [Spacer(1, 92 * mm)]
    s.append(Paragraph("ĐỀ CƯƠNG ÔN TẬP", S["cover_s"]))
    s.append(Spacer(1, 3))
    s.append(Paragraph("GIỮA HỌC KÌ I", S["cover_t"]))
    s.append(Spacer(1, 2))
    s.append(Paragraph("MÔN TOÁN – LỚP 10", S["cover_s"]))
    s.append(Spacer(1, 6))
    s.append(Paragraph("Chương trình <b>Kết nối tri thức với cuộc sống</b>",
                       _p("cv", fontSize=11, leading=16, alignment=TA_CENTER, textColor=GREY)))
    s.append(Spacer(1, 12))

    rows = [
        ["Trường", "THPT Hà Huy Tập – Tổ Toán – Tin"],
        ["Môn học", "Toán, lớp 10"],
        ["Năm học", "2026 – 2027"],
        ["Hình thức kiểm tra", "Trắc nghiệm + Tự luận"],
        ["Thời gian làm bài", "90 phút"],
        ["Cấu trúc đề", "12 TN chọn đáp án • 2 TN đúng–sai • 4 TN trả lời ngắn • 3 tự luận"],
        ["Nội dung", "Chương I, II, III, IV – SGK Toán 10 (KNTT), đến hết Bài 7"],
    ]
    data = []
    for k, v in rows:
        data.append([Paragraph(inline("<b>%s</b>" % k),
                               _p("cvk", fontSize=8.6, leading=12.6, textColor=TEAL)),
                     Paragraph(inline(v),
                               _p("cvv", fontSize=8.8, leading=12.6, textColor=INK))])
    t = Table(data, colWidths=[38 * mm, None])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW", (0, 0), (-1, -2), 0.4, RULE),
        ("TOPPADDING", (0, 0), (-1, -1), 4.6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.6),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ]))
    s.append(t)
    s.append(Spacer(1, 10))
    s.append(Paragraph(
        inline("<i>Tài liệu gồm 4 phần: hệ thống kiến thức trọng tâm – đề thi tham khảo bám sát ma trận – "
               "đáp án và lời giải chi tiết – phân tích ma trận, đặc tả và kế hoạch ôn tập.</i>"),
        _p("cvnote", fontSize=8.8, leading=13, textColor=GREY, alignment=TA_CENTER)))
    return s


def preface():
    s = []
    s += h1(None, "MỞ ĐẦU: TÀI LIỆU NÀY ĐƯỢC XÂY DỰNG NHƯ THẾ NÀO?",
            "Bám sát ma trận – bảng đặc tả đề kiểm tra giữa học kì I của trường, đối chiếu với SGK Kết nối tri thức")

    s.append(P("Tài liệu được biên soạn trực tiếp từ văn bản **“MA TRẬN ĐỀ KIỂM TRA GIỮA KÌ I NĂM HỌC 2026–2027 – "
               "MÔN TOÁN, LỚP 10”** của Tổ Toán – Tin, Trường THPT Hà Huy Tập: mục tiêu, hình thức, ma trận và bảng "
               "đặc tả trong văn bản gốc được phân tích rồi chuyển hoá thành đề cương dùng để học và tự kiểm tra."))
    s.extend(box(["**Một lưu ý quan trọng về văn bản gốc.** Tệp “MA TRẬN TOÁN 10 – GIỮA KÌ I.docx” là **ma trận đề** "
                  "kèm **bảng đặc tả** và phần **mô tả 3 câu tự luận**; trong tệp **không có nội dung câu hỏi** "
                  "(đề gốc chưa được đính kèm). Vì vậy, để bảo đảm yêu cầu “có đầy đủ câu hỏi và đáp án”, tài liệu "
                  "này **biên soạn lại một đề tham khảo đủ 24 câu**, phân bố đúng theo từng đơn vị kiến thức, đúng "
                  "mức độ nhận thức và đúng số điểm trong ma trận – kèm **đáp án và lời giải chi tiết cho cả 24 câu** "
                  "ở Phần III. Nếu nhận được đề gốc, chỉ cần giữ nguyên Phần I (lí thuyết) và thay đề ở Phần II "
                  "bằng đề thật; cách giải trong Phần III vẫn dùng được vì bám đúng đặc tả.",
                  "**Nguồn lí thuyết:** SGK Toán 10 – bộ Kết nối tri thức với cuộc sống (Bài 1 → Bài 7 và các bài "
                  "liên quan). Số liệu trong các ví dụ được chọn để kết quả đẹp, kiểm tra được bằng tay."],
                 kind="box_warn", title="Về nguồn đề"))

    s.append(h3("Những gì có trong tài liệu"))
    rows = [["Phần", "Nội dung", "Dùng để"],
            ["I. Kiến thức trọng tâm", "4 chương: định nghĩa, công thức, phương pháp giải từng dạng, ví dụ mẫu có lời giải",
             "học – hiểu – nhớ"],
            ["II. Đề thi tham khảo", "Đủ 24 câu theo đúng cấu trúc và mức độ của ma trận (12 TN + 2 ĐS + 4 TLN + 3 TL)",
             "luyện tập có bấm giờ"],
            ["III. Đáp án & lời giải", "Giải chi tiết cả 24 câu, chỉ rõ bẫy của từng phương án nhiễu",
             "chữa bài, rút kinh nghiệm"],
            ["IV. Ma trận – đặc tả – kế hoạch", "Bảng ma trận, đặc tả tóm tắt, nhận xét, kế hoạch ôn 7 ngày, checklist",
             "định hướng ôn tập"]]
    s.append(data_table(rows, widths=[42 * mm, None, 34 * mm], align_center=False))

    s.append(h3("Ba nguyên tắc khi dùng đề cương"))
    s.extend(steps([
        "**Học theo chủ đề, không học theo trang.** Mỗi chương ở Phần I đi đúng thứ tự nhận thức: "
        "khái niệm → công thức → phương pháp → ví dụ. Đã chắc khái niệm thì đi thẳng vào dạng toán.",
        "**Làm đề trước, xem lời giải sau.** Tự làm Phần II trong 90 phút, ghi đáp án ra giấy rồi mới mở Phần III; "
        "phần đúng–sai phải ghi rõ từng ý Đ/S để đối chiếu.",
        "**Chữa lỗi mới là lúc học.** Với mỗi câu sai, ghi lại lỗi (quên công thức, tính toán, đọc sai đề, thiếu điều kiện) "
        "rồi đọc lại đúng mục lí thuyết tương ứng.",
    ]))

    return s


def toc_page():
    s = [Paragraph(inline("<b>MỤC LỤC</b>"),
                   _p("toch", fontName="Noto-Bold", fontSize=15, leading=20, textColor=NAVY,
                      spaceAfter=8))]
    s.append(toc())
    return s
