---
kind: schema
id: bld_schema_curriculum_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for curriculum_config
quality: null
title: "Curriculum Config Builder - Schema ISO"
version: "1.0.0"
author: n03_builder
tags: [curriculum_config, builder, schema]
tldr: "Schema for curriculum config artifacts -- fields, types, and constraints."
domain: "training curriculum"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_output_curriculum_config
  - bld_eval_curriculum_config
---

# Schema: curriculum_config

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p07_cc_{slug}) | YES | - | Namespace compliance |
| kind | literal "curriculum_config" | YES | - | Type integrity |
| pillar | literal "P07" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| strategy | enum | YES | - | easy_to_hard, self_paced, competence_based, data_mixing |
| difficulty_metric | string | YES | - | How difficulty is measured |
| num_phases | integer | YES | - | Number of curriculum phases |
| warmup_fraction | float | REC | 0.1 | Fraction of training as warmup |
| data_sources | list[string] | YES | - | Training data sources |
| mixing_ratios | map | REC | - | Per-source proportions per phase |
| annealing | string | REC | - | Annealing schedule type |
| domain | string | YES | - | Target domain |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "curriculum" |
| tldr | string <= 160ch | YES | - | Dense summary |

## ID Pattern

Regex: `^p07_cc_[a-z][a-z0-9_]+$`

## Body Structure (required sections)

1. `## Strategy` -- approach and rationale
2. `## Data Sources` -- sources, sizes, mixing ratios
3. `## Difficulty Progression` -- metric and schedule
4. `## Schedule` -- warmup, phases, annealing
5. `## Checkpoints` -- evaluation points and competence gates

## Constraints

- naming: p07_cc_{config_slug}.md
- strategy MUST be one of: easy_to_hard, self_paced, competence_based, data_mixing
- num_phases MUST be >= 1
- warmup_fraction MUST be between 0.0 and 1.0
- quality: null always
