#import "template.typ": *

// ============================================================================
// TRANG BÌA & MỤC LỤC TỔNG QUAN
// ============================================================================

#block(
  width: 100%,
  fill: c-navy,
  radius: 10pt,
  inset: (x: 18pt, y: 12pt),
  breakable: false,
)[
  #grid(
    columns: (1fr, auto),
    align: (left + horizon, right + horizon),
    gutter: 6pt,
    [
      #text(fill: rgb("#93C5FD"), size: 8.0pt, weight: "bold", tracking: 0.1pt)[TRƯỜNG THPT HÀ HUY TẬP • TỔ TOÁN – TIN • NĂM HỌC 2026–2027]
    ],
    box(fill: rgb("#1E40AF"), stroke: 0.7pt + rgb("#60A5FA"), radius: 4pt, inset: (x: 8pt, y: 3pt))[
      #text(fill: white, size: 7.8pt, weight: "bold")[SGK KẾT NỐI TRI THỨC VỚI CUỘC SỐNG]
    ]
  )
  #v(5pt)
  #text(fill: rgb("#FACC15"), size: 10.5pt, weight: "bold", tracking: 0.5pt)[TÀI LIỆU HỆ THỐNG HÓA LÝ THUYẾT, PHƯƠNG PHÁP & LUYỆN ĐỀ THỰC CHIẾN]
  #v(3pt)
  #text(fill: white, size: 19.5pt, weight: "extrabold")[ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I]
  #v(2pt)
  #text(fill: rgb("#60A5FA"), size: 14.5pt, weight: "extrabold")[MÔN TOÁN LỚP 10 — NĂM HỌC 2026–2027]
  #v(5pt)
  #line(length: 100%, stroke: 0.7pt + rgb("#334155"))
  #v(4.5pt)
  #text(fill: rgb("#E2E8F0"), size: 8.8pt)[
    Biên soạn bám sát *100% từng ô câu hỏi, mức độ nhận thức và chỉ báo kỹ năng* trong văn bản gốc *Ma trận & Bảng đặc tả Đề kiểm tra Giữa kì I năm học 2026–2027* của nhà trường. Bao gồm đầy đủ lý thuyết trực quan từ *Bài 1 đến Bài 7*, ngân hàng bài tập phân dạng và *trọn bộ câu hỏi kèm đáp án, lời giải chi tiết bài kiểm tra giữa học kì I năm học 2026–2027*.
  ]
]

#v(4.5pt)

#grid(
  columns: (1fr, 1fr, 1fr, 1fr),
  gutter: 7pt,
  block(width: 100%, fill: c-blue-bg, stroke: 0.9pt + c-blue-bd, radius: 6pt, inset: (x: 7pt, y: 5.5pt))[
    #align(center)[
      #text(fill: c-primary, size: 12.5pt, weight: "extrabold")[90 Phút]\
      #text(fill: c-navy, size: 8pt, weight: "bold")[7,0đ TN + 3,0đ TL]\
      #text(fill: c-slate, size: 7.5pt)[4 phần thi chuẩn Bộ GD&ĐT]
    ]
  ],
  block(width: 100%, fill: c-teal-bg, stroke: 0.9pt + c-teal-bd, radius: 6pt, inset: (x: 7pt, y: 5.5pt))[
    #align(center)[
      #text(fill: c-teal, size: 12.5pt, weight: "extrabold")[4 Chương]\
      #text(fill: c-navy, size: 8pt, weight: "bold")[Bài 1 $arrow.r$ Bài 7 SGK]\
      #text(fill: c-slate, size: 7.5pt)[Kết nối tri thức Tập 1]
    ]
  ],
  block(width: 100%, fill: c-amber-bg, stroke: 0.9pt + c-amber-bd, radius: 6pt, inset: (x: 7pt, y: 5.5pt))[
    #align(center)[
      #text(fill: c-amber, size: 12.5pt, weight: "extrabold")[75 Bài Tập]\
      #text(fill: c-navy, size: 8pt, weight: "bold")[Ngân hàng 4 dạng thức]\
      #text(fill: c-slate, size: 7.5pt)[Phủ kín 100% ô Đặc tả]
    ]
  ],
  block(width: 100%, fill: c-red-bg, stroke: 0.9pt + c-red-bd, radius: 6pt, inset: (x: 7pt, y: 5.5pt))[
    #align(center)[
      #text(fill: c-red, size: 12.5pt, weight: "extrabold")[03 Đề Thi Mới]\
      #text(fill: c-navy, size: 8pt, weight: "bold")[66 Câu + Full Đáp án]\
      #text(fill: c-slate, size: 7.5pt)[Chuẩn Ma trận 2026–2027]
    ]
  ],
)

#v(4.5pt)

#block(
  width: 100%,
  fill: c-zebra,
  stroke: 0.8pt + c-border,
  radius: 7pt,
  inset: (x: 12pt, y: 7pt),
)[
  #text(fill: c-navy, size: 9.8pt, weight: "extrabold")[📌 LỘ TRÌNH 5 PHẦN KHÉP KÍN TRONG ĐỀ CƯƠNG]
  #v(2pt)
  #set text(size: 8.2pt)
  #set par(leading: 0.42em)
  #show outline.entry: set block(above: 3.2pt, below: 0pt)
  #outline(
    title: none,
    indent: 10pt,
    depth: 2,
  )
]

