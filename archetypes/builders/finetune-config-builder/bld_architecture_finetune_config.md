---
kind: architecture
id: bld_architecture_finetune_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of finetune_config -- inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Finetune Config"
version: "1.0.0"
author: n03_builder
tags: [finetune_config, builder, architecture, P02]
tldr: "Component map for finetune_config: base model, adapter, dataset, hyperparams, eval, and dependency graph."
domain: "finetune_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_collaboration_finetune_config
  - finetune-config-builder
  - p03_sp_finetune_config_builder
  - bld_schema_finetune_config
  - bld_collaboration_training_method
  - training-method-builder
  - p01_kc_finetune_config
  - p11_qg_finetune_config
  - p03_sp_training_method_builder
  - bld_examples_finetune_config
---
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| base_model | Pre-trained model being adapted: HF model ID or local path | finetune-config-builder | required |
| adapter_type | Adaptation method: lora, qlora, full, prefix_tuning, p_tuning | finetune-config-builder | required |
| adapter_params | Type-specific parameters: rank, alpha, dropout, target_modules, bits | finetune-config-builder | required |
| dataset | Training data: path, format, field_mapping, size, preprocessing | finetune-config-builder | required |
| hyperparameters | Training dynamics: lr, batch size, epochs, scheduler, warmup, optimizer | finetune-config-builder | required |
| eval_strategy | Evaluation plan: metrics, eval_steps, checkpoint, early stopping | finetune-config-builder | required |
| compute | Hardware requirement: GPU type, VRAM estimate, distributed flag | finetune-config-builder | recommended |
| task_type | Training paradigm: sft, dpo, rlhf, orpo, reward_modeling | finetune-config-builder | recommended |
| framework | Training framework: transformers, trl, axolotl, unsloth, llamafactory | finetune-config-builder | recommended |

## Dependency Graph
```
dataset (P01 or external) --feeds--> finetune_config (training data source)
model_card (P02) --documents--> finetune_config (result of running this config)
finetune_config --produces--> model_card (P02) (trained adapter or checkpoint)
finetune_config --consumed_by--> boot_config (P02) (adapter merged at provider boot)
finetune_config --consumed_by--> model_provider (P02) (adapter loaded at inference)
benchmark (P07) --evaluates_output_of--> finetune_config (post-training eval)
guardrail (P11) --constrains--> finetune_config (safety rules for training data, output)
```

| From | To | Type | Data |
|------|----|------|------|
| dataset | finetune_config | feeds | training examples, format, field names |
| finetune_config | model_card | produces | trained weights, adapter checkpoint, training metrics |
| finetune_config | boot_config | consumed_by | adapter path, quantization settings at provider boot |
| finetune_config | model_provider | consumed_by | adapter ID, merge strategy for inference |
| benchmark | finetune_config | evaluates_output_of | post-training quality assessment |
| guardrail | finetune_config | constrains | training data safety rules |

## Boundary Table
| finetune_config IS | finetune_config IS NOT |
|-------------------|----------------------|
| A training job specification: how to adapt a base model | model_provider (P02): configures runtime API routing and provider selection |
| Covers adapter parameters, dataset, hyperparameters, eval | model_card (P02): documents a TRAINED model (post-training artifact) |
| Defines the training process before training starts | boot_config (P02): per-provider startup parameters (runtime, not training) |
| Consumed by training frameworks (TRL, Axolotl, Unsloth) | benchmark (P07): evaluates a trained model's outputs |
| Specifies evaluation DURING training (eval_loss, checkpoints) | agent (P02): defines a runtime agent persona and capabilities |

## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Specification | base_model, adapter_type, dataset, task_type | Define WHAT is being trained and HOW |
| Execution | hyperparameters, framework, compute | Define HOW training runs operationally |
| Evaluation | eval_strategy, eval_metrics, checkpointing | Define HOW quality is assessed during training |
| Safety | guardrail constraints, credential exclusion | Enforce training data safety and secret hygiene |

## Position in P02 (Model Pillar)
| Kind | Stage | Relationship |
|------|-------|-------------|
| agent | Design | Defines runtime agent persona |
| finetune_config | Training | Specifies how base model is adapted |
| model_card | Post-training | Documents trained model capabilities |
| model_provider | Runtime | Routes requests to model endpoints |
| boot_config | Runtime | Starts provider with correct settings |
| fallback_chain | Runtime | Degrades gracefully when provider fails |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_finetune_config]] | downstream | 0.57 |
| [[finetune-config-builder]] | upstream | 0.57 |
| [[p03_sp_finetune_config_builder]] | upstream | 0.46 |
| [[bld_schema_finetune_config]] | upstream | 0.41 |
| [[bld_collaboration_training_method]] | downstream | 0.41 |
| [[training-method-builder]] | upstream | 0.39 |
| [[p01_kc_finetune_config]] | upstream | 0.37 |
| [[p11_qg_finetune_config]] | downstream | 0.34 |
| [[p03_sp_training_method_builder]] | upstream | 0.34 |
| [[bld_examples_finetune_config]] | upstream | 0.32 |
