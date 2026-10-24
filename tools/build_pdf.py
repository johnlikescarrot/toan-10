# -*- coding: utf-8 -*-
"""Dựng đề cương ôn tập Giữa học kì I – Toán 10 (bộ Kết nối tri thức) thành PDF.

Cách dùng:
    python tools/build_pdf.py [đường_dẫn_đầu_ra.pdf]
Yêu cầu: reportlab (xem requirements.txt).
"""
from __future__ import annotations

import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import (
    BaseDocTemplate, Frame, NextPageTemplate, PageBreak, PageTemplate,
    Paragraph, Spacer, Table, TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

sys.path.insert(0, str(Path(__file__).resolve().parent))

import pdfkit
from pdfkit import (
    CONTENT_W, FONT, FONT_B, FONT_I, GOLD, GREY, INK, LINE, MARGIN_B,
    MARGIN_L, MARGIN_R, MARGIN_T, NAVY, PAGE_H, PAGE_W, P, S, STY, TEAL, TINT_BLUE,
    build_styles, register_fonts,
)

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "DE_CUONG_ON_TAP_TOAN_10_GK1.pdf"

TITLE = "ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I"
SUBTITLE = "MÔN TOÁN – LỚP 10"
TAGLINE = "Bộ sách Kết nối tri thức với cuộc sống"


from pdfkit import Heading


class GuideDoc(BaseDocTemplate):
    def __init__(self, filename, **kw):
        super().__init__(filename, pagesize=(PAGE_W, PAGE_H),
                         leftMargin=MARGIN_L, rightMargin=MARGIN_R,
                         topMargin=MARGIN_T, bottomMargin=MARGIN_B,
                         title="Đề cương ôn tập Giữa học kì I – Toán 10 (KNTT)",
                         author="Tổ Toán – Tin, Trường THPT Hà Huy Tập",
                         subject="Đề cương ôn tập + đề luyện Giữa học kì I môn Toán lớp 10",
                         creator="ReportLab", **kw)
        body_frame = Frame(MARGIN_L, MARGIN_B, CONTENT_W,
                           PAGE_H - MARGIN_T - MARGIN_B, id="body",
                           leftPadding=0, rightPadding=0,
                           topPadding=0, bottomPadding=0)
        cover_frame = Frame(0, 0, PAGE_W, PAGE_H, id="cover",
                            leftPadding=0, rightPadding=0,
                            topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[cover_frame], onPage=draw_cover),
            PageTemplate(id="body", frames=[body_frame], onPage=draw_body_chrome),
        ])

    def afterFlowable(self, flowable):
        if getattr(flowable, "toc_text", None):
            key = f"h{self.page}-{abs(hash(flowable.toc_text)) % 100000}"
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(flowable.toc_text, key,
                                      level=flowable.toc_level, closed=False)
            self.notify("TOCEntry", (flowable.toc_level, flowable.toc_text,
                                     self.page, key))