#v(4pt)
#block(
  width: 100%,
  fill: c-amber-bg,
  stroke: 0.8pt + c-amber-bd,
  radius: 6pt,
  inset: (x: 11pt, y: 5.5pt),
)[
  #text(fill: c-amber, weight: "bold", size: 8.7pt)[💡 HƯỚNG DẪN SỬ DỤNG ĐỀ CƯƠNG HIỆU QUẢ NHẤT CHO HỌC SINH LỚP 10:]
  #v(1.5pt)
  #set text(size: 8.1pt)
  #set par(leading: 0.45em)
  - *Mục tiêu nắm chắc 6,5 – 7,5 điểm:* Học kỹ *Phần B (Tờ Công thức Vàng + 12 Khẩu quyết)*, nắm vững ví dụ cơ bản ở *Phần C* và làm trọn vẹn các câu *Nhận biết – Thông hiểu* cùng *Câu 1 Tự luận (1,0 điểm phép toán tập hợp)*.
  - *Mục tiêu bứt phá 8,0 – 9,0 điểm:* Luyện thành thạo *Câu 1d, 2d Đúng/Sai*, *4 câu Trả lời ngắn (0,5 điểm/câu)* và *Câu 2 Tự luận (1,0 điểm bài toán đo đạc thực tế bằng Định lí Sin/Côsin)*.
  - *Mục tiêu chinh phục 9,5 – 10,0 điểm:* Làm chủ quy trình 4 bước giải bài toán tối ưu Quy hoạch tuyến tính ở *Câu 3 Tự luận (1,0 điểm VDC)* và bấm giờ 90 phút thực chiến đủ *03 Đề kiểm tra Giữa kì I năm học 2026–2027* ở *Phần E*.
]

#pagebreak()

// ============================================================================
// PHẦN A — GIẢI MÃ MA TRẬN ĐẶC TẢ & CHIẾN THUẬT 90 PHÚT VÀNG
// ============================================================================

= PHẦN A. GIẢI MÃ MA TRẬN ĐẶC TẢ & CHIẾN THUẬT PHÒNG THI 90 PHÚT

== A.1. Cấu trúc tổng thể đề kiểm tra Giữa kì I năm học 2026–2027 (90 phút — 10,0 điểm)

Theo văn bản *Ma trận và Bảng đặc tả Đề kiểm tra Giữa kì I năm học 2026–2027* của *Tổ Toán – Tin, Trường THPT Hà Huy Tập*, đề thi kết hợp *70% Trắc nghiệm khách quan (7,0 điểm)* và *30% Tự luận (3,0 điểm)* gồm 4 phần chuẩn định dạng mới:

