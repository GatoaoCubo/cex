---
id: n02_kc_typography_web
kind: knowledge_card
8f: F3_inject
pillar: P01
title: Web Typography — Scale, Pairing & Performance
version: 1.0.0
created: 2026-04-01
updated: 2026-04-01
author: shaka_research
domain: typography
quality: 9.2
tags: [knowledge_card, typography, fonts, type-scale, variable-fonts, font-display, N02]
tldr: Font pairing contrast principle, type scale ratios, line-height rules, max line length, font-display swap, variable fonts, hierarchy via weight+size+color — not size alone.
when_to_use: Load before choosing fonts, setting up a type system, or writing CSS typography foundations.
keywords: [typography, type scale, line-height, font pairing, variable fonts, font-display, Google Fonts, FOUT, letter-spacing, readability]
long_tails:
  - What is the ideal line-height for body text on web
  - How to pair fonts using the contrast principle
  - What font-display value prevents FOUT and CLS
  - How to use variable fonts in CSS
  - What is the maximum line length for readable web text
axioms:
  - ALWAYS establish type scale from a ratio before picking sizes individually
  - ALWAYS set max line width — unconstrained text destroys readability
  - NEVER pair two fonts from the same classification without clear contrast axis
  - NEVER use font-display:block for web fonts — invisible text for 3s kills UX
linked_artifacts:
  related: [n02_kc_visual_hierarchy_principles, n02_kc_color_theory_applied]
density_score: 0.91
data_source: fonts.google.com/knowledge + typescale.com + refactoringui.com + internal_distillation
related:
  - p01_kc_typography_web
  - n02_kc_responsive_layout_systems
  - p06_schema_responsive_breakpoints
  - n06_output_pricing_page
  - p05_output_email_template
  - kc_visual_hierarchy_principles
  - n02_kc_email_html_responsive
  - p01_kc_responsive_layouts
  - p05_output_social_card
  - n06_output_visual_identity
---

# Web Typography — Scale, Pairing & Performance

## Quick Reference

```yaml
domain: typography
nucleus: N02
default_scale: 1.333 (Perfect Fourth)
body_line_height: 1.5–1.75
heading_line_height: 1.1–1.3
max_line_length: 45–75 chars (65 optimal)
base_font_size: 16px
font_display_default: swap
```

---

## 1. Font Pairing — The Contrast Principle

**Rule**: Pair fonts that differ on at least 2 axes. Similarity creates visual tension without harmony.

### Pairing Axes
| Axis | Options |
|------|---------|
| **Classification** | Serif ↔ Sans-serif (strongest contrast) |
| **Personality** | Geometric ↔ Humanist |
| **Weight** | Display (heavy) ↔ Text (light) |
| **Structure** | High x-height ↔ Low x-height |

### What NOT to pair
- Two geometric sans-serifs (Inter + DM Sans → too similar)
- Two serifs at similar weight (Georgia + Merriweather → visual conflict)
- Decorative + Decorative (unreadable noise)

### Proven Google Fonts Pairings

| Heading | Body | Character |
|---------|------|-----------|
| **Playfair Display** | **Source Sans Pro** | Editorial, luxury, premium |
| **Raleway** | **Lato** | Clean, modern, SaaS |
| **Merriweather** | **Open Sans** | Blog, content, readable |
| **Montserrat** | **Merriweather** | Bold brand + readable body |
| **Nunito** | **Inter** | Friendly, product UI |
| **DM Serif Display** | **DM Sans** | Same family, curated contrast |
| **Fraunces** | **Figtree** | Expressive, contemporary |

**Simple rule for pairing**: Use the same type family's display + text variants (DM Serif + DM Sans) — designed to work together, zero guessing.

---

## 2. Type Scale System

### Ratios Reference

| Name | Ratio | Steps from 16px base |
|------|-------|----------------------|
| Minor Second | 1.067 | Subtle — dense UIs |
| Major Second | 1.125 | Conservative editorial |
| Minor Third | 1.200 | Moderate hierarchy |
| **Major Third** | **1.250** | Balanced landing pages |
| **Perfect Fourth** | **1.333** | Recommended default |
| Augmented Fourth | 1.414 | Bold, magazine |
| Perfect Fifth | 1.500 | Hero-forward layouts |
| Golden Ratio | 1.618 | Maximum drama |

### Perfect Fourth Scale (base 16px) — Implementation

