#!/usr/bin/env python3
"""
Compile src/main.typ into DE_CUONG_ON_TAP_GIUA_KI_I_TOAN_10_2026_2027.pdf
using the embedded Be Vietnam Pro font family.
"""

from pathlib import Path
import typst

ROOT = Path(__file__).resolve().parent.parent
INPUT_TYP = ROOT / "src" / "main.typ"
FONTS_DIR = ROOT / "src" / "fonts"
OUTPUT_PDF = ROOT / "DE_CUONG_ON_TAP_GIUA_KI_I_TOAN_10_2026_2027.pdf"


def main() -> None:
    pdf_bytes = typst.compile(
        str(INPUT_TYP),
        root=str(ROOT),
        font_paths=[str(FONTS_DIR)],
    )
    OUTPUT_PDF.write_bytes(pdf_bytes)
    size_kb = len(pdf_bytes) / 1024
    print(f"Built {OUTPUT_PDF.name} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
