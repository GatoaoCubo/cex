---
id: bld_instruction_landing_page
kind: instruction
pillar: P03
builder: landing-page-builder
version: 1.0.0
quality: 9.0
title: "Instruction Landing Page"
author: n03_builder
tags: [landing_page, builder, examples]
tldr: "Golden and anti-examples for landing page construction, demonstrating ideal structure and common pitfalls."
domain: "landing page construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: REASON
related:
  - kc_landing_page
  - bld_system_prompt_landing_page
  - bld_architecture_landing_page
  - landing-page-builder
  - bld_schema_landing_page
  - bld_quality_gate_landing_page
  - bld_knowledge_card_landing_page
  - bld_examples_landing_page
  - spec_n02_part2
  - p03_sp_visual_frontend_marketing
---
# Instruction: Landing Page Construction Pipeline

## Steps
1. **BRIEF** — Gather: brand_config OR user input (product, audience, goal, tone, stack preference)
2. **STRUCTURE** — Choose section order based on goal:
   - SaaS product: HERO > FEATURES > SOCIAL-PROOF > PRICING > FAQ > CTA
   - Service/Agency: HERO > PROBLEM > SOLUTION > HOW-IT-WORKS > TESTIMONIALS > CTA
   - Course/Infoproduct: HERO > PROBLEM > TRANSFORMATION > MODULES > PRICING > FAQ > CTA > GUARANTEE
   - Portfolio: HERO > WORK > ABOUT > TESTIMONIALS > CONTACT
3. **DESIGN TOKENS** — Extract from brand_config or define:
   - Colors: primary, secondary, accent, bg, text, muted
   - Fonts: heading (display), body (sans), mono
   - Spacing: section padding, component gaps
   - Border radius, shadow depth
4. **BUILD** — Generate each section as a self-contained block:
   - Each section has: id, aria-label, responsive classes, CTA or interaction
   - Use Tailwind utility classes (no costm CSS unless unavoidable)
   - shadcn/ui components for interactive elements (accordion, dialog, tabs)
5. **ASSEMBLE** — Combine into single file with:
   - DOCTYPE, html lang, head (meta, fonts, Tailwind CDN), body
   - Smooth scroll, scroll-margin for anchored nav
   - JS: mobile menu toggle, FAQ accordion, scroll animations (IntersectionObserver)
6. **OPTIMIZE** — Add:
   - Open Graph meta tags (title, description, image, url)
   - JSON-LD structured data (Organization or Product)
   - GTM/GA4 data attributes on CTAs
   - Lazy loading on below-fold images
   - Print stylesheet basics
7. **VALIDATE** — Check:
   - All 12 sections present (or justified omission)
   - Mobile responsive (no horizontal scroll)
   - All CTAs have href or onclick
   - All images have alt text
   - Color contrast passes WCAG AA

## Stack Options
| Stack | When | Output |
|-------|------|--------|
| HTML + Tailwind CDN | Default, zero build | Single .html file |
| React + Tailwind | User has React project | .tsx component |
| Next.js App Router | User has Next.js | page.tsx + layout.tsx |
| Astro | User wants static | .astro page |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_landing_page]] | upstream | 0.40 |
| [[bld_system_prompt_landing_page]] | related | 0.38 |
| [[bld_architecture_landing_page]] | downstream | 0.38 |
| [[landing-page-builder]] | downstream | 0.38 |
| [[bld_schema_landing_page]] | downstream | 0.33 |
| [[bld_quality_gate_landing_page]] | downstream | 0.33 |
| [[bld_knowledge_card_landing_page]] | upstream | 0.29 |
| [[bld_examples_landing_page]] | upstream | 0.29 |
| [[spec_n02_part2]] | downstream | 0.27 |
| [[p03_sp_visual_frontend_marketing]] | related | 0.25 |
