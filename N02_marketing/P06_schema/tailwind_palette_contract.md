---
id: p06_schema_tailwind_palette
kind: input_schema
8f: F1_constrain
pillar: P06
title: "Tailwind Palette Contract"
version: 1.0.0
created: 2026-04-01
author: n02_visual_frontend
domain: frontend
quality: 9.1
tags: [schema, tailwind, palette, design-system, color]
tldr: "Restricted palette contract — 60-30-10 rule, zero hardcoded hex, CODEXA tokens."
density_score: 0.93
related:
  - p05_output_dashboard_ui
  - p10_dtc_design_token_contract
  - n02_kc_color_theory_applied
  - spec_n02_part2
  - p05_output_style_guide
  - p01_kc_color_theory_applied
  - spec_n02_visual_frontend_engineer
  - p09_lpt_landing_page_template
  - p10_hos_html_output_visual_frontend
  - n06_output_visual_identity
---

# Tailwind Palette Contract

## Schema Purpose
Restricts all N02 output to design-system-approved colors only.
Zero hardcoded hex values in component classes. All colors via CSS custom properties.

---

## Allowed Color Tokens

### Primitives (Layer 1)

```css
:root {
  --background:    0 0% 100%;        /* white */
  --foreground:    240 10% 3.9%;     /* near-black */
  --primary:       240 5.9% 10%;
  --secondary:     240 4.8% 95.9%;
  --muted:         240 4.8% 95.9%;
  --accent:        240 4.8% 95.9%;
  --destructive:   0 84.2% 60.2%;
  --border:        240 5.9% 90%;
  --radius:        0.5rem;
}

.dark {
  --background:    240 10% 3.9%;     /* near-black */
  --foreground:    0 0% 98%;         /* near-white */
  --primary:       0 0% 98%;
  --secondary:     240 3.7% 15.9%;
  --muted:         240 3.7% 15.9%;
  --accent:        240 3.7% 15.9%;
  --destructive:   0 62.8% 30.6%;
  --border:        240 3.7% 15.9%;
}
```

### CODEXA Semantic (Layer 2)

```css
:root {
  --codexa-accent:          #50C878;
  --codexa-accent-hover:    #45b56b;
  --codexa-accent-active:   #3da25f;
  --codexa-surface-900:     hsl(240 10% 5%);
  --codexa-surface-800:     hsl(240 8% 12%);
  --codexa-surface-700:     hsl(240 6% 20%);
  --codexa-surface-600:     hsl(240 5% 30%);
  --codexa-surface-500:     hsl(240 4% 40%);
  --codexa-text-primary:    hsl(0 0% 95%);
  --codexa-text-secondary:  hsl(0 0% 70%);
  --codexa-text-tertiary:   hsl(0 0% 50%);
  --codexa-border-default:  hsl(240 5% 25%);
  --codexa-border-subtle:   hsl(240 5% 15%);
}
```

### Semantic Colors (Functional)

```yaml
semantic:
  success:  "#22c55e"  # green-500
  warning:  "#f59e0b"  # amber-500
  error:    "#ef4444"  # red-500
  info:     "#3b82f6"  # blue-500
```

## 60-30-10 Rule Implementation

| Allocation | Colors | Classes | Measurement |
|------------|--------|---------|-------------|
| **60% (Dominant)** | `--background`, `--codexa-surface-*` | `bg-background`, `bg-codexa-surface-800` | Count `bg-` classes in component |
| **30% (Secondary)** | `--foreground`, `--muted`, `--secondary` | `text-foreground`, `bg-secondary` | Count `text-`, `border-` classes |
| **10% (Accent)** | `--codexa-accent`, `--primary`, `--destructive` | `bg-codexa-accent`, `text-primary` | Count accent/CTA classes |

### Enforcement Criteria

```yaml
per_component_audit:
  background_ratio: ">= 60% of visual area"
  text_secondary_ratio: "~ 30% of visual elements"
  accent_ratio: "<= 10% (CTAs, highlights only)"
  measurement: "DOM element count per color category"
  threshold: "Accent colors on max 2 elements per screen"
```

## Forbidden Patterns

```yaml
forbidden:
  - pattern: "bg-[#...]"
    reason: "Arbitrary hex in Tailwind class"
  - pattern: "text-[#...]"
    reason: "Arbitrary hex in Tailwind class"
  - pattern: "border-[#...]"
    reason: "Arbitrary hex in Tailwind class"
  - pattern: 'style="color:.*#'
    reason: "Inline hex color"
  - pattern: 'style="background:.*#'
    reason: "Inline hex background"
```

## Allowed Tailwind Color Classes

```yaml
allowed_classes:
  backgrounds: [bg-background, bg-primary, bg-secondary, bg-muted, bg-accent, bg-destructive]
  text: [text-foreground, text-primary, text-secondary, text-muted-foreground]
  borders: [border-border, border-primary, border-destructive]
  codexa: [bg-codexa-accent, text-codexa-text-primary, border-codexa-border-default]
  semantic: [text-green-500, text-amber-500, text-red-500, text-blue-500]
```

## Dark Mode

```yaml
dark_mode:
  strategy: "class-based (.dark on <html>)"
  rule: "Invert lightness, preserve hue"
  toggle: "JS class toggle on documentElement"
  test: "All text readable, all contrast ratios maintained"
```

## Validation

```yaml
validation:
  scan_for: "hardcoded hex in className or style attributes"
  expected: 0
  tool: "grep -rn '#[0-9a-fA-F]{3,8}' --include='*.html'"
  exceptions: ["meta theme-color", "SVG fill/stroke in design tokens file only"]
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p05_output_dashboard_ui]] | upstream | 0.54 |
| [[p10_dtc_design_token_contract]] | sibling | 0.53 |
| [[n02_kc_color_theory_applied]] | upstream | 0.41 |
| [[spec_n02_part2]] | related | 0.40 |
| [[p05_output_style_guide]] | upstream | 0.39 |
| [[p01_kc_color_theory_applied]] | upstream | 0.31 |
| [[spec_n02_visual_frontend_engineer]] | related | 0.31 |
| [[p09_lpt_landing_page_template]] | downstream | 0.31 |
| [[p10_hos_html_output_visual_frontend]] | sibling | 0.30 |
| [[n06_output_visual_identity]] | upstream | 0.30 |
