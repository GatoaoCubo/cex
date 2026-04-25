---
quality: 8.1
quality: 7.7
id: bld_schema_lineage_record
kind: schema
pillar: P06
llm_function: CONSTRAIN
purpose: "Formal schema -- SINGLE SOURCE OF TRUTH for lineage_record"
title: "Schema: lineage_record"
version: "1.0.0"
author: builder
tags: [schema, lineage_record, P01]
domain: "knowledge provenance"
created: "2026-04-17"
updated: "2026-04-17"
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for lineage_record"
density_score: null
related:
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_integration_guide
  - bld_schema_quickstart_guide
  - bld_schema_search_strategy
  - bld_schema_pitch_deck
  - bld_schema_dataset_card
  - bld_schema_benchmark_suite
  - bld_schema_sandbox_config
  - bld_schema_sandbox_spec
---

# Schema: lineage_record

## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p01_lr_{name_slug}) | YES | - | Namespace compliance |
| kind | literal "lineage_record" | YES | - | Type integrity |
| pillar | literal "P01" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Version |
| target_artifact | string | YES | - | Artifact whose provenance is recorded |
| sources_count | integer | YES | - | Must match sources list |
| activities_count | integer | YES | - | Must match activities list |
| derivation_type | enum: wasDerivedFrom, wasGeneratedBy, wasQuotedFrom, wasRevisionOf | YES | wasDerivedFrom | Primary PROV-O relation |
| domain | string | YES | - | Knowledge domain |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "lineage_record" |
| tldr | string <= 160ch | YES | - | Dense summary |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |

## ID Pattern
Regex: `^p01_lr_[a-z][a-z0-9_]+$`

## Body Structure
1. `## Entities` -- table: id, type, location, retrieval_timestamp
2. `## Activities` -- table: id, label, used, generated, agent, timestamp
3. `## Agents` -- table: id, type, role
4. `## Derivation Relations` -- PROV-O triples in table or list

## Constraints
- max_bytes: 3072
- naming: p01_lr_{name_slug}.md
- sources_count and activities_count must match actual list lengths
- All timestamps: ISO 8601 format
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
| [[bld_schema_reranker_config]] | sibling | 0.69 |
| [[bld_schema_usage_report]] | sibling | 0.69 |
| [[bld_schema_integration_guide]] | sibling | 0.68 |
| [[bld_schema_quickstart_guide]] | sibling | 0.68 |
| [[bld_schema_search_strategy]] | sibling | 0.67 |
| [[bld_schema_pitch_deck]] | sibling | 0.66 |
| [[bld_schema_dataset_card]] | sibling | 0.65 |
| [[bld_schema_benchmark_suite]] | sibling | 0.65 |
| [[bld_schema_sandbox_config]] | sibling | 0.64 |
| [[bld_schema_sandbox_spec]] | sibling | 0.64 |
