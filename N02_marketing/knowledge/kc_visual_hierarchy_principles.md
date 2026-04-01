---
id: n02_kc_visual_hierarchy_principles
kind: knowledge_card
pillar: P01
title: Visual Hierarchy — Principles & Layout Patterns
version: 1.0.0
created: 2026-04-01
updated: 2026-04-01
author: shaka_research
domain: design-theory
quality: 9.0
tags: [knowledge_card, design, visual-hierarchy, gestalt, ux-laws, layout, N02]
tldr: F/Z scanning patterns, Gestalt laws, visual weight, type scale ratios, UX laws (Fitts, Hick, Jakob, Miller) — operational reference for UI/marketing layout decisions.
when_to_use: Load before designing landing pages, ads, email layouts, or any visual hierarchy decision.
keywords: [visual hierarchy, F-pattern, Z-pattern, Gestalt, Fitts law, Hick law, Miller law, Jakob law, whitespace, golden ratio, rule of thirds, type scale]
long_tails:
  - When to use F-pattern vs Z-pattern in landing page design
  - How Gestalt principles apply to UI component grouping
  - What type scale ratio to use for a marketing landing page
  - How whitespace increases perceived quality and conversion
  - Which UX laws apply to CTA design and menu complexity
axioms:
  - ALWAYS establish visual hierarchy before choosing colors — structure first, decoration second
  - ALWAYS match scan pattern (F vs Z) to content density of the page
  - NEVER rely on size alone for hierarchy — combine weight, color, and spacing
  - NEVER put more than 7 items in a navigation or list without grouping
linked_artifacts:
  related: [n02_kc_color_theory_applied, n02_kc_typography_web]
density_score: 0.93
data_source: laws-of-ux.com + refactoringui.com + typescale.com + internal_distillation
---

# Visual Hierarchy — Principles & Layout Patterns

## Quick Reference

```yaml
domain: design-theory
nucleus: N02
patterns: [F-pattern, Z-pattern, Gestalt, UX-laws, scale-ratios]
ux_laws: [Fitts, Hick, Jakob, Miller, Von-Restorff, Doherty, Zeigarnik]
type_scale_default: 1.333 (Perfect Fourth)
golden_ratio: 1.618
```

---

## 1. Eye Scanning Patterns

### F-Pattern
- **When**: Text-heavy pages — blogs, news, article pages, long-form copy
- **How eyes move**: Horizontal scan top → secondary horizontal scan mid-page → vertical scan down left margin
- **Implication**: Most important content goes in top-left and first 2 lines; users skip right side and bottom
- **Use for**: Blog posts, documentation, email newsletters, product description pages

### Z-Pattern
- **When**: Low-density pages — landing pages, ads, hero sections, minimal UIs
- **How eyes move**: Top-left → top-right (1st horizontal) → diagonal to bottom-left → bottom-right (2nd horizontal)
- **Implication**: CTAs belong at top-right or bottom-right; logo/trust at top-left; benefit at bottom-left
- **Use for**: Hero sections, print ads, social media ads, splash pages

### Gutenberg Diagram (variant)
- 4 quadrants: Primary (top-left) → Follow area (top-right) → Fallow area (bottom-left) → Terminal (bottom-right)
- Terminal zone = natural CTA placement for Z-pattern pages

---

## 2. Gestalt Principles

| Principle | Definition | Design Application |
|-----------|------------|-------------------|
| **Proximity** | Elements close together appear related | Group form fields, card content; separate unrelated sections with space |
| **Similarity** | Same visual style = same category | Consistent button styles per action type; uniform card layouts |
| **Closure** | Brain completes incomplete shapes | Dashed borders, icon outlines, partial circles → perceived as whole |
| **Continuity** | Eyes follow lines and curves | Carousels, progress steps, timeline flows |
| **Figure-Ground** | Object (figure) vs background separation | Modals, tooltips, dropdowns — contrast separates layered content |
| **Symmetry** | Symmetrical layouts feel stable | Centering hero sections, balanced 2-col layouts |
| **Common Fate** | Elements moving together appear grouped | Hover states, animated groups, parallax sections |

---

## 3. Visual Weight Hierarchy

Ranking from heaviest to lightest visual weight:

1. **Size** — larger = more dominant (most powerful lever)
2. **Color/Saturation** — bright, saturated colors attract more attention than muted
3. **Contrast** — high contrast element on low-contrast field = focal point
4. **Position** — top > bottom; left > right (in LTR languages)
5. **Whitespace** — isolated elements gain weight from surrounding space
6. **Texture/Complexity** — complex shapes attract more attention than simple
7. **Warm vs Cool** — warm colors (red, orange) advance; cool (blue, green) recede

**Rule**: Vary weight across exactly 3 levels per screen section (primary, secondary, tertiary). More than 3 collapses into noise.

---

## 4. Typography Scale Ratios

