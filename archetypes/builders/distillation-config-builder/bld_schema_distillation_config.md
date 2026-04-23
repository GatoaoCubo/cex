---
kind: schema
id: bld_schema_distillation_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for distillation_config
quality: null
title: "Distillation Config Builder - Schema ISO"
version: "1.0.0"
author: n03_builder
tags: [distillation_config, builder, schema]
tldr: "Schema for distillation config artifacts -- fields, types, and constraints."
domain: "model distillation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_output_distillation_config
  - bld_eval_distillation_config
---

# Schema: distillation_config

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p02_dc_{slug}) | YES | - | Namespace compliance |
| kind | literal "distillation_config" | YES | - | Type integrity |
| pillar | literal "P02" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| teacher_model | string | YES | - | Teacher model identifier |
| student_model | string | YES | - | Student model identifier |
| temperature | float | YES | 4.0 | Softmax temperature for KD |
| alpha | float | YES | 0.5 | KD loss weight (1-alpha = task loss weight) |
| method | enum | YES | "logit" | logit, feature, progressive |
| compression_ratio | float | REC | - | Teacher params / student params |
| learning_rate | float | REC | - | Training learning rate |
| epochs | integer | REC | - | Training epochs |
| domain | string | YES | - | Target domain |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "distillation" |
| tldr | string <= 160ch | YES | - | Dense summary |

## ID Pattern

Regex: `^p02_dc_[a-z][a-z0-9_]+$`

## Body Structure (required sections)

1. `## Teacher` -- teacher model specs and performance
2. `## Student` -- student architecture and target size
3. `## Training` -- temperature, alpha, schedule
4. `## Loss Function` -- KD + task loss composition
5. `## Evaluation` -- checkpoints and quality thresholds

## Constraints

- naming: p02_dc_{config_slug}.md
- temperature MUST be > 1.0 for meaningful distillation
- alpha MUST be between 0.0 and 1.0
- method MUST be one of: logit, feature, progressive
- quality: null always
