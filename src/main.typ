#import "template.typ": *

#set document(
  title: "Đề Cương Ôn Tập Giữa Học Kì I Môn Toán 10 (Năm học 2026–2027)",
  author: "Trường THPT Hà Huy Tập — Tổ Toán-Tin (Bộ sách Kết nối tri thức với cuộc sống)",
)

#set page(
  paper: "a4",
  margin: (top: 20mm, bottom: 18mm, left: 16mm, right: 16mm),
  header: context {
    if counter(page).get().first() > 1 [
      #set text(size: 8pt, fill: c-slate)
      #grid(
        columns: (1fr, auto),
        align: (left + bottom, right + bottom),
        [*ĐỀ CƯƠNG ÔN TẬP KTGK I — TOÁN 10 (2026–2027) — THPT HÀ HUY TẬP*],
        [_Chuẩn Ma trận Đặc tả 70% TN + 30% TL (90 phút)_]
      )
      #v(-4pt)
      #line(length: 100%, stroke: 0.5pt + c-border)
    ]
  },
  footer: context {
    set text(size: 8pt, fill: c-slate)
    line(length: 100%, stroke: 0.5pt + c-border)
    v(3pt)
    grid(
      columns: (1fr, auto),
      align: (left, right),
      [Bộ sách _Kết nối tri thức với cuộc sống_ — Ôn tập toàn diện Chương I $arrow.r$ Chương IV (Bài 1 $arrow.r$ Bài 7)],
      [*Trang #counter(page).display("1 / 1", both: true)*]
    )
  },
)

#set text(
  font: "Be Vietnam Pro",
  lang: "vi",
  size: 9.8pt,
  fill: c-navy,
)

#set par(
  leading: 0.58em,
  justify: true,
)

#show heading.where(level: 1): it => {
  block(
    width: 100%,
    fill: c-navy,
    radius: 7pt,
    inset: (x: 13pt, y: 9pt),
    above: 6pt,
    below: 6pt,
    breakable: false,
    sticky: true,
  )[
    #text(fill: rgb("#FACC15"), weight: "extrabold", size: 12.5pt)[#it.body]
  ]
}

#show heading.where(level: 2): it => {
  block(
    width: 100%,
    stroke: (left: 4pt + c-primary, bottom: 0.6pt + c-blue-bd),
    fill: c-blue-bg,
    inset: (left: 10pt, right: 8pt, y: 5.5pt),
    radius: (right: 4pt),
    above: 8pt,
    below: 5pt,
    breakable: false,
    sticky: true,
  )[
    #text(fill: c-navy, weight: "bold", size: 11pt)[#it.body]
  ]
}

#show heading.where(level: 3): it => {
  block(
    above: 7pt,
    below: 4pt,
    breakable: false,
    sticky: true,
  )[
    #text(fill: c-teal, weight: "bold", size: 10.2pt)[▸ #it.body]
  ]
}

#include "part1_overview_cheatsheet.typ"
#include "part2_theory_lessons.typ"
#include "part3_question_bank.typ"
#include "part4_mock_exams.typ"
