#!/usr/bin/env python3
"""
Generate 14 crisp, mathematically exact vector SVG figures for the Grade 10 Math
Midterm I Study Guide (Kết nối tri thức với cuộc sống — Năm học 2026–2027).
"""

import math
from pathlib import Path

ASSETS_DIR = Path(__file__).resolve().parent.parent / "src" / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

FONT = "Be Vietnam Pro"


def save_svg(name: str, content: str) -> None:
    path = ASSETS_DIR / name
    path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"Generated {path.relative_to(ASSETS_DIR.parent.parent)}")


# ---------------------------------------------------------------------------
# 1. venn_operations.svg — 4 phép toán trên tập hợp (Giao, Hợp, Hiệu, Phần bù)
# ---------------------------------------------------------------------------
def gen_venn_operations() -> None:
    w, h = 760, 175
    panels = [
        ("Giao: A ∩ B", "x ∈ A và x ∈ B"),
        ("Hợp: A ∪ B", "x ∈ A hoặc x ∈ B"),
        ("Hiệu: A \\ B", "x ∈ A và x ∉ B"),
        ("Phần bù: C_A B (B ⊂ A)", "A \\ B khi B ⊂ A"),
    ]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        '<defs>',
        '  <clipPath id="clipA1"><circle cx="78" cy="82" r="42"/></clipPath>',
        '  <mask id="maskDiffA">',
        '    <rect x="0" y="0" width="800" height="200" fill="white"/>',
        '    <circle cx="497" cy="82" r="42" fill="black"/>',
        '  </mask>',
        '  <mask id="maskComp">',
        '    <rect x="0" y="0" width="800" height="200" fill="white"/>',
        '    <circle cx="678" cy="86" r="22" fill="black"/>',
        '  </mask>',
        '</defs>',
    ]
    for i, (title, sub) in enumerate(panels):
        ox = i * 190
        parts.append(
            f'<rect x="{ox+4}" y="4" width="182" height="167" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>'
        )
        parts.append(
            f'<text x="{ox+95}" y="23" text-anchor="middle" font-family="{FONT}" font-size="11.5" font-weight="bold" fill="#0F172A">{title}</text>'
        )
        if i == 0:  # Intersection
            c1x, c2x, cy, r = ox + 78, ox + 112, 82, 42
            parts.append(f'<circle cx="{c1x}" cy="{cy}" r="{r}" fill="#FFFFFF" stroke="#64748B" stroke-width="1.4"/>')
            parts.append(f'<circle cx="{c2x}" cy="{cy}" r="{r}" fill="#FFFFFF" stroke="#64748B" stroke-width="1.4"/>')
            parts.append(f'<circle cx="{c2x}" cy="{cy}" r="{r}" fill="#3B82F6" fill-opacity="0.45" clip-path="url(#clipA1)"/>')
            parts.append(f'<circle cx="{c1x}" cy="{cy}" r="{r}" fill="none" stroke="#1E3A8A" stroke-width="1.5"/>')
            parts.append(f'<circle cx="{c2x}" cy="{cy}" r="{r}" fill="none" stroke="#1E3A8A" stroke-width="1.5"/>')
            parts.append(f'<text x="{c1x-18}" y="{cy+4}" font-family="{FONT}" font-size="12" font-weight="bold" fill="#0F172A">A</text>')
            parts.append(f'<text x="{c2x+12}" y="{cy+4}" font-family="{FONT}" font-size="12" font-weight="bold" fill="#0F172A">B</text>')
        elif i == 1:  # Union
            c1x, c2x, cy, r = ox + 78, ox + 112, 82, 42
            parts.append(f'<circle cx="{c1x}" cy="{cy}" r="{r}" fill="#14B8A6" fill-opacity="0.38"/>')
            parts.append(f'<circle cx="{c2x}" cy="{cy}" r="{r}" fill="#14B8A6" fill-opacity="0.38"/>')
            parts.append(f'<circle cx="{c1x}" cy="{cy}" r="{r}" fill="none" stroke="#0F766E" stroke-width="1.5"/>')
            parts.append(f'<circle cx="{c2x}" cy="{cy}" r="{r}" fill="none" stroke="#0F766E" stroke-width="1.5"/>')
            parts.append(f'<text x="{c1x-18}" y="{cy+4}" font-family="{FONT}" font-size="12" font-weight="bold" fill="#0F172A">A</text>')
            parts.append(f'<text x="{c2x+12}" y="{cy+4}" font-family="{FONT}" font-size="12" font-weight="bold" fill="#0F172A">B</text>')
        elif i == 2:  # Difference A \ B (ox = 380 -> c1x=458, c2x=497)
            c1x, c2x, cy, r = 458, 497, 82, 42
            parts.append(f'<circle cx="{c2x}" cy="{cy}" r="{r}" fill="#FFFFFF"/>')
            parts.append(f'<circle cx="{c1x}" cy="{cy}" r="{r}" fill="#F59E0B" fill-opacity="0.45" mask="url(#maskDiffA)"/>')
            parts.append(f'<circle cx="{c1x}" cy="{cy}" r="{r}" fill="none" stroke="#B45309" stroke-width="1.5"/>')
            parts.append(f'<circle cx="{c2x}" cy="{cy}" r="{r}" fill="none" stroke="#64748B" stroke-width="1.4" stroke-dasharray="4,3"/>')
            parts.append(f'<text x="{c1x-18}" y="{cy+4}" font-family="{FONT}" font-size="12" font-weight="bold" fill="#0F172A">A</text>')
            parts.append(f'<text x="{c2x+14}" y="{cy+4}" font-family="{FONT}" font-size="12" font-weight="bold" fill="#475569">B</text>')
        else:  # Complement C_A B (ox = 570 -> outer cx=665, inner cx=678)
            cx_out, cy_out, r_out = 665, 82, 45
            cx_in, cy_in, r_in = 678, 86, 22
            parts.append(f'<circle cx="{cx_out}" cy="{cy_out}" r="{r_out}" fill="#8B5CF6" fill-opacity="0.35" mask="url(#maskComp)"/>')
            parts.append(f'<circle cx="{cx_in}" cy="{cy_in}" r="{r_in}" fill="#FFFFFF" stroke="#475569" stroke-width="1.4"/>')
            parts.append(f'<circle cx="{cx_out}" cy="{cy_out}" r="{r_out}" fill="none" stroke="#6D28D9" stroke-width="1.6"/>')
            parts.append(f'<text x="{cx_out-28}" y="{cy_out-12}" font-family="{FONT}" font-size="12" font-weight="bold" fill="#4C1D95">A</text>')
            parts.append(f'<text x="{cx_in}" y="{cy_in+4}" text-anchor="middle" font-family="{FONT}" font-size="11.5" font-weight="bold" fill="#0F172A">B</text>')
        parts.append(
            f'<text x="{ox+95}" y="154" text-anchor="middle" font-family="{FONT}" font-size="10.2" fill="#334155">{sub}</text>'
        )
    parts.append("</svg>")
    save_svg("venn_operations.svg", "\n".join(parts))


# ---------------------------------------------------------------------------
# 2. number_line_intervals.svg — Biểu diễn khoảng, đoạn, nửa khoảng & phép toán trên trục số
# ---------------------------------------------------------------------------
def gen_number_line_intervals() -> None:
    w, h = 760, 215
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        '<rect x="2" y="2" width="756" height="211" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>',
        f'<text x="380" y="24" text-anchor="middle" font-family="{FONT}" font-size="12" font-weight="bold" fill="#0F172A">Minh họa biểu diễn tập hợp và phép toán trên trục số thực ℝ (Ví dụ: A = [-2; 3), B = (1; 5])</text>',
    ]

    def x_pos(val: float) -> float:
        # map [-5, 7] -> [175, 715]
        return 175 + (val + 5) * (540 / 12.0)

    def draw_slashes(x1: float, x2: float, y: float) -> None:
        step = 9
        cur = x1 + 4
        while cur <= x2 - 4:
            parts.append(f'<line x1="{cur-3:.1f}" y1="{y+7}" x2="{cur+3:.1f}" y2="{y-7}" stroke="#94A3B8" stroke-width="1.1"/>')
            cur += step

    rows = [
        ("A = [-2; 3)", 60, -2, 3, "[", ")", "#1D4ED8"),
        ("B = (1; 5]", 105, 1, 5, "(", "]", "#0F766E"),
        ("A ∩ B = (1; 3)", 150, 1, 3, "(", ")", "#B45309"),
        ("A ∪ B = [-2; 5]", 192, -2, 5, "[", "]", "#6D28D9"),
    ]
    for label, y, a, b, lb, rb, col in rows:
        parts.append(f'<text x="18" y="{y+4}" font-family="{FONT}" font-size="11.2" font-weight="bold" fill="{col}">{label}</text>')
        parts.append(f'<line x1="165" y1="{y}" x2="735" y2="{y}" stroke="#475569" stroke-width="1.4"/>')
        parts.append(f'<polygon points="735,{y-4} 744,{y} 735,{y+4}" fill="#475569"/>')
        xa, xb = x_pos(a), x_pos(b)
        draw_slashes(168, xa, y)
        draw_slashes(xb, 730, y)
        parts.append(f'<line x1="{xa:.1f}" y1="{y}" x2="{xb:.1f}" y2="{y}" stroke="{col}" stroke-width="3.2"/>')
        parts.append(f'<text x="{xa:.1f}" y="{y+5}" text-anchor="middle" font-family="{FONT}" font-size="15" font-weight="bold" fill="{col}">{lb}</text>')
        parts.append(f'<text x="{xb:.1f}" y="{y+5}" text-anchor="middle" font-family="{FONT}" font-size="15" font-weight="bold" fill="{col}">{rb}</text>')
        parts.append(f'<text x="{xa:.1f}" y="{y-10}" text-anchor="middle" font-family="{FONT}" font-size="10.5" font-weight="bold" fill="#0F172A">{a}</text>')
        parts.append(f'<text x="{xb:.1f}" y="{y-10}" text-anchor="middle" font-family="{FONT}" font-size="10.5" font-weight="bold" fill="#0F172A">{b}</text>')
        # dashed vertical guide for 1 and 3
        if y == 60:
            for v in (-2, 1, 3, 5):
                xv = x_pos(v)
                parts.append(f'<line x1="{xv:.1f}" y1="48" x2="{xv:.1f}" y2="200" stroke="#CBD5E1" stroke-width="0.9" stroke-dasharray="3,3"/>')

    parts.append("</svg>")
    save_svg("number_line_intervals.svg", "\n".join(parts))


