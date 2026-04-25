---
kind: architecture
id: bld_architecture_synthetic_data_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of synthetic_data_config -- dependencies and architectural position
quality: null
title: "Synthetic Data Config Builder - Architecture ISO"
version: "1.0.0"
author: n03_builder
tags: [synthetic_data_config, builder, architecture]
tldr: "Architecture context for synthetic data config: components, dependencies, and boundary."
domain: "synthetic data generation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_model_synthetic_data_config
  - bld_schema_synthetic_data_config
---

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| generation_method | How synthetic data is created | synthetic-data-config-builder | required |
| source_model | Teacher model for generation | synthetic-data-config-builder | required |
| seed_examples | Human-written examples for bootstrapping | synthetic-data-config-builder | required |
| quality_filters | Post-generation filtering criteria | synthetic-data-config-builder | required |
| decontamination | Eval set overlap removal | synthetic-data-config-builder | required |
| output_format | Generated data schema | synthetic-data-config-builder | required |

## Dependency Graph

```
seed_examples --input--> synthetic_data_config --output--> training_dataset
synthetic_data_config --consumed_by--> distillation_config (P02)
synthetic_data_config --independent-- embedding_config (P01)
synthetic_data_config --independent-- eval_metric (P07)
```

## Boundary Table

| synthetic_data_config IS | synthetic_data_config IS NOT |
|-------------------------|------------------------------|
| Generation configuration: method, model, filters | A distillation_config -- distillation configures training |
| Specifies how to create artificial data | An eval_metric -- eval measures model performance |
| Includes quality filtering and decontamination | A knowledge_card -- KC distills domain knowledge |
| Static spec for a data generation pipeline | An embedding_config -- embedding configures vectorization |

## Component Boundaries

Synthetic training data generation pipeline. NOT dataset_card (data documentation and metadata) nor eval_dataset (evaluation data specification) nor finetune_config (training job parameters).

| Boundary | In Scope | Out of Scope |
|----------|----------|-------------|
| Kind scope | synthetic data config | Adjacent kinds |
| Dependencies | dataset_card, eval_dataset | Transitive deps |

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
| Domain | synthetic data config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
