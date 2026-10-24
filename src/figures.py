# -*- coding: utf-8 -*-
"""Sinh các hình minh hoạ (PNG) cho đề cương."""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Wedge
import numpy as np

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(HERE, "assets", "fig")
os.makedirs(FIG, exist_ok=True)

NAVY = "#12395B"
TEAL = "#0E6E6E"
ORANGE = "#B4560F"
GREY = "#5B6770"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.edgecolor": GREY,
    "axes.linewidth": 0.8,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.04,
})


def _arrow_ax(ax, xlim, ylim, xlabel="x", ylabel="y"):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axhline(0, color=GREY, lw=0.9, zorder=1)
    ax.axvline(0, color=GREY, lw=0.9, zorder=1)
    ax.annotate("", xy=(xlim[1], 0), xytext=(xlim[0], 0),
                arrowprops=dict(arrowstyle="-|>", color=GREY, lw=0.9))
    ax.annotate("", xy=(0, ylim[1]), xytext=(0, ylim[0]),
                arrowprops=dict(arrowstyle="-|>", color=GREY, lw=0.9))
    ax.text(xlim[1], -0.06 * (ylim[1] - ylim[0]), xlabel, color=GREY, ha="left", va="top")
    ax.text(-0.02 * (xlim[1] - xlim[0]), ylim[1], ylabel, color=GREY, ha="right", va="top")
    for sp in ("top", "right", "left", "bottom"):
        ax.spines[sp].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])


# ---------------------------------------------------------------- hình 1
def number_line():
    fig, axes = plt.subplots(3, 1, figsize=(6.4, 1.9))
    rows = [("[−3; 5)", -3, 5, "tr", "tr", "A = [−3; 5)"),
            ("[1; +∞)", 1, 9, "sq", "none", "B = [1; +∞)"),
            ("[1; 5)", 1, 5, "sq", "tr", "A ∩ B = [1; 5)")]
    for ax, (lbl, a, b, left, right, name) in zip(axes, rows):
        ax.set_xlim(-5, 10)
        ax.set_ylim(-1.0, 1.7)
        ax.axis("off")
        ax.annotate("", xy=(9.8, 0), xytext=(-5, 0),
                    arrowprops=dict(arrowstyle="-|>", color=GREY, lw=0.9))
        for t in range(-4, 10):
            ax.plot([t, t], [-0.09, 0.09], color=GREY, lw=0.7)
            ax.text(t, -0.30, str(t), color=GREY, ha="center", va="top", fontsize=7)
        ax.plot([a, b], [0, 0], color=TEAL, lw=3.4, solid_capstyle="butt", alpha=0.85)
        for pos, style in ((a, left), (b, right)):
            if style == "none":
                continue
            if style == "sq":
                ax.plot([pos], [0], marker="o", ms=6, mfc=TEAL, mec=TEAL, zorder=4)
            else:
                ax.plot([pos], [0], marker="o", ms=7, mfc="white", mec=TEAL, mew=1.5, zorder=4)
        ax.text(-4.85, 1.15, name, color=NAVY, fontsize=8.6, va="center")
    fig.subplots_adjust(hspace=1.05)
    fig.savefig(os.path.join(FIG, "f1_numberline.png"))
    plt.close(fig)


# ---------------------------------------------------------------- hình 2
def half_plane():
    fig, ax = plt.subplots(figsize=(3.5, 3.1))
    _arrow_ax(ax, (-1.2, 4.6), (-1.0, 5.4))
    x = np.linspace(-1.2, 4.6, 10)
    ax.plot(x, 4 - 2 * x, color=ORANGE, lw=1.8)
    ax.fill_between(x, -1.0, np.clip(4 - 2 * x, -1.0, 5.4), color=TEAL, alpha=0.14)
    ax.plot([2], [0], "o", color=ORANGE, ms=4.5)
    ax.plot([0], [4], "o", color=ORANGE, ms=4.5)
    ax.plot([0], [0], "o", color=NAVY, ms=4.5)
    ax.annotate("A(2; 0)", (2, 0), textcoords="offset points", xytext=(4, -12), fontsize=8, color=ORANGE)
    ax.annotate("B(0; 4)", (0, 4), textcoords="offset points", xytext=(6, 2), fontsize=8, color=ORANGE)
    ax.annotate("O(0; 0)", (0, 0), textcoords="offset points", xytext=(6, 6), fontsize=8, color=NAVY)
    ax.text(2.15, 4.4, "Δ: 2x + y − 4 = 0", color=ORANGE, fontsize=8, ha="left")
    ax.text(2.9, 0.55, "2x + y − 4 ≤ 0", color=TEAL, fontsize=8.6, ha="center")
    fig.savefig(os.path.join(FIG, "f2_halfplane.png"))
    plt.close(fig)


