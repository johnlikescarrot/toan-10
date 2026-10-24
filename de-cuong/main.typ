#import "style.typ": *

#set document(
  title: "Đề cương ôn tập Toán 10 – Giữa học kì I – 2026–2027",
  author: "Tài liệu ôn tập biên soạn từ ma trận được cung cấp",
  keywords: ("Toán 10", "Kết nối tri thức", "Giữa học kì I", "Mệnh đề", "Tập hợp", "Bất phương trình", "Hệ thức lượng", "Vectơ"),
)

#set page(
  paper: "a4",
  margin: (left: 17mm, right: 17mm, top: 20mm, bottom: 18mm),
  header: context {
    let p = counter(page).get().first()
    if p > 1 [
      #text(size: 8pt, fill: muted)[TOÁN 10 · GIỮA HỌC KÌ I · 2026–2027]
      #h(1fr)
      #text(size: 8pt, fill: muted)[KẾT NỐI TRI THỨC]
      #v(2pt)
      #std.line(length: 100%, stroke: 0.5pt + line)
    ]
  },
  footer: context {
    let p = counter(page).get().first()
    let total = counter(page).final().first()
    if p > 1 [
      #std.line(length: 100%, stroke: 0.5pt + line)
      #v(2pt)
      #align(center)[#text(size: 8pt, fill: muted)[Trang #p / #total]]
    ]
  },
)

#set text(font: "DejaVu Sans", size: 10.3pt, lang: "vi", fill: ink)
#set par(justify: true, leading: 0.65em, spacing: 0.70em)
#set heading(numbering: none)
#set table(stroke: 0.55pt + line, inset: 5pt)
#show table.cell: set par(justify: false)
#set enum(indent: 5mm, body-indent: 2mm)
#set list(indent: 5mm, body-indent: 2mm)
#show link: set text(fill: blue)
#show heading.where(level: 1): it => {
  pagebreak(weak: true)
  block(
    width: 100%,
    fill: navy,
    inset: (x: 12pt, y: 10pt),
    radius: 5pt,
    below: 14pt,
  )[#text(fill: white, size: 17pt, weight: "bold")[#it.body]]
}
#show heading.where(level: 2): it => block(above: 13pt, below: 7pt)[
  #text(fill: navy, size: 13pt, weight: "bold")[#it.body]
  #v(2pt)
  #std.line(length: 100%, stroke: 1pt + blue)
]
#show heading.where(level: 3): it => block(above: 10pt, below: 5pt)[
  #text(fill: teal, size: 11pt, weight: "bold")[#it.body]
]
#show outline.entry.where(level: 1): set text(weight: "bold", fill: navy)

// ───────────────────────────── Cover ─────────────────────────────
#align(center)[
  #v(12mm)
  #tag("TÀI LIỆU ÔN TẬP · BÁM SÁT MA TRẬN", fill: teal)
  #v(13mm)
  #text(fill: navy, size: 28pt, weight: "bold")[ĐỀ CƯƠNG ÔN TẬP\ TOÁN 10]
  #v(5mm)
  #text(fill: blue, size: 20pt, weight: "bold")[GIỮA HỌC KÌ I]
  #v(4mm)
  #text(fill: muted, size: 13pt)[Kết nối tri thức với cuộc sống · Năm học 2026–2027]
  #v(9mm)
  #std.line(length: 62%, stroke: 2pt + blue)
  #v(7mm)
  #text(size: 11pt)[Theo ma trận Trường THPT Hà Huy Tập\ Thời gian làm bài quy định: *90 phút*]
  #v(10mm)
  #grid(
    columns: (1fr, 1fr, 1fr, 1fr),
    column-gutter: 7pt,
    block(fill: pale-blue, inset: 8pt, radius: 5pt)[#text(size: 18pt, weight: "bold", fill: blue)[04]\ #text(size: 8.5pt)[chuyên đề]],
    block(fill: pale-teal, inset: 8pt, radius: 5pt)[#text(size: 18pt, weight: "bold", fill: teal)[21]\ #text(size: 8.5pt)[câu đề ôn]],
    block(fill: pale-orange, inset: 8pt, radius: 5pt)[#text(size: 18pt, weight: "bold", fill: orange)[08]\ #text(size: 8.5pt)[ý đúng–sai]],
    block(fill: pale-gray, inset: 8pt, radius: 5pt)[#text(size: 18pt, weight: "bold", fill: navy)[100%]\ #text(size: 8.5pt)[có đáp án]],
  )
  #v(12mm)
  #block(fill: pale-gray, inset: 10pt, radius: 5pt, width: 88%)[
    #text(size: 9.5pt, fill: muted)[
      Lý thuyết dễ tiếp cận · Ví dụ từng bước · Bài luyện có đáp án\
      Đề ôn đúng cấu trúc · Lời giải chi tiết · Bảng đối chiếu không bỏ sót
    ]
  ]
  #v(1fr)
  #text(size: 9pt, fill: muted)[Phiên bản biên soạn ngày 24/10/2026\ Đề ôn trong tài liệu *không phải nguyên văn đề thi chính thức*]
]

