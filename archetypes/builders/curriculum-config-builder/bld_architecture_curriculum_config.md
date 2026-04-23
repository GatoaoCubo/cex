---
kind: architecture
id: bld_architecture_curriculum_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of curriculum_config
quality: null
title: "Curriculum Config Builder - Architecture ISO"
version: "1.0.0"
author: n03_builder
tags: [curriculum_config, builder, architecture]
tldr: "Architecture context for curriculum config: components and boundary."
domain: "training curriculum"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_model_curriculum_config
---

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| strategy | Curriculum approach | curriculum-config-builder | required |
| difficulty_metric | How difficulty is measured | curriculum-config-builder | required |
| data_sources | Training data catalog | curriculum-config-builder | required |
| mixing_ratios | Per-source proportions | curriculum-config-builder | optional |
| phases | Training stages with transitions | curriculum-config-builder | required |
| checkpoints | Evaluation points | curriculum-config-builder | optional |

## Dependency Graph

```
synthetic_data_config (P01) --provides_data--> curriculum_config
curriculum_config --consumed_by--> distillation_config (P02, training schedule)
curriculum_config --evaluated_by--> eval_metric (P07)
curriculum_config --independent-- inference_config (P09)
```

## Boundary Table

| curriculum_config IS | curriculum_config IS NOT |
|---------------------|-------------------------|
| Training data scheduling and ordering | A synthetic_data_config -- that generates data |
| Defines difficulty progression and mixing | A distillation_config -- that configures teacher-student |
| Specifies phases and competence gates | An eval_metric -- that defines quality measures |
