---
id: bld_quality_gate_landing_page
kind: quality_gate
pillar: P07
builder: landing-page-builder
version: 1.0.0
---
# Quality Gate: Landing Page Builder

## HARD gates (must pass or artifact is rejected)
- H01: Frontmatter has id, kind, title, version, created, quality:null, stack
- H02: Output is syntactically valid HTML/JSX (no unclosed tags)
- H03: At least 6 sections present (hero + 4 content + footer minimum)
- H04: Primary CTA visible above the fold (first section)
- H05: Responsive: no fixed widths > 100vw, uses relative/flex/grid
- H06: All images have alt attributes
- H07: DOCTYPE, html lang attribute, meta charset present (HTML output)

## SOFT gates (warnings, not blockers)
- S01: All 12 sections present
- S02: Dark mode classes/variables included
- S03: Open Graph meta tags present
- S04: JSON-LD structured data present
- S05: Analytics data attributes on CTAs
- S06: Lazy loading on below-fold images
- S07: ARIA labels on interactive elements (accordion, menu, dialog)
- S08: Google Fonts loaded with display=swap
- S09: Color contrast >= 4.5:1 (WCAG AA)
- S10: Print stylesheet or print-friendly structure

## Scoring Rubric
| Dimension | Weight | 10/10 means |
|-----------|--------|-------------|
| Completeness | 20% | All 12 sections, all meta, all analytics hooks |
| Visual Quality | 20% | Professional design, consistent spacing, polished |
| Responsiveness | 20% | Pixel-perfect on 375px, 768px, 1024px, 1440px |
| Performance | 15% | < 2s load, lazy images, critical CSS inline |
| Conversion | 15% | CTA above fold, clear value prop, urgency elements |
| Accessibility | 10% | WCAG AA, keyboard nav, screen reader friendly |
