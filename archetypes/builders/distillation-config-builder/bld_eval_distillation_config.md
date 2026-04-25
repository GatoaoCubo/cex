---
kind: quality_gate
id: bld_eval_distillation_config
pillar: P07
llm_function: GOVERN
purpose: Quality gate for distillation_config artifacts
quality: null
title: "Distillation Config Builder - Eval ISO"
version: "1.0.0"
author: n03_builder
tags: [distillation_config, builder, quality_gate]
tldr: "Quality gate for distillation config: validates teacher-student pair, temperature, and loss function."
domain: "model distillation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_schema_distillation_config
---

## Quality Gate

## HARD Gates

| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax |
| H02 | ID matches pattern | ID does not match ^p02_dc_[a-z][a-z0-9_]+$ |
| H03 | kind field matches | kind is not 'distillation_config' |
| H04 | teacher_model defined | teacher_model missing or empty |
| H05 | quality is null | quality must be null |
| H06 | student_model defined | student_model missing or empty |
| H07 | temperature > 1.0 | temperature <= 1 defeats distillation |

## SOFT Scoring

| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D1 | Teacher documented | 0.15 | Model ID, params, performance baseline |
| D2 | Student justified | 0.15 | Architecture choice explained |
| D3 | Temperature rationale | 0.15 | Temperature value justified for use case |
| D4 | Loss composition | 0.15 | KD + task weights specified, sum to 1.0 |
| D5 | Compression target | 0.10 | Ratio specified with quality budget |
| D6 | Training schedule | 0.10 | Epochs, LR, checkpoints defined |
| D7 | Evaluation plan | 0.10 | Quality thresholds and regression criteria |
| D8 | Documentation | 0.10 | tldr captures key info |

## Actions

| Score | Action |
|-------|--------|
| >=9.5 | GOLDEN |
| >=8.0 | PUBLISH |
| >=7.0 | REVIEW |
| <7.0 | REJECT |

## Validation Checklist

| Check | Method | Automated |
|-------|--------|-----------|
| Frontmatter schema | cex_compile.py --validate | Yes |
| Naming convention | Regex match against p02_dc_{{name}}.md + .yaml | Yes |
| Size limit | Byte count <= 4096 | Yes |
| Density score | Token/byte ratio >= 0.85 | Yes |
| Cross-references valid | Link resolution check | Partial |

## Properties

| Property | Value |
|----------|-------|
| Kind | `eval` |
| Pillar | P07 |
| Domain | distillation config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