# ---------------------------------------------------------------------------
# 3. venn_counting_model.svg — Biểu đồ Ven đếm số phần tử (2 tập & 3 tập)
# ---------------------------------------------------------------------------
def gen_venn_counting_model() -> None:
    w, h = 760, 195
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        '<rect x="2" y="2" width="368" height="191" rx="8" fill="#EFF6FF" stroke="#93C5FD" stroke-width="1.2"/>',
        '<rect x="382" y="2" width="376" height="191" rx="8" fill="#F0FDFA" stroke="#5EEAD4" stroke-width="1.2"/>',
        # Left: 2 sets inside universal Omega
        f'<text x="186" y="22" text-anchor="middle" font-family="{FONT}" font-size="11.5" font-weight="bold" fill="#1E3A8A">Mô hình 2 tập hợp trong tập vũ trụ Ω</text>',
        '<rect x="18" y="32" width="336" height="122" rx="6" fill="#FFFFFF" stroke="#64748B" stroke-width="1.3"/>',
        f'<text x="30" y="48" font-family="{FONT}" font-size="11" font-weight="bold" fill="#334155">Ω</text>',
        '<circle cx="142" cy="94" r="49" fill="#3B82F6" fill-opacity="0.22" stroke="#1D4ED8" stroke-width="1.6"/>',
        '<circle cx="218" cy="94" r="49" fill="#F59E0B" fill-opacity="0.22" stroke="#B45309" stroke-width="1.6"/>',
        f'<text x="114" y="89" text-anchor="middle" font-family="{FONT}" font-size="10" font-weight="bold" fill="#1E3A8A">Chỉ A</text>',
        f'<text x="114" y="103" text-anchor="middle" font-family="{FONT}" font-size="9" fill="#1E3A8A">n(A) - x</text>',
        f'<text x="180" y="90" text-anchor="middle" font-family="{FONT}" font-size="10" font-weight="bold" fill="#B91C1C">A ∩ B</text>',
        f'<text x="180" y="105" text-anchor="middle" font-family="{FONT}" font-size="10.2" font-weight="bold" fill="#B91C1C">x</text>',
        f'<text x="246" y="89" text-anchor="middle" font-family="{FONT}" font-size="10" font-weight="bold" fill="#92400E">Chỉ B</text>',
        f'<text x="246" y="103" text-anchor="middle" font-family="{FONT}" font-size="9" fill="#92400E">n(B) - x</text>',
        f'<text x="314" y="143" text-anchor="middle" font-family="{FONT}" font-size="9.5" fill="#475569">Ngoài: k</text>',
        f'<text x="186" y="175" text-anchor="middle" font-family="{FONT}" font-size="10.2" font-weight="bold" fill="#0F172A">n(Ω) = n(A ∪ B) + k = n(A) + n(B) - n(A ∩ B) + k</text>',
        # Right: 3 sets
        f'<text x="570" y="22" text-anchor="middle" font-family="{FONT}" font-size="11.5" font-weight="bold" fill="#0F766E">Mô hình 3 tập hợp (Điền từ vùng lõi giữa ra ngoài)</text>',
        '<circle cx="545" cy="80" r="42" fill="#3B82F6" fill-opacity="0.18" stroke="#1D4ED8" stroke-width="1.4"/>',
        '<circle cx="595" cy="80" r="42" fill="#10B981" fill-opacity="0.18" stroke="#047857" stroke-width="1.4"/>',
        '<circle cx="570" cy="118" r="42" fill="#F59E0B" fill-opacity="0.18" stroke="#B45309" stroke-width="1.4"/>',
        f'<text x="512" y="55" font-family="{FONT}" font-size="11" font-weight="bold" fill="#1D4ED8">A</text>',
        f'<text x="622" y="55" font-family="{FONT}" font-size="11" font-weight="bold" fill="#047857">B</text>',
        f'<text x="612" y="148" font-family="{FONT}" font-size="11" font-weight="bold" fill="#B45309">C</text>',
        f'<text x="570" y="97" text-anchor="middle" font-family="{FONT}" font-size="9.5" font-weight="bold" fill="#B91C1C">① Lõi</text>',
        f'<text x="570" y="68" text-anchor="middle" font-family="{FONT}" font-size="9" fill="#0F172A">②</text>',
        f'<text x="545" y="109" text-anchor="middle" font-family="{FONT}" font-size="9" fill="#0F172A">②</text>',
        f'<text x="595" y="109" text-anchor="middle" font-family="{FONT}" font-size="9" fill="#0F172A">②</text>',
        f'<text x="526" y="78" text-anchor="middle" font-family="{FONT}" font-size="9" fill="#334155">③</text>',
        f'<text x="614" y="78" text-anchor="middle" font-family="{FONT}" font-size="9" fill="#334155">③</text>',
        f'<text x="570" y="140" text-anchor="middle" font-family="{FONT}" font-size="9" fill="#334155">③</text>',
        f'<text x="570" y="175" text-anchor="middle" font-family="{FONT}" font-size="9.8" font-weight="bold" fill="#0F172A">n(A∪B∪C) = Σn(A) - Σn(A∩B) + n(A∩B∩C)</text>',
        "</svg>",
    ]
    save_svg("venn_counting_model.svg", "\n".join(parts))


# ---------------------------------------------------------------------------
# Helper for Oxy coordinate plots
# ---------------------------------------------------------------------------
class OxyCanvas:
    def __init__(self, ox: float, oy: float, w: float, h: float, xmin: float, xmax: float, ymin: float, ymax: float):
        self.ox, self.oy, self.w, self.h = ox, oy, w, h
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax

    def px(self, x: float) -> float:
        return self.ox + (x - self.xmin) / (self.xmax - self.xmin) * self.w

    def py(self, y: float) -> float:
        return self.oy + self.h - (y - self.ymin) / (self.ymax - self.ymin) * self.h

    def pt(self, x: float, y: float) -> str:
        return f"{self.px(x):.1f},{self.py(y):.1f}"

    def grid_and_axes(self, step: int = 1) -> list[str]:
        out = []
        for xv in range(math.ceil(self.xmin), math.floor(self.xmax) + 1, step):
            x = self.px(xv)
            out.append(f'<line x1="{x:.1f}" y1="{self.oy}" x2="{x:.1f}" y2="{self.oy+self.h}" stroke="#E2E8F0" stroke-width="0.8"/>')
        for yv in range(math.ceil(self.ymin), math.floor(self.ymax) + 1, step):
            y = self.py(yv)
            out.append(f'<line x1="{self.ox}" y1="{y:.1f}" x2="{self.ox+self.w}" y2="{y:.1f}" stroke="#E2E8F0" stroke-width="0.8"/>')
        x0, y0 = self.px(0), self.py(0)
        # x-axis
        out.append(f'<line x1="{self.ox}" y1="{y0:.1f}" x2="{self.ox+self.w}" y2="{y0:.1f}" stroke="#0F172A" stroke-width="1.4"/>')
        out.append(f'<polygon points="{self.ox+self.w-6},{y0-3.5:.1f} {self.ox+self.w+2},{y0:.1f} {self.ox+self.w-6},{y0+3.5:.1f}" fill="#0F172A"/>')
        out.append(f'<text x="{self.ox+self.w-4}" y="{y0-7:.1f}" font-family="{FONT}" font-size="11" font-style="italic" font-weight="bold" fill="#0F172A">x</text>')
        # y-axis
        out.append(f'<line x1="{x0:.1f}" y1="{self.oy+self.h}" x2="{x0:.1f}" y2="{self.oy}" stroke="#0F172A" stroke-width="1.4"/>')
        out.append(f'<polygon points="{x0-3.5:.1f},{self.oy+6} {x0:.1f},{self.oy-2} {x0+3.5:.1f},{self.oy+6}" fill="#0F172A"/>')
        out.append(f'<text x="{x0+8:.1f}" y="{self.oy+10}" font-family="{FONT}" font-size="11" font-style="italic" font-weight="bold" fill="#0F172A">y</text>')
        out.append(f'<text x="{x0-10:.1f}" y="{y0+13:.1f}" font-family="{FONT}" font-size="10" font-weight="bold" fill="#0F172A">O</text>')
        return out


