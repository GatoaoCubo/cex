---
id: p10_lr_model_architecture_builder
kind: memory
pillar: P10
version: 1.0.0
quality: 8.9
title: "Memory Model Architecture Builder"
tags: [model_architecture, memory, learning_record, P10]
tldr: "Learning record: boundary conditions, common mistakes, quality patterns for model_architecture."
domain: "model_architecture construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
llm_function: INJECT
related:
  - bld_knowledge_card_model_architecture
  - bld_tools_model_architecture
  - bld_architecture_model_architecture
  - p03_sp_model_architecture_builder
  - p11_qg_model_architecture
  - bld_examples_model_architecture
  - bld_instruction_model_architecture
  - p10_lr_training_method_builder
  - bld_output_template_model_architecture
  - bld_collaboration_model_architecture
---

# Memory: model-architecture-builder Learning Record

## Boundary Decisions
| Situation | Route To | Not To |
|-----------|----------|--------|
| "Define 7B transformer layer structure" | model_architecture | finetune_config |
| "LoRA training job for Llama-3" | finetune_config | model_architecture |
| "Document GPT-4o performance" | model_card | model_architecture |
| "Route requests to Claude vs GPT-4" | model_provider | model_architecture |
| "Pre-training paradigm for BERT" | training_method | model_architecture |
| "Evaluate on MMLU benchmark" | benchmark | model_architecture |

## Common Mistakes
| Mistake | Correction |
|---------|-----------|
| quality: 9.0 (self-scored) | Always quality: null |
| Missing parameter_count | Required -- specify "7B", "340M", etc. |
| No Layer Structure table | Required section with at least 3 rows |
| Mixing deployment config | model_architecture = structure, not serving |
| Prose only, no tables | Use tables for layer structure and params |

## Quality Patterns
| Pattern | Why High Score |
|---------|---------------|
| Explicit param breakdown | Shows understanding of architecture |
| FLOPs + memory both specified | Enables resource planning |
| Connectivity pattern documented | Distinguishes from other architectures |
| Training considerations section | Practical guidance for practitioners |
| Boundary conditions referenced | Disambiguates from 4+ adjacent kinds |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_model_architecture]] | upstream | 0.45 |
| [[bld_tools_model_architecture]] | upstream | 0.44 |
| [[bld_architecture_model_architecture]] | upstream | 0.40 |
| [[p03_sp_model_architecture_builder]] | upstream | 0.39 |
| [[p11_qg_model_architecture]] | downstream | 0.35 |
| [[bld_examples_model_architecture]] | upstream | 0.34 |
| [[bld_instruction_model_architecture]] | upstream | 0.32 |
| [[p10_lr_training_method_builder]] | sibling | 0.31 |
| [[bld_output_template_model_architecture]] | upstream | 0.31 |
| [[bld_collaboration_model_architecture]] | downstream | 0.30 |
