---
id: n00_finetune_config_manifest
kind: knowledge_card
pillar: P02
nucleus: n00
title: "Finetune Config -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, finetune_config, p02, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P02 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Finetune Config specifies the complete configuration for a model fine-tuning job: base model, training hyperparameters, dataset reference, evaluation strategy, and stopping criteria. It constrains the training pipeline to produce a consistent, reproducible fine-tuned model. Used when adapting a foundation model to specific CEX domains or tasks.

## Pillar
P02 -- Model

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `finetune_config` |
| pillar | string | yes | Always `P02` |
| title | string | yes | Job name and target model |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| base_model | string | yes | Foundation model identifier |
| method | enum | yes | full\|lora\|qlora\|dpo\|orpo\|sft |
| dataset_ref | string | yes | Reference to dataset_card artifact |
| learning_rate | float | yes | Training learning rate |
| num_epochs | int | yes | Number of training epochs |
| batch_size | int | yes | Per-device training batch size |
| eval_strategy | enum | yes | epoch\|steps\|no |

## When to use
- When adapting a foundation model to CEX-specific 8F output format
- When creating a domain-specialized model for a vertical
- When running DPO/ORPO alignment training on preference data

## Builder
`archetypes/builders/finetune_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind finetune_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N03 or N05)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- ML engineers running training jobs
- `{{DOMAIN_CONTEXT}}` -- task domain and adaptation target

## Example (minimal)
```yaml
---
id: finetune_config_gemma2_8f_sft
kind: finetune_config
pillar: P02
nucleus: n05
title: "Gemma2 9B 8F SFT Fine-Tune"
version: 1.0
quality: null
---
base_model: gemma2:9b
method: lora
dataset_ref: dataset_card_cex_8f_ft_v1
learning_rate: 0.0002
num_epochs: 3
batch_size: 4
eval_strategy: epoch
```

## Related kinds
- `dataset_card` (P01) -- training dataset this config uses
- `training_method` (P02) -- training technique specification
- `model_card` (P02) -- the resulting fine-tuned model documentation
