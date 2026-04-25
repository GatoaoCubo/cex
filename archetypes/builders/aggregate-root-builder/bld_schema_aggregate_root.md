---
id: bld_schema_aggregate_root
kind: schema
pillar: P06
title: "Aggregate Root Builder -- Schema"
version: 1.0.0
quality: 8.0
tags: [builder, aggregate_root, schema]
llm_function: CONSTRAIN
author: builder
tldr: "Aggregate Root schema: data contract, field types, and validation rules"
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_schema_model_registry
  - bld_schema_experiment_tracker
  - n06_schema_brand_config
  - bld_schema_training_method
  - bld_schema_input_schema
  - bld_schema_prompt_compiler
  - bld_schema_enum_def
  - bld_schema_retriever_config
  - bld_schema_multimodal_prompt
  - bld_schema_benchmark_suite
---
# Schema: aggregate_root
## Frontmatter Fields
### Required
| Field | Type | Notes |
|-------|------|-------|
| id | string `p06_ar_{slug}` | namespace + slug |
| kind | literal `aggregate_root` | type integrity |
| pillar | literal `P06` | pillar assignment |
| title | string | human label |
| version | semver | versioning |
| bounded_context | string | which domain context owns this |
| invariants | list[string] | at least 2 concrete rules |
| commands | list[string] | allowed mutations |
| domain_events | list[string] | emitted facts |
| repository | string | persistence interface name |
| quality | null | never self-score |
| tags | list[string] >= 3 | searchability |
| tldr | string <= 160ch | dense summary |
### Recommended
| Field | Type | Notes |
|-------|------|-------|
| cluster_members | list[string] | entities + value_objects inside boundary |
| identity_type | string | UUID, natural key, surrogate |
| concurrency_strategy | enum(optimistic, pessimistic, none) | conflict resolution |
| linked_artifacts | object | cross-references |
## ID Pattern
Regex: `^p06_ar_[a-z][a-z0-9_]+$`
## Body Structure
1. `## Identity` -- root entity, bounded context, cluster members
2. `## Invariants` -- numbered hard rules, each concrete and measurable
3. `## Commands` -- mutations with pre/postconditions
4. `## Domain Events` -- emitted facts with payloads
5. `## Repository` -- find_by_id + save interface only
6. `## Boundaries` -- inside vs outside the aggregate
## Constraints
- max_bytes: 4096
- naming: p06_ar_{slug}.md
- other aggregates referenced by ID only, never object
- at least 2 invariants required
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
| [[bld_schema_model_registry]] | sibling | 0.49 |
| [[bld_schema_experiment_tracker]] | sibling | 0.44 |
| [[n06_schema_brand_config]] | related | 0.40 |
| [[bld_schema_training_method]] | sibling | 0.40 |
| [[bld_schema_input_schema]] | sibling | 0.39 |
| [[bld_schema_prompt_compiler]] | sibling | 0.39 |
| [[bld_schema_enum_def]] | sibling | 0.38 |
| [[bld_schema_retriever_config]] | sibling | 0.37 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.37 |
| [[bld_schema_benchmark_suite]] | sibling | 0.37 |
