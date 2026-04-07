---
id: brand_context_n03
kind: config
pillar: P09
title: Brand Context for N03
version: 2.0.0
created: 2026-04-01
updated: 2026-04-07
author: n04_knowledge
quality: 9.1
tags: [brand, context, n03, engineering, design-system]
tldr: "Brand context for N03 Engineering — visual design system, component standards, accessibility rules, and technical implementation guidelines for GATO³ PB minimal aesthetic."
density_score: 0.95
---

# Brand Context — N03 Engineering

> Source: `.cex/brand/brand_config.yaml`
> Nucleus: N03 (Engineering/Build)
> Domain: Artifact construction, templates, code, schemas

## Core Brand Identity

| Field | Value |
|-------|-------|
| **Brand** | GATO³ (Gato ao Cubo) |
| **Tagline** | Educação que acalma, soluções que funcionam, casa que continua elegante. |
| **Style** | minimal-pb (monochrome minimalism) |
| **Language** | pt-BR |
| **Archetype** | Caregiver |

## Visual Design System

### Color Palette

| Token | Hex | Usage |
|-------|-----|-------|
| `--color-primary` | `#000000` | Headlines, CTAs, nav, icons |
| `--color-secondary` | `#1F1F1F` | Body text, secondary elements |
| `--color-accent` | `#7A7A7A` | Muted labels, borders, captions |
| `--color-background` | `#FFFFFF` | Page background, card surfaces |
| `--color-foreground` | `#000000` | Text on light backgrounds |
| `--color-surface` | `#D1D1D1` | Cards, dividers, hover states |

### Accessibility Rules
- Contrast ratio: `#000000` on `#FFFFFF` = 21:1 (WCAG AAA ✓)
- Contrast ratio: `#7A7A7A` on `#FFFFFF` = 4.56:1 (WCAG AA ✓, AAA ✗ — use only for large text/decorative)
- Never use `#D1D1D1` for text — insufficient contrast (1.98:1)
- All interactive elements must have `:focus-visible` outlines

### Typography

| Role | Font | Fallback | Weight | Usage |
|------|------|----------|--------|-------|
| Headings | Allrounder | system-ui, sans-serif | 600-700 | H1-H4, hero text, CTAs |
| Body | Kenao | Georgia, serif | 400-500 | Paragraphs, descriptions, lists |
| Code/Data | JetBrains Mono | monospace | 400 | Code blocks, prices, SKUs |

### Spacing & Layout
- Base unit: 8px grid
- Section padding: 48px (6 units) desktop, 24px (3 units) mobile
- Card border-radius: 4px (subtle, not rounded)
- Max content width: 1200px
- Minimal shadows — prefer borders with `#D1D1D1`

## N03 Engineering Guidelines

### Component Architecture
1. **Template naming**: `tpl_{pillar}_{kind}_{descriptor}.md`
2. **Schema naming**: `schema_{kind}.yaml`
3. **Variables**: Use `{{BRAND_*}}` mustache syntax — never hardcode brand values
4. **Localization**: All user-facing strings default to `pt-BR`

### Build Quality Standards
| Criterion | Threshold | Rationale |
|-----------|-----------|-----------|
| Frontmatter completeness | 100% required fields | Schema compliance |
| Variable resolution | 0 unresolved `{{BRAND_*}}` | No broken templates |
| Accessibility | WCAG 2.1 AA minimum | Legal + ethical requirement |
| Mobile-first | All layouts responsive at 375px+ | ICP is mobile-heavy (25-45 urban) |
| Performance | LCP < 2.5s, CLS < 0.1 | SEO + UX for marketplace conversion |

### Design Decisions for GATO³
- **PB aesthetic**: Monochrome by default. Product photos provide the only color.
- **Whitespace-heavy**: Caregiver archetype demands calm, uncluttered layouts
- **No ornamental elements**: Icons only when functional (nav, status, actions)
- **Photography style**: High-key, soft shadows, cat-centric compositions
- **CTA style**: Solid black buttons, white text, no gradients or animations

### Anti-Patterns (N03-specific)
- ❌ Colorful badges, ribbons, or "SALE!" overlays — contradicts minimal-pb
- ❌ Stock photos of generic cats — use brand photography or illustration
- ❌ Rounded pill buttons — angular (4px radius) aligns with sophistication
- ❌ Comic Sans, cursive, or playful fonts — undermines authority
- ❌ Auto-playing videos or carousels — contradicts calm UX

## Brand Assets

| Asset | URL/Path |
|-------|----------|
| Logo (SVG) | `https://gato3.com.br/logo.svg` |
| Favicon | `https://gato3.com.br/favicon.ico` |
| Design tokens | `.cex/brand/tokens.css` |
| Brand config | `.cex/brand/brand_config.yaml` |

## Cross-References
- N02 voice guidelines → `N02_marketing/config/brand_context.md`
- N04 content structure → `N04_knowledge/config/brand_context.md`
- Brand validation → `python _tools/brand_validate.py`
- Brand propagation → `python _tools/brand_propagate.py`
