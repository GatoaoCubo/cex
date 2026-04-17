---
id: n00_training_method_manifest
kind: knowledge_card
pillar: P02
nucleus: n00
title: "Training Method -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, training_method, p02, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P02 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Training Method defines a model training or adaptation technique: the approach, data requirements, compute constraints, and expected outcomes. It covers the full spectrum from pre-training to fine-tuning, PEFT methods (LoRA, QLoRA), RLHF, and domain adaptation. Used as the BECOME specification when N03 or N05 designs model training pipelines.

## Pillar
P02 -- Model

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `training_method` |
| pillar | string | yes | Always `P02` |
| title | string | yes | Method name and technique |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| technique | enum | yes | pretrain\|sft\|lora\|qlora\|dpo\|rlhf\|rlaif\|orpo |
| data_type | enum | yes | instruction\|preference\|completion\|raw |
| min_gpu_vram_gb | int | yes | Minimum GPU VRAM required |
| expected_improvement | string | yes | What capability improves and by how much |
| training_time_hours | string | no | Approximate training duration |
| open_source_tools | list | no | Tools: Axolotl, Unsloth, TRL, HF Trainer |

## When to use
- When selecting a training approach for model adaptation
- When documenting a training methodology for reproducibility
- When comparing techniques for a specific capability improvement goal

## Builder
`archetypes/builders/training_method-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind training_method --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N03 or N05)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- ML engineers designing training pipelines
- `{{DOMAIN_CONTEXT}}` -- model size, task, and hardware constraints

## Example (minimal)
```yaml
---
id: training_method_qlora_4bit
kind: training_method
pillar: P02
nucleus: n03
title: "QLoRA 4-bit Fine-Tuning"
version: 1.0
quality: null
---
technique: qlora
data_type: instruction
min_gpu_vram_gb: 16
expected_improvement: "Domain-specific task performance +20-40% over base model"
training_time_hours: "4-8h for 9B model on single RTX 4090"
open_source_tools: [Unsloth, TRL, bitsandbytes]
```

## Related kinds
- `rl_algorithm` (P02) -- specific RL algorithm within RLHF/DPO methods
- `finetune_config` (P02) -- training job using this method
- `model_architecture` (P02) -- model architecture being trained
- `dataset_card` (P01) -- training data for this method
