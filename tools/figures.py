# -*- coding: utf-8 -*-
"""Các hình vẽ minh hoạ (vector) dựng bằng ReportLab: sắc nét ở mọi độ phóng."""
from __future__ import annotations

import math

from reportlab.graphics.shapes import Circle, Drawing, Line, Polygon, String
from reportlab.lib import colors
from reportlab.platypus import Flowable

from pdfkit import BLUE, FONT, FONT_B, FONT_I, GOLD, GREY, INK, NAVY, RED, TEAL

WHITE = colors.white
FILL_BLUE = colors.HexColor("#EAF1F8")
FILL_GOLD = colors.HexColor("#FCF4DF")
FILL_INTER = colors.HexColor("#B7CFE4")
FILL_GREEN = colors.HexColor("#CFE3D4")
GRIDC = colors.HexColor("#ECEFF3")


def _txt(d, x, y, s, size=9, font=FONT, color=INK, anchor="middle"):
    t = String(x, y, s, fontName=font, fontSize=size, fillColor=color)
    t.textAnchor = anchor
    d.add(t)
    return t


# ==========================================================================
# Venn (dùng clip path -> vùng giao chính xác)
# ==========================================================================
class _Venn(Flowable):
    """Biểu đồ Ven hai tập hợp, có thể chú thích vùng được tô."""

    def __init__(self, width=300, height=160, mode="intersection",
                 caption="", note=""):
        super().__init__()
        self.width, self.height = width, height
        self.mode, self.caption, self.note = mode, caption, note

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        top = 16 if self.caption else 6
        r = min((h - top - 12) / 2.0, w * 0.285)
        cy = h - top - r - 2
        xa, xb = w / 2 - r * 0.46, w / 2 + r * 0.46
        c.saveState()

        def fill(x, y, rad, col):
            c.setFillColor(col)
            c.circle(x, y, rad, stroke=0, fill=1)

        def clip(x, y, rad):
            p = c.beginPath()
            p.circle(x, y, rad)
            c.clipPath(p, stroke=0, fill=0)

        if self.mode == "intersection":
            fill(xa, cy, r, FILL_BLUE)
            fill(xb, cy, r, FILL_GOLD)
            c.saveState(); clip(xa, cy, r); fill(xb, cy, r, FILL_INTER); c.restoreState()
            c.saveState(); clip(xb, cy, r); fill(xa, cy, r, FILL_BLUE); c.restoreState()
        elif self.mode == "union":
            fill(xa, cy, r, FILL_INTER)
            fill(xb, cy, r, FILL_INTER)
        elif self.mode == "only_a":
            fill(xa, cy, r, FILL_BLUE)
            fill(xb, cy, r, WHITE)
            c.saveState(); clip(xa, cy, r); fill(xb, cy, r, WHITE); c.restoreState()
        else:
            fill(xa, cy, r, FILL_BLUE)
            fill(xb, cy, r, FILL_GOLD)

        c.setLineWidth(1.1)
        c.setStrokeColor(BLUE)
        c.circle(xa, cy, r, stroke=1, fill=0)
        c.setStrokeColor(GOLD)
        c.circle(xb, cy, r, stroke=1, fill=0)

        c.setFont(FONT_B, max(7.5, min(10.5, r * 0.30)))
        c.setFillColor(BLUE)
        c.drawString(xa - r * 0.66, cy - r * 0.14, "A")
        c.setFillColor(GOLD)
        c.drawString(xb + r * 0.50, cy - r * 0.14, "B")

        if self.note:
            c.setFont(FONT_B, max(6.5, min(8.4, r * 0.22)))
            c.setFillColor(NAVY)
            c.drawCentredString(w / 2, cy - r * 0.16, self.note)
        if self.caption:
            c.setFont(FONT_I, 7.5)
            c.setFillColor(GREY)
            c.drawCentredString(w / 2, 4, self.caption)
        c.restoreState()


