---
id: p01_kc_pandoc_pipeline
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Pandoc Pipeline — Multi-Format Publishing for Content Factory"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: n04_knowledge
domain: pandoc
quality: 9.1
tags: [pandoc, ebook, pdf, epub, docx, markdown, content-factory, integration, INJECT]
tldr: "Universal document converter: Markdown → PDF/EPUB/DOCX with templates, metadata YAML, citations, cross-refs, and Lua filters"
when_to_use: "When any nucleus needs to publish long-form content in multiple formats — ebooks, reports, EPUB distribution"
keywords: [pandoc, epub, pdf, docx, markdown, ebook, multi-format, publishing]
feeds_kinds: [cli_tool, workflow, dag, formatter]
linked_artifacts: [kc_typst_patterns, kc_marp_cli]
density_score: null
related:
  - p04_fn_cf_ebook_compile
  - p04_fn_cf_pdf_generate
  - p05_fmt_content_adapter
  - p04_document_loader_NAME
  - p04_loader_pdf
  - n04_output_cf_integration_kcs
  - p01_kc_typst_patterns
  - p01_kc_document_loader
  - bld_examples_document_loader
  - spec_content_factory_v1
---

# Pandoc Pipeline

## Quick Reference
```yaml
install: winget install JohnMacFarlane.Pandoc  # or choco install pandoc
binary: pandoc
version_check: pandoc --version
input_formats: markdown, rst, org, docx, html, latex, json, csv (80+ total)
output_formats: pdf, epub, docx, html, pptx, latex, odt, rtf (60+ total)
pdf_engines: [xelatex, lualatex, tectonic, typst, weasyprint, wkhtmltopdf]
```

## Metadata YAML (front matter or separate file)

```yaml
# metadata.yaml
title: "Guia Completo de IA para Criadores"
subtitle: "Da Ideia ao Conteúdo Publicado"
author:
  - name: "Brand Name"
    affiliation: "Content Factory"
date: "Abril 2026"
lang: pt-BR
rights: "© 2026 Brand Name. Todos os direitos reservados."
description: "Um guia prático sobre IA generativa para criadores de conteúdo"
cover-image: assets/cover.png    # EPUB cover
css: assets/style.css            # EPUB/HTML stylesheet
toc: true                        # Table of contents
toc-depth: 3
number-sections: true
colorlinks: true
linkcolor: blue
geometry: margin=2.5cm           # PDF margins
fontsize: 11pt
mainfont: "Inter"                # XeLaTeX/LuaLaTeX font
monofont: "JetBrains Mono"
```

## Core Pipeline Commands

```bash
# Markdown → PDF (via LaTeX)
pandoc book.md -o book.pdf \
  --metadata-file=metadata.yaml \
  --pdf-engine=xelatex \
  --template=template.latex \
  --toc --toc-depth=3 \
  --number-sections \
  -V geometry:margin=2.5cm \
  -V fontsize=11pt \
  -V mainfont="Inter"

# Markdown → EPUB (for Kindle/Apple Books/Google Play)
pandoc book.md -o book.epub \
  --metadata-file=metadata.yaml \
  --epub-cover-image=assets/cover.png \
  --css=assets/epub.css \
  --toc --toc-depth=3 \
  --number-sections

# Markdown → DOCX (for editors/collaborators)
pandoc book.md -o book.docx \
  --metadata-file=metadata.yaml \
  --reference-doc=template.docx \
  --toc

# Markdown → HTML (for web/blog)
pandoc book.md -o book.html \
  --metadata-file=metadata.yaml \
  --standalone --self-contained \
  --css=assets/web.css \
  --toc

# Multi-file book (chapters as separate files)
pandoc ch01.md ch02.md ch03.md appendix.md -o book.pdf \
  --metadata-file=metadata.yaml \
  --pdf-engine=xelatex \
  --toc --number-sections

# Markdown → PDF via Typst (faster, no LaTeX needed)
pandoc book.md -o book.pdf \
  --pdf-engine=typst \
  --metadata-file=metadata.yaml
```

## Cross-References (with pandoc-crossref filter)

