# -*- coding: utf-8 -*-
"""Hình minh hoạ vẽ trực tiếp bằng canvas (không cần ảnh ngoài)."""
import math

from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import Flowable

from design import FRAME_W, GREY, NAVY, TEAL, AMBER

GRID = colors.HexColor('#DDE5EA')
SHADE = colors.HexColor('#CFE6E3')
FAINT = colors.HexColor('#F4F7F9')
RED = colors.HexColor('#A63D40')


class Figure(Flowable):
    """Khung chứa hình vẽ + chú thích dưới hình."""

    caption = ''
    fixed_height = 40 * mm

    def __init__(self, caption=''):
        super().__init__()
        self.width = FRAME_W
        self.height = self.fixed_height
        self.caption = caption

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        self.render()
        if self.caption:
            c = self.canv
            c.setFont('VN', 7.6)
            c.setFillColor(GREY)
            c.drawString(0, 0.4 * mm, self.caption)

    def render(self):
        raise NotImplementedError


# --------------------------------------------------------------------------
class NumberLine(Figure):
    """Hai trục số minh hoạ cách lấy giao và hợp của hai khoảng."""

    fixed_height = 47 * mm

    def __init__(self, caption='Hình 1. Giao, hợp, hiệu của hai khoảng trên trục số.'):
        super().__init__(caption)
        self.xmin, self.xmax = -3.8, 5.8

    def _x(self, v):
        return 16 * mm + (v - self.xmin) / (self.xmax - self.xmin) * (self.width - 34 * mm)

    def _axis(self, c, y, label):
        c.setFont('VN-Bold', 7.6)
        c.setFillColor(NAVY)
        c.drawString(0, y + 2.6 * mm, label)
        c.setStrokeColor(GREY)
        c.setLineWidth(0.8)
        xa = self._x(self.xmax) + 2 * mm
        c.line(self._x(self.xmin) - 2 * mm, y, xa, y)
        c.setFillColor(GREY)
        p = c.beginPath()
        p.moveTo(xa + 1.7 * mm, y)
        p.lineTo(xa, y + 0.85 * mm)
        p.lineTo(xa, y - 0.85 * mm)
        p.close()
        c.drawPath(p, fill=1, stroke=0)
        c.setFont('VN', 6.4)
        for v in range(math.ceil(self.xmin), int(self.xmax) + 1):
            x = self._x(v)
            c.setStrokeColor(GRID)
            c.setLineWidth(0.5)
            c.line(x, y - 0.55 * mm, x, y + 0.55 * mm)
            c.setFillColor(GREY)
            c.drawCentredString(x, y - 3.0 * mm, str(v))

    def _mark(self, c, x, y, closed, color):
        if closed:
            c.setFillColor(color)
            c.setStrokeColor(color)
            c.circle(x, y, 0.9 * mm, stroke=1, fill=1)
        else:
            c.setFillColor(colors.white)
            c.setStrokeColor(color)
            c.setLineWidth(1.0)
            c.circle(x, y, 0.9 * mm, stroke=1, fill=1)

    def _segment(self, c, y, a, b, lc, rc, color):
        c.setStrokeColor(color)
        c.setLineWidth(2.4)
        c.line(self._x(a), y, self._x(b), y)
        self._mark(c, self._x(a), y, lc, color)
        self._mark(c, self._x(b), y, rc, color)

    def render(self):
        c = self.canv
        y1, y2 = 33 * mm, 19 * mm
        self._axis(c, y1, 'A = [−3; 2)')
        self._segment(c, y1, -3, 2, True, False, NAVY)
        self._axis(c, y2, 'B = (0; 5]')
        self._segment(c, y2, 0, 5, False, True, AMBER)

        c.setFont('VN-Bold', 7.4)
        c.setFillColor(TEAL)
        c.drawString(0, 11.5 * mm, 'A ∩ B = (0; 2)')
        c.drawString(0, 6.0 * mm, 'A ∪ B = [−3; 5]')
        c.setFillColor(NAVY)
        c.drawString(self.width * 0.42, 11.5 * mm, 'A \\ B = [−3; 0]')
        c.drawString(self.width * 0.42, 6.0 * mm, 'CℝB = (−∞; 0] ∪ (5; +∞)')
        c.setFont('VN', 6.6)
        c.setFillColor(GREY)
        c.drawRightString(self.width, 6.0 * mm, '● lấy đầu mút    ○ không lấy')