def venn_intersection(width=280, height=135, note="A ∩ B",
                      caption="Vùng tô màu: A ∩ B"):
    """note=None, caption=None khi dùng trong đề (tránh lộ đáp án)."""
    return _Venn(width, height, "intersection", caption or "", note or "")


def venn_union(width=280, height=135):
    return _Venn(width, height, "union", "Vùng tô màu: A ∪ B", "")


def venn_difference(width=280, height=135):
    return _Venn(width, height, "only_a", "Vùng tô màu: A \\ B", "")


# ==========================================================================
# Trục số biểu diễn khoảng, đoạn
# ==========================================================================
def number_line(width=430, height=86, marks=(), intervals=(),
                xmin=-4.4, xmax=5.4, caption=""):
    """intervals: [(a|None, b|None, kín_trái, kín_phải, màu, nhãn, hàng)]"""
    d = Drawing(width, height)
    pad, y0 = 26, 26
    scale = (width - 2 * pad) / (xmax - xmin)

    def X(v):
        return pad + (v - xmin) * scale

    d.add(Line(pad - 14, y0, width - pad + 14, y0, strokeColor=INK, strokeWidth=0.9))
    d.add(Polygon([width - pad + 16, y0, width - pad + 5, y0 + 3.2,
                   width - pad + 5, y0 - 3.2], fillColor=INK, strokeColor=INK))
    d.add(Polygon([pad - 16, y0, pad - 5, y0 + 3.2, pad - 5, y0 - 3.2],
                  fillColor=INK, strokeColor=INK))
    for v, lab in marks:
        d.add(Line(X(v), y0 - 3.5, X(v), y0 + 3.5, strokeColor=INK, strokeWidth=0.9))
        _txt(d, X(v), y0 - 13, lab, 8.2, FONT, INK)

    for (a, b, ca, cb, col, lab, row) in intervals:
        yb = y0 + 20 + row * 16
        x1 = X(a) if a is not None else pad - 12
        x2 = X(b) if b is not None else width - pad + 12
        d.add(Line(x1, yb, x2, yb, strokeColor=col, strokeWidth=3.2))
        for xv, cl in ((x1, ca), (x2, cb)):
            if cl is None:
                continue
            if cl:
                d.add(Circle(xv, yb, 3.0, fillColor=col, strokeColor=col))
            else:
                d.add(Circle(xv, yb, 3.0, fillColor=WHITE, strokeColor=col,
                             strokeWidth=1.1))
        if lab:
            _txt(d, x2 + 7 if b is not None else x1 + 7, yb + 4, lab, 7.8, FONT_B, col,
                 anchor="start")
    if caption:
        _txt(d, width / 2, 5, caption, 7.4, FONT_I, GREY)
    return d


