# -*- coding: utf-8 -*-
"""Ghép và xuất PDF: Đề cương ôn tập Giữa học kì I – Toán 10 (KNTT)."""
import os
import sys

from reportlab.lib.units import mm
from reportlab.platypus import PageBreak, Spacer
from reportlab.platypus.tableofcontents import TableOfContents

import design as D
import sec_front
import sec_ch1
import sec_ch2
import sec_ch3
import sec_ch4
import sec_exam
import sec_solutions
import sec_appendix

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(os.path.dirname(HERE), 'output')
OUT = os.path.join(OUT_DIR, 'De-cuong-on-tap-Toan-10-GK1-KNTT.pdf')


def build():
    os.makedirs(OUT_DIR, exist_ok=True)

    doc = D.Doc(
        OUT,
        title='Đề cương ôn tập Giữa học kì I – Toán 10 (Kết nối tri thức)',
        author='Tổng hợp và biên soạn theo ma trận đề của Tổ trường THPT Hà Huy Tập',
        subject='Đề cương ôn tập + đề kiểm tra + đáp án chi tiết, năm học 2026–2027',
        keywords='Toán 10, giữa kì I, Kết nối tri thức, đề cương, đáp án',
        creator='Arena Agent (ReportLab)',
    )

    toc = TableOfContents()
    toc.levelStyles = D.toc_styles()
    toc.dotsMinLevel = 0

    story = []
    # --- bìa (trang 1, template Cover)
    story += sec_front.cover()
    # --- mục lục
    story += sec_front.toc_page(toc)
    # --- phần mở đầu
    story += D.flatten(sec_front.how_to_use())
    story += [PageBreak()]
    story += D.flatten(sec_front.exam_structure())

    # --- Phần 1: lý thuyết
    story += [PageBreak()]
    story += D.flatten([D.H1('I', 'Hệ thống kiến thức trọng tâm', 'Phần 1  ·  Bốn chương')])
    story += D.flatten([
        D.P('Phần này đi theo đúng thứ tự chương của sách Kết nối tri thức và đúng phạm vi '
            'kiểm tra ghi trong ma trận. Mỗi chương gồm bốn khối: <b>kiến thức cần thuộc</b>, '
            '<b>công thức</b>, <b>các dạng toán thường gặp</b> (kèm ví dụ mẫu có lời giải) và '
            '<b>lỗi hay mắc</b>. Bạn có thể đọc liền mạch hoặc tra theo đơn vị kiến thức khi '
            'làm bài.', 'lead')])
    for mod, idx in ((sec_ch1, 1), (sec_ch2, 2), (sec_ch3, 3), (sec_ch4, 4)):
        if idx > 1:
            story += [PageBreak()]
        story += D.flatten(mod.chapter())

    # --- Phần 2: đề
    story += [PageBreak()]
    story += D.flatten(sec_exam.part())

    # --- Phần 3: đáp án
    story += [PageBreak()]
    story += D.flatten(sec_solutions.part())

    # --- Phần 4: tra cứu
    story += [PageBreak()]
    story += D.flatten(sec_appendix.appendix())

    doc.multiBuild(story)
    size = os.path.getsize(OUT)
    print(f'Đã tạo {OUT} ({size/1024:.1f} KB, {doc.page} trang)')
    return OUT


if __name__ == '__main__':
    build()
