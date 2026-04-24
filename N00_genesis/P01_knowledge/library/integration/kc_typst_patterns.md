---
id: p01_kc_typst_patterns
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Typst Patterns — PDF Generation for Content Factory"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: n04_knowledge
domain: typst
quality: 9.0
tags: [typst, pdf, ebook, report, typesetting, content-factory, integration, INJECT]
tldr: "Modern markup → professional PDF with templates, functions, data loading, and programmatic layout — the LaTeX replacement"
when_to_use: "When any nucleus needs to generate professional PDFs — ebooks, reports, whitepapers, certificates"
keywords: [typst, pdf, typesetting, ebook, report, template, programmatic-layout]
feeds_kinds: [cli_tool, workflow, dag, formatter]
linked_artifacts: [kc_pandoc_pipeline, kc_marp_cli]
density_score: null
related:
  - p04_fn_cf_pdf_generate
  - p05_output_visual_report
  - p05_fmt_content_adapter
  - bld_examples_landing_page
  - p04_document_loader_NAME
  - n02_kc_typography_web
  - p04_fn_cf_ebook_compile
  - bld_examples_document_loader
---

# Typst Patterns

## Quick Reference
```yaml
install: winget install Typst.Typst   # or cargo install typst-cli
binary: typst
version_check: typst --version
compile: typst compile input.typ output.pdf
watch: typst watch input.typ output.pdf  # auto-recompile on save
file_extension: .typ
output: PDF (native), PNG, SVG
```

## Document Structure

```typst
// document metadata
#set document(title: "Guia Completo de IA", author: "Brand Name", date: auto)

// page setup
#set page(
  paper: "a4",
  margin: (top: 2.5cm, bottom: 2.5cm, left: 3cm, right: 2.5cm),
  header: align(right)[_Content Factory — v1.0_],
  footer: context [
    #align(center)[#counter(page).display("1 / 1", both: true)]
  ],
  numbering: "1",
)

// typography
#set text(font: "Inter", size: 11pt, lang: "pt")
#set par(justify: true, leading: 0.65em)
#set heading(numbering: "1.1")

// title page
#align(center + horizon)[
  #text(size: 28pt, weight: "bold", fill: rgb("#2563eb"))[Guia Completo de IA]
  #v(1em)
  #text(size: 14pt, fill: gray)[Para Criadores de Conteúdo]
  #v(2em)
  #text(size: 12pt)[Brand Name — 2026]
]

#pagebreak()

// table of contents
#outline(indent: auto, depth: 3)

#pagebreak()

= Introdução

Este guia apresenta as melhores práticas...

== Conceitos Fundamentais

Texto do capítulo aqui.

=== Subseção

Mais detalhes...
```

## Headings and Formatting

```typst
= Heading 1 (chapter)
== Heading 2 (section)
=== Heading 3 (subsection)

*bold text*
_italic text_
`inline code`
#link("https://example.com")[link text]
#highlight[highlighted text]
#strike[strikethrough]
#underline[underlined]

- Bullet list item
- Another item
  - Nested item

+ Numbered list
+ Second item

/ Term: Definition list item
```

## Functions and Variables

```typst
// Define reusable function
#let tip(body) = block(
  fill: rgb("#f0f9ff"),
  stroke: rgb("#2563eb"),
  inset: 12pt,
  radius: 4pt,
  width: 100%,
)[
  #text(weight: "bold", fill: rgb("#2563eb"))[💡 Dica: ]
  #body
]

// Use it
#tip[Sempre valide seus dados antes de publicar.]

// Variables
#let brand_color = rgb("#2563eb")
#let version = "1.0.0"

O sistema está na versão #version.
```

## Data Loading (from external files)

```typst
// Load YAML data
#let config = yaml("brand_config.yaml")
Marca: #config.brand_name

// Load CSV data → table
#let data = csv("metrics.csv")
#table(
  columns: 4,
  ..data.flatten()
)

// Load JSON
#let tools = json("tools.json")
#for tool in tools.items [
  - *#tool.name*: #tool.description
]

// Load and embed image
#figure(
  image("chart.png", width: 80%),
  caption: [Crescimento mensal de receita]
)
```

## Template Pattern (reusable across documents)

```typst
// template.typ — shared template
#let ebook(title: "", author: "", date: "", body) = {
  set document(title: title, author: author)
  set page(paper: "a4", margin: 2.5cm)
  set text(font: "Inter", size: 11pt, lang: "pt")
  set heading(numbering: "1.1")
  set par(justify: true)

  // Title page
  align(center + horizon)[
    #text(size: 28pt, weight: "bold")[#title]
    #v(1em)
    #text(size: 14pt)[#author — #date]
  ]
  pagebreak()
  outline(indent: auto)
  pagebreak()

  body
}

// chapter.typ — use the template
#import "template.typ": ebook

#show: ebook.with(
  title: "Guia de Produtividade",
  author: "Brand Name",
  date: "Abril 2026",
)

= Primeiro Capítulo
Conteúdo aqui...
```

## Tables

```typst
#table(
  columns: (1fr, 2fr, auto),
  align: (left, left, center),
  stroke: 0.5pt + gray,
  inset: 8pt,
  fill: (x, y) => if y == 0 { rgb("#2563eb").lighten(80%) },
  [*Ferramenta*], [*Descrição*], [*Custo*],
  [Canva], [Design de imagens e posts], [Free],
  [ElevenLabs], [Narração por IA], [\$22/mês],
  [Runway], [Geração de vídeo], [\$28/mês],
)
```

## CLI Commands

```bash
# Compile to PDF
typst compile ebook.typ ebook.pdf

# Watch mode (auto-recompile)
typst watch ebook.typ ebook.pdf

# Specify font paths
typst compile --font-path ./fonts/ ebook.typ ebook.pdf

# Compile to PNG (one per page)
typst compile ebook.typ page_{n}.png

# Compile specific pages
typst compile --pages 1-5 ebook.typ preview.pdf

# List available fonts
typst fonts
```

## Gotchas

- **Typst is NOT Markdown.** Headings use `=` not `#`. Bold is `*text*` not `**text**`. Italic is `_text_` not `*text*`.
- **`#` is the function/code prefix in Typst.** `#text()`, `#set`, `#let`, `#for` — everything programmatic starts with `#`.
- **No native EPUB output.** Typst outputs PDF, PNG, SVG only. For EPUB, use Pandoc.
- **Custom fonts must be installed or `--font-path` specified.** Typst does not download fonts from the internet.
- **`context` keyword required for counter/state access in headers/footers.** Without it, counters show nothing.
- **Images paths are relative to the `.typ` file**, not the working directory. Use absolute paths in automated pipelines.
- **Large documents (500+ pages) compile in seconds** — Typst is incremental. LaTeX equivalent would take minutes.
- **PT-BR hyphenation works automatically** with `#set text(lang: "pt")`. Don't skip the lang setting.

## Docs
- Reference: https://typst.app/docs/reference/
- Tutorial: https://typst.app/docs/tutorial/
- Packages: https://typst.app/universe/ (community templates)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_fn_cf_pdf_generate]] | downstream | 0.36 |
| [[p05_output_visual_report]] | downstream | 0.18 |
| [[p05_fmt_content_adapter]] | downstream | 0.17 |
| [[bld_examples_landing_page]] | related | 0.17 |
| [[p04_document_loader_NAME]] | downstream | 0.17 |
| [[n02_kc_typography_web]] | sibling | 0.16 |
| [[p04_fn_cf_ebook_compile]] | downstream | 0.15 |
| [[bld_examples_document_loader]] | downstream | 0.15 |
