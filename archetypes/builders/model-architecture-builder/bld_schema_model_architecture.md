---
kind: schema
id: bld_schema_model_architecture
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for model_architecture
quality: 9.0
title: "Schema Model Architecture"
version: "1.0.0"
author: n05_builder
tags: [model_architecture, builder, schema]
tldr: "Formal schema for model_architecture artifacts: neural net structure, layers, connectivity."
domain: "model_architecture construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
related:
  - bld_schema_model_registry
  - bld_schema_training_method
  - bld_schema_experiment_tracker
  - bld_config_model_architecture
  - bld_schema_multimodal_prompt
  - n06_schema_brand_config
  - bld_schema_dataset_card
  - bld_schema_agent_computer_interface
  - bld_schema_tagline
  - bld_schema_benchmark_suite
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
| :--- | :--- | :--- | :--- | :--- |
| id | string | Y | "" | Unique identifier, pattern: p02_ma_[a-z][a-z0-9_]+ |
| kind | string | Y | "model_architecture" | CEX type, always model_architecture |
| pillar | string | Y | "P02" | Pillar ID, always P02 |
| title | string | Y | "" | Descriptive name |
| version | string | Y | "1.0.0" | SemVer |
| created | datetime | Y | now() | Creation date |
| updated | datetime | Y | now() | Last update |
| author | string | Y | "system" | Creator name |
| domain | string | Y | "deep_learning" | Architecture domain |
| quality | null | Y | null | Always null -- peer review assigns |
| tags | list | Y | [] | Metadata tags |
| tldr | string | Y | "" | Brief summary |
| architecture_type | string | Y | "transformer" | Enum: transformer, cnn, rnn, mlp, hybrid, diffusion, graph |
| parameter_count | string | Y | "unknown" | e.g. "7B", "340M", "large" |

### Recommended
| Field | Type | Notes |
| :--- | :--- | :--- |
| input_modality | string | text, image, audio, multimodal |
| output_modality | string | text, image, embedding, logits |
| framework | string | pytorch, jax, tensorflow |
| context_length | integer | Max sequence length |

## Body Sections
| Section | Required | Content |
| :--- | :--- | :--- |
| Overview | Y | Architecture rationale, design goals, novelty |
| Layer Structure | Y | Ordered table of layers with types and dims |
| Connectivity Pattern | Y | How layers connect: sequential, skip, attention |
| Parameter Profile | Y | Total params, breakdown by component |
| Compute Profile | Y | FLOPs, memory, inference time |
| Training Considerations | Y | Initialization, optimization notes |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_model_registry]] | sibling | 0.62 |
| [[bld_schema_training_method]] | sibling | 0.56 |
| [[bld_schema_experiment_tracker]] | sibling | 0.53 |
| [[bld_config_model_architecture]] | downstream | 0.52 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.47 |
| [[n06_schema_brand_config]] | related | 0.45 |
| [[bld_schema_dataset_card]] | sibling | 0.43 |
| [[bld_schema_agent_computer_interface]] | sibling | 0.43 |
| [[bld_schema_tagline]] | sibling | 0.42 |
| [[bld_schema_benchmark_suite]] | sibling | 0.42 |
