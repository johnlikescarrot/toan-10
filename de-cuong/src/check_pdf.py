#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_pdf.py -- Kiem tra chat luong ban in: tran le, chong chu, trang trong.

Chay: python3 de-cuong/src/check_pdf.py [duong_dan.pdf]
"""
import sys

import pypdfium2 as pdfium

PT = 72 / 25.4          # 1 mm = 2.8346 pt
PAGE_W, PAGE_H = 595.2760, 841.8898
MARGIN = 18 * PT        # le trai/phai 18 mm
TOP_LIMIT = PAGE_H - 7 * PT    # tran tren (header o 9-13 mm)
BOT_LIMIT = 8 * PT            # tran duoi (footer o 12-16 mm)


def rects(page):
    tp = page.get_textpage()
    out = []
    for i in range(tp.count_rects()):
        x0, y0, x1, y1 = tp.get_rect(i)
        txt = tp.get_text_bounded(left=x0 - 1, bottom=y0 - 1,
                                  right=x1 + 1, top=y1 + 1)
        if txt.strip():
            out.append((x0, y0, x1, y1, txt))
    return out


def overlap_area(a, b):
    ax0, ay0, ax1, ay1 = a[:4]
    bx0, by0, bx1, by1 = b[:4]
    dx = min(ax1, bx1) - max(ax0, bx0)
    dy = min(ay1, by1) - max(ay0, by0)
    if dx <= 0.6 or dy <= 0.6:
        return 0.0
    return dx * dy


def main() -> int:
    path = sys.argv[1] if len(sys.argv) > 1 else (
        "de-cuong/De-cuong-on-tap-Toan-10-Giua-ki-I-2026-2027.pdf")
    pdf = pdfium.PdfDocument(path)
    problems = 0
    print(f"Kiem tra {len(pdf)} trang: {path}\n")

    for pno in range(len(pdf)):
        page = pdf[pno]
        pw, ph = page.get_size()
        landscape = pw > ph
        m = MARGIN if not landscape else 18 * PT
        top_lim = ph - 7 * PT
        bot_lim = 8 * PT
        right_lim = pw - m
        rs = rects(page)
        page_no = pno + 1
        issues = []

        if len(rs) < 3:
            issues.append(f"TRANG GAN NHU TRONG ({len(rs)} dong)")
        if landscape and len(rs) < 8:
            issues.append(f"TRANG NGANG GAN NHU TRONG ({len(rs)} dong)")

        for (x0, y0, x1, y1, t) in rs:
            if ("Đề cương ôn tập giữa kì I" in t and "Trang" in t) or t.strip().startswith("Trang "):
                continue
            if "Bám sát ma trận đề kiểm tra" in t or t.strip().startswith("—") and t.strip().endswith("—"):
                continue
            if x1 > right_lim + 2.0:
                issues.append(f"TRAN PHAI x1={x1:.1f} > {right_lim:.1f} | {t[:60]!r}")
            if x0 < m - 2.0:
                issues.append(f"TRAN TRAI x0={x0:.1f} < {m:.1f} | {t[:60]!r}")
            if y1 > top_lim:
                issues.append(f"TRAN TREN y1={y1:.1f} | {t[:60]!r}")
            if y0 < bot_lim:
                issues.append(f"TRAN DUOI y0={y0:.1f} | {t[:60]!r}")

        # chong chu
        for i in range(len(rs)):
            for j in range(i + 1, len(rs)):
                a, b = rs[i], rs[j]
                ov = overlap_area(a, b)
                if ov <= 0:
                    continue
                amin = min((a[2] - a[0]) * (a[3] - a[1]),
                           (b[2] - b[0]) * (b[3] - b[1]))
                if amin > 0 and ov / amin > 0.45:
                    issues.append(
                        f"CHONG CHU {ov / amin:.0%} | {a[4][:32]!r} <> {b[4][:32]!r}")

        if issues:
            problems += len(issues)
            print(f"--- trang {page_no} ---")
            for s in dict.fromkeys(issues):
                print("   ", s)

    print()
    if problems:
        print(f"==> {problems} van de can sua")
        return 1
    print("==> Khong phat hien van de (tran le / chong chu / trang trong)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