class Venn(Figure):
    """Biểu đồ Ven hai tập hợp kèm số liệu bài toán đếm."""

    fixed_height = 55 * mm

    def __init__(self, caption='Hình 2. Biểu đồ Ven cho bài toán hai câu lạc bộ.'):
        super().__init__(caption)

    def render(self):
        c = self.canv
        r = 17.5 * mm
        cx1, cx2, cy = 62 * mm, 92 * mm, 32 * mm

        for cx, col in ((cx1, NAVY), (cx2, TEAL)):
            c.setFillColor(FAINT)
            c.setStrokeColor(col)
            c.setLineWidth(1.1)
            c.circle(cx, cy, r, stroke=1, fill=1)

        c.setFont('VN-Bold', 8.6)
        c.setFillColor(NAVY)
        c.drawCentredString(cx1 - 9 * mm, cy + r + 1.6 * mm, 'Toán (25)')
        c.setFillColor(TEAL)
        c.drawCentredString(cx2 + 9 * mm, cy + r + 1.6 * mm, 'Tin (18)')

        c.setFont('VN-Bold', 10.5)
        c.setFillColor(NAVY)
        c.drawCentredString(cx1 - 8.5 * mm, cy - 1.2 * mm, '15')
        c.setFillColor(TEAL)
        c.drawCentredString(cx2 + 8.5 * mm, cy - 1.2 * mm, '8')
        c.setFillColor(RED)
        c.drawCentredString((cx1 + cx2) / 2, cy - 1.2 * mm, '10')

        c.setFont('VN', 7.4)
        c.setFillColor(GREY)
        c.drawString(0, 6.2 * mm,
                     '|A ∪ B| = 25 + 18 − 10 = 33  →  số học sinh không tham gia câu lạc bộ nào: '
                     '40 − 33 = 7')


class FeasibleRegion(Figure):
    """Miền nghiệm (đa giác OABC) của một hệ bất phương trình bậc nhất hai ẩn."""

    fixed_height = 62 * mm

    def __init__(self, caption='Hình 3. Miền nghiệm của hệ x ≥ 0, y ≥ 0, 2x + y ≤ 8, x + y ≤ 6.'):
        super().__init__(caption)
        self.ox, self.oy = 15 * mm, 11 * mm
        self.sx, self.sy = 9.4 * mm, 5.2 * mm

    def _px(self, x):
        return self.ox + x * self.sx

    def _py(self, y):
        return self.oy + y * self.sy

    def render(self):
        c = self.canv
        XMAX, YMAX = 6.4, 9.4

        c.setStrokeColor(GRID)
        c.setLineWidth(0.4)
        for v in range(1, int(XMAX) + 1):
            c.line(self._px(v), self._py(0), self._px(v), self._py(YMAX))
        for v in range(1, int(YMAX) + 1):
            c.line(self._px(0), self._py(v), self._px(XMAX), self._py(v))

        # tô miền nghiệm
        poly = [(0, 0), (4, 0), (2, 4), (0, 6)]
        p = c.beginPath()
        p.moveTo(self._px(poly[0][0]), self._py(poly[0][1]))
        for x, y in poly[1:]:
            p.lineTo(self._px(x), self._py(y))
        p.close()
        c.setFillColor(SHADE)
        c.setStrokeColor(TEAL)
        c.setLineWidth(1.2)
        c.drawPath(p, fill=1, stroke=1)

        # trục toạ độ
        c.setStrokeColor(GREY)
        c.setLineWidth(0.9)
        c.line(self._px(0), self._py(0), self._px(XMAX), self._py(0))
        c.line(self._px(0), self._py(0), self._px(0), self._py(YMAX))
        c.setFont('VN', 7.2)
        c.setFillColor(GREY)
        c.drawString(self._px(XMAX) + 1 * mm, self._py(0) - 0.8 * mm, 'x')
        c.drawString(self._px(0) + 1 * mm, self._py(YMAX) + 0.8 * mm, 'y')

        # các đường biên
        for (x1, y1), (x2, y2), lab, lx, ly, col in (
                ((4, 0), (0, 8), '2x + y = 8', 4.15, 2.0, NAVY),
                ((6, 0), (0, 6), 'x + y = 6', 4.55, 3.55, AMBER)):
            c.setStrokeColor(col)
            c.setLineWidth(0.9)
            c.setDash(3, 2)
            c.line(self._px(x1), self._py(y1), self._px(x2), self._py(y2))
            c.setDash()
            c.setFont('VN', 7.0)
            c.setFillColor(col)
            c.drawString(self._px(lx), self._py(ly), lab)

        # các đỉnh
        c.setFont('VN-Bold', 7.2)
        for (x, y), name, dx, dy in (((0, 0), 'O', -4.4, -3.4),
                                     ((4, 0), 'A(4; 0)', -3.0, -4.6),
                                     ((2, 4), 'B(2; 4)', 1.0, 0.4),
                                     ((0, 6), 'C(0; 6)', 1.4, 1.4)):
            c.setFillColor(NAVY)
            c.circle(self._px(x), self._py(y), 0.85 * mm, stroke=0, fill=1)
            c.setFillColor(NAVY)
            c.drawString(self._px(x) + dx * mm, self._py(y) + dy * mm, name)

        c.setFont('VN', 7.0)
        c.setFillColor(TEAL)
        c.drawCentredString(self._px(1.35), self._py(2.1), 'miền nghiệm')


