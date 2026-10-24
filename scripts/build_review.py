#!/usr/bin/env python3
"""Build the Grade 10 midterm review PDF and its original SVG diagrams.

Usage:
    python scripts/build_review.py

The only runtime dependency is the `typst` Python package. All diagrams are
created locally; the build does not download fonts, images, or Typst packages.
"""

from __future__ import annotations

import math
from pathlib import Path

import typst

ROOT = Path(__file__).resolve().parents[1]
DOC_DIR = ROOT / "de-cuong"
ASSET_DIR = DOC_DIR / "assets"
OUTPUT = DOC_DIR / "DE-CUONG-TOAN-10-GIUA-KI-I-2026-2027.pdf"

NAVY = "#16324F"
BLUE = "#2F6FED"
TEAL = "#0E7490"
ORANGE = "#C55A11"
LIGHT_BLUE = "#DCE8FF"
LIGHT_TEAL = "#DDF3F1"
GRAY = "#64748B"
GRID = "#D8E0EA"


def write_svg(name: str, width: int, height: int, body: str) -> None:
    """Write one standalone, high-contrast SVG diagram."""
    source = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="{NAVY}"/>
    </marker>
    <marker id="blue-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="{BLUE}"/>
    </marker>
    <style>
      text {{ font-family: 'DejaVu Sans', sans-serif; fill: {NAVY}; font-size: 16px; }}
      .small {{ font-size: 13px; }}
      .label {{ font-weight: 700; }}
      .axis {{ stroke: {NAVY}; stroke-width: 1.8; }}
      .grid {{ stroke: {GRID}; stroke-width: 1; }}
      .boundary {{ stroke: {BLUE}; stroke-width: 2.6; fill: none; }}
    </style>
  </defs>
  <rect width="100%" height="100%" fill="white"/>
{body}
</svg>
'''
    (ASSET_DIR / name).write_text(source, encoding="utf-8")


def venn_intersection() -> None:
    body = f'''
  <defs><clipPath id="circle-a"><circle cx="185" cy="120" r="76"/></clipPath></defs>
  <rect x="35" y="20" width="360" height="190" rx="12" fill="#F8FAFC" stroke="{NAVY}" stroke-width="2"/>
  <circle cx="185" cy="120" r="76" fill="white" stroke="{BLUE}" stroke-width="2.5"/>
  <circle cx="265" cy="120" r="76" fill="{LIGHT_BLUE}" clip-path="url(#circle-a)"/>
  <circle cx="265" cy="120" r="76" fill="none" stroke="{TEAL}" stroke-width="2.5"/>
  <text x="377" y="42" class="label">U</text>
  <text x="120" y="65" class="label" fill="{BLUE}">A</text>
  <text x="315" y="65" class="label" fill="{TEAL}">B</text>
  <text x="215" y="225" class="small" text-anchor="middle">Phần tô màu</text>
'''
    write_svg("venn-giao.svg", 430, 240, body)


def inequality_region() -> None:
    # One consistent mapping for the axes, grid and boundary:
    # X = 117 + 52x; Y = 250 - 42y. Thus O=(117,250),
    # (6,0)=(429,250), and (0,3)=(117,124).
    body = f'''
  <rect x="13" y="35" width="442" height="300" fill="#FBFDFF" stroke="{GRID}"/>
  <path d="M 13 82 L 455 260.5 L 455 335 L 13 335 Z" fill="{LIGHT_TEAL}" opacity="0.95"/>
  <path d="M 65 40 L 65 335 M 117 40 L 117 335 M 169 40 L 169 335 M 221 40 L 221 335 M 273 40 L 273 335 M 325 40 L 325 335 M 377 40 L 377 335 M 429 40 L 429 335" class="grid"/>
  <path d="M 20 292 L 450 292 M 20 250 L 450 250 M 20 208 L 450 208 M 20 166 L 450 166 M 20 124 L 450 124 M 20 82 L 450 82 M 20 40 L 450 40" class="grid"/>
  <line x1="35" y1="250" x2="448" y2="250" class="axis" marker-end="url(#arrow)"/>
  <line x1="117" y1="330" x2="117" y2="42" class="axis" marker-end="url(#arrow)"/>
  <line x1="13" y1="82" x2="455" y2="260.5" class="boundary"/>
  <circle cx="117" cy="250" r="4" fill="{ORANGE}"/>
  <text x="101" y="270" class="small">O</text>
  <text x="437" y="272" class="label">x</text>
  <text x="126" y="48" class="label">y</text>
  <text x="421" y="270" class="small">6</text>
  <text x="88" y="130" class="small">3</text>
  <text x="265" y="168" class="label" fill="{BLUE}">d: x + 2y = 6</text>
  <text x="235" y="350" class="label" fill="{TEAL}" text-anchor="middle">Miền nghiệm x + 2y ≤ 6</text>
  <text x="235" y="367" class="small" text-anchor="middle">(nửa mặt phẳng chứa O, kể cả bờ d)</text>