# ---------------------------------------------------------------------------
# 4. halfplane_steps.svg — Nửa mặt phẳng bờ liền (2x + y <= 4) vs bờ đứt (x - y > 1)
# ---------------------------------------------------------------------------
def gen_halfplane_steps() -> None:
    w, h = 760, 235
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        '<defs>',
        '  <pattern id="hatchRed" width="8" height="8" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">',
        '    <line x1="0" y1="0" x2="0" y2="8" stroke="#EF4444" stroke-width="1.2" stroke-opacity="0.55"/>',
        '  </pattern>',
        '  <clipPath id="clipLeftHP"><rect x="28" y="34" width="320" height="175"/></clipPath>',
        '  <clipPath id="clipRightHP"><rect x="408" y="34" width="320" height="175"/></clipPath>',
        '</defs>',
        '<rect x="4" y="4" width="368" height="227" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>',
        '<rect x="388" y="4" width="368" height="227" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>',
        f'<text x="188" y="23" text-anchor="middle" font-family="{FONT}" font-size="11.2" font-weight="bold" fill="#1E3A8A">a) BPT có dấu “≤”: 2x + y ≤ 4 (Bờ d nét liền, giữ phần chứa O)</text>',
        f'<text x="572" y="23" text-anchor="middle" font-family="{FONT}" font-size="11.2" font-weight="bold" fill="#0F766E">b) BPT ngặt “>”: x - y &gt; 1 (Bờ d nét đứt, gạch phần chứa O)</text>',
    ]
    # Left canvas: 2x + y <= 4 -> hatch 2x + y > 4
    c1 = OxyCanvas(28, 34, 320, 175, -1.5, 4.5, -1.0, 5.0)
    parts.extend(c1.grid_and_axes(1))
    # Polygon for 2x + y >= 4 inside [-2, 5] x [-2, 6]: line from (-1, 6) to (3, -2)
    poly1 = f"{c1.pt(-1, 6)} {c1.pt(5, 6)} {c1.pt(5, -2)} {c1.pt(3, -2)}"
    parts.append(f'<polygon points="{poly1}" fill="url(#hatchRed)" clip-path="url(#clipLeftHP)"/>')
    parts.append(f'<line x1="{c1.px(-1):.1f}" y1="{c1.py(6):.1f}" x2="{c1.px(3):.1f}" y2="{c1.py(-2):.1f}" stroke="#1D4ED8" stroke-width="2.2" clip-path="url(#clipLeftHP)"/>')
    for xv, yv, dx, dy in [(2, 0, -4, 14), (0, 4, -14, 4)]:
        parts.append(f'<circle cx="{c1.px(xv):.1f}" cy="{c1.py(yv):.1f}" r="3" fill="#1D4ED8"/>')
        lbl = str(xv) if yv == 0 else str(yv)
        parts.append(f'<text x="{c1.px(xv)+dx:.1f}" y="{c1.py(yv)+dy:.1f}" font-family="{FONT}" font-size="10.5" font-weight="bold" fill="#1E3A8A">{lbl}</text>')
    parts.append(f'<text x="{c1.px(0.5):.1f}" y="{c1.py(1.3):.1f}" font-family="{FONT}" font-size="10.5" font-weight="bold" fill="#15803D">Miền nghiệm</text>')
    parts.append(f'<text x="188" y="222" text-anchor="middle" font-family="{FONT}" font-size="9.8" fill="#334155">Thay O(0;0): 2·0 + 0 = 0 ≤ 4 (Đúng) ⇒ Giữ nửa mặt phẳng chứa O</text>')

    # Right canvas: x - y > 1 -> hatch x - y <= 1 (which contains O(0,0))
    c2 = OxyCanvas(408, 34, 320, 175, -1.5, 4.5, -2.5, 3.5)
    parts.extend(c2.grid_and_axes(1))
    # Line x - y = 1: (-2, -3) to (5, 4). Side x - y <= 1 has y >= x - 1 (upper-left)
    poly2 = f"{c2.pt(-2, -3)} {c2.pt(-2, 4)} {c2.pt(5, 4)}"
    parts.append(f'<polygon points="{poly2}" fill="url(#hatchRed)" clip-path="url(#clipRightHP)"/>')
    parts.append(f'<line x1="{c2.px(-2):.1f}" y1="{c2.py(-3):.1f}" x2="{c2.px(5):.1f}" y2="{c2.py(4):.1f}" stroke="#0F766E" stroke-width="2.2" stroke-dasharray="6,4" clip-path="url(#clipRightHP)"/>')
    for xv, yv, dx, dy in [(1, 0, 4, 14), (0, -1, -16, 4)]:
        parts.append(f'<circle cx="{c2.px(xv):.1f}" cy="{c2.py(yv):.1f}" r="3" fill="#0F766E"/>')
        lbl = str(xv) if yv == 0 else str(yv)
        parts.append(f'<text x="{c2.px(xv)+dx:.1f}" y="{c2.py(yv)+dy:.1f}" font-family="{FONT}" font-size="10.5" font-weight="bold" fill="#0F766E">{lbl}</text>')
    parts.append(f'<text x="{c2.px(2.4):.1f}" y="{c2.py(-1.2):.1f}" font-family="{FONT}" font-size="10.5" font-weight="bold" fill="#15803D">Miền nghiệm</text>')
    parts.append(f'<text x="572" y="222" text-anchor="middle" font-family="{FONT}" font-size="9.8" fill="#334155">Thay O(0;0): 0 - 0 &gt; 1 (Sai) ⇒ Gạch nửa mặt phẳng chứa O, bờ đứt</text>')

    parts.append("</svg>")
    save_svg("halfplane_steps.svg", "\n".join(parts))


# ---------------------------------------------------------------------------
# 5. lp_feasible_theory.svg — Miền đa giác nghiệm OABC cho bài toán Quy hoạch tuyến tính
# ---------------------------------------------------------------------------
def gen_lp_feasible_theory() -> None:
    # System: x >= 0, y >= 0, x + 2y <= 8, 2x + y <= 10 -> vertices O(0,0), A(0,4), B(4,2), C(5,0)
    w, h = 760, 225
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        '<rect x="2" y="2" width="756" height="221" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>',
        '<clipPath id="clipLP"><rect x="30" y="22" width="380" height="185"/></clipPath>',
    ]
    c = OxyCanvas(30, 22, 380, 185, -1.0, 9.0, -1.0, 6.5)
    parts.extend(c.grid_and_axes(1))
    # Feasible polygon O(0,0) - A(0,4) - B(4,2) - C(5,0)
    poly = f"{c.pt(0,0)} {c.pt(0,4)} {c.pt(4,2)} {c.pt(5,0)}"
    parts.append(f'<polygon points="{poly}" fill="#3B82F6" fill-opacity="0.26" stroke="#1D4ED8" stroke-width="2"/>')
    # Lines d1: x + 2y = 8 -> (-1, 4.5) to (9, -0.5); d2: 2x + y = 10 -> (1.5, 7) to (5.5, -1)
    parts.append(f'<line x1="{c.px(-1):.1f}" y1="{c.py(4.5):.1f}" x2="{c.px(9):.1f}" y2="{c.py(-0.5):.1f}" stroke="#1D4ED8" stroke-width="1.5" clip-path="url(#clipLP)"/>')
    parts.append(f'<line x1="{c.px(1.5):.1f}" y1="{c.py(7):.1f}" x2="{c.px(5.5):.1f}" y2="{c.py(-1):.1f}" stroke="#0F766E" stroke-width="1.5" clip-path="url(#clipLP)"/>')
    for name, xv, yv, dx, dy in [("", 0, 0, 0, 0), ("A(0;4)", 0, 4, 6, -6), ("B(4;2)", 4, 2, 8, -5), ("C(5;0)", 5, 0, 8, -5)]:
        parts.append(f'<circle cx="{c.px(xv):.1f}" cy="{c.py(yv):.1f}" r="3.8" fill="#B91C1C"/>')
        if name:
            parts.append(f'<text x="{c.px(xv)+dx:.1f}" y="{c.py(yv)+dy:.1f}" font-family="{FONT}" font-size="10.2" font-weight="bold" fill="#B91C1C">{name}</text>')
    parts.append(f'<text x="{c.px(6.6):.1f}" y="{c.py(1.3):.1f}" font-family="{FONT}" font-size="9.8" font-weight="bold" fill="#1D4ED8">d₁: x + 2y = 8</text>')
    parts.append(f'<text x="{c.px(2.4):.1f}" y="{c.py(5.5):.1f}" font-family="{FONT}" font-size="9.8" font-weight="bold" fill="#0F766E">d₂: 2x + y = 10</text>')
    parts.append(f'<text x="{c.px(1.3):.1f}" y="{c.py(1.4):.1f}" font-family="{FONT}" font-size="10.5" font-weight="bold" fill="#1E3A8A">Miền OABC</text>')

    # Right explanation card
    parts.extend([
        '<rect x="430" y="20" width="312" height="187" rx="7" fill="#FFFFFF" stroke="#93C5FD" stroke-width="1.2"/>',
        f'<text x="586" y="42" text-anchor="middle" font-family="{FONT}" font-size="11.5" font-weight="bold" fill="#1E3A8A">Minh họa tìm GTLN của F(x; y) = 3x + 4y</text>',
        f'<text x="444" y="64" font-family="{FONT}" font-size="10.2" fill="#334155">Hệ ràng buộc: x ≥ 0; y ≥ 0; x + 2y ≤ 8; 2x + y ≤ 10.</text>',
        f'<text x="444" y="84" font-family="{FONT}" font-size="10.2" fill="#334155">Miền nghiệm là tứ giác lồi OABC với 4 đỉnh:</text>',
        f'<text x="454" y="106" font-family="{FONT}" font-size="10.3" fill="#0F172A">• Tại O(0; 0):   F(0; 0) = 3·0 + 4·0 = 0</text>',
        f'<text x="454" y="126" font-family="{FONT}" font-size="10.3" fill="#0F172A">• Tại A(0; 4):   F(0; 4) = 3·0 + 4·4 = 16</text>',
        f'<text x="454" y="146" font-family="{FONT}" font-size="10.5" font-weight="bold" fill="#B91C1C">• Tại B(4; 2):   F(4; 2) = 3·4 + 4·2 = 20 (MAX)</text>',
        f'<text x="454" y="166" font-family="{FONT}" font-size="10.3" fill="#0F172A">• Tại C(5; 0):   F(5; 0) = 3·5 + 4·0 = 15</text>',
        f'<text x="444" y="192" font-family="{FONT}" font-size="10.2" font-weight="bold" fill="#0F766E">⇒ GTLN của F bằng 20 đạt tại đỉnh B(4; 2).</text>',
        "</svg>",
    ])
    save_svg("lp_feasible_theory.svg", "\n".join(parts))


