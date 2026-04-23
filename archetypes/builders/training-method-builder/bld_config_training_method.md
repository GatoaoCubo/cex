---
kind: config
id: bld_config_training_method
pillar: P09
llm_function: CONSTRAIN
quality: 9.0
title: "Config Training Method"
version: "1.0.0"
author: n05_builder
tags: [training_method, config, P09, builder]
tldr: "Builder configuration for training-method-builder: constraints, size limits, naming rules, and allowed enums."
domain: "training_method construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.87
related:
  - bld_schema_training_method
  - bld_config_model_architecture
  - bld_schema_model_registry
  - bld_schema_experiment_tracker
  - bld_schema_model_architecture
  - bld_schema_multimodal_prompt
  - n06_schema_brand_config
  - bld_schema_tagline
  - bld_schema_eval_metric
  - bld_schema_benchmark_suite
---

# Config: training-method-builder

## Builder Constraints
| Constraint | Value | Enforcement |
|-----------|-------|------------|
| kind | training_method | Frontmatter required field |
| pillar | P02 | Frontmatter required field |
| max_body_bytes | 4096 | cex_hooks validate |
| min_density | 0.85 | cex_doctor check |
| quality | null | Never self-score |
| naming_pattern | `p02_tm_[a-z][a-z0-9_]+` | naming_rule |

## Allowed Enums
| Field | Allowed Values |
|-------|---------------|
| learning_paradigm | supervised, unsupervised, reinforcement, self_supervised, transfer, hybrid |
| compute_intensity | low, medium, high |
| optimizer | adam, adamw, sgd, adagrad, rmsprop, lion |
| scheduler | linear, cosine, constant, polynomial, warmup_cosine |
| domain | NLP, CV, RL, multimodal, tabular, audio, time_series, AI_ML, LLM_alignment |

## Required Frontmatter
| Field | Type | Notes |
|-------|------|-------|
| id | string | Unique, follows naming_pattern |
| kind | string | Always `training_method` |
| pillar | string | Always `P02` |
| title | string | Descriptive name |
| version | string | SemVer (1.0.0) |
| learning_paradigm | string | From allowed enum |
| compute_intensity | string | From allowed enum |
| domain | string | From allowed enum or custom |
| quality | null | Always null -- never self-score |
| tags | list | Include domain + paradigm tags |
| tldr | string | One-sentence summary |

## Build Mode
| Mode | Trigger | Behavior |
|------|---------|---------|
| F1 CONSTRAIN | kind=training_method detected | Load this config, schema, pillar P02 |
| F4 REASON | Template-First if >= 60% match | Adapt existing example; else fresh |
| F7 GOVERN | After F6 PRODUCE | Run 10 HARD gates; retry if < 8.0 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_training_method]] | upstream | 0.56 |
| [[bld_config_model_architecture]] | sibling | 0.49 |
| [[bld_schema_model_registry]] | upstream | 0.43 |
| [[bld_schema_experiment_tracker]] | upstream | 0.39 |
| [[bld_schema_model_architecture]] | upstream | 0.36 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.35 |
| [[n06_schema_brand_config]] | upstream | 0.35 |
| [[bld_schema_tagline]] | upstream | 0.34 |
| [[bld_schema_eval_metric]] | upstream | 0.33 |
| [[bld_schema_benchmark_suite]] | upstream | 0.33 |
