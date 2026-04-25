---
kind: quality_gate
id: bld_eval_curriculum_config
pillar: P07
llm_function: GOVERN
purpose: Quality gate for curriculum_config artifacts
quality: null
title: "Curriculum Config Builder - Eval ISO"
version: "1.0.0"
author: n03_builder
tags: [curriculum_config, builder, quality_gate]
tldr: "Quality gate for curriculum config: validates strategy, difficulty metric, and data sources."
domain: "training curriculum"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_schema_curriculum_config
---

## Quality Gate

## HARD Gates

| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax |
| H02 | ID matches pattern | ID does not match ^p07_cc_[a-z][a-z0-9_]+$ |
| H03 | kind field matches | kind is not 'curriculum_config' |
| H04 | strategy defined | strategy field missing or not in enum |
| H05 | quality is null | quality must be null |
| H06 | difficulty_metric defined | difficulty_metric missing or empty |
| H07 | data_sources non-empty | data_sources list empty or missing |

## SOFT Scoring

| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D1 | Strategy rationale | 0.20 | Approach justified for task (1.0) vs arbitrary (0.0) |
| D2 | Difficulty metric | 0.15 | Metric defined with measurement method |
| D3 | Data source coverage | 0.15 | All sources listed with sizes and ratios |
| D4 | Phase definition | 0.15 | Phases described with transition criteria |
| D5 | Warmup specified | 0.10 | Warmup fraction and strategy documented |
| D6 | Checkpoints defined | 0.10 | Evaluation points and competence gates |
| D7 | Annealing plan | 0.10 | Schedule type and parameters if applicable |
| D8 | Documentation | 0.05 | tldr captures key info |

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
| Naming convention | Regex match against p07_cc_{{name}}.md + .yaml | Yes |
| Size limit | Byte count <= 4096 | Yes |
| Density score | Token/byte ratio >= 0.85 | Yes |
| Cross-references valid | Link resolution check | Partial |

## Properties

| Property | Value |
|----------|-------|
| Kind | `eval` |
| Pillar | P07 |
| Domain | curriculum config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
