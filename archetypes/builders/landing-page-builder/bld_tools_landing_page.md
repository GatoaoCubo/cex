---
id: bld_tools_landing_page
kind: tools
pillar: P04
builder: landing-page-builder
version: 1.0.0
quality: 9.1
title: "Tools Landing Page"
author: n03_builder
tags: [landing_page, builder, examples]
tldr: "Golden and anti-examples for landing page construction, demonstrating ideal structure and common pitfalls."
domain: "landing page construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: CALL
---
# Tools: Landing Page Builder

## Required Tools
1. `brand_config_reader`: Read design tokens from .cex/brand/brand_config.yaml
2. `cex_query.py`: Find tagline-builder output, pricing data, brand artifacts
3. `cex_retriever.py`: Search existing page templates and design patterns

## Construction Tools (available in stack)
1. `browser_playwright`: Preview generated page, take screenshots, test responsive
2. `browser_design_extractor`: Extract design tokens from reference URLs
3. `computer_use`: Visual validation of rendered page (optional)

## Reference Tools
1. `browser_web_scraping`: Analyze competitor landing pages for inspiration
2. `browser_awesome_list`: Find design resources, icon sets, font pairings

## No Build Dependencies for HTML Output
Default HTML+Tailwind CDN output requires ZERO build tools. User saves file and deploys.
React/Next.js outputs require user's existing project setup.

## Tool Permissions
1. READ: brand config, existing artifacts, competitor pages, design resources
2. WRITE: output files only (landing page HTML/JSX + compiled YAML)
3. EXECUTE: preview tools (browser_playwright, browser_design_extractor)
4. DENY: no database writes, no deployment, no external API mutations

## Metadata

```yaml
id: bld_tools_landing_page
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-landing-page.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `tools` |
| Pillar | P04 |
| Domain | landing page construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
