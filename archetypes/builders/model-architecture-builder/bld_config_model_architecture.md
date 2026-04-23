---
kind: config
id: bld_config_model_architecture
pillar: P09
llm_function: CONSTRAIN
quality: 8.9
title: "Config Model Architecture"
version: "1.0.0"
author: n05_builder
tags: [model_architecture, config, P09, builder]
tldr: "Builder config for model-architecture-builder: constraints, size limits, naming, allowed enums."
domain: "model_architecture construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
related:
  - bld_schema_model_architecture
  - bld_config_training_method
  - bld_schema_model_registry
  - bld_schema_training_method
  - bld_schema_experiment_tracker
  - bld_schema_multimodal_prompt
  - n06_schema_brand_config
  - bld_schema_tagline
  - bld_schema_benchmark_suite
  - bld_schema_graph_rag_config
---

# Config: model-architecture-builder

## Builder Constraints
| Constraint | Value | Enforcement |
|-----------|-------|------------|
| kind | model_architecture | Frontmatter required |
| pillar | P02 | Frontmatter required |
| max_body_bytes | 4096 | cex_hooks validate |
| min_density | 0.85 | cex_doctor check |
| quality | null | Never self-score |
| naming_pattern | `p02_ma_[a-z][a-z0-9_]+` | naming_rule |

## Allowed Enums
| Field | Allowed Values |
|-------|---------------|
| architecture_type | transformer, cnn, rnn, mlp, diffusion, graph, hybrid |
| input_modality | text, image, audio, video, multimodal, tabular |
| output_modality | text, image, embedding, logits, multimodal |
| framework | pytorch, jax, tensorflow, onnx, mlx |
| domain | NLP, vision, audio, multimodal, RL, tabular, deep_learning |

## Required Frontmatter
| Field | Type | Notes |
|-------|------|-------|
| id | string | pattern: p02_ma_[name] |
| kind | string | Always model_architecture |
| pillar | string | Always P02 |
| title | string | Descriptive name |
| version | string | SemVer |
| architecture_type | string | From allowed enum |
| parameter_count | string | e.g., "7B", "340M", "large" |
| domain | string | From allowed enum |
| quality | null | Always null |
| tags | list | Include architecture_type + domain |
| tldr | string | One-sentence summary |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_model_architecture]] | upstream | 0.60 |
| [[bld_config_training_method]] | sibling | 0.52 |
| [[bld_schema_model_registry]] | upstream | 0.48 |
| [[bld_schema_training_method]] | upstream | 0.40 |
| [[bld_schema_experiment_tracker]] | upstream | 0.40 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.39 |
| [[n06_schema_brand_config]] | upstream | 0.37 |
| [[bld_schema_tagline]] | upstream | 0.36 |
| [[bld_schema_benchmark_suite]] | upstream | 0.35 |
| [[bld_schema_graph_rag_config]] | upstream | 0.35 |
