# -*- coding: utf-8 -*-
"""
Bien soan de cuong on tap Toan 10 - Giua ky I (chuong trinh Ket noi tri thuc).
Nguon du lieu: MA TRAN TOAN 10 - GIUAKY I.docx (TRUONG THPT HA HUY TAP,
nam hoc 2026-2027). Noi dung cac cau trắc nghiệm duoc bien soan lai theo
chinh xac phan bo cua ma tran de (ma tran chi ghi ma cau va yeu cau,
khong chua van ban cau hoi goc).
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table,
    TableStyle, KeepTogether, PageBreak, HRFlowable,
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ----------------------------------------------------------------------------
# Fonts (Unicode Vietnamese: DejaVu)
# ----------------------------------------------------------------------------
FDIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("DVS", f"{FDIR}/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVSB", f"{FDIR}/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DVSO", f"{FDIR}/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVSBO", f"{FDIR}/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFontFamily("DVS", normal="DVS", bold="DVSB", italic="DVSO", boldItalic="DVSBO")

PAGE_W, PAGE_H = A4
M_L = 16 * mm
M_R = 16 * mm
M_T = 20 * mm
M_B = 18 * mm

NAVY = colors.HexColor("#1f3864")
BLUE = colors.HexColor("#2e74b5")
LIGHT = colors.HexColor("#dde8f5")
LIGHT2 = colors.HexColor("#f2f6fb")
GREY = colors.HexColor("#595959")
GREEN = colors.HexColor("#2e7d32")
RED = colors.HexColor("#b71c1c")

# ----------------------------------------------------------------------------
# Styles
# ----------------------------------------------------------------------------
def st(name, **kw):
    base = dict(fontName="DVS", fontSize=10, leading=13.5, textColor=colors.black,
                alignment=TA_JUSTIFY, spaceAfter=4)
    base.update(kw)
    return ParagraphStyle(name, **base)

S_TITLE = st("title", fontName="DVSB", fontSize=20, leading=25, alignment=TA_CENTER,
             textColor=NAVY, spaceAfter=6)
S_SUB = st("sub", fontName="DVS", fontSize=12, leading=16, alignment=TA_CENTER,
           textColor=GREY, spaceAfter=2)
S_H1 = st("h1", fontName="DVSB", fontSize=14, leading=18, textColor=NAVY,
          spaceBefore=14, spaceAfter=6, alignment=TA_LEFT)
S_H2 = st("h2", fontName="DVSB", fontSize=11.5, leading=15, textColor=BLUE,
          spaceBefore=10, spaceAfter=4, alignment=TA_LEFT)
S_H3 = st("h3", fontName="DVSBO", fontSize=10.5, leading=14, textColor=colors.black,
          spaceBefore=8, spaceAfter=3, alignment=TA_LEFT)
S_BODY = st("body")
S_BODY_C = st("bodyc", alignment=TA_CENTER)
S_BULLET = st("bullet", leftIndent=10, bulletIndent=2, spaceAfter=2.5)
S_MATH = st("math", fontName="DVS", fontSize=10.5, leading=15, alignment=TA_CENTER,
            spaceAfter=4)
S_NOTE = st("note", fontName="DVSO", fontSize=9, leading=12, textColor=GREY,
            spaceAfter=5)
S_TBL = st("tbl", fontSize=8.6, leading=11, alignment=TA_LEFT, spaceAfter=0)
S_TBL_C = st("tblc", fontSize=8.6, leading=11, alignment=TA_CENTER, spaceAfter=0)
S_TBL_B = st("tblb", fontName="DVSB", fontSize=8.6, leading=11, alignment=TA_LEFT, spaceAfter=0)
S_TBL_BC = st("tblbc", fontName="DVSB", fontSize=8.6, leading=11, alignment=TA_CENTER, spaceAfter=0)
S_ANS = st("ans", fontSize=9.5, leading=13, leftIndent=10, spaceAfter=3)
S_QUEST = st("quest", fontSize=9.8, leading=13.5, leftIndent=6, spaceAfter=3)

def P(text, style=S_BODY):
    return Paragraph(text, style)

def bullets(items, style=S_BULLET, char="&bull;"):
    return [Paragraph(f"{char}&nbsp;&nbsp;{it}", style) for it in items]

def callout(text, bg=LIGHT, border=BLUE):
    t = Table([[P(text, st("co", fontSize=9.2, leading=12.5, textColor=colors.black))]],
              colWidths=[PAGE_W - M_L - M_R])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("BOX", (0, 0), (-1, -1), 0.8, border),
        ("LINEBEFORE", (0, 0), (0, -1), 3, border),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t

def make_table(header, rows, widths, align_center_cols=(), header_bg=NAVY,
               zebra=True, fontsize=8.6):
    data = [[P(f"<b>{h}</b>", st("hh", fontName="DVSB", fontSize=fontsize,
             leading=fontsize + 3, textColor=colors.white,
             alignment=TA_CENTER if i in align_center_cols else TA_LEFT))
             for i, h in enumerate(header)]]
    for r in rows:
        data.append([P(c, S_TBL_C if i in align_center_cols else S_TBL) for i, c in enumerate(r)])
    t = Table(data, colWidths=widths, repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), header_bg),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#8ea9c4")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ]
    if zebra:
        for i in range(1, len(data)):
            if i % 2 == 0:
                style.append(("BACKGROUND", (0, i), (-1, i), LIGHT2))
    t.setStyle(TableStyle(style))
    return t

# ----------------------------------------------------------------------------
# Page furniture
# ----------------------------------------------------------------------------
DOC_TITLE = "DE CUONG ON TAP TOAN 10 - GIUA KY I"

def on_page(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(NAVY)
    canvas.setLineWidth(0.8)
    canvas.line(M_L, PAGE_H - 14 * mm, PAGE_W - M_R, PAGE_H - 14 * mm)
    canvas.setFont("DVSB", 8.5)
    canvas.setFillColor(NAVY)
    canvas.drawString(M_L, PAGE_H - 12.5 * mm, DOC_TITLE.upper())
    canvas.setFont("DVS", 8.5)
    canvas.setFillColor(GREY)
    canvas.drawRightString(PAGE_W - M_R, PAGE_H - 12.5 * mm,
                           "Chuong trinh Ket noi tri thuc - Tap 1")
    canvas.setStrokeColor(NAVY)
    canvas.line(M_L, 13 * mm, PAGE_W - M_R, 13 * mm)
    canvas.setFont("DVS", 8)
    canvas.drawString(M_L, 10 * mm, "Duoc tao boi ma tran de kiem tra giua ky I mon Toan 10 nam hoc 2026-2027")
    canvas.drawRightString(PAGE_W - M_R, 10 * mm, f"Trang {doc.page}")
    canvas.restoreState()

# ----------------------------------------------------------------------------
# Document
# ----------------------------------------------------------------------------
doc = BaseDocTemplate("DE_CUONG_TOAN_10_GIUAKY1_KET_NOI_TRI_THUC.pdf",
                      pagesize=A4,
                      leftMargin=M_L, rightMargin=M_R,
                      topMargin=M_T, bottomMargin=M_B,
                      title=DOC_TITLE,
                      author="Bo mon Toan - THPT Ha Huy Tap",
                      subject="De cuong on tap Toan 10 giua ky I")
frame = Frame(M_L, M_B, PAGE_W - M_L - M_R, PAGE_H - M_T - M_B, id="main")
doc.addPageTemplates([PageTemplate(id="page", frames=[frame], onPage=on_page)])

story = []

# ----------------------------------------------------------------------------
# COVER / HEADER
# ----------------------------------------------------------------------------
story.append(Spacer(1, 6 * mm))
story.append(P("TRUONG THPT HA HUY TAP", S_SUB))
story.append(P("TO BO MON TOAN", S_SUB))
story.append(Spacer(1, 4 * mm))
story.append(P("DE CUONG ON TAP MON TOAN LOP 10", S_TITLE))
story.append(P("KIEM TRA GIUA KY I - NAM HOC 2026-2027", S_TITLE))
story.append(Spacer(1, 3 * mm))
story.append(P("Chuong trinh: <b>Toan 10 - Ket noi tri thuc</b> &nbsp;|&nbsp; Thoi gian lam bai: 90 phut &nbsp;|&nbsp; Tong diem: 10", S_SUB))
story.append(Spacer(1, 5 * mm))
story.append(callout(
    "<b>Nguon du lieu:</b> Ma tran de kiem tra giua ky I mon Toan 10 (Ma tran toan 10 - giua ky I.docx, To bo mon Toan - Toan-Tin, THPT Ha Huy Tap). "
    "De cương duoc bien soan theo chinh xac khoi luong, so luong cau va phan bo muc do nhan thuc cua ma tran de. "
    "Noi dung van ban cac cau hoi trong ma tran goc chi ghi ma cau va yeu cau kiem tra, duoc bien soan lai lai de dung lam de bai on tap."))
story.append(Spacer(1, 7 * mm))

story.append(P("MUC LUC", S_H1))
toc_items = [
    "1. Gioi thieu va cau truc de kiem tra",
    "2. Bang phan bo khoi luong va so luong cau (theo ma tran de)",
    "3. Bang phan bo noi dung theo muc do nhan thuc",
    "4. De cuong on tap chi theo chuong",
    "   4.1. Chuong 1: Menh de va tap hop",
    "   4.2. Chuong 2: Bat phuong trinh va he bat phuong trinh bac nhat hai an",
    "   4.3. Chuong 3: He thuc luong trong tam giac",
    "   4.4. Chuong 4: Vecto (phan mo dau)",
    "5. De bai on tap trac nghiem (12 chon phuong an, 2 dung/sai, 4 tra loi ngan)",
    "6. De bai tu luan (3 cau)",
    "7. Dap an va loi giai chi tiet",
    "8. Luu yeu khi lam bai",
]
for it in toc_items:
    story.append(P(it, S_BULLET))
story.append(Spacer(1, 3 * mm))

# ----------------------------------------------------------------------------
# 1. GIOI THIEU
# ----------------------------------------------------------------------------
story.append(P("1. GIOI THIEU VA CAU TRUC DE KIEM TRA", S_H1))
story.append(P("De kiem tra cac kien thuc dai so va hinh hoc den het giua hoc ky 1 lop 10. "
               "Gom kien thuc thuoc cac chuong: Chuyen 1. Menh de va tap hop; Chuyen 2. Bat phuong trinh, he bat phuong trinh bac nhat hai an; "
               "Chuyen 3. He thuc luong trong tam giac; Chuyen 4. Vecto (pham vi: Bai 7 khai niem mo dau)."))
story.append(P("Hinh thuc: 12 cau trac nghiem chon phuong an (3 diem); 2 cau trac nghiem dung sai - moi cau co 4 y "
               "(dung 1 y: 0,1 - dung 2 y: 0,25 - dung 3 y: 0,5 - dung 4 y: 1,0 diem); 4 cau tra loi ngan (2 diem); "
               "3 cau tu luan (3 diem). Tong 24 cau trac nghiem (7,0 diem) + 3 cau tu luan (3,0 diem) = 10 diem."))

# ----------------------------------------------------------------------------
# 2. BANG PHAN BO KHOI LUONG
# ----------------------------------------------------------------------------
story.append(P("2. BANG PHAN BO KHOI LUONG VA SO LUONG CAU (THEO MA TRAN DE)", S_H1))
hdr = ["Noi dung kien thuc", "Don vi kien thuc",
       "Trac nghiem chon phuong an (NB/TH/VD)", "Trac nghiem Dung/Sai (NB/TH/VD)",
       "Tra loi ngan (NB/TH/VD)", "Tu luan (TH/VD/VDC)", "So cau", "Diem"]
rows = [
    ["1", "Menh de. Tap hop.", "1.1. Menh de", "2 / - / -", "- / - / -", "- / - / -", "- / - / -", "2", "0,5"],
    ["", "", "1.2. Tap hop", "1 / - / -", "1 / 1 / -", "1 / - / -", "- / - / -", "4", "1,25"],
    ["", "", "1.3. Cac phep toan tren tap hop", "1 / - / -", "- / 1 / 1", "- / - / 1", "1 / 1 / -", "4", "1,25"],
    ["2", "Bat phuong trinh va he bat phuong trinh bac nhat hai an", "2.1. Bat phuong trinh bac nhat hai an",
     "1 / - / -", "1 / 2 / 1", "- / - / -", "- / - / -", "5", "1,25"],
    ["", "", "2.2. He bat phuong trinh bac nhat hai an", "1 / - / -", "- / - / -", "- / - / -", "- / 1 / -", "1", "0,25"],
    ["", "", "", "", "", "", "- / - / 1", "", "1,0"],
    ["3", "He thuc luong trong tam giac.", "3.1. Gia tri luong giac cua mot goc tu 0 den 180",
     "1 / 1 / -", "- / - / -", "- / - / 1", "- / - / -", "3", "1,0"],
    ["", "", "3.2. He thuc luong trong tam giac", "1 / 1 / -", "- / - / -", "1 / - / -", "1 / - / -", "3", "1,0"],
    ["", "", "", "", "", "", "", "", "1,0"],
    ["4", "Vecto", "4.1. Khai niem vecto", "1 / 1 / -", "- / - / -", "- / - / -", "- / - / -", "2", "0,5"],
    ["Tong", "", "", "9 / 3 / 0", "2 / 4 / 2", "0 / 2 / 2", "1 / 1 / 1", "24", "7,0 / 3,0"],
]
story.append(make_table(hdr, rows,
    [10*mm, 26*mm, 27*mm, 27*mm, 27*mm, 27*mm, 13*mm, 13*mm],
    align_center_cols=(0, 6, 7)))
story.append(P("Chu NB: Nhan biet; TH: Thong hieu; VD: Ung dung; VDC: Ung dung cao. "
               "Trac nghiem dung/sai: 2 cau x 4 y; diem cho tung y nhu mot tap hop. "
               "Tong so diem trac nghiem: 7,0 diem; tu luan: 3,0 diem.", S_NOTE))

# ----------------------------------------------------------------------------
# 3. BANG PHAN BO THEO MUC DO
# ----------------------------------------------------------------------------
story.append(P("3. BANG PHAN BO NOI DUNG THEO MUC DO NHAN THUC", S_H1))
hdr2 = ["STT", "Noi dung kien thuc", "Don vi kien thuc", "Muc do kien thuc, ky nang can kiem tra danh gia",
        "NB", "TH", "VD", "VDC"]
rows2 = [
    ["1", "Menh de. Tap hop.", "1.1. Menh de",
     "Nhan biet: Cau 1. Biet gi la mot menh de, menh de phu dinh, menh de chua bien. "
     "Cau 2. Biet nghia ki hieu pho bien (forall) va ki hieu ton tai (exists).", "2", "-", "-", "-"],
    ["", "", "1.2. Tap hop",
     "Nhan biet: Cau 3. Biet cho tap hop bang cach liet ke cac phan tu hoac chi ra tinh chat dac trung cua cac phan tu cua tap hop; "
     "Cau 1a (DS). Su dung dung cac ki hieu khoang. Thong hieu: Cau 1b. Bieu dien duoc cac khoang, doan tren truc so. "
     "Lay duoc vi ve tap hop, tap hop con, tap hop bang nhau. Cau 1 (TLN): Tim so tap hop con cua 1 tap hop.", "1+1", "1+1", "-", "-"],
    ["", "", "1.3. Cac phep toan tren tap hop",
     "Nhan biet: Cau 4. Biet dung bieu do Ven de bieu dien giao cua hai tap hop, hop cua hai tap hop. "
     "Thong hieu: Thuc hiencac phep toan giao, hop, phan bu (Cau 1c, Cau 1 TL). Ung dung: Cau 1d; Cau 2 (TLN) bai toan thuc te phep toan tap hop.",
     "1", "1+1 TL", "1+1", "-"],
    ["2", "Bat phuong trinh va he bat phuong trinh bac nhat hai an", "2.1. Bat phuong trinh bac nhat hai an",
     "Nhan biet: Cau 5. Nhan biet duoc bat phuong trinh bac nhat hai an; Cau 2a nhan biet nghia va mien nghia tren mat phang toa do. "
     "Thong hieu: Cau 2b, 2c. Mo ta duoc mien nghia. Ung dung: Cau 2d. Chuyen dieu kien bai toan thuc te ve dang bat phuong trinh.",
     "1+1", "2", "1", "-"],
    ["", "", "2.2. He bat phuong trinh bac nhat hai an",
     "Nhan biet: Cau 6. Nhan biet he bat phuong trinh; nghia va mien nghia cua he. Ung dung cao: Cau 3 (TL). Mo ta mien nghia he, tim gia tri toi uu cua bai toan chon phuong an toi uu.",
     "1", "-", "-", "1 TL"],
    ["3", "He thuc luong trong tam giac.", "3.1. Gia tri luong giac cua mot goc tu 0 den 180",
     "Nhan biet: Cau 7. Nhan biet gia tri luong giac mot goc tu 0 den 180; he thuc lien giac cua cac goc phu nhau, bu nhau. "
     "Tinh dung hoac gan dung GTLG bang may tinh cam tay. Thong hieu: Cau 8. Tinh GTLG mot goc khi biet 1 trong 4 GTLG cua no. "
     "Ung dung: Cau 3 (TLN). Cho biet 1 GTLG, tinh GTLG cua 1 bieu thuc.", "1", "1", "1", "-"],
    ["", "", "3.2. He thuc luong trong tam giac",
     "Nhan biet: Cau 9. Nhan biet he thuc luong co ban: dinh ly cosin, dinh ly sin, cong thuc dien tich tam giac. "
     "Thong hieu: Cau 10 TN, Cau 4 (TLN). Su dung he thuc luong de tinh canh, goc chua biet, dien tich tam giac; ung dung bai toan thuc te don gian. "
     "Ung dung: Cau 2 (TL). Mo ta cach giai tam giac va ung dung bai toan thuc te (khoang cach hai diem gap vat can, chieu cao vat...).",
     "2", "1+1 TLN", "1 TL", "-"],
    ["4", "Vecto", "4.1. Khai niem vecto",
     "Nhan biet: Cau 11. Biet cac khai niem va tinh chat vecto, vecto-khong, do dai vecto, hai vecto cung phuong, cung hung, hai vecto bang nhau; vecto-khong cung phuong va cung hung voi moi vecto. "
     "Thong hieu: Cau 12. Hieu duoc khai niem va dac diem vecto; chung minh duoc hai vecto bang nhau trong mot cac truong hop don gian.", "1", "1", "-", "-"],
]
story.append(make_table(hdr2, rows2,
    [9*mm, 20*mm, 20*mm, 78*mm, 11*mm, 12*mm, 11*mm, 11*mm],
    align_center_cols=(0, 4, 5, 6, 7)))
story.append(P("Ghi: co nhieu o gom nhieu cap (vi du \"1+1 TL\") co nghia la nhieu cau hoi o muc do do. "
               "TLN = tra loi ngan; TL = tu luan.", S_NOTE))

doc_part1 = story

# ----------------------------------------------------------------------------
# 4. DE CUONG CHI TIET
# ----------------------------------------------------------------------------
story.append(PageBreak())
story.append(P("4. DE CUONG ON TAP CHI THEO CHUONG", S_H1))
story.append(P("Hoc tap dau tien: doc lai sach bac toan Toan 10 tap 1 (Ket noi tri thuc), bai tap cuoi chuong va cac bai da lam trong ky. "
               "Luu y: pham vi vecto o giua ky chi den cuoi Bai 7 (khai niem mo dau).", S_NOTE))

# ---------------- 4.1 Chuong 1 ----------------
story.append(P("4.1. CHUONG 1: MENH DE VA TAP HOP", S_H2))
story.append(P("Phan bo: Menh de - 2 cau chon phuong an (muc Nhan biet, 0,5 diem). Tap hop - 1 cau chon phuong an (NB), 2 cau Dung/Sai (1 NB, 1 TH), "
               "1 cau Tra loi ngan (TH - tim so tap hop con). Phep toan tap hop - 1 cau chon phuong an (NB), 2 cau Dung/Sai (1 TH, 1 VD), "
               "1 cau Tra loi ngan (VD - bai toan thuc te), 1 cau Tu luan TH (1d) + 1 cau Tu luan VD (2c thuc te). Tong Khoi 1: 1,25 + 1,25 diem.", S_BODY))

story.append(P("A. Menh de", S_H3))
story.extend(bullets([
    "Menh de: khung khanh co xac dinh duoc tinh dung sai. Khung khanh khong xac dinh duoc tinh dung sai khong phai menh de.",
    "Menh de chua bien: nhan biet hieu P(x); khi x co gia tri cu the thi xac dinh duoc tinh dung sai.",
    "Menh de phu dinh (not P): trai nghich cua P. Neu P dung thi not P sai, va nguoc lai.",
    "Menh de dao (P => Q thanh Q => P), menh de contra-positive (not Q => not P), menh de tuong duong (P <=> Q).",
    "Ki hieu: forall x (moi x), exists x (co it it nhat mot x).",
    "Dieu kien can, dieu kien du, dieu kien can va du; xac dinh duoc trong truong hop don gian.",
    "Xac dinh tinh dung/sai cua mot menh de toan hoc don gian.",
]))
story.append(P("B. Tap hop va cac phep toan tren tap hop", S_H3))
story.extend(bullets([
    "Khai niem tap hop; tap con, hai tap hop bang nhau, tap rong emptyset.",
    "Cach khai bao tap hop: liet ke cac phan tu; quy mo {x | x thoa man tinh chat ...}.",
    "Tap so: N* (so nguyen duong), N (so nguyen duong va 0), Z (so nguyen), Q (so thuc), R (so thuc).",
    "Khoang tren truc so: (a; b), [a; b], (a; b], [a; b), (-oo; a), (-oo; a], (a; +oo), [a; +oo), (-oo; +oo).",
    "Phep toan: giao A n B (pho bien: &), hop A u B (pho bien: \cup), hieu A \ B, phan bu cua A (complement A).",
    "Bieu do Ven de bieu dien giao, hop, hieu, phan bu.",
    "Cua tap co n phan tu co 2^n tap hop con (ung dung tra loi ngan).",
]))
story.append(callout("CONG THUC / KI HIEU CAN NHO: A \subseteq B &lt;=&gt; moi phan tu cua A cung la phan tu cua B. "
                     "A = B &lt;=&gt; A \subseteq B va B \subseteq A. Complement: C_U A = {x \in U | x \notin A}."))

# ---------------- 4.2 Chuong 2 ----------------
story.append(P("4.2. CHUONG 2: BAT PHUONG TRINH VA HE BAT PHUONG TRINH BAC NHAT HAI AN", S_H2))
story.append(P("Phan bo: BPT - 1 cau chon phuong an (NB), 4 cau Dung/Sai (1 NB, 2 TH, 1 VD - chuyen dieu kien thuc te). "
               "He BPT - 1 cau chon phuong an (NB), 1 cau Tu luan VD cao (mien nghia + gia tri toi uu). Tong Khoi 2: 1,25 + 0,25 + 1,0 diem.", S_BODY))
story.append(P("A. Bat phuong trinh bac nhat hai an", S_H3))
story.extend(bullets([
    "Dang tong quat: ax + by &lt; c (cung cung: le, ge, gt); a, b khong dong thoi bang 0.",
    "Nghiem cua BPT hai an: mot cap so (x0; y0) thoa man bat phuong trinh (vo so nghiem).",
    "Cach xac dinh mien nghia tren mat phang toa do Oxy: ve duong thang d: ax + by = c; lay diem M0 khong thuoc d (thuong la goc toa do O neu c != 0, hoac (1;0)/(0;1) neu c = 0); tinh ax0 + by0 va so sanh voi c; chon nua mat phang thoa man.",
    "Duong thang d khong duoc phep (bordo) khi bat phuong trinh la &lt; hoac &gt;; duoc phep khi &lt;= hoac &gt;=.",
    "Ung dung: chuyen dieu kien cua bai toan thuc te ve dang BPT bac nhat hai an.",
]))
story.append(P("B. He bat phuong trinh bac nhat hai an", S_H3))
story.extend(bullets([
    "He BPT: he gom hai (hoac nhieu) BPT bac nhat hai an.",
    "Nghiem cua he: cap so dong thoi la nghiem cua tat ca cac BPT trong he.",
    "Mien nghia cua he: giao cac mien nghia cua moi BPT (phan khong bi gach sau khi ve tat ca duong thang bordo).",
    "Bai toan toi uu: tren mien nghia la da giac A1A2...An, gia tri toi uu cua ham so F(x,y) = ax + by luon xay dai mot dinh cua da giac. Tim gia tri lon nhat / nho nhat bang cach tinh tai cac dinh.",
]))
story.append(callout("MAU BAI TOAN TOI UU: Cho he x >= 0, y >= 0, x + y <= 100, 2x + y <= 120 va F = 3,5x + 2y. Tim GTLN F. "
                     "Cac dinh mien nghia: (0;0), (60;0), (20;80), (0;100). Tinh F tai tung dinh => GTLN = 230 tai (20;80).", LIGHT, GREEN))

# ---------------- 4.3 Chuong 3 ----------------
story.append(P("4.3. CHUONG 3: HE THUC LUONG TRONG TAM GIAC", S_H2))
story.append(P("Phan bo: GTLG goc 0-180 - 1 cau CP (NB), 1 cau CP (TH), 1 cau TLN (VD). He thuc luong - 1 cau CP (NB), 2 cau CP? (TH: cau 10 TN + cau 4 TLN), "
               "1 cau TL (VD). Tong Khoi 3: 1,0 + 1,0 + 1,0 diem.", S_BODY))
story.append(P("A. Gia tri luong giac cua mot goc tu 0 den 180", S_H3))
story.extend(bullets([
    "Voi moi goc alpha (0° <= alpha <= 180°), dinh diem M(x0; y0) tren nua duong tron don vi sao cho goc xOM = alpha. "
    "sin alpha = y0; cos alpha = x0; tan alpha = y0/x0 (alpha != 90°); cot alpha = x0/y0 (alpha khac 0°, 180°).",
    "Quan he: tan alpha = sin alpha / cos alpha; cot alpha = cos alpha / sin alpha; tan alpha = 1/cot alpha.",
    "Bảng GTLG cac goc dac biet: sin/cos/tan/cot cua 0°, 30°, 45°, 60°, 90°, 120°, 135°, 150°, 180°.",
    "Goc bu nhau: sin(180° - alpha) = sin alpha; cos(180° - alpha) = -cos alpha; tan(180° - alpha) = -tan alpha.",
    "Co so luong giac: sin² alpha + cos² alpha = 1.",
    "Tinh GTLG dung hoac gan dung bang may tinh cam tay; tinh GTLG mot goc khi biet 1 trong 4 GTLG cua no.",
]))
story.append(callout("BANG GTLG CAN GAN: sin30=1/2, cos30=√3/2, tan30=√3/3; sin45=cos45=√2/2, tan45=1; sin60=√3/2, cos60=1/2, tan60=√3; "
                     "sin90=1, cos90=0; sin120=√3/2, cos120=-1/2; sin135=√2/2, cos135=-√2/2; sin150=1/2, cos150=-√3/2; sin180=0, cos180=-1.", LIGHT, GREEN))

story.append(P("B. He thuc luong trong tam giac", S_H3))
story.extend(bullets([
    "Dinh ly Cosin: a² = b² + c² - 2bc cos A (va cac dang tuong tu). Dung khi biet 2 canh va goc xen giua, hoac biet 3 canh.",
    "Dinh ly Sin: a/sin A = b/sin B = c/sin C = 2R. Dung khi biet cap canh - goc doi nhau.",
    "Cong thuc dien tich: S = 1/2 bc sin A (biet 2 canh va goc xen giua). Cong thuc Heron: S = sqrt(p(p-a)(p-b)(p-c)), p = nua chu vi.",
    "Giai tam giac: xac dinh cac canh, goc chua biet.",
    "Ung dung: bai toan thuc te don gian (xac dinh khoang cach hai diem gap vat can; chieu cao vat khong the do truc tiep...).",
]))

# ---------------- 4.4 Chuong 4 ----------------
story.append(P("4.4. CHUONG 4: VECTO (PHAM VI: BAI 7 - KHAI NIEM MO DAU)", S_H2))
story.append(P("Phan bo: 2 cau chon phuong an (1 NB, 1 TH), 0,5 diem.", S_BODY))
story.extend(bullets([
    "Vecto la mot doan thang co huong (da chi dinh diem dau va diem cuoi).",
    "Khai bao: vecto co diem dau A, diem cuoi B kieu theo AB (doc: vecto AB); doan thang di qua A, B la gia cua vecto.",
    "Vecto-khong: vecto co diem dau va diem cuoi trung nhau, kieu theo 0; do dai bang 0; cung phuong, cung hung voi moi vecto.",
    "Hai vecto cung phuong neu gia cua chung song song hoac trung nhau (cung hung hoac nguoc hung).",
    "Ba point phan biet A, B, C thang hang &lt;=&gt; hai vecto cung phuong.",
    "Hai vecto bang nhau neu cung do dai, cung phuong, cung hung.",
]))

# ----------------------------------------------------------------------------
# 5. DE ON TAP TRAC NGHIEM
# ----------------------------------------------------------------------------
story.append(PageBreak())
story.append(P("5. DE BAI ON TAP TRAC NGHIEM", S_H1))
story.append(P("Duoc bien soan theo phan bo cua ma tran de: 12 cau chon phuong an (muc NB: 9 cau; TH: 3 cau); "
               "2 cau dung/sai (muc NB: 2 y; TH: 4 y; VD: 2 y); 4 cau tra loi ngan (muc TH: 2 cau; VD: 2 cau).", S_BODY))
story.append(P("5.1. Phan trac nghiem chon phuong an (12 cau)", S_H2))

mcqs = [
    # Câu 1 - NB - Menh de
    ("Cau 1. (Muc: Nhan biet - Menh de) Cau nao sau day la mot menh de?",
     ["A. Mot so thuc lon hon 0.", "B. 7 chia het cho 3.", "C. x + 5 = 10.", "D. Toi yeu toan hoc."], "B"),
    # Câu 2 - NB - ki hieu
    ("Cau 2. (Muc: Nhan biet - Menh de chua bien) Ki hieu \u2200 x \in R, x^2 \ge 0 co nghia la:",
     ["A. Co it it nhat mot so thuc x sao cho binh phuong lon hon hoac bang 0.",
      "B. Moi so thuc x deu co binh phuong lon hon hoac bang 0.",
      "C. Co mot so thuc duy nhat co binh phuong bang 0.",
      "D. Khong co so thuc nao co binh phuong am."], "B"),
    # Câu 3 - NB - Tap hop
    ("Cau 3. (Muc: Nhan biet - Tap hop) Cach khai bao tap hop khong chinh xac la:",
     ["A. Liet ke cac phan tu: A = {1, 2, 3}.",
      "B. Chi ra tinh chat dac trung: B = {x | x la so nguyen duong nho hon 5}.",
      "C. Viet: C = {cac so thuc}.",
      "D. Doi voi tap vo han chi co the khai bao bang bieu do Ven."], "D"),
    # Câu 4 - NB - Phep toan tap hop
    ("Cau 4. (Muc: Nhan biet - Phep toan tap hop) Bieu do Ven nao bieu dien hop cua hai tap hop A va B?",
     ["A. Vung chung cua hai vung day da A va B.",
      "B. Vung giao cua A va B.",
      "C. Vung thuoc A nhung khong thuoc B.",
      "D. Vung ngoai cua A u B."], "A"),
    # Câu 5 - NB - BPT
    ("Cau 5. (Muc: Nhan biet - Bat phuong trinh bac nhat hai an) Phuong trinh/bai phuong trinh nao sau day LA bat phuong trinh bac nhat hai an?",
     ["A. x^2 + y < 4", "B. 3x + 2y \ge 7", "C. xy > 5", "D. x + y + z = 0"], "B"),
    # Câu 6 - NB - He BPT
    ("Cau 6. (Muc: Nhan biet - He bat phuong trinh) He nao sau day la he bat phuong trinh bac nhat hai an?",
     ["A. {x + y < 5; x - y = 2}", "B. {x^2 + y < 9; y > 0}", "C. {x + 2y \le 6; 2x - y > 1}", "D. {x + y > 0}"], "C"),
    # Câu 7 - NB - GTLG
    ("Cau 7. (Muc: Nhan biet - GTLG) Voi alpha = 120°, ta co:",
     ["A. sin 120° = -√3/2", "B. cos 120° = 1/2", "C. tan 120° = -√3", "D. cot 120° = √3/3"], "C"),
    # Câu 8 - TH - GTLG
    ("Cau 8. (Muc: Thong hieu - GTLG) Neu cos alpha = 3/5 voi alpha thuoc khoang (0°; 90°), thi sin alpha bang:",
     ["A. 4/5", "B. -4/5", "C. 3/4", "D. 5/3"], "A"),
    # Câu 9 - NB - He thuc luong
    ("Cau 9. (Muc: Nhan biet - He thuc luong trong tam giac) Cong thuc cua dinh ly Cosin cho canh a la:",
     ["A. a = b + c - 2bc cos A", "B. a^2 = b^2 + c^2 - 2bc cos A",
      "C. cos A = (b^2 + c^2 - a^2) / (2bc)", "D. a/sin A = 2R"], "B"),
    # Câu 10 - TH - He thuc luong
    ("Cau 10. (Muc: Thong hieu - He thuc luong) Trong tam giac ABC biet a = 13, b = 14, cos C = 5/13. Canh c bang:",
     ["A. 12", "B. 13", "C. 14", "D. 15"], "D"),
    # Câu 11 - NB - Vecto
    ("Cau 11. (Muc: Nhan biet - Vecto) Khai bao vecto co diem dau A va diem cuoi B la:",
     ["A. BA", "B. AB", "C. |AB|", "D. Vecto-khong"], "B"),
    # Câu 12 - TH - Vecto
    ("Cau 12. (Muc: Thong hieu - Vecto) Hai vecto a va b bang nhau neu va chi neu:",
     ["A. Cung do dai.", "B. Cung phuong.", "C. Cung do dai, cung phuong, cung huong.",
      "D. Co cung diem dau."], "C"),
]

for q, opts, key in mcqs:
    story.append(KeepTogether([P(q, S_QUEST),
                               Spacer(1, 1.2 * mm)] +
                               [P(f"{o[0]}. {o[1]}", S_TBL_C) for o in opts] +
                               [Spacer(1, 2.5 * mm)]))

story.append(P("5.2. Phan trac nghiem Dung/Sai (2 cau, moi cau 4 y)", S_H2))
story.append(P("Quyen tac: Moi cau gom 4 y. Dung 1 y = 0,1 diem; dung 2 y = 0,25; dung 3 y = 0,5; dung 4 y = 1,0. "
               "Ghi D (dung) hoac S (sai) truoc moi y.", S_BODY))
story.append(P("Cau I. (Muc: Nhan biet - Tap hop / Menh de) Dinh gia cac y sau:",
               S_QUEST))
story.extend(bullets([
    "Tap hop khoang (-3; 2] chua chua so -3, nhung chua chua so 2. (S)",
    "Voi moi tap hop co 4 phan tu, so luong tap hop con bang 16. (D)",
    "Menh de \"5 chia het cho 2\" la menh de sai. (D)",
    "Ki hieu \u2203 x \in R, x^2 = -1 co nghia ton tai it it nhat mot so thuc x thoa man x^2 = -1. (S)",
], char="&square;"))
story.append(P("Cau II. (Muc: Nhan biet / Thong hieu - Bat phuong trinh bac nhat hai an) Dinh gia cac y sau:",
               S_QUEST))
story.extend(bullets([
    "Cap so (0; 1) la nghiem cua bat phuong trinh 2x - 3y < 4. (D)",
    "Cap so (2; 1) thuoc mien nghia cua bat phuong trinh x + y > 4. (S)",
    "Duong thang d: 3x + y = 6 la duong thang bordo cua bat phuong trinh 3x + y \le 6. (D)",
    "Mien nghia cua bat phuong trinh ax + by < c luon la mot nua mat phang khong chua duong thang bordo. (D)",
], char="&square;"))

# ----------------------------------------------------------------------------
# 6. TU LUAN
# ----------------------------------------------------------------------------
story.append(PageBreak())
story.append(P("6. DE BAI TU LUAN (3 CAU)", S_H1))
story.append(P("Cau 1. (Muc do: Thong hieu - 1,0 diem; Don vi: 1.3 Phep toan tren tap hop)",
               S_QUEST))
story.append(P("Cho hai tap hop A = {x \in R | -2 \le x < 5} va B = {x \in R | x > 1}. Tren truc so, hay: "
               "a) Xac dinh va bieu dien tap hop A n B; A u B; C_R A (phan bu cua A). "
               "b) Tinh so luong tap hop con cua tap hop C = {x \in Z | -2 \le x \le 2}.", S_QUEST))
story.append(P("Cau 2. (Muc do: Thong hieu - 1,0 diem; Don vi: 3.2 He thuc luong trong tam giac)", S_QUEST))
story.append(P("Cho tam giac ABC co AB = 8 m, AC = 6 m, goc A = 60°. Tinh do dai canh BC va dien tich tam giac ABC. "
               "Ung dung: Hai diem A, B nam o hai ben cua mot ho (khong the do truc tiep). Tu mot diem C o cung mot ben ho, "
               "ta do duoc AC = 8 m, BC = 6 m va goc ACB = 60°. Tinh khoang cach AB giua hai diem."))
story.append(P("Cau 3. (Muc do: Ung dung cao - 1,0 diem; Don vi: 2.2 He bat phuong trinh bac nhat hai an)", S_QUEST))
story.append(P("May cong ty san xuat hai loai do uong A va B. Mot ca san xuat can x thung loai A va y thung loai B, thoa man: "
               "x \ge 0, y \ge 0, x + y \le 100 (kha nang kho), 2x + y \le 160 (kha nang dong co). "
               "Loi nhuot moi thung A la 3,5 trieu dong, moi thung B la 2 trieu dong. "
               "Dat phuong trinh loi nhuot F(x; y) = 3,5x + 2y. Tim so luong san xuat cua hai loai do uong de loi nhuot lon nhat va tinh loi nhuot lon nhat."))

doc_part2 = story

# ----------------------------------------------------------------------------
# 7. DAP AN VA LOI GIAI
# ----------------------------------------------------------------------------
story.append(PageBreak())
story.append(P("7. DAP AN VA LOI GIAI CHI TIET", S_H1))

story.append(P("7.1. Dap an trac nghiem chon phuong an", S_H2))
ans_rows = []
for i, (q, opts, key) in enumerate(mcqs, 1):
    # Extract statement text only (before first period-space-number)
    ans_rows.append([str(i), key, ""])
t_ans = Table([[P("<b>Cau</b>", S_TBL_BC), P("<b>Dap an</b>", S_TBL_BC), P("<b>Loi giai ngon ngan</b>", S_TBL_BC)]] +
              [[P(r[0], S_TBL_C), P(r[1], S_TBL_C), P(r[2], S_TBL)] for r in ans_rows],
              colWidths=[14*mm, 20*mm, 136*mm], repeatRows=1)
t_ans.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#8ea9c4")),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
]))
for i in range(1, len(ans_rows)+1):
    if i % 2 == 0:
        t_ans.setStyle(TableStyle([("BACKGROUND", (0, i), (-1, i), LIGHT2)]))
story.append(t_ans)
story.append(Spacer(1, 4 * mm))
story.append(P("Loi giai chi tiet:", S_H3))
solutions_mc = {
    1: "B dung vi co xac dinh duoc tinh dung sai (7 khong chia het cho 3 -> mệnh đề sai, nhưng vẫn là mệnh đề). A là mệnh đề chứa biến, C là mệnh đề chứa biến, D là kh sentía không phải mệnh đề.",
    2: "B: \u2200 (phổ biến) nghĩa là 'mọi x'.",
    3: "D: Dành cho tập hữu hạn hoặc quy mô; với tập vô hạn có thể quy mô nếu tính chất xác định rõ, không bắt buộc phải dùng biểu đồ Ven.",
    4: "A: Hợp A u B là vùng chứa tất cả phần tử thuộc A hoặc thuộc B.",
    5: "B: dạng ax + by \ge c với a=3, b=2 không đồng thời bằng 0. A có x^2 (bậc 2), C có tích xy, D là phương trình.",
    6: "C: hai bước đều là BPT bậc nhất hai ẩn. A có phương trình, D chỉ có một BPT, B có x^2.",
    7: "C: goc 120° thuoc goc II: tan(180°-60°) = -tan60° = -√3. sin120 = sin60 = √3/2; cos120 = -cos60 = -1/2; cot120 = -cot60 = -√3/3.",
    8: "A: sin² = 1 - cos² = 1 - 9/25 = 16/25, alpha goc I duong => sin = 4/5.",
    9: "B: a^2 = b^2 + c^2 - 2bc cos A. (C la he qua dien tuc cua Cosin, khong phai cong thuc chinh).",
    10: "A: Dinh ly Cosin: a^2 = b^2 + c^2 - 2bc cos A = 25 + 49 - 2*5*7*(13/35) = 74 - 91 = ... sai; tinh: 2*5*7*13/35 = 70*13/35 = 2*13 = 26; 25+49-26 = 48? Lai xet: a^2 = 25+49-26 = 48 khong phai BAP. Thay c de tim: b^2 = a^2 + c^2 - 2ac cos B khong du. Thay cos A formula thuc te: cos A = (b^2+c^2-a^2)/(2c) -> 13/35 = (25+c^2-49)/(10c) => 130c = 35(c^2 -24) => 7c^2 -26c -168 =0 => c = (26 ± sqrt(676+4704))/14 = (26 ± sqrt5380)/14 — qua phuc. Sua de: cho a=7, b=5, cos A=13/35 tim c: ap dung cong thuc cos A = (b^2 + c^2 - a^2)/(2bc): 13/35 = (25 + c^2 - 49)/(10c) = (c^2 - 24)/(10c) => 130c = 35c^2 - 840 => 7c^2 - 26c - 168 = 0 => c = [26 ± sqrt(676 + 4704)]/14 = [26 ± sqrt(5380)]/14. Khong phai so nguyen. Thay cau: cho b=8, c=5, cos A=13/35 tim a: a^2 = 64+25-2*8*5*13/35 = 89 - 800*13/35 = 89 - 29.71... khong dung. Thay: a=7, c=5, cos A = 13/35 tim b: b^2 = a^2+c^2-2ac cos A = 49+25-70*13/35 = 74-26 = 48, khong BAP. Thay: cos A = 13/35 khong Hop. Thay cos A = 3/7: b^2 = 49+25-70*3/7 = 74-30 = 44 khong. Thay a=13, b=5, cos C... Bo: Loi giai cau 10 duoc viet chung: su dung dinh ly cosin, ket qua c = 4.",
    11: "B: khai bao vecto AB.",
    12: "C: bang nhau = cung do dai, cung phuong, cung huong.",
}
# Fix solution for 10 properly:
solutions_mc[10] = ("D: Dinh ly Cosin: c^2 = a^2 + b^2 - 2ab cos C = 169 + 196 - 2*13*14*(5/13) = 365 - 140 = 225 => c = 15.")

story.append(Spacer(1, 2 * mm))
for i in range(1, len(mcqs)+1):
    story.append(P(f"<b>{i}.</b> {solutions_mc[i]}", S_ANS))

story.append(P("7.2. Dap an trac nghiem Dung/Sai", S_H2))
ds_answers = {
    "I": ["S", "D", "D", "S"],
    "II": ["D", "S", "D", "D"],
}
ds_expl = {
    "I": ["Khoang (-3;2] khong chua -3, nhung chua chua 2 -> y khai bao la sai.",
          "Tap hop 4 phan tu co 2^4 = 16 tap hop con -> dung.",
          "\"5 chia het cho 2\" la mệnh đề sai (tinh dung sai xac dinh) -> dung.",
          "\u2203 x, x^2=-1 khong co so thuc -> y khai bao 'ton it nhat mot x' thoa man x^2=-1 la sai."],
    "II": ["2(0)-3(1) = -3 < 4 -> dung.",
           "2+1 = 3 khong > 4 -> sai.",
           "Duong thang 3x+y=6 chinh la bordo, va bo phep '<=' chua duong thang -> dung.",
           "Bat phuong trinh '<' => nua mat phang khong chua duong thang bordo -> dung."],
}
for part, keys in ds_answers.items():
    story.append(P(f"Cau {part}:", S_H3))
    story.append(P(" &nbsp; ".join(f"Y{k+1}: <b>{v}</b>" for k, v in enumerate(keys)), S_ANS))
    for k, v in enumerate(keys):
        story.append(P(f"Y{k+1} = {v}: {ds_expl[part][k]}", S_ANS))
    story.append(Spacer(1, 2 * mm))

story.append(P("7.3. Dap an tra loi ngan", S_H2))
tln_sol = [
    ("Cau 1. (TH) Tap hop A={x | -2 <= x < 5}. So tap hop con cua tap hop co 5 phan tu la 2^5 = 32.",
     "C = {x \in Z | -2 \le x \le 2} = {-2,-1,0,1,2} co 5 phan tu => so tap hop con = 2^5 = 32."),
    ("Cau 2. (VD) Bai toan thuc te phep toan tap hop: cho tap hop khach hang mua san pham X la A, mua san pham Y la B. "
     "Tinh so khach hang mua ca hai (A n B), mua it it nhat mot san pham (A u B), mua X nhung khong mua Y (A \ B).",
     "Ap dung cong thuc phep toan tap hop va bieu do Ven; kiem tra phan tu thuoc tap hop nao."),
    ("Cau 3. (VD) Cho biet GTLG cua goc alpha, tinh GTLG cua bieu thuc, vi du: neu sin alpha = 3/5 (alpha goc I) thi cos alpha = 4/5, tan alpha = 3/4.",
     "Dung cong so sin²+cos²=1 va tan = sin/cos."),
    ("Cau 4. (TH) Dinh ly cosin/sin va cong thuc dien tich: trong tam giac ABC biet a=7, b=8, goc C=60°, tim c va dien tich.",
     "c^2 = 49+64-2*7*8*cos60 = 113-56 = 57 => c=√57. S = 1/2*7*8*sin60 = 14√3."),
]
for name, sol in tln_sol:
    story.append(P(f"<b>{name}</b>", S_H3))
    story.append(P(sol, S_ANS))

story.append(P("7.4. Dap an tu luan", S_H2))
story.append(P("Cau 1. (1,0 diem)", S_H3))
story.append(P("a) A = [-2; 5), B = (1; +oo). A n B = (1; 5). A u B = [-2; +oo). C_R A = (-oo; -2) u [5; +oo).", S_ANS))
story.append(P("b) C = {-2; -1; 0; 1; 2} co 5 phan tu, nen co 2^5 = 32 tap hop con.", S_ANS))
story.append(P("Cau 2. (1,0 diem)", S_H3))
story.append(P("BC^2 = 8^2 + 6^2 - 2*8*6*cos60° = 100 - 48 = 52 => BC = 2√13 (m). "
               "S_ABC = 1/2 * 8 * 6 * sin60° = 12√3 (m^2). Ung dung ho: AB = √52 = 2√13 (m).", S_ANS))
story.append(P("Cau 3. (1,0 diem)", S_H3))
story.append(P("Mien nghia la da giac co cac dinh: (0;0), (80;0) [x+y=100, y=0 -> x=100? x+y<=100 va y=0 => x<=100; 2x<=160 => x<=80 -> dinh (80;0)], "
               "giao x+y=100 va 2x+y=160: x=60, y=40 -> (60;40); va (0;100) [x=0: y<=100, y<=160 -> (0;100)]. "
               "Tinh F tai cac dinh: F(0;0)=0; F(80;0)=280; F(60;40)=210+80=290; F(0;100)=200. "
               "GTLN = 290 trieu dong tai x=60 thung A, y=40 thung B.", S_ANS))

# ----------------------------------------------------------------------------
# 8. LUU Y
# ----------------------------------------------------------------------------
story.append(P("8. LUU YEU KHI LAM BAI", S_H1))
story.extend(bullets([
    "Doc het de bai, ghi ro ma cau va dap an vao phieu tra loi.",
    "Voi phan Dung/Sai, phai lam du tat ca 4 y cua moi cau moi duoc tinh toan diem.",
    "Phep toan tap hop: luon kiem tra thanh phan, khong bo buoc bieu do Ven khi can.",
    "Bat phuong trinh hai an: ve duong thang bordro dung (keo ke khi < hoac >), chon diem check dung dung.",
    "GTLG: ghi ro bang GTLG cac goc dac biet, su dung cong so sin²+cos²=1.",
    "Dinh ly Cosin/Sin: ghep dung canh voi goc doi nhau; dien tich S = 1/2bc sin A.",
    "Quan ly thoi gian: 90 phut cho 27 cau (dem tung y cua Dung/Sai), trung binh khoang 3 phut/cau.",
    "Ket luan bai tu luan phai co bieu buoc, giai biet bac va ket qua cuoi cung.",
]))

story.append(Spacer(1, 6 * mm))
story.append(HRFlowable(width="100%", thickness=0.7, color=NAVY))
story.append(P("De cuong duoc bien soan tu Ma tran de kiem tra giua ky I mon Toan 10, nam hoc 2026-2027, THPT Ha Huy Tap. "
               "Noi dung cac cau hoi goc trong ma tran chi ghi ma va yeu kiem tra; cac chi tiet de bai o phan 5, 6 duoc bien soan lai theo phan bo ma tran de phuc vu on tap.", S_NOTE))

doc.build(story)
print("PDF built:", "DE_CUONG_TOAN_10_GIUAKY1_KET_NOI_TRI_THUC.pdf")
