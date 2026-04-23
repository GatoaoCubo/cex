---
id: bld_config_landing_page
kind: config
pillar: P06
builder: landing-page-builder
version: 1.0.0
effort: high
max_turns: 30
disallowed_tools: []
permission_scope: nucleus
quality: 9.1
title: "Config Landing Page"
author: n03_builder
tags: [landing_page, builder, examples]
tldr: "Golden and anti-examples for landing page construction, demonstrating ideal structure and common pitfalls."
domain: "landing page construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: CONSTRAIN
related:
  - bld_schema_landing_page
  - tpl_validation_schema
  - skill
  - landing-page-builder
  - bld_config_tagline
  - research_then_build
  - bld_tools_landing_page
  - bld_memory_landing_page
  - bld_output_template_landing_page
  - bld_collaboration_landing_page
---
# Config: Landing Page Builder

output_format: html
quality_floor: 8.5

defaults:
  stack: html-tailwind    # html-tailwind | react | nextjs | astro
  sections: 12
  mobile_first: true
  dark_mode: true
  tailwind_version: "3.4"
  font_provider: google-fonts
  image_placeholders: picsum
  analytics: gtm
  a11y_level: AA          # WCAG AA minimum

brand_injection:
  required: false
  fields: [BRAND_NAME, BRAND_COLORS, BRAND_FONTS, BRAND_TONE, BRAND_TAGLINE]
  fallback: generate_defaults

design_tokens:
  colors:
    primary: "#2563eb"    # blue-600
    secondary: "#7c3aed"  # violet-600
    accent: "#f59e0b"     # amber-500
    bg: "#ffffff"
    text: "#111827"       # gray-900
    muted: "#6b7280"      # gray-500
  fonts:
    heading: "Inter"
    body: "Inter"
    mono: "JetBrains Mono"
  radius: "0.5rem"
  shadow: "0 4px 6px -1px rgb(0 0 0 / 0.1)"

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_config_landing_page
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-landing-page.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
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
| [[bld_schema_landing_page]] | related | 0.52 |
| [[tpl_validation_schema]] | related | 0.43 |
| [[skill]] | downstream | 0.37 |
| [[landing-page-builder]] | upstream | 0.37 |
| [[bld_config_tagline]] | sibling | 0.36 |
| [[research_then_build]] | downstream | 0.36 |
| [[bld_tools_landing_page]] | upstream | 0.36 |
| [[bld_memory_landing_page]] | downstream | 0.34 |
| [[bld_output_template_landing_page]] | upstream | 0.32 |
| [[bld_collaboration_landing_page]] | downstream | 0.32 |
