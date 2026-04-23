---
kind: quality_gate
id: bld_eval_synthetic_data_config
pillar: P07
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for synthetic_data_config
quality: null
title: "Synthetic Data Config Builder - Eval ISO"
version: "1.0.0"
author: n03_builder
tags: [synthetic_data_config, builder, quality_gate]
tldr: "Quality gate for synthetic data config: validates generation method, quality filters, and decontamination."
domain: "synthetic data generation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_schema_synthetic_data_config
  - bld_model_synthetic_data_config
---

## Quality Gate

## HARD Gates

| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing fields |
| H02 | ID matches pattern | ID does not match ^p01_sdc_[a-z][a-z0-9_]+$ |
| H03 | kind field matches | kind is not 'synthetic_data_config' |
| H04 | generation_method defined | generation_method field missing or empty |
| H05 | quality is null | quality must be null at authoring time |
| H06 | Required fields present | Missing required fields |
| H07 | source_model specified | source_model field missing or empty |

## SOFT Scoring

| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D1 | Method clarity | 0.20 | Method described with parameters (1.0) vs name-only (0.0) |
| D2 | Quality filters | 0.20 | Numeric thresholds for filters (1.0) vs absent (0.0) |
| D3 | Decontamination | 0.15 | Eval set overlap removal defined (1.0) vs missing (0.0) |
| D4 | Seed diversity | 0.15 | Diversity requirements documented |
| D5 | Output format | 0.10 | Schema and validation rules specified |
| D6 | Cost estimate | 0.10 | API cost or compute time documented |
| D7 | Documentation | 0.10 | tldr captures key info in <= 160 characters |

## Actions

| Score | Action |
|-------|--------|
| >=9.5 | GOLDEN |
| >=8.0 | PUBLISH |
| >=7.0 | REVIEW |
| <7.0 | REJECT |
