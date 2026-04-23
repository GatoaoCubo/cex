---
kind: schema
id: bld_schema_synthetic_data_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for synthetic_data_config
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: null
title: "Synthetic Data Config Builder - Schema ISO"
version: "1.0.0"
author: n03_builder
tags: [synthetic_data_config, builder, schema]
tldr: "Schema for synthetic data config artifacts -- fields, types, constraints."
domain: "synthetic data generation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_output_synthetic_data_config
  - bld_eval_synthetic_data_config
---

# Schema: synthetic_data_config

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p01_sdc_{slug}) | YES | - | Namespace compliance |
| kind | literal "synthetic_data_config" | YES | - | Type integrity |
| pillar | literal "P01" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| generation_method | enum | YES | - | self_instruct, evol_instruct, backtranslation, seed_expand |
| source_model | string | YES | - | Teacher model identifier |
| seed_count | integer | YES | - | Number of seed examples |
| output_format | enum | YES | "jsonl" | jsonl, alpaca, sharegpt, chatml |
| target_samples | integer | REC | - | Target number of generated samples |
| temperature | float | REC | 0.7 | Sampling temperature |
| quality_filter | string | REC | - | Filter type (perplexity, dedup, toxicity) |
| decontamination | boolean | REC | true | Whether to decontaminate against eval sets |
| domain | string | YES | - | Target domain |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "synthetic-data" |
| tldr | string <= 160ch | YES | - | Dense summary |

## ID Pattern

Regex: `^p01_sdc_[a-z][a-z0-9_]+$`

## Body Structure (required sections)

1. `## Generation Method` -- method, parameters, source model
2. `## Seed Examples` -- count, format, diversity
3. `## Quality Filters` -- filtering criteria with thresholds
4. `## Decontamination` -- eval set overlap removal
5. `## Output Format` -- schema and validation

## Constraints

- naming: p01_sdc_{config_slug}.md
- generation_method MUST be one of: self_instruct, evol_instruct, backtranslation, seed_expand
- seed_count MUST be >= 5
- quality: null always
- synthetic_data_config is GENERATION CONFIG -- no training logic
