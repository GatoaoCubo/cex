---
id: bld_schema_landing_page
kind: schema
pillar: P06
builder: landing-page-builder
version: 1.0.0
quality: 9.1
title: "Schema Landing Page"
author: n03_builder
tags: [landing_page, builder, examples]
tldr: "Golden and anti-examples for landing page construction, demonstrating ideal structure and common pitfalls."
domain: "landing page construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: CONSTRAIN
related:
  - bld_schema_tagline
  - bld_schema_model_registry
  - bld_schema_experiment_tracker
  - bld_config_landing_page
  - n06_schema_brand_config
  - bld_output_template_landing_page
  - landing-page-builder
  - bld_schema_training_method
  - bld_schema_model_architecture
  - bld_schema_multimodal_prompt
---
# Schema: Landing Page Output

```yaml
# Required frontmatter
id: string               # unique landing page artifact id
kind: landing_page
pillar: P05
title: string            # page title (also <title> tag)
version: string
created: date
author: string
quality: null            # never self-score
tags: [landing-page, ...]
stack: enum[html-tailwind, react, nextjs, astro]
sections_count: integer  # number of sections
responsive: true
dark_mode: true
a11y: AA

# Body: the actual code
# Single HTML file OR component file(s)

# Metadata block (in frontmatter or separate)
seo:
  title: string
  description: string    # max 160 chars
  og_image: string       # Open Graph image URL
  canonical: string
  json_ld_type: enum[Organization, Product, SoftwareApplication, Course]

design_tokens:
  colors: {primary, secondary, accent, bg, text, muted}
  fonts: {heading, body, mono}
  radius: string
  shadow: string

sections:
  - id: string
    type: enum[hero, problem, solution, features, social-proof, how-it-works, pricing, testimonials, faq, cta, footer, meta]
    has_cta: boolean
    responsive: boolean
```

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Properties

| Property | Value |
|----------|-------|
| Kind | `schema` |
| Pillar | P06 |
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
| [[bld_schema_tagline]] | sibling | 0.47 |
| [[bld_schema_model_registry]] | sibling | 0.43 |
| [[bld_schema_experiment_tracker]] | sibling | 0.40 |
| [[bld_config_landing_page]] | related | 0.40 |
| [[n06_schema_brand_config]] | related | 0.38 |
| [[bld_output_template_landing_page]] | upstream | 0.38 |
| [[landing-page-builder]] | upstream | 0.37 |
| [[bld_schema_training_method]] | sibling | 0.35 |
| [[bld_schema_model_architecture]] | sibling | 0.34 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.34 |
