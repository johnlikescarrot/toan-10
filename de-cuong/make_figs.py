# -*- coding: utf-8 -*-
"""Sinh các hình minh hoạ (PNG) dùng trong đề cương."""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "assets")

NAVY = "#16324F"
BLUE = "#1F4E79"
TEAL = "#0F6E63"
RED = "#C0392B"
GREY = "#5B6770"
FILL = "#F2C14E"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9.5,
    "savefig.dpi": 260,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.06,
})


def ven():
    fig, axes = plt.subplots(1, 2, figsize=(7.6, 3.1))
    titles = ["A ∩ B  (giao)", "A ∪ B  (hợp)"]
    for k, (ax, title) in enumerate(zip(axes, titles)):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6.6)
        ax.set_aspect("equal")
        ax.axis("off")

        c1, c2, r = (4.0, 3.1), (6.0, 3.1), 2.4
        th = np.linspace(0, 2 * np.pi, 400)
        # nền nhạt cho cả hai đường tròn
        for c in (c1, c2):
            ax.fill(c[0] + r * np.cos(th), c[1] + r * np.sin(th),
                    color="#E8EDF4", zorder=1)

        # vùng giao (thấu kính)
        d = c2[0] - c1[0]
        a = d / 2.0
        h = np.sqrt(r ** 2 - a ** 2)
        t1 = np.arctan2(h, a)
        arc1 = np.column_stack([c1[0] + r * np.cos(np.linspace(-t1, t1, 240)),
                                c1[1] + r * np.sin(np.linspace(-t1, t1, 240))])
        arc2 = np.column_stack([c2[0] + r * np.cos(np.linspace(np.pi - t1, np.pi + t1, 240)),
                                c2[1] + r * np.sin(np.linspace(np.pi - t1, np.pi + t1, 240))])
        lens = np.vstack([arc1, arc2])

        if k == 0:
            ax.fill(lens[:, 0], lens[:, 1], color=FILL, alpha=0.95, zorder=2)
        else:
            # hợp = hai đường tròn (đã tô nền) -> tô đậm toàn bộ
            for c in (c1, c2):
                ax.fill(c[0] + r * np.cos(th), c[1] + r * np.sin(th),
                        color=FILL, alpha=0.95, zorder=2)

        for c in (c1, c2):
            ax.add_patch(Circle(c, r, fill=False, lw=1.7, ec=NAVY, zorder=4))
        ax.text(c1[0] - 1.15, c1[1], "A", fontsize=15, color=NAVY,
                ha="center", va="center", zorder=5)
        ax.text(c2[0] + 1.15, c2[1], "B", fontsize=15, color=NAVY,
                ha="center", va="center", zorder=5)
        ax.set_title(title, fontsize=12.5, color=TEAL, pad=1,
                     fontweight="bold")
    fig.savefig(os.path.join(OUT, "ven.png"), facecolor="white")
    plt.close(fig)


def mien_nghiem():
    """Miền nghiệm của hệ: 3x + 2y <= 120 ; x + 2y <= 80 ; x>=0 ; y>=0"""
    fig, ax = plt.subplots(figsize=(6.6, 4.5))
    x = np.linspace(-6, 48, 800)

    y1 = (120 - 3 * x) / 2.0   # 3x + 2y = 120
    y2 = (80 - x) / 2.0        # x + 2y  = 80

    ax.plot(x, y1, color=BLUE, lw=1.7, label="3x + 2y = 120")
    ax.plot(x, y2, color=TEAL, lw=1.7, label="x + 2y = 80")

    xs = [0, 40, 20, 0]
    ys = [0, 0, 30, 40]
    ax.fill(xs, ys, color=FILL, alpha=0.45, zorder=1)
    ax.plot(xs + [0], ys + [0], color=RED, lw=1.4, zorder=3)

    pts = [(0, 0), (40, 0), (20, 30), (0, 40)]
    lab = ["O(0; 0)", "A(40; 0)", "B(20; 30)", "C(0; 40)"]
    off = [(1.2, 1.3), (1.2, 1.3), (1.2, 1.3), (1.2, 1.3)]
    for (px, py), s, (dx, dy) in zip(pts, lab, off):
        ax.plot([px], [py], "o", ms=5.5, color=RED, zorder=6)
        ax.text(px + dx, py + dy, s, fontsize=9, color=RED, zorder=6)

    ax.axhline(0, color=GREY, lw=1.0)
    ax.axvline(0, color=GREY, lw=1.0)
    ax.set_xlim(-7, 50)
    ax.set_ylim(-6, 46)
    ax.set_xlabel("x", fontsize=11, color=NAVY)
    ax.set_ylabel("y", fontsize=11, color=NAVY)
    ax.set_xticks([0, 10, 20, 30, 40])
    ax.set_yticks([0, 10, 20, 30, 40])
    ax.grid(alpha=0.25, ls=":")
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.legend(loc="upper right", fontsize=9, frameon=False)
    fig.savefig(os.path.join(OUT, "mien-nghiem.png"), facecolor="white")
    plt.close(fig)


def truc_so():
    """Biểu diễn [−3; 2) và [1; +∞) trên trục số."""
    fig, axes = plt.subplots(3, 1, figsize=(7.2, 2.9))
    data = [
        ("A = [−3; 2)", -3, 2, "left_closed_right_open"),
        ("B = [1; +∞)", 1, None, "left_closed"),
        ("A ∩ B = [1; 2)", 1, 2, "left_closed_right_open"),
    ]
    for ax, (name, a, b, kind) in zip(axes, data):
        ax.set_xlim(-5.2, 6.2)
        ax.set_ylim(-1.5, 1.5)
        ax.axis("off")
        ax.annotate("", xy=(6.0, 0), xytext=(-5.0, 0),
                    arrowprops=dict(arrowstyle="-|>", color=GREY, lw=1.1))
        for t in range(-5, 7):
            ax.plot([t, t], [-0.09, 0.09], color=GREY, lw=0.9)
        end = b if b is not None else 6.0
        ax.plot([a, end], [0, 0], color=BLUE, lw=3.4, solid_capstyle="butt")
        ax.plot([a], [0], "o", ms=7, mfc=BLUE, mec=BLUE)
        if b is None:
            ax.annotate("", xy=(6.1, 0), xytext=(5.3, 0),
                        arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=3.0))
        elif kind.endswith("open"):
            ax.plot([b], [0], "o", ms=7, mfc="white", mec=BLUE, mew=1.6)
        else:
            ax.plot([b], [0], "o", ms=7, mfc=BLUE, mec=BLUE)
        ax.text(-5.2, 0.42, name, fontsize=10, color=NAVY, fontweight="bold")
        if b is not None:
            ax.text(b, -0.55, str(b).replace("-", "−"), ha="center",
                    fontsize=9, color=GREY)
        ax.text(a, -0.55, str(a).replace("-", "−"), ha="center",
                fontsize=9, color=GREY)
    fig.subplots_adjust(hspace=0.15)
    fig.savefig(os.path.join(OUT, "truc-so.png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    ven()
    mien_nghiem()
    truc_so()
    print("Đã tạo hình:", sorted(os.listdir(OUT)))