# ---------------------------------------------------------------------------
# 6. unit_semicircle.svg — Nửa đường tròn đơn vị & Hai góc bù nhau α, 180° - α
# ---------------------------------------------------------------------------
def gen_unit_semicircle() -> None:
    w, h = 760, 210
    cx, cy, R = 230, 172, 130
    ang = math.radians(52)
    mx, my = cx + R * math.cos(ang), cy - R * math.sin(ang)
    nx, ny = cx - R * math.cos(ang), cy - R * math.sin(ang)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        '<rect x="2" y="2" width="756" height="206" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>',
        # Axes
        f'<line x1="65" y1="{cy}" x2="395" y2="{cy}" stroke="#0F172A" stroke-width="1.4"/>',
        f'<polygon points="390,{cy-3.5} 398,{cy} 390,{cy+3.5}" fill="#0F172A"/>',
        f'<line x1="{cx}" y1="194" x2="{cx}" y2="18" stroke="#0F172A" stroke-width="1.4"/>',
        f'<polygon points="{cx-3.5},23 {cx},15 {cx+3.5},23" fill="#0F172A"/>',
        f'<text x="392" y="{cy-8}" font-family="{FONT}" font-size="11" font-weight="bold" font-style="italic" fill="#0F172A">x</text>',
        f'<text x="{cx+8}" y="24" font-family="{FONT}" font-size="11" font-weight="bold" font-style="italic" fill="#0F172A">y</text>',
        # Semicircle
        f'<path d="M {cx-R} {cy} A {R} {R} 0 0 1 {cx+R} {cy}" fill="#EFF6FF" fill-opacity="0.55" stroke="#1D4ED8" stroke-width="2.2"/>',
        # Projections for M and M'
        f'<line x1="{mx:.1f}" y1="{my:.1f}" x2="{mx:.1f}" y2="{cy}" stroke="#1D4ED8" stroke-width="1.2" stroke-dasharray="4,3"/>',
        f'<line x1="{nx:.1f}" y1="{ny:.1f}" x2="{nx:.1f}" y2="{cy}" stroke="#B91C1C" stroke-width="1.2" stroke-dasharray="4,3"/>',
        f'<line x1="{nx:.1f}" y1="{ny:.1f}" x2="{mx:.1f}" y2="{my:.1f}" stroke="#0F766E" stroke-width="1.3" stroke-dasharray="4,3"/>',
        # Rays OM and OM'
        f'<line x1="{cx}" y1="{cy}" x2="{mx:.1f}" y2="{my:.1f}" stroke="#1D4ED8" stroke-width="2"/>',
        f'<line x1="{cx}" y1="{cy}" x2="{nx:.1f}" y2="{ny:.1f}" stroke="#B91C1C" stroke-width="2"/>',
        # Angle arcs
        f'<path d="M {cx+32} {cy} A 32 32 0 0 0 {cx+32*math.cos(ang):.1f} {cy-32*math.sin(ang):.1f}" fill="none" stroke="#1D4ED8" stroke-width="1.5"/>',
        f'<path d="M {cx+46} {cy} A 46 46 0 0 0 {cx-46*math.cos(ang):.1f} {cy-46*math.sin(ang):.1f}" fill="none" stroke="#B91C1C" stroke-width="1.3"/>',
        f'<text x="{cx+36}" y="{cy-12}" font-family="{FONT}" font-size="10.5" font-weight="bold" fill="#1D4ED8">α</text>',
        f'<text x="{cx-32}" y="{cy-38}" font-family="{FONT}" font-size="10" font-weight="bold" fill="#B91C1C">180°-α</text>',
        # Points & labels
        f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="4" fill="#1D4ED8"/>',
        f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="4" fill="#B91C1C"/>',
        f'<circle cx="{cx}" cy="{my:.1f}" r="3.2" fill="#0F766E"/>',
        f'<text x="{mx+7:.1f}" y="{my-4:.1f}" font-family="{FONT}" font-size="10.5" font-weight="bold" fill="#1D4ED8">M(x₀; y₀)</text>',
        f'<text x="{nx-68:.1f}" y="{ny-4:.1f}" font-family="{FONT}" font-size="10.5" font-weight="bold" fill="#B91C1C">M\'(-x₀; y₀)</text>',
        f'<text x="{cx+6}" y="{my-4:.1f}" font-family="{FONT}" font-size="10" font-weight="bold" fill="#0F766E">sin α = y₀</text>',
        f'<text x="{mx-18:.1f}" y="{cy+14}" font-family="{FONT}" font-size="10" font-weight="bold" fill="#1D4ED8">cos α</text>',
        f'<text x="{nx-22:.1f}" y="{cy+14}" font-family="{FONT}" font-size="10" font-weight="bold" fill="#B91C1C">-cos α</text>',
        f'<text x="{cx+R-4}" y="{cy+15}" font-family="{FONT}" font-size="10" font-weight="bold" fill="#0F172A">1</text>',
        f'<text x="{cx-R-10}" y="{cy+15}" font-family="{FONT}" font-size="10" font-weight="bold" fill="#0F172A">-1</text>',
        f'<text x="{cx-12}" y="{cy-R-5}" font-family="{FONT}" font-size="10" font-weight="bold" fill="#0F172A">1</text>',
        f'<text x="{cx-10}" y="{cy+14}" font-family="{FONT}" font-size="10" font-weight="bold" fill="#0F172A">O</text>',
        # Summary card right
        '<rect x="410" y="16" width="336" height="178" rx="7" fill="#FFFFFF" stroke="#93C5FD" stroke-width="1.2"/>',
        f'<text x="578" y="37" text-anchor="middle" font-family="{FONT}" font-size="11.2" font-weight="bold" fill="#1E3A8A">Định nghĩa &amp; Dấu GTLG trên [0°; 180°]</text>',
        f'<text x="422" y="59" font-family="{FONT}" font-size="9.7" fill="#0F172A">• Điểm M(x₀; y₀) trên nửa đường tròn đơn vị:</text>',
        f'<text x="432" y="78" font-family="{FONT}" font-size="9.8" font-weight="bold" fill="#1D4ED8">sin α = y₀ ;  cos α = x₀ ;  tan α = y₀/x₀ ;  cot α = x₀/y₀</text>',
        f'<text x="422" y="101" font-family="{FONT}" font-size="9.7" fill="#15803D">• Góc nhọn (0° &lt; α &lt; 90°): sin, cos, tan, cot đều &gt; 0.</text>',
        f'<text x="422" y="121" font-family="{FONT}" font-size="9.6" font-weight="bold" fill="#B91C1C">• Góc tù (90° &lt; α &lt; 180°): sin α &gt; 0; cos, tan, cot &lt; 0!</text>',
        f'<text x="422" y="145" font-family="{FONT}" font-size="9.7" fill="#0F172A">• Hai góc bù nhau (α và 180° - α) — “Sin bù”:</text>',
        f'<text x="432" y="165" font-family="{FONT}" font-size="9.8" font-weight="bold" fill="#0F766E">sin(180°-α) = sin α ;  cos(180°-α) = -cos α</text>',
        f'<text x="432" y="182" font-family="{FONT}" font-size="9.8" font-weight="bold" fill="#0F766E">tan(180°-α) = -tan α ; cot(180°-α) = -cot α</text>',
        "</svg>",
    ]
    save_svg("unit_semicircle.svg", "\n".join(parts))


