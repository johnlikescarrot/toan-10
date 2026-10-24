# -*- coding: utf-8 -*-
"""Dựng đề cương PDF hoàn chỉnh."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import engine
import make_figs
import content1
import content2
import content3
import content4

OUT = os.path.join(os.path.dirname(HERE), "DE-CUONG-ON-TAP-TOAN-10-GIUA-KI-1.pdf")

blocks = (content1.FRONT + content1.PART0 + content1.PART1
          + content1.PART1_EXTRA
          + content2.PART2 + content2.PART2_EXTRA
          + content2.PART3 + content2.PART3_EXTRA
          + content3.PART4 + content3.PART4_EXTRA + content3.PART4_SUMMARY
          + content3.EXAM
          + content4.PART6 + content4.PART7)

if __name__ == "__main__":
    make_figs.ven()
    make_figs.mien_nghiem()
    make_figs.truc_so()
    engine.build(blocks, OUT, "Đề cương ôn tập giữa học kì I – Toán 10 (KNTT)")
    print("Đã tạo:", OUT, os.path.getsize(OUT), "bytes")
