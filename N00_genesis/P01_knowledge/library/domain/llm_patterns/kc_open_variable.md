---
id: p01_kc_open_variable
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Open Variable Pattern — Mustache Templating for LLM Systems"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: llm_patterns
quality: 9.0
tags: [open-variable, mustache, templating, brand, injection]
tldr: "Use {{VARIABLE}} placeholders in prompts and configs. Fill at runtime from context (brand, user, environment). Separates structure from content."
when_to_use: "Building multi-tenant or brand-aware LLM systems"
keywords: [open-variable, mustache, template, brand-injection, multi-tenant]
density_score: 0.92
updated: "2026-04-07"
related:
  - bld_knowledge_card_prompt_template
  - bld_memory_prompt_template
  - p03_sp_brand_nucleus
  - spec_n06_brand_verticalization
  - p01_kc_refinement
  - p01_kc_distillation_pipeline
  - p01_kc_prompt_template
  - p01_kc_anti_isolated_sessions
  - p03_ins_prompt_template
  - p01_kc_pattern_extraction
---

# Open Variable Pattern

## Core Concept
Separate structure from content. The template defines WHAT goes where. Variables define WHO/WHAT fills it. Runtime hydrates the template.

## The Pattern
```
TEMPLATE: "Welcome to {{BRAND_NAME}}. Our {{BRAND_ARCHETYPE}} voice says..."
CONFIG:   { BRAND_NAME: "Codexa", BRAND_ARCHETYPE: "sage" }
OUTPUT:   "Welcome to Codexa. Our sage voice says..."
```

## Hydration Sources

| Source | Variables | When |
|--------|-----------|------|
| Brand config | `{{BRAND_*}}` (41 vars) | Every prompt |
| Decision manifest | `{{DP_*}}` | Per-mission |
| Environment | `{{ENV_*}}` | Deploy-time |
| User input | `{{USER_*}}` | Per-request |

## CEX Implementation
1. `.cex/brand/brand_config_template.yaml` (41 mustache variables)
2. `brand_inject.py` hydrates prompts with brand values
3. `cex_schema_hydrate.py` hydrates schema templates
4. "X" in CEX is the ultimate open variable

## Quality Criteria

| Dimension | Requirement | Weight |
|-----------|------------|--------|
| Factual accuracy | Verifiable claims only | 0.25 |
| Atomicity | One concept per card | 0.20 |
| Actionability | Reader knows next steps | 0.20 |
| Density | No filler sentences | 0.20 |
| Searchability | Tags enable retrieval | 0.15 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_prompt_template]] | sibling | 0.26 |
| [[bld_memory_prompt_template]] | downstream | 0.26 |
| [[p03_sp_brand_nucleus]] | downstream | 0.25 |
| [[spec_n06_brand_verticalization]] | downstream | 0.25 |
| [[p01_kc_refinement]] | sibling | 0.25 |
| [[p01_kc_distillation_pipeline]] | sibling | 0.25 |
| [[p01_kc_prompt_template]] | sibling | 0.24 |
| [[p01_kc_anti_isolated_sessions]] | sibling | 0.23 |
| [[p03_ins_prompt_template]] | downstream | 0.23 |
| [[p01_kc_pattern_extraction]] | sibling | 0.23 |
