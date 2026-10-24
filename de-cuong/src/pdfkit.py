"""
pdfkit.py -- Bo ve PDF tieng Viet (khong phu thuoc LaTeX / WeasyPrint).

Dung fpdf2 + bo font DejaVu (co day du dau tieng Viet va ki hieu toan hoc).

Toan bo doan van ban deu di qua multi_cell(markdown=True), va moi hop/bang
duoc DO CHIEU CAO TRUOC bang dry_run de khong bao gio de chu tran ra ngoai
hoac chong len nhau.
"""
from __future__ import annotations

import math
from typing import Callable, Dict, List, Optional, Sequence

from fpdf import FPDF
from fpdf.enums import XPos, YPos

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
SANS = "DejaVuSans"
SANS_B = "DejaVuSans-Bold"
SERIF = "DejaVuSerif"
SERIF_B = "DejaVuSerif-Bold"

# ---- Bang mau -------------------------------------------------------------
INK = (28, 32, 38)
MUTED = (98, 106, 118)
NAVY = (23, 58, 110)
BLUE = (30, 96, 178)
TEAL = (13, 104, 104)
RULE = (198, 206, 216)
PANEL = (244, 247, 251)
BOX_INFO_BG, BOX_INFO_FG = (233, 242, 252), (18, 70, 132)
BOX_WARN_BG, BOX_WARN_FG = (253, 236, 234), (146, 34, 28)
BOX_TIP_BG, BOX_TIP_FG = (255, 247, 224), (118, 80, 6)
BOX_EX_BG, BOX_EX_FG = (236, 246, 238), (18, 88, 50)
TBL_HEAD_BG = (35, 71, 128)
TBL_HEAD_FG = (255, 255, 255)
TBL_ALT_BG = (245, 248, 252)

LH = 4.75       # chieu cao dong van ban
BODY = 9.7      # co chu than bai
SMALL = 8.5