| Ratio Name | Value | Use Case |
|-----------|-------|----------|
| Minor Second | 1.067 | Dense UIs, data tables, micro-copy |
| Major Second | 1.125 | Body-heavy interfaces, dashboards |
| Minor Third | 1.200 | Conservative, editorial |
| **Major Third** | **1.250** | Balanced — landing pages, SaaS |
| **Perfect Fourth** | **1.333** | Default recommendation — clear hierarchy |
| Augmented Fourth | 1.414 | Bold, magazine-style layouts |
| Perfect Fifth | 1.500 | Hero-heavy, minimal-text designs |
| Golden Ratio | 1.618 | Max drama, large displays only |

**How to apply (base 16px, Perfect Fourth 1.333)**:

```
xs:  10px  (16 / 1.333^2)
sm:  12px  (16 / 1.333)
base: 16px
md:  21px  (16 × 1.333)
lg:  28px  (16 × 1.333²)
xl:  37px  (16 × 1.333³)
2xl: 50px  (16 × 1.333⁴)
3xl: 67px  (16 × 1.333⁵)
```

---

## 5. Layout Geometry

### Golden Ratio (1.618)
- Column widths: narrow col / wide col = 1 / 1.618
- Common split: 38% / 62% (sidebar vs main content)
- Logo sizing, spacing proportions, image ratios

### Rule of Thirds
- Divide canvas into 3×3 grid (2 horizontal + 2 vertical lines)
- Place focal elements at 4 intersection points
- Apply to: hero images, ad visuals, product photos, section layouts

### 8px Grid System
- All spacing in multiples of 8px (4px for micro-spacing)
- Rationale: screens divide evenly at 360, 375, 768, 1024, 1440px
- Tailwind default: `space-2 = 8px, space-4 = 16px, space-8 = 32px`

---

## 6. Laws of UX

### Fitts's Law
- **Rule**: Time to reach a target = f(distance / target size) — smaller and farther = harder
- **Application**: Primary CTAs must be large (min 44×44px touch target) and near natural eye position
- **Anti-pattern**: Small "Buy Now" button far from product image

### Hick's Law
- **Rule**: Decision time ∝ log₂(n+1) where n = number of choices
- **Application**: Limit navigation to ≤7 items; use progressive disclosure for complex forms
- **Anti-pattern**: 15-item mega menu; showing all 30 options at once

### Jakob's Law
- **Rule**: Users expect your interface to work like interfaces they already know
- **Application**: Follow platform conventions (hamburger at top-left mobile, logo links home)
- **Anti-pattern**: Putting checkout button at left; unconventional navigation placement

### Miller's Law
- **Rule**: Working memory holds ~7 (±2) items at a time
- **Application**: Chunk phone numbers (555-867-5309), group form fields, paginate long lists
- **Anti-pattern**: 12-item list without visual grouping

### Von Restorff Effect (Isolation Effect)
- **Rule**: Distinctive items are remembered better than conforming items
- **Application**: Highlight one "recommended" pricing tier; use a contrasting CTA color
- **Anti-pattern**: All pricing tiers the same visual weight — none converts

### Doherty Threshold
- **Rule**: User attention maintained when system responds in <400ms
- **Application**: Show skeleton screens, progress indicators for operations >400ms
- **Anti-pattern**: Blank white screen during page transitions

### Zeigarnik Effect
- **Rule**: Incomplete tasks are remembered better than completed ones
- **Application**: Progress bars, onboarding checklists, "You're 60% done!" nudges
- **Anti-pattern**: No completion indicator on multi-step flows

### Serial Position Effect
- **Rule**: Items at beginning and end of a list are remembered best (primacy + recency)
- **Application**: Put most important nav items first and last; strongest social proof first/last
- **Anti-pattern**: Burying the best feature in the middle of a feature list

---

## 7. Whitespace as a Design Feature

### Macro Whitespace (between sections)
- Minimum section padding: 80–120px vertical on desktop
- Creates breathing room, signals topic transitions
- Premium brands use 2–3× more whitespace than budget brands (Apple vs. Wish)

### Micro Whitespace (between elements)
- Paragraph spacing: 1em–1.5em between paragraphs
- Component padding: match to 8px grid (16px, 24px, 32px common)
- Letter-spacing: body = 0; large headings = -0.01 to -0.03em (tighten)

### Whitespace and Perceived Quality
- More whitespace → higher perceived price point and brand quality
- Reduce clutter by removing, not shrinking — dead space communicates confidence

---

## 8. Anti-Patterns

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| Equal visual weight on all elements | No focal point — eye doesn't know where to go | Establish 1 primary, 2 secondary, rest tertiary |
| F-pattern layout on minimal landing page | Users skip key content | Switch to Z-pattern for low-density pages |
| 10+ nav items | Hick's Law — decision paralysis | Limit to 5–7 or use mega menu with grouping |
| CTA at bottom-right of long page | User never reaches it | Sticky CTA or repeat at F/Z terminal zone |
| Centered body text > 3 lines | Hard to read, unnatural scan pattern | Left-align body text; center only short headlines |
| No whitespace between sections | Content feels cramped → lower trust | Add 80–120px section padding |
