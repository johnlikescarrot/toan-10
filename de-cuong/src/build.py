#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ghép các phần nội dung rồi dựng PDF đề cương."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PARTS = ["01_mo_dau.md", "02_kien_thuc.md", "03_de_thi.md", "04_dap_an.md", "05_tu_luyen.md"]


def main():
    out_pdf = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "DE-CUONG-ON-TAP-TOAN-10-GK1.pdf")
    chunks = []
    for p in PARTS:
        with open(os.path.join(HERE, "parts", p), encoding="utf-8") as f:
            chunks.append(f.read().rstrip() + "\n")
    merged = "\n".join(chunks)
    merged_path = os.path.join(HERE, "content.md")
    with open(merged_path, "w", encoding="utf-8") as f:
        f.write(merged)
    import md2pdf
    md2pdf.build(merged_path, out_pdf)
    print("PDF:", os.path.abspath(out_pdf))


if __name__ == "__main__":
    main()