'''
    write_svg("mien-nghiem-bpt.svg", 470, 375, body)


def system_region() -> None:
    # View: 0 ≤ x,y ≤ 60. Mapping: X=70+5.5x, Y=315-4.2y.
    body = f'''
  <path d="M 70 63 L 70 357 M 125 63 L 125 357 M 180 63 L 180 357 M 235 63 L 235 357 M 290 63 L 290 357 M 345 63 L 345 357 M 400 63 L 400 357" class="grid"/>
  <path d="M 45 315 L 420 315 M 45 273 L 420 273 M 45 231 L 420 231 M 45 189 L 420 189 M 45 147 L 420 147 M 45 105 L 420 105 M 45 63 L 420 63" class="grid"/>
  <polygon points="70,315 290,315 235,231 70,105" fill="{LIGHT_BLUE}" stroke="{TEAL}" stroke-width="2"/>
  <line x1="70" y1="105" x2="345" y2="315" class="boundary"/>
  <line x1="290" y1="315" x2="125" y2="63" class="boundary"/>
  <line x1="45" y1="315" x2="415" y2="315" class="axis" marker-end="url(#arrow)"/>
  <line x1="70" y1="345" x2="70" y2="48" class="axis" marker-end="url(#arrow)"/>
  <circle cx="70" cy="315" r="4" fill="{NAVY}"/><circle cx="290" cy="315" r="4" fill="{NAVY}"/>
  <circle cx="235" cy="231" r="4" fill="{ORANGE}"/><circle cx="70" cy="105" r="4" fill="{NAVY}"/>
  <text x="54" y="337" class="small">O(0;0)</text>
  <text x="275" y="339" class="small">A(40;0)</text>
  <text x="243" y="229" class="small">B(30;20)</text>
  <text x="78" y="103" class="small">C(0;50)</text>
  <text x="398" y="339" class="label">x</text><text x="79" y="52" class="label">y</text>
  <text x="310" y="145" class="small" fill="{BLUE}">x + y = 50</text>
  <text x="138" y="70" class="small" fill="{BLUE}">2x + y = 80</text>
  <text x="121" y="260" class="label" fill="{TEAL}">Miền nghiệm</text>
  <text x="52" y="378" class="small">Các vạch lưới cách nhau 10 đơn vị.</text>
'''
    write_svg("mien-nghiem-he.svg", 440, 390, body)


def triangle_notation() -> None:
    body = f'''
  <polygon points="95,235 375,235 255,48" fill="#F8FAFC" stroke="{NAVY}" stroke-width="2.5"/>
  <path d="M 129 235 A 34 34 0 0 0 116 213" fill="none" stroke="{BLUE}" stroke-width="2"/>
  <path d="M 341 235 A 34 34 0 0 1 354 213" fill="none" stroke="{BLUE}" stroke-width="2"/>
  <path d="M 239 78 A 38 38 0 0 1 271 78" fill="none" stroke="{BLUE}" stroke-width="2"/>
  <text x="238" y="35" class="label">A</text>
  <text x="73" y="255" class="label">B</text>
  <text x="378" y="255" class="label">C</text>
  <text x="229" y="258" class="label" fill="{TEAL}">a = BC</text>
  <text x="112" y="137" class="label" fill="{TEAL}" transform="rotate(58 112 137)">c = AB</text>
  <text x="330" y="137" class="label" fill="{TEAL}" transform="rotate(-57 330 137)">b = CA</text>
  <text x="133" y="218" class="small">B</text><text x="322" y="218" class="small">C</text><text x="250" y="88" class="small">A</text>
'''
    write_svg("tam-giac-ki-hieu.svg", 450, 280, body)


def pond_triangle() -> None:
    body = f'''
  <ellipse cx="255" cy="92" rx="93" ry="45" fill="#DDF3F1" stroke="{TEAL}" stroke-width="1.8"/>
  <path d="M 178 91 Q 200 78 222 91 T 266 91 T 310 91" fill="none" stroke="{TEAL}" stroke-width="1.4"/>
  <line x1="110" y1="48" x2="365" y2="112" stroke="{GRAY}" stroke-width="2" stroke-dasharray="7 6"/>
  <line x1="110" y1="48" x2="72" y2="230" stroke="{NAVY}" stroke-width="2.5"/>
  <line x1="72" y1="230" x2="365" y2="112" stroke="{NAVY}" stroke-width="2.5"/>
  <path d="M 91 208 A 32 32 0 0 1 105 221" fill="none" stroke="{ORANGE}" stroke-width="2.4"/>
  <circle cx="110" cy="48" r="4" fill="{NAVY}"/><circle cx="365" cy="112" r="4" fill="{NAVY}"/><circle cx="72" cy="230" r="4" fill="{NAVY}"/>
  <text x="94" y="35" class="label">A</text><text x="371" y="118" class="label">B</text><text x="51" y="251" class="label">C</text>
  <text x="43" y="132" class="label" transform="rotate(78 43 132)">80 m</text>
  <text x="201" y="197" class="label" transform="rotate(-22 201 197)">50 m</text>
  <text x="104" y="206" class="small" fill="{ORANGE}">60°</text>
  <text x="229" y="63" class="label">AB = ?</text>
  <text x="220" y="105" class="small" fill="{TEAL}">mặt nước</text>
