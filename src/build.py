# -*- coding: utf-8 -*-
"""Dựng PDF "Đề cương ôn tập Giữa kì I – Toán 10".

Chạy:  /tmp/venv/bin/python src/build.py [--out PATH]

Yêu cầu: reportlab (pip install reportlab). Font DejaVu nằm trong assets/fonts/
để không phụ thuộc font hệ thống.
"""
from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.platypus import PageBreak, PageTemplate

import pdf_kit as K
import content_front as F
import content_b1 as B1
import content_b2 as B2
import content_b3 as B3
import content_cd as CD
import content_e as E

DEFAULT_OUT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "de-cuong-on-tap-giua-ki-1-toan-10.pdf",
)


def build_story() -> list:
    story: list = []
    story += F.front_matter()
    story += B1.part_b1()
    story += B1.exercises_b1()
    story += B2.part_b2()
    story += B2.exercises_b2()
    story += B3.part_b3()
    story += B3.exercises_b3()
    story += B3.part_b4()
    story += B3.exercises_b4()
    story += B3.part_b5()
    story += B3.part_b5_tail()
    story += [PageBreak()]
    story += CD.part_c()
    story += [PageBreak()]
    story += CD.part_d()
    story += [PageBreak()]
    story += E.part_e()
    story += E.part_f()
    return story


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DEFAULT_OUT)
    args = ap.parse_args()

    out = os.path.abspath(args.out)
    # Lượt 1: đếm số trang (mục lục + tổng số trang ở chân trang cần số này).
    tmp = out + ".tmp"
    doc = K.build_doc(tmp)
    doc.pageTemplates[0].onPage = F.draw_cover
    doc.multiBuild(build_story())
    total = doc.page

    # Lượt 2: dựng bản chính thức với tổng số trang đã biết.
    doc = K.build_doc(out)
    doc._total_pages = total
    doc.pageTemplates[0].onPage = F.draw_cover
    doc.multiBuild(build_story())
    if os.path.exists(tmp):
        os.remove(tmp)
    print(f"wrote {out} ({doc.page} pages)")


if __name__ == "__main__":
    main()
