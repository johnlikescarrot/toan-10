#!/usr/bin/env python3
"""Verify the generated review PDF, its text layer, structure, and coverage."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import pymupdf
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
DOC_DIR = ROOT / "de-cuong"
PDF = DOC_DIR / "DE-CUONG-TOAN-10-GIUA-KI-I-2026-2027.pdf"
EXAM_SOURCE = DOC_DIR / "02-de-on.typ"


def source_question_counts() -> dict[str, int]:
    source = EXAM_SOURCE.read_text(encoding="utf-8")
    labels = re.findall(r'#exam-question\("([A-ZĐ0-9]+)"', source)
    return {
        "multiple_choice": sum(re.fullmatch(r"C\d+", label) is not None for label in labels),
        "true_false": sum(label.startswith("ĐS") for label in labels),
        "short_answer": sum(label.startswith("TLN") for label in labels),
        "essay": sum(re.fullmatch(r"TL\d+", label) is not None for label in labels),
    }


def render_contact_sheets(doc: pymupdf.Document, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for start in range(0, len(doc), 8):
        out = pymupdf.open()
        sheet = out.new_page(width=900, height=1320)
        for j, pno in enumerate(range(start, min(start + 8, len(doc)))):
            col, row = j % 2, j // 2
            rect = pymupdf.Rect(15 + col * 445, 30 + row * 320, 435 + col * 445, 315 + row * 320)
            sheet.show_pdf_page(rect, doc, pno)
            sheet.insert_text((rect.x0, rect.y0 - 8), f"PDF page {pno + 1}", fontsize=10)
        target = output_dir / f"contact-{start + 1:02}-{min(start + 8, len(doc)):02}.png"
        sheet.get_pixmap(matrix=pymupdf.Matrix(1.2, 1.2), alpha=False).save(target)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--render", action="store_true", help="also render contact sheets for visual review")
    args = parser.parse_args()

    assert PDF.is_file(), f"Missing {PDF}; run scripts/build_review.py first"
    assert PDF.stat().st_size > 100_000, "PDF is unexpectedly small"
    counts = source_question_counts()
    assert counts == {"multiple_choice": 12, "true_false": 2, "short_answer": 4, "essay": 3}, counts

    doc = pymupdf.open(PDF)
    reader = PdfReader(str(PDF))
    assert len(doc) == len(reader.pages)
    assert 24 <= len(doc) <= 40, f"Unexpected page count: {len(doc)}"
    assert "Toán 10" in (doc.metadata.get("title") or "")
    assert len(doc.get_toc()) >= 50, "PDF bookmarks/outline are incomplete"

    page_texts = [page.get_text() for page in doc]
    text = "\n".join(page_texts)
    assert "\ufffd" not in text, "Unicode replacement character found"
    assert len(text) > 45_000, "Searchable text layer is incomplete"
    assert min(len(t.strip()) for t in page_texts) >= 300, "A nearly blank page remains"

    required_text = [
        "Chuyên đề 1 · Mệnh đề và tập hợp",
        "Chuyên đề 2 · Bất phương trình",
        "Chuyên đề 3 · Hệ thức lượng trong tam giác",
        "Chuyên đề 4 · Vectơ",
        "Đề ôn tổng hợp · 90 phút",
        "Đáp án và lời giải chi tiết đề ôn",
        "Phụ lục đối chiếu ma trận và nguồn",
        "không phải nguyên văn đề thi chính thức",
        "30 sản phẩm X và 20 sản phẩm Y",
        "130 triệu",
        "27/27",
    ]
    for needle in required_text:
        assert needle in text, f"Missing required text: {needle}"

    for pno, page in enumerate(doc, 1):
        assert abs(page.rect.width - 595.28) < 0.2 and abs(page.rect.height - 841.89) < 0.2
        for block in page.get_text("blocks"):
            x0, y0, x1, y1 = block[:4]
            assert x0 >= -1 and y0 >= -1 and x1 <= page.rect.width + 1 and y1 <= page.rect.height + 1, (
                f"Text outside page bounds on page {pno}: {(x0, y0, x1, y1)}"
            )

    font_names = {f[3] for page in doc for f in page.get_fonts(full=True)}
    assert any("DejaVuSans" in name for name in font_names), font_names
    assert any("NewCMMath" in name for name in font_names), font_names
    assert sum(len(page.get_links()) for page in doc) >= 7, "Reference links missing"
    assert len(list((DOC_DIR / "assets").glob("*.svg"))) == 7, "Expected seven original SVG diagrams"

    if args.render:
        render_contact_sheets(doc, ROOT / "verification")

    print(f"PASS: {PDF.relative_to(ROOT)}")
    print(f"  {len(doc)} A4 pages; {len(text):,} searchable characters; {len(doc.get_toc())} bookmarks")
    print(f"  Questions: {counts}; 8 true/false statements; 27/27 mapped responses")
    print(f"  Fonts: {', '.join(sorted(font_names))}")
    print(f"  Links: {sum(len(page.get_links()) for page in doc)}; SVG diagrams: 7")
    if args.render:
        print(f"  Contact sheets: {(ROOT / 'verification').relative_to(ROOT)}")


if __name__ == "__main__":
    main()
