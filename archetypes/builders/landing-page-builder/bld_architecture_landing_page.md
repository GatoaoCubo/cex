---
id: bld_architecture_landing_page
kind: architecture
pillar: P08
builder: landing-page-builder
version: 1.0.0
---
# Architecture: Landing Page Builder

## Pipeline
```
BRIEF → STRUCTURE → DESIGN_TOKENS → BUILD(12 sections) → ASSEMBLE → OPTIMIZE(SEO+A11y+Perf) → VALIDATE
```

## Section Component Model
Each section is a self-contained block:
```
<section id="{name}" aria-label="{label}" class="py-16 md:py-24 {bg}">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    {content}
  </div>
</section>
```

## Stack Architecture
```
HTML + Tailwind CDN (default)
├── index.html (single file, everything inline)
├── Tailwind via CDN <script> (no build step)
├── Google Fonts via <link>
├── JS: inline <script> at bottom (menu, accordion, scroll)
└── Deploy: any static host (Vercel, Netlify, S3, GitHub Pages)

React + Tailwind (optional)
├── page.tsx (component)
├── components/ (Section components)
├── lib/design-tokens.ts
└── Deploy: Vercel, any React host

Next.js App Router (optional)
├── app/page.tsx
├── app/layout.tsx (fonts, metadata)
├── components/sections/
└── Deploy: Vercel
```

## Dependencies
- brand_config.yaml (optional — design tokens fallback to defaults)
- tagline-builder output (optional — hero headline)
- No runtime dependencies for HTML output (zero-JS except interactions)

## Integration Points
- tagline-builder → hero headline and sub-headline
- social-publisher-builder → Open Graph meta for social sharing
- content-monetization-builder → pricing section tiers
- N02 Marketing → campaign-specific landing pages
- N05 Operations → deploy pipeline (Vercel/Netlify/S3)
