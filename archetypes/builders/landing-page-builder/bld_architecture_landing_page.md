---
id: bld_architecture_landing_page
kind: architecture
pillar: P08
builder: landing-page-builder
version: 1.0.0
quality: 9.1
title: "Architecture Landing Page"
author: n03_builder
tags: [landing_page, builder, examples]
tldr: "Golden and anti-examples for landing page construction, demonstrating ideal structure and common pitfalls."
domain: "landing page construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: CONSTRAIN
related:
  - bld_collaboration_landing_page
  - landing-page-builder
  - kc_landing_page
  - bld_instruction_landing_page
  - bld_output_template_landing_page
  - bld_tools_landing_page
  - bld_knowledge_card_landing_page
  - bld_memory_landing_page
  - bld_system_prompt_landing_page
  - bld_schema_landing_page
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
1. brand_config.yaml (optional — design tokens fallback to defaults)
2. tagline-builder output (optional — hero headline)
3. No runtime dependencies for HTML output (zero-JS except interactions)

## Integration Points
1. tagline-builder → hero headline and sub-headline
2. social-publisher-builder → Open Graph meta for social sharing
3. content-monetization-builder → pricing section tiers
4. N02 Marketing → campaign-specific landing pages
5. N05 Operations → deploy pipeline (Vercel/Netlify/S3)

## Properties

| Property | Value |
|----------|-------|
| Kind | `architecture` |
| Pillar | P08 |
| Domain | landing page construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_landing_page]] | downstream | 0.43 |
| [[landing-page-builder]] | upstream | 0.39 |
| [[kc_landing_page]] | upstream | 0.38 |
| [[bld_instruction_landing_page]] | upstream | 0.37 |
| [[bld_output_template_landing_page]] | upstream | 0.36 |
| [[bld_tools_landing_page]] | upstream | 0.35 |
| [[bld_knowledge_card_landing_page]] | upstream | 0.35 |
| [[bld_memory_landing_page]] | downstream | 0.35 |
| [[bld_system_prompt_landing_page]] | upstream | 0.33 |
| [[bld_schema_landing_page]] | upstream | 0.30 |
