---
id: n00_model_architecture_manifest
kind: knowledge_card
pillar: P02
nucleus: n00
title: "Model Architecture -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, model_architecture, p02, n00, archetype, template]
density_score: 1.0
updated: "2026-04-17"
related:
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_thinking_config
  - bld_schema_integration_guide
  - bld_schema_rl_algorithm
  - bld_schema_search_strategy
  - bld_schema_benchmark_suite
  - bld_collaboration_model_architecture
  - bld_schema_dataset_card
  - bld_schema_app_directory_entry
---

<!-- 8F: F1=knowledge_card P02 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Model Architecture defines the neural network architecture for a machine learning model: layer structure, attention mechanism, parameter count, and training paradigm. It serves as the technical specification for understanding or implementing a foundation model. Used by N03 and N05 when designing or selecting model architectures for fine-tuning and deployment.

## Pillar
P02 -- Model

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `model_architecture` |
| pillar | string | yes | Always `P02` |
| title | string | yes | Architecture name and variant |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| architecture_type | enum | yes | transformer\|mamba\|diffusion\|hybrid |
| parameter_count | string | yes | Total parameters (e.g., 9B, 70B) |
| attention_type | enum | no | MHA\|GQA\|MQA\|flash-attn |
| context_length | int | yes | Maximum input context window |
| training_paradigm | enum | yes | autoregressive\|masked\|encoder-decoder |
| open_source | bool | yes | Whether weights are publicly available |

## When to use
- When documenting the architecture of a model used in CEX
- When comparing architectures for fine-tuning suitability
- When designing a custom model for a specific task

## Builder
`archetypes/builders/model_architecture-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind model_architecture --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N03 or N05)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- ML engineers and model researchers
- `{{DOMAIN_CONTEXT}}` -- intended task and deployment constraints

## Example (minimal)
```yaml
---
id: model_architecture_gemma2_9b
kind: model_architecture
pillar: P02
nucleus: n03
title: "Gemma 2 9B Architecture"
version: 1.0
quality: null
---
architecture_type: transformer
parameter_count: "9B"
attention_type: GQA
context_length: 8192
training_paradigm: autoregressive
open_source: true
```

## Related kinds
- `model_card` (P02) -- operational spec for using this architecture
- `finetune_config` (P02) -- training job targeting this architecture
- `training_method` (P02) -- adaptation technique for this architecture

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | downstream | 0.46 |
| [[bld_schema_usage_report]] | downstream | 0.42 |
| [[bld_schema_thinking_config]] | downstream | 0.42 |
| [[bld_schema_integration_guide]] | downstream | 0.42 |
| [[bld_schema_rl_algorithm]] | downstream | 0.41 |
| [[bld_schema_search_strategy]] | downstream | 0.41 |
| [[bld_schema_benchmark_suite]] | downstream | 0.41 |
| [[bld_collaboration_model_architecture]] | downstream | 0.41 |
| [[bld_schema_dataset_card]] | downstream | 0.41 |
| [[bld_schema_app_directory_entry]] | downstream | 0.41 |
