#!/usr/bin/env python3
"""Compile src/main.typ into DE_CUONG_ON_TAP_KTGK_I_TOAN_10_2026.pdf using Typst."""
import os
import sys
import typst

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_TYP = os.path.join(ROOT, "src", "main.typ")
OUTPUT_PDF = os.path.join(ROOT, "DE_CUONG_ON_TAP_KTGK_I_TOAN_10_2026.pdf")
REPO_FONTS = os.path.join(ROOT, "src", "fonts")
FONT_DIRS = [d for d in (REPO_FONTS, "/tmp/fonts") if os.path.isdir(d)]


def main():
    print(f"Compiling {INPUT_TYP} with fonts from {FONT_DIRS} ...")
    typst.compile(INPUT_TYP, output=OUTPUT_PDF, font_paths=FONT_DIRS)
    size_kb = os.path.getsize(OUTPUT_PDF) / 1024
    print(f"Compiled PDF -> {OUTPUT_PDF} ({size_kb:,.1f} KB)")


if __name__ == "__main__":
    sys.exit(main())