```bash
pip install pandoc-crossref  # or download binary

pandoc book.md -o book.pdf \
  --filter pandoc-crossref \
  --pdf-engine=xelatex \
  --citeproc
```

In markdown:
```markdown
See @fig:architecture for the system diagram.
As shown in @tbl:pricing, the cost is...
Equation @eq:roi calculates the return.

![System Architecture](arch.png){#fig:architecture}

| Plan | Cost |
|------|------|
| Free | $0   |

: Pricing comparison {#tbl:pricing}

$$ ROI = \frac{Revenue - Cost}{Cost} $$ {#eq:roi}
```

## Citations (with --citeproc)

```bash
pandoc book.md -o book.pdf \
  --citeproc \
  --bibliography=refs.bib \
  --csl=apa.csl
```

In markdown: `According to @smith2024, AI content creation...`

## Lua Filters (custom transformations)

```lua
-- wordcount.lua — count words in document
local words = 0
function Str(el) words = words + 1 end
function Pandoc(doc)
  doc.blocks:walk({ Str = Str })
  print(words .. " words")
  return doc
end
```

```bash
pandoc book.md --lua-filter=wordcount.lua -o /dev/null
```

## Full Ebook Pipeline (all formats at once)

```bash
#!/bin/bash
SRC="book.md"
META="metadata.yaml"
OUT="dist"
mkdir -p $OUT

# PDF (print-ready)
pandoc $SRC -o $OUT/book.pdf --metadata-file=$META \
  --pdf-engine=xelatex --toc --number-sections \
  --template=template.latex

# EPUB (digital distribution)
pandoc $SRC -o $OUT/book.epub --metadata-file=$META \
  --epub-cover-image=assets/cover.png --css=assets/epub.css \
  --toc --number-sections

# DOCX (editor review)
pandoc $SRC -o $OUT/book.docx --metadata-file=$META \
  --reference-doc=template.docx --toc

# HTML (web preview)
pandoc $SRC -o $OUT/book.html --metadata-file=$META \
  --standalone --self-contained --css=assets/web.css --toc

echo "Published: PDF + EPUB + DOCX + HTML"
```

## Gotchas

- **PDF requires a LaTeX engine (xelatex/lualatex) OR Typst.** Install TeX Live (~4GB) or use `--pdf-engine=typst` as a lighter alternative.
- **EPUB cover image must be a separate file**, not embedded in markdown. Recommended: 1600x2400px JPG.
- **`--self-contained` embeds all assets (images, CSS) into a single HTML file.** Great for sharing but can be huge. For EPUB, assets are bundled automatically.
- **`--reference-doc` for DOCX defines styles, not content.** Create a template.docx with custom heading styles, then Pandoc applies them.
- **Multi-file order matters.** `pandoc ch01.md ch02.md` processes in argument order. Use numbered filenames.
- **UTF-8 everywhere.** Pandoc assumes UTF-8 input. PT-BR characters (ã, ç, é) work fine if files are UTF-8.
- **Images in EPUB must be local files, not URLs.** Download external images before building EPUB.
- **`--toc` adds TOC at the beginning.** To control placement in LaTeX PDF, use `\tableofcontents` in template instead.

## Docs
- Manual: https://pandoc.org/MANUAL.html
- EPUB guide: https://pandoc.org/epub.html
- Lua filters: https://pandoc.org/lua-filters.html

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_fn_cf_ebook_compile]] | downstream | 0.41 |
| [[p04_fn_cf_pdf_generate]] | downstream | 0.32 |
| [[p05_fmt_content_adapter]] | downstream | 0.29 |
| [[p04_document_loader_NAME]] | downstream | 0.24 |
| [[p04_loader_pdf]] | downstream | 0.21 |
| [[n04_output_cf_integration_kcs]] | related | 0.20 |
| [[p01_kc_typst_patterns]] | sibling | 0.16 |
| [[p01_kc_document_loader]] | sibling | 0.16 |
| [[bld_examples_document_loader]] | downstream | 0.16 |
| [[spec_content_factory_v1]] | downstream | 0.15 |
