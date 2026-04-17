---
id: n02_kc_color_theory_applied
kind: knowledge_card
pillar: P01
title: Color Theory Applied — Palettes, Systems & Accessibility
version: 1.0.0
created: 2026-04-01
updated: 2026-04-01
author: shaka_research
domain: color-systems
quality: 9.2
tags: [knowledge_card, color, design-system, WCAG, dark-mode, accessibility, N02]
tldr: 60-30-10 rule, color harmony, HSL manipulation, semantic naming, dark mode derivation, WCAG contrast ratios, GitHub Primer + Material Design 3 patterns.
when_to_use: Load before building any color system, choosing palette for a brand/UI, or implementing dark mode.
keywords: [color theory, 60-30-10, HSL, WCAG, contrast ratio, dark mode, semantic color, color blindness, Material Design, GitHub Primer]
long_tails:
  - How to derive a dark mode palette from a light mode palette
  - What WCAG contrast ratio is required for accessible text
  - How to name colors semantically in a design system
  - How to build a color palette safe for color-blind users
  - 60-30-10 rule with real examples for landing pages
axioms:
  - ALWAYS name colors by role/semantic meaning, never by hue (--color-danger not --color-red)
  - ALWAYS verify contrast ratio before shipping — 4.5:1 minimum for body text
  - NEVER use pure black (#000000) or pure white (#ffffff) as dark mode backgrounds
  - NEVER rely on color alone to convey meaning — pair with icon, text, or shape
linked_artifacts:
  related: [n02_kc_visual_hierarchy_principles, n02_kc_typography_web]
density_score: 0.92
data_source: primer.style/foundations/color + m3.material.io + webaim.org/contrastchecker + internal_distillation
---

# Color Theory Applied — Palettes, Systems & Accessibility

## Quick Reference

```yaml
domain: color-systems
nucleus: N02
60_30_10: dominant / secondary / accent
wcag_aa_normal: 4.5:1
wcag_aa_large: 3:1
wcag_aaa_normal: 7:1
dark_mode_bg: #121212 (not #000000)
color_blindness_affected: 8% men, 0.5% women
```

---

## 1. The 60-30-10 Rule

Distribution of color in any design composition:

| Role | % | Use |
|------|---|-----|
| **Dominant** | 60% | Background, neutral base, large surfaces |
| **Secondary** | 30% | Cards, sidebars, secondary UI elements |
| **Accent** | 10% | CTAs, highlights, links, key data points |

**Practical examples**:

```
Light UI: 60% white/light gray → 30% medium gray/soft tone → 10% brand blue
Dark UI:  60% #1a1a2e → 30% #16213e → 10% #e94560
Ad layout: 60% white space → 30% product image → 10% CTA button color
```

**Warning**: Reversing to 10% dominant destroys visual clarity. Accent must stay ≤15%.

---

## 2. Color Harmony Patterns

| Harmony | Description | Best For | Risk |
|---------|-------------|----------|------|
| **Complementary** | Opposite on color wheel (e.g., blue + orange) | CTAs, high-contrast highlights | Vibrating effect if used at full saturation |
| **Analogous** | Adjacent on wheel (e.g., blue + blue-green + cyan) | Backgrounds, calm UIs, nature brands | Low contrast between shades |
| **Triadic** | Equidistant (e.g., red + blue + yellow) | Playful, energetic brands | Hard to balance — reduce saturation of 2 |
| **Split-complementary** | Base + 2 adjacent to complement | Safer than complementary | Still needs saturation management |
| **Tetradic/Square** | 4 colors 90° apart | Complex, rich palettes | Easy to feel chaotic — use 1 dominant |
| **Monochromatic** | Single hue, varied lightness/saturation | Elegant, minimal, premium | Risk of monotony — use texture/type weight |

**Rule**: Start with analogous for brand harmony, add complementary accent for CTA contrast.

---

## 3. HSL — Color Manipulation in Code

HSL = Hue (0–360°) + Saturation (0–100%) + Lightness (0–100%)

```css
/* Base brand color */
--brand: hsl(220, 90%, 50%);

/* Shade variations */
--brand-50:  hsl(220, 100%, 97%);  /* near-white tint */
--brand-100: hsl(220, 95%, 92%);
--brand-200: hsl(220, 94%, 84%);
--brand-300: hsl(220, 92%, 72%);
--brand-400: hsl(220, 91%, 62%);
--brand-500: hsl(220, 90%, 50%);   /* base */
--brand-600: hsl(220, 85%, 40%);
--brand-700: hsl(220, 80%, 32%);
--brand-800: hsl(220, 70%, 22%);
--brand-900: hsl(220, 60%, 12%);   /* near-black shade */
```

**Manipulation rules**:
- **Darken**: decrease L by 8–10 per step
- **Lighten**: increase L by 8–10 per step
- **Desaturate (muted)**: decrease S by 20–40 (for disabled/inactive states)
- **Shift warmth**: +10–15° on hue toward yellow/orange warms; –10–15° toward blue cools

**HSL vs Hex**: Always store as HSL in CSS custom properties — enables runtime theming. Hex is output only.

---

## 4. Semantic Color Naming

**Never name by hue. Name by role.**

| Semantic Role | CSS Variable Pattern | Primer Example | Material 3 Role |
|--------------|---------------------|----------------|-----------------|
| Primary brand | `--color-primary` | `--fgColor-accent` | `primary` |
| Destructive/danger | `--color-destructive` | `--fgColor-danger` | `error` |
| Success/positive | `--color-success` | `--fgColor-success` | (custom) |
| Warning/attention | `--color-warning` | `--fgColor-attention` | (custom) |
| Muted/secondary text | `--color-muted` | `--fgColor-muted` | `onSurfaceVariant` |
| Disabled | `--color-disabled` | `--fgColor-disabled` | (custom) |
| Background default | `--color-bg` | `--bgColor-default` | `surface` |
| Background inset | `--color-bg-inset` | `--bgColor-inset` | `surfaceVariant` |
| Border default | `--color-border` | `--borderColor-default` | `outline` |

### GitHub Primer Pattern (3-layer naming)
```
--{property}Color-{semantic}-{variant}

Layers:
  property: fg / bg / border / shadow / button
  semantic: accent / danger / success / attention / done / neutral / muted
  variant:  default / emphasis (solid) / muted (tinted/translucent)

Examples:
  --bgColor-danger-emphasis  → solid red background (#cf222e)
  --bgColor-danger-muted     → tinted red background (#ffebe9)
  --fgColor-danger           → red text (#d1242f)
```

### Material Design 3 Color Roles
```
primary           → main brand actions
on-primary        → text/icons ON primary surface
primary-container → lower emphasis primary surfaces  
on-primary-container → text ON primary-container

secondary / tertiary → supporting roles (same pattern)
error               → destructive actions
surface             → background canvases
on-surface          → text/icons on surfaces
surface-variant     → slightly differentiated surface
outline             → borders and dividers
```

---

## 5. Dark Mode Palette Derivation

**Do NOT simply invert lightness.** Inversion creates harsh, unrealistic gradients.

### Correct approach:

```
Light mode surface:  L=97% (near white)
Dark mode surface:   #121212 (not #000000)
  Why: Pure black creates eye strain; #121212 matches OLED efficiency + contrast targets
```

**Surface hierarchy in dark mode** (Material 3 elevation via lightness):
```
Level 0 (base surface):   #121212
Level 1 (cards/popups):   #1d1d1d  (+5% lightness)
Level 2 (raised cards):   #212121  (+8%)
Level 3 (nav/appbar):     #272727  (+11%)
Level 4 (modals):         #2c2c2c  (+14%)
Level 5 (tooltips):       #2e2e2e  (+16%)
```

**Color saturation in dark mode**:
- Reduce saturation by 20–30% for all palette colors
- Reason: Saturated colors on dark backgrounds cause halation (vibrating/bleeding effect)
- Increase lightness of accent colors: L=50% in light → L=65–75% in dark

**Semantic mapping**:
```
Light:  --color-primary: hsl(220, 90%, 50%)
Dark:   --color-primary: hsl(220, 70%, 68%)  (less sat, more light)
```

---

## 6. WCAG Contrast Ratios

Source: WCAG 2.1 + WebAIM Contrast Checker

| Level | Text Type | Minimum Ratio | Notes |
|-------|-----------|---------------|-------|
| **AA** | Normal text | **4.5:1** | Body copy, labels, placeholder |
| **AA** | Large text | **3:1** | ≥18px regular OR ≥14px bold |
| **AA** | UI components / graphics | **3:1** | Form borders, icons, charts |
| **AAA** | Normal text | **7:1** | Highest accessibility target |
| **AAA** | Large text | **4.5:1** | Large headings at AAA level |

**Large text definition**: ≥18pt (24px) regular **or** ≥14pt (18.66px) bold

**Testing**:
```
Tool: webaim.org/resources/contrastchecker
API: https://webaim.org/resources/contrastchecker/?fcolor=0969DA&bcolor=FFFFFF&api
Returns: { ratio, AA, AAA, AALarge, AAALarge }
```

**Primer passing examples**:
```
#0969da on #ffffff  → ratio ≈ 4.7:1 (AA pass)
#1a7f37 on #ffffff  → ratio ≈ 4.5:1 (AA pass, minimal)
#ffffff on #0969da  → ratio ≈ 4.7:1 (on-emphasis pass)
```

---

## 7. Color Blindness Safe Design

**Prevalence**: ~8% of men, ~0.5% of women have some form of color vision deficiency

| Type | Affected | Problem |
|------|----------|---------|
| Deuteranopia | Most common (~5%) | Red-green (green weak) |
| Protanopia | ~1% | Red-green (red weak) |
| Tritanopia | Rare (<0.01%) | Blue-yellow |

**Rules for accessible color**:
1. **Never** use red vs green alone to convey success/error — add icon + text label
2. Use **blue** as primary accent — visible across all major CVD types
3. Avoid **red+green** side-by-side charts — use blue+orange instead
4. Test with simulator: browser extensions (Colorblinding, Stark) or Figma plugins

**Safe complementary pair**: Blue (#0066CC) + Orange (#E87722) — distinguishable by all CVD types

**Pattern**: Always combine color + shape + text:
```
Error: red background + ✕ icon + "Error" label
Success: green background + ✓ icon + "Success" label
```

---

## 8. Color Psychology Quick Reference

| Color | Association | Use In | Avoid |
|-------|-------------|--------|-------|
| Blue | Trust, stability, calm | Finance, SaaS, health, tech | Food (appetite suppressor) |
| Red | Urgency, danger, passion | CTAs, sale badges, alerts | Trust-building contexts |
| Green | Growth, success, nature | Success states, eco, finance | N/A — broadly safe |
| Orange | Energy, warmth, affordability | E-commerce CTAs, food | Premium/luxury brands |
| Purple | Luxury, creativity, mystery | Beauty, premium, creative | B2B enterprise |
| Yellow | Optimism, attention, caution | Warning states, highlights | Large background areas (fatiguing) |
| Black | Sophistication, authority | Luxury, fashion, premium tech | Budget/friendly brands |
| White | Clean, minimal, space | Backgrounds, breathing room | Solo use without contrast |

---

## 9. Anti-Patterns

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| Naming variables `--red`, `--blue` | Breaks on theme change | Use `--color-danger`, `--color-primary` |
| Pure black on pure white | Max contrast → eye strain for long reading | Use #1f2328 on #ffffff (GitHub default) |
| Saturated accent on dark bg | Halation / vibrating effect | Desaturate 20–30% for dark mode |
| Color alone for status | Fails WCAG + color blindness | Add icon + text label |
| Inverting light palette for dark | Harsh, unrealistic | Start from #121212, build up with lightness steps |
| 4+ accent colors | Visual noise | 1 primary accent + 1 semantic accent max per section |
