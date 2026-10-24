// ============================================================================
// TEMPLATE & DESIGN SYSTEM — ĐỀ CƯƠNG ÔN TẬP KTGK I TOÁN 10 (2026–2027)
// Bộ sách: Kết nối tri thức với cuộc sống | Trường THPT Hà Huy Tập
// ============================================================================

#let c-navy      = rgb("#0F172A")
#let c-primary   = rgb("#1D4ED8")
#let c-blue-dark = rgb("#1E3A8A")
#let c-blue-bg   = rgb("#EFF6FF")
#let c-blue-bd   = rgb("#93C5FD")
#let c-teal      = rgb("#0F766E")
#let c-teal-bg   = rgb("#F0FDFA")
#let c-teal-bd   = rgb("#5EEAD4")
#let c-amber     = rgb("#B45309")
#let c-amber-bg  = rgb("#FFFBEB")
#let c-amber-bd  = rgb("#FCD34D")
#let c-red       = rgb("#B91C1C")
#let c-red-bg    = rgb("#FEF2F2")
#let c-red-bd    = rgb("#FCA5A5")
#let c-purple    = rgb("#6D28D9")
#let c-purple-bg = rgb("#F5F3FF")
#let c-purple-bd = rgb("#C4B5FD")
#let c-green     = rgb("#15803D")
#let c-green-bg  = rgb("#F0FDF4")
#let c-slate     = rgb("#475569")
#let c-border    = rgb("#CBD5E1")
#let c-zebra     = rgb("#F8FAFC")

// Math helpers chuẩn kí hiệu SGK Toán 10 Kết nối tri thức
#let vt(x) = $arrow(#x)$
#let goc(x) = $accent(#x, hat)$
#let notin = sym.in.not

#let badge(label, bg: c-blue-bg, fg: c-primary, bd: c-blue-bd) = box(
  fill: bg,
  stroke: 0.6pt + bd,
  radius: 3pt,
  inset: (x: 5pt, y: 1.8pt),
  baseline: 15%,
)[#text(size: 7.8pt, weight: "bold", fill: fg)[#label]]

#let lv-badge(lv) = {
  if lv == "NB" {
    badge("Nhận biết", bg: rgb("#ECFDF5"), fg: rgb("#047857"), bd: rgb("#6EE7B7"))
  } else if lv == "TH" {
    badge("Thông hiểu", bg: c-blue-bg, fg: c-primary, bd: c-blue-bd)
  } else if lv == "VD" {
    badge("Vận dụng", bg: c-amber-bg, fg: c-amber, bd: c-amber-bd)
  } else {
    badge("Vận dụng cao", bg: c-red-bg, fg: c-red, bd: c-red-bd)
  }
}

#let part-banner(code, title, subtitle) = {
  block(
    width: 100%,
    fill: c-navy,
    radius: 8pt,
    inset: (x: 15pt, y: 10pt),
    above: 6pt,
    below: 8pt,
    breakable: false,
    sticky: true,
  )[
    #text(fill: rgb("#60A5FA"), weight: "bold", size: 9pt, tracking: 0.8pt)[#upper(code)]
    #v(2.5pt)
    #text(fill: white, weight: "extrabold", size: 14.2pt)[#title]
    #if subtitle != "" [
      #v(2.5pt)
      #text(fill: rgb("#CBD5E1"), size: 9pt)[#subtitle]
    ]
  ]
}

#let chapter-banner(chap-code, title, sgk-lessons, weight-text) = {
  block(
    width: 100%,
    fill: c-blue-dark,
    radius: 6pt,
    inset: (x: 12pt, y: 8pt),
    above: 10pt,
    below: 6pt,
    breakable: false,
    sticky: true,
  )[
    #grid(
      columns: (1fr, auto),
      align: (left + horizon, right + horizon),
      gutter: 8pt,
      [
        #text(fill: rgb("#93C5FD"), size: 8.3pt, weight: "bold")[#upper(chap-code) — #sgk-lessons]\
        #text(fill: white, size: 11.8pt, weight: "extrabold")[#title]
      ],
      box(
        fill: rgb("#FACC15"),
        radius: 4pt,
        inset: (x: 8pt, y: 4pt),
      )[
        #text(fill: c-navy, size: 8.5pt, weight: "extrabold")[#weight-text]
      ]
    )
  ]
}

#let theory-card(title, body) = {
  block(
    width: 100%,
    fill: white,
    stroke: 0.8pt + c-border,
    radius: 6pt,
    inset: (x: 10pt, y: 7.5pt),
    above: 5pt,
    below: 5pt,
    breakable: true,
  )[
    #text(fill: c-primary, weight: "bold", size: 9.8pt)[◆ #title]
    #v(2.5pt)
    #body
  ]
}

#let method-box(title, body) = {
  block(
    width: 100%,
    fill: c-teal-bg,
    stroke: (left: 3.5pt + c-teal, top: 0.6pt + c-teal-bd, right: 0.6pt + c-teal-bd, bottom: 0.6pt + c-teal-bd),
    radius: (right: 5pt),
    inset: (x: 10pt, y: 7pt),
    above: 5pt,
    below: 5pt,
    breakable: false,
  )[
    #text(fill: c-teal, weight: "bold", size: 9.5pt)[⚙ PHƯƠNG PHÁP GIẢI NHANH — #title]
    #v(2.5pt)
    #body
  ]
}