# ---------------------------------------------------------------------------
# 7. triangle_theorems.svg — Tam giác ABC với a, b, c, h_a, R, r
# ---------------------------------------------------------------------------
def gen_triangle_theorems() -> None:
    w, h = 760, 205
    # Triangle vertices in pixel coords so entire circumcircle stays inside [14, 188]
    Ax, Ay = 165, 38
    Bx, By = 106, 134
    Cx, Cy = 266, 134
    # Circumcenter & circumcircle of A(155,42), B(85,162), C(285,162)
    D = 2 * (Ax * (By - Cy) + Bx * (Cy - Ay) + Cx * (Ay - By))
    ux = ((Ax**2 + Ay**2) * (By - Cy) + (Bx**2 + By**2) * (Cy - Ay) + (Cx**2 + Cy**2) * (Ay - By)) / D
    uy = ((Ax**2 + Ay**2) * (Cx - Bx) + (Bx**2 + By**2) * (Ax - Cx) + (Cx**2 + Cy**2) * (Bx - Ax)) / D
    R = math.hypot(Ax - ux, Ay - uy)
    # Incenter & inradius
    la = math.hypot(Cx - Bx, Cy - By)
    lb = math.hypot(Ax - Cx, Ay - Cy)
    lc = math.hypot(Ax - Bx, Ay - By)
    ix = (la * Ax + lb * Bx + lc * Cx) / (la + lb + lc)
    iy = (la * Ay + lb * By + lc * Cy) / (la + lb + lc)
    area = 0.5 * abs((Bx - Ax) * (Cy - Ay) - (Cx - Ax) * (By - Ay))
    r_in = 2 * area / (la + lb + lc)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        '<rect x="2" y="2" width="756" height="201" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>',
        # Circumcircle
        f'<circle cx="{ux:.1f}" cy="{uy:.1f}" r="{R:.1f}" fill="#EFF6FF" fill-opacity="0.45" stroke="#93C5FD" stroke-width="1.4" stroke-dasharray="5,3"/>',
        # Incircle
        f'<circle cx="{ix:.1f}" cy="{iy:.1f}" r="{r_in:.1f}" fill="#FEF3C7" fill-opacity="0.55" stroke="#F59E0B" stroke-width="1.3"/>',
        # Altitude AH
        f'<line x1="{Ax}" y1="{Ay}" x2="{Ax}" y2="{By}" stroke="#B91C1C" stroke-width="1.4" stroke-dasharray="4,3"/>',
        f'<rect x="{Ax}" y="{By-9}" width="9" height="9" fill="none" stroke="#B91C1C" stroke-width="1.1"/>',
        # Triangle ABC
        f'<polygon points="{Ax},{Ay} {Bx},{By} {Cx},{Cy}" fill="none" stroke="#1E3A8A" stroke-width="2.1"/>',
        # Radius R from U to C
        f'<line x1="{ux:.1f}" y1="{uy:.1f}" x2="{Cx}" y2="{Cy}" stroke="#1D4ED8" stroke-width="1.2"/>',
        f'<circle cx="{ux:.1f}" cy="{uy:.1f}" r="2.8" fill="#1D4ED8"/>',
        f'<circle cx="{ix:.1f}" cy="{iy:.1f}" r="2.8" fill="#B45309"/>',
        f'<line x1="{ix:.1f}" y1="{iy:.1f}" x2="{ix:.1f}" y2="{By}" stroke="#B45309" stroke-width="1.2"/>',
        # Labels
        f'<text x="{Ax-5}" y="{Ay-8}" font-family="{FONT}" font-size="12" font-weight="bold" fill="#0F172A">A</text>',
        f'<text x="{Bx-15}" y="{By+5}" font-family="{FONT}" font-size="12" font-weight="bold" fill="#0F172A">B</text>',
        f'<text x="{Cx+7}" y="{Cy+5}" font-family="{FONT}" font-size="12" font-weight="bold" fill="#0F172A">C</text>',
        f'<text x="{Ax-4}" y="{By+14}" font-family="{FONT}" font-size="10" font-weight="bold" fill="#B91C1C">H</text>',
        f'<text x="{Ax-18}" y="{(Ay+By)/2+6:.1f}" font-family="{FONT}" font-size="10.5" font-weight="bold" fill="#B91C1C">hₐ</text>',
        f'<text x="110" y="98" font-family="{FONT}" font-size="11" font-weight="bold" fill="#1E3A8A">c</text>',
        f'<text x="228" y="96" font-family="{FONT}" font-size="11" font-weight="bold" fill="#1E3A8A">b</text>',
        f'<text x="195" y="150" font-family="{FONT}" font-size="11" font-weight="bold" fill="#1E3A8A">a</text>',
        f'<text x="{(ux+Cx)/2+4:.1f}" y="{(uy+Cy)/2-4:.1f}" font-family="{FONT}" font-size="10" font-weight="bold" fill="#1D4ED8">R</text>',
        f'<text x="{ix+4:.1f}" y="{(iy+By)/2+3:.1f}" font-family="{FONT}" font-size="10" font-weight="bold" fill="#B45309">r</text>',
        # Right formula summary box
        '<rect x="345" y="14" width="398" height="177" rx="7" fill="#FFFFFF" stroke="#93C5FD" stroke-width="1.2"/>',
        f'<text x="544" y="34" text-anchor="middle" font-family="{FONT}" font-size="11.5" font-weight="bold" fill="#1E3A8A">3 Trụ cột Hệ thức lượng trong tam giác ABC</text>',
        f'<text x="358" y="56" font-family="{FONT}" font-size="10.2" font-weight="bold" fill="#1D4ED8">1. Định lí Côsin:</text>',
        f'<text x="458" y="56" font-family="{FONT}" font-size="10.2" fill="#0F172A">a² = b² + c² - 2bc·cos A  ⇒  cos A = (b²+c²-a²)/(2bc)</text>',
        f'<text x="358" y="80" font-family="{FONT}" font-size="10.2" font-weight="bold" fill="#0F766E">2. Định lí Sin:</text>',
        f'<text x="458" y="80" font-family="{FONT}" font-size="10.2" fill="#0F172A">a / sin A = b / sin B = c / sin C = 2R</text>',
        f'<text x="358" y="104" font-family="{FONT}" font-size="10.2" font-weight="bold" fill="#B45309">3. Năm công thức diện tích S (với p = (a+b+c)/2):</text>',
        f'<text x="368" y="125" font-family="{FONT}" font-size="10.1" fill="#0F172A">• S = ½·a·hₐ = ½·b·h_b = ½·c·h_c</text>',
        f'<text x="368" y="144" font-family="{FONT}" font-size="10.1" fill="#0F172A">• S = ½·b·c·sin A = ½·a·c·sin B = ½·a·b·sin C</text>',
        f'<text x="368" y="163" font-family="{FONT}" font-size="10.1" fill="#0F172A">• S = abc / (4R)   • S = p·r   • Heron: S = √[p(p-a)(p-b)(p-c)]</text>',
        f'<text x="368" y="182" font-family="{FONT}" font-size="9.8" font-weight="bold" fill="#B91C1C">⇒ Suy ra nhanh: hₐ = 2S/a ;  R = abc/(4S) ;  r = S/p</text>',
        "</svg>",
    ]
    save_svg("triangle_theorems.svg", "\n".join(parts))