```css
:root {
  --text-xs:   0.640rem;  /* ~10px */
  --text-sm:   0.750rem;  /* ~12px */
  --text-base: 1.000rem;  /* 16px  */
  --text-md:   1.333rem;  /* ~21px */
  --text-lg:   1.777rem;  /* ~28px */
  --text-xl:   2.369rem;  /* ~38px */
  --text-2xl:  3.157rem;  /* ~51px */
  --text-3xl:  4.209rem;  /* ~67px */
}
```

**When to choose a ratio**:
- Data-dense UI / dashboard → Minor Second (1.067) or Major Second (1.125)
- Marketing page / blog → Perfect Fourth (1.333)
- Hero-heavy landing page → Augmented Fourth (1.414) or Perfect Fifth (1.500)

---

## 3. Line-Height Rules

### By Context

| Context | line-height | Rationale |
|---------|------------|-----------|
| **Body text** | **1.5–1.75** | Optimal for reading long paragraphs |
| **Short body (UI)** | **1.4–1.5** | Cards, summaries, form descriptions |
| **Headings (h1–h2)** | **1.1–1.2** | Large type needs tighter leading |
| **Subheadings (h3–h4)** | **1.2–1.3** | Slightly looser than h1 |
| **Captions / small** | **1.4** | Compensate for small size |
| **Code / mono** | **1.6–1.8** | Needs more air for readability |

```css
/* Practical defaults */
body        { line-height: 1.6; }
h1, h2      { line-height: 1.15; }
h3, h4      { line-height: 1.25; }
.caption    { line-height: 1.4; }
pre, code   { line-height: 1.7; }
```

**Avoid**: `line-height: 2` on body — feels like a draft document, not a product.

---

## 4. Max Line Length (Measure)

**Optimal**: 65 characters (including spaces)
**Acceptable range**: 45–75 characters
**Absolute max**: 90 characters (beyond this, eye loses track of line start)

```css
/* Constraint methods */
.prose    { max-width: 65ch; }      /* ch = width of "0" character */
.prose    { max-width: 680px; }     /* at 16px, ~65 chars */
.prose    { max-width: 38rem; }     /* relative units */
```

**Short lines (<45 chars)**: Create a choppy, fragmented reading experience (newspaper column effect).
**Long lines (>80 chars)**: Eye must travel far — readers lose their place; reading speed decreases.

---

## 5. Letter-Spacing (Tracking)

| Context | letter-spacing | Why |
|---------|---------------|-----|
| **Large headings (>48px)** | `-0.02em` to `-0.04em` | Optical tightening — large type feels loose at 0 |
| **Medium headings (24–48px)** | `-0.01em` to `-0.02em` | Slight tightening |
| **Body text** | `0` | Designed for neutral tracking — don't touch |
| **Small caps / uppercase** | `+0.05em` to `+0.1em` | All-caps needs opening to remain readable |
| **Captions / metadata** | `+0.01em` to `+0.02em` | Slight opening aids small-size readability |

```css
h1 { letter-spacing: -0.03em; }
h2 { letter-spacing: -0.02em; }
.uppercase-label { letter-spacing: 0.08em; text-transform: uppercase; }
```

---

## 6. Font Display Strategy

Controls how browsers handle font loading:

| Value | Behavior | Use Case |
|-------|----------|----------|
| `auto` | Browser decides (usually block) | Avoid |
| `block` | Invisible text for 3s → swap | Avoid — terrible UX |
| `swap` | Show fallback immediately → swap when loaded | **Default choice** |
| `fallback` | Invisible 100ms → fallback → swap within 3s | Good for critical UI |
| `optional` | Brief invisible → if loaded, use it; if not, skip | Best for performance / no FOUT |

```css
/* Standard implementation */
@font-face {
  font-family: 'Inter';
  src: url('/fonts/inter.woff2') format('woff2');
  font-display: swap;   /* show system font immediately */
  font-weight: 100 900; /* variable font range */
}
```

**FOUT (Flash of Unstyled Text)**: `swap` causes visible swap. Mitigate by matching fallback metrics:
```css
/* Size-adjust fallback to minimize layout shift */
@font-face {
  font-family: 'Inter-Fallback';
  src: local('Arial');
  size-adjust: 107%;
  ascent-override: 90%;
  descent-override: 22%;
}
```

---

## 7. Variable Fonts

Single font file with continuous axis ranges instead of separate files per weight.

### Common Axes