# ==========================================================================
# Miền nghiệm của hệ bất phương trình (bài toán tối ưu)
# ==========================================================================
def feasible_region(width=330, height=290, xmax=58, ymax=46,
                    caption="Hình 4. Miền nghiệm là tứ giác OABC"):
    d = Drawing(width, height)
    left, bottom = 44, 40
    pw, ph = width - left - 26, height - bottom - 30
    sx, sy = pw / xmax, ph / ymax

    def X(v):
        return left + v * sx

    def Y(v):
        return bottom + v * sy

    for gx in range(0, int(xmax) + 1, 10):
        d.add(Line(X(gx), bottom, X(gx), bottom + ph, strokeColor=GRIDC, strokeWidth=0.5))
        if gx:
            _txt(d, X(gx), bottom - 11, str(gx), 6.6, FONT, GREY)
    for gy in range(0, int(ymax) + 1, 10):
        d.add(Line(left, Y(gy), left + pw, Y(gy), strokeColor=GRIDC, strokeWidth=0.5))
        if gy:
            _txt(d, left - 13, Y(gy) - 2.4, str(gy), 6.6, FONT, GREY)

    poly = [(0, 0), (50, 0), (40, 20), (0, 40)]
    pts = []
    for px, py in poly:
        pts += [X(px), Y(py)]
    d.add(Polygon(pts, fillColor=FILL_GREEN, strokeColor=TEAL, strokeWidth=1.3))

    d.add(Line(left, bottom, left + pw + 10, bottom, strokeColor=INK, strokeWidth=1))
    d.add(Line(left, bottom, left, bottom + ph + 10, strokeColor=INK, strokeWidth=1))
    _txt(d, left + pw + 16, bottom - 3, "x", 8.4, FONT_I, INK)
    _txt(d, left - 12, bottom + ph + 10, "y", 8.4, FONT_I, INK)

    # d1: 2x + y = 100
    d.add(Line(X(27), Y(46), X(50), Y(0), strokeColor=BLUE, strokeWidth=1.5))
    _txt(d, X(25.5), Y(45.6), "d₁: 2x + y = 100", 7.0, FONT_B, BLUE, anchor="end")
    # d2: x + 2y = 80
    d.add(Line(X(0), Y(40), X(58), Y(11), strokeColor=RED, strokeWidth=1.5))
    _txt(d, X(3), Y(43.4), "d₂: x + 2y = 80", 7.0, FONT_B, RED, anchor="start")

    for pt, lab, dx, dy, anc in (
            ((0, 0), "O", 7, -12, "start"),
            ((50, 0), "A(50; 0)", 2, 6, "start"),
            ((40, 20), "B(40; 20)", 7, -3, "start"),
            ((0, 40), "C(0; 40)", -8, 5, "end")):
        d.add(Circle(X(pt[0]), Y(pt[1]), 2.6, fillColor=NAVY, strokeColor=NAVY))
        _txt(d, X(pt[0]) + dx, Y(pt[1]) + dy, lab, 7.2, FONT_B, NAVY, anchor=anc)

    if caption:
        _txt(d, width / 2, 8, caption, 7.2, FONT_I, GREY)
    return d


def _clip_halfplane(poly, f):
    """Sutherland–Hodgman: giữ phần đa giác có f(x, y) >= 0."""
    out = []
    n = len(poly)
    for i in range(n):
        cur = poly[i]
        nxt = poly[(i + 1) % n]
        fc, fn = f(*cur), f(*nxt)
        if fc >= 0:
            out.append(cur)
        if (fc >= 0) != (fn >= 0):
            t = fc / (fc - fn)
            out.append((cur[0] + t * (nxt[0] - cur[0]),
                        cur[1] + t * (nxt[1] - cur[1])))
    return out