# --------------------------------------------------------------------------
# Trang bìa
# --------------------------------------------------------------------------
def draw_cover(canv, doc):
    canv.saveState()
    w, h = PAGE_W, PAGE_H
    canv.setFillColor(colors.HexColor("#FBFCFD"))
    canv.rect(0, 0, w, h, stroke=0, fill=1)

    # khối màu trên
    top_h = 15.0 * cm
    canv.setFillColor(NAVY)
    canv.rect(0, h - top_h, w, top_h, stroke=0, fill=1)
    canv.setFillColor(TEAL)
    canv.rect(0, h - top_h - 0.28 * cm, w, 0.28 * cm, stroke=0, fill=1)
    # hoạ tiết
    canv.setFillColor(colors.Color(1, 1, 1, alpha=0.06))
    canv.circle(w - 1.2 * cm, h - 2.0 * cm, 5.2 * cm, stroke=0, fill=1)
    canv.setFillColor(colors.Color(1, 1, 1, alpha=0.05))
    canv.circle(0.4 * cm, h - 13.6 * cm, 4.0 * cm, stroke=0, fill=1)

    # dòng trường
    canv.setFillColor(colors.Color(1, 1, 1, alpha=0.9))
    canv.setFont(FONT_B, 10.5)
    canv.drawCentredString(w / 2, h - 2.3 * cm, "TRƯỜNG THPT HÀ HUY TẬP")
    canv.setFont(FONT, 9.5)
    canv.setFillColor(colors.Color(1, 1, 1, alpha=0.72))
    canv.drawCentredString(w / 2, h - 3.05 * cm, "TỔ TOÁN – TIN")

    canv.setStrokeColor(colors.Color(1, 1, 1, alpha=0.35))
    canv.setLineWidth(0.8)
    canv.line(w / 2 - 2.2 * cm, h - 3.6 * cm, w / 2 + 2.2 * cm, h - 3.6 * cm)

    # badge năm học
    bw, bh = 6.0 * cm, 0.86 * cm
    canv.setFillColor(colors.HexColor("#E8B04B"))
    canv.roundRect(w / 2 - bw / 2, h - 5.05 * cm, bw, bh, 0.43 * cm, stroke=0, fill=1)
    canv.setFillColor(colors.HexColor("#3B2A00"))
    canv.setFont(FONT_B, 11)
    canv.drawCentredString(w / 2, h - 4.79 * cm, "NĂM HỌC 2026 – 2027")

    # tiêu đề
    canv.setFillColor(colors.white)
    canv.setFont(FONT_B, 25)
    canv.drawCentredString(w / 2, h - 6.9 * cm, "ĐỀ CƯƠNG ÔN TẬP")
    canv.setFont(FONT_B, 22)
    canv.drawCentredString(w / 2, h - 8.2 * cm, "GIỮA HỌC KÌ I")
    canv.setFillColor(colors.HexColor("#E8B04B"))
    canv.setFont(FONT_B, 17)
    canv.drawCentredString(w / 2, h - 9.5 * cm, "MÔN TOÁN – LỚP 10")
    canv.setFillColor(colors.Color(1, 1, 1, alpha=0.82))
    canv.setFont(FONT_I, 11)
    canv.drawCentredString(w / 2, h - 10.5 * cm, TAGLINE)
    canv.setFont(FONT, 9.6)
    canv.drawCentredString(w / 2, h - 11.4 * cm,
                           "Lý thuyết trọng tâm  •  Phương pháp giải  •  Đề luyện + đáp án chi tiết")

    # ô thông tin 4 chương
    box_y = h - top_h - 0.9 * cm
    bx, bw2 = 1.9 * cm, w - 3.8 * cm
    bh2 = 4.9 * cm
    canv.setFillColor(colors.white)
    canv.setStrokeColor(LINE)
    canv.setLineWidth(0.8)
    canv.roundRect(bx, box_y - bh2, bw2, bh2, 0.25 * cm, stroke=1, fill=1)

    canv.setFillColor(NAVY)
    canv.setFont(FONT_B, 10.5)
    canv.drawString(bx + 0.7 * cm, box_y - 0.85 * cm, "NỘI DUNG ÔN TẬP")

    items = [
        "Chương 1. Mệnh đề và tập hợp",
        "Chương 2. Bất phương trình và hệ bất phương trình bậc nhất hai ẩn",
        "Chương 3. Hệ thức lượng trong tam giác",
        "Chương 4. Vectơ (khái niệm vectơ)",
    ]
    yy = box_y - 1.6 * cm
    for it in items:
        canv.setFillColor(TEAL)
        canv.circle(bx + 0.85 * cm, yy + 0.1 * cm, 0.07 * cm, stroke=0, fill=1)
        canv.setFillColor(INK)
        canv.setFont(FONT, 9.8)
        canv.drawString(bx + 1.15 * cm, yy, it)
        yy -= 0.83 * cm

    # hộp cấu trúc đề
    canv.setFillColor(colors.HexColor("#F4F7FA"))
    canv.roundRect(bx, box_y - bh2 - 2.35 * cm, bw2, 1.95 * cm, 0.25 * cm, stroke=0, fill=1)
    canv.setFillColor(NAVY)
    canv.setFont(FONT_B, 10.2)
    canv.drawString(bx + 0.7 * cm, box_y - bh2 - 0.85 * cm,
                    "CẤU TRÚC ĐỀ KIỂM TRA")
    canv.setFont(FONT, 9.4)
    canv.setFillColor(colors.HexColor("#33414F"))
    canv.drawString(bx + 0.7 * cm, box_y - bh2 - 1.4 * cm,
                    "12 câu trắc nghiệm (3,0 đ)  •  2 câu đúng – sai (2,0 đ)  •  4 câu trả lời ngắn (2,0 đ)")
    canv.drawString(bx + 0.7 * cm, box_y - bh2 - 1.85 * cm,
                    "3 câu tự luận (3,0 đ)  •  Thời gian làm bài: 90 phút")

    # chân trang
    canv.setFillColor(colors.HexColor("#EEF2F6"))
    canv.rect(0, 0, w, 2.5 * cm, stroke=0, fill=1)
    canv.setFillColor(GREY)
    canv.setFont(FONT_I, 9.2)
    canv.drawCentredString(w / 2, 1.45 * cm,
                           "Tài liệu lưu hành nội bộ – dùng cho học sinh lớp 10 ôn thi Giữa học kì I")
    canv.setFont(FONT, 8.6)
    canv.drawCentredString(w / 2, 0.95 * cm,
                           "Biên soạn dựa trên ma trận và bảng đặc tả đề kiểm tra của Tổ Toán – Tin")
    canv.restoreState()


