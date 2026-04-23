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
related:
  - bld_examples_landing_page
  - p10_hos_html_output_visual_frontend
  - landing_page_petshop_crm
  - bld_system_prompt_landing_page
  - bld_instruction_landing_page
  - p05_output_visual_report
  - landing-page-builder
  - p09_lpt_landing_page_template
  - p03_pt_visual_frontend_marketing
  - p01_kc_tailwind_patterns
---

## Quality Gate

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

## Examples

# Examples: Landing Page Builder

## Example 1: SaaS Product (HTML + Tailwind)

**Input**: "Create a landing page for CodeForge, an AI testing tool for developers"

**Output sketch** (abbreviated — real output is complete HTML):
```html
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CodeForge — Tests First. Code Fearless.</title>
  <meta name="description" content="AI that writes tests before you write code. Ship faster with confidence.">
  <meta property="og:title" content="CodeForge — Tests First. Code Fearless.">
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body class="bg-white dark:bg-gray-950 text-gray-900 dark:text-gray-100">
  <!-- HERO -->
  <section id="hero" aria-label="Hero" class="min-h-screen flex items-center">
    <div class="max-w-7xl mx-auto px-4 text-center">
      <h1 class="text-5xl md:text-7xl font-bold">Tests First. Code Fearless.</h1>
      <p class="mt-6 text-xl text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">
        AI that writes your tests before you write code. Ship 3x faster with full coverage.
      </p>
      <a href="#pricing" data-track="hero-cta"
         class="mt-8 inline-block px-8 py-4 bg-blue-600 text-white rounded-lg text-lg font-semibold hover:bg-blue-700 transition">
        Start Free Trial
      </a>
    </div>
  </section>
  <!-- ... 11 more sections ... -->
</body>
</html>
```

## Example 2: Infoproduct/Curso (PT-BR)

**Input**: "Create landing page for AI automation course, R$497, 8 modules"

**Section order** (infoproduct template):
HERO (transformation) > PROBLEMA (dor do manual) > TRANSFORMACAO (antes/depois) >
MODULOS (8 cards) > DEPOIMENTOS > GARANTIA (7 dias) > PRICING (R$497 ou 12x) >
FAQ > CTA FINAL > FOOTER

## Anti-Example
```html
<!-- BAD: Not a landing page, just a wireframe -->
<div>
  <h1>Title here</h1>
  <p>Description here</p>
  <button>CTA</button>
</div>
<!-- Missing: responsive, dark mode, SEO, a11y, sections, styling, EVERYTHING -->
```

## Exemplar Requirements

1. Score 9.0+ to qualify as few-shot reference
2. Demonstrate ideal structure for this artifact kind
3. Populate all frontmatter fields with realistic values
4. Use domain-specific content not generic placeholders
5. Enable retrieval via tags and TF-IDF matching

## Properties

| Property | Value |
|----------|-------|
| Kind | `examples` |
| Pillar | P01 |
| Domain | landing page construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