# ---------------------------------------------------------------- hình 3
def feasible():
    fig, ax = plt.subplots(figsize=(3.5, 3.1))
    _arrow_ax(ax, (-1.0, 10.2), (-1.0, 8.2))
    pts = np.array([[0, 0], [8, 0], [6, 2], [0, 6]])
    ax.add_patch(Polygon(pts, closed=True, facecolor=TEAL, alpha=0.16, edgecolor="none"))
    x1 = np.linspace(0, 8.6, 5)
    ax.plot(x1, 8 - x1, color=ORANGE, lw=1.5)
    x2 = np.linspace(0, 9.6, 5)
    ax.plot(x2, (18 - 2 * x2) / 3, color=NAVY, lw=1.5)
    for (px, py), lab, off in [((0, 0), "O(0; 0)", (5, 5)), ((8, 0), "M(8; 0)", (2, -13)),
                               ((0, 6), "N(0; 6)", (6, 2)), ((6, 2), "P(6; 2)", (6, 2))]:
        ax.plot([px], [py], "o", color=TEAL, ms=5, zorder=5)
        ax.annotate(lab, (px, py), textcoords="offset points", xytext=off,
                    fontsize=7.6, color=NAVY)
    from matplotlib.lines import Line2D
    handles = [Line2D([], [], color=ORANGE, lw=1.6, label="x + y = 8"),
               Line2D([], [], color=NAVY, lw=1.6, label="2x + 3y = 18")]
    leg = ax.legend(handles=handles, loc="upper right", fontsize=7.4, frameon=True,
                    borderpad=0.6, handlelength=1.6, labelspacing=0.4)
    leg.get_frame().set_edgecolor("#C9D6DF")
    leg.get_frame().set_linewidth(0.6)
    fig.savefig(os.path.join(FIG, "f3_feasible.png"))
    plt.close(fig)


# -------------------------------------------------------------- hình 3b
def feasible_coat():
    fig, ax = plt.subplots(figsize=(3.5, 3.1))
    _arrow_ax(ax, (-6, 90), (-6, 96))
    pts = np.array([[0, 0], [75, 0], [30, 60], [0, 80]])
    ax.add_patch(Polygon(pts, closed=True, facecolor=TEAL, alpha=0.16, edgecolor="none"))
    x1 = np.linspace(0, 80, 5)
    ax.plot(x1, (240 - 2 * x1) / 3, color=ORANGE, lw=1.5)
    x2 = np.linspace(0, 100, 5)
    ax.plot(x2, (300 - 4 * x2) / 3, color=NAVY, lw=1.5)
    for (px, py), lab, off in [((0, 0), "O(0; 0)", (5, 4)), ((75, 0), "M(75; 0)", (-6, -13)),
                               ((0, 80), "N(0; 80)", (6, 1)), ((30, 60), "P(30; 60)", (7, 2))]:
        ax.plot([px], [py], "o", color=TEAL, ms=5, zorder=5)
        ax.annotate(lab, (px, py), textcoords="offset points", xytext=off, fontsize=7.6, color=NAVY)
    from matplotlib.lines import Line2D
    handles = [Line2D([], [], color=ORANGE, lw=1.6, label="2x + 3y = 240"),
               Line2D([], [], color=NAVY, lw=1.6, label="4x + 3y = 300")]
    leg = ax.legend(handles=handles, loc="upper right", fontsize=7.2, frameon=True,
                    borderpad=0.6, handlelength=1.6, labelspacing=0.4)
    leg.get_frame().set_edgecolor("#C9D6DF")
    leg.get_frame().set_linewidth(0.6)
    fig.savefig(os.path.join(FIG, "f3b_coat.png"))
    plt.close(fig)


# ---------------------------------------------------------------- hình 4
def triangle():
    fig, ax = plt.subplots(figsize=(3.6, 2.6))
    ax.set_xlim(-0.4, 5.6)
    ax.set_ylim(-0.6, 3.8)
    ax.axis("off")
    A, B, C = (0, 0), (4.6, 0), (2.0, 3.2)
    ax.add_patch(Polygon([A, B, C], closed=True, facecolor=TEAL, alpha=0.10, edgecolor=NAVY, lw=1.4))
    for p, lab, off, al in [(A, "A", (-12, -4), "right"), (B, "B", (8, -4), "left"), (C, "C", (0, 8), "center")]:
        ax.plot([p[0]], [p[1]], "o", color=NAVY, ms=4)
        ax.annotate(lab, p, textcoords="offset points", xytext=off, fontsize=10,
                    color=NAVY, fontweight="bold", ha=al)
    ax.text(2.3, -0.32, "c", fontsize=9.5, color=ORANGE, ha="center", style="italic")
    ax.text(1.0, 1.7, "b", fontsize=9.5, color=ORANGE, ha="center", style="italic")
    ax.text(3.5, 1.75, "a", fontsize=9.5, color=ORANGE, ha="center", style="italic")
    ax.add_patch(Wedge(A, 0.62, 0, np.degrees(np.arctan2(3.2, 2.0)), color=ORANGE, alpha=0.25))
    ax.add_patch(Wedge(B, 0.62, 180 - np.degrees(np.arctan2(3.2, 2.6)), 180, color=ORANGE, alpha=0.25))
    ax.add_patch(Wedge(C, 0.55, 180 + np.degrees(np.arctan2(3.2, 2.6)), 360 - np.degrees(np.arctan2(3.2, 2.0)),
                       color=ORANGE, alpha=0.25))
    ax.text(0.95, 0.30, "A", fontsize=8, color=ORANGE)
    ax.text(4.05, 0.32, "B", fontsize=8, color=ORANGE)
    ax.text(1.85, 2.68, "C", fontsize=8, color=ORANGE)
    fig.savefig(os.path.join(FIG, "f4_triangle.png"))
    plt.close(fig)


if __name__ == "__main__":
    number_line()
    half_plane()
    feasible()
    feasible_coat()
    triangle()
    print("Đã tạo hình tại", FIG)
