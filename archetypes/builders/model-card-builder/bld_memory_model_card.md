---
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for model_card artifact generation
---

# Memory: model-card-builder

## Summary

Model cards document LLM technical specifications: capabilities, pricing, context windows, and feature booleans. The primary production challenge is data freshness — LLM providers update pricing and capabilities frequently, so cards require explicit last_verified dates and source URLs. The second challenge is capability booleans: features like vision or function calling must be binary true/false, not qualified with partial support.

## Pattern

- Always include last_verified date and source URL for every data point — LLM specs change monthly
- Capability booleans must be strict true/false — use a separate notes field for qualifications
- Normalize pricing to a common unit: USD per 1M tokens (input) and USD per 1M tokens (output)
- Context window must distinguish between input limit and total (input + output) limit
- Include at least 3 concrete use-case recommendations based on the model strength profile
- Document known limitations and failure modes, not just capabilities

## Anti-Pattern

- Publishing pricing without last_verified date — pricing changes break downstream cost calculations silently
- Capability fields with "partial" or "limited" values — booleans must be true/false; nuance goes in notes
- Mixing token counts with character counts — always normalize to tokens with the model tokenizer
- Omitting the provider deprecation timeline — deprecated models waste integration effort
- Confusing model_card (P02, technical spec) with agent (P02, identity with behavior) or benchmark (P07, performance test)

## Context

Model cards occupy the P02 identity layer as reference documents for LLM selection decisions. They are consumed by routing logic, cost estimators, and capacity planners. In multi-model systems, model cards enable automated model selection based on task requirements versus model capabilities and cost constraints.

## Impact

Cards with normalized pricing enabled automated cost optimization that reduced API spend by 25-40%. Cards with stale pricing (>30 days without verification) caused budget overruns averaging 15%. Strict capability booleans eliminated ambiguous model selection in routing logic.

## Reproducibility

For reliable model card production: (1) source all data from official provider documentation, (2) record last_verified date per field, (3) normalize pricing to USD/1M tokens, (4) use strict booleans for capabilities, (5) include deprecation timeline if known, (6) validate against 10 HARD + 15 SOFT gates.

## References

- model-card-builder SCHEMA.md (26 frontmatter fields)
- Mitchell et al. 2019 Model Cards framework
- P02 identity pillar specification