'''
    write_svg("tam-giac-thuc-te.svg", 440, 270, body)


def parallelogram_vectors() -> None:
    body = f'''
  <polygon points="85,205 295,205 380,58 170,58" fill="#F8FAFC" stroke="{GRAY}" stroke-width="1.7"/>
  <line x1="85" y1="205" x2="295" y2="205" stroke="{BLUE}" stroke-width="3" marker-end="url(#blue-arrow)"/>
  <line x1="170" y1="58" x2="380" y2="58" stroke="{TEAL}" stroke-width="3" marker-end="url(#arrow)"/>
  <line x1="85" y1="205" x2="170" y2="58" stroke="{NAVY}" stroke-width="2.5" marker-end="url(#arrow)"/>
  <line x1="295" y1="205" x2="380" y2="58" stroke="{NAVY}" stroke-width="2.5" marker-end="url(#arrow)"/>
  <text x="66" y="226" class="label">A</text><text x="292" y="228" class="label">B</text>
  <text x="384" y="59" class="label">C</text><text x="151" y="49" class="label">D</text>
  <text x="175" y="226" class="small" fill="{BLUE}">cùng hướng, cùng độ dài</text>
  <text x="213" y="45" class="small" fill="{TEAL}">AB = DC (theo vectơ)</text>
'''
    write_svg("hinh-binh-hanh-vecto.svg", 450, 245, body)


def unit_semicircle() -> None:
    body = f'''
  <path d="M 95 220 A 130 130 0 0 1 355 220" fill="#F8FAFC" stroke="{NAVY}" stroke-width="2.2"/>
  <line x1="65" y1="220" x2="390" y2="220" class="axis" marker-end="url(#arrow)"/>
  <line x1="225" y1="245" x2="225" y2="48" class="axis" marker-end="url(#arrow)"/>
  <line x1="225" y1="220" x2="160" y2="107.5" stroke="{BLUE}" stroke-width="2.5"/>
  <line x1="160" y1="107.5" x2="160" y2="220" stroke="{GRAY}" stroke-width="1.5" stroke-dasharray="5 4"/>
  <line x1="160" y1="107.5" x2="225" y2="107.5" stroke="{GRAY}" stroke-width="1.5" stroke-dasharray="5 4"/>
  <path d="M 275 220 A 50 50 0 0 0 200 176.7" fill="none" stroke="{ORANGE}" stroke-width="2"/>
  <circle cx="160" cy="107.5" r="4" fill="{BLUE}"/>
  <text x="143" y="96" class="label">M(x₀; y₀)</text>
  <text x="229" y="174" class="small" fill="{ORANGE}">α</text>
  <text x="144" y="240" class="small">x₀ = cos α</text>
  <text x="230" y="102" class="small">y₀ = sin α</text>
  <text x="375" y="241" class="label">x</text><text x="235" y="52" class="label">y</text>
  <text x="208" y="240" class="small">O</text><text x="346" y="240" class="small">1</text><text x="88" y="240" class="small">−1</text>
'''
    write_svg("nua-duong-tron-don-vi.svg", 450, 265, body)


def generate_assets() -> None:
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    venn_intersection()
    inequality_region()
    system_region()
    triangle_notation()
    pond_triangle()
    parallelogram_vectors()
    unit_semicircle()


def validate_numerical_results() -> None:
    """Guard the exact numerical answers used in the mock exam."""
    assert 25 + 18 - 8 == 35  # Short-answer question 2.
    assert 2**5 == 32  # Short-answer question 1.
    assert math.isclose(5**2 + 7**2 - 2 * 5 * 7 * math.cos(math.radians(60)), 39)
    assert math.isclose(3 * (1 - (-1 / 3) ** 2) + 2 * (-1 / 3), 2)
    assert math.isclose(0.5 * 6 * 8 * math.sin(math.radians(150)), 12)
    assert math.isclose(math.sqrt(80**2 + 50**2 - 2 * 80 * 50 * math.cos(math.radians(60))), 70)
    vertices = [(0, 0), (40, 0), (30, 20), (0, 50)]
    values = [3 * x + 2 * y for x, y in vertices]
    assert values == [0, 120, 130, 100]
    assert max(values) == 130 and vertices[values.index(max(values))] == (30, 20)


def main() -> None:
    validate_numerical_results()
    generate_assets()
    typst.compile(
        str(DOC_DIR / "main.typ"),
        root=str(ROOT),
        output=str(OUTPUT),
        font_paths=["/usr/share/fonts/truetype/dejavu"],
        format="pdf",
    )
    print(f"Created {OUTPUT.relative_to(ROOT)} ({OUTPUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
