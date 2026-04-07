---
id: p03_constraint_cf_ebook
kind: constraint_spec
pillar: P03
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n01_intelligence"
name: "Content Factory eBook Format Constraints"
constraint_type: "format_rules"
pattern: "multi_rule_set"
quality: 9.1
tags: [constraint_spec, content-factory, ebook, publishing, pdf]
tldr: "eBook constraints: 5-15 chapters, 2K-5K words/chapter, TOC, ISBN-ready, PDF+EPUB+MOBI export"
description: "Governs all eBook outputs from dag_cf_ebook for publishing quality and multi-format compatibility"
provider_compat: "pandoc, calibre, canva"
fallback: "Manual editorial review if automated validation unavailable"
temperature_override: "0.5"
max_tokens: "2048"
density_score: 1.0
---

## Overview

Constrains all eBook artifacts produced by the Content Factory eBook pipeline (dag_cf_ebook). Ensures every published eBook meets professional publishing standards, is multi-format compatible, and maintains brand consistency. Applied at quality_check node before export.

## Constraint Definition

### Structure Rules
| Element | Min | Target | Max |
|---------|-----|--------|-----|
| chapters | 5 | 10 | 15 |
| words_per_chapter | 2000 | 3500 | 5000 |
| total_word_count | 10000 | 35000 | 75000 |
| illustrations_per_chapter | 1 | 2 | 5 |

### MUST Rules
- eBook MUST include: title page, table of contents, introduction, conclusion
- Each chapter MUST have: title, opening hook, body sections, chapter summary
- TOC MUST be hyperlinked in PDF and EPUB formats
- Cover MUST follow brand palette with title, subtitle, author, brand logo
- All body text MUST use brand-approved typography (font, size, line spacing)
- Page numbers MUST appear on all body pages (not title/TOC)
- Export MUST produce all 3 formats: PDF, EPUB, MOBI

### MUST NOT Rules
- MUST NOT have chapters shorter than 2000 words
- MUST NOT use more than 3 heading levels (H1=chapter, H2=section, H3=subsection)
- MUST NOT include orphan pages (< 3 lines on final page of chapter)
- MUST NOT embed fonts that lack distribution license

### Typography
| Element | Spec |
|---------|------|
| body_font | Brand serif or sans-serif (from brand_config) |
| heading_font | Brand display font |
| body_size | 11-12pt (PDF), reflowable (EPUB) |
| line_spacing | 1.4-1.6x |
| margins | 2.5cm top/bottom, 2cm left/right (PDF) |

### Export Formats
| Format | Engine | Spec |
|--------|--------|------|
| PDF | Pandoc/LaTeX or Canva | A4 or 6x9in, embedded fonts, hyperlinked TOC |
| EPUB | Pandoc/Calibre | EPUB3, reflowable, metadata complete |
| MOBI | Calibre | Kindle-compatible, cover thumbnail |

### Quality Metrics
| Metric | Min | Target | Max |
|--------|-----|--------|-----|
| flesch_readability | 40 | 60 | 80 |
| chapters_with_illustrations | 60% | 80% | 100% |
| metadata_completeness | 90% | 100% | 100% |

## Provider Compatibility

| Provider | Support | Method |
|----------|---------|--------|
| Pandoc | native | Markdown → PDF/EPUB/MOBI with templates |
| Calibre | native | Format conversion + metadata editing |
| Canva | partial | Cover design + PDF layout (no EPUB) |
| LaTeX | native | Professional typesetting for PDF |

## Integration

- Consumed by: dag_cf_ebook (quality_check node)
- Validates outputs from: assemble_ebook node
- Cross-references: brand_config.yaml (fonts, palette, logo)
- Feeds: quality_gate node in dag_cf_master for final approval