# ---------------------------------------------------------------------------
# 8. realworld_trig_models.svg — Hai mô hình thực tế kinh điển Câu 2 Tự luận
# ---------------------------------------------------------------------------
def gen_realworld_trig_models() -> None:
    w, h = 760, 200
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        '<rect x="4" y="4" width="368" height="192" rx="8" fill="#EFF6FF" stroke="#93C5FD" stroke-width="1.2"/>',
        '<rect x="388" y="4" width="368" height="192" rx="8" fill="#F0FDFA" stroke="#5EEAD4" stroke-width="1.2"/>',
        # Model 1: Pond obstacle AB
        f'<text x="188" y="23" text-anchor="middle" font-family="{FONT}" font-size="11.2" font-weight="bold" fill="#1E3A8A">Mô hình 1: Đo khoảng cách AB qua vật cản (hồ nước)</text>',
        '<ellipse cx="195" cy="96" rx="68" ry="32" fill="#93C5FD" fill-opacity="0.6" stroke="#3B82F6" stroke-width="1.2"/>',
        f'<text x="195" y="100" text-anchor="middle" font-family="{FONT}" font-size="10" font-style="italic" fill="#1E40AF">Hồ nước</text>',
        '<line x1="95" y1="152" x2="108" y2="68" stroke="#0F172A" stroke-width="1.8"/>',
        '<line x1="95" y1="152" x2="290" y2="112" stroke="#0F172A" stroke-width="1.8"/>',
        '<line x1="108" y1="68" x2="290" y2="112" stroke="#B91C1C" stroke-width="2" stroke-dasharray="6,4"/>',
        '<circle cx="95" cy="152" r="3.5" fill="#0F172A"/>',
        '<circle cx="108" cy="68" r="3.5" fill="#B91C1C"/>',
        '<circle cx="290" cy="112" r="3.5" fill="#B91C1C"/>',
        f'<text x="76" y="162" font-family="{FONT}" font-size="11" font-weight="bold" fill="#0F172A">C</text>',
        f'<text x="90" y="63" font-family="{FONT}" font-size="11" font-weight="bold" fill="#B91C1C">A</text>',
        f'<text x="297" y="116" font-family="{FONT}" font-size="11" font-weight="bold" fill="#B91C1C">B</text>',
        f'<text x="78" y="112" font-family="{FONT}" font-size="10" font-weight="bold" fill="#1E3A8A">b</text>',
        f'<text x="196" y="147" font-family="{FONT}" font-size="10" font-weight="bold" fill="#1E3A8A">a</text>',
        f'<text x="115" y="140" font-family="{FONT}" font-size="10" font-weight="bold" fill="#B45309">∠C</text>',
        f'<text x="188" y="183" text-anchor="middle" font-family="{FONT}" font-size="10" font-weight="bold" fill="#0F172A">Đo CA = b, CB = a, góc C ⇒ AB = √(a² + b² - 2ab·cos C)</text>',
        # Model 2: Tower height from 2 points A, B
        f'<text x="572" y="23" text-anchor="middle" font-family="{FONT}" font-size="11.2" font-weight="bold" fill="#0F766E">Mô hình 2: Đo chiều cao tháp CH từ 2 vị trí ngắm A, B</text>',
        '<line x1="415" y1="152" x2="725" y2="152" stroke="#334155" stroke-width="1.6"/>',
        # Tower CH at x = 685, top C(685, 48), H(685, 152)
        '<rect x="678" y="48" width="14" height="104" fill="#CBD5E1" stroke="#475569" stroke-width="1.3"/>',
        '<line x1="685" y1="36" x2="685" y2="48" stroke="#B91C1C" stroke-width="2"/>',
        '<rect x="676" y="143" width="9" height="9" fill="none" stroke="#B91C1C" stroke-width="1.1"/>',
        # Points A(445, 152), B(555, 152) -> C(685, 48)
        '<line x1="445" y1="152" x2="685" y2="48" stroke="#1D4ED8" stroke-width="1.7"/>',
        '<line x1="555" y1="152" x2="685" y2="48" stroke="#0F766E" stroke-width="1.7"/>',
        '<circle cx="445" cy="152" r="3.5" fill="#1D4ED8"/>',
        '<circle cx="555" cy="152" r="3.5" fill="#0F766E"/>',
        '<circle cx="685" cy="48" r="3.5" fill="#B91C1C"/>',
        f'<text x="440" y="167" font-family="{FONT}" font-size="11" font-weight="bold" fill="#1D4ED8">A</text>',
        f'<text x="550" y="167" font-family="{FONT}" font-size="11" font-weight="bold" fill="#0F766E">B</text>',
        f'<text x="682" y="167" font-family="{FONT}" font-size="11" font-weight="bold" fill="#0F172A">H</text>',
        f'<text x="694" y="50" font-family="{FONT}" font-size="11" font-weight="bold" fill="#B91C1C">C</text>',
        f'<text x="478" y="148" font-family="{FONT}" font-size="10" font-weight="bold" fill="#1D4ED8">α</text>',
        f'<text x="582" y="148" font-family="{FONT}" font-size="10" font-weight="bold" fill="#0F766E">β</text>',
        f'<text x="500" y="167" text-anchor="middle" font-family="{FONT}" font-size="10" font-weight="bold" fill="#B45309">d = AB</text>',
        f'<text x="702" y="106" font-family="{FONT}" font-size="10.5" font-weight="bold" fill="#B91C1C">h</text>',
        f'<text x="572" y="185" text-anchor="middle" font-family="{FONT}" font-size="9.8" font-weight="bold" fill="#0F172A">∠ACB = β - α ⇒ Định lí Sin trong ΔABC tìm BC ⇒ h = BC·sin β</text>',
        "</svg>",
    ]
    save_svg("realworld_trig_models.svg", "\n".join(parts))


# ---------------------------------------------------------------------------
# 9. vector_concepts_hex.svg — Hình bình hành ABCD & Lục giác đều ABCDEF tâm O
# ---------------------------------------------------------------------------
def gen_vector_concepts_hex() -> None:
    w, h = 760, 200
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        '<defs>',
        '  <marker id="arrBlue" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">',
        '    <polygon points="0,1 8,4 0,7" fill="#1D4ED8"/>',
        '  </marker>',
        '  <marker id="arrRed" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">',
        '    <polygon points="0,1 8,4 0,7" fill="#B91C1C"/>',
        '  </marker>',
        '</defs>',
        '<rect x="4" y="4" width="356" height="192" rx="8" fill="#EFF6FF" stroke="#93C5FD" stroke-width="1.2"/>',
        '<rect x="372" y="4" width="384" height="192" rx="8" fill="#F0FDFA" stroke="#5EEAD4" stroke-width="1.2"/>',
        # Left: Parallelogram ABCD tâm O
        f'<text x="182" y="24" text-anchor="middle" font-family="{FONT}" font-size="11.2" font-weight="bold" fill="#1E3A8A">a) Hình bình hành ABCD tâm O</text>',
        '<polygon points="85,62 255,62 295,146 125,146" fill="#FFFFFF" stroke="#64748B" stroke-width="1.3"/>',
        '<line x1="85" y1="62" x2="295" y2="146" stroke="#CBD5E1" stroke-width="1.1" stroke-dasharray="4,3"/>',
        '<line x1="255" y1="62" x2="125" y2="146" stroke="#CBD5E1" stroke-width="1.1" stroke-dasharray="4,3"/>',
        '<line x1="85" y1="62" x2="253" y2="62" stroke="#1D4ED8" stroke-width="2.2" marker-end="url(#arrBlue)"/>',
        '<line x1="125" y1="146" x2="293" y2="146" stroke="#1D4ED8" stroke-width="2.2" marker-end="url(#arrBlue)"/>',
        '<circle cx="190" cy="104" r="3.2" fill="#B91C1C"/>',
        f'<text x="70" y="60" font-family="{FONT}" font-size="11.5" font-weight="bold" fill="#0F172A">A</text>',
        f'<text x="260" y="60" font-family="{FONT}" font-size="11.5" font-weight="bold" fill="#0F172A">B</text>',
        f'<text x="301" y="150" font-family="{FONT}" font-size="11.5" font-weight="bold" fill="#0F172A">C</text>',
        f'<text x="108" y="150" font-family="{FONT}" font-size="11.5" font-weight="bold" fill="#0F172A">D</text>',
        f'<text x="186" y="96" font-family="{FONT}" font-size="10.5" font-weight="bold" fill="#B91C1C">O</text>',
        f'<text x="182" y="180" text-anchor="middle" font-family="{FONT}" font-size="10" font-weight="bold" fill="#1E3A8A">AB = DC ;  AD = BC ;  AO = OC ;  BO = OD (Chú ý thứ tự đỉnh!)</text>',
    ]
    # Right: Regular hexagon ABCDEF center O
    parts.append(f'<text x="564" y="24" text-anchor="middle" font-family="{FONT}" font-size="11.2" font-weight="bold" fill="#0F766E">b) Lục giác đều ABCDEF tâm O (Đề rất hay hỏi!)</text>')
    cx, cy, R = 468, 108, 58
    # Vertices: A top-left (-120 deg in SVG y-down -> 240?), let's make AB horizontal on top!
    # Top edge A -> B: A at 120 deg math, B at 60 deg math, C at 0, D at -60, E at -120, F at 180
    angs = [120, 60, 0, -60, -120, 180]
    names = ["A", "B", "C", "D", "E", "F"]
    pts = [(cx + R * math.cos(math.radians(a)), cy - R * math.sin(math.radians(a))) for a in angs]
    poly_pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    parts.append(f'<polygon points="{poly_pts}" fill="#FFFFFF" stroke="#64748B" stroke-width="1.4"/>')
    for i in range(3):
        x1, y1 = pts[i]
        x2, y2 = pts[i + 3]
        parts.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#CBD5E1" stroke-width="1.1"/>')
    # Highlight 4 equal vectors: AB, FO, OC, ED
    equal_segs = [
        (pts[0], pts[1]),       # A -> B
        (pts[5], (cx, cy)),     # F -> O
        ((cx, cy), pts[2]),     # O -> C
        (pts[4], pts[3]),       # E -> D
    ]
    for (x1, y1), (x2, y2) in equal_segs:
        parts.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#B91C1C" stroke-width="2.2" marker-end="url(#arrRed)"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="3.2" fill="#0F172A"/>')
    parts.append(f'<text x="{cx-4}" y="{cy-8}" font-family="{FONT}" font-size="10.5" font-weight="bold" fill="#0F172A">O</text>')
    offsets = [(-12, -6), (6, -6), (8, 4), (6, 14), (-14, 14), (-16, 4)]
    for (x, y), nm, (dx, dy) in zip(pts, names, offsets):
        parts.append(f'<text x="{x+dx:.1f}" y="{y+dy:.1f}" font-family="{FONT}" font-size="11" font-weight="bold" fill="#0F172A">{nm}</text>')
    # Text notes on right of hexagon
    parts.extend([
        f'<text x="556" y="66" font-family="{FONT}" font-size="9.8" font-weight="bold" fill="#B91C1C">• Bằng vectơ AB (3 vectơ):</text>',
        f'<text x="566" y="84" font-family="{FONT}" font-size="9.8" fill="#0F172A">FO ,  OC ,  ED</text>',
        f'<text x="556" y="108" font-family="{FONT}" font-size="9.8" font-weight="bold" fill="#0F766E">• Cùng phương AB (khác 0):</text>',
        f'<text x="566" y="125" font-family="{FONT}" font-size="9.6" fill="#0F172A">9 vectơ trên AB, FC, ED</text>',
        f'<text x="566" y="141" font-family="{FONT}" font-size="8.9" fill="#475569">(BA, FO, OF, OC, CO, FC, CF, ED, DE)</text>',
        f'<text x="556" y="168" font-family="{FONT}" font-size="9.6" font-weight="bold" fill="#1E3A8A">• Vectơ 0 cùng hướng mọi vectơ!</text>',
        "</svg>",
    ])
    save_svg("vector_concepts_hex.svg", "\n".join(parts))


