---
id: p06_schema_tailwind_palette
kind: input_schema
pillar: P06
title: "Tailwind Palette Contract"
version: 1.0.0
created: 2026-04-01
author: n02_visual_frontend
domain: frontend
quality: 8.8
tags: [schema, tailwind, palette, design-system, color]
tldr: "Restricted palette contract — 60-30-10 rule, zero hardcoded hex, CODEXA tokens."
density_score: 0.93
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

## 60-30-10 Rule

```yaml
distribution:
  60_percent: "background / surface colors (--background, --codexa-surface-*)"
  30_percent: "secondary / muted / text (--secondary, --muted, --foreground)"
  10_percent: "accent / CTA / highlights (--codexa-accent, --primary)"
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
