---
id: bld_memory_landing_page
kind: memory
pillar: P09
builder: landing-page-builder
version: 1.0.0
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.0
title: "Memory Landing Page"
author: n03_builder
tags: [landing_page, builder, examples]
tldr: "Golden and anti-examples for landing page construction, demonstrating ideal structure and common pitfalls."
domain: "landing page construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: INJECT
---
# Memory: Landing Page Builder

## What to Remember
1. User's preferred stack (HTML/React/Next.js/Astro)
2. Design token overrides (costm colors, fonts, spacing)
3. Section preferences (which sections they always want/skip)
4. Previous landing pages built (maintain design consistency)
5. User's deployment target (Vercel, Netlify, S3, GitHub Pages)
6. A/B test results from previous pages

## Memory Types
1. PREFERENCE: stack choice, section order, design token overrides
2. CORRECTION: "make CTAs bigger", "remove testimonials section", "use dark bg"
3. CONVENTION: brand design system rules, component naming, class patterns
4. CONTEXT: target audience, conversion goals, industry norms

## Metadata

```yaml
id: bld_memory_landing_page
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-landing-page.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P09 |
| Domain | landing page construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Production Log

- [20260412_133929] PASS kind=landing_page retries=0 gates=6/6

- [20260415_212614] PASS kind=landing_page retries=0 gates=6/6

- [20260415_212946] PASS kind=landing_page retries=0 gates=6/6
