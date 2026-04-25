---
kind: collaboration
id: bld_orchestration_synthetic_data_config
pillar: P12
llm_function: COLLABORATE
purpose: How synthetic-data-config-builder works in crews
quality: null
title: "Synthetic Data Config Builder - Orchestration ISO"
version: "1.0.0"
author: n03_builder
tags: [synthetic_data_config, builder, collaboration]
tldr: "Crew collaboration protocol for synthetic data config builder."
domain: "synthetic data generation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_model_synthetic_data_config
---

# Collaboration: synthetic-data-config-builder

## My Role in Crews

I am a SPECIALIST. I answer: "how to generate synthetic data for this use case?"
I do not train models. I do not evaluate model performance.
I configure data generation so downstream training pipelines have quality input.

## Crew Compositions

### Crew: "Fine-Tuning Data Pipeline"
```
1. synthetic-data-config-builder -> "generation config with quality filters"
2. distillation-config-builder -> "training configuration"
3. eval-metric-builder -> "evaluation metrics for trained model"
```

## Handoff Protocol

### I Receive
- seeds: use case, target domain, desired sample count, format preference

### I Produce
- synthetic_data_config artifact (.md with YAML frontmatter)

### I Signal
- signal: complete (with quality score)

## Builders I Depend On
None -- independent builder.

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| distillation-config-builder | Needs generated data specification for training |

## Integration Points

| Point | Direction | Protocol |
|-------|-----------|----------|
| F8 COLLABORATE | outbound | signal_writer.write_signal() |
| F3 INJECT | inbound | Receives upstream artifacts via handoff |
| dataset_card | upstream | Must exist before synthetic data config production |
| eval_dataset | upstream | Must exist before synthetic data config production |

## Dependencies

| Dependency | Required | Purpose |
|-----------|----------|---------|
| dataset_card | yes | Upstream artifact for synthetic data config |
| eval_dataset | yes | Upstream artifact for synthetic data config |

## Properties

| Property | Value |
|----------|-------|
| Kind | `orchestration` |
| Pillar | P12 |
| Domain | synthetic data config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
