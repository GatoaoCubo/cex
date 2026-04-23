---
id: n02_kc_responsive_layout_systems
kind: knowledge_card
pillar: P01
title: Responsive Layout Systems
domain: N02_marketing / Frontend
tags: [css, grid, flexbox, responsive, mobile-first, typography, container-queries]
quality: 9.0
density_score: 1.0
source: every-layout.dev, css-tricks.com, web.dev/learn/css
created: 2026-04-01
related:
  - p06_schema_responsive_breakpoints
  - p01_kc_responsive_layouts
  - n06_output_pricing_page
  - kc_visual_hierarchy_principles
  - n02_kc_typography_web
  - p10_dtc_design_token_contract
  - p05_output_social_card
  - spec_n02_part2
  - p01_kc_typography_web
  - p05_output_email_template
---

# KC: Responsive Layout Systems

## Core Mental Model

Mobile-first: write base styles for small screens, use `min-width` queries to enhance.
Never use `max-width` as primary breakpoint strategy — it forces override-heavy CSS.

---

## CSS Grid

### Template Areas (semantic layouts)
```css
.layout {
  display: grid;
  grid-template-columns: 1fr min(65ch, 100%) 1fr;
  grid-template-rows: auto 1fr auto;
}

/* Named areas */
.page {
  display: grid;
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
  grid-template-columns: 280px 1fr;
  gap: 1.5rem;
}
```

### Auto-fill vs Auto-fit
```css
/* auto-fill: keeps empty columns */
grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));

/* auto-fit: collapses empty columns — preferred for card grids */
grid-template-columns: repeat(auto-fit, minmax(min(200px, 100%), 1fr));
```

### Intrinsic Sizing (Every Layout pattern)
```css
/* Stack: vertical rhythm */
.stack > * + * { margin-top: var(--space, 1.5rem); }

/* Center: horizontal centering with max-width */
.center {
  max-width: min(65ch, 100% - 3rem);
  margin-inline: auto;
}

/* Cluster: wrapping flex row */
.cluster {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space, 1rem);
  justify-content: flex-start;
  align-items: center;
}
```

---

## Flexbox

### Key Properties
```css
/* Parent */
.flex-parent {
  display: flex;
  flex-direction: row;       /* row | column | row-reverse | column-reverse */
  flex-wrap: wrap;           /* nowrap | wrap | wrap-reverse */
  justify-content: center;   /* flex-start | flex-end | center | space-between | space-around | space-evenly */
  align-items: stretch;      /* flex-start | flex-end | center | baseline | stretch */
  gap: 1rem;
}

/* Child */
.flex-child {
  flex: 1 1 200px;           /* grow shrink basis */
  flex-grow: 1;              /* how much to grow */
  flex-shrink: 0;            /* 0 = don't shrink below basis */
  flex-basis: auto;          /* initial size before grow/shrink */
  align-self: center;        /* override align-items for this child */
  order: 2;                  /* visual reorder (avoid for a11y) */
}
```

### Sidebar Pattern (Holy Grail)
```css
/* Sidebar breaks below viewport threshold */
.with-sidebar {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}
.sidebar { flex-basis: 280px; flex-grow: 1; }
.main-content { flex-basis: 0; flex-grow: 999; min-inline-size: 50%; }
```

---

## Mobile-First Breakpoints

### Breakpoint Strategy
```css
/* Base: mobile (no query) */
.component { padding: 1rem; }

/* Tablet */
@media (min-width: 48rem) {   /* 768px */
  .component { padding: 2rem; }
}

/* Desktop */
@media (min-width: 64rem) {   /* 1024px */
  .component { padding: 3rem; }
}

/* Wide */
@media (min-width: 90rem) {   /* 1440px */
  .component { max-width: 1280px; margin-inline: auto; }
}
```

### Tokens (avoid magic numbers)
```css
:root {
  --bp-sm: 30rem;    /* 480px */
  --bp-md: 48rem;    /* 768px */
  --bp-lg: 64rem;    /* 1024px */
  --bp-xl: 90rem;    /* 1440px */
}
```

---

## Fluid Typography

### clamp() — no media queries needed
```css
/* clamp(min, preferred, max) */
h1 { font-size: clamp(1.75rem, 4vw + 1rem, 3rem); }
h2 { font-size: clamp(1.5rem, 3vw + 0.75rem, 2.25rem); }
p  { font-size: clamp(1rem, 1.5vw + 0.5rem, 1.125rem); }

/* Fluid spacing */
.section { padding-block: clamp(3rem, 8vw, 8rem); }
```