def half_plane(width=330, height=225, caption="Hình. Miền nghiệm của 2x − y ≤ 3 (kể cả bờ d)"):
    """Miền nghiệm của 2x − y ≤ 3, tức y ≥ 2x − 3."""
    d = Drawing(width, height)
    left, bottom = 44, 40
    pw, ph = width - left - 24, height - bottom - 30
    xmin, xmax, ymin, ymax = -3.2, 4.4, -4.2, 4.0
    sx, sy = pw / (xmax - xmin), ph / (ymax - ymin)

    def X(v):
        return left + (v - xmin) * sx

    def Y(v):
        return bottom + (v - ymin) * sy

    f = lambda x, y: y - (2 * x - 3)          # y >= 2x - 3

    rect = [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]
    region = _clip_halfplane(rect, f)
    if region:
        pts = []
        for px, py in region:
            pts += [X(px), Y(py)]
        d.add(Polygon(pts, fillColor=FILL_GREEN, strokeColor=None, strokeWidth=0))

    # lưới nhẹ
    for gx in range(int(xmin), int(xmax) + 1):
        d.add(Line(X(gx), bottom, X(gx), bottom + ph,
                   strokeColor=GRIDC, strokeWidth=0.5))
    for gy in range(int(ymin), int(ymax) + 1):
        d.add(Line(left, Y(gy), left + pw, Y(gy),
                   strokeColor=GRIDC, strokeWidth=0.5))

    # trục toạ độ
    d.add(Line(left, Y(0), left + pw + 12, Y(0), strokeColor=INK, strokeWidth=1))
    d.add(Line(X(0), bottom, X(0), bottom + ph + 12, strokeColor=INK, strokeWidth=1))
    _txt(d, left + pw + 17, Y(0) - 3, "x", 8.6, FONT_I, INK)
    _txt(d, X(0) + 7, bottom + ph + 12, "y", 8.6, FONT_I, INK)
    _txt(d, X(0) - 9, Y(0) - 10, "O", 8.6, FONT_I, INK)

    # đường bờ d: qua (0; -3) và (3; 3) — nét đứt, không kể bờ
    d.add(Line(X(-0.35), Y(2 * (-0.35) - 3), X(3.35), Y(2 * 3.35 - 3),
               strokeColor=RED, strokeWidth=1.6, strokeDashArray=[4.5, 2.5]))
    _txt(d, X(2.55), Y(2 * 2.55 - 3) - 11, "d: 2x − y = 3", 7.6, FONT_B, RED, anchor="end")

    # điểm O(0; 0)
    d.add(Circle(X(0), Y(0), 2.6, fillColor=NAVY, strokeColor=NAVY))
    _txt(d, X(0) + 8, Y(0) + 5, "O(0; 0)", 7.4, FONT_B, NAVY, anchor="start")
    _txt(d, X(-1.6), Y(2.6), "miền nghiệm", 7.6, FONT_B, TEAL)

    if caption:
        _txt(d, width / 2, 6, caption, 7.2, FONT_I, GREY)
    return d


# ==========================================================================
def triangle_labels(width=280, height=165,
                    caption="Hình. Tam giác ABC với BC = a, CA = b, AB = c"):
    d = Drawing(width, height)
    A = (width * 0.52, height - 20)
    B = (26, 26)
    C = (width - 34, 40)
    d.add(Polygon([A[0], A[1], B[0], B[1], C[0], C[1]],
                  fillColor=FILL_BLUE, strokeColor=NAVY, strokeWidth=1.2))
    for pt, lab, dx, dy in ((A, "A", 0, 7), (B, "B", -3, -13), (C, "C", 6, -8)):
        _txt(d, pt[0] + dx, pt[1] + dy, lab, 10.5, FONT_B, NAVY)
    _txt(d, (B[0] + C[0]) / 2, (B[1] + C[1]) / 2 - 12, "a", 9.5, FONT_I, RED)
    _txt(d, (A[0] + C[0]) / 2 + 11, (A[1] + C[1]) / 2 + 1, "b", 9.5, FONT_I, RED)
    _txt(d, (A[0] + B[0]) / 2 - 11, (A[1] + B[1]) / 2 + 1, "c", 9.5, FONT_I, RED)
    if caption:
        _txt(d, width / 2, 4, caption, 7.4, FONT_I, GREY)
    return d


def parallelogram(width=250, height=145,
                  caption="Hình. Hình bình hành ABCD"):
    d = Drawing(width, height)
    A, B = (30, 28), (150, 28)
    D, C = (88, 110), (208, 110)
    d.add(Polygon([A[0], A[1], B[0], B[1], C[0], C[1], D[0], D[1]],
                  fillColor=FILL_GOLD, strokeColor=GOLD, strokeWidth=1.3))
    for pt, lab, dx, dy, anc in ((A, "A", -11, -3, "end"), (B, "B", 9, -3, "start"),
                                 (C, "C", 9, -3, "start"), (D, "D", -11, -3, "end")):
        _txt(d, pt[0] + dx, pt[1] + dy, lab, 10, FONT_B, GOLD, anchor=anc)
    if caption:
        _txt(d, width / 2, 5, caption, 7.4, FONT_I, GREY)
    return d
