---
id: bld_collaboration_landing_page
kind: collaboration
pillar: P12
builder: landing-page-builder
version: 1.0.0
quality: 9.0
title: "Collaboration Landing Page"
author: n03_builder
tags: [landing_page, builder, examples]
tldr: "Golden and anti-examples for landing page construction, demonstrating ideal structure and common pitfalls."
domain: "landing page construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: COLLABORATE
---
# Collaboration: Landing Page Builder

## Upstream (receives from)
1. brand_config.yaml → colors, fonts, tone, logo URL
2. tagline-builder → hero headline, sub-headline, CTA text
3. content-monetization-builder → pricing tiers, feature lists
4. N01 Research → competitor page analysis, market positioning
5. N06 Commercial → pricing strategy, conversion goals

## Downstream (sends to)
1. N05 Operations → deployment (Vercel, Netlify, S3, GitHub Pages)
2. social-publisher-builder → Open Graph previews for social sharing
3. N02 Marketing → campaign landing pages, A/B variants
4. N04 Knowledge → page templates added to knowledge library

## Crew Behavior
1. In a crew, landing-page-builder runs LATE (needs tagline, pricing, brand tokens first)
2. Consumes outputs from tagline-builder and content-monetization-builder
3. Produces a DEPLOYABLE artifact, not a design spec
4. If A/B testing requested, produces 2 variants with clear differentiators

## Metadata

```yaml
id: bld_collaboration_landing_page
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-collaboration-landing-page.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `collaboration` |
| Pillar | P12 |
| Domain | landing page construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
