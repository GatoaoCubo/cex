---
kind: schema
id: bld_schema_training_method
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for training_method
quality: 9.0
title: "Schema Training Method"
version: "1.0.0"
author: n05_builder
tags: [training_method, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for training_method"
domain: "training_method construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
| :--- | :--- | :--- | :--- | :--- |
| id | string | Y | "" | Unique identifier, pattern: p02_tm_[a-z][a-z0-9_]+ |
| kind | string | Y | "training_method" | CEX type, always training_method |
| pillar | string | Y | "P02" | Pillar ID, always P02 |
| title | string | Y | "" | Descriptive name |
| version | string | Y | "1.0.0" | SemVer |
| created | datetime | Y | now() | Creation date |
| updated | datetime | Y | now() | Last update |
| author | string | Y | "system" | Creator name |
| domain | string | Y | "AI_ML" | Functional domain |
| quality | null | Y | null | Always null -- peer review assigns |
| tags | list | Y | [] | Metadata tags |
| tldr | string | Y | "" | Brief summary |
| learning_paradigm | string | Y | "supervised" | Enum: supervised, unsupervised, reinforcement, self_supervised, transfer, hybrid |
| compute_intensity | string | Y | "medium" | Enum: low, medium, high |

### Recommended
| Field | Type | Notes |
| :--- | :--- | :--- |
| target_audience | string | Intended users |
| hyperparameters | object | Key hyperparameter set |
| dataset_dependency | string | Required data sources |
| optimizer | string | Training optimizer name |
| scheduler | string | LR scheduler name |

## Body Sections
| Section | Required | Content |
| :--- | :--- | :--- |
| Overview | Y | Task, base model, paradigm rationale |
| Learning Paradigm | Y | Paradigm type, objective, label requirements |
| Compute Profile | Y | Hardware, memory, training time |
| Hyperparameters | Y | All key params with values/ranges |
| Dataset Requirements | Y | Source, format, field_mapping, preprocessing |
| Evaluation | Y | Metrics, frequency, convergence criteria |

## Size Constraints
| Component | Limit |
| :--- | :--- |
| Body | 4096 bytes |
| Total with frontmatter | 6144 bytes |
| Min density | 0.85 |
