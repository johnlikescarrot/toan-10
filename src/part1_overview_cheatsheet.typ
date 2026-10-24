#import "template.typ": *

// ============================================================================
// COVER & EXECUTIVE DASHBOARD
// ============================================================================

#block(
  width: 100%,
  fill: c-navy,
  radius: 10pt,
  inset: (x: 20pt, y: 18pt),
)[
  #align(center)[
    #box(
      fill: rgb("#1E3A8A"),
      stroke: 0.8pt + rgb("#60A5FA"),
      radius: 20pt,
      inset: (x: 12pt, y: 4pt),
    )[
      #text(fill: rgb("#93C5FD"), weight: "bold", size: 8.8pt, tracking: 0.6pt)[TRƯỜNG THPT HÀ HUY TẬP — TỔ TOÁN-TIN — CHUẨN MA TRẬN ĐẶC TẢ 2026–2027]
    ]
    #v(8pt)
    #text(fill: white, weight: "extrabold", size: 20pt)[ĐỀ CƯƠNG ÔN TẬP KIỂM TRA GIỮA HỌC KÌ I]
    #v(4pt)
    #text(fill: rgb("#FACC15"), weight: "extrabold", size: 15pt)[MÔN TOÁN LỚP 10 — BỘ SÁCH KẾT NỐI TRI THỨC VỚI CUỘC SỐNG]
    #v(5pt)
    #text(fill: rgb("#E2E8F0"), size: 9.6pt)[Biên soạn chuyên sâu bám sát 100% file _“MA TRẬN TOÁN 10 - GIỮA KÌ I.docx”_ (Năm học 2026–2027)]
    #v(12pt)
    #grid(
      columns: (1fr, 1fr, 1fr, 1fr),
      column-gutter: 8pt,
      box(fill: rgb("#1E293B"), stroke: 0.6pt + rgb("#334155"), radius: 6pt, inset: 8pt, width: 100%)[
        #text(fill: rgb("#93C5FD"), size: 8pt, weight: "bold")[THỜI GIAN LÀM BÀI]\
        #v(2pt)
        #text(fill: white, size: 12pt, weight: "extrabold")[90 Phút]
      ],
      box(fill: rgb("#1E293B"), stroke: 0.6pt + rgb("#334155"), radius: 6pt, inset: 8pt, width: 100%)[
        #text(fill: rgb("#6EE7B7"), size: 8pt, weight: "bold")[CẤU TRÚC ĐỀ THI]\
        #v(2pt)
        #text(fill: white, size: 11pt, weight: "extrabold")[70% TN + 30% TL]
      ],
      box(fill: rgb("#1E293B"), stroke: 0.6pt + rgb("#334155"), radius: 6pt, inset: 8pt, width: 100%)[
        #text(fill: rgb("#FCD34D"), size: 8pt, weight: "bold")[PHẠM VI KIẾN THỨC]\
        #v(2pt)
        #text(fill: white, size: 11pt, weight: "extrabold")[Chương I → IV]
      ],
      box(fill: rgb("#1E293B"), stroke: 0.6pt + rgb("#334155"), radius: 6pt, inset: 8pt, width: 100%)[
        #text(fill: rgb("#FCA5A5"), size: 8pt, weight: "bold")[NGÂN HÀNG & ĐỀ THI]\
        #v(2pt)
        #text(fill: white, size: 11pt, weight: "extrabold")[135+ Câu & Giải]
      ],
    )
  ]
]

#v(8pt)

#block(
  width: 100%,
  fill: rgb("#F8FAFC"),
  stroke: 0.8pt + c-border,
  radius: 8pt,
  inset: (x: 14pt, y: 10pt),
)[
  #text(weight: "extrabold", size: 10.5pt, fill: c-navy)[LỘ TRÌNH SỬ DỤNG ĐỀ CƯƠNG HIỆU QUẢ NHẤT (5 PHẦN KHÉP KÍN)]
  #v(4pt)
  #grid(
    columns: (1fr, 1fr),
    column-gutter: 14pt,
    row-gutter: 5pt,
    [• *Phần A — Giải mã Ma trận & Chiến thuật 90 phút:* Nắm rõ từng ô câu hỏi, điểm số từng chương và bản đồ 27 lệnh hỏi trong đề thi chính thức.],
    [• *Phần D — Ngân hàng Câu hỏi & Tự luận kèm Đáp án:* Quét sạch mọi dạng câu hỏi Phần I (12 câu), Phần II (2 câu Đ/S), Phần III (4 câu TLN), Phần IV (3 câu TL).],
    [• *Phần B — Tờ Công Thức Vàng & 10 Khẩu Quyết:* Học thuộc lòng toàn bộ công thức, bảng lượng giác và mẹo giải nhanh chỉ trong 15 phút.],
    [• *Phần E — 02 Đề Kiểm Tra Chuẩn Hóa 100% Ma Trận 2026–2027:* Luyện đề thực chiến 90 phút kèm bảng chấm điểm chi tiết từng 0,25 điểm.],
    [• *Phần C — Lý thuyết Trọng tâm 4 Chương & Sơ đồ:* Cô đọng đúng các chỉ báo Nhận biết – Thông hiểu – Vận dụng – Vận dụng cao trong Bản đặc tả.],
    [• *Cam kết độ phủ:* Bao quát *100% câu hỏi, dạng bài và đáp án* theo đúng Ma trận & Bản đặc tả Giữa học kì I năm học 2026–2027.]
  )
]

#v(4pt)
#outline(
  title: [MỤC LỤC TRA CỨU NHANH],
  indent: 12pt,
  depth: 2,
)

