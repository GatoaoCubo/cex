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
tldr: "Orchestration protocol for curriculum config: workflow integration, handoff signals, dependency management, and cross-nucleus coordination for training data ordering, difficulty scheduling, and adaptive pacing configuration."
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

## Integration Points

| Point | Direction | Protocol |
|-------|-----------|----------|
| F8 COLLABORATE | outbound | signal_writer.write_signal() |
| F3 INJECT | inbound | Receives upstream artifacts via handoff |
| dataset_card | upstream | Must exist before curriculum config production |
| training_method | upstream | Must exist before curriculum config production |
| eval_metric | upstream | Must exist before curriculum config production |

## Dependencies

| Dependency | Required | Purpose |
|-----------|----------|---------|
| dataset_card | yes | Upstream artifact for curriculum config |
| training_method | yes | Upstream artifact for curriculum config |
| eval_metric | yes | Upstream artifact for curriculum config |

## Properties

| Property | Value |
|----------|-------|
| Kind | `orchestration` |
| Pillar | P12 |
| Domain | curriculum config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
