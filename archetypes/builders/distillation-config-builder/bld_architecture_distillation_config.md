---
kind: architecture
id: bld_architecture_distillation_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of distillation_config
quality: null
title: "Distillation Config Builder - Architecture ISO"
version: "1.0.0"
author: n03_builder
tags: [distillation_config, builder, architecture]
tldr: "Architecture context for distillation config: components and boundary."
domain: "model distillation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_model_distillation_config
---

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| teacher_model | Source model for knowledge transfer | distillation-config-builder | required |
| student_model | Target compressed model | distillation-config-builder | required |
| temperature | Softmax temperature for soft targets | distillation-config-builder | required |
| alpha | KD loss vs task loss balance | distillation-config-builder | required |
| method | Distillation approach | distillation-config-builder | required |
| training_schedule | Epochs, LR, checkpoints | distillation-config-builder | optional |

## Dependency Graph

```
teacher_model --knowledge--> distillation_config --produces--> student_model
synthetic_data_config (P01) --optional_input--> distillation_config
distillation_config --evaluated_by--> eval_metric (P07)
distillation_config --independent-- embedding_config (P01)
```

## Boundary Table

| distillation_config IS | distillation_config IS NOT |
|-----------------------|---------------------------|
| Training config for teacher-student compression | A model architecture spec |
| Specifies loss function and temperature | A synthetic_data_config -- that configures data generation |
| Defines compression targets and quality budget | An inference_config -- that configures model serving |

## Component Boundaries

Teacher-student knowledge transfer and model compression. NOT finetune_config (full model training) nor quantization_config (weight precision reduction) nor model_card (model documentation).

| Boundary | In Scope | Out of Scope |
|----------|----------|-------------|
| Kind scope | distillation config | Adjacent kinds |
| Dependencies | finetune_config, quantization_config, model_card | Transitive deps |

## Interfaces

| Interface | Direction | Contract |
|-----------|-----------|----------|
| Schema (P06) | upstream | Validates structure |
| Output (P05) | downstream | Produces artifacts |
| Config (P09) | lateral | Constrains production |

## Properties

| Property | Value |
|----------|-------|
| Kind | `architecture` |
| Pillar | P08 |
| Domain | distillation config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
