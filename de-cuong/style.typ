// Shared visual language for the review guide. No external Typst packages.

#let navy = rgb("#16324F")
#let blue = rgb("#2F6FED")
#let teal = rgb("#0E7490")
#let orange = rgb("#C55A11")
#let red = rgb("#A73535")
#let green = rgb("#236B4E")
#let ink = rgb("#1F2937")
#let muted = rgb("#526277")
#let line = rgb("#CBD5E1")
#let pale-blue = rgb("#EDF3FF")
#let pale-teal = rgb("#EAF8F6")
#let pale-orange = rgb("#FFF5E9")
#let pale-red = rgb("#FFF0F0")
#let pale-gray = rgb("#F5F7FA")

#let tag(body, fill: blue) = box(
  fill: fill,
  inset: (x: 5pt, y: 2pt),
  radius: 3pt,
)[#text(fill: white, size: 8pt, weight: "bold")[#body]]

#let callout(title, body, accent: blue, background: pale-blue, breakable: false) = block(
  width: 100%,
  fill: background,
  stroke: (left: 3pt + accent),
  inset: (x: 10pt, y: 8pt),
  radius: (right: 5pt),
  breakable: breakable,
  above: 6pt,
  below: 6pt,
)[
  #text(fill: accent, weight: "bold")[#title]
  #v(2pt)
  #body
]

#let note(title, body) = callout(title, body, accent: blue, background: pale-blue)
#let remember(title, body) = callout(title, body, accent: teal, background: pale-teal)
#let warning(title, body) = callout(title, body, accent: orange, background: pale-orange)
#let source-note(title, body) = callout(title, body, accent: red, background: pale-red, breakable: true)

#let example(title, statement, solution) = block(
  width: 100%,
  stroke: 0.8pt + line,
  inset: 10pt,
  radius: 5pt,
  breakable: true,
  above: 6pt,
  below: 6pt,
)[
  #text(fill: blue, weight: "bold")[#title]
  #v(3pt)
  #statement
  #v(5pt)
  #std.line(length: 100%, stroke: 0.6pt + line)
  #v(4pt)
  #text(fill: green, weight: "bold")[LỜI GIẢI]
  #v(2pt)
  #solution
]

#let drill(label, body) = block(
  width: 100%,
  breakable: false,
  above: 4pt,
  below: 4pt,
)[
  #grid(columns: (12mm, 1fr), column-gutter: 4pt,
    [#tag(label, fill: teal)],
    [#body],
  )
]

#let exam-question(label, body, level: none) = block(
  width: 100%,
  breakable: false,
  above: 8pt,
  below: 5pt,
)[
  #grid(columns: (15mm, 1fr), column-gutter: 5pt,
    [#tag(label, fill: navy)],
    [
      #if level != none [#tag(level, fill: muted) #h(3pt)]
      #body
    ],
  )
]

#let solution-heading(label, title) = block(
  width: 100%,
  fill: pale-gray,
  stroke: (left: 3pt + navy),
  inset: (x: 8pt, y: 6pt),
  breakable: false,
  above: 10pt,
  below: 6pt,
)[#text(fill: navy, weight: "bold")[#label · #title]]

#let two-options(a, b, c, d) = grid(
  columns: (1fr, 1fr),
  rows: (auto, auto),
  column-gutter: 12pt,
  row-gutter: 5pt,
  [
    #set par(justify: false)
    A. #a
  ],
  [
    #set par(justify: false)
    B. #b
  ],
  [
    #set par(justify: false)
    C. #c
  ],
  [
    #set par(justify: false)
    D. #d
  ],
)

#let four-options(a, b, c, d) = grid(
  columns: (1fr, 1fr, 1fr, 1fr),
  column-gutter: 8pt,
  [
    #set par(justify: false)
    A. #a
  ],
  [
    #set par(justify: false)
    B. #b
  ],
  [
    #set par(justify: false)
    C. #c
  ],
  [
    #set par(justify: false)
    D. #d
  ],
)

#let th(body) = table.cell(fill: pale-blue)[
  #text(fill: navy, weight: "bold", size: 8.5pt)[#body]
]

#let figure-local(path, width, caption) = align(center)[
  #block(breakable: false, above: 6pt, below: 6pt)[
    #image(path, width: width)
    #v(2pt)
    #text(size: 8.5pt, fill: muted)[#caption]
  ]
]

#let answer-strip(body) = block(
  width: 100%,
  fill: pale-teal,
  inset: 7pt,
  radius: 4pt,
  breakable: true,
)[#text(fill: green)[#body]]
