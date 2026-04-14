---
id: bld_quality_gate_landing_page
kind: quality_gate
pillar: P07
builder: landing-page-builder
version: 1.0.0
quality: 9.1
title: "Quality Gate Landing Page"
author: n03_builder
tags: [landing_page, builder, examples]
tldr: "Golden and anti-examples for landing page construction, demonstrating ideal structure and common pitfalls."
domain: "landing page construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: GOVERN
---
# Quality Gate: Landing Page Builder

## HARD gates (must pass or artifact is rejected)
1. H01: Frontmatter has id, kind, title, version, created, quality:null, stack
2. H02: Output is syntactically valid HTML/JSX (no unclosed tags)
3. H03: At least 6 sections present (hero + 4 content + footer minimum)
4. H04: Primary CTA visible above the fold (first section)
5. H05: Responsive: no fixed widths > 100vw, uses relative/flex/grid
6. H06: All images have alt attributes
7. H07: DOCTYPE, html lang attribute, meta charset present (HTML output)

## SOFT gates (warnings, not blockers)
1. S01: All 12 sections present
2. S02: Dark mode classes/variables included
3. S03: Open Graph meta tags present
4. S04: JSON-LD structured data present
5. S05: Analytics data attributes on CTAs
6. S06: Lazy loading on below-fold images
7. S07: ARIA labels on interactive elements (accordion, menu, dialog)
8. S08: Google Fonts loaded with display=swap
9. S09: Color contrast >= 4.5:1 (WCAG AA)
10. S10: Print stylesheet or print-friendly structure

## Scoring Rubric
| Dimension | Weight | 10/10 means |
|-----------|--------|-------------|
| Completeness | 20% | All 12 sections, all meta, all analytics hooks |
| Visual Quality | 20% | Professional design, consistent spacing, polished |
| Responsiveness | 20% | Pixel-perfect on 375px, 768px, 1024px, 1440px |
| Performance | 15% | < 2s load, lazy images, critical CSS inline |
| Conversion | 15% | CTA above fold, clear value prop, urgency elements |
| Accessibility | 10% | WCAG AA, keyboard nav, screen reader friendly |

## Scoring Command

```bash
python _tools/cex_score.py --apply --verbose target.md
```

```bash
python _tools/cex_score.py --apply N0*/*.md
```
