---
kind: schema
id: bld_schema_eval_dataset
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for eval_dataset
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Eval Dataset"
version: "1.0.0"
author: n03_builder
tags: [eval_dataset, builder, examples]
tldr: "Golden and anti-examples for eval dataset construction, demonstrating ideal structure and common pitfalls."
domain: "eval dataset construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_dataset_card
  - bld_schema_output_validator
  - bld_schema_handoff_protocol
  - bld_schema_unit_eval
  - bld_schema_golden_test
  - bld_schema_memory_scope
  - bld_schema_constraint_spec
  - bld_schema_chunk_strategy
  - bld_schema_smoke_eval
---

# Schema: eval_dataset
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p07_ds_{slug}) | YES | - | Namespace compliance |
| kind | literal "eval_dataset" | YES | - | Type integrity |
| pillar | literal "P07" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable dataset name |
| size | integer >= 1 | YES | - | Total number of test cases |
| splits | map[string, float] | YES | - | train/test/val ratios (must sum to 1.0) |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "eval_dataset" |
| tldr | string <= 160ch | YES | - | Dense summary |
| schema_fields | list[string] | YES | - | Field names present in each test case |
| description | string <= 200ch | REC | - | What the dataset covers |
| source | string | REC | - | Origin of data (human, synthetic, scraped) |
| framework | enum: braintrust, langsmith, deepeval, huggingface, costm | REC | - | Target eval framework |
| task_type | string | REC | - | Classification, QA, summarization, etc. |
| language | string | REC | "en" | Dataset language (ISO 639-1) |
| license | string | REC | - | Data license (MIT, CC-BY, proprietary) |
| refresh_cadence | string | OPT | - | How often dataset is updated |
## ID Pattern
Regex: `^p07_ds_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what the dataset covers, use case, who uses it
2. `## Schema` — field-by-field definition (input, expected_output, metadata)
3. `## Splits` — train/test/val rationale and percentages
4. `## Integration` — framework adapter, loading pattern, version migration
## Constraints
- max_bytes: 4096 (body only — dataset spec with schema detail)
- naming: p07_dataset.md (single file per dataset)
- machine_format: yaml (compiled artifact)
- id == filename stem
- splits values MUST sum to 1.0
- schema_fields MUST include at minimum: input, expected_output
- quality: null always
- NO actual test case data in body — schema and spec only

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.66 |
| [[bld_schema_dataset_card]] | sibling | 0.65 |
| [[bld_schema_output_validator]] | sibling | 0.65 |
| [[bld_schema_handoff_protocol]] | sibling | 0.65 |
| [[bld_schema_unit_eval]] | sibling | 0.65 |
| [[bld_schema_golden_test]] | sibling | 0.65 |
| [[bld_schema_memory_scope]] | sibling | 0.65 |
| [[bld_schema_constraint_spec]] | sibling | 0.64 |
| [[bld_schema_chunk_strategy]] | sibling | 0.63 |
| [[bld_schema_smoke_eval]] | sibling | 0.63 |
