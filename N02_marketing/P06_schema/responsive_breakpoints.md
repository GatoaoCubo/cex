---
id: p06_schema_responsive_breakpoints
kind: input_schema
pillar: P06
title: "Responsive Breakpoints Contract"
version: 1.0.0
created: 2026-04-01
author: n02_visual_frontend
domain: frontend
quality: 9.1
tags: [schema, responsive, breakpoints, tailwind, mobile-first]
tldr: "Mobile-first breakpoint contract — Tailwind defaults, fluid typography, grid rules."
density_score: 0.91
related:
  - n02_kc_responsive_layout_systems
  - n06_output_pricing_page
  - p01_kc_responsive_layouts
  - kc_visual_hierarchy_principles
  - spec_n02_part2
  - n02_kc_typography_web
  - p10_dtc_design_token_contract
  - p01_kc_typography_web
  - p06_schema_a11y_checklist
---

# Responsive Breakpoints Contract

## Schema Purpose
Enforces consistent responsive behavior across all N02 HTML output.
Mobile-first: base styles = mobile, breakpoints add complexity upward.

---

## Breakpoint Definitions (Tailwind Defaults)

```yaml
breakpoints:
  base:  { min: 0,    max: 639,  label: "mobile",     columns: 1 }
  sm:    { min: 640,  max: 767,  label: "small",      columns: 1 }
  md:    { min: 768,  max: 1023, label: "tablet",     columns: 2 }
  lg:    { min: 1024, max: 1279, label: "desktop",    columns: 3 }
  xl:    { min: 1280, max: 1535, label: "wide",       columns: 4 }
  2xl:   { min: 1536, max: null, label: "ultrawide",  columns: 4 }
```

## Layout Rules

| Rule | Specification | Enforced |
|------|---------------|----------|
| Max content width | `max-w-7xl` (1280px) | yes |
| Container padding | `px-4` mobile, `px-6` md+, `px-8` lg+ | yes |
| Grid columns | 1→2→3→4 per breakpoint table | yes |
| Sidebar | hidden mobile, drawer md, fixed lg+ | yes |
| Navigation | hamburger mobile, horizontal lg+ | yes |
| Hero image | full-width mobile, 50/50 lg+ | recommended |

## Fluid Typography

```css
/* Body text */
font-size: clamp(1rem, 2.5vw, 1.25rem);      /* 16px → 20px */

/* H1 */
font-size: clamp(1.5rem, 4vw, 3rem);          /* 24px → 48px */

/* H2 */
font-size: clamp(1.25rem, 3vw, 2.25rem);      /* 20px → 36px */

/* H3 */
font-size: clamp(1.125rem, 2.5vw, 1.5rem);    /* 18px → 24px */
```

## Touch Targets

```yaml
touch_targets:
  minimum_size: "48px × 48px"
  minimum_spacing: "8px between targets"
  applies_to: ["buttons", "links", "form inputs", "nav items"]
  breakpoint_scope: "base through md (touch devices)"
```

## Spacing Scale (4px base)

```yaml
spacing:
  0: "0px"
  1: "4px"     # 0.25rem
  2: "8px"     # 0.5rem
  3: "12px"    # 0.75rem
  4: "16px"    # 1rem
  5: "20px"    # 1.25rem
  6: "24px"    # 1.5rem
  8: "32px"    # 2rem
  10: "40px"   # 2.5rem
  12: "48px"   # 3rem
  16: "64px"   # 4rem
  20: "80px"   # 5rem
  24: "96px"   # 6rem
```

## Responsive Images

```yaml
images:
  strategy: "srcset + sizes"
  formats: ["webp", "avif", "jpg fallback"]
  lazy_loading: "loading='lazy' for below-fold"
  aspect_ratio: "aspect-ratio CSS property, no CLS"
  max_width: "100% on mobile, constrained on desktop"
```

## Validation

```yaml
validation:
  must_render_clean:
    - 320px   # smallest mobile
    - 375px   # iPhone SE
    - 768px   # iPad portrait
    - 1024px  # iPad landscape / small laptop
    - 1280px  # standard desktop
    - 1536px  # wide monitor
  no_horizontal_scroll: true
  no_overlapping_elements: true
  no_text_truncation: true
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n02_kc_responsive_layout_systems]] | upstream | 0.70 |
| [[n06_output_pricing_page]] | upstream | 0.45 |
| [[p01_kc_responsive_layouts]] | upstream | 0.44 |
| [[kc_visual_hierarchy_principles]] | upstream | 0.39 |
| [[spec_n02_part2]] | related | 0.28 |
| [[n02_kc_typography_web]] | upstream | 0.27 |
| [[p10_dtc_design_token_contract]] | sibling | 0.22 |
| [[p01_kc_typography_web]] | upstream | 0.19 |
| [[p06_schema_a11y_checklist]] | sibling | 0.16 |
