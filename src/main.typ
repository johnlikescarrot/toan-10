#import "template.typ": *

#set document(
  title: "Đề Cương Ôn Tập Giữa Học Kì I Môn Toán 10 (Năm học 2026–2027) — Kết nối tri thức",
  author: "Biên soạn bám sát 100% Ma trận & Đặc tả THPT Hà Huy Tập (Tổ Toán – Tin)",
)

#set page(
  paper: "a4",
  margin: (top: 19mm, bottom: 17mm, left: 15mm, right: 15mm),
  header: context {
    if counter(page).get().first() > 1 [
      #set text(size: 7.7pt, fill: c-slate)
      #grid(
        columns: (1fr, auto),
        align: (left + bottom, right + bottom),
        [*ĐỀ CƯƠNG ÔN TẬP GIỮA KÌ I TOÁN 10 (2026–2027)*],
        [_SGK Kết nối tri thức với cuộc sống • Chuẩn Ma trận THPT Hà Huy Tập (90 phút)_]
      )
      #v(-3.5pt)
      #line(length: 100%, stroke: 0.5pt + c-border)
    ]
  },
  footer: context {
    set text(size: 7.8pt, fill: c-slate)
    line(length: 100%, stroke: 0.5pt + c-border)
    v(2.5pt)
    grid(
      columns: (1fr, auto),
      align: (left, right),
      [Tài liệu ôn tập toàn diện Chương I $arrow.r$ Chương IV (Bài 1 $arrow.r$ Bài 7) & Bộ Đề + Đáp án KTGK I 2026–2027],
      [*Trang #counter(page).display("1 / 1", both: true)*]
    )
  },
)

#set text(
  font: "Be Vietnam Pro",
  lang: "vi",
  size: 9.5pt,
  fill: c-navy,
)

#set par(
  leading: 0.56em,
  justify: true,
)

#show heading.where(level: 1): it => {
  block(
    width: 100%,
    fill: c-navy,
    radius: 7pt,
    inset: (x: 12pt, y: 8pt),
    above: 8pt,
    below: 6pt,
    breakable: false,
    sticky: true,
  )[
    #text(fill: rgb("#FACC15"), weight: "extrabold", size: 12pt)[#it.body]
  ]
}

#show heading.where(level: 2): it => {
  block(
    width: 100%,
    stroke: (left: 4pt + c-primary, bottom: 0.6pt + c-blue-bd),
    fill: c-blue-bg,
    inset: (left: 9pt, right: 8pt, y: 5pt),
    radius: (right: 4pt),
    above: 8pt,
    below: 5pt,
    breakable: false,
    sticky: true,
  )[
    #text(fill: c-navy, weight: "bold", size: 10.6pt)[#it.body]
  ]
}

#show heading.where(level: 3): it => {
  block(
    above: 6.5pt,
    below: 3.5pt,
    breakable: false,
    sticky: true,
  )[
    #text(fill: c-teal, weight: "bold", size: 9.9pt)[▸ #it.body]
  ]
}

#include "part1_matrix_cheatsheet.typ"
#include "part2_theory_kntt.typ"
#include "part3_question_bank.typ"
#include "part4_exams_2026_2027.typ"