#table(
  columns: (0.95fr, 1.85fr, 0.9fr, 1.05fr, 2.25fr),
  align: (left + horizon, left + horizon, center + horizon, center + horizon, left + horizon),
  stroke: 0.6pt + c-border,
  inset: (x: 6pt, y: 5pt),
  fill: (x, y) => if y == 0 { c-navy } else if calc.odd(y) { white } else { c-zebra },
  [#text(fill: white, weight: "bold", size: 8.5pt)[Phần thi]],
  [#text(fill: white, weight: "bold", size: 8.5pt)[Dạng thức câu hỏi]],
  [#text(fill: white, weight: "bold", size: 8.5pt)[Số lượng]],
  [#text(fill: white, weight: "bold", size: 8.5pt)[Thang điểm]],
  [#text(fill: white, weight: "bold", size: 8.5pt)[Phân bổ mức độ nhận thức]],

  [*PHẦN I*], [Trắc nghiệm nhiều phương án lựa chọn (A, B, C, D)], [12 câu], [*3,00 điểm*\ (0,25 đ/câu)], [*9 Nhận biết + 3 Thông hiểu*\ (0 Vận dụng — lấy điểm nền nhanh)],
  [*PHẦN II*], [Trắc nghiệm Đúng / Sai\ (mỗi câu gồm 4 ý a, b, c, d)], [2 câu\ *(8 lệnh hỏi)*], [*2,00 điểm*\ *(lũy tiến)*], [*2 Nhận biết + 4 Thông hiểu + 2 Vận dụng*\ • Đúng 1 ý: *0,1đ* | 2 ý: *0,25đ* | 3 ý: *0,5đ* | 4 ý: *1,0đ*],
  [*PHẦN III*], [Trắc nghiệm Trả lời ngắn\ (tự tính và điền đáp số)], [4 câu], [*2,00 điểm*\ *(0,50 đ/câu!)*], [*2 Thông hiểu + 2 Vận dụng*\ (Mỗi câu gấp đôi điểm 1 câu Phần I!)],
  [*PHẦN IV*], [Tự luận trình bày lời giải chi tiết], [3 câu], [*3,00 điểm*\ (1,00 đ/câu)], [*1 Thông hiểu (MĐ2) + 1 Vận dụng (MĐ2) + 1 VDC (MĐ3)*],
  [*TỔNG*], [*22 câu bài tập (27 lệnh hỏi)*], [*24 TN + 3 TL*], [*10,00 điểm*], [*NB: 2,75đ (27,5%) • TH: 3,75đ (37,5%) • VD: 2,50đ (25%) • VDC: 1,00đ (10%)*],
)

== A.2. Bảng giải mã trọng số điểm theo từng Chương & Bài học SGK Kết nối tri thức

#table(
  columns: (1.5fr, 1.75fr, 0.72fr, 0.78fr, 0.72fr, 0.72fr, 0.95fr),
  align: (left + horizon, left + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon),
  stroke: 0.55pt + c-border,
  inset: (x: 5pt, y: 4.5pt),
  fill: (x, y) => if y == 0 { c-blue-dark } else if y == 9 { c-blue-bg } else if calc.odd(y) { white } else { c-zebra },
  [#text(fill: white, weight: "bold", size: 8.2pt)[Chương (SGK Tập 1)]],
  [#text(fill: white, weight: "bold", size: 8.2pt)[Đơn vị kiến thức (Bài SGK)]],
  [#text(fill: white, weight: "bold", size: 8.2pt)[Phần I\ (0,25đ)]],
  [#text(fill: white, weight: "bold", size: 8.2pt)[Phần II\ (ý Đ/S)]],
  [#text(fill: white, weight: "bold", size: 8.2pt)[Phần III\ (0,50đ)]],
  [#text(fill: white, weight: "bold", size: 8.2pt)[Phần IV\ (1,00đ)]],
  [#text(fill: white, weight: "bold", size: 8.2pt)[Tổng điểm\ (Tỉ trọng)]],

  [*Chương I*\ Mệnh đề & Tập hợp\ *(4,00 điểm — 40%)*], [1.1. Mệnh đề *(Bài 1)*], [2 NB], [—], [—], [—], [*0,50 đ* (5,0%)],
  [*(Trọng tâm số 1)*], [1.2. Tập hợp *(Bài 2 – phần 1)*], [1 NB], [1 NB + 1 TH], [1 TH], [—], [*1,25 đ* (12,5%)],
  [], [1.3. Phép toán tập hợp *(Bài 2 – phần 2)*], [1 NB], [1 TH + 1 VD], [1 VD], [1 TH], [*2,25 đ* (22,5%)],

  [*Chương II*\ BPT & Hệ BPT bậc nhất 2 ẩn *(2,50đ — 25%)*], [2.1. BPT bậc nhất hai ẩn *(Bài 3)*], [1 NB], [1 NB + 2 TH + 1 VD], [—], [—], [*1,25 đ* (12,5%)],
  [], [2.2. Hệ BPT bậc nhất hai ẩn *(Bài 4)*], [1 NB], [—], [—], [1 VDC], [*1,25 đ* (12,5%)],

  [*Chương III*\ Hệ thức lượng tam giác *(3,00đ — 30%)*], [3.1. GTLG góc $0^circle arrow.r 180^circle$ *(Bài 5)*], [1 NB + 1 TH], [—], [1 VD], [—], [*1,00 đ* (10,0%)],
  [], [3.2. Hệ thức lượng tam giác *(Bài 6)*], [1 NB + 1 TH], [—], [1 TH], [1 VD], [*2,00 đ* (20,0%)],

  [*Chương IV: Vectơ*], [4.1. Khái niệm vectơ *(Chỉ học Bài 7!)*], [1 NB + 1 TH], [—], [—], [—], [*0,50 đ* (5,0%)],

  [*TỔNG TOÀN ĐỀ*], [*7 Bài học đầu tiên SGK Tập 1*], [*12 câu\ (3,0 đ)*], [*8 ý = 2 câu\ (2,0 đ)*], [*4 câu\ (2,0 đ)*], [*3 câu\ (3,0 đ)*], [*10,00 điểm\ (100%)*],
)

#trap-box("PHẠM VI CHƯƠNG IV (VECTƠ) & LƯU Ý ĐỐI CHIẾU MA TRẬN – ĐẶC TẢ")[
  1. *Giới hạn Chương IV cực kỳ quan trọng:* Giữa học kì I *chỉ kiểm tra đúng đơn vị 4.1 — Khái niệm vectơ (Bài 7 SGK)* với 2 câu trắc nghiệm (0,5 điểm). Các Bài 8, 9, 10, 11 (tổng/hiệu vectơ, tích vectơ với một số, tọa độ, tích vô hướng) thuộc nửa sau Học kì I — *tuyệt đối không ôn lan man gây mất thời gian!*
  2. *Riêng Bài 2 (Tập hợp & Các phép toán trên tập hợp)* chiếm tới *3,50 điểm (35% toàn đề thi)* xuất hiện ở cả 4 phần thi! Nắm chắc Bài 2 + Bài 6 (*2,00 điểm*) đã giúp em cầm chắc *5,50 điểm*.
  3. *Ghi chú chuẩn hóa Bảng đặc tả:* Ở dòng 3.2 trong Bảng đặc tả gốc có ghi số `2` ở cột Nhận biết do gộp nhầm đếm, trong khi nội dung mô tả chỉ rõ đúng *Câu 9 (NB)* và *Câu 10TN (TH)*, hoàn toàn khớp với Bảng Ma trận chuẩn (*9 NB + 3 TH = 12 câu Phần I*).
]

== A.3. Bản đồ định vị chính xác từng câu hỏi trong Đề KTGK I (2026–2027)

#grid(
  columns: (1fr, 1fr),
  gutter: 8pt,
  block(width: 100%, fill: white, stroke: 0.7pt + c-border, radius: 6pt, inset: 8pt)[
    #text(fill: c-primary, weight: "bold", size: 9.2pt)[🔹 PHẦN I — 12 CÂU CHỌN 1 ĐÁP ÁN (3,0 ĐIỂM)]
    #v(2pt)
    #set text(size: 8.3pt)
    - *Câu 1 (NB – 1.1):* Nhận biết mệnh đề, mệnh đề phủ định, mệnh đề chứa biến.
    - *Câu 2 (NB – 1.1):* Ý nghĩa và phủ định mệnh đề chứa kí hiệu $forall$, $exists$.
    - *Câu 3 (NB – 1.2):* Cho tập hợp bằng cách liệt kê hoặc chỉ ra tính chất đặc trưng.
    - *Câu 4 (NB – 1.3):* Dùng biểu đồ Ven nhận diện giao $A inter B$, hợp $A union B$, hiệu $A without B$.
    - *Câu 5 (NB – 2.1):* Nhận biết bất phương trình bậc nhất hai ẩn $a x + b y <= c$.
    - *Câu 6 (NB – 2.2):* Nhận biết hệ BPT bậc nhất hai ẩn, nghiệm và miền nghiệm.
    - *Câu 7 (NB – 3.1):* GTLG góc $0^circle arrow.r 180^circle$, hệ thức góc phụ – góc bù, bấm MTCT.
    - *Câu 8 (TH – 3.1):* Biết 1 trong 4 GTLG của góc $alpha$, tính giá trị lượng giác còn lại.
    - *Câu 9 (NB – 3.2):* Nhận diện công thức Định lí Côsin, Định lí Sin, diện tích $S$.
    - *Câu 10 (TH – 3.2):* Áp dụng Định lí Côsin, Sin, diện tích $S$ tính cạnh, góc, bài toán đơn giản.
    - *Câu 11 (NB – 4.1):* Khái niệm vectơ, độ dài, cùng phương, cùng hướng, bằng nhau, $vt(0)$.
    - *Câu 12 (TH – 4.1):* Đếm/chứng minh hai vectơ bằng nhau, cùng phương trên hình phẳng.
  ],
  block(width: 100%, fill: white, stroke: 0.7pt + c-border, radius: 6pt, inset: 8pt)[
    #text(fill: c-teal, weight: "bold", size: 9.2pt)[🔹 PHẦN II (2,0Đ), PHẦN III (2,0Đ) & PHẦN IV (3,0Đ)]
    #v(2pt)
    #set text(size: 8.3pt)
    - *Phần II – Câu 1 Đ/S (Tập hợp – 1,0đ):* *a) (NB)* kí hiệu $in, notin, subset, supset, emptyset$, khoảng/đoạn; *b) (TH)* trục số, tập con, bằng nhau; *c) (TH)* giao, hợp, phần bù; *d) (VD)* phép toán tập hợp nâng cao/chứa tham số $m$.
    - *Phần II – Câu 2 Đ/S (BPT bậc nhất 2 ẩn – 1,0đ):* *a) (NB)* kiểm tra cặp nghiệm/miền nghiệm; *b, c) (TH)* mô tả bờ và miền nghiệm trên $O x y$; *d) (VD)* lập BPT từ bài toán thực tế.
    - *Phần III – Câu 1 TLN (TH – 0,5đ):* Tìm số tập hợp con của một tập hợp.
    - *Phần III – Câu 2 TLN (VD – 0,5đ):* Bài toán thực tế phép toán tập hợp (biểu đồ Ven).
    - *Phần III – Câu 3 TLN (VD – 0,5đ):* Cho 1 GTLG, tính giá trị biểu thức lượng giác.
    - *Phần III – Câu 4 TLN (TH – 0,5đ):* Tính cạnh, góc, diện tích hoặc ứng dụng thực tế tam giác.
    - *Phần IV – Câu 1 TL (TH/MĐ2 – 1,0đ):* Thực hiện phép toán giao, hợp, hiệu, phần bù tập hợp.
    - *Phần IV – Câu 2 TL (VD/MĐ2 – 1,0đ):* Vận dụng hệ thức lượng tam giác giải toán thực tiễn.
    - *Phần IV – Câu 3 TL (VDC/MĐ3 – 1,0đ):* Lập hệ BPT bậc nhất hai ẩn, vẽ miền nghiệm & tìm phương án tối ưu thực tiễn.
  ]
)

== A.4. Chiến thuật phân bổ 90 phút vàng & Quy tắc tô phiếu Trả lời ngắn

#grid(
  columns: (1.15fr, 1fr),
  gutter: 8pt,
  block(width: 100%, fill: c-teal-bg, stroke: 0.8pt + c-teal-bd, radius: 6pt, inset: 8pt)[
    #text(fill: c-teal, weight: "bold", size: 9pt)[⏱ LỊCH TRÌNH PHÂN BỔ 90 PHÚT TỐI ƯU ĐIỂM SỐ]
    #v(2pt)
    #set text(size: 8.3pt)
    1. *Phút 01 – 15 (15 phút):* Giải quyết trọn vẹn *12 câu Phần I (3,0đ)*. Đọc kỹ từ khóa *“KHÔNG phải”*, *“SAI”*, gạch chân tập nguồn $NN, ZZ, RR$.
    2. *Phút 16 – 30 (15 phút):* Xử lý *2 câu Đúng/Sai Phần II (2,0đ)*. Chú ý: cố gắng chắc chắn đúng cả 4 ý vì nhảy từ 3 ý (*0,5đ*) lên 4 ý được gấp đôi (*1,0đ*)!
    3. *Phút 31 – 48 (18 phút):* Giải *4 câu Trả lời ngắn Phần III (2,0đ)*. Kiểm tra kỹ yêu cầu làm tròn (*hàng phần mười* hay *hàng phần trăm*).
    4. *Phút 49 – 82 (34 phút):* Trình bày sạch đẹp *3 câu Tự luận Phần IV (3,0đ)*: Câu 1 (8p) $arrow.r$ Câu 2 (11p) $arrow.r$ Câu 3 Quy hoạch tuyến tính (15p).
    5. *Phút 83 – 90 (08 phút):* Rà soát phiếu tô trắc nghiệm, kiểm tra đơn vị bài toán thực tế, ngoặc vuông `[ ]` / ngoặc tròn `( )` và điều kiện $x, y >= 0$.
  ],
  block(width: 100%, fill: c-purple-bg, stroke: 0.8pt + c-purple-bd, radius: 6pt, inset: 8pt)[
    #text(fill: c-purple, weight: "bold", size: 9pt)[📝 QUY TẮC ĐIỀN Ô TRẢ LỜI NGẮN (4 KÝ TỰ)]
    #v(2pt)
    #set text(size: 8.3pt)
    - Mỗi câu Trả lời ngắn trên phiếu có *4 cột ký tự* (gồm chữ số `0–9`, dấu trừ `-` ở cột đầu và dấu phẩy thập phân `,`), viết *từ trái sang phải* và bỏ trống các ô bên phải.
    - *Ví dụ chuẩn:*
      - Kết quả bằng `16` $arrow.r$ điền `1 | 6 |   |  `.
      - Kết quả bằng `-2,5` $arrow.r$ điền `- | 2 | , | 5`.
      - Kết quả phân số $7/4 = 1,75$ $arrow.r$ đổi ra số thập phân điền `1 | , | 7 | 5` (tuyệt đối không ghi dấu `/`).
    - Luôn đặt máy tính Casio ở chế độ *Độ (`DEG` — chữ `D` trên màn hình)* khi bấm $sin, cos, tan$ các góc $30^circle, 120^circle, ...$!
  ]
)

