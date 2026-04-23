---
kind: schema
id: bld_schema_preference_dataset
pillar: P11
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for preference_dataset
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Preference Dataset"
version: "1.0.0"
author: n03_builder
tags: [preference_dataset, builder, schema]
tldr: "Frontmatter + body schema for preference_dataset: required fields, pair structure, quality constraints."
domain: "preference dataset construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_eval_dataset
  - bld_schema_golden_test
  - bld_schema_output_validator
  - bld_schema_unit_eval
  - bld_schema_memory_scope
  - bld_schema_action_prompt
  - bld_schema_handoff_protocol
  - bld_schema_smoke_eval
  - bld_schema_dataset_card
---

# Schema: preference_dataset

## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p11_pd_{slug}) | YES | - | Namespace compliance |
| kind | literal "preference_dataset" | YES | - | Type integrity |
| pillar | literal "P11" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| training_objective | enum: rlhf, dpo, kto, constitutional, custom | YES | - | Training technique |
| preference_signal | string | YES | - | Criterion making chosen > rejected |
| annotation_method | enum: human, model_assisted, constitutional, hybrid | YES | - | How pairs were labeled |
| rater_count | int >= 1 | YES | - | Number of annotators per pair |
| agreement_rate | float 0.0-1.0 | YES | - | Inter-annotator agreement threshold |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "preference_dataset" |
| tldr | string <= 160ch | YES | - | Dense summary |
| domain | string | REC | - | Task domain (coding, summarization, safety) |
| language | string | REC | "en" | Dataset language |
| total_pairs | int | REC | - | Target or actual pair count |
| split_ratios | {train, eval, test} floats summing to 1.0 | REC | 0.8/0.1/0.1 | Train/eval/test split |
| source | string | REC | - | Data provenance |

## ID Pattern
Regex: `^p11_pd_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)
1. `## Overview` -- training objective, domain, scope, intended use
2. `## Annotation Protocol` -- criteria defining chosen vs rejected, edge cases
3. `## Quality Filters` -- thresholds, exclusion rules, automated checks
4. `## Pairs` -- example triplets: prompt, chosen, rejected, metadata

## Pair Schema
```yaml
pairs:
  - id: "{pair_id}"
    prompt: "{instruction or conversation}"
    chosen: "{preferred response}"
    rejected: "{dispreferred response}"
    metadata:
      rater_count: int
      agreement: float
      confidence: float
      tags: [list]
```

## Constraints
- max_bytes: 4096 (dataset spec, not full dataset dump)
- naming: p11_pd_{scope}.md
- machine_format: yaml (compiled artifact)
- id == filename stem
- pairs array MUST have >= 1 example
- preference_signal MUST be non-empty string
- agreement_rate MUST be in [0.0, 1.0]
- quality: null always
- Do NOT store full dataset in artifact -- store schema + examples + config

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.65 |
| [[bld_schema_eval_dataset]] | sibling | 0.64 |
| [[bld_schema_golden_test]] | sibling | 0.64 |
| [[bld_schema_output_validator]] | sibling | 0.64 |
| [[bld_schema_unit_eval]] | sibling | 0.63 |
| [[bld_schema_memory_scope]] | sibling | 0.63 |
| [[bld_schema_action_prompt]] | sibling | 0.63 |
| [[bld_schema_handoff_protocol]] | sibling | 0.63 |
| [[bld_schema_smoke_eval]] | sibling | 0.62 |
| [[bld_schema_dataset_card]] | sibling | 0.62 |
