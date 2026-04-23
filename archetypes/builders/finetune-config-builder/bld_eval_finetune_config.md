---
kind: quality_gate
id: p11_qg_finetune_config
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of finetune_config artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: 9.0
title: "Gate: finetune_config"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, finetune-config, training, lora, peft, P11]
tldr: "Gates for finetune_config: validates adapter completeness, hyperparameter coverage, dataset spec, eval metrics, and no credentials."
domain: "finetune_config -- LLM fine-tuning job specifications with base model, adapter, dataset, hyperparameters, and eval metrics"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.92
related:
  - bld_examples_finetune_config
  - p02_qg_training_method
  - p03_sp_finetune_config_builder
  - bld_instruction_finetune_config
  - p11_qg_chunk_strategy
  - bld_schema_finetune_config
  - p11_qg_embedding_config
  - p11_qg_kind_builder
  - p11_qg_batch_config
  - p11_qg_retriever_config
---

## Quality Gate

# Gate: finetune_config
## Definition
| Field | Value |
|-------|-------|
| metric | Composite score from SOFT dimensions + all HARD gates pass |
| threshold | >= 7.0 to publish; >= 9.5 golden |
| operator | AND (all HARD) + weighted_sum (SOFT) |
| scope | All artifacts where `kind: finetune_config` |

## HARD Gates
All must pass. Any single failure = REJECT regardless of SOFT score.
| ID | Check | Failure message |
|----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | "Frontmatter YAML syntax error" |
| H02 | `id` matches `^p02_ft_[a-z][a-z0-9_]+$` | "ID fails finetune_config namespace regex" |
| H03 | `id` value equals filename stem | "ID does not match filename" |
| H04 | `kind` equals literal `"finetune_config"` | "Kind is not 'finetune_config'" |
| H05 | `quality` field is `null` | "Quality must be null at authoring time" |
| H06 | All required fields present: id, kind, pillar, base_model, adapter_type, dataset, version, created, author, tags, tldr | "Missing required field(s)" |
| H07 | `adapter_type` is from the enum: lora, qlora, full, prefix_tuning, p_tuning | "adapter_type not from allowed enum" |
| H08 | For adapter_type lora or qlora: rank (r), lora_alpha, lora_dropout, and target_modules are specified in body | "LoRA/QLoRA config missing required parameters" |
| H09 | For adapter_type qlora: bits and quant_type are specified in body | "QLoRA quantization parameters missing" |
| H10 | Hyperparameters section present and contains: learning_rate, per_device_train_batch_size, num_train_epochs or max_steps, warmup_ratio, lr_scheduler_type | "Required hyperparameters missing" |
| H11 | At least one eval_metric specified (frontmatter or Evaluation section) | "No evaluation metrics defined" |
| H12 | No credentials, API keys, HuggingFace tokens, or passwords in any field | "Credentials detected in artifact" |

## SOFT Scoring
Dimensions sum to 100%. Score each 0.0-10.0; multiply by weight.
| Dimension | Weight | What to assess |
|-----------|--------|----------------|
| Adapter config completeness | 1.5 | All adapter params specified; target_modules explicit, not default |
| Hyperparameter completeness | 1.5 | All 8 standard params present with explicit values, no TBD |
| Dataset specification quality | 1.0 | Format, field_mapping, size, preprocessing all documented |
| Evaluation strategy | 1.0 | eval_strategy, save_strategy, metric_for_best_model all set |
| Compute feasibility | 0.5 | VRAM requirement documented; max_seq_length consistent with compute |
| Effective batch size clarity | 1.0 | per_device_batch_size * gradient_accum * num_gpus documented |
| Base model justification | 0.5 | Model choice rationale stated in Overview |
| Task type accuracy | 0.5 | task_type (sft/dpo/rlhf/orpo) matches training paradigm |
| Framework alignment | 0.5 | framework specified and consistent with adapter/task type |
| Boundary clarity | 1.0 | Explicitly not model_provider (runtime), not model_card (docs) |
| Reproducibility | 1.0 | Config is executable as-is; no values require external lookup |
| Documentation density | 0.5 | tldr names model, adapter, task type, and key stats |
Weight sum: 1.5+1.5+1.0+1.0+0.5+1.0+0.5+0.5+0.5+1.0+1.0+0.5 = 10.0 (100%)

## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool as golden exemplar |
| >= 8.0 | PUBLISH | Publish to pool |
| >= 7.0 | REVIEW | Flag for human review before publish |
| < 7.0 | REJECT | Return to author with failure report |

## Bypass
| Field | Value |
|-------|-------|
| conditions | Exploratory configs where hyperparameters are intentionally under-specified for sweep |
| approver | ML lead approval required (written); H12 (no credentials) never bypassed |

## Examples

