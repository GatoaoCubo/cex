---
kind: knowledge_card
id: bld_knowledge_card_model_card
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for model_card production — atomic searchable facts
sources: model-card-builder MANIFEST.md + SCHEMA.md, Mitchell 2019, LiteLLM, HuggingFace
quality: 9.1
title: "Knowledge Card Model Card"
version: "1.0.0"
author: n03_builder
tags: [model_card, builder, examples]
tldr: "Golden and anti-examples for model card construction, demonstrating ideal structure and common pitfalls."
domain: "model card construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_ins_model_card
  - bld_memory_model_card
  - p03_sp_model_card_builder
  - model-card-builder
  - bld_collaboration_model_card
  - p06_bp_model_card
  - bld_schema_model_card
  - p11_qg_model_card
  - bld_knowledge_card_model_provider
  - bld_config_model_card
---

# Domain Knowledge: model_card
## Executive Summary
Model cards are technical specification artifacts for LLMs — they encode pricing, context limits, capability booleans, and use-case guidance into a structured, sourced document. Every specification row must cite a source URL; no self-scoring at creation. They differ from benchmarks (which measure performance), boot configs (which configure runtime), and agents (which define capabilities) by being static reference specs used for model selection and comparison.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P02 (design-time spec) |
| Kind | `model_card` (exact literal) |
| ID pattern | `p02_mc_{provider}_{model_slug}` |
| Required frontmatter | 26 fields |
| Quality gates | 10 HARD + 15 SOFT |
| Max body | 4096 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Domain field | always `model_selection` |
| Modalities | 5 booleans (text_input, text_output, image_input, audio_input, pdf_input) |
| Features | 8 booleans (tool_calling, structured_output, reasoning, etc.) |
| Min When-to-Use rows | 5 |
| Provider enum | anthropic, openai, google, meta, mistral, cohere, deepseek, alibaba, ai21, other |
## Patterns
| Pattern | Application |
|---------|-------------|
| Pricing normalization | Per 1M tokens, USD; `null` for open-weight, `0.00` for free-tier |
| Capability booleans | Always true/false, never string or null |
| Sourced specifications | Every spec row MUST have a source URL — never `-` |
| Identity/Capability/Economics split | Immutable identity, mutable capabilities, volatile pricing |
| Status lifecycle | active -> deprecated -> sunset |
| Freshness gate | 90 days (providers update pricing/features quarterly) |
| Tiered pricing | Lowest tier in frontmatter; document higher tiers in body |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Pricing `0` for open-weight model | Must be `null`; 0 implies free API |
| Spec row without source URL | Fails HARD gate — every row needs citation |
| Modality as string "yes"/"no" | Must be boolean true/false |
| `domain: llm` | Must be literal `model_selection` |
| Self-assigned quality score | `quality` must be null |
| When-to-Use table with < 5 rows | Fails HARD gate — insufficient guidance |
| Capability as prose paragraph | Must be structured boolean fields |
## Application
1. Set `id: p02_mc_{provider}_{model_slug}` — must equal filename stem
2. Populate all 26 required frontmatter fields; set `quality: null`
3. Set `pricing`: base tier per 1M tokens; `null` for open-weight
4. Fill `modalities` (5 booleans) and `features` (8 booleans) from official docs
5. Write `## Specifications` table with Value + Source URL per row
6. Write `## When to Use` decision table with >= 5 rows
7. Validate: body <= 4096 bytes, all specs sourced, 10 HARD + 15 SOFT gates
## References
- model-card-builder SCHEMA.md v2.0.0
- Mitchell et al. 2019 "Model Cards for Model Reporting"
- HuggingFace Model Cards documentation
- LiteLLM model registry (2593 models)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_model_card]] | downstream | 0.51 |
| [[bld_memory_model_card]] | downstream | 0.42 |
| [[p03_sp_model_card_builder]] | downstream | 0.41 |
| [[model-card-builder]] | downstream | 0.37 |
| [[bld_collaboration_model_card]] | downstream | 0.35 |
| [[p06_bp_model_card]] | downstream | 0.34 |
| [[bld_schema_model_card]] | downstream | 0.34 |
| [[p11_qg_model_card]] | downstream | 0.33 |
| [[bld_knowledge_card_model_provider]] | sibling | 0.33 |
| [[bld_config_model_card]] | downstream | 0.32 |
