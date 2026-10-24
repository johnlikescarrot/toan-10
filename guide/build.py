#!/usr/bin/env python3
"""Build the final Vietnamese review-guide PDF."""
from __future__ import annotations

import sys
from pathlib import Path

import pymupdf

# Allow `python3 guide/build.py` from the repository root.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from guide.content import build_story
from guide.pdfguide import BUILD_DIR, GuideBuilder, GuideDocTemplate

OUTPUT = ROOT / "DE-CUONG-ON-TAP-TOAN-10-GIUA-KI-1-2026-2027.pdf"


def main() -> None:
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    raw = BUILD_DIR / "guide-raw.pdf"
    builder = GuideBuilder()
    try:
        story = build_story(builder)
        doc = GuideDocTemplate(str(raw))
        doc.multiBuild(story, maxPasses=12)
    finally:
        builder.math.close()

    # Post-process metadata without changing page content, links or bookmarks.
    pdf = pymupdf.open(raw)
    catalog = pdf.pdf_catalog()
    pdf.xref_set_key(catalog, "Lang", "(vi-VN)")
    pdf.xref_set_key(catalog, "PageMode", "/UseOutlines")
    pdf.xref_set_key(catalog, "ViewerPreferences", "<</DisplayDocTitle true>>")
    metadata = pdf.metadata
    metadata.update({
        "title": "Đề cương ôn tập Toán 10 – Giữa học kì I – 2026–2027",
        "author": "Tài liệu ôn tập biên soạn theo ma trận Trường THPT Hà Huy Tập",
        "subject": "Toán 10 Kết nối tri thức: lý thuyết, ví dụ, đề luyện tập 90 phút và đáp án chi tiết",
        "keywords": "Toán 10, Kết nối tri thức, giữa học kì 1, mệnh đề, tập hợp, bất phương trình, hệ thức lượng, vectơ",
        "creator": "ReportLab + MathJax",
    })
    pdf.set_metadata(metadata)
    pdf.save(OUTPUT, garbage=4, deflate=True)
    pages = len(pdf)
    pdf.close()
    print(f"Built {OUTPUT} ({pages} pages, {OUTPUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
