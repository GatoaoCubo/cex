---
kind: collaboration
id: bld_orchestration_distillation_config
pillar: P12
llm_function: COLLABORATE
purpose: How distillation-config-builder works in crews
quality: null
title: "Distillation Config Builder - Orchestration ISO"
version: "1.0.0"
author: n03_builder
tags: [distillation_config, builder, collaboration]
tldr: "Orchestration protocol for distillation config: workflow integration, handoff signals, dependency management, and cross-nucleus coordination for teacher-student model compression and knowledge distillation setup."
domain: "model distillation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_model_distillation_config
---

# Collaboration: distillation-config-builder

## My Role in Crews

I am a SPECIALIST. I answer: "how to compress this teacher into a smaller student?"
I do not generate training data. I do not define model architecture.

## Crew Compositions

### Crew: "Model Compression Pipeline"
```
1. synthetic-data-config-builder -> "training data generation"
2. distillation-config-builder -> "teacher-student training config"
3. eval-metric-builder -> "quality metrics for distilled model"
```

## Handoff Protocol

### I Receive
- seeds: teacher model, compression target, quality budget

### I Produce
- distillation_config artifact (.md with YAML frontmatter)

### I Signal
- signal: complete (with quality score)

## Builders I Depend On

| Builder | Why |
|---------|-----|
| synthetic-data-config-builder | May provide training data for distillation |

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| eval-metric-builder | Needs distillation quality targets for evaluation |
| inference-config-builder | Configures serving for distilled student model |

## Integration Points

| Point | Direction | Protocol |
|-------|-----------|----------|
| F8 COLLABORATE | outbound | signal_writer.write_signal() |
| F3 INJECT | inbound | Receives upstream artifacts via handoff |
| finetune_config | upstream | Must exist before distillation config production |
| quantization_config | upstream | Must exist before distillation config production |
| model_card | upstream | Must exist before distillation config production |

## Dependencies

| Dependency | Required | Purpose |
|-----------|----------|---------|
| finetune_config | yes | Upstream artifact for distillation config |
| quantization_config | yes | Upstream artifact for distillation config |
| model_card | yes | Upstream artifact for distillation config |

## Properties

| Property | Value |
|----------|-------|
| Kind | `orchestration` |
| Pillar | P12 |
| Domain | distillation config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
