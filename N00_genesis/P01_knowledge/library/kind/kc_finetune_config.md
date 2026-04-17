---
id: p01_kc_finetune_config
kind: knowledge_card
type: kind
pillar: P02
title: "finetune_config: Model Fine-Tuning Configuration"
version: 1.0.0
created: 2026-04-12
updated: 2026-04-12
author: n03_builder
domain: finetune_config
quality: 9.1
tags: [finetune_config, p02, CONSTRAIN, kind-kc]
tldr: "Defines how to fine-tune a base model -- adapter type, hyperparams, dataset, eval metrics, output path"
when_to_use: "Building, reviewing, or reasoning about finetune_config artifacts"
keywords: [fine-tuning, LoRA, PEFT, QLoRA, adapter, training]
feeds_kinds: [finetune_config]
density_score: null
---

# Finetune Config

## Spec
```yaml
kind: finetune_config
pillar: P02
llm_function: CONSTRAIN
max_bytes: 2048
naming: p02_ft_{{model}}_{{adapter}}.yaml
core: false
```

## What It Is
A finetune_config specifies everything needed to fine-tune a base LLM: the dataset reference, base model identifier, adapter type (LoRA, QLoRA, full), hyperparameters (learning rate, epochs, rank, alpha), evaluation metrics, and output model path. It is NOT a model_provider (P02, which configures runtime inference routing) nor a model_card (P02, which describes a model's capabilities). The finetune_config governs the TRAINING step -- transforming a general model into a domain-specialized one.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| HuggingFace PEFT | `LoraConfig`, `PeftConfig` | `r`, `lora_alpha`, `target_modules`, `task_type` |
| HuggingFace Trainer | `TrainingArguments` | `learning_rate`, `num_train_epochs`, `per_device_train_batch_size` |
| OpenAI Fine-tuning | `POST /fine_tuning/jobs` | `training_file`, `model`, `hyperparameters.n_epochs` |
| Anthropic | No public fine-tuning API | Enterprise-only; constitutional AI alignment |
| Axolotl | `axolotl.yaml` config | Full YAML config: base_model, datasets, adapter, lr_scheduler |
| Unsloth | `FastLanguageModel.get_peft_model()` | 2x faster LoRA; `r`, `lora_alpha`, `target_modules` |
| LitGPT | `finetune/lora.py` | CLI-driven: `litgpt finetune --config config.yaml` |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| base_model | string | required | Larger model = better quality but higher VRAM/cost |
| adapter_type | enum(lora/qlora/full) | lora | LoRA = efficient; QLoRA = 4-bit quantized; full = maximum quality |
| rank (r) | int | 16 | Higher rank = more parameters = better fit but slower/larger |
| lora_alpha | int | 32 | alpha/r ratio controls effective learning rate scaling |
| learning_rate | float | 2e-4 | Too high = catastrophic forgetting; too low = underfitting |
| epochs | int | 3 | More epochs on small data = overfitting risk |
| dataset_path | string | required | JSONL with instruction/input/output or messages format |
| eval_split | float | 0.1 | Held-out fraction for validation loss tracking |
| output_path | string | required | Where to save adapter weights or merged model |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| LoRA rank-16 | General domain adaptation, moderate VRAM | Llama 3 8B + domain Q&A dataset |
| QLoRA 4-bit | Limited VRAM (<16GB), acceptable quality tradeoff | 70B model on single GPU via bitsandbytes |
| Full fine-tune | Maximum quality, large compute budget | GPT-4 class via OpenAI API |
| Merged export | Deploy without adapter overhead | `model.merge_and_unload()` after training |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Training on <100 examples | Model memorizes, doesn't generalize | Minimum 500+ diverse examples or use few-shot instead |
| High rank on small dataset | Overfits rapidly, wastes compute | Start with r=8, increase only if val loss plateaus |
| Ignoring eval metrics | No signal for early stopping | Track val_loss + task-specific metric (F1, BLEU) |
| Mixing adapter with full weights | Undefined behavior, corrupt model | Choose one: adapter OR full fine-tune, never both |

## Integration Graph
```
[eval_dataset] --> [finetune_config] --> [model_card (updated)]
                        |
                 [base model_provider]
                        |
                 [output adapter/merged model]
```

## Decision Tree
- IF <1000 examples AND quick iteration THEN few-shot prompting (skip fine-tune)
- IF VRAM < 16GB THEN QLoRA with r=16
- IF VRAM 16-48GB THEN LoRA with r=16-64
- IF unlimited compute + maximum quality THEN full fine-tune or OpenAI API
- DEFAULT: LoRA r=16, alpha=32, lr=2e-4, 3 epochs

## Quality Criteria
- GOOD: Base model + adapter type + dataset path + hyperparams specified
- GREAT: Eval metrics defined; early stopping configured; output path with versioning
- FAIL: No dataset reference; no eval strategy; rank/alpha ratio unjustified