# ---------------------------------------------------------------------------
# 10 & 11. bank_bpt_graph1.svg & bank_bpt_graph2.svg — Đồ thị cho Ngân hàng câu hỏi
# ---------------------------------------------------------------------------
def gen_bank_bpt_graphs() -> None:
    # Graph 1: Unshaded region for 3x + 2y <= 6 (boundary passes through (2,0) and (0,3), solid line, keeps O)
    w, h = 340, 215
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        '<defs>',
        '  <pattern id="hG1" width="7" height="7" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">',
        '    <line x1="0" y1="0" x2="0" y2="7" stroke="#64748B" stroke-width="1.3" stroke-opacity="0.65"/>',
        '  </pattern>',
        '  <clipPath id="cG1"><rect x="20" y="14" width="300" height="185"/></clipPath>',
        '</defs>',
        '<rect x="2" y="2" width="336" height="211" rx="7" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.1"/>',
    ]
    c = OxyCanvas(20, 14, 300, 185, -1.5, 4.0, -1.0, 4.5)
    parts.extend(c.grid_and_axes(1))
    # Hatch 3x + 2y > 6: line from (-1, 4.5) to (3, -1.5)
    poly = f"{c.pt(-1, 4.5)} {c.pt(4.5, 4.5)} {c.pt(4.5, -1.5)} {c.pt(3, -1.5)}"
    parts.append(f'<polygon points="{poly}" fill="url(#hG1)" clip-path="url(#cG1)"/>')
    parts.append(f'<line x1="{c.px(-1):.1f}" y1="{c.py(4.5):.1f}" x2="{c.px(3):.1f}" y2="{c.py(-1.5):.1f}" stroke="#1D4ED8" stroke-width="2.1" clip-path="url(#cG1)"/>')
    parts.append(f'<circle cx="{c.px(2):.1f}" cy="{c.py(0):.1f}" r="3" fill="#1D4ED8"/>')
    parts.append(f'<circle cx="{c.px(0):.1f}" cy="{c.py(3):.1f}" r="3" fill="#1D4ED8"/>')
    parts.append(f'<text x="{c.px(2)-4:.1f}" y="{c.py(0)+15:.1f}" font-family="{FONT}" font-size="10.5" font-weight="bold" fill="#1E3A8A">2</text>')
    parts.append(f'<text x="{c.px(0)-13:.1f}" y="{c.py(3)+4:.1f}" font-family="{FONT}" font-size="10.5" font-weight="bold" fill="#1E3A8A">3</text>')
    parts.append("</svg>")
    save_svg("bank_bpt_graph1.svg", "\n".join(parts))

    # Graph 2: Unshaded region for x - 2y < 2 -> boundary x - 2y = 2 passes through (2,0) and (0,-1), dashed line, keeps O(0,0)!
    parts2 = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        '<defs>',
        '  <pattern id="hG2" width="7" height="7" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">',
        '    <line x1="0" y1="0" x2="0" y2="7" stroke="#64748B" stroke-width="1.3" stroke-opacity="0.65"/>',
        '  </pattern>',
        '  <clipPath id="cG2"><rect x="20" y="14" width="300" height="185"/></clipPath>',
        '</defs>',
        '<rect x="2" y="2" width="336" height="211" rx="7" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.1"/>',
    ]
    c2 = OxyCanvas(20, 14, 300, 185, -1.5, 4.0, -2.5, 2.5)
    parts2.extend(c2.grid_and_axes(1))
    # Hatch x - 2y >= 2 (below-right of line y = 0.5x - 1): from (-2, -2) to (4.5, 1.25)
    poly2 = f"{c2.pt(-2, -2)} {c2.pt(4.5, 1.25)} {c2.pt(4.5, -3)} {c2.pt(-2, -3)}"
    parts2.append(f'<polygon points="{poly2}" fill="url(#hG2)" clip-path="url(#cG2)"/>')
    parts2.append(f'<line x1="{c2.px(-2):.1f}" y1="{c2.py(-2):.1f}" x2="{c2.px(4.5):.1f}" y2="{c2.py(1.25):.1f}" stroke="#0F766E" stroke-width="2.1" stroke-dasharray="6,4" clip-path="url(#cG2)"/>')
    parts2.append(f'<circle cx="{c2.px(2):.1f}" cy="{c2.py(0):.1f}" r="3" fill="#0F766E"/>')
    parts2.append(f'<circle cx="{c2.px(0):.1f}" cy="{c2.py(-1):.1f}" r="3" fill="#0F766E"/>')
    parts2.append(f'<text x="{c2.px(2)-3:.1f}" y="{c2.py(0)-7:.1f}" font-family="{FONT}" font-size="10.5" font-weight="bold" fill="#0F766E">2</text>')
    parts2.append(f'<text x="{c2.px(0)-17:.1f}" y="{c2.py(-1)+4:.1f}" font-family="{FONT}" font-size="10.5" font-weight="bold" fill="#0F766E">-1</text>')
    parts2.append("</svg>")
    save_svg("bank_bpt_graph2.svg", "\n".join(parts2))


