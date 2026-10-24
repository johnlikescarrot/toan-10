# -*- coding: utf-8 -*-
"""Dựng file PDF đề cương: python build.py [đường_dẫn_ra]"""
import os
import sys

from kit import Doc, mm
from reportlab.platypus import CondPageBreak, PageBreak, NextPageTemplate, Spacer

import c_front
import c_theory1
import c_theory2
import c_exam
import c_solution
import c_back

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    ROOT, "De cuong on tap giua hoc ki I - Toan 10 KNTT.pdf")


def story():
    s = []
    # ------------------------------------------------ bìa
    s += c_front.cover()
    s.append(NextPageTemplate("Body"))
    s.append(PageBreak())
    # ------------------------------------------------ mở đầu + mục lục
    s += c_front.preface()
    s.append(PageBreak())
    s += c_front.toc_page()
    s.append(PageBreak())
    # ------------------------------------------------ phần I
    s += c_theory1.chapter1()
    s.append(CondPageBreak(105 * mm))
    s += c_theory1.chapter2()
    s.append(CondPageBreak(105 * mm))
    s += c_theory2.chapter3()
    s.append(CondPageBreak(105 * mm))
    s += c_theory2.chapter4()
    s.append(PageBreak())
    # ------------------------------------------------ phần II
    s += c_exam.exam()
    s.append(PageBreak())
    # ------------------------------------------------ phần III
    s += c_solution.solutions()
    s.append(PageBreak())
    # ------------------------------------------------ phần IV
    s += c_back.matrix()
    return s


def main():
    doc = Doc(OUT)
    doc.multiBuild(story())
    print("Đã tạo:", OUT)


if __name__ == "__main__":
    main()