#let mnemonic-box(title, body) = {
  block(
    width: 100%,
    fill: c-amber-bg,
    stroke: 0.9pt + c-amber-bd,
    radius: 6pt,
    inset: (x: 10pt, y: 7pt),
    above: 5pt,
    below: 5pt,
    breakable: false,
  )[
    #text(fill: c-amber, weight: "bold", size: 9.5pt)[★ MẸO SIÊU TRÍ NHỚ — #title]
    #v(2.5pt)
    #body
  ]
}

#let trap-box(title, body) = {
  block(
    width: 100%,
    fill: c-red-bg,
    stroke: 0.9pt + c-red-bd,
    radius: 6pt,
    inset: (x: 10pt, y: 7pt),
    above: 5pt,
    below: 5pt,
    breakable: false,
  )[
    #text(fill: c-red, weight: "bold", size: 9.5pt)[⚠ CẢNH BÁO BẪY HAY SAI — #title]
    #v(2.5pt)
    #body
  ]
}

// Question formatting components
#let mcq(num, lv, stem, a, b, c, d, cols: 2) = {
  block(
    width: 100%,
    above: 5.5pt,
    below: 5.5pt,
    breakable: false,
  )[
    *Câu #num.* #if lv != "" [#lv-badge(lv) ] #stem
    #v(2.5pt)
    #if cols == 4 {
      grid(
        columns: (1fr, 1fr, 1fr, 1fr),
        row-gutter: 3.5pt,
        column-gutter: 6pt,
        [*A.* #a], [*B.* #b], [*C.* #c], [*D.* #d],
      )
    } else if cols == 1 {
      grid(
        columns: (1fr,),
        row-gutter: 3pt,
        [*A.* #a], [*B.* #b], [*C.* #c], [*D.* #d],
      )
    } else {
      grid(
        columns: (1fr, 1fr),
        row-gutter: 3.5pt,
        column-gutter: 10pt,
        [*A.* #a], [*B.* #b], [*C.* #c], [*D.* #d],
      )
    }
  ]
}

#let tf-question(label, stem, a, b, c, d) = {
  block(
    width: 100%,
    fill: c-zebra,
    stroke: 0.7pt + c-border,
    radius: 6pt,
    inset: (x: 10pt, y: 7pt),
    above: 5.5pt,
    below: 5.5pt,
    breakable: false,
  )[
    *#label* #stem
    #v(3pt)
    #table(
      columns: (24pt, 1fr, 58pt),
      align: (center + horizon, left + horizon, center + horizon),
      stroke: 0.5pt + c-border,
      inset: (x: 5pt, y: 4.5pt),
      fill: (x, y) => if y == 0 { c-blue-bg } else { white },
      [*Ý*], [*Mệnh đề phát biểu*], [*Đ / S*],
      [*a)*], [#a], [☐ Đ #h(3pt) ☐ S],
      [*b)*], [#b], [☐ Đ #h(3pt) ☐ S],
      [*c)*], [#c], [☐ Đ #h(3pt) ☐ S],
      [*d)*], [#d], [☐ Đ #h(3pt) ☐ S],
    )
  ]
}

#let sa-box-preview() = box(baseline: 20%)[
  #grid(
    columns: (13pt, 13pt, 13pt, 13pt),
    stroke: 0.6pt + c-slate,
    inset: 2.5pt,
    align: center,
    [\u{00A0}], [\u{00A0}], [\u{00A0}], [\u{00A0}]
  )
]

#let sa-question(label, lv, stem) = {
  block(
    width: 100%,
    above: 5pt,
    below: 5pt,
    breakable: false,
  )[
    *#label* #if lv != "" [#lv-badge(lv) ] #stem #h(6pt) #h(1fr) #box[#text(size: 8.5pt, fill: c-slate)[*Đáp số:* ]#sa-box-preview()]
  ]
}

#let exam-paper-header(exam-title, code, subtitle) = {
  block(
    width: 100%,
    stroke: 1.2pt + c-navy,
    fill: c-zebra,
    radius: 6pt,
    inset: (x: 12pt, y: 9pt),
    above: 6pt,
    below: 8pt,
    breakable: false,
  )[
    #grid(
      columns: (1fr, 1.25fr),
      align: (center + horizon, center + horizon),
      gutter: 8pt,
      [
        #text(size: 9pt, weight: "bold")[TRƯỜNG THPT HÀ HUY TẬP]\
        #text(size: 8.8pt, weight: "semibold")[TỔ TOÁN – TIN]\
        #line(length: 45%, stroke: 0.7pt + c-navy)
        #v(2pt)
        #box(stroke: 0.7pt + c-primary, fill: c-blue-bg, radius: 3pt, inset: (x: 7pt, y: 2pt))[
          #text(size: 8.5pt, weight: "bold", fill: c-primary)[Mã đề: #code]
        ]
      ],
      [
        #text(size: 9.8pt, weight: "extrabold", fill: c-navy)[ĐỀ KIỂM TRA GIỮA HỌC KÌ I — NĂM HỌC 2026–2027]\
        #text(size: 9.5pt, weight: "bold", fill: c-primary)[MÔN: TOÁN – LỚP 10 (CHƯƠNG TRÌNH KẾT NỐI TRI THỨC)]\
        #text(size: 8.6pt, style: "italic", fill: c-slate)[Thời gian làm bài: 90 phút (không kể thời gian phát đề)]
      ]
    )
    #v(4pt)
    #line(length: 100%, stroke: 0.5pt + c-border)
    #v(3pt)
    #align(center)[#text(size: 9.5pt, weight: "extrabold", fill: c-red)[#exam-title] #text(size: 8.6pt, fill: c-slate)[— #subtitle]]
  ]
}