class TriangleFigure(Figure):
    """Tam giác ABC với quy ước cạnh a, b, c và ba góc."""

    fixed_height = 46 * mm

    def __init__(self, caption='Hình 4. Quy ước cạnh và góc trong tam giác ABC.'):
        super().__init__(caption)

    @staticmethod
    def _angle(u, v):
        a1 = math.degrees(math.atan2(u[1], u[0])) % 360
        a2 = math.degrees(math.atan2(v[1], v[0])) % 360
        diff = (a2 - a1) % 360
        if diff <= 180:
            return a1, diff
        return a2, 360 - diff

    def render(self):
        c = self.canv
        A, B, C = (22 * mm, 8 * mm), (66 * mm, 8 * mm), (44 * mm, 34 * mm)

        p = c.beginPath()
        p.moveTo(*A)
        p.lineTo(*B)
        p.lineTo(*C)
        p.close()
        c.setFillColor(FAINT)
        c.setStrokeColor(NAVY)
        c.setLineWidth(1.1)
        c.drawPath(p, fill=1, stroke=1)

        # góc (cung nhỏ)
        c.setStrokeColor(RED)
        c.setFillColor(colors.HexColor('#F7E4E4'))
        c.setLineWidth(0.8)
        for V, P1, P2 in ((A, B, C), (B, A, C), (C, A, B)):
            u = (P1[0] - V[0], P1[1] - V[1])
            v = (P2[0] - V[0], P2[1] - V[1])
            start, extent = self._angle(u, v)
            r = 5.4 * mm
            c.wedge(V[0] - r, V[1] - r, V[0] + r, V[1] + r, start, extent,
                    stroke=0, fill=1)

        # nhãn đỉnh
        c.setFont('VN-Bold', 9.4)
        c.setFillColor(NAVY)
        c.drawRightString(A[0] - 2.0 * mm, A[1] - 1.0 * mm, 'A')
        c.drawString(B[0] + 2.0 * mm, B[1] - 1.0 * mm, 'B')
        c.drawCentredString(C[0], C[1] + 1.8 * mm, 'C')

        # tên cạnh
        c.setFont('VN', 8.2)
        c.setFillColor(AMBER)
        c.drawCentredString((B[0] + C[0]) / 2 + 3.8 * mm, (B[1] + C[1]) / 2, 'a')
        c.drawCentredString((A[0] + C[0]) / 2 - 3.8 * mm, (A[1] + C[1]) / 2, 'b')
        c.setFillColor(TEAL)
        c.drawCentredString((A[0] + B[0]) / 2, A[1] - 4.0 * mm, 'c')

        # công thức kèm theo
        c.setFont('VN', 7.4)
        c.setFillColor(GREY)
        for i, line in enumerate(['BC = a,  CA = b,  AB = c',
                                  'a² = b² + c² − 2bc·cos A',
                                  'a / sin A = 2R',
                                  'S = ½ab·sin C = pr = abc/(4R)']):
            c.drawString(82 * mm, 30 * mm - i * 4.6 * mm, line)
