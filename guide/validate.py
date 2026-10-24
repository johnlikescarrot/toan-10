#!/usr/bin/env python3
"""Structural, mathematical and visual-QA checks for the generated guide."""
from __future__ import annotations

import math
from pathlib import Path
import re

import pymupdf
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "DE-CUONG-ON-TAP-TOAN-10-GIUA-KI-1-2026-2027.pdf"
BUILD = ROOT / "build" / "guide"


def verify_mathematics() -> None:
    assert 2**5 == 32
    assert 40 - (24 + 17 - 9) == 8
    cos_a = -math.sqrt(1 - (3 / 5) ** 2)
    tan_a = (3 / 5) / cos_a
    assert math.isclose(5 * cos_a + 2 * tan_a, -5.5)
    assert math.isclose(8**2 + 5**2 - 2 * 8 * 5 * math.cos(math.radians(60)), 49)
    assert math.isclose(50**2 + 80**2 - 2 * 50 * 80 * math.cos(math.radians(60)), 4900)
    vertices = [(0, 0), (30, 0), (20, 20), (0, 40)]
    values = [400 * x + 300 * y for x, y in vertices]
    assert values == [0, 12000, 14000, 12000]
    assert vertices[values.index(max(values))] == (20, 20)
    assert math.isclose(math.sqrt(21 * 8 * 7 * 6), 84)


def verify_question_counts(text: str) -> None:
    start = text.rindex("PHẦN VII • ĐỀ LUYỆN TẬP BÁM SÁT MA TRẬN")
    end = text.rindex("PHẦN VIII • ĐÁP ÁN VÀ LỜI GIẢI CHI TIẾT")
    exam = text[start:end]
    markers = [
        "PHẦN I • TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN",
        "PHẦN II • TRẮC NGHIỆM ĐÚNG–SAI",
        "PHẦN III • TRẢ LỜI NGẮN",
        "PHẦN IV • TỰ LUẬN",
    ]
    positions = [exam.index(marker) for marker in markers]
    sections = [
        exam[positions[0]:positions[1]],
        exam[positions[1]:positions[2]],
        exam[positions[2]:positions[3]],
        exam[positions[3]:],
    ]
    expected = [12, 2, 4, 3]
    for index, (section, count) in enumerate(zip(sections, expected), 1):
        found = re.findall(r"Câu\s+(\d+)(?:\.|\s+\(1,0 điểm\))", section)
        assert len(found) == count, f"Exam section {index}: expected {count} questions, found {found}"
    for n in range(1, 13):
        assert re.search(rf"Câu\s+{n}\.", sections[0]), f"Missing MC question {n}"
    assert "đúng 1 ý 0,1" in text.lower()
    assert "Câu 1 — C" in text and "Câu 12 — C" in text


def make_contact_sheet(pdf: pymupdf.Document) -> None:
    BUILD.mkdir(parents=True, exist_ok=True)
    scale = 0.34
    thumbs = []
    for number, page in enumerate(pdf, 1):
        pix = page.get_pixmap(matrix=pymupdf.Matrix(scale, scale), alpha=False)
        image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        tile = Image.new("RGB", (image.width + 8, image.height + 25), "white")
        tile.paste(image, (4, 20))
        ImageDraw.Draw(tile).text((6, 4), f"Trang {number}", fill="#16324F")
        thumbs.append(tile)
    columns = 5
    rows = math.ceil(len(thumbs) / columns)
    tw = max(im.width for im in thumbs)
    th = max(im.height for im in thumbs)
    sheet = Image.new("RGB", (columns * tw, rows * th), "#CFDCE3")
    for index, image in enumerate(thumbs):
        sheet.paste(image, ((index % columns) * tw, (index // columns) * th))
    sheet.save(BUILD / "contact-sheet.png")


def main() -> None:
    verify_mathematics()
    assert PDF.exists() and PDF.stat().st_size > 500_000
    pdf = pymupdf.open(PDF)
    assert len(pdf) >= 30, f"Unexpectedly short guide: {len(pdf)} pages"
    text = "\n".join(page.get_text() for page in pdf)
    flat_text = re.sub(r"\s+", " ", text)
    required = [
        "không có đề thi hoàn chỉnh và không có đáp án chính thức",
        "PHẦN II • CHƯƠNG I: MỆNH ĐỀ VÀ TẬP HỢP",
        "PHẦN III • CHƯƠNG II:",
        "PHẦN IV • CHƯƠNG III:",
        "PHẦN V • CHƯƠNG IV:",
        "PHẦN VI • PHIẾU CÔNG THỨC",
        "PHẦN VII • ĐỀ LUYỆN TẬP BÁM SÁT MA TRẬN",
        "PHẦN VIII • ĐÁP ÁN VÀ LỜI GIẢI CHI TIẾT",
        "PHẦN IX • PHỤ LỤC ĐỐI CHIẾU TOÀN BỘ BẢNG ĐẶC TẢ",
        "20 sản phẩm X và 20 sản phẩm Y",
        "rgep.moet.gov.vn",
        "hanhtrangso.nxbgd.vn",
    ]
    for phrase in required:
        assert phrase in flat_text, f"Missing required text: {phrase}"
    for bad in ["ngườI", "NgườI", "mớI", "lờI", "LờI", "thờI", "ThờI", "�"]:
        assert bad not in text, f"Unexpected typo/replacement character: {bad}"
    verify_question_counts(flat_text)

    # ReportLab must embed a Unicode Vietnamese font; math is high-resolution artwork.
    fonts = {}
    for page in pdf:
        for item in page.get_fonts(full=True):
            fonts[item[0]] = item
    assert any("DejaVuSans" in str(item) for item in fonts.values()), "Unicode font not found"
    for xref, item in fonts.items():
        if "DejaVu" in str(item):
            assert pdf.extract_font(xref)[3], f"Font is not embedded: {item}"

    assert len(pdf.get_toc()) >= 35, "PDF bookmarks/table of contents are incomplete"
    lang = pdf.xref_get_key(pdf.pdf_catalog(), "Lang")
    assert "vi-VN" in str(lang), f"PDF language missing: {lang}"

    sparse = []
    outside = []
    for number, page in enumerate(pdf, 1):
        if len(page.get_text().strip()) < 100:
            sparse.append(number)
        rect = page.rect
        for block in page.get_text("blocks"):
            x0, y0, x1, y1 = block[:4]
            if x0 < -2 or y0 < -2 or x1 > rect.width + 2 or y1 > rect.height + 2:
                outside.append((number, (x0, y0, x1, y1)))
    assert not sparse, f"Possible blank pages: {sparse}"
    assert not outside, f"Text outside page: {outside[:3]}"

    make_contact_sheet(pdf)
    print(f"PASS: {PDF.name}")
    print(f"  {len(pdf)} pages; {PDF.stat().st_size:,} bytes; {len(pdf.get_toc())} bookmarks")
    print(f"  12 MC + 2 true/false + 4 short-answer + 3 essay questions verified")
    print("  Numeric answers, source notice, Vietnamese font, language and page bounds verified")
    print(f"  Visual overview: {BUILD / 'contact-sheet.png'}")
    pdf.close()


if __name__ == "__main__":
    main()
