---
id: n00_model_card_manifest
kind: knowledge_card
8f: F3_inject
pillar: P02
nucleus: n00
title: "Model Card -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, model_card, p02, n00, archetype, template]
density_score: 1.0
updated: "2026-04-17"
related:
  - bld_schema_reranker_config
  - bld_schema_model_provider
  - bld_schema_usage_report
  - bld_schema_thinking_config
  - bld_schema_dataset_card
  - bld_schema_integration_guide
  - bld_schema_context_window_config
  - bld_schema_search_strategy
  - bld_schema_quickstart_guide
  - bld_schema_benchmark_suite
---

<!-- 8F: F1=knowledge_card P02 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Model Card documents the operational specification of an LLM in use: pricing per token, context window size, capabilities, known limitations, and deployment constraints. It governs provider selection in the 8F pipeline (F1 CONSTRAIN) and informs cost planning. Every nucleus model assignment should reference a model_card.

## Pillar
P02 -- Model

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `model_card` |
| pillar | string | yes | Always `P02` |
| title | string | yes | Model name and provider |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| model_id | string | yes | Provider model identifier |
| provider | string | yes | Anthropic, OpenAI, Google, Ollama, etc. |
| context_window | int | yes | Maximum context in tokens |
| input_cost_per_1m | float | yes | USD cost per 1M input tokens |
| output_cost_per_1m | float | yes | USD cost per 1M output tokens |
| capabilities | list | yes | Supported features (tools, vision, etc.) |
| tier | enum | yes | opus\|sonnet\|haiku\|local -- quality tier |

## When to use
- When documenting a new LLM for use in CEX routing
- When updating pricing or capability information for existing models
- When selecting a model for a specific nucleus or task

## Builder
`archetypes/builders/model_card-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind model_card --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- operators and cost planners
- `{{DOMAIN_CONTEXT}}` -- deployment environment and budget constraints

## Example (minimal)
```yaml
---
id: model_card_claude_sonnet_4_6
kind: model_card
pillar: P02
nucleus: n07
title: "Claude Sonnet 4.6"
version: 1.0
quality: null
---
model_id: claude-sonnet-4-6
provider: Anthropic
context_window: 200000
input_cost_per_1m: 3.0
output_cost_per_1m: 15.0
capabilities: [tools, vision, prompt-caching, extended-thinking]
tier: sonnet
```

## Related kinds
- `model_provider` (P02) -- provider adapter this model belongs to
- `fallback_chain` (P02) -- routing chains that reference this model
- `model_architecture` (P02) -- underlying architecture documentation

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | downstream | 0.47 |
| [[bld_schema_model_provider]] | downstream | 0.46 |
| [[bld_schema_usage_report]] | downstream | 0.45 |
| [[bld_schema_thinking_config]] | downstream | 0.44 |
| [[bld_schema_dataset_card]] | downstream | 0.44 |
| [[bld_schema_integration_guide]] | downstream | 0.44 |
| [[bld_schema_context_window_config]] | downstream | 0.44 |
| [[bld_schema_search_strategy]] | downstream | 0.43 |
| [[bld_schema_quickstart_guide]] | downstream | 0.43 |
| [[bld_schema_benchmark_suite]] | downstream | 0.43 |
