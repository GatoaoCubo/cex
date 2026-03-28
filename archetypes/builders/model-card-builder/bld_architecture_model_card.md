---
kind: architecture
id: bld_architecture_model_card
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of model_card — inventory, dependencies, and architectural position
---

# Architecture: model_card in the CEX

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 26-field metadata header (id, kind, pillar, provider, model_id, etc.) | model-card-builder | active |
| capabilities_table | Boolean feature matrix (vision, function_calling, streaming, etc.) | author | active |
| pricing_block | Normalized cost per million tokens (input/output/cached) | author | active |
| context_window | Maximum token capacity and effective context details | author | active |
| provider_info | API provider, endpoints, authentication requirements | author | active |
| limitations | Known weaknesses, failure modes, and unsupported scenarios | author | active |
| recommended_uses | Optimal use cases matched to model strengths | author | active |

## Dependency Graph

```
provider_docs  --produces-->  model_card  --consumed_by-->  boot_config
model_card     --consumed_by-->  agent     --referenced_by-> router
model_card     --signals-->      cost_estimate
```

| From | To | Type | Data |
|------|----|------|------|
| provider_docs (external) | model_card | data_flow | official specs, pricing, and capability data |
| model_card | boot_config (P02) | consumes | model selection parameters for agent configuration |
| model_card | agent (P02) | data_flow | capability awareness for task feasibility checks |
| model_card | router (P02) | data_flow | model capabilities inform routing decisions |
| model_card | cost_estimate | produces | token cost projection for budget planning |
| rag_source (P01) | model_card | dependency | external documentation URLs tracked for freshness |

## Boundary Table

| model_card IS | model_card IS NOT |
|---------------|-------------------|
| A technical specification of an LLM with concrete data | An agent identity or persona definition (agent P02) |
| Pricing normalized per million tokens for comparison | A boot-time configuration for a specific satellite (boot_config P02) |
| Feature matrix with boolean capability flags | A routing decision tree (mental_model P02) |
| Provider-specific with API endpoint details | A performance benchmark with measured results (benchmark P07) |
| Updated when provider releases new model versions | A static document — must track provider changes |
| Scoped to one model version from one provider | A comparison table of multiple models |

## Layer Map

| Layer | Components | Purpose |
|-------|------------|---------|
| Source | provider_docs, rag_source | Official documentation and tracking URLs |
| Identity | frontmatter, provider_info | Model name, version, provider, and API details |
| Specification | capabilities_table, context_window, pricing_block | Technical specs, features, and cost data |
| Guidance | recommended_uses, limitations | Optimal and suboptimal usage patterns |
| Consumers | boot_config, agent, router | Systems that select and configure models |
