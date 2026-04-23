---
kind: collaboration
id: bld_orchestration_curriculum_config
pillar: P12
llm_function: COLLABORATE
purpose: How curriculum-config-builder works in crews
quality: null
title: "Curriculum Config Builder - Orchestration ISO"
version: "1.0.0"
author: n03_builder
tags: [curriculum_config, builder, collaboration]
tldr: "Crew collaboration protocol for curriculum config builder."
domain: "training curriculum"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_model_curriculum_config
---

# Collaboration: curriculum-config-builder

## My Role in Crews

I am a SPECIALIST. I answer: "in what order and proportion should training data be presented?"
I do not generate data. I do not define model architecture.

## Crew Compositions

### Crew: "Training Data Pipeline"
```
1. synthetic-data-config-builder -> "data generation"
2. curriculum-config-builder -> "training data scheduling"
3. distillation-config-builder -> "teacher-student training"
4. eval-metric-builder -> "quality evaluation"
```

## Handoff Protocol

### I Receive
- seeds: training task, data sources, model type, quality targets

### I Produce
- curriculum_config artifact (.md with YAML frontmatter)

### I Signal
- signal: complete (with quality score)

## Builders I Depend On

| Builder | Why |
|---------|-----|
| synthetic-data-config-builder | Provides generated data sources for curriculum |

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| distillation-config-builder | Uses curriculum schedule for training data ordering |