class Doc(FPDF):
    """Tai lieu co header/footer, muc luc va cac khoi noi dung."""

    def __init__(self, title: str, subtitle: str):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.doc_title = title
        self.doc_subtitle = subtitle
        self.figures: Dict[str, Callable[["Doc"], None]] = {}
        self.sections: List[tuple] = []
        self.install_fonts()
        self.set_auto_page_break(True, margin=18)
        self.set_margins(18, 18, 18)
        self.set_font(SANS, "", BODY)
        self.set_text_color(*INK)

    # ---------------------------------------------------------------- fonts
    def install_fonts(self) -> None:
        # Dang ki ca theo style (SANS + "B") va theo family (SANS_B)
        # de moi cach goi set_font() deu hop le.
        self.add_font(SANS, "", f"{FONT_DIR}/DejaVuSans.ttf")
        self.add_font(SANS, "B", f"{FONT_DIR}/DejaVuSans-Bold.ttf")
        self.add_font(SANS_B, "", f"{FONT_DIR}/DejaVuSans-Bold.ttf")
        self.add_font(SERIF, "", f"{FONT_DIR}/DejaVuSerif.ttf")
        self.add_font(SERIF, "B", f"{FONT_DIR}/DejaVuSerif-Bold.ttf")
        self.add_font(SERIF_B, "", f"{FONT_DIR}/DejaVuSerif-Bold.ttf")
        import os as _os
        for _fam in (SANS, SERIF):
            for _st, _fn in (("I", "DejaVuSans-Oblique.ttf"),
                             ("BI", "DejaVuSans-BoldOblique.ttf")):
                _p = f"{FONT_DIR}/{_fn}"
                if _os.path.exists(_p):
                    try:
                        self.add_font(_fam, _st, _p)
                    except Exception:
                        pass

    @property
    def cw(self) -> float:
        return self.w - self.l_margin - self.r_margin

    # ------------------------------------------------------ header / footer
    def header(self) -> None:
        if self.page_no() == 1:
            return
        self.set_y(9)
        self.set_font(SANS, "", 7.6)
        self.set_text_color(*MUTED)
        self.cell(self.cw / 2, 4.2, self.doc_title, align="L")
        self.cell(self.cw / 2, 4.2, f"Trang {self.page_no()}", align="R",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_draw_color(*RULE)
        self.set_line_width(0.25)
        self.line(self.l_margin, 13.6, self.w - self.r_margin, 13.6)
        self.set_y(19)

    def footer(self) -> None:
        self.set_y(-14)
        self.set_draw_color(*RULE)
        self.set_line_width(0.25)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.set_y(-12.4)
        self.set_font(SANS, "", 7.6)
        self.set_text_color(*MUTED)
        self.cell(self.cw / 2, 4.2, self.doc_subtitle, align="L")
        self.cell(self.cw / 2, 4.2, f"— {self.page_no()} —", align="R",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # ---------------------------------------------------------------- utils
    def start_section(self, name=None, level=0, **kwargs):
        super().start_section(name, level, **kwargs)
        self.sections.append((name or "", level, self.page_no()))

    def _measure(self, text: str, w: float, lh: float, *, font, size: float,
                 style: str = "", align: str = "J", markdown: bool = True,
                 padding: float = 0.0) -> float:
        """Do chieu cao khoi van ban (mm) khi ve trong khung rong w."""
        with self.local_context():
            self.set_font(font, style, size)
            h = self.multi_cell(max(w, 5.0), lh, text, align=align,
                                markdown=markdown, dry_run=True, output="HEIGHT",
                                padding=0)
        return float(h)

    def _block(self, text: str, w: float, lh: float, *, font, size: float,
               style: str = "", align: str = "J", color=INK, markdown: bool = True,
               padding: float = 0.0, x: Optional[float] = None) -> None:
        """Ve khoi van ban va tu ngat trang o muc DONG neu can."""
        self.set_font(font, style, size)
        self.set_text_color(*color)
        if x is not None:
            self.set_x(x)
        self.multi_cell(w, lh, text, align=align, markdown=markdown,
                        padding=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    def ensure(self, h: float) -> None:
        # chi ngat trang khi phan con lai that su khong du cho khoi nay
        if self.get_y() + h > self.page_break_trigger and h < 60:
            self.add_page()

    def _room(self) -> float:
        return self.page_break_trigger - self.get_y()

    def _break_if_tight(self, needed: float, slack: float) -> None:
        """Neu trang con it cho (`needed` + `slack`) thi sang trang moi, de
        tieu de khong bi bo lai mot minh o cuoi trang."""
        if self._room() < needed + slack:
            self.add_page()

    def para(self, text: str, size: float = BODY, color=INK, indent: float = 0.0,
             align: str = "J", lh: float = LH, gap: float = 1.9) -> None:
        w = self.cw - indent
        h = self._measure(text, w, lh, font=SANS, size=size, align=align)
        if self._room() < min(h, 2.2 * lh) + 0.8:
            self.add_page()
        self._block(text, w, lh, font=SANS, size=size, align=align, color=color,
                    x=self.l_margin + indent)
        self.ln(gap)

    # ------------------------------------------------------------- headings
    def h1(self, text: str) -> None:
        self.add_page()
        self.start_section(text, level=0)
        y = self.get_y()
        self.set_fill_color(*NAVY)
        self.rect(self.l_margin, y, self.cw, 11.0, style="F")
        self.set_font(SANS_B, "", 12.6)
        self.set_text_color(255, 255, 255)
        self.set_xy(self.l_margin + 4, y + 2.4)
        self.cell(self.cw - 8, 6.2, text.upper(), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_y(y + 15.0)
        self.set_text_color(*INK)

    def h2(self, text: str) -> None:
        h = self._measure(text, self.cw - 9, 5.4, font=SANS_B, size=11.0, align="L",
                          markdown=False)
        box_h = max(9.0, h + 4.4)
        self._break_if_tight(box_h, 4.4 + 3 * LH)
        self.start_section(text, level=1)
        y = self.get_y()
        self.set_fill_color(*PANEL)
        self.rect(self.l_margin, y, self.cw, box_h, style="F")
        self.set_fill_color(*BLUE)
        self.rect(self.l_margin, y, 1.4, box_h, style="F")
        self.set_font(SANS_B, "", 11.0)
        self.set_text_color(*NAVY)
        self.set_xy(self.l_margin + 4.2, y + 2.2)
        self.multi_cell(self.cw - 9.0, 5.4, text, align="L", markdown=False,
                        padding=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_y(y + box_h + 3.4)
        self.set_text_color(*INK)

    def h3(self, text: str) -> None:
        h = self._measure(text, self.cw, 5.2, font=SANS_B, size=10.2, align="L",
                          markdown=False)
        self._break_if_tight(h + 2.2, 3 * LH)
        self.set_font(SANS_B, "", 10.2)
        self.set_text_color(*TEAL)
        self.multi_cell(self.cw, 5.2, text, align="L", markdown=False,
                        padding=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(*INK)
        self.ln(2.2)

    def h4(self, text: str) -> None:
        self._break_if_tight(LH, 2 * LH)
        self.set_font(SANS_B, "", BODY)
        self.set_text_color(*NAVY)
        self.multi_cell(self.cw, LH, text, markdown=True, padding=0,
                        new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(*INK)
        self.ln(0.6)

    # --------------------------------------------------------------- blocks
    def item(self, marker: str, text: str, indent: float = 5.0,
             marker_w: float = 4.6, color=None) -> None:
        """Muc danh sach co thut le treo (hanging indent)."""
        w = self.cw - indent - marker_w
        h = self._measure(text, w, LH, font=SANS, size=BODY)
        if self._room() < min(h, 2.2 * LH) + 1.0:
            self.add_page()
        y = self.get_y()
        self.set_font(SANS, "", BODY)
        self.set_text_color(*(color or BLUE))
        self.set_xy(self.l_margin + indent, y)
        self.cell(marker_w, LH, marker, align="L")
        self._block(text, w, LH, font=SANS, size=BODY,
                    x=self.l_margin + indent + marker_w)
        self.ln(1.0)

    def bullet(self, text: str, indent: float = 5.0) -> None:
        self.item("\u2022", text, indent=indent, marker_w=4.6)

    def numitem(self, marker: str, text: str, indent: float = 5.0) -> None:
        self.item(marker, text, indent=indent, marker_w=6.8, color=INK)

    def formula(self, text: str) -> None:
        pad = 3.2
        w = self.cw - 2 * pad
        h = self._measure(text, w, 6.0, font=SERIF_B, size=10.2, align="C",
                          markdown=False)
        box_h = max(9.4, h + 4.0)
        if self._room() < box_h + 2.0:
            self.add_page()
        y = self.get_y()
        self.set_fill_color(247, 249, 252)
        self.set_draw_color(*RULE)
        self.set_line_width(0.25)
        self.rect(self.l_margin, y, self.cw, box_h, style="DF")
        self.set_font(SERIF_B, "", 10.2)
        self.set_text_color(22, 44, 86)
        self.set_xy(self.l_margin + pad, y + 2.0)
        self.multi_cell(w, 6.0, text, align="C", markdown=False, padding=0,
                        new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_y(y + box_h + 2.2)
        self.set_text_color(*INK)

    # ----------------------------------------------------------------- hop
    def box(self, title: str, body: List[str], bg, fg, accent) -> None:
        pad_x, pad_y, gap = 4.6, 3.0, 3.2
        w = self.cw - 2 * pad_x
        items = body if body else [""]
        # do chieu cao
        h = pad_y
        if title:
            h += self._measure(title, w, 5.0, font=SANS_B, size=9.6, align="L",
                               markdown=False) + 1.8
        for it in items:
            if it.startswith("\u2022  "):
                h += self._measure(it[3:], w - 4.6, LH - 0.25, font=SANS, size=9.1,
                                   align="L") + 1.5
            else:
                h += self._measure(it, w, LH - 0.25, font=SANS, size=9.1, align="L") + 1.5
        h += pad_y - 1.5

        if self.get_y() + h > self.page_break_trigger:
            self.add_page()
        y = self.get_y()
        self.set_fill_color(*bg)
        self.rect(self.l_margin, y, self.cw, h, style="F")
        self.set_fill_color(*accent)
        self.rect(self.l_margin, y, 1.5, h, style="F")

        cur = y + pad_y
        if title:
            self.set_font(SANS_B, "", 9.6)
            self.set_text_color(*fg)
            th = self._measure(title, w, 5.0, font=SANS_B, size=9.6, align="L",
                               markdown=False)
            self.set_xy(self.l_margin + pad_x, cur)
            self.multi_cell(w, 5.0, title, align="L", markdown=False, padding=0,
                            new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            cur += th + 1.8
        for it in items:
            bulleted = it.startswith("\u2022  ")
            txt = it[3:] if bulleted else it
            tw = w - 4.6 if bulleted else w
            ih = self._measure(txt, tw, LH - 0.25, font=SANS, size=9.1, align="L")
            if bulleted:
                self.set_font(SANS, "", 9.1)
                self.set_text_color(*BLUE)
                self.set_xy(self.l_margin + pad_x, cur)
                self.cell(4.6, LH - 0.25, "\u2022")
            self.set_font(SANS, "", 9.1)
            self.set_text_color(*INK)
            self.set_xy(self.l_margin + pad_x + (4.6 if bulleted else 0), cur)
            self.multi_cell(tw, LH - 0.25, txt, align="L", markdown=True, padding=0,
                            new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            cur += ih + 1.5
        self.set_y(y + h + gap)
        self.set_text_color(*INK)

    def note(self, title, body):
        self.box(title, body, BOX_INFO_BG, BOX_INFO_FG, BLUE)

    def warn(self, title, body):
        self.box(title, body, BOX_WARN_BG, BOX_WARN_FG, (186, 60, 50))

    def tip(self, title, body):
        self.box(title, body, BOX_TIP_BG, BOX_TIP_FG, (200, 142, 26))

    def example(self, title, body):
        self.box(title, body, BOX_EX_BG, BOX_EX_FG, (36, 130, 74))

    # ---------------------------------------------------------------- bang
    def table(self, rows: List[List[str]], font_size: float = SMALL,
              aligns: Optional[List[str]] = None) -> None:
        ncol = len(rows[0])
        # Bang nhieu cot: bat dau tu co chu nho hon de cac o ngan khong bi ngat
        if ncol >= 8:
            font_size = 7.4
        elif ncol >= 6:
            font_size = 8.0
        font_size = self._fit_font(rows, font_size)
        widths = self._auto_widths(rows, font_size)
        if aligns is None:
            aligns = ["L"] + ["C"] * (ncol - 1)

        lh = font_size * 0.46 + 1.15

        def row_height(cells: List[str], head: bool) -> float:
            hmax = 0.0
            for c, w in zip(cells, widths):
                if not c.strip():
                    continue
                h = self._measure(c, w - 2 * self._CELL_PAD, lh,
                                  font=SANS_B if head else SANS, size=font_size,
                                  align="L", markdown=False)
                hmax = max(hmax, h)
            return max(hmax, font_size * 0.5) + 2.3

        heights = [row_height(r, ri == 0) for ri, r in enumerate(rows)]
        total_h = sum(heights)
        full_page = self.page_break_trigger - self.t_margin - 3.0
        # Bang vua mot trang -> khong cat vat: dua ca bang sang trang moi.
        if total_h <= full_page and self.get_y() + total_h > self.page_break_trigger:
            self.add_page()
            if self.get_y() + total_h > self.page_break_trigger:
                pass

        for ri, row in enumerate(rows):
            head = ri == 0
            rh = heights[ri]
            if self.get_y() + rh > self.page_break_trigger:
                self.add_page()
                # ve lai dong tieu de o trang moi cho de doc
                if ri > 0 and ncol > 1:
                    self._table_header(rows[0], widths, font_size, lh,
                                       aligns, row_height(rows[0], True))
            y = self.get_y()
            self.set_fill_color(*(TBL_HEAD_BG if head else
                                  (TBL_ALT_BG if ri % 2 == 0 else (255, 255, 255))))
            self.rect(self.l_margin, y, self.cw, rh, style="F")
            x = self.l_margin
            for ci, (cell_txt, w) in enumerate(zip(row, widths)):
                self.set_font(SANS_B if (head or ci == 0) else SANS, "", font_size)
                self.set_text_color(*(TBL_HEAD_FG if head else INK))
                self.set_xy(x + self._CELL_PAD, y + 1.15)
                align = aligns[ci] if ci < len(aligns) else "L"
                self.multi_cell(w - 2 * self._CELL_PAD, lh,
                                cell_txt.replace("**", ""), align=align,
                                markdown=False, padding=0,
                                new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                x += w
            self.set_draw_color(*RULE)
            self.set_line_width(0.22)
            self.set_y(y)
            self.set_x(self.l_margin)
            self.cell(self.cw, rh, "", border=1)
            x = self.l_margin
            for w in widths[:-1]:
                x += w
                self.line(x, y, x, y + rh)
            self.set_y(y + rh)
        self.set_text_color(*INK)
        self.ln(2.8)

    def _table_header(self, row, widths, font_size, lh, aligns, rh) -> None:
        y = self.get_y()
        self.set_fill_color(*TBL_HEAD_BG)
        self.rect(self.l_margin, y, self.cw, rh, style="F")
        x = self.l_margin
        for ci, (cell_txt, w) in enumerate(zip(row, widths)):
            self.set_font(SANS_B, "", font_size)
            self.set_text_color(*TBL_HEAD_FG)
            self.set_xy(x + self._CELL_PAD, y + 1.15)
            align = aligns[ci] if ci < len(aligns) else "L"
            self.multi_cell(w - 2 * self._CELL_PAD, lh, cell_txt.replace("**", ""),
                            align=align, markdown=False, padding=0,
                            new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            x += w
        self.set_draw_color(*RULE)
        self.set_line_width(0.22)
        self.set_y(y)
        self.set_x(self.l_margin)
        self.cell(self.cw, rh, "", border=1)
        x = self.l_margin
        for w in widths[:-1]:
            x += w
            self.line(x, y, x, y + rh)
        self.set_y(y + rh)

    _CELL_PAD = 2.6      # khoang dem 2 ben trong o (do minh dat)
    _CELL_SLACK = 0.8
    _CELL_MARGIN = 1.0   # fpdf2 tu chua them ~1 mm moi ben khi nguong dong

    def _min_cell_width(self, text: str, size: float) -> float:
        """Be rong nho nhat de multi_cell khong bao loi (do bang font DAM —
        font rong nhat — de dung duoc cho ca o thuong lan o dam)."""
        widest = 0.0
        for fam in (SANS, SANS_B):
            with self.local_context():
                self.set_font(fam, "", size)
                for word in text.split(" "):
                    if word:
                        widest = max(widest, self.get_string_width(word))
        return widest + 2 * self._CELL_PAD + 2 * self._CELL_MARGIN + self._CELL_SLACK

    def _min_total(self, rows: List[List[str]], size: float) -> float:
        return sum(max((self._min_cell_width((r[ci] if ci < len(r) else ""), size)
                        for r in rows), default=6.0)
                   for ci in range(len(rows[0])))

    def _fit_font(self, rows: List[List[str]], size: float) -> float:
        """Giam co chu cho den khi moi cot du rong (khong nho hon 6,4 pt)."""
        s = size
        while s > 6.4:
            mins = [max((self._min_cell_width((r[ci] if ci < len(r) else ""), s)
                         for r in rows), default=6.0)
                    for ci in range(len(rows[0]))]
            if sum(mins) <= self.cw:
                return s
            s -= 0.4
        return s

    def _auto_widths(self, rows: List[List[str]], size: float) -> List[float]:
        ncol = len(rows[0])
        if ncol == 1:
            return [self.cw]
        min_w, want_w = [], []
        for ci in range(ncol):
            mw, ww = 0.0, 0.0
            for r in rows:
                txt = (r[ci] if ci < len(r) else "").replace("**", "").strip()
                if not txt:
                    continue
                mw = max(mw, self._min_cell_width(txt, size))
                with self.local_context():
                    self.set_font(SANS, "", size)
                    ww = max(ww, self.get_string_width(txt) / 2.6 + 2 * self._CELL_PAD)
            # Neu ca cot chi chua noi dung ngan thi cho no du rong de khong
            # bi ngat giua cum ki hieu, vi du "(a; b)" hay "[a; +inf)".
            full_w = 0.0
            for r in rows:
                t2 = (r[ci] if ci < len(r) else "").replace("**", "").strip()
                if not t2:
                    continue
                for fam in (SANS, SANS_B):
                    with self.local_context():
                        self.set_font(fam, "", size)
                        full_w = max(full_w, self.get_string_width(t2))
            short_limit = 0.42 * self.cw if ncol >= 6 else 0.30 * self.cw
            if full_w <= short_limit:
                ww = max(ww, full_w + 2 * self._CELL_PAD + 2 * self._CELL_MARGIN
                         + self._CELL_SLACK)
            m = max(mw, 7.0)
            min_w.append(m)
            want_w.append(max(m, ww))
        total_min = sum(min_w)
        if total_min >= self.cw:                       # khong the: chia theo min
            k = self.cw / total_min
            return [w * k for w in min_w]
        extra = max(0.0, self.cw - total_min)
        flex = [max(0.0, w - m) for w, m in zip(want_w, min_w)]
        tf = sum(flex)
        if tf <= 0.0:            # moi cot da rong nhat: chia deu theo min
            out = [m + extra * m / total_min for m in min_w]
        else:
            out = [m + extra * f / tf for m, f in zip(min_w, flex)]
        # bao dam tuyet doi: khong cot nao hep hon min, tong dung bang cw
        out = [max(o, m) for o, m in zip(out, min_w)]
        total = sum(out)
        if total > 0:
            out = [o * self.cw / total for o in out]
            out = [max(o, m) for o, m in zip(out, min_w)]
            drift = self.cw - sum(out)
            if abs(drift) > 0.01 and len(out) > 1:
                # tra phan du ve cot rong rai nhat
                k = out.index(max(out))
                out[k] += drift
        return out

    # ---------------------------------------------------------------- hinh
    def figure(self, name: str, caption: str, h: float) -> None:
        cap_h = 0.0
        if caption:
            cap_h = self._measure(caption, self.cw, LH - 0.7, font=SANS,
                                  size=SMALL, align="C") + 2.0
        if self._room() < h + cap_h + 2.0:
            self.add_page()
        y = self.get_y()
        self.set_fill_color(252, 253, 255)
        self.set_draw_color(*RULE)
        self.set_line_width(0.25)
        self.rect(self.l_margin, y, self.cw, h, style="DF")
        fn = self.figures.get(name)
        if fn:
            self.set_xy(self.l_margin, y)
            fn(self, self.l_margin + 2.0, y + 2.0, self.cw - 4.0, h - 4.0)
        else:
            self.set_font(SANS, "", SMALL)
            self.set_text_color(*MUTED)
            self.set_xy(self.l_margin, y + h / 2 - 2)
            self.cell(self.cw, 4, f"[hinh: {name}]", align="C")
        self.set_y(y + h + 1.2)
        if caption:
            self.set_font(SANS, "", SMALL)
            self.set_text_color(*MUTED)
            self.multi_cell(self.cw, LH - 0.7, caption, align="C", padding=0,
                            new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(*INK)
        self.ln(2.4)

    # --------------------------------------------------------- ve hinh phu
    def dline(self, x1, y1, x2, y2, color=RULE, width=0.3, dash=0.0):
        self.set_draw_color(*color)
        self.set_line_width(width)
        if dash:
            self.dashed_line(x1, y1, x2, y2, dash_length=dash, space_length=dash)
        else:
            self.line(x1, y1, x2, y2)

    def dtext(self, x, y, txt, size=7.4, family=SANS, style="", color=MUTED,
              align="L", w=0):
        self.set_font(family, style, size)
        self.set_text_color(*color)
        yy = y - size * 0.20
        self.set_xy(x, yy)
        self.cell(w, size * 0.42, txt, align=align)

    def dtext_c(self, x, y, txt, size=7.4, family=SANS, style="", color=MUTED):
        self.set_font(family, style, size)
        self.set_text_color(*color)
        w = self.get_string_width(txt) + 1.0
        self.set_xy(x - w / 2, y - size * 0.20)
        self.cell(w, size * 0.42, txt, align="C")

    def arrow(self, x1, y1, x2, y2, color=INK, width=0.35, head=1.6):
        self.dline(x1, y1, x2, y2, color=color, width=width)
        ang = math.atan2(y2 - y1, x2 - x1)
        for s in (-1, 1):
            a = ang + s * math.radians(22)
            self.dline(x2, y2, x2 - head * math.cos(a), y2 - head * math.sin(a),
                       color=color, width=width)

    def poly(self, pts, fill=(214, 231, 247), border=None, width=0.3):
        with self.local_context():
            self.set_fill_color(*fill)
            self.set_draw_color(*(border or fill))
            self.set_line_width(width)
            self.draw_polygon(pts, style="DF" if border else "F")

    def circle_fill(self, cx, cy, r, fill, border=NAVY, width=0.35):
        with self.local_context():
            self.set_fill_color(*fill)
            self.set_draw_color(*border)
            self.set_line_width(width)
            self.ellipse(cx - r, cy - r, 2 * r, 2 * r, style="DF")

    draw_polygon = FPDF.polygon


# ---------------------------------------------------------------------------
# Hinh ve: moi ham nhan (d, x, y, w, h) va CHI ve trong khung do.
# ---------------------------------------------------------------------------
def _clip_poly(poly, a, b, c):
    """Giu phan da giac thoa a*x + b*y <= c (Sutherland-Hodgman)."""
    def f(p):
        return c - (a * p[0] + b * p[1])

    def interp(p, q):
        f1, f2 = f(p), f(q)
        t = f1 / (f1 - f2) if (f1 - f2) != 0 else 0.0
        return (p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]))

    out = []
    n = len(poly)
    for i in range(n):
        cur, nxt = poly[i], poly[(i + 1) % n]
        ci, ni = f(cur) >= 0, f(nxt) >= 0
        if ci:
            out.append(cur)
        if ci != ni:
            out.append(interp(cur, nxt))
    return out


def _clip_seg(p, q, xmin, xmax, ymin, ymax):
    """Cat doan thang pq theo hinh chu nhat (Liang-Barsky)."""
    x1, y1 = p
    dx, dy = q[0] - x1, q[1] - y1
    t0, t1 = 0.0, 1.0
    for pp, qq in ((-dx, x1 - xmin), (dx, xmax - x1),
                   (-dy, y1 - ymin), (dy, ymax - y1)):
        if pp == 0:
            if qq < 0:
                return None
            continue
        r = qq / pp
        if pp < 0:
            t0 = max(t0, r)
        else:
            t1 = min(t1, r)
        if t0 > t1:
            return None
    return ((x1 + t0 * dx, y1 + t0 * dy), (x1 + t1 * dx, y1 + t1 * dy))


def _lens_points(c1, c2, r, n=72):
    """Mien giao cua hai hinh tron cung ban kinh.

    Giao = hop cua hai "hinh vien phan" (circular segment). Dung goc cuc de
    sinh dung cung tron, tranh da giac tu cat nhu cach ghep cung gian tiep.
    """
    (x1, y1), (x2, y2) = c1, c2
    dd = math.hypot(x2 - x1, y2 - y1)
    if dd >= 2 * r or dd == 0:
        return []
    a = dd / 2
    h = math.sqrt(max(0.0, r * r - a * a))
    alpha = math.atan2(h, a)                  # nua goc mo cua cung
    th = math.atan2(y2 - y1, x2 - x1)
    pts = []
    # cung thuoc hinh tron 1, huong ve phia tam 2
    for i in range(n + 1):
        t = th - alpha + 2 * alpha * i / n
        pts.append((x1 + r * math.cos(t), y1 + r * math.sin(t)))
    # cung thuoc hinh tron 2, huong ve phia tam 1 (dao chieu de dong kin)
    for i in range(n + 1):
        t = th + math.pi + alpha - 2 * alpha * i / n
        pts.append((x2 + r * math.cos(t), y2 + r * math.sin(t)))
    return pts


def fig_venn(d, x, y, w, h):
    cx, cy = x + w / 2, y + h / 2
    r = min(h * 0.36, w * 0.17)
    sep = r * 0.74
    c1, c2 = (cx - sep, cy), (cx + sep, cy)
    for c in (c1, c2):
        d.circle_fill(c[0], c[1], r, (233, 243, 253), border=NAVY, width=0.5)
    lens = _lens_points(c1, c2, r)
    if lens:
        with d.local_context():
            d.set_draw_color(30, 96, 178)
            d.set_line_width(0.35)
            d.set_fill_color(126, 178, 224)
            d.draw_polygon(lens, style="DF")
    for c in (c1, c2):
        with d.local_context():
            d.set_draw_color(*NAVY)
            d.set_line_width(0.5)
            d.ellipse(c[0] - r, c[1] - r, 2 * r, 2 * r, style="D")
    d.dtext(c1[0] - r + 2.4, cy - 1.4, "A", size=9.6, family=SANS_B, color=NAVY)
    d.dtext(c2[0] + r - 6.2, cy - 1.4, "B", size=9.6, family=SANS_B, color=NAVY)
    d.dtext_c(cx, cy + 1.0, "A ∩ B", size=8.2, family=SANS_B, color=(14, 50, 100))
    d.dtext_c(cx, y + h - 5.0, "Phần tô đậm biểu diễn tập A ∩ B", size=7.2, color=MUTED)


def fig_number_line(d, x, y, w, h):
    lo, hi = -6.5, 8.5
    x0 = x + 22
    pw = w - 30

    def X(v):
        return x0 + (v - lo) / (hi - lo) * pw

    y1, y2 = y + 10, y + h - 12
    for yy, lab, a, b, a_open, b_open, col in (
        (y1, "A = (−3; 4]", -3, 4, True, False, (30, 96, 178)),
        (y2, "B = [0; +∞)", 0, 8, False, True, (13, 104, 104)),
    ):
        d.dline(x0, yy, x0 + pw, yy, color=(150, 158, 168), width=0.45)
        for v in range(-6, 9, 2):
            d.dline(X(v), yy - 1.0, X(v), yy + 1.0, color=(150, 158, 168), width=0.3)
            d.dtext_c(X(v), yy + 3.6, str(v), size=6.4)
        d.dline(X(a), yy, X(b), yy, color=col, width=1.7)
        for v, is_open in ((a, a_open), (b, b_open)):
            d.circle_fill(X(v), yy, 1.4, (255, 255, 255) if is_open else col,
                          border=col, width=0.5)
        d.dtext(x0 - 21, yy - 1.4, lab, size=7.8, family=SANS_B, color=col)
    d.arrow(x0 + pw - 3.0, y2, x0 + pw + 2.0, y2, color=(150, 158, 168), width=0.4)
    d.dtext_c(x0 + pw + 4.6, y2 - 1.6, "x", size=7.4, family=SERIF)


def _axes(d, x, y, w, h, xmin, xmax, ymin, ymax, xstep=1, ystep=1,
          draw=True):
    def X(v):
        return x + (v - xmin) / (xmax - xmin) * w

    def Y(v):
        return y + h - (v - ymin) / (ymax - ymin) * h

    if not draw:
        return X, Y

    d.dline(X(xmin), Y(0), X(xmax), Y(0), color=(120, 128, 140), width=0.45)
    d.dline(X(0), Y(ymin), X(0), Y(ymax), color=(120, 128, 140), width=0.45)
    d.arrow(X(xmax) - 4.0, Y(0), X(xmax), Y(0), color=(120, 128, 140), width=0.45)
    d.arrow(X(0), Y(ymax) + 4.0, X(0), Y(ymax), color=(120, 128, 140), width=0.45)
    d.dtext(X(xmax) - 4.6, Y(0) + 1.4, "x", size=7.2, family=SERIF)
    d.dtext(X(0) + 1.4, Y(ymax) + 1.2, "y", size=7.2, family=SERIF)
    d.dtext(X(0) - 4.6, Y(0) + 1.4, "O", size=6.6, family=SERIF)
    for v in range(int(xmin) + xstep, int(xmax) + 1, xstep):
        if v == 0:
            continue
        d.dline(X(v), Y(0) - 0.8, X(v), Y(0) + 0.8, color=(165, 172, 182), width=0.25)
        d.dtext_c(X(v), Y(0) + 3.2, str(v), size=5.9)
    for v in range(int(ymin) + ystep, int(ymax) + 1, ystep):
        if v == 0:
            continue
        d.dline(X(0) - 0.8, Y(v), X(0) + 0.8, Y(v), color=(165, 172, 182), width=0.25)
        d.dtext(X(0) - 6.8, Y(v) - 1.3, str(v), size=5.9, w=5.4, align="R")
    return X, Y


def fig_halfplane(d, x, y, w, h):
    pw, ph = w * 0.55, h - 13
    px, py = x + 13, y + 5
    xmin, xmax, ymin, ymax = -1, 7, -1, 8
    X, Y = _axes(d, px, py, pw, ph, xmin, xmax, ymin, ymax, xstep=1, ystep=2,
                 draw=False)
    box = [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]
    reg = _clip_poly(box, 3, 2, 12)
    d.poly([(X(a), Y(b)) for a, b in reg], fill=(210, 231, 248))
    seg = _clip_seg((-2, 9), (6, -3), xmin, xmax, ymin, ymax)
    if seg:
        d.dline(X(seg[0][0]), Y(seg[0][1]), X(seg[1][0]), Y(seg[1][1]),
                color=(30, 96, 178), width=0.85)
    _axes(d, px, py, pw, ph, xmin, xmax, ymin, ymax, xstep=1, ystep=2)
    for vx, vy in ((4, 0), (0, 6)):
        d.circle_fill(X(vx), Y(vy), 1.1, NAVY, border=NAVY)
    d.dtext(X(1.0), Y(7.6), "d: 3x + 2y = 12", size=6.8, family=SERIF, color=NAVY)
    d.dtext_c(X(0.5), Y(2.2), "Miền nghiệm", size=7.0, family=SANS_B,
              color=(22, 72, 136))
    tx = px + pw + 13
    lines = ["Điểm tô đậm:", "A(4; 0) trên Ox,", "B(0; 6) trên Oy.",
             "Miền nghiệm là nửa", "mặt phẳng bờ d, chứa", "O, kể cả d."]
    for i, t in enumerate(lines):
        d.dtext(tx, y + 8 + i * 5.4, t, size=6.9,
                color=NAVY if i == 0 else INK,
                family=SANS_B if i == 0 else SANS)


def fig_system(d, x, y, w, h):
    pw, ph = w * 0.55, h - 13
    px, py = x + 13, y + 5
    xmin, xmax, ymin, ymax = -1, 14.5, -1, 14.5
    X, Y = _axes(d, px, py, pw, ph, xmin, xmax, ymin, ymax, xstep=2, ystep=2,
                 draw=False)
    box = [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]
    reg = box
    for (a, b, c) in ((-1, 0, 0), (0, -1, 0), (4, 3, 48), (2, 3, 36)):
        reg = _clip_poly(reg, a, b, c)
    if reg:
        d.poly([(X(a), Y(b)) for a, b in reg], fill=(205, 230, 216))
    for (p1, p2, col) in (((18, -8), (-3, 20), (186, 100, 30)),
                          ((21, -2), (-4, 16), (13, 104, 104))):
        seg = _clip_seg(p1, p2, xmin, xmax, ymin, ymax)
        if seg:
            d.dline(X(seg[0][0]), Y(seg[0][1]), X(seg[1][0]), Y(seg[1][1]),
                    color=col, width=0.85)
    _axes(d, px, py, pw, ph, xmin, xmax, ymin, ymax, xstep=2, ystep=2)
    for vx, vy in ((0, 0), (12, 0), (6, 8), (0, 12)):
        d.circle_fill(X(vx), Y(vy), 1.0, NAVY, border=NAVY)
    d.dtext(X(6) + 2.2, Y(8) - 1.0, "(6; 8)", size=6.8, family=SANS_B, color=NAVY)
    d.dtext_c(X(2.0), Y(6.0), "Miền", size=6.8, family=SANS_B, color=(16, 92, 58))
    d.dtext_c(X(2.0), Y(4.4), "nghiệm", size=6.8, family=SANS_B, color=(16, 92, 58))
    tx = px + pw + 13
    d.dtext(tx, y + 6, "Bốn đỉnh của miền:", size=6.9, family=SANS_B, color=NAVY)
    for i, t in enumerate(["O(0; 0)", "(12; 0)", "(6; 8)", "(0; 12)"]):
        d.dtext(tx + 1, y + 11.5 + i * 5.0, "• " + t, size=6.8, color=INK)
    d.dtext(tx, y + 34, "F = ax + by đạt GTLN,", size=6.7, family=SANS_B, color=NAVY)
    d.dtext(tx, y + 39, "GTNN tại một trong", size=6.7, color=INK)
    d.dtext(tx, y + 44, "các đỉnh.", size=6.7, color=INK)


def fig_triangle(d, x, y, w, h):
    gy = y + h - 12
    A, B, Cc = x + 8, x + 46, x + 80
    Dy = y + 6
    d.dline(x + 2, gy, x + w * 0.58, gy, color=(150, 158, 168), width=0.5)
    d.dline(Cc, gy, Cc, Dy, color=NAVY, width=0.6, dash=1.2)
    d.dline(A, gy, Cc, Dy, color=(186, 60, 50), width=0.6)
    d.dline(B, gy, Cc, Dy, color=(30, 96, 178), width=0.6)
    d.dline(Cc - 3.0, gy, Cc - 3.0, gy - 3.0, color=NAVY, width=0.3)
    d.dline(Cc - 3.0, gy - 3.0, Cc, gy - 3.0, color=NAVY, width=0.3)
    d.circle_fill(Cc, gy, 1.0, INK, border=INK)
    d.dtext_c(A, gy + 4.6, "A", size=8.0, family=SANS_B, color=INK)
    d.dtext_c(B, gy + 4.6, "B", size=8.0, family=SANS_B, color=INK)
    d.dtext_c(Cc, gy + 4.6, "C", size=8.0, family=SANS_B, color=INK)
    d.dtext_c(Cc, Dy - 4.6, "D", size=8.0, family=SANS_B, color=INK)
    d.dtext_c((A + B) / 2, gy + 4.6, "24 m", size=6.8, color=MUTED)
    d.dtext_c(A + 6.0, gy - 4.6, "35°", size=7.0, color=(186, 60, 50))
    d.dtext_c(B + 5.4, gy - 4.6, "50°", size=7.0, color=(30, 96, 178))
    d.dtext(Cc + 2.2, (gy + Dy) / 2, "h = ?", size=7.4, family=SERIF, color=NAVY)
    tx = x + w * 0.60
    d.dtext(tx, y + 6, "Trong tam giác ABD:", size=7.0, family=SANS_B, color=NAVY)
    for i, s in enumerate(["góc DAB = 35°",
                           "góc ABD = 180° − 50° = 130°",
                           "⇒ góc ADB = 180° − 35° − 130°",
                           "            = 15°"]):
        d.dtext(tx + 1, y + 12 + i * 5.0, ("• " if i < 3 else "   ") + s,
                size=6.8, color=INK)


def fig_vectors(d, x, y, w, h):
    Ax, Ay = x + 6, y + h - 8
    Bx, By = x + 52, y + h - 6
    Dx, Dy = x + 22, y + 18
    Cx, Cy = Bx + (Dx - Ax), By + (Dy - Ay)
    Ox, Oy = (Ax + Cx) / 2, (Ay + Cy) / 2
    for p, q in (((Ax, Ay), (Bx, By)), ((Bx, By), (Cx, Cy)),
                 ((Cx, Cy), (Dx, Dy)), ((Dx, Dy), (Ax, Ay))):
        d.dline(p[0], p[1], q[0], q[1], color=(140, 148, 160), width=0.45)
    d.dline(Ax, Ay, Cx, Cy, color=(200, 208, 218), width=0.3, dash=1.2)
    d.dline(Bx, By, Dx, Dy, color=(200, 208, 218), width=0.3, dash=1.2)
    d.arrow(Ax, Ay, Bx, By, color=(30, 96, 178), width=0.75, head=2.3)
    d.arrow(Dx, Dy, Cx, Cy, color=(30, 96, 178), width=0.75, head=2.3)
    d.arrow(Ax, Ay, Dx, Dy, color=(186, 60, 50), width=0.75, head=2.3)
    d.arrow(Cx, Cy, Bx, By, color=(186, 60, 50), width=0.75, head=2.3)
    for xx, yy, lab, dx, dy in ((Ax, Ay, "A", -4.2, 3.6), (Bx, By, "B", 1.6, 3.6),
                                (Cx, Cy, "C", 1.8, 1.0), (Dx, Dy, "D", -4.4, -2.2)):
        d.dtext(xx + dx, yy + dy, lab, size=8.0, family=SANS_B, color=INK)
    d.circle_fill(Ox, Oy, 0.95, INK, border=INK)
    d.dtext(Ox + 1.4, Oy + 1.4, "O", size=7.4, family=SANS_B, color=INK)
    tx = x + w * 0.52
    d.dtext(tx, y + 8, "Trong hình bình hành ABCD:", size=7.0, family=SANS_B, color=NAVY)
    d.dtext(tx + 1, y + 14, "vectơ AB = vectơ DC", size=7.2, family=SANS_B,
            color=(30, 96, 178))
    d.dtext(tx + 1, y + 20, "vectơ AD = vectơ BC", size=7.2, family=SANS_B,
            color=(186, 60, 50))
    d.dtext(tx + 1, y + 26, "suy ra vectơ AD = −vectơ CB", size=7.0, color=MUTED)


def fig_unit_circle(d, x, y, w, h):
    cx, cy = x + 30, y + h - 10
    r = min(h - 14, 22)
    d.dline(cx - 26, cy, cx + r + 6, cy, color=(120, 128, 140), width=0.45)
    d.dline(cx, cy + 3, cx, cy - r - 6, color=(120, 128, 140), width=0.45)
    d.arrow(cx + r + 3, cy, cx + r + 6, cy, color=(120, 128, 140), width=0.4)
    d.arrow(cx, cy - r - 3, cx, cy - r - 6, color=(120, 128, 140), width=0.4)
    pts = [(cx + r * math.cos(math.radians(180 * i / 90)),
            cy - r * math.sin(math.radians(180 * i / 90))) for i in range(91)]
    with d.local_context():
        d.set_draw_color(*NAVY)
        d.set_line_width(0.65)
        for i in range(90):
            d.line(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1])
    al = math.radians(125)
    Mx, My = cx + r * math.cos(al), cy - r * math.sin(al)
    d.arrow(cx, cy, Mx, My, color=(186, 60, 50), width=0.7, head=2.0)
    d.dline(Mx, My, Mx, cy, color=(30, 96, 178), width=0.6, dash=0.9)
    d.dline(cx, cy, Mx, cy, color=(13, 104, 104), width=0.6, dash=0.9)
    for i in range(8):
        t1 = math.radians(125 * i / 8)
        t2 = math.radians(125 * (i + 1) / 8)
        d.dline(cx + 7 * math.cos(t1), cy - 7 * math.sin(t1),
                cx + 7 * math.cos(t2), cy - 7 * math.sin(t2),
                color=(90, 98, 110), width=0.3)
    d.dtext_c(cx + 10, cy - 7.6, "α", size=8.2, family=SERIF, color=INK)
    d.dtext(Mx - 6.0, My - 7.4, "M(cosα; sinα)", size=7.0, family=SERIF,
            color=(186, 60, 50))
    d.dtext_c((cx + Mx) / 2, cy - 4.6, "cos α", size=6.8, family=SERIF,
              color=(13, 104, 104))
    d.dtext(Mx + 1.4, (cy + My) / 2 + 1.0, "sin α", size=6.8, family=SERIF,
            color=(30, 96, 178))
    d.dtext(cx - 4.8, cy + 0.6, "O", size=7.0, family=SERIF)
    d.dtext(cx + r + 7, cy + 1.0, "x", size=7.0, family=SERIF)
    d.dtext(cx + 1.2, cy - r - 8, "y", size=7.0, family=SERIF)
    tx = cx + r + 16
    d.dtext(tx, y + 7, "Với 0° ≤ α ≤ 180°:", size=7.4, family=SANS_B, color=NAVY)
    for i, s in enumerate([
        "M(cosα; sinα) trên nửa đường tròn đơn vị",
        "sinα = tung độ của M, luôn ≥ 0",
        "cosα = hoành độ của M",
        "α nhọn: sin, cos, tan, cot đều dương",
        "α tù: sin > 0; cos, tan, cot âm",
    ]):
        d.dtext(tx + 1, y + 13 + i * 6.4, "• " + s, size=6.9, color=INK)


DEFAULT_FIGURES = {
    "venn": (fig_venn, 50),
    "trucso": (fig_number_line, 40),
    "nua_mp": (fig_halfplane, 54),
    "mien_he": (fig_system, 54),
    "do_thap": (fig_triangle, 44),
    "vecto": (fig_vectors, 46),
    "duong_tron": (fig_unit_circle, 54),
}
