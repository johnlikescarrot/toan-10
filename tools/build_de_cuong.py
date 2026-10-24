#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dựng ĐỀ CƯƠNG ÔN TẬP TOÁN 10 – GIỮA HỌC KỲ I (năm học 2026-2027) ra file PDF.

Cách dùng:
    python3 tools/build_de_cuong.py [đường_dẫn_pdf]

Yêu cầu: reportlab và bộ font DejaVu (Sans/Serif/Mono + bản Oblique/Italic).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (KeepTogether, NextPageTemplate, PageBreak, Paragraph,
                                Spacer, Table, TableStyle)

from dung_pdf import (Doc, Ctx, NEN_BANG, NEN_XANH, NumberedCanvas, XAM, XANH,
                      XANH_DAM, XANH_SANG, XANH_ONG, XANH_LA, DUONG, register_fonts,
                      build_styles)

from noi_dung_phan_a import phan_a
from noi_dung_phan_b import phan_b
from noi_dung_phan_cde import phan_c, phan_d, phan_e

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_OUT = os.path.join(ROOT, "DE CUONG ON TAP TOAN 10 - GIUA KY I 2026-2027.pdf")


# --------------------------------------------------------------------------
def trang_bia(ctx):
    # ---- băng tiêu đề trường ----
    bang = Table(
        [[Paragraph("TRƯỜNG THPT HÀ HUY TẬP", ctx.st["cover_k"].clone("ck1")),
          Paragraph("TỔ TOÁN – TIN", ctx.st["cover_k"].clone("ck2"))]],
        colWidths=[95 * mm, 55 * mm],
    )
    bang.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), XANH_DAM),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (0, 0), (0, 0), "CENTER"),
        ("ALIGN", (1, 0), (1, 0), "CENTER"),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    ctx.add(bang)
    ctx.sp(30)

    ctx.add(Paragraph("ĐỀ CƯƠNG ÔN TẬP", ctx.st["cover_t"].clone("ct1")))
    ctx.add(Paragraph("TOÁN 10", ctx.st["cover_t"].clone("ct2")))
    ctx.sp(6)
    ctx.add(Paragraph("GIỮA HỌC KỲ I &nbsp;·&nbsp; NĂM HỌC 2026-2027",
                      ctx.st["cover_s"].clone("cs1")))
    ctx.add(Paragraph("Chương trình “Kết nối tri thức”", ctx.st["cover_s"].clone("cs2")))
    ctx.sp(18)

    rows = [
        ["Môn học", "Toán"],
        ["Lớp", "10"],
        ["Thời gian làm bài", "90 phút"],
        ["Tổng điểm – số câu", "10,0 điểm – 21 câu"],
        ["Cấu trúc đề",
         "Phần I: 12 câu trắc nghiệm chọn phương án (3,0 đ)<br/>"
         "Phần II: 2 câu trắc nghiệm đúng sai (2,0 đ)<br/>"
         "Phần III: 4 câu trắc nghiệm trả lời ngắn (2,0 đ)<br/>"
         "Phần IV: 3 câu tự luận (3,0 đ)"],
        ["Nội dung ôn tập",
         "Chương 1. Mệnh đề và tập hợp (Bài 1 – Bài 2)<br/>"
         "Chương 2. Bất phương trình và hệ bất phương trình bậc nhất hai ẩn (Bài 3 – Bài 4)<br/>"
         "Chương 3. Hệ thức lượng trong tam giác (Bài 5 – Bài 6)<br/>"
         "Chương 4. Vectơ (Bài 7)"],
        ["Căn cứ xây dựng",
         "Ma trận và bảng đặc tả đề kiểm tra giữa kỳ I năm học 2026-2027<br/>"
         "(tài liệu gốc: “MA TRẬN TOÁN 10 - GIỮA KÌ I.docx”)"],
    ]
    data = []
    sty_k = ctx.st["cover_v"].clone("cvk")
    sty_k.textColor = colors.white
    sty_k.fontName = "DJV-Bold"
    for k, v in rows:
        data.append([
            Paragraph(k, sty_k),
            Paragraph(v, ctx.st["cover_v"]),
        ])
    t = Table(data, colWidths=[42 * mm, 108 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), XANH),
        ("TEXTCOLOR", (0, 0), (0, -1), colors.white),
        ("BOX", (0, 0), (-1, -1), 0.9, XANH_DAM),
        ("INNERGRID", (0, 0), (-1, -1), 0.4, colors.white),
        ("BACKGROUND", (1, 0), (1, -1), NEN_XANH),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    ctx.add(t)
    ctx.sp(20)
    ctx.add(Paragraph(
        "Tài liệu gồm 5 phần: A – Thông tin chung và cấu trúc đề; B – Kiến thức nền tảng và dạng bài "
        "theo từng chương; C – Đề kiểm tra đầy đủ 21 câu; D – Đáp án chi tiết; E – Phụ lục "
        "(bảng công thức, bảng đáp án nhanh, phiếu tự đánh giá).",
        ctx.st["small"].clone("cv")))
    ctx.page_break()


def muc_luc(ctx):
    ctx.h1("MỤC LỤC")
    from reportlab.platypus.tableofcontents import TableOfContents
    toc = TableOfContents()
    toc.levelStyles = [ctx.st["toc1"], ctx.st["toc2"], ctx.st["toc3"]]
    toc.dotsMinLevel = 0
    ctx.add(toc)
    ctx.page_break()


# --------------------------------------------------------------------------
def _dung(out_path, tong_so_trang):
    """Dựng một lần, biết trước tổng số trang (None ở lượt đầu)."""
    doc = Doc(out_path,
              title="Đề cương ôn tập Toán 10 – Giữa học kỳ I 2026-2027",
              author="Tổ Toán-Tin – Trường THPT Hà Huy Tập")
    doc.total_pages = tong_so_trang
    ctx = Ctx(doc)

    trang_bia(ctx)
    muc_luc(ctx)
    phan_a(ctx)
    ctx.page_break()
    phan_b(ctx)
    ctx.page_break()
    phan_c(ctx)
    ctx.page_break()
    phan_d(ctx)
    ctx.page_break()
    phan_e(ctx)

    doc.multiBuild(ctx.story)
    return doc.page


def main(out_path=None):
    register_fonts()
    out_path = out_path or DEFAULT_OUT

    tong = None
    for _ in range(5):
        n = _dung(out_path, tong)
        if n == tong:
            break
        tong = n
    print("Đã tạo: %s  (%d trang)" % (out_path, tong))
    return out_path


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