// ───────────────────────────── Front matter ─────────────────────────────
= Hướng dẫn sử dụng và phạm vi tài liệu

#source-note("LƯU Ý QUAN TRỌNG VỀ TỆP NGUỒN", [
  Tệp *“MA TRẬN TOÁN 10 - GIỮA KÌ I.docx”* được cung cấp chỉ chứa *mục tiêu, hình thức kiểm tra, ma trận và bảng đặc tả*. Tệp không chứa đề thi hoàn chỉnh và không chứa đáp án chính thức. Vì vậy, không thể trích nguyên văn các câu hỏi và đáp án của đề thi từ riêng tệp này.

  Để hoàn thành tài liệu mà không làm mất phạm vi kiểm tra, đề cương này:
  + Ghi lại đầy đủ yêu cầu của từng đơn vị kiến thức và lập bảng đối chiếu *mọi vị trí câu hỏi* trong bảng đặc tả.
  + Biên soạn mới *một đề ôn 21 câu* có đúng dạng, số lượng, mức độ và nội dung tương ứng; mọi câu đều có đáp án hoặc lời giải.
  + Không gắn nhãn đề ôn là “đề chính thức” hoặc “nguyên văn đề thi”. Nếu có thêm tệp đề thi chính thức, cần đối chiếu và bổ sung nguyên văn riêng.
])

== 1. Cấu trúc kiểm tra được phân tích từ tệp nguồn

#table(
  columns: (1.45fr, 1fr, 1.15fr, 1.9fr),
  table.header(
    [#th[Phần]], [#th[Số lượng]], [#th[Điểm]], [#th[Cách tính]],
  ),
  [Trắc nghiệm chọn phương án], [12 câu], [3,0], [0,25 điểm/câu],
  [Trắc nghiệm đúng–sai], [2 câu · 8 ý], [2,0], [Mỗi câu 1 điểm; đúng 1 ý: 0,1; 2 ý: 0,25; 3 ý: 0,5; 4 ý: 1,0],
  [Trắc nghiệm trả lời ngắn], [4 câu], [2,0], [0,5 điểm/câu],
  [Tự luận], [3 câu], [3,0], [1,0 điểm/câu],
  [#text(weight: "bold")[Tổng]], [#text(weight: "bold")[21 câu chính]], [#text(weight: "bold")[10,0]], [#text(weight: "bold")[90 phút]],
)

#note("VÌ SAO MA TRẬN GHI 24 CÂU TRẮC NGHIỆM?", [
  Cách đếm trong ma trận là $12$ câu chọn phương án $+$ $8$ ý đúng–sai $+$ $4$ câu trả lời ngắn $=$ $24$. Đây không phải 24 câu chính. Khi làm bài, học sinh nhận 21 câu chính, trong đó hai câu đúng–sai có bốn ý mỗi câu.
])

== 2. Trọng số theo chương và vị trí trong SGK

#table(
  columns: (0.65fr, 2.5fr, 1.9fr, 0.7fr),
  table.header(
    [#th[Chương]], [#th[Nội dung đến giữa kì]], [#th[Bài trong Kết nối tri thức]], [#th[Điểm]],
  ),
  [I], [Mệnh đề và tập hợp], [Bài 1–2], [4,0],
  [II], [Bất phương trình và hệ bất phương trình bậc nhất hai ẩn], [Bài 3–4], [2,5],
  [III], [Hệ thức lượng trong tam giác], [Bài 5–6], [3,0],
  [IV], [Vectơ: các khái niệm mở đầu], [Bài 7], [0,5],
  [], [#text(weight: "bold")[Tổng]], [], [#text(weight: "bold")[10,0]],
)

#warning("PHẠM VI CẦN HỌC — KHÔNG HỌC THỪA HOẶC HỌC THIẾU", [
  Chương IV trong ma trận chỉ kiểm tra *khái niệm vectơ, độ dài, giá, cùng phương, cùng/ngược hướng, bằng nhau và vectơ-không*. Các phép toán cộng, trừ vectơ, nhân vectơ với một số, tọa độ và tích vô hướng không nằm trong bảng đặc tả này.
])

