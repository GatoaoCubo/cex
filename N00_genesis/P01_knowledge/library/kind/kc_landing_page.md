---
id: kc_landing_page
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "KC: Landing Page"
version: 1.0.0
created: 2026-04-06
author: n07_orchestrator
quality: 9.0
tags: [knowledge-card, landing-page, frontend, ui, marketing, conversion]
density_score: 1.0
updated: "2026-04-07"
domain: "knowledge management"
aliases: ["sales page", "squeeze page", "conversion page", "marketing page", "lead capture page"]
user_says: ["make me a landing page", "criar landing page", "build a website", "I need a page to sell my product", "create a sales page"]
long_tails: ["I need a website to sell my product with pricing and testimonials", "create a conversion-optimized page to capture leads", "build a responsive landing page with hero section and CTA", "make a marketing page for my SaaS product launch"]
cross_provider:
  lovable: "Page component"
  v0: "UI generation"
  framer: "Landing page template"
  webflow: "Landing page"
  bolt: "Full-stack page"
  astro: "Astro page component"
related:
  - bld_knowledge_card_landing_page
  - landing-page-builder
  - bld_architecture_landing_page
  - bld_instruction_landing_page
  - bld_system_prompt_landing_page
  - bld_collaboration_landing_page
  - bld_schema_landing_page
  - bld_tools_landing_page
  - bld_memory_landing_page
  - landing_page_template
---
# Knowledge Card: landing_page

## Definition
A **landing page** is a standalone, production-ready web page designed for a single
conversion goal. Built with HTML+Tailwind (zero build step) or React/Next.js/Astro.
12 sections: HERO > PROBLEM > SOLUTION > FEATURES > SOCIAL-PROOF > HOW-IT-WORKS >
PRICING > TESTIMONIALS > FAQ > CTA > FOOTER > META.

## Builder
`landing-page-builder` (13 ISOs) — Pillar P05

## What Makes It Different
Unlike Lovable/Bolt/v0/Framer/Webflow:
- **You own the code** — no platform lock-in
- **Zero build step** — HTML+Tailwind CDN deploys anywhere
- **Conversion-optimized** — CRO baked into every section
- **Brand-injectable** — {{BRAND_*}} placeholders for any client
- **Production-ready** — responsive, dark mode, SEO, a11y, analytics hooks

## Stack Options
| Stack | Build | Best For |
|-------|-------|----------|
| HTML + Tailwind CDN | None | Quick pages, non-devs |
| React + Tailwind | npm | Existing React apps |
| Next.js App Router | next | SEO-critical, SSR |
| Astro | astro | Multi-page, content |

## Section Psychology
Hero=hook, Problem=empathy, Solution=relief, Features=logic,
Social-Proof=trust, Pricing=decision, FAQ=objection-clearing, CTA=conversion.

## Relations
- Consumes: tagline-builder (hero headline)
- Consumes: content-monetization-builder (pricing tiers)
- Consumes: brand_config.yaml (design tokens)
- Feeds into: N05 deploy pipeline, N02 campaign pages

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `kc_landing_page`
- **Tags**: [knowledge-card, landing-page, frontend, ui, marketing, conversion]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_landing_page]] | sibling | 0.56 |
| [[landing-page-builder]] | downstream | 0.53 |
| [[bld_architecture_landing_page]] | downstream | 0.40 |
| [[bld_instruction_landing_page]] | downstream | 0.39 |
| [[bld_system_prompt_landing_page]] | downstream | 0.39 |
| [[bld_collaboration_landing_page]] | downstream | 0.38 |
| [[bld_schema_landing_page]] | downstream | 0.36 |
| [[bld_tools_landing_page]] | downstream | 0.35 |
| [[bld_memory_landing_page]] | downstream | 0.31 |
| [[landing_page_template]] | downstream | 0.29 |
