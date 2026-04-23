---
id: bld_context_sources_data_contract
kind: rag_source
pillar: P10
llm_function: CONSTRAIN
version: 1.0.0
quality: 8.1
tags: [data_contract, context, rag]
title: "Context Sources: data_contract"
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_collaboration_validation_schema
  - bld_collaboration_input_schema
  - bld_architecture_kind
  - bld_tools_kind
  - bld_instruction_kind
  - p10_lr_kind_builder
  - bld_collaboration_kind
  - validation-schema-builder
  - kind-builder
  - bld_output_template_kind
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

## Configuration Checklist

- Verify all required fields are present in frontmatter before saving
- Validate config values against schema constraints (type, range, enum)
- Cross-reference with related configs to avoid contradictions
- Test config loading in target runtime before committing

## Validation

```yaml
# Required config validation
fields_present: true
types_valid: true
ranges_checked: true
cross_refs_verified: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope {BUILDER}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_validation_schema]] | upstream | 0.26 |
| [[bld_collaboration_input_schema]] | downstream | 0.25 |
| [[bld_architecture_kind]] | upstream | 0.25 |
| [[bld_tools_kind]] | upstream | 0.23 |
| [[bld_instruction_kind]] | upstream | 0.22 |
| [[p10_lr_kind_builder]] | related | 0.20 |
| [[bld_collaboration_kind]] | downstream | 0.20 |
| [[validation-schema-builder]] | upstream | 0.19 |
| [[kind-builder]] | upstream | 0.18 |
| [[bld_output_template_kind]] | upstream | 0.18 |