== 3. Lộ trình ba vòng để học chắc

#table(
  columns: (0.75fr, 1.15fr, 3.4fr),
  table.header([#th[Vòng]], [#th[Thời lượng gợi ý]], [#th[Việc cần làm]]),
  [1 · Nắm ý], [4–6 giờ], [Đọc phần “Cốt lõi”, thuộc công thức, tự nói lại điều kiện áp dụng. Che lời giải và làm lại từng ví dụ.],
  [2 · Thuần thục], [3–4 giờ], [Làm bài luyện nhanh, đánh dấu lỗi theo bốn nhóm: sai kiến thức, sai dấu, sai tính toán, thiếu trình bày.],
  [3 · Mô phỏng], [90 phút + 45 phút], [Làm đề ôn đúng giờ, không xem tài liệu. Chấm theo đáp án, ghi lại từng lỗi và làm lại sau 24 giờ.],
)

=== Kế hoạch 7 ngày (có thể điều chỉnh)

#table(
  columns: (0.6fr, 2.6fr, 2.3fr),
  table.header([#th[Ngày]], [#th[Nhiệm vụ chính]], [#th[Kết quả cần đạt]]),
  [1], [Mệnh đề; hai cách mô tả tập hợp; kí hiệu khoảng–đoạn], [Làm được Câu 1–3, ĐS 1a–b],
  [2], [Giao, hợp, hiệu, phần bù; số tập con; bài toán Ven], [Làm được Câu 4, TLN 1–2, TL 1],
  [3], [BPT và hệ BPT bậc nhất hai ẩn; vẽ miền nghiệm], [Làm được Câu 5–6, ĐS 2],
  [4], [Bài toán tối ưu; giá trị lượng giác $0°$–$180°$], [Làm được TL 3, Câu 7–8, TLN 3],
  [5], [Định lí côsin, sin; diện tích; giải tam giác], [Làm được Câu 9–10, TLN 4, TL 2],
  [6], [Khái niệm vectơ; tổng ôn công thức; sửa lỗi cũ], [Làm được Câu 11–12; hoàn thiện phiếu lỗi],
  [7], [Làm đề ôn 90 phút; chấm và làm lại câu sai], [Có điểm mô phỏng và kế hoạch khắc phục],
)

== 4. Phiếu tự kiểm trước khi làm đề

Đánh dấu *[x]* chỉ khi em có thể tự làm, không nhìn ví dụ:

#grid(columns: (1fr, 1fr), column-gutter: 10pt, row-gutter: 5pt,
  [[ ] Nhận biết mệnh đề, mệnh đề chứa biến.],
  [[ ] Phủ định đúng mệnh đề có $forall$ hoặc $exists$.],
  [[ ] Đọc đúng $in, subset, emptyset$ và các khoảng–đoạn.],
  [[ ] Tính giao, hợp, hiệu, phần bù và số tập con.],
  [[ ] Vẽ đường bờ, thử điểm, kết luận miền nghiệm.],
  [[ ] Tìm đỉnh miền đa giác và xét giá trị $F=m x+n y$.],
  [[ ] Nhớ dấu của $cos alpha$ khi $alpha$ nhọn hoặc tù.],
  [[ ] Chọn đúng định lí côsin/sin/công thức diện tích.],
  [[ ] Giải bài toán khoảng cách bằng hệ thức lượng.],
  [[ ] Phân biệt cùng phương, cùng hướng và bằng nhau.],
)

#remember("NGUYÊN TẮC LÀM BÀI 90 PHÚT", [
  *35 phút* cho 12 câu chọn phương án · *15 phút* cho đúng–sai · *15 phút* cho trả lời ngắn · *20 phút* cho tự luận · *5 phút* kiểm tra. Nếu một câu làm quá 4 phút mà chưa có hướng, đánh dấu và chuyển câu; không bỏ qua bước kiểm tra đơn vị, dấu và điều kiện xác định.
])

// The outline is placed after the practical instructions so the source note is visible.
#heading(level: 1)[Mục lục]
#outline(title: none, depth: 2, indent: auto)

#include "01-ly-thuyet.typ"
#include "02-de-on.typ"
#include "03-dap-an.typ"
#include "04-doi-chieu.typ"