#pagebreak()

// ============================================================================
// PHẦN B.1 — TỜ CÔNG THỨC VÀNG 1 TRANG A4 (CHƯƠNG I -> CHƯƠNG IV)
// ============================================================================

= PHẦN B. TỜ CÔNG THỨC VÀNG & 12 KHẨU QUYẾT SIÊU TRÍ NHỚ

#block(
  width: 100%,
  fill: c-blue-bg,
  stroke: 0.9pt + c-primary,
  radius: 6pt,
  inset: (x: 10pt, y: 5pt),
)[
  #align(center)[#text(fill: c-blue-dark, weight: "extrabold", size: 9.6pt)[⚡ TỜ CÔNG THỨC VÀNG TOÁN 10 GIỮA HỌC KÌ I — TÓM GỌN TRỌN VẸN TRÊN 1 MẶT TRANG A4]]
]

#v(3pt)

#grid(
  columns: (1fr, 1fr),
  gutter: 7pt,

  // CỘT TRÁI
  [
    #block(width: 100%, stroke: 0.7pt + c-border, radius: 5pt, inset: 7pt, fill: white)[
      #text(fill: c-primary, weight: "bold", size: 9pt)[1. MỆNH ĐỀ & LƯỢNG TỪ (BÀI 1)]
      #v(2pt)
      #set text(size: 8.1pt)
      - *Mệnh đề phủ định $overline(P)$:* $P$ đúng $arrow.l.r.double overline(P)$ sai.
      - *Mệnh đề kéo theo $P arrow.r.double Q$:* *CHỈ SAI* khi $P$ đúng mà $Q$ sai ($1 arrow.r.double 0$).
        - $P$ là *điều kiện đủ* để có $Q$; $Q$ là *điều kiện cần* để có $P$.
      - *Mệnh đề đảo:* $Q arrow.r.double P$ ($P arrow.r.double Q$ đúng chưa chắc $Q arrow.r.double P$ đúng!).
      - *Tương đương $P arrow.l.r.double Q$:* Đúng khi cả $P arrow.r.double Q$ và $Q arrow.r.double P$ cùng đúng ($P, Q$ cùng đúng hoặc cùng sai) — *điều kiện cần và đủ*.
      - *Phủ định lượng từ $forall$ và $exists$:*
        $ overline(forall x in X comma P(x)) &equiv exists x in X comma overline(P(x)) \
          overline(exists x in X comma P(x)) &equiv forall x in X comma overline(P(x)) $
        *(Đổi đối ngẫu: $=$ thành $!=$ ; $>$ thành $<=$ ; $>=$ thành $<$)*.
    ]
    #v(4pt)
    #block(width: 100%, stroke: 0.7pt + c-border, radius: 5pt, inset: 7pt, fill: white)[
      #text(fill: c-primary, weight: "bold", size: 9pt)[2. TẬP HỢP & CÁC PHÉP TOÁN (BÀI 2 — 3,50 ĐIỂM)]
      #v(2pt)
      #set text(size: 8.1pt)
      - *Quan hệ tập số:* $NN^* subset NN subset ZZ subset QQ subset RR$. Quy ước: $emptyset subset A, forall A$.
      - *Số tập con của tập $A$ có $n$ phần tử:*
        - Tổng số tập con: *$2^n$* | Tập con khác $emptyset$: *$2^n - 1$*.
        - Tập con thực sự ($!= A$): *$2^n - 1$* | Tập con thực sự khác $emptyset$: *$2^n - 2$*.
        - Số tập $X$ thỏa $A subset X subset B$ (với $A subset B$): *$2^(n(B) - n(A))$*.
      - *Bốn phép toán cốt lõi:*
        - Giao: $A inter B = {x | x in A "và" x in B}$
        - Hợp: $A union B = {x | x in A "hoặc" x in B}$
        - Hiệu: $A without B = {x | x in A "và" x notin B}$
        - Phần bù (khi $B subset A$): $C_A B = A without B$; đặc biệt $C_RR A = RR without A$.
      - *Công thức đếm Biểu đồ Ven (Bao hàm – Loại trừ):*
        $ n(A union B) = n(A) + n(B) - n(A inter B) $
        $ n(A union B union C) &= n(A)+n(B)+n(C)-n(A inter B) \ &- n(B inter C)-n(C inter A)+n(A inter B inter C) $
    ]
    #v(4pt)
    #block(width: 100%, stroke: 0.7pt + c-border, radius: 5pt, inset: 7pt, fill: white)[
      #text(fill: c-primary, weight: "bold", size: 9pt)[3. BPT & HỆ BPT BẬC NHẤT HAI ẨN (BÀI 3 & 4 — 2,50 ĐIỂM)]
      #v(2pt)
      #set text(size: 8.1pt)
      - *Dạng chuẩn:* $a x + b y < c$ ($<=, >, >=$) với $a, b, c in RR$ và *$a^2 + b^2 != 0$*.
      - *Biểu diễn miền nghiệm:* Vẽ bờ $d: a x + b y = c$ (*nét liền* nếu $<=, >=$; *nét đứt* nếu $<, >$). Lấy điểm thử $M_0(x_0; y_0) notin d$ (ưu tiên $O(0;0)$ nếu $c != 0$) thay vào BPT: thỏa mãn thì giữ miền chứa $M_0$, sai thì gạch bỏ miền chứa $M_0$.
      - *Phương trình đoạn chắn đọc nhanh đồ thị:* Đường thẳng cắt $O x$ tại $(a; 0)$ và $O y$ tại $(0; b)$ ($a, b != 0$) có phương trình: *$x/a + y/b = 1$*.
      - *Định lí Cực trị Quy hoạch tuyến tính:* Biểu thức $F(x; y) = p x + q y$ trên miền đa giác nghiệm lồi luôn đạt *GTLN (max)* và *GTNN (min)* tại một trong *các đỉnh của đa giác* đó.
    ]
  ],

  // CỘT PHẢI
  [
    #block(width: 100%, stroke: 0.7pt + c-border, radius: 5pt, inset: 7pt, fill: white)[
      #text(fill: c-teal, weight: "bold", size: 9pt)[4. GIÁ TRỊ LƯỢNG GIÁC GÓC $0^circle arrow.r 180^circle$ (BÀI 5)]
      #v(2pt)
      #set text(size: 8.0pt)
      - *Trên nửa đường tròn đơn vị $M(x_0; y_0)$:* $sin alpha = y_0 in [0; 1]$; $cos alpha = x_0 in [-1; 1]$; $tan alpha = y_0 / x_0$ ($alpha != 90^circle$); $cot alpha = x_0 / y_0$ ($alpha notin {0^circle, 180^circle}$).
      - *Hai góc PHỤ nhau ($alpha + beta = 90^circle$):* $sin(90^circle - alpha) = cos alpha$; $cos(90^circle - alpha) = sin alpha$; $tan(90^circle - alpha) = cot alpha$; $cot(90^circle - alpha) = tan alpha$.
      - *Hai góc BÙ nhau ($alpha + beta = 180^circle$):* *$sin(180^circle - alpha) = sin alpha$*, còn *$cos(180^circle - alpha) = -cos alpha$*; *$tan(180^circle - alpha) = -tan alpha$*; *$cot(180^circle - alpha) = -cot alpha$*.
      - *Hệ thức cơ bản:* $sin^2 alpha + cos^2 alpha = 1$; $tan alpha dot cot alpha = 1$;
        $ 1 + tan^2 alpha = 1 / (cos^2 alpha) quad ; quad 1 + cot^2 alpha = 1 / (sin^2 alpha) $
      #v(2pt)
      #table(
        columns: (0.85fr, 0.7fr, 0.85fr, 0.85fr, 0.85fr, 0.75fr, 0.95fr, 0.95fr, 0.95fr, 0.8fr),
        align: center + horizon,
        stroke: 0.45pt + c-border,
        inset: (x: 1.5pt, y: 2.5pt),
        fill: (x, y) => if y == 0 { c-teal-bg } else { white },
        [$alpha$], [$0^circle$], [$30^circle$], [$45^circle$], [$60^circle$], [$90^circle$], [$120^circle$], [$135^circle$], [$150^circle$], [$180^circle$],
        [$sin$], [$0$], [$1/2$], [$sqrt(2)/2$], [$sqrt(3)/2$], [$1$], [$sqrt(3)/2$], [$sqrt(2)/2$], [$1/2$], [$0$],
        [$cos$], [$1$], [$sqrt(3)/2$], [$sqrt(2)/2$], [$1/2$], [$0$], [$-1/2$], [$-sqrt(2)/2$], [$-sqrt(3)/2$], [$-1$],
          [$tan$], [$0$], [$sqrt(3)/3$], [$1$], [$sqrt(3)$], [$||$], [$-sqrt(3)$], [$-1$], [$-sqrt(3)/3$], [$0$],
          [$cot$], [$||$], [$sqrt(3)$], [$1$], [$sqrt(3)/3$], [$0$], [$-sqrt(3)/3$], [$-1$], [$-sqrt(3)$], [$||$],
      )
    ]
    #v(4pt)
    #block(width: 100%, stroke: 0.7pt + c-border, radius: 5pt, inset: 7pt, fill: white)[
      #text(fill: c-teal, weight: "bold", size: 9pt)[5. HỆ THỨC LƯỢNG TRONG TAM GIÁC (BÀI 6 — 2,00 ĐIỂM)]
      #v(2pt)
      #set text(size: 8.1pt)
      - *Định lí Côsin:* $a^2 = b^2 + c^2 - 2 b c cos A arrow.r.double cos A = (b^2 + c^2 - a^2) / (2 b c)$.
        *(Tương tự cho $b^2, c^2$; góc $A$ nhọn $arrow.l.r.double b^2 + c^2 > a^2$; góc $A$ tù $arrow.l.r.double b^2 + c^2 < a^2$)*.
      - *Định lí Sin:* $a / (sin A) = b / (sin B) = c / (sin C) = 2 R$ ($R$: bán kính ngoại tiếp).
      - *5 Công thức diện tích $S$* (nửa chu vi $p = (a + b + c)/2$, $r$: bán kính nội tiếp):
        $ S = 1/2 a h_a = 1/2 b c sin A = (a b c) / (4 R) = p r = sqrt(p(p - a)(p - b)(p - c)) $
      - *Công thức suy ra cực nhanh:* $h_a = (2 S)/a$ ; $R = (a b c)/(4 S)$ ; $r = S/p$.
    ]
    #v(4pt)
    #block(width: 100%, stroke: 0.7pt + c-border, radius: 5pt, inset: 7pt, fill: white)[
      #text(fill: c-teal, weight: "bold", size: 9pt)[6. KHÁI NIỆM MỞ ĐẦU VỀ VECTƠ (BÀI 7 — 0,50 ĐIỂM)]
      #v(2pt)
      #set text(size: 8.1pt)
      - *Giá của $vt(A B)$* (với $A != B$): Đường thẳng $A B$. Độ dài: $|vt(A B)| = A B$.
      - *Cùng phương:* Giá song song hoặc trùng nhau ($A, B, C$ thẳng hàng $arrow.l.r.double vt(A B), vt(A C)$ cùng phương). Hai vectơ cùng phương chỉ có thể *cùng hướng* hoặc *ngược hướng*.
      - *Hai vectơ bằng nhau:* $vt(a) = vt(b) arrow.l.r.double cases(vt(a) comma vt(b) "cùng hướng", |vt(a)| = |vt(b)|)$.
      - *Quy ước vàng SGK KNTT:* Vectơ-không $vt(0) = vt(A A)$ có độ dài bằng $0$, *cùng phương và CÙNG HƯỚNG với mọi vectơ*.
    ]
  ]
)

