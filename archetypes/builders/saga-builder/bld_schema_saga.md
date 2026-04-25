---
quality: 8.1
quality: 7.7
id: bld_schema_saga
kind: schema
pillar: P06
llm_function: CONSTRAIN
purpose: "Formal schema -- SINGLE SOURCE OF TRUTH for saga"
title: "Schema: saga"
version: "1.0.0"
author: builder
tags: [schema, saga, P12]
domain: "distributed orchestration"
created: "2026-04-17"
updated: "2026-04-17"
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for saga"
density_score: null
related:
  - bld_schema_quickstart_guide
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - bld_schema_usage_report
  - bld_schema_search_strategy
  - bld_schema_pitch_deck
  - bld_schema_benchmark_suite
  - bld_schema_dataset_card
  - bld_schema_sandbox_spec
  - bld_schema_sandbox_config
---

# Schema: saga

## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p12_saga_{name_slug}) | YES | - | Namespace compliance |
| kind | literal "saga" | YES | - | Type integrity |
| pillar | literal "P12" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Version |
| saga_name | string | YES | - | Business transaction name |
| steps_count | integer | YES | - | Must match step list |
| topology | enum: choreography, orchestration | YES | orchestration | Coordination style |
| on_failure | enum: compensate_all, compensate_partial, abort | YES | compensate_all | Saga-level failure policy |
| domain | string | YES | - | Business domain |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "saga" |
| tldr | string <= 160ch | YES | - | Dense summary |
| created | date YYYY-MM-DD | YES | - | Creation date |

## ID Pattern
Regex: `^p12_saga_[a-z][a-z0-9_]+$`

## Body Structure (required sections)
1. `## Goal` -- one-sentence business transaction outcome
2. `## Steps` -- table: id, participant, action, compensating_action, on_failure
3. `## Rollback Sequence` -- ordered list of compensating actions on failure
4. `## Topology` -- choreography or orchestration, with participant diagram

## Constraints
- max_bytes: 4096
- naming: p12_saga_{name_slug}.md
- EVERY step MUST have compensating_action (non-empty)
- steps_count MUST match actual step count
- quality: null always

## Schema Validation Checklist

- Verify all required fields have type annotations
- Validate enum values against domain vocabulary
- Cross-reference with related schemas for consistency
- Test schema parsing with sample data before publishing

## Schema Pattern

```yaml
# Schema validation contract
types_annotated: true
enums_valid: true
cross_refs_checked: true
sample_data_tested: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_schema_hydrate.py --check
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_quickstart_guide]] | sibling | 0.65 |
| [[bld_schema_reranker_config]] | sibling | 0.64 |
| [[bld_schema_integration_guide]] | sibling | 0.64 |
| [[bld_schema_usage_report]] | sibling | 0.64 |
| [[bld_schema_search_strategy]] | sibling | 0.62 |
| [[bld_schema_pitch_deck]] | sibling | 0.62 |
| [[bld_schema_benchmark_suite]] | sibling | 0.62 |
| [[bld_schema_dataset_card]] | sibling | 0.61 |
| [[bld_schema_sandbox_spec]] | sibling | 0.60 |
| [[bld_schema_sandbox_config]] | sibling | 0.60 |
