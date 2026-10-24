// ============================================================================
// TEMPLATE & DESIGN SYSTEM — ĐỀ CƯƠNG ÔN TẬP KTGK I TOÁN 10 (2026–2027)
// ============================================================================

#let c-navy     = rgb("#0F172A")
#let c-primary  = rgb("#1D4ED8")
#let c-blue-bg  = rgb("#EFF6FF")
#let c-blue-bd  = rgb("#93C5FD")
#let c-teal     = rgb("#0F766E")
#let c-teal-bg  = rgb("#F0FDFA")
#let c-teal-bd  = rgb("#5EEAD4")
#let c-amber    = rgb("#B45309")
#let c-amber-bg = rgb("#FFFBEB")
#let c-amber-bd = rgb("#FCD34D")
#let c-red      = rgb("#B91C1C")
#let c-red-bg   = rgb("#FEF2F2")
#let c-red-bd   = rgb("#FCA5A5")
#let c-purple   = rgb("#6D28D9")
#let c-purple-bg= rgb("#F5F3FF")
#let c-slate    = rgb("#475569")
#let c-border   = rgb("#CBD5E1")
#let c-zebra    = rgb("#F8FAFC")

#let part-banner(code, title, subtitle) = {
  block(
    width: 100%,
    fill: c-navy,
    radius: 8pt,
    inset: (x: 16pt, y: 11pt),
    above: 6pt,
    below: 8pt,
    breakable: false,
    sticky: true,
  )[
    #text(fill: rgb("#60A5FA"), weight: "bold", size: 9.5pt, tracking: 0.8pt)[#upper(code)]
    #v(3pt)
    #text(fill: white, weight: "extrabold", size: 15pt)[#title]
    #if subtitle != "" [
      #v(3pt)
      #text(fill: rgb("#CBD5E1"), size: 9.2pt)[#subtitle]
    ]
  ]
}

#let section-heading(title) = {
  block(
    width: 100%,
    stroke: (left: 4pt + c-primary),
    fill: c-blue-bg,
    inset: (left: 10pt, right: 10pt, y: 6pt),
    radius: (right: 5pt),
    above: 9pt,
    below: 5pt,
    breakable: false,
    sticky: true,
  )[
    #text(fill: c-navy, weight: "bold", size: 11.2pt)[#title]
  ]
}

#let lesson-header(num, title, matrix-info, weight-note) = {
  block(
    width: 100%,
    fill: rgb("#1E3A8A"),
    radius: 6pt,
    inset: (x: 12pt, y: 8pt),
    above: 11pt,
    below: 6pt,
    breakable: false,
    sticky: true,
  )[
    #grid(
      columns: (1fr, auto),
      align: (left + horizon, right + horizon),
      [
        #text(fill: rgb("#93C5FD"), size: 8.5pt, weight: "bold")[CHỦ ĐỀ #num — #matrix-info]\
        #text(fill: white, size: 12pt, weight: "bold")[#title]
      ],
      box(
        fill: rgb("#FACC15"),
        radius: 4pt,
        inset: (x: 8pt, y: 4pt),
      )[
        #text(fill: c-navy, size: 8.5pt, weight: "extrabold")[#weight-note]
      ]
    )
  ]
}

#let mnemonic-box(title, body) = {
  block(
    width: 100%,
    fill: c-amber-bg,
    stroke: 1pt + c-amber-bd,
    radius: 6pt,
    inset: (x: 11pt, y: 8pt),
    breakable: false,
  )[
    #text(fill: c-amber, weight: "bold", size: 9.5pt)[★ MẸO SIÊU TRÍ NHỚ — #title]
    #v(3pt)
    #set text(size: 9.3pt, fill: c-navy)
    #body
  ]
}

#let trap-box(title, body) = {
  block(
    width: 100%,
    fill: c-red-bg,
    stroke: 1pt + c-red-bd,
    radius: 6pt,
    inset: (x: 11pt, y: 8pt),
    breakable: false,
  )[
    #text(fill: c-red, weight: "bold", size: 9.5pt)[⚠ CẢNH BÁO BẪY HAY SAI — #title]
    #v(3pt)
    #set text(size: 9.3pt, fill: c-navy)
    #body
  ]
}