# Examples: finetune-config-builder
## Golden Example
INPUT: "Configure QLoRA fine-tuning of Llama-3-8B for instruction following on a custom dataset"
OUTPUT:
```yaml
id: p02_ft_llama3_8b_instruct_qlora
kind: finetune_config
pillar: P02
version: "1.0.0"
created: "2026-04-13"
updated: "2026-04-13"
author: "builder_agent"
base_model: "meta-llama/Meta-Llama-3-8B"
adapter_type: qlora
dataset: "data/instruct_train.jsonl"
quality: null
tags: [finetune_config, qlora, llama3, instruction-following, sft]
tldr: "QLoRA SFT on Llama-3-8B: rank=16, 4-bit NF4, 3 epochs, cosine LR, instruction dataset 50K rows"
description: "QLoRA fine-tune of Llama-3-8B for instruction following using a 50K-row Alpaca-format dataset"
task_type: sft
framework: trl
compute: "1x A10G 24GB or 1x RTX 4090 24GB"
eval_metrics:
  - eval_loss
  - perplexity
```
## Overview
Adapt Llama-3-8B to follow instructions in a custom domain using supervised fine-tuning.
QLoRA chosen to fit within 24GB VRAM while retaining near-full-fine-tune quality.
4-bit NF4 quantization of base model with LoRA adapters on attention and MLP projections.
## Base Model
| Field | Value |
|-------|-------|
| model_id | meta-llama/Meta-Llama-3-8B |
| architecture | llama3 |
| param_count | 8B |
| license | llama3 |
| quantization | 4bit (NF4, loaded for training) |
## Dataset
| Field | Value |
|-------|-------|
| path | data/instruct_train.jsonl |
| size | 50000 rows |
| format | alpaca |
| field_mapping | instruction / input / output |
| language | en |
| preprocessing | filter max_len=2048, deduplicate |
## Adapter Config
| Parameter | Value |
|-----------|-------|
| r (rank) | 16 |
| lora_alpha | 32 |
| lora_dropout | 0.05 |
| target_modules | q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj |
| bias | none |
| task_type | CAUSAL_LM |
| bits | 4 |
| quant_type | nf4 |
| double_quant | true |
## Hyperparameters
| Parameter | Value |
|-----------|-------|
| learning_rate | 2e-4 |
| per_device_train_batch_size | 2 |
| gradient_accumulation_steps | 8 |
| num_train_epochs | 3 |
| max_steps | -1 |
| warmup_ratio | 0.03 |
| lr_scheduler_type | cosine |
| weight_decay | 0.01 |
| max_grad_norm | 1.0 |
| fp16 | false |
| bf16 | true |
| gradient_checkpointing | true |
| optim | paged_adamw_8bit |
| max_seq_length | 2048 |
## Evaluation
| Parameter | Value |
|-----------|-------|
| eval_strategy | epoch |
| eval_steps | null |
| save_strategy | epoch |
| save_steps | null |
| save_total_limit | 3 |
| load_best_model_at_end | true |
| metric_for_best_model | eval_loss |
| early_stopping_patience | 2 |
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p02_ft_ pattern (H02 pass)
- kind: finetune_config (H04 pass)
- adapter_type from allowed enum (H06 pass)
- LoRA rank/alpha/dropout/target_modules all specified (H07 pass)
- QLoRA bits/quant_type specified (H08 pass)
- All required hyperparameters have explicit values (H09 pass)
- eval_metrics non-empty (H10 pass)
- No credentials anywhere (H03 pass)
- tldr: 92 chars <= 160 (S01 pass)
- tags: 5 items, includes "finetune_config" (S02 pass)
- All 6 body sections present (S03 pass)
## Anti-Example
INPUT: "fine-tune GPT for my data"
BAD OUTPUT:
```yaml
id: gpt-finetune
kind: training
pillar: models
adapter: lora
rank: TBD
dataset: my_data.csv
quality: 8.5
tags: [training]
```
Fine-tune GPT on my data. Use LoRA with rank TBD. Training settings TBD.
FAILURES:
1. id: "gpt-finetune" uses hyphens and no `p02_ft_` prefix -> H02 FAIL
2. kind: "training" not "finetune_config" -> H04 FAIL
3. pillar: "models" not "P02" -> H06 FAIL
4. quality: 8.5 (not null) -> H05 FAIL
5. adapter_type not from enum (uses "adapter") -> H06 FAIL
6. rank: TBD -- placeholder value for required param -> H09 FAIL
7. Missing fields: version, created, updated, author, base_model, tldr -> H06 FAIL
8. tags: only 1 item, missing "finetune_config" -> S02 FAIL
9. Body missing all 6 required sections -> S03 FAIL
10. No lora_alpha, dropout, target_modules specified -> H07 FAIL
11. No hyperparameters section at all -> H09 FAIL
12. No eval_metrics -> H10 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
