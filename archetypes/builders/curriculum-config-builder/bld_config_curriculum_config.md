---
kind: config
id: bld_config_curriculum_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions and constraints for curriculum_config
quality: null
title: "Curriculum Config Builder - Config ISO"
version: "1.0.0"
author: n03_builder
tags: [curriculum_config, builder, config]
tldr: "Production config for curriculum config: naming, paths, and constraints."
domain: "training curriculum"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_schema_curriculum_config
---

# Config: curriculum_config Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | p07_cc_{config_slug}.md | p07_cc_domain_adapt_v1.md |
| Builder directory | kebab-case | curriculum-config-builder/ |
| Frontmatter fields | snake_case | difficulty_metric, warmup_fraction |

## File Paths

1. Output: P07_evals/examples/p07_cc_{slug}.md
2. Compiled: P07_evals/compiled/p07_cc_{slug}.yaml

## Size Limits

1. Body: max 2048 bytes
2. Density: >= 0.85

## Strategy Reference

| Strategy | Difficulty Progression | Data Requirement |
|----------|----------------------|------------------|
| easy_to_hard | Linear or stepped | Difficulty-scored dataset |
| self_paced | Loss-driven | Any dataset |
| competence_based | Gate-driven | Tiered dataset with checkpoints |
| data_mixing | Ratio-driven | Multiple data sources |