# --------------------------------------------------------------------------
# Header / footer cho các trang nội dung
# --------------------------------------------------------------------------
def draw_body_chrome(canv, doc):
    canv.saveState()
    w, h = PAGE_W, PAGE_H
    # header
    canv.setFont(FONT_I, 7.9)
    canv.setFillColor(GREY)
    canv.drawString(MARGIN_L, h - 1.28 * cm, "Đề cương ôn tập Giữa học kì I – Toán 10")
    canv.drawRightString(w - MARGIN_R, h - 1.28 * cm, "Kết nối tri thức với cuộc sống")
    canv.setStrokeColor(LINE)
    canv.setLineWidth(0.6)
    canv.line(MARGIN_L, h - 1.45 * cm, w - MARGIN_R, h - 1.45 * cm)
    canv.setFillColor(TEAL)
    canv.rect(MARGIN_L, h - 1.62 * cm, 1.6 * cm, 0.075 * cm, stroke=0, fill=1)

    # footer
    canv.setStrokeColor(LINE)
    canv.line(MARGIN_L, 1.32 * cm, w - MARGIN_R, 1.32 * cm)
    canv.setFont(FONT, 8.2)
    canv.setFillColor(GREY)
    canv.drawString(MARGIN_L, 1.02 * cm, "Năm học 2026 – 2027")
    canv.setFont(FONT_B, 8.6)
    canv.setFillColor(NAVY)
    canv.drawCentredString(w / 2, 1.02 * cm, f"Trang {doc.page}")
    canv.setFont(FONT_I, 8.2)
    canv.setFillColor(GREY)
    canv.drawRightString(w - MARGIN_R, 1.02 * cm, "Tổ Toán – Tin • THPT Hà Huy Tập")
    canv.restoreState()


# --------------------------------------------------------------------------
# Các hàm tiện dụng cho nội dung
# --------------------------------------------------------------------------
def H1(text, toc=None):
    return Heading(text, S("h1"), level=0, toc_text=toc)


def H2(text, toc=None):
    return Heading(text, S("h2"), level=1, toc_text=toc)


def H3(text, toc=None):
    return Heading(text, S("h3"), level=2, toc_text=toc)


def bullets(items, style="bullet", bullet="•"):
    return [Paragraph(t, S[style], bulletText=bullet) for t in items]


def chapter(number, title, subtitle, color=NAVY):
    from pdfkit import ChapterBanner, spacing
    from reportlab.platypus import CondPageBreak
    return [CondPageBreak(11.5 * cm), spacing(0.32),
            ChapterBanner(number, title, subtitle, color), spacing(0.32)]


def build(out_path: Path = OUT) -> Path:
    register_fonts()
    STY.update(build_styles())

    import content_front, content_theory, content_methods, content_exam
    import content_answers, content_appendix

    story = []
    # ---- bìa ----
    story.append(Spacer(1, PAGE_H - MARGIN_T - MARGIN_B))
    story.append(NextPageTemplate("body"))
    story.append(PageBreak())

    # ---- mục lục ----
    story.append(Paragraph("MỤC LỤC", S("h2")))
    story.append(Paragraph(
        "Nhấn vào tiêu đề bất kỳ trong mục lục để chuyển nhanh tới mục tương ứng.",
        S("small")))
    story.append(Spacer(1, 0.18 * cm))
    toc = TableOfContents()
    toc.levelStyles = [S("toc1"), S("toc2"), S("toc3")]
    toc.dotsMinLevel = 0
    toc.tableStyle = TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0.3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0.3),
    ])
    story.append(toc)
    story.append(PageBreak())

    story += content_front.story()
    story += content_theory.story()
    story += content_methods.story()
    story += content_exam.story()
    story += content_answers.story()
    story += content_appendix.story()

    doc = GuideDoc(str(out_path))
    doc.multiBuild(story)
    return out_path


if __name__ == "__main__":
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else OUT
    p = build(out)
    print(f"Đã tạo: {p}  ({p.stat().st_size/1024:.0f} KB)")