### Typographic Scale
```css
:root {
  --font-xs:   clamp(0.75rem,  1vw + 0.5rem,  0.875rem);
  --font-sm:   clamp(0.875rem, 1.5vw + 0.5rem, 1rem);
  --font-base: clamp(1rem,     1.5vw + 0.5rem, 1.125rem);
  --font-lg:   clamp(1.125rem, 2vw + 0.5rem,   1.5rem);
  --font-xl:   clamp(1.5rem,   3vw + 0.75rem,  2.25rem);
  --font-2xl:  clamp(1.75rem,  4vw + 1rem,     3rem);
  --font-3xl:  clamp(2rem,     5vw + 1rem,     4rem);
}
```

---

## Container Queries

### Component-level responsiveness (no global breakpoints)
```css
/* Define container */
.card-wrapper {
  container-type: inline-size;
  container-name: card;
}

/* Query the container, not viewport */
@container card (min-width: 400px) {
  .card { flex-direction: row; }
  .card__image { width: 200px; flex-shrink: 0; }
}

@container card (min-width: 600px) {
  .card { gap: 2rem; }
}
```

### Size Units
```css
/* cqi = 1% of container inline size */
.card__title { font-size: clamp(1rem, 4cqi, 2rem); }
```

**Browser support**: 96%+ (2025). Use with confidence.

---

## Viewport Units

```css
/* Problem: 100vh includes browser chrome on mobile */
/* Solution: svh/dvh/lvh */

.hero {
  height: 100dvh;   /* dynamic: adjusts when browser UI shows/hides */
  height: 100svh;   /* small: always smallest viewport (safest) */
  height: 100lvh;   /* large: always largest viewport */
}

/* Horizontal: svw, dvw, lvw */
/* Inline/block logical: svi, dvi, lvi, svb, dvb, lvb */

/* Safe fallback */
.hero {
  height: 100vh;
  height: 100dvh;   /* overrides if supported */
}
```

---

## Responsive Images (srcset)

```html
<!-- Resolution switching -->
<img
  src="hero-800.jpg"
  srcset="hero-400.jpg 400w, hero-800.jpg 800w, hero-1200.jpg 1200w"
  sizes="(max-width: 48rem) 100vw,
         (max-width: 64rem) 80vw,
         1200px"
  alt="Hero"
  loading="lazy"
  decoding="async"
/>

<!-- Art direction (different crop per breakpoint) -->
<picture>
  <source media="(max-width: 48rem)" srcset="hero-mobile.jpg">
  <source media="(max-width: 64rem)" srcset="hero-tablet.jpg">
  <img src="hero-desktop.jpg" alt="Hero" />
</picture>
```

**Next.js / React:**
```jsx
import Image from 'next/image';
<Image src="/hero.jpg" alt="Hero" fill sizes="(max-width: 768px) 100vw, 50vw" />
```

---

## Touch Targets (a11y + mobile UX)

```css
/* WCAG 2.5.5: minimum 44x44px touch target */
.btn {
  min-height: 44px;
  min-width: 44px;
  padding: 0.75rem 1.25rem;
  touch-action: manipulation;  /* removes 300ms delay */
}

/* Expand hit area without changing visual size */
.icon-btn {
  position: relative;
}
.icon-btn::before {
  content: '';
  position: absolute;
  inset: -8px;
}

/* Spacing between touch targets: min 8px */
.nav-links { gap: 0.5rem; }
```

---

## Anti-Patterns

| Anti-Pattern | Problem | Fix |
|---|---|---|
| `max-width` breakpoints | Override-heavy | Use `min-width` mobile-first |
| Fixed px font sizes | Ignores user preferences | Use rem / clamp |
| `100vh` on mobile | Includes browser UI | Use `100dvh` |
| `display: none` for mobile | Still renders | CSS `content-visibility` or conditional rendering |
| No `gap` — using margins | Layout coupling | Use gap in flex/grid |
| Absolute breakpoints tied to devices | Devices change | Break when layout breaks |

---

## Checklist

- [ ] Mobile-first base styles (no media query)
- [ ] Breakpoints: 48rem, 64rem, 90rem min-width
- [ ] Font sizes use `clamp()` with rem units
- [ ] Container queries for component-level breakpoints
- [ ] Images use `srcset` + `sizes` + `loading="lazy"`
- [ ] Touch targets >= 44x44px
- [ ] `100dvh` for full-height sections
- [ ] `gap` instead of margin for spacing in flex/grid

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p06_schema_responsive_breakpoints]] | downstream | 0.72 |
| [[p01_kc_responsive_layouts]] | sibling | 0.55 |
| [[n06_output_pricing_page]] | downstream | 0.53 |
| [[kc_visual_hierarchy_principles]] | sibling | 0.42 |
| [[n02_kc_typography_web]] | sibling | 0.30 |
| [[p10_dtc_design_token_contract]] | downstream | 0.25 |
| [[p05_output_social_card]] | downstream | 0.23 |
| [[spec_n02_part2]] | downstream | 0.22 |
| [[p01_kc_typography_web]] | sibling | 0.21 |
| [[p05_output_email_template]] | downstream | 0.17 |
