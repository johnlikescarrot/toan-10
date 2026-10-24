#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build.py -- Sinh file PDF de cuong on tap Toan 10 (giua ki I, 2026-2027).

Cach chay:
    python3 de-cuong/src/build.py                 # sinh PDF
    python3 de-cuong/src/build.py --check         # chi kiem tra ki tu thieu trong font
"""
from __future__ import annotations

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.abspath(os.path.join(HERE, ".."))
OUT_PDF = os.path.join(OUT_DIR, "De-cuong-on-tap-Toan-10-Giua-ki-I-2026-2027.pdf")
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

sys.path.insert(0, HERE)
import content  # noqa: E402
from fpdf.enums import XPos, YPos  # noqa: E402
from pdfkit import (BODY, DEFAULT_FIGURES, Doc, LH, MUTED, NAVY, PANEL,  # noqa: E402
                    RULE, SANS, SANS_B, SERIF, SMALL, INK, BOX_INFO_BG)

FIG_H = {name: h for name, (_, h) in DEFAULT_FIGURES.items()}


# ---------------------------------------------------------------------------
# Kiem tra ki tu co trong font hay khong
# ---------------------------------------------------------------------------
def check_glyphs() -> int:
    """Kiem tra moi ki tu deu co trong font se dung de ve no.

    Van ban thuong ve bang DejaVu Sans (regular + bold); cac dong cong thuc
    (bat dau bang '= ') ve bang DejaVu Serif bold. Vi vay phai kiem tra rieng.
    """
    from fontTools.ttLib import TTFont

    def cmap(path):
        return TTFont(os.path.join(FONT_DIR, path)).getBestCmap()

    sans = cmap("DejaVuSans.ttf")
    sans_b = cmap("DejaVuSans-Bold.ttf")
    serif = cmap("DejaVuSerif.ttf")
    serif_b = cmap("DejaVuSerif-Bold.ttf")

    text = "\n".join(content.SECTIONS)
    formula_chars = set()
    for ln in text.split("\n"):
        if ln.strip().startswith("= "):
            formula_chars |= set(ln)

    missing_sans = {c: hex(ord(c)) for c in set(text)
                    if c not in "\n\t" and (ord(c) not in sans or ord(c) not in sans_b)}
    missing_serif = {c: hex(ord(c)) for c in formula_chars
                     if c not in "\n\t" and (ord(c) not in serif or ord(c) not in serif_b)}

    if missing_sans or missing_serif:
        if missing_sans:
            print("Thieu trong DejaVu Sans (van ban thuong):", missing_sans)
        if missing_serif:
            print("Thieu trong DejaVu Serif (dong cong thuc):", missing_serif)
        return 1
    print(f"OK: {len(set(text))} ki tu van ban + {len(formula_chars)} ki tu cong thuc "
          f"deu co glyph trong font tuong ung.")
    return 0


# ---------------------------------------------------------------------------
# Bo phan tich mini-markup
# ---------------------------------------------------------------------------
class Block:
    def __init__(self, kind, data):
        self.kind = kind
        self.data = data


def check_tables(src: str) -> list[str]:
    """Bao loi khi mot dong bang co so o khac dong tieu de (thuong do ki tu '|'
    nam trong noi dung, vi du '|vecto MA|')."""
    errors, head = [], None
    for i, ln in enumerate(src.split("\n"), 1):
        t = ln.strip()
        if t.startswith("|"):
            n = len(t.strip("|").split("|"))
            if head is None:
                head = n
            elif n != head:
                errors.append(f"dong {i}: {n} o, tieu de {head} o — {t[:80]}")
        else:
            head = None
    return errors


def _strip_md(s: str) -> str:
    return s.replace("**", "").replace("*", "")


_EMPH = re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)")


def clean_md(text: str) -> str:
    """Chuan hoa markdown: bo backtick, bo *nghieng* (khong co font Oblique),
    giu lai **in dam** (fpdf2 ho tro)."""
    t = text.replace("`", "")
    prev = None
    while prev != t:
        prev = t
        t = _EMPH.sub(r"\1", t)
    return t


def parse(src: str) -> list[Block]:
    lines = src.split("\n")
    blocks: list[Block] = []
    i = 0
    n = len(lines)

    def is_special(ln: str) -> bool:
        t = ln.lstrip()
        return (t.startswith(("#", "- ", "> ", "! ", "~ ", "= ", "|", "@@hinh:", "[PB]"))
                or re.match(r"^\d+\.\s", t) is not None
                or re.match(r"^[a-zđ]\)\s", t) is not None
                or (t.startswith("*") and t.endswith("*") and len(t) > 2))

    while i < n:
        raw = lines[i]
        line = raw.rstrip()
        t = line.strip()

        if not t:
            i += 1
            continue

        # --- heading
        if t.startswith("####"):
            blocks.append(Block("h4", clean_md(t.lstrip("#").strip())))
            i += 1
            continue
        if t.startswith("###"):
            blocks.append(Block("h3", clean_md(t.lstrip("#").strip())))
            i += 1
            continue
        if t.startswith("##"):
            blocks.append(Block("h2", clean_md(t.lstrip("#").strip())))
            i += 1
            continue
        if t.startswith("#"):
            blocks.append(Block("h1", clean_md(t.lstrip("#").strip())))
            i += 1
            continue

        if t == "[PB]":
            blocks.append(Block("pb", None))
            i += 1
            continue

        # --- hinh ve + chu thich ngay sau (neu co)
        m = re.match(r"@@hinh:([A-Za-z0-9_]+)@@", t)
        if m:
            name = m.group(1)
            i += 1
            cap = ""
            j = i
            while j < n and not lines[j].strip():
                j += 1
            if j < n:
                nt = lines[j].strip()
                if (nt.startswith("*") and nt.endswith("*") and len(nt) > 2
                        and not nt.startswith("**") and nt.count("*") == 2):
                    cap = clean_md(nt.strip("*").strip())
                    i = j + 1
            blocks.append(Block("fig", (name, cap)))
            continue

        # --- bang
        if t.startswith("|"):
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                    rows.append([clean_md(c) for c in cells])
                i += 1
            blocks.append(Block("table", rows))
            continue

        # --- cong thuc
        if t.startswith("= "):
            items = []
            while i < n and lines[i].strip().startswith("= "):
                items.append(lines[i].strip()[2:].strip())
                i += 1
            blocks.append(Block("formula", items))
            continue

        # --- hop (! / ~ / >)
        if t.startswith("! ") or t.startswith("~ "):
            kind = "warn" if t.startswith("! ") else "tip"
            head = t[2:].strip()
            m_bold = re.fullmatch(r"\*\*(.+?)\*\*", head)
            title = m_bold.group(1) if m_bold else _strip_md(head)
            raw, i = _read_box_lines(lines, i + 1, n)
            blocks.append(Block(kind, (clean_md(title),
                                       [clean_md(x) for x in _group_items(raw)])))
            continue
        if t.startswith(">"):
            raw, i = _read_box_lines(lines, i, n)
            title = ""
            if raw and re.fullmatch(r"\*\*(.+?)\*\*", raw[0].strip()):
                title = re.fullmatch(r"\*\*(.+?)\*\*", raw[0].strip()).group(1)
                raw = raw[1:]
            blocks.append(Block("note", (clean_md(title),
                                         [clean_md(x) for x in _group_items(raw)])))
            continue

        # --- muc a) b) c) ... : mot doan rieng, gom cac dong noi tiep
        m_sub = re.match(r"^([a-zđ]\))\s+(.*)$", t)
        if m_sub:
            parts = [m_sub.group(2).strip()]
            i += 1
            while i < n:
                nxt = lines[i].rstrip()
                nt = nxt.strip()
                if not nt or is_special(nxt) or re.match(r"^[a-zđ]\)\s", nt):
                    break
                parts.append(nt)
                i += 1
            blocks.append(Block("sub", (m_sub.group(1), clean_md(" ".join(parts)))))
            continue

        # --- gach dau dong / muc danh so (gom ca cac dong noi tiep)
        m_num = re.match(r"^(\d+\.)\s+(.*)$", t)
        if t.startswith("- ") or m_num:
            if m_num:
                marker, first = m_num.group(1), m_num.group(2)
            else:
                marker, first = "\u2022", t[2:]
            parts = [first.strip()]
            i += 1
            while i < n:
                nxt = lines[i].rstrip()
                nt = nxt.strip()
                if not nt or is_special(nxt):
                    break
                parts.append(nt)
                i += 1
            text = clean_md(" ".join(parts))
            if marker == "\u2022":
                blocks.append(Block("bullet", text))
            else:
                blocks.append(Block("num", (marker, text)))
            continue

        # --- doan van ban (noi cac dong lien tiep)
        buf = [t]
        i += 1
        while i < n:
            nxt = lines[i].rstrip()
            nt = nxt.strip()
            if not nt or is_special(nxt):
                break
            buf.append(nt)
            i += 1
        blocks.append(Block("p", clean_md(" ".join(buf))))

    return blocks


def _read_box_lines(lines, i, n):
    """Doc cac dong bat dau bang '>' va tra ve danh sach noi dung tho."""
    raw = []
    while i < n:
        t = lines[i].strip()
        if not t.startswith(">"):
            break
        raw.append(t[1:].strip())
        i += 1
    return raw, i


def _group_items(raw):
    """Gop cac dong tho thanh cac muc: doan van, '- ' -> '•  ', '1. ' -> muc so."""
    items: list[str] = []
    cur = None
    for ln in raw:
        if not ln.strip():
            if cur is not None:
                items.append(cur)
                cur = None
            continue
        if ln.startswith("- "):
            if cur is not None:
                items.append(cur)
            cur = "\u2022  " + ln[2:].strip()
        elif re.match(r"^\d+\.\s", ln):
            if cur is not None:
                items.append(cur)
            cur = ln.strip()
        else:
            cur = ln if cur is None else cur + " " + ln
    if cur is not None:
        items.append(cur)
    return items


# ---------------------------------------------------------------------------
# Ve
# ---------------------------------------------------------------------------
def render(blocks: list[Block], out: str,
           toc: list[tuple[str, int, int]] | None = None) -> list[tuple[str, int, int]]:
    """Ve tai lieu. Goi 2 luot: luot 1 (toc=None) de thu so trang, luot 2 de in muc luc."""
    pdf = Doc(title="Đề cương ôn tập giữa kì I – Toán 10 (2026–2027)",
              subtitle="Bám sát ma trận đề kiểm tra giữa kì I – Trường THPT Hà Huy Tập")
    pdf.set_title("Đề cương ôn tập giữa học kì I – môn Toán lớp 10 – năm học 2026–2027")
    pdf.set_subject("Bám sát ma trận đề kiểm tra giữa kì I – Trường THPT Hà Huy Tập – "
                    "chương trình Kết nối tri thức với cuộc sống")
    pdf.set_author("Biên soạn từ ma trận đề của Tổ Toán–Tin, Trường THPT Hà Huy Tập")
    pdf.set_keywords("Toán 10, giữa kì I, 2026-2027, Kết nối tri thức, mệnh đề, tập hợp, "
                     "bất phương trình bậc nhất hai ẩn, hệ thức lượng, vectơ, đề cương ôn tập")
    pdf.set_creator("de-cuong/src/build.py (fpdf2)")
    for name, (fn, _) in DEFAULT_FIGURES.items():
        pdf.figures[name] = fn

    pdf.add_page()
    _cover(pdf)

    if toc is not None:
        pdf.add_page()
        _draw_toc(pdf, toc)

    first_content_page = pdf.page_no() + 1 if toc is not None else pdf.page_no()

    for b in blocks:
        k = b.kind
        if k == "h1":
            pdf.h1(b.data)
        elif k == "h2":
            pdf.h2(b.data)
        elif k == "h3":
            pdf.h3(b.data)
        elif k == "h4":
            pdf.h4(b.data)
        elif k == "pb":
            pdf.add_page()
        elif k == "p":
            if b.data.startswith("**Câu "):
                pdf.ln(1.5)
            pdf.para(b.data)
        elif k == "bullet":
            pdf.bullet(b.data)
        elif k == "num":
            pdf.numitem(b.data[0], b.data[1])
        elif k == "sub":
            pdf.numitem(b.data[0], b.data[1], indent=6.5)
        elif k == "formula":
            for f in b.data:
                pdf.formula(f)
        elif k in ("note", "warn", "tip"):
            title, body = b.data
            getattr(pdf, k)(clean_md(title), [clean_md(x) for x in body])
        elif k == "table":
            rows = b.data
            ncol = max(len(r) for r in rows)
            rows = [r + [""] * (ncol - len(r)) for r in rows]
            pdf.table(rows)
        elif k == "fig":
            name, cap = b.data
            h = FIG_H.get(name, 50)
            pdf.figure(name, cap, h)

    pdf.output(out)
    del first_content_page
    return pdf.sections


def _draw_toc(p: Doc, entries: list[tuple[str, int, int]]) -> None:
    """Ve muc luc (cap 1 va cap 2) tren trang hien tai."""
    p.set_font(SANS_B, "", 15)
    p.set_text_color(*NAVY)
    p.set_y(20)
    p.cell(0, 9, "MỤC LỤC", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    p.set_draw_color(*RULE)
    p.set_line_width(0.6)
    p.line(17, p.get_y() + 1, 193, p.get_y() + 1)
    p.set_y(p.get_y() + 6)

    for name, level, page in entries:
        if level == 0:
            p.set_font(SANS_B, "", 10.4)
            p.set_text_color(*NAVY)
            indent, h = 0.0, 6.2
            p.ln(1.2)
        else:
            p.set_font(SANS, "", 9.4)
            p.set_text_color(*INK)
            indent, h = 7.0, 5.0
        p.set_x(17 + indent)
        p.cell(150 - indent, h, name)
        p.set_font(SANS, "B" if level == 0 else "", 9.4 if level else 10.4)
        p.cell(0, h, str(page), align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    p.set_text_color(*INK)


def _widths(rows, total):
    """Chia chieu rong cot theo noi dung, co chan duoi."""
    ncol = len(rows[0])
    if ncol == 1:
        return [total]
    maxlens = []
    for c in range(ncol):
        m = 0
        for r in rows:
            m = max(m, len(_strip_md(r[c])))
        maxlens.append(max(3, m))
    s = sum(maxlens)
    widths = [max(total * 0.055, total * m / s) for m in maxlens]
    k = total / sum(widths)
    return [w * k for w in widths]


def _cover(d: Doc) -> None:
    d.set_fill_color(*NAVY)
    d.rect(0, 0, 210, 74, style="F")
    d.set_fill_color(30, 96, 178)
    d.rect(0, 74, 210, 3, style="F")
    d.set_xy(20, 16)
    d.set_font(SANS_B, "", 10.4)
    d.set_text_color(196, 216, 240)
    d.cell(0, 5.4, content.COVER_LINES[0], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    d.set_x(20)
    d.cell(0, 5.4, content.COVER_LINES[1], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    d.set_xy(20, 34)
    d.set_font(SANS_B, "", 22)
    d.set_text_color(255, 255, 255)
    d.cell(0, 10, "ĐỀ CƯƠNG ÔN TẬP", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    d.set_x(20)
    d.set_font(SANS_B, "", 15.5)
    d.set_text_color(214, 231, 249)
    d.cell(0, 8, "KIỂM TRA GIỮA HỌC KÌ I — MÔN TOÁN — LỚP 10", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    d.set_x(20)
    d.set_font(SANS, "", 11.5)
    d.set_text_color(176, 202, 232)
    d.cell(0, 7, "Năm học 2026 – 2027  |  Thời gian làm bài: 90 phút",
           new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    y = 88
    d.set_xy(20, y)
    d.set_font(SANS_B, "", 11.2)
    d.set_text_color(*NAVY)
    d.cell(0, 6, "Bám sát chương trình Kết nối tri thức với cuộc sống",
           new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    info = [
        ("Phạm vi kiểm tra", "Chương 1. Mệnh đề và tập hợp  •  Chương 2. Bất phương trình và hệ "
                            "bất phương trình bậc nhất hai ẩn  •  Chương 3. Hệ thức lượng trong tam "
                            "giác  •  Chương 4. Vectơ"),
        ("Cấu trúc đề", "12 câu trắc nghiệm nhiều phương án (3,0 đ)  •  2 câu đúng–sai gồm 8 ý "
                        "(2,0 đ)  •  4 câu trả lời ngắn (2,0 đ)  •  3 câu tự luận (3,0 đ)"),
        ("Nội dung tài liệu", "Phân tích ma trận • Kiến thức trọng tâm 4 chương • Đề kiểm tra minh "
                              "họa đầy đủ • Đáp án và lời giải chi tiết cho toàn bộ 27 lệnh hỏi • "
                              "Ngân hàng bài tập tự luyện • Phụ lục công thức và mẹo bấm máy"),
    ]
    d.set_y(98)
    for label, val in info:
        y0 = d.get_y()
        d.set_font(SANS_B, "", 9.4)
        d.set_text_color(*NAVY)
        d.set_x(20)
        d.cell(38, 5, label)
        d.set_font(SANS, "", 9.4)
        d.set_text_color(*INK)
        d.multi_cell(132, 5, val, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        h = d.get_y() - y0
        d.set_y(y0 + max(h, 6) + 3.5)

    # khung ma tran tom tat
    y0 = d.get_y() + 4
    d.set_fill_color(*PANEL)
    d.rect(20, y0, 170, 40, style="F")
    d.set_draw_color(*RULE)
    d.set_line_width(0.3)
    d.rect(20, y0, 170, 40)
    d.set_xy(25, y0 + 4)
    d.set_font(SANS_B, "", 10.2)
    d.set_text_color(*NAVY)
    d.cell(0, 5.4, "TRỌNG SỐ ĐIỂM THEO CHƯƠNG", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    bars = [("Chương 1. Mệnh đề và tập hợp", 40, 4.00),
            ("Chương 3. Hệ thức lượng trong tam giác", 30, 3.00),
            ("Chương 2. Bất phương trình & hệ BPT", 25, 2.50),
            ("Chương 4. Vectơ", 5, 0.50)]
    yy = y0 + 12
    for name, pct, pts in bars:
        d.set_font(SANS, "", 8.4)
        d.set_text_color(*INK)
        d.set_xy(25, yy)
        d.cell(76, 4.6, name)
        d.set_fill_color(30, 96, 178)
        d.rect(103, yy + 0.6, pct * 1.5, 3.4, style="F")
        d.set_font(SANS_B, "", 8.4)
        d.set_text_color(*NAVY)
        d.set_xy(103 + pct * 1.5 + 2, yy)
        d.cell(30, 4.6, f"{pct}%  ({pts:.1f} đ)")
        yy += 6.6

    d.set_xy(20, 258)
    d.set_font(SANS, "", 8.6)
    d.set_text_color(*MUTED)
    d.multi_cell(170, 4.6,
                 "Tài liệu được biên soạn từ tệp “MA TRẬN TOÁN 10 - GIỮA KÌ I.docx” (Ma trận đề kiểm "
                 "tra giữa kì I năm học 2026-2027, môn Toán lớp 10 — Trường THPT Hà Huy Tập, Tổ "
                 "Toán–Tin). Đề kiểm tra ở Phần 3 là đề minh họa bám sát 100% ma trận và bảng đặc tả "
                 "gốc; toàn bộ đáp án và lời giải chi tiết ở Phần 4.", align="C")


def main() -> int:
    if "--check" in sys.argv:
        return check_glyphs()
    src = "\n".join(content.SECTIONS)
    errs = check_tables(src)
    if errs:
        print("LOI CAU TRUC BANG:")
        for e in errs:
            print("  ", e)
        return 1
    blocks = parse(src)
    kinds = {}
    for b in blocks:
        kinds[b.kind] = kinds.get(b.kind, 0) + 1
    print("Da phan tich:", kinds)
    # Lap den khi so trang trong muc luc on dinh (TOC chiem dung 1 trang).
    entries: list[tuple[str, int, int]] = []
    for attempt in range(1, 6):
        sections = render(blocks, OUT_PDF, toc=entries if entries else None)
        new = [(n, lv, pg) for (n, lv, pg) in sections if lv <= 1]
        if new == entries:
            print(f"  muc luc on dinh sau {attempt} luot: {len(entries)} muc")
            break
        entries = new
        print(f"  luot {attempt}: {len(entries)} muc, tong ket qua se tinh lai")
    else:
        print("  CANH BAO: muc luc khong on dinh")
    size = os.path.getsize(OUT_PDF)
    print(f"Da sinh: {OUT_PDF}  ({size:,} byte)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