#pagebreak()

// ============================================================================
// PHẦN A: GIẢI MÃ MA TRẬN ĐẶC TẢ & CHIẾN THUẬT PHÒNG THI 90 PHÚT
// ============================================================================

= PHẦN A. GIẢI MÃ MA TRẬN ĐẶC TẢ KTGK I (2026–2027) & CHIẾN THUẬT 90 PHÚT

== A.1. Bảng Ma trận Đề kiểm tra Giữa kì I & Quy đổi Trọng số Điểm chi tiết

Theo văn bản chính thức *“MA TRẬN ĐỀ KIỂM TRA GIỮA KÌ I NĂM HỌC 2026–2027”* của *Trường THPT Hà Huy Tập (Tổ Toán-Tin)*, đề thi môn Toán lớp 10 có thời gian làm bài *90 phút*, thiết kế theo cấu trúc định dạng mới gồm *4 phần*: Phần I – Trắc nghiệm 4 lựa chọn (*12 câu = 3,0 điểm*), Phần II – Trắc nghiệm Đúng/Sai (*2 câu / 8 ý = 2,0 điểm*), Phần III – Trắc nghiệm trả lời ngắn (*4 câu = 2,0 điểm*), và Phần IV – Tự luận (*3 câu = 3,0 điểm*).