#let formula-box(title, body) = {
  block(
    width: 100%,
    fill: c-teal-bg,
    stroke: 1pt + c-teal-bd,
    radius: 6pt,
    inset: (x: 11pt, y: 8pt),
    breakable: false,
  )[
    #text(fill: c-teal, weight: "bold", size: 9.5pt)[◆ CÔNG THỨC CỐT LÕI — #title]
    #v(3pt)
    #set text(size: 9.4pt, fill: c-navy)
    #body
  ]
}

#let badge(label, bg: c-blue-bg, fg: c-primary) = {
  box(
    fill: bg,
    radius: 3pt,
    inset: (x: 5pt, y: 1.5pt),
    baseline: 15%,
  )[#text(fill: fg, weight: "bold", size: 8pt)[#label]]
}

#let nb-tag = badge("NB", bg: rgb("#DBEAFE"), fg: rgb("#1E40AF"))
#let th-tag = badge("TH", bg: rgb("#DCFCE7"), fg: rgb("#166534"))
#let vd-tag = badge("VD", bg: rgb("#FEF3C7"), fg: rgb("#92400E"))
#let vdc-tag = badge("VDC", bg: rgb("#FEE2E2"), fg: rgb("#991B1B"))

#let mcq(num, tag, stem, a, b, c, d, cols: 2) = {
  block(width: 100%, breakable: false, above: 5.5pt, below: 5.5pt)[
    #text(weight: "bold", fill: c-primary)[Câu #num.] #tag #stem
    #v(2pt)
    #if cols == 4 [
      #grid(
        columns: (1fr, 1fr, 1fr, 1fr),
        column-gutter: 8pt,
        row-gutter: 4pt,
        [*A.* #a], [*B.* #b], [*C.* #c], [*D.* #d]
      )
    ] else if cols == 2 [
      #grid(
        columns: (1fr, 1fr),
        column-gutter: 12pt,
        row-gutter: 4pt,
        [*A.* #a], [*B.* #b],
        [*C.* #c], [*D.* #d]
      )
    ] else [
      #stack(
        spacing: 3.5pt,
        [*A.* #a],
        [*B.* #b],
        [*C.* #c],
        [*D.* #d]
      )
    ]
  ]
}

#let tf-question(num, meta, stem, visual, a-txt, b-txt, c-txt, d-txt) = {
  block(width: 100%, above: 7pt, below: 7pt, breakable: false)[
    #text(weight: "bold", fill: c-primary)[Câu #num] #badge(meta, bg: c-purple-bg, fg: c-purple)*:* #stem
    #if visual != none [
      #v(4pt)
      #align(center)[#visual]
    ]
    #v(4pt)
    #table(
      columns: (28pt, 1fr, 44pt, 44pt),
      align: (center + horizon, left + horizon, center + horizon, center + horizon),
      stroke: 0.6pt + c-border,
      fill: (x, y) => if y == 0 { rgb("#F1F5F9") } else { white },
      inset: (x: 6pt, y: 4.5pt),
      [*Ý*], [*Mệnh đề nhận định*], [*Đúng*], [*Sai*],
      [*a)*], [#a-txt], [], [],
      [*b)*], [#b-txt], [], [],
      [*c)*], [#c-txt], [], [],
      [*d)*], [#d-txt], [], [],
    )
  ]
}

#let solution-card(title, body) = {
  block(
    width: 100%,
    fill: rgb("#F8FAFC"),
    stroke: (left: 3pt + c-teal, top: 0.5pt + c-border, right: 0.5pt + c-border, bottom: 0.5pt + c-border),
    radius: (right: 5pt),
    inset: (x: 10pt, y: 7pt),
    above: 6pt,
    below: 6pt,
  )[
    #text(weight: "bold", fill: c-teal, size: 9.5pt)[✓ #title]
    #v(3pt)
    #set text(size: 9.2pt)
    #body
  ]
}
