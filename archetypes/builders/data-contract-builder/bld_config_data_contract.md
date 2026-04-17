---
id: bld_context_sources_data_contract
kind: rag_source
pillar: P10
llm_function: INJECT
version: 1.0.0
quality: null
tags: [data_contract, context, rag]
title: "Context Sources: data_contract"
---
# Context Sources: data_contract
## Mandatory Sources (load at F3 INJECT)
| Source | Path | Why |
|--------|------|-----|
| Kind KC | N00_genesis/P01_knowledge/library/kind/kc_data_contract.md | Definition + boundary |
| Schema | archetypes/builders/data-contract-builder/bld_schema_data_contract.md | Required fields |
| Examples | archetypes/builders/data-contract-builder/bld_examples_data_contract.md | Golden patterns |

## Optional Sources (load if relevant)
| Source | Path | When to Load |
|--------|------|-------------|
| domain_event KC | N00_genesis/P01_knowledge/library/kind/kc_domain_event.md | If contract formalizes event schema |
| bounded_context KC | N00_genesis/P01_knowledge/library/kind/kc_bounded_context.md | BC boundary context |
| Existing contracts | {nucleus}/P06_*/dc_*.md | Consistency with existing agreements |

## Search Queries for Retrieval
- "data contract producer consumer schema SLA"
- "DDD published language bounded context"
- "schema registry Avro Protobuf contract"
- "consumer-driven contract testing Pact"

## Anti-Sources (do NOT confuse with)
- validation_schema (LLM output validation, not cross-system contract)
- dataset_card (data asset metadata, not exchange agreement)
- input_schema (single system, not cross-boundary)