#v(3pt)
#set text(size: 7.9pt)
#table(
  columns: (0.35fr, 1.45fr, 1.55fr, 0.38fr, 0.38fr, 0.38fr, 0.38fr, 0.38fr, 0.38fr, 0.38fr, 0.38fr, 0.38fr, 0.38fr, 0.38fr, 0.42fr, 0.45fr, 0.45fr, 0.52fr, 0.52fr),
  align: (center + horizon, left + horizon, left + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon),
  stroke: 0.5pt + c-border,
  fill: (x, y) => if y < 3 { rgb("#1E3A8A") } else if y == 11 { rgb("#DBEAFE") } else if calc.odd(y) { rgb("#F8FAFC") } else { white },
  inset: (x: 2.5pt, y: 4pt),

  table.cell(rowspan: 3)[#text(fill: white, weight: "bold")[TT]],
  table.cell(rowspan: 3)[#text(fill: white, weight: "bold")[Nội dung\ kiến thức]],
  table.cell(rowspan: 3)[#text(fill: white, weight: "bold")[Đơn vị kiến thức\ (SGK Kết nối tri thức)]],
  table.cell(colspan: 3)[#text(fill: rgb("#BAE6FD"), weight: "bold")[TN Nhiều lựa chọn\ (12 câu – 3,0đ)]],
  table.cell(colspan: 3)[#text(fill: rgb("#A7F3D0"), weight: "bold")[TN Đúng / Sai\ (2 câu/8 ý – 2,0đ)]],
  table.cell(colspan: 3)[#text(fill: rgb("#FDE68A"), weight: "bold")[Trả lời ngắn\ (4 câu – 2,0đ)]],
  table.cell(colspan: 3)[#text(fill: rgb("#FECACA"), weight: "bold")[Tự luận\ (3 câu – 3,0đ)]],
  table.cell(colspan: 4)[#text(fill: rgb("#FACC15"), weight: "bold")[TỔNG]],

  table.cell(rowspan: 2)[#text(fill: white, weight: "bold")[NB]],
  table.cell(rowspan: 2)[#text(fill: white, weight: "bold")[TH]],
  table.cell(rowspan: 2)[#text(fill: white, weight: "bold")[VD]],
  table.cell(rowspan: 2)[#text(fill: white, weight: "bold")[NB]],
  table.cell(rowspan: 2)[#text(fill: white, weight: "bold")[TH]],
  table.cell(rowspan: 2)[#text(fill: white, weight: "bold")[VD]],
  table.cell(rowspan: 2)[#text(fill: white, weight: "bold")[NB]],
  table.cell(rowspan: 2)[#text(fill: white, weight: "bold")[TH]],
  table.cell(rowspan: 2)[#text(fill: white, weight: "bold")[VD]],
  table.cell(rowspan: 2)[#text(fill: white, weight: "bold")[TH]],
  table.cell(rowspan: 2)[#text(fill: white, weight: "bold")[VD]],
  table.cell(rowspan: 2)[#text(fill: white, weight: "bold")[VDC]],
  table.cell(colspan: 2)[#text(fill: white, weight: "bold")[Số câu]],
  table.cell(colspan: 2)[#text(fill: white, weight: "bold")[Điểm]],

  [#text(fill: white, weight: "bold")[TN]],
  [#text(fill: white, weight: "bold")[TL]],
  [#text(fill: white, weight: "bold")[TN]],
  [#text(fill: white, weight: "bold")[TL]],

  table.cell(rowspan: 3)[*1*],
  table.cell(rowspan: 3)[*Chương I.*\ Mệnh đề và\ Tập hợp\ *(4,00 điểm)*],
  [*1.1.* Mệnh đề _(Bài 1)_], [2], [–], [–], [–], [–], [–], [–], [–], [–], [–], [–], [–], [2], [–], [*0,50*], [–],
  [*1.2.* Tập hợp _(Bài 2a)_], [1], [–], [–], [1], [1], [–], [–], [1], [–], [–], [–], [–], [4], [–], [*1,25*], [–],
  [*1.3.* Phép toán tập hợp _(Bài 2b)_], [1], [–], [–], [–], [1], [1], [–], [–], [1], [1], [–], [–], [4], [1], [*1,25*], [*1,00*],

  table.cell(rowspan: 2)[*2*],
  table.cell(rowspan: 2)[*Chương II.*\ BPT & Hệ BPT\ bậc nhất 2 ẩn\ *(2,50 điểm)*],
  [*2.1.* BPT bậc nhất hai ẩn _(Bài 3)_], [1], [–], [–], [1], [2], [1], [–], [–], [–], [–], [–], [–], [5], [–], [*1,25*], [–],
  [*2.2.* Hệ BPT bậc nhất 2 ẩn _(Bài 4)_], [1], [–], [–], [–], [–], [–], [–], [–], [–], [–], [–], [1], [1], [1], [*0,25*], [*1,00*],

  table.cell(rowspan: 2)[*3*],
  table.cell(rowspan: 2)[*Chương III.*\ Hệ thức lượng\ trong tam giác\ *(3,00 điểm)*],
  [*3.1.* GTLG góc $0^degree arrow.r 180^degree$ _(Bài 5)_], [1], [1], [–], [–], [–], [–], [–], [–], [1], [–], [–], [–], [3], [–], [*1,00*], [–],
  [*3.2.* Hệ thức lượng tam giác _(Bài 6)_], [1], [1], [–], [–], [–], [–], [–], [1], [–], [–], [1], [–], [3], [1], [*1,00*], [*1,00*],

  [*4*],
  [*Chương IV.*\ Vectơ *(0,50đ)*],
  [*4.1.* Khái niệm vectơ _(Bài 7)_], [1], [1], [–], [–], [–], [–], [–], [–], [–], [–], [–], [–], [2], [–], [*0,50*], [–],

  table.cell(colspan: 3)[*TỔNG TOÀN ĐỀ (27 LỆNH HỎI = 10,0 ĐIỂM)*],
  [*9*], [*3*], [*0*], [*2*], [*4*], [*2*], [*0*], [*2*], [*2*], [*1*], [*1*], [*1*], [*24*], [*3*], [*7,00*], [*3,00*],
)
#set text(size: 9.8pt)

#v(4pt)
#grid(
  columns: (1fr, 1fr),
  column-gutter: 10pt,
  mnemonic-box("Phân tích Trọng số Điểm 4 Chương trong Ma trận", [
    • *Chương I (Mệnh đề & Tập hợp):* Chiếm *4,00 điểm (40% đề thi)* — riêng *Mục 1.3 (Phép toán tập hợp)* chiếm tới *2,25 điểm*!\
    • *Chương III (Hệ thức lượng trong tam giác):* Chiếm *3,00 điểm (30%)* (gồm 2 câu P.I + 2 câu P.III + Câu 2 Tự luận thực tế 1,0đ).\
    • *Chương II (BPT & Hệ BPT bậc nhất 2 ẩn):* Chiếm *2,50 điểm (25%)* (gồm 2 câu P.I + trọn vẹn Câu 2 Đúng/Sai 1,0đ + Câu 3 Tự luận VDC 1,0đ).\
    • *Chương IV (Khái niệm Vectơ – Bài 7):* Chiếm *0,50 điểm (5%)* (chỉ hỏi đúng 2 câu Phần I: Câu 11 NB và Câu 12 TH).
  ]),
  trap-box("Lưu ý đối chiếu Bảng Ma trận & Bảng Đặc tả", [
    • Ở *Mục 3.2 (Hệ thức lượng trong tam giác)*: Ma trận (Bảng 1) quy định chính xác *3 lệnh hỏi TN (1,0đ) + 1 câu TL (1,0đ)*, được liệt kê rõ trong Bản đặc tả (Bảng 2) gồm: *Câu 9 (NB)* và *Câu 10 (TH)* ở Phần I ($2 times 0,25 = 0,50$ đ), *Câu 4 (TH)* ở Phần III Trả lời ngắn ($0,50$ đ), và *Câu 2 (VD)* ở Phần IV Tự luận ($1,00$ đ).\
    • Như vậy: *Chương I + Chương III = 7,0 điểm*; nếu nắm chắc thêm *Câu 2 Đúng/Sai* và *Câu 3 Tự luận* của Chương II là chinh phục trọn vẹn *10/10 điểm*!
  ])
)

== A.2. Bản Đồ 27 Lệnh Hỏi Chính Thức Trong Đề Kiểm Tra Giữa Kì I (2026–2027)

#set text(size: 8.0pt)
#table(
  columns: (1.05fr, 1.05fr, 1.35fr, 3.15fr),
  align: (left + horizon, center + horizon, left + horizon, left + horizon),
  stroke: 0.5pt + c-border,
  fill: (x, y) => if y == 0 { c-navy } else if calc.odd(y) { rgb("#F8FAFC") } else { white },
  inset: (x: 5pt, y: 2.8pt),
  [#text(fill: white, weight: "bold")[Phần & Câu hỏi]],
  [#text(fill: rgb("#FACC15"), weight: "bold")[Mức độ & Điểm]],
  [#text(fill: white, weight: "bold")[Đơn vị kiến thức]],
  [#text(fill: white, weight: "bold")[Nội dung kiểm tra cụ thể theo đúng Bản đặc tả THPT Hà Huy Tập]],

  [*Phần I — Câu 1*], [NB — 0,25 đ], [1.1. Mệnh đề], [Nhận biết mệnh đề toán học, mệnh đề phủ định $overline(P)$, mệnh đề chứa biến $P(x)$.],
  [*Phần I — Câu 2*], [NB — 0,25 đ], [1.1. Mệnh đề], [Ý nghĩa kí hiệu phổ biến ($forall$) và tồn tại ($exists$); mệnh đề phủ định chứa $forall, exists$.],
  [*Phần I — Câu 3*], [NB — 0,25 đ], [1.2. Tập hợp], [Cho tập hợp bằng cách liệt kê phần tử hoặc chỉ ra tính chất đặc trưng.],
  [*Phần I — Câu 4*], [NB — 0,25 đ], [1.3. Phép toán tập hợp], [Dùng biểu đồ Ven để nhận biết biểu diễn giao ($A inter B$), hợp ($A union B$), hiệu ($A backslash B$).],
  [*Phần I — Câu 5*], [NB — 0,25 đ], [2.1. BPT bậc nhất 2 ẩn], [Nhận biết dạng của bất phương trình bậc nhất hai ẩn ($a x + b y < c, <=, >, >=$).],
  [*Phần I — Câu 6*], [NB — 0,25 đ], [2.2. Hệ BPT bậc nhất 2 ẩn], [Nhận biết hệ BPT bậc nhất hai ẩn; kiểm tra cặp số $(x_0; y_0)$ thuộc miền nghiệm.],
  [*Phần I — Câu 7*], [NB — 0,25 đ], [3.1. GTLG góc $0^degree arrow.r 180^degree$], [Nhận biết GTLG góc đặc biệt, hệ thức hai góc phụ nhau / bù nhau, bấm máy tính.],
  [*Phần I — Câu 8*], [TH — 0,25 đ], [3.1. GTLG góc $0^degree arrow.r 180^degree$], [Tính GTLG của một góc khi biết 1 trong 4 GTLG ($sin alpha, cos alpha, tan alpha, cot alpha$).],
  [*Phần I — Câu 9*], [NB — 0,25 đ], [3.2. Hệ thức lượng $Delta$], [Nhận biết công thức định lí côsin, định lí sin, các công thức diện tích tam giác.],
  [*Phần I — Câu 10*], [TH — 0,25 đ], [3.2. Hệ thức lượng $Delta$], [Áp dụng định lí côsin, định lí sin, diện tích tam giác để tính cạnh, góc, $S, R, r$.],
  [*Phần I — Câu 11*], [NB — 0,25 đ], [4.1. Khái niệm vectơ], [Khái niệm vectơ, độ dài, cùng phương, cùng hướng, bằng nhau; vectơ-không $arrow(0)$.],
  [*Phần I — Câu 12*], [TH — 0,25 đ], [4.1. Khái niệm vectơ], [Đặc điểm vectơ, chứng minh / nhận diện hai vectơ bằng nhau trong hình học phẳng.],
  [*Phần II — Câu 1*\ _(4 ý: a, b, c, d)_], [1a: NB | 1b,1c: TH\ 1d: VD — *1,00 đ*], [1.2 & 1.3. Tập hợp &\ Phép toán tập hợp], [*1a:* Kí hiệu $in, in.not, subset, supset, emptyset$, khoảng/đoạn. *1b:* Biểu diễn trên trục số, tập con/bằng nhau. *1c:* Tính $A inter B, A union B, C_R A$. *1d:* Phép toán tập hợp mức vận dụng / chứa tham số $m$.],
  [*Phần II — Câu 2*\ _(4 ý: a, b, c, d)_], [2a: NB | 2b,2c: TH\ 2d: VD — *1,00 đ*], [2.1. Bất phương trình\ bậc nhất hai ẩn], [*2a:* Nghiệm & miền nghiệm BPT. *2b, 2c:* Mô tả miền nghiệm trên mặt phẳng $O x y$ (đường bờ, nửa mặt phẳng). *2d:* Chuyển điều kiện bài toán thực tế về BPT bậc nhất 2 ẩn.],
  [*Phần III — Câu 1*], [TH — 0,50 đ], [1.2. Tập hợp], [Tìm số tập hợp con của một tập hợp ($2^n$ tập con, tập con có điều kiện).],
  [*Phần III — Câu 2*], [VD — 0,50 đ], [1.3. Phép toán tập hợp], [Bài toán thực tế sử dụng các phép toán tập hợp và công thức biểu đồ Ven.],
  [*Phần III — Câu 3*], [VD — 0,50 đ], [3.1. GTLG góc $0^degree arrow.r 180^degree$], [Cho biết 1 giá trị lượng giác (VD: $tan alpha = k$), tính giá trị của một biểu thức lượng giác.],
  [*Phần III — Câu 4*], [TH — 0,50 đ], [3.2. Hệ thức lượng $Delta$], [Tính cạnh, góc, diện tích tam giác hoặc giải bài toán thực tiễn đơn giản bằng ĐL sin/côsin.],
  [*Phần IV — Câu 1*], [TH (MĐ2) — 1,00 đ], [1.3. Phép toán tập hợp], [Thực hiện các phép toán giao ($A inter B$), hợp ($A union B$), hiệu ($A backslash B$), phần bù ($C_R A$).],
  [*Phần IV — Câu 2*], [VD (MĐ2) — 1,00 đ], [3.2. Hệ thức lượng $Delta$], [Vận dụng hệ thức lượng trong tam giác giải bài toán thực tiễn (khoảng cách, chiều cao...).],
  [*Phần IV — Câu 3*], [VDC (MĐ3) — 1,00 đ], [2.2. Hệ BPT bậc nhất 2 ẩn], [Mô tả miền nghiệm hệ BPT bậc nhất 2 ẩn và tìm giá trị tối ưu (GTLN / GTNN) thực tiễn.],
)
#set text(size: 9.8pt)

== A.3. Chiến thuật Phân bổ 90 Phút Vàng & Checklist Rà soát

#set text(size: 8.3pt)
#table(
  columns: (1.1fr, 1.35fr, 2.45fr, 0.85fr),
  align: (left + horizon, left + horizon, left + horizon, center + horizon),
  stroke: 0.5pt + c-border,
  fill: (x, y) => if y == 0 { rgb("#F1F5F9") } else { white },
  inset: (x: 5.5pt, y: 3.3pt),
  [*Phần thi*], [*Cấu trúc & Thang điểm*], [*Chiến thuật làm bài ăn trọn điểm — Tránh bẫy thường gặp*], [*Thời gian*],
  [*PHẦN I*\ Nhiều lựa chọn], [12 câu $times$ 0,25 đ\ = *3,00 điểm*], [9 câu Nhận biết giải nhanh trong 7 phút; 3 câu Thông hiểu (Câu 8, 10, 12) nháp cẩn thận dấu của $cos alpha$ ở góc tù và thứ tự đỉnh vectơ.], [*15 phút*\ _(Phút 0–15)_],
  [*PHẦN II*\ Đúng / Sai], [2 câu $times$ 4 ý = *2,00 điểm*\ 1 ý: 0,1đ | 2 ý: 0,25đ\ 3 ý: 0,5đ | *4 ý: 1,00đ*], [*Ý thứ 4 quyết định 0,50 điểm!* Ở Câu 1 chú ý ngoặc tròn `()` vs ngoặc vuông `[]` và $emptyset subset A$; ở Câu 2 chú ý kể cả bờ ($<=, >=$) vs không kể bờ ($<, >$).], [*15 phút*\ _(Phút 15–30)_],
  [*PHẦN III*\ Trả lời ngắn], [4 câu $times$ 0,50 đ\ = *2,00 điểm*], [Mỗi câu trị giá *0,50 điểm* (gấp đôi câu Phần I)! Đọc kỹ yêu cầu làm tròn (đến hàng đơn vị, hàng phần mười hay phần trăm).], [*15 phút*\ _(Phút 30–45)_],
  [*PHẦN IV*\ Tự luận], [3 câu $times$ 1,00 đ\ = *3,00 điểm*], [• *Câu 1 (1,0đ):* Vẽ trục số minh họa và kết luận rõ ràng từng tập hợp.\ • *Câu 2 (1,0đ):* Nêu rõ áp dụng Định lí Côsin / Định lí Sin trong tam giác nào.\ • *Câu 3 (1,0đ):* Trình bày đủ 4 bước: Gọi ẩn + Hệ BPT $arrow.r$ Vẽ miền đa giác & Tìm đỉnh $arrow.r$ Tính $F(x;y)$ tại các đỉnh $arrow.r$ Kết luận.], [*35 phút*\ _(Phút 45–80)_],
  [*RÀ SOÁT*], [Kiểm tra toàn bài], [Kiểm tra lại phiếu tô trắc nghiệm (12 câu P.I + 8 ý P.II + 4 câu P.III) và đơn vị, kết luận ở 3 bài Tự luận.], [*10 phút*\ _(Phút 80–90)_],
)
#set text(size: 9.8pt)

#pagebreak()

// ============================================================================
// PHẦN B: TỜ CÔNG THỨC VÀNG 1 TRANG & 10 KHẨU QUYẾT SIÊU TRÍ NHỚ
// ============================================================================

= PHẦN B. “TỜ CÔNG THỨC VÀNG 1 TRANG” & 10 KHẨU QUYẾT SIÊU TRÍ NHỚ

== B.1. Bảng Tổng Hợp 100% Công Thức Toán 10 Giữa Kì I (Tra Cứu Thần Tốc)

#set text(size: 7.7pt)
#table(
  columns: (1.14fr, 1.94fr, 2.18fr),
  align: (left + horizon, center + horizon, left + horizon),
  stroke: 0.5pt + c-border,
  fill: (x, y) => if y == 0 { c-navy } else if calc.odd(y) { rgb("#F8FAFC") } else { white },
  inset: (x: 4.5pt, y: 2.2pt),
  [#text(fill: white, weight: "bold")[Chủ đề / Đơn vị]],
  [#text(fill: rgb("#FACC15"), weight: "bold")[Công thức & Quy tắc chuẩn SGK Kết nối tri thức]],
  [#text(fill: white, weight: "bold")[Giải thích ký hiệu & Lưu ý vàng khi làm bài]],

  [*1. Mệnh đề &\ Lượng từ $forall, exists$*\ _(Mục 1.1)_],
  [Phủ định của $P$: $overline(P)$\ $overline(forall x in X comma P(x)) arrow.l.r.double exists x in X comma overline(P(x))$\ $overline(exists x in X comma P(x)) arrow.l.r.double forall x in X comma overline(P(x))$],
  [• $P arrow.r.double Q$ *chỉ SAI* khi $P$ đúng mà $Q$ sai ($1 arrow.r.double 0$).\ • Trong $P arrow.r.double Q$: *$P$ là điều kiện ĐỦ* để có $Q$; *$Q$ là điều kiện CẦN* để có $P$.\ • Đổi dấu phủ định: $=$ thành $!=$, $>$ thành $<=$, $<$ thành $>=$.],

  [*2. Tập hợp &\ Số tập con*\ _(Mục 1.2)_],
  [$NN^* subset NN subset ZZ subset QQ subset RR$\ Tập $A$ có $n$ phần tử $arrow.r.double$ Số tập con $= 2^n$\ Tập con khác $emptyset$: $2^n - 1$ | Tập con thực sự: $2^n - 1$],
  [• Kí hiệu: *Phần tử $in$ Tập hợp* (VD: $1 in A$); *Tập con $subset$ Tập hợp* (VD: $\{1\} subset A, emptyset subset A$).\ • Tập rỗng $emptyset$ và chính $A$ luôn là tập con của mọi tập $A$.\ • Số tập con gồm đúng $k$ phần tử ($0 <= k <= n$): $C_n^k = frac(n!, k!(n-k)!)$.],

  [*3. Các tập con\ của $RR$*\ _(Mục 1.2)_],
  [Đoạn $[a; b] = \{x in RR | a <= x <= b\}$\ Khoảng $(a; b) = \{x in RR | a < x < b\}$\ Nửa khoảng $[a; b) = \{a <= x < b\}$; $(a; b] = \{a < x <= b\}$],
  [• Ngoặc vuông `[a; b]` ứng với dấu $<=, >=$ (*lấy* đầu mút).\ • Ngoặc tròn `(a; b)` ứng với dấu $<, >$ (*không lấy* đầu mút).\ • Tại $-infinity$ và $+infinity$ *luôn luôn dùng ngoặc tròn*: $(-infinity; a], [a; +infinity)$.],

  [*4. Phép toán\ trên tập hợp*\ _(Mục 1.3)_],
  [$A inter B = \{x | x in A " và " x in B\}$ _(Giao)_\ $A union B = \{x | x in A " hoặc " x in B\}$ _(Hợp)_\ $A backslash B = \{x | x in A " và " x in.not B\}$ _(Hiệu)_\ $C_E A = E backslash A$ (khi $A subset E$) _(Phần bù)_],
  [• *Mẹo lấy Hiệu $A backslash B$ hoặc Phần bù $C_RR A$ trên trục số:* Phần đầu mút bị gạch bỏ bởi tập $B$ sẽ *ĐỔI NGOẶC*: ngoặc tròn `(` đổi thành vuông `]`, ngoặc vuông `[` đổi thành tròn `)`!\ • Điều kiện $A inter B = emptyset$ với $A = [a; b], B = (c; d)$: $b <= c$ hoặc $d <= a$.],

  [*5. Công thức đếm\ Biểu đồ Ven*\ _(Mục 1.3 — TLN 2)_],
  [*2 tập hợp:* $n(A union B) = n(A) + n(B) - n(A inter B)$\ *Chỉ riêng $A$:* $n(A backslash B) = n(A) - n(A inter B)$\ *3 tập hợp:* $n(A union B union C) = n(A)+n(B)+n(C)$\ $- n(A inter B) - n(B inter C) - n(C inter A) + n(A inter B inter C)$],
  [• Nếu cả lớp có $N$ học sinh, trong đó có $k$ em *không tham gia câu lạc bộ nào* thì số học sinh tham gia ít nhất 1 CLB là: *$n(A union B) = N - k$*.\ • Số học sinh tham gia *đúng 1 môn*: $n(A) + n(B) - 2 n(A inter B)$.],

  [*6. BPT & Hệ BPT\ bậc nhất 2 ẩn*\ _(Mục 2.1 & 2.2)_],
  [Dạng: $a x + b y < c$ (hoặc $<=, >, >=$) với $a^2 + b^2 > 0$\ Đường thẳng bờ $d: a x + b y = c$\ PT đoạn chắn qua $A(a; 0), B(0; b)$: $frac(x, a) + frac(y, b) = 1$],
  [• *Thử điểm $M_0(x_0; y_0) in.not d$* (thường chọn gốc $O(0; 0)$ nếu $c != 0$): Nếu $a x_0 + b y_0 <= c$ *ĐÚNG* $arrow.r$ miền nghiệm là nửa mặt phẳng bờ $d$ *chứa $M_0$*.\ • *Bài toán tối ưu:* Giá trị GTLN / GTNN của $F(x; y) = a x + b y$ trên miền đa giác lồi đạt tại *một trong các đỉnh* của đa giác đó.],

  [*7. GTLG góc\ $0^degree arrow.r 180^degree$*\ _(Mục 3.1)_],
  [Với $M(x_0; y_0)$ trên nửa đường tròn đơn vị:\ $sin alpha = y_0 in [0; 1]$; #h(6pt) $cos alpha = x_0 in [-1; 1]$\ $tan alpha = frac(sin alpha, cos alpha)$ ($alpha != 90^degree$); #h(4pt) $cot alpha = frac(cos alpha, sin alpha)$ ($0^degree < alpha < 180^degree$)],
  [• *Hai góc bù nhau ($180^degree - alpha$):* $sin(180^degree - alpha) = sin alpha$, còn $cos, tan, cot$ *đổi dấu âm* ($cos(180^degree - alpha) = -cos alpha$).\ • *Hai góc phụ nhau ($90^degree - alpha$):* $sin(90^degree - alpha) = cos alpha$, $tan(90^degree - alpha) = cot alpha$.\ • *4 Hệ thức cơ bản:* $sin^2 alpha + cos^2 alpha = 1$; $tan alpha dot cot alpha = 1$; $1 + tan^2 alpha = frac(1, cos^2 alpha)$; $1 + cot^2 alpha = frac(1, sin^2 alpha)$.],

  [*8. Định lí Côsin,\ Sin & Trung tuyến*\ _(Mục 3.2)_],
  [*Định lí Côsin:* $a^2 = b^2 + c^2 - 2 b c cos A$\ $arrow.r.double cos A = frac(b^2 + c^2 - a^2, 2 b c)$\ *Định lí Sin:* $frac(a, sin A) = frac(b, sin B) = frac(c, sin C) = 2 R$\ *Trung tuyến:* $m_a^2 = frac(b^2 + c^2, 2) - frac(a^2, 4) = frac(2(b^2 + c^2) - a^2, 4)$],
  [• Dùng *Định lí Côsin* khi biết: *(1)* 2 cạnh và góc xen giữa ($b, c, hat(A)$), hoặc *(2)* cả 3 cạnh ($a, b, c$).\ • Dùng *Định lí Sin* khi biết: *(1)* 1 cạnh và 2 góc, hoặc *(2)* tìm bán kính đường tròn ngoại tiếp $R = frac(a, 2 sin A)$.\ • Kiểm tra góc tù/nhọn: $b^2 + c^2 > a^2 arrow.r hat(A)$ nhọn; $b^2 + c^2 < a^2 arrow.r hat(A)$ tù.],

  [*9. 5 Công thức\ Diện tích $Delta A B C$*\ _(Mục 3.2)_],
  [$S = frac(1, 2) a h_a = frac(1, 2) b c sin A = frac(a b c, 4 R) = p r$\ *Công thức Heron:* $S = sqrt(p(p - a)(p - b)(p - c))$],
  [• $p = frac(a + b + c, 2)$ là *nửa chu vi* tam giác; $R$ là bán kính đường tròn ngoại tiếp; $r$ là bán kính đường tròn nội tiếp.\ • Suy ra nhanh: $h_a = frac(2 S, a)$; #h(6pt) $R = frac(a b c, 4 S)$; #h(6pt) $r = frac(S, p)$.],

  [*10. Khái niệm\ Vectơ*\ _(Mục 4.1)_],
  [Độ dài: $|arrow(A B)| = A B$; #h(6pt) Vectơ-không: $arrow(0) = arrow(A A)$\ Hai vectơ bằng nhau: $arrow(a) = arrow(b) arrow.l.r.double cases(arrow(a) " và " arrow(b) " cùng hướng", |arrow(a)| = |arrow(b)|)$],
  [• *Giá của vectơ* $arrow(A B)$ là đường thẳng $A B$. Hai vectơ *cùng phương* $arrow.l.r.double$ giá của chúng *song song hoặc trùng nhau*.\ • Từ $n$ điểm phân biệt lập được *$n(n - 1)$* vectơ khác $arrow(0)$.\ • Trong hình bình hành $A B C D$: $arrow(A B) = arrow(D C)$ và $arrow(A D) = arrow(B C)$.],
)

#v(3pt)
#table(
  columns: (1.3fr, 0.7fr, 0.85fr, 0.85fr, 0.85fr, 0.85fr, 0.85fr, 0.85fr, 0.85fr, 0.75fr),
  align: center + horizon,
  stroke: 0.5pt + c-border,
  fill: (x, y) => if y == 0 { rgb("#1E3A8A") } else if calc.odd(y) { rgb("#EFF6FF") } else { white },
  inset: (x: 3pt, y: 3pt),
  [#text(fill: white, weight: "bold")[Góc đặc biệt $alpha$]],
  [#text(fill: rgb("#FACC15"), weight: "bold")[$0^degree$]],
  [#text(fill: rgb("#FACC15"), weight: "bold")[$30^degree$]],
  [#text(fill: rgb("#FACC15"), weight: "bold")[$45^degree$]],
  [#text(fill: rgb("#FACC15"), weight: "bold")[$60^degree$]],
  [#text(fill: rgb("#FACC15"), weight: "bold")[$90^degree$]],
  [#text(fill: rgb("#FACC15"), weight: "bold")[$120^degree$]],
  [#text(fill: rgb("#FACC15"), weight: "bold")[$135^degree$]],
  [#text(fill: rgb("#FACC15"), weight: "bold")[$150^degree$]],
  [#text(fill: rgb("#FACC15"), weight: "bold")[$180^degree$]],
  [*$sin alpha$*], [$0$], [$1/2$], [$sqrt(2)/2$], [$sqrt(3)/2$], [$1$], [$sqrt(3)/2$], [$sqrt(2)/2$], [$1/2$], [$0$],
  [*$cos alpha$*], [$1$], [$sqrt(3)/2$], [$sqrt(2)/2$], [$1/2$], [$0$], [$-1/2$], [$-sqrt(2)/2$], [$-sqrt(3)/2$], [$-1$],
  [*$tan alpha$*], [$0$], [$sqrt(3)/3$], [$1$], [$sqrt(3)$], [$||$], [$-sqrt(3)$], [$-1$], [$-sqrt(3)/3$], [$0$],
  [*$cot alpha$*], [$||$], [$sqrt(3)$], [$1$], [$sqrt(3)/3$], [$0$], [$-sqrt(3)/3$], [$-1$], [$-sqrt(3)$], [$||$],
)
#set text(size: 9.8pt)

#pagebreak()

== B.2. 10 Khẩu Quyết Siêu Trí Nhớ — Đọc 1 Lần Thuộc Ngay Toàn Bộ Đề Cương

#grid(
  columns: (1fr, 1fr),
  column-gutter: 10pt,
  row-gutter: 6.5pt,
  mnemonic-box("1. Nhận diện Mệnh đề & Bảng chân trị (Mục 1.1)", [
    *“Cảm – Cầu – Hỏi: KHÔNG phải mệnh đề; Kéo theo chỉ SAI khi Đúng kéo Sai”*\
    • Câu hỏi (`?`), câu cảm thán (`!`), câu mệnh lệnh *không* phải là mệnh đề.\
    • Mệnh đề $P arrow.r.double Q$ chỉ *SAI* duy nhất khi *$P$ Đúng mà $Q$ Sai* (còn $P$ Sai thì $P arrow.r.double Q$ luôn Đúng!).
  ]),
  mnemonic-box("2. Phủ định Lượng từ ∀ và ∃ (Mục 1.1 — Câu 2 TN)", [
    *“Đổi VỚI MỌI ($forall$) thành TỒN TẠI ($exists$) — Đổi luôn dấu mệnh đề sau!”*\
    • *Giữ nguyên* tập hợp nguồn $x in X$ (tuyệt đối không đổi $x in RR$ thành $x in.not RR$!).\
    • Đổi cặp dấu đối lập: ($=$ $arrow.l.r$ $!=$), ($>$ $arrow.l.r$ $<=$), ($<$ $arrow.l.r$ $>=$), (“chia hết” $arrow.l.r$ “không chia hết”).
  ]),
  mnemonic-box("3. Điều kiện Cần vs Điều kiện Đủ (Mục 1.1)", [
    *“TRƯỚC ĐỦ — SAU CẦN”* (Trong mệnh đề đúng $P arrow.r.double Q$):\
    • Giả thiết đứng *trước* mũi tên ($P$) là *điều kiện ĐỦ* để có $Q$.\
    • Kết luận đứng *sau* mũi tên ($Q$) là *điều kiện CẦN* để có $P$.
  ]),
  mnemonic-box("4. Kí hiệu Tập hợp & Đếm Tập con (Mục 1.2)", [
    *“Phần tử THUỘC ($in$) — Tập con CHỨA ($subset$) — Rỗng con mọi nhà ($emptyset subset A$)”*\
    • Viết $a in A$ nhưng phải viết $\{a\} subset A$. Kí hiệu $\{emptyset\}$ là tập có *1 phần tử* (không phải tập rỗng!).\
    • Tập có $n$ phần tử có đúng *$2^n$ tập con*, *$2^n - 1$ tập con khác rỗng*.
  ]),
  mnemonic-box("5. 4 Phép toán Tập hợp trên Trục số (Mục 1.3)", [
    *“GIAO lấy CHUNG — HỢP lấy TẤT — HIỆU lấy RIÊNG (Đổi ngoặc đầu mút!)”*\
    • Khi tính $A backslash B$ hoặc $C_RR A = RR backslash A$: tại biên bị gạch bỏ, ngoặc tròn `(` biến thành ngoặc vuông `[`, ngoặc vuông `[` biến thành ngoặc tròn `)`!
  ]),
  mnemonic-box("6. Thử miền nghiệm BPT trong 5 giây (Mục 2.1)", [
    *“Thay gốc O(0; 0) — Đúng lấy chứa O, Sai bỏ chứa O; Có dấu bằng lấy bờ”*\
    • Nếu đường bờ $a x + b y = c$ có $c != 0$, thay $(0; 0)$ vào vế trái được $0$: so sánh $0$ với $c$ là biết ngay miền nghiệm chứa $O$ hay không!\
    • Nếu $c = 0$ (bờ đi qua $O$), thay điểm $M(1; 0)$ hoặc $N(0; 1)$.
  ]),
  mnemonic-box("7. Góc bù nhau & Dấu GTLG Góc tù (Mục 3.1)", [
    *“SIN BÙ — PHỤ CHÉO — Góc tù chỉ mỗi SIN dương!”*\
    • Hai góc bù nhau ($alpha + beta = 180^degree$): *chỉ có $sin$ bằng nhau* ($sin(180^degree - alpha) = sin alpha$), còn $cos, tan, cot$ đều *thêm dấu trừ*!\
    • Khi $90^degree < alpha < 180^degree$ (góc tù): $sin alpha > 0$, nhưng *$cos alpha < 0, tan alpha < 0, cot alpha < 0$*.
  ]),
  mnemonic-box("8. Tính Biểu thức Lượng giác khi biết tan α (Câu 3 TLN)", [
    *“Biết $tan alpha$ chia cho $cos alpha$ — Biết $cot alpha$ chia cho $sin alpha$”*\
    • Gặp $P = frac(a sin alpha + b cos alpha, c sin alpha + d cos alpha)$ khi biết $tan alpha = k$: chia cả tử và mẫu cho $cos alpha$ được ngay *$P = frac(a tan alpha + b, c tan alpha + d) = frac(a k + b, c k + d)$*!
  ]),
  mnemonic-box("9. Chọn Định lí Côsin hay Định lí Sin? (Mục 3.2)", [
    *“Hai cạnh góc xen (C-G-C) hoặc Ba cạnh (C-C-C) $arrow.r$ CÔSIN; Nhiều góc hoặc Bán kính $R$ $arrow.r$ SIN”*\
    • Nhớ hệ số $2 R$ trong Định lí Sin: $frac(a, sin A) = 2 R arrow.r.double a = 2 R sin A$ và $R = frac(a, 2 sin A)$ (đừng quên số $2$!).
  ]),
  mnemonic-box("10. Phản xạ Vectơ trong 3 giây (Mục 4.1)", [
    *“Vectơ-không ($arrow(0)$) cùng phương, cùng hướng MỌI vectơ — Hình bình hành $A B C D$ có $arrow(A B) = arrow(D C)$”*\
    • Đếm vectơ khác $arrow(0)$ từ $n$ điểm: lấy *$n(n - 1)$* (VD: 4 điểm tạo ra $4 times 3 = 12$ vectơ; 5 điểm tạo ra $5 times 4 = 20$ vectơ).
  ]),
)

#pagebreak()
