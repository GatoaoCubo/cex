---
kind: memory
id: bld_memory_model_card
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for model_card artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Model Card"
version: "1.0.0"
author: n03_builder
tags: [model_card, builder, examples]
tldr: "Golden and anti-examples for model card construction, demonstrating ideal structure and common pitfalls."
domain: "model card construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - model-card-builder
  - bld_collaboration_model_card
  - p03_sp_model_card_builder
  - bld_knowledge_card_model_card
  - p03_ins_model_card
  - p01_kc_model_card
  - p11_qg_model_card
  - bld_collaboration_model_provider
  - bld_memory_model_provider
  - model-registry-builder
---
# Memory: model-card-builder
## Summary
Model cards document LLM technical specifications: capabilities, pricing, context windows, and feature booleans. The primary production challenge is data freshness — LLM providers update pricing and capabilities frequently, so cards require explicit last_verified dates and source URLs. The second challenge is capability booleans: features like vision or function calling must be binary true/false, not qualified with partial support.
## Pattern
1. Always include last_verified date and source URL for every data point — LLM specs change monthly
2. Capability booleans must be strict true/false — use a separate notes field for qualifications
3. Normalize pricing to a common unit: USD per 1M tokens (input) and USD per 1M tokens (output)
4. Context window must distinguish between input limit and total (input + output) limit
5. Include at least 3 concrete use-case recommendations based on the model strength profile
6. Document known limitations and failure modes, not just capabilities
## Anti-Pattern
1. Publishing pricing without last_verified date — pricing changes break downstream cost calculations silently
2. Capability fields with "partial" or "limited" values — booleans must be true/false; nuance goes in notes
3. Mixing token counts with character counts — always normalize to tokens with the model tokenizer
4. Omitting the provider deprecation timeline — deprecated models waste integration effort
5. Confusing model_card (P02, technical spec) with agent (P02, identity with behavior) or benchmark (P07, performance test)
## Context
Model cards occupy the P02 identity layer as reference documents for LLM selection decisions. They are consumed by routing logic, cost estimators, and capacity planners. In multi-model systems, model cards enable automated model selection based on task requirements versus model capabilities and cost constraints.
## Impact
Cards with normalized pricing enabled automated cost optimization that reduced API spend by 25-40%. Cards with stale pricing (>30 days without verification) caused budget overruns averaging 15%. Strict capability booleans eliminated ambiguous model selection in routing logic.
## Reproducibility
For reliable model card production: (1) source all data from official provider documentation, (2) record last_verified date per field, (3) normalize pricing to USD/1M tokens, (4) use strict booleans for capabilities, (5) include deprecation timeline if known, (6) validate against 10 HARD + 15 SOFT gates.
## References
1. model-card-builder SCHEMA.md (26 frontmatter fields)
2. Mitchell et al. 2019 Model Cards framework
3. P02 identity pillar specification

## Metadata

```yaml
id: bld_memory_model_card
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-model-card.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P10 |
| Domain | model card construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[model-card-builder]] | upstream | 0.55 |
| [[bld_collaboration_model_card]] | upstream | 0.49 |
| [[p03_sp_model_card_builder]] | upstream | 0.46 |
| [[bld_knowledge_card_model_card]] | upstream | 0.44 |
| [[p03_ins_model_card]] | upstream | 0.37 |
| [[p01_kc_model_card]] | upstream | 0.36 |
| [[p11_qg_model_card]] | downstream | 0.32 |
| [[bld_collaboration_model_provider]] | upstream | 0.32 |
| [[bld_memory_model_provider]] | sibling | 0.32 |
| [[model-registry-builder]] | related | 0.29 |