| Axis Tag | Range | Description |
|----------|-------|-------------|
| `wght` | 100–900 | Weight (thin to black) |
| `wdth` | 75–125 | Width (condensed to expanded) |
| `slnt` | -15 to 0 | Slant (oblique) |
| `ital` | 0 or 1 | Italic (discrete) |
| `opsz` | 8–144 | Optical size (adjusts letter forms per size) |

```css
/* Variable font: single file, any weight */
body { font-weight: 400; }           /* Regular */
strong { font-weight: 700; }         /* Bold */
.display { font-weight: 800; }       /* Extrabold */

/* Custom optical size */
h1 { font-variation-settings: 'opsz' 48; }
p  { font-variation-settings: 'opsz' 16; }
```

**Performance**: 1 variable font file ≈ 2–3 separate weight files combined, but serves all weights.
**Top variable fonts from Google Fonts**: Inter, Roboto Flex, Source Serif 4, Fraunces, Recursive

---

## 8. Typographic Hierarchy — Not Just Size

**Bad hierarchy**: Only varying font-size.
**Good hierarchy**: Combining size + weight + color + spacing.

```css
/* Three-level hierarchy example */

/* Primary — most important */
.h1-primary {
  font-size: var(--text-2xl);    /* 51px */
  font-weight: 800;
  color: var(--color-text);      /* full contrast */
  letter-spacing: -0.03em;
  line-height: 1.1;
}

/* Secondary — supporting */
.h2-secondary {
  font-size: var(--text-lg);     /* 28px */
  font-weight: 600;
  color: var(--color-text);
  letter-spacing: -0.01em;
  line-height: 1.25;
}

/* Tertiary — context */
.body-tertiary {
  font-size: var(--text-base);   /* 16px */
  font-weight: 400;
  color: var(--color-muted);     /* reduced contrast */
  line-height: 1.6;
}
```

**The 4 axes of visual hierarchy in type**:
1. **Size** — most obvious; use scale ratio
2. **Weight** — 400 (regular) vs 700 (bold) — most versatile lever
3. **Color** — full contrast vs muted (--color-text vs --color-muted)
4. **Letter-spacing** — subtle but powerful at large sizes

---

## 9. Top Font Pairings with CSS Implementation

### Inter + Merriweather (SaaS + Content)
```css
body    { font-family: 'Merriweather', Georgia, serif; }
.ui, h1 { font-family: 'Inter', system-ui, sans-serif; }
```

### Playfair Display + Lato (Editorial + Clean)
```css
h1, h2  { font-family: 'Playfair Display', Georgia, serif; }
body    { font-family: 'Lato', Helvetica, sans-serif; }
```

### Montserrat + Open Sans (Brand + Readable)
```css
h1, h2  { font-family: 'Montserrat', sans-serif; font-weight: 700; }
body    { font-family: 'Open Sans', sans-serif; font-weight: 400; }
```

---

## 10. Anti-Patterns

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| All text the same weight | No hierarchy → eye doesn't know where to start | Use 400/600/800 weight scale |
| `line-height: 1` on body text | Lines crash together — unreadable | Min 1.5 for body |
| Unconstrained text width | >80 chars/line → eye loses position | `max-width: 65ch` on prose containers |
| 3+ typefaces on one page | Visual chaos | Max 2 typefaces, max 3 weights each |
| `font-display: block` | 3s invisible text → bad FCP, bad UX | Use `swap` or `optional` |
| `letter-spacing: 0.1em` on body | Breaks word rhythm, harder to read | Only open letter-spacing on caps/captions |
| Centering long body paragraphs | Unnatural eye tracking for reads >3 lines | Left-align body; center only short headlines/CTAs |
| Using px for font-size on html | Overrides user browser font preferences | Set `html { font-size: 100% }` then use rem |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_typography_web]] | sibling | 0.32 |
| [[n02_kc_responsive_layout_systems]] | sibling | 0.31 |
| [[p06_schema_responsive_breakpoints]] | downstream | 0.28 |
| [[n06_output_pricing_page]] | downstream | 0.24 |
| [[p05_output_email_template]] | downstream | 0.21 |
| [[kc_visual_hierarchy_principles]] | sibling | 0.21 |
| [[n02_kc_email_html_responsive]] | sibling | 0.20 |
| [[p01_kc_responsive_layouts]] | sibling | 0.18 |
| [[p05_output_social_card]] | downstream | 0.18 |
| [[n06_output_visual_identity]] | downstream | 0.18 |