#pagebreak()

// ============================================================================
// PHẦN B.2 — 12 KHẨU QUYẾT SIÊU TRÍ NHỚ (1 TRANG A4)
// ============================================================================

#block(
  width: 100%,
  fill: c-amber-bg,
  stroke: 0.9pt + c-amber,
  radius: 6pt,
  inset: (x: 10pt, y: 5.5pt),
)[
  #align(center)[#text(fill: c-amber, weight: "extrabold", size: 9.8pt)[🧠 12 KHẨU QUYẾT SIÊU TRÍ NHỚ — CHỐNG NHẦM DẤU & TRÁNH SẬP BẪY TRẮC NGHIỆM]]
]

#v(4pt)

#grid(
  columns: (1fr, 1fr),
  gutter: 7pt,
  row-gutter: 6.5pt,

  mnemonic-box("1. Kéo theo 1 → 0 mới Sai")[
    Mệnh đề $P arrow.r.double Q$ chỉ *SAI* duy nhất khi Giả thiết $P$ *Đúng* mà Kết luận $Q$ *Sai*. Nếu $P$ đã Sai thì $P arrow.r.double Q$ luôn Đúng!
  ],
  mnemonic-box("2. Sau ĐỦ là P — Sau CẦN là Q")[
    Trong định lí $P arrow.r.double Q$: Cụm từ đi ngay sau chữ *“điều kiện đủ”* chính là giả thiết $P$; đi ngay sau chữ *“điều kiện cần”* là kết luận $Q$.
  ],
  mnemonic-box("3. Phủ định Lượng từ: Đổi Ký hiệu + Đổi Dấu")[
    Lập mệnh đề phủ định phải làm *đủ 2 việc*: đổi $forall arrow.l.r exists$ *VÀ* phủ định mệnh đề phía sau ($=$ thành $!=$, $>$ thành $<=$, “chia hết” thành “không chia hết”).
  ],
  mnemonic-box("4. Phần bù đổi Ngoặc Vuông ↔ Tròn")[
    Khi tìm hiệu $A without B$ hoặc phần bù $C_RR A$, tại đầu mút biên: nếu tập bị trừ *có lấy* `[` thì kết quả *bỏ đi* `)` ; nếu tập bị trừ *không lấy* `(` thì kết quả *giữ lại* `]`!
  ],
  mnemonic-box("5. Bẫy Tập Con Rỗng khi tìm tham số m")[
    Cho $B = (m - 1; 2m + 3)$, muốn $B subset A$ thì phải xét *Trường hợp 1: $B = emptyset arrow.l.r.double m - 1 >= 2m + 3$* trước, trừ khi đề bài nói rõ “hai tập hợp *khác rỗng*”!
  ],
  mnemonic-box("6. Biểu đồ Ven: Điền từ LÕI GIAO ra ngoài")[
    Giải toán đếm thực tế luôn điền số phần tử của vùng *giao chung nhất* ($A inter B$ hoặc $A inter B inter C$) trước, sau đó trừ ngược ra để tìm phần “chỉ riêng”.
  ],
  mnemonic-box("7. Miền nghiệm BPT: Thử O(0;0) + Nhìn dấu Bằng")[
    Có dấu `=` ($<=, >=$) vẽ bờ *nét liền*; không có dấu `=` ($<, >$) vẽ bờ *nét đứt*. Nếu bờ không đi qua $O(0;0)$, thay $(0;0)$ vào: đúng thì giữ phía chứa $O$, sai thì gạch phía chứa $O$.
  ],
  mnemonic-box("8. Quy hoạch tuyến tính: Cực trị ở ĐỈNH")[
    Lợi nhuận lớn nhất hoặc chi phí nhỏ nhất của $F(x; y) = a x + b y$ luôn đạt tại một trong *các đỉnh của miền đa giác nghiệm*. Tìm đủ tọa độ đỉnh $arrow.r$ thay vào $F$ so sánh!
  ],
  mnemonic-box("9. Góc Tù (90° < α < 180°): Chỉ mình SIN dương!")[
    Với góc tù, tung độ $y_0 > 0$ nên *$sin alpha > 0$*, nhưng hoành độ $x_0 < 0$ nên *$cos alpha < 0, tan alpha < 0, cot alpha < 0$*. Tính $cos alpha = -sqrt(1 - sin^2 alpha)$ nhớ dấu trừ!
  ],
  mnemonic-box("10. Biết tan α: Chia cả tử và mẫu cho cosᵏ α")[
    Gặp phân thức bậc nhất $P = (a sin alpha + b cos alpha)/(c sin alpha + d cos alpha)$ khi biết $tan alpha$, chia cả tử và mẫu cho $cos alpha$ để đưa ngay về $(a tan alpha + b)/(c tan alpha + d)$. (Nếu bậc hai thì chia cho $cos^2 alpha$).
  ],
  mnemonic-box("11. Khi nào dùng Côsin — Khi nào dùng Sin?")[
    - Biết *3 cạnh* hoặc *2 cạnh + góc xen giữa* $arrow.r.double$ *Định lí Côsin*.
    - Biết *2 góc + 1 cạnh* hoặc tìm bán kính ngoại tiếp $R$ $arrow.r.double$ *Định lí Sin*.
  ],
  mnemonic-box("12. Hình bình hành ABCD: Đọc vòng tròn thứ tự đỉnh!")[
    Trong hình bình hành $A B C D$: *$vt(A B) = vt(D C)$* (không phải $vt(C D)$!) và *$vt(A D) = vt(B C)$*. Và nhớ kỹ: vectơ-không $vt(0)$ *cùng phương, cùng hướng* với mọi vectơ!
  ],
)

#pagebreak()