# ---------------------------------------------------------------------------
# 12, 13, 14. exam1_lp_solution.svg, exam2_lp_solution.svg, exam3_lp_solution.svg
# ---------------------------------------------------------------------------
def gen_exam_lp_solutions() -> None:
    # Exam 1 LP: Workshop producing type I (x) and type II (y):
    # x >= 0, y >= 0, 2x + y <= 16 (machine hours), x + 3y <= 18 (raw material kg)
    # Vertices: O(0,0), A(0,6), B(6,4), C(8,0). Profit F(x,y) = 5x + 4y (million VND) -> Max at B(6,4) = 46!
    w, h = 420, 225
    parts1 = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        '<clipPath id="cE1"><rect x="30" y="16" width="372" height="192"/></clipPath>',
        '<rect x="2" y="2" width="416" height="221" rx="7" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.1"/>',
    ]
    c1 = OxyCanvas(30, 16, 372, 192, -1.5, 19.5, -1.5, 17.5)
    parts1.extend(c1.grid_and_axes(2))
    poly1 = f"{c1.pt(0,0)} {c1.pt(0,6)} {c1.pt(6,4)} {c1.pt(8,0)}"
    parts1.append(f'<polygon points="{poly1}" fill="#3B82F6" fill-opacity="0.28" stroke="#1D4ED8" stroke-width="2"/>')
    parts1.append(f'<line x1="{c1.px(-0.5):.1f}" y1="{c1.py(17):.1f}" x2="{c1.px(8.75):.1f}" y2="{c1.py(-1.5):.1f}" stroke="#1D4ED8" stroke-width="1.5" clip-path="url(#cE1)"/>')
    parts1.append(f'<line x1="{c1.px(-1.5):.1f}" y1="{c1.py(6.5):.1f}" x2="{c1.px(19.5):.1f}" y2="{c1.py(-0.5):.1f}" stroke="#0F766E" stroke-width="1.5" clip-path="url(#cE1)"/>')
    for nm, xv, yv, dx, dy in [("", 0, 0, 0, 0), ("A(0;6)", 0, 6, 6, -5), ("B(6;4)", 6, 4, 7, -5), ("C(8;0)", 8, 0, 6, -5)]:
        parts1.append(f'<circle cx="{c1.px(xv):.1f}" cy="{c1.py(yv):.1f}" r="3.5" fill="#B91C1C"/>')
        if nm:
            parts1.append(f'<text x="{c1.px(xv)+dx:.1f}" y="{c1.py(yv)+dy:.1f}" font-family="{FONT}" font-size="9.8" font-weight="bold" fill="#B91C1C">{nm}</text>')
    parts1.append(f'<text x="{c1.px(2.4):.1f}" y="{c1.py(12.2):.1f}" font-family="{FONT}" font-size="9.5" font-weight="bold" fill="#1D4ED8">2x + y = 16</text>')
    parts1.append(f'<text x="{c1.px(11.0):.1f}" y="{c1.py(3.0):.1f}" font-family="{FONT}" font-size="9.5" font-weight="bold" fill="#0F766E">x + 3y = 18</text>')
    parts1.append("</svg>")
    save_svg("exam1_lp_solution.svg", "\n".join(parts1))

    # Exam 2 LP: Farm renting large trucks (x) and small trucks (y):
    # 0 <= x <= 10, 0 <= y <= 9, 5x + 3y >= 45 (450 pigs / 10), 5x + y >= 35 (35 tons feed)
    # Wait: let's check vertices of {0<=x<=10, 0<=y<=9, 5x+3y>=45, 5x+y>=35}:
    # Intersection of y=9 and 5x+y=35 -> x = 26/5 = 5.2 -> let's pick cleaner integer vertices!
    # Clean integer truck problem:
    # 0 <= x <= 12, 0 <= y <= 10, 5x + 3y >= 45, 5x + y >= 35:
    # - y = 10 in 5x + y = 35 -> x = 5! Check 5(5) + 3(10) = 55 >= 45! Vertex M(5, 10)!
    # - Intersection of 5x + 3y = 45 and 5x + y = 35 -> 2y = 10 -> y = 5, 5x = 30 -> x = 6! Vertex A(6, 5)!
    # - y = 0 in 5x + 3y = 45 -> x = 9! Check 5(9) + 0 = 45 >= 35! Vertex B(9, 0)!
    # - x = 12, y = 0 -> C(12, 0); x = 12, y = 10 -> D(12, 10)!
    # ALL 5 VERTICES ARE INTEGERS: M(5;10), A(6;5), B(9;0), C(12;0), D(12;10)!!
    # Cost F(x,y) = 4x + 2y (million VND):
    # F(5,10)=40, F(6,5)=34 (MIN!), F(9,0)=36, F(12,0)=48, F(12,10)=68!
    parts2 = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        '<clipPath id="cE2"><rect x="30" y="16" width="372" height="192"/></clipPath>',
        '<rect x="2" y="2" width="416" height="221" rx="7" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.1"/>',
    ]
    c2 = OxyCanvas(30, 16, 372, 192, -1.0, 14.0, -1.5, 12.5)
    parts2.extend(c2.grid_and_axes(2))
    poly2 = f"{c2.pt(5,10)} {c2.pt(6,5)} {c2.pt(9,0)} {c2.pt(12,0)} {c2.pt(12,10)}"
    parts2.append(f'<polygon points="{poly2}" fill="#10B981" fill-opacity="0.26" stroke="#0F766E" stroke-width="2"/>')
    # Lines: 5x + y = 35 -> (4.6, 12) to (7.3, -1.5); 5x + 3y = 45 -> (1.8, 12) to (9.9, -1.5); x=12; y=10
    parts2.append(f'<line x1="{c2.px(4.5):.1f}" y1="{c2.py(12.5):.1f}" x2="{c2.px(7.3):.1f}" y2="{c2.py(-1.5):.1f}" stroke="#1D4ED8" stroke-width="1.4" clip-path="url(#cE2)"/>')
    parts2.append(f'<line x1="{c2.px(1.5):.1f}" y1="{c2.py(12.5):.1f}" x2="{c2.px(9.9):.1f}" y2="{c2.py(-1.5):.1f}" stroke="#B45309" stroke-width="1.4" clip-path="url(#cE2)"/>')
    parts2.append(f'<line x1="{c2.px(12):.1f}" y1="{c2.py(-1.5):.1f}" x2="{c2.px(12):.1f}" y2="{c2.py(12.5):.1f}" stroke="#6D28D9" stroke-width="1.3" stroke-dasharray="4,3" clip-path="url(#cE2)"/>')
    parts2.append(f'<line x1="{c2.px(-1):.1f}" y1="{c2.py(10):.1f}" x2="{c2.px(14):.1f}" y2="{c2.py(10):.1f}" stroke="#6D28D9" stroke-width="1.3" stroke-dasharray="4,3" clip-path="url(#cE2)"/>')
    for nm, xv, yv, dx, dy in [
        ("M(5;10)", 5, 10, -44, -5),
        ("A(6;5)", 6, 5, -42, 4),
        ("B(9;0)", 9, 0, -18, 15),
        ("C(12;0)", 12, 0, 4, 15),
        ("D(12;10)", 12, 10, 4, -5),
    ]:
        parts2.append(f'<circle cx="{c2.px(xv):.1f}" cy="{c2.py(yv):.1f}" r="3.4" fill="#B91C1C"/>')
        parts2.append(f'<text x="{c2.px(xv)+dx:.1f}" y="{c2.py(yv)+dy:.1f}" font-family="{FONT}" font-size="9.5" font-weight="bold" fill="#B91C1C">{nm}</text>')
    parts2.append("</svg>")
    save_svg("exam2_lp_solution.svg", "\n".join(parts2))

    # Exam 3 LP: Cooperative growing dragon fruit (x ha) and mango (y ha):
    # x >= 0, y >= 0, x + y <= 8 (land), 2x + 3y <= 20 (200 workdays / 10), x <= 6
    # Wait: check intersections:
    # - x=0 -> y <= 20/3? Let's make ALL vertices clean integers!
    # Try: x >= 0, y >= 0, x + y <= 10 (10 ha), 2x + 3y <= 24 (240 công -> 20 công/ha & 30 công/ha), x <= 8!
    # Check vertices of {0 <= x <= 8, y >= 0, x + y <= 10, 2x + 3y <= 24}:
    # - O(0, 0)
    # - A(0, 8) (since 3*8 = 24, 0+8 <= 10!)
    # - Intersection of x + y = 10 and 2x + 3y = 24: 2(10-y) + 3y = 24 -> y = 4, x = 6! Vertex B(6, 4)!
    # - Intersection of x = 8 and x + y = 10: y = 2! Check 2(8)+3(2)=22 <= 24! Vertex C(8, 2)!
    # - Intersection of x = 8 and y = 0: Vertex D(8, 0)!
    # ALL 5 VERTICES ARE EXACT INTEGERS: O(0;0), A(0;8), B(6;4), C(8;2), D(8;0)!
    # Profit F(x,y) = 30x + 40y (million VND):
    # F(0,0)=0, F(0,8)=320, F(6,4)=340 (MAX!), F(8,2)=320, F(8,0)=240!
    parts3 = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        '<clipPath id="cE3"><rect x="30" y="16" width="372" height="192"/></clipPath>',
        '<rect x="2" y="2" width="416" height="221" rx="7" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.1"/>',
    ]
    c3 = OxyCanvas(30, 16, 372, 192, -1.2, 13.0, -1.2, 11.2)
    parts3.extend(c3.grid_and_axes(2))
    poly3 = f"{c3.pt(0,0)} {c3.pt(0,8)} {c3.pt(6,4)} {c3.pt(8,2)} {c3.pt(8,0)}"
    parts3.append(f'<polygon points="{poly3}" fill="#F59E0B" fill-opacity="0.28" stroke="#B45309" stroke-width="2"/>')
    parts3.append(f'<line x1="{c3.px(-1):.1f}" y1="{c3.py(11):.1f}" x2="{c3.px(11.2):.1f}" y2="{c3.py(-1.2):.1f}" stroke="#1D4ED8" stroke-width="1.4" clip-path="url(#cE3)"/>')
    parts3.append(f'<line x1="{c3.px(-1.2):.1f}" y1="{c3.py(8.8):.1f}" x2="{c3.px(12.5):.1f}" y2="{c3.py(-0.33):.1f}" stroke="#0F766E" stroke-width="1.4" clip-path="url(#cE3)"/>')
    parts3.append(f'<line x1="{c3.px(8):.1f}" y1="{c3.py(-1.2):.1f}" x2="{c3.px(8):.1f}" y2="{c3.py(11.2):.1f}" stroke="#6D28D9" stroke-width="1.4" stroke-dasharray="4,3" clip-path="url(#cE3)"/>')
    for nm, xv, yv, dx, dy in [
        ("", 0, 0, 0, 0),
        ("A(0;8)", 0, 8, 6, -4),
        ("B(6;4)", 6, 4, 6, -5),
        ("C(8;2)", 8, 2, 6, -2),
        ("D(8;0)", 8, 0, 6, 14),
    ]:
        parts3.append(f'<circle cx="{c3.px(xv):.1f}" cy="{c3.py(yv):.1f}" r="3.4" fill="#B91C1C"/>')
        if nm:
            parts3.append(f'<text x="{c3.px(xv)+dx:.1f}" y="{c3.py(yv)+dy:.1f}" font-family="{FONT}" font-size="9.5" font-weight="bold" fill="#B91C1C">{nm}</text>')
    parts3.append("</svg>")
    save_svg("exam3_lp_solution.svg", "\n".join(parts3))


def main() -> None:
    gen_venn_operations()
    gen_number_line_intervals()
    gen_venn_counting_model()
    gen_halfplane_steps()
    gen_lp_feasible_theory()
    gen_unit_semicircle()
    gen_triangle_theorems()
    gen_realworld_trig_models()
    gen_vector_concepts_hex()
    gen_bank_bpt_graphs()
    gen_exam_lp_solutions()
    print("All 14 SVG assets generated successfully.")


if __name__ == "__main__":
    main()
