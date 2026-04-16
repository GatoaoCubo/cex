---
kind: config
id: bld_config_finetune_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.1
title: "Config Finetune Config"
version: "1.0.0"
author: n03_builder
tags: [finetune_config, builder, config, P02]
tldr: "Operational rules for finetune_config production: naming, paths, size limits, adapter enums, task enums."
domain: "finetune_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---
# Config: finetune_config Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p02_ft_{name}.yaml` | `p02_ft_llama3_8b_instruct_qlora.yaml` |
| Builder directory | kebab-case | `finetune-config-builder/` |
| Frontmatter fields | snake_case | `adapter_type`, `base_model`, `task_type` |
| Name slug | snake_case, lowercase, no hyphens | `llama3_8b_instruct_qlora`, `mistral_7b_sft` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
Name slug SHOULD encode: model_family + param_count + adapter_type (+ task if non-SFT).

## File Paths
1. Output: `P02_model/examples/p02_ft_{name}.yaml`
2. Compiled: `P02_model/compiled/p02_ft_{name}.yaml`
3. Builder: `archetypes/builders/finetune-config-builder/`

## Size Limits (aligned with SCHEMA)
1. Body: max 4096 bytes
2. Total (frontmatter + body): ~5500 bytes
3. Density: >= 0.80 (no filler prose)

## Adapter Type Enum (canonical values)
| Value | Full name | When |
|-------|-----------|------|
| lora | Low-Rank Adaptation | Standard parameter-efficient fine-tune |
| qlora | Quantized LoRA | Memory-constrained GPU (< 24GB VRAM) |
| full | Full fine-tune | All parameters updated; large compute budget |
| prefix_tuning | Prefix Tuning | Prepend trainable tokens; lightweight |
| p_tuning | Prompt Tuning | Virtual tokens via MLP; classification tasks |

## Task Type Enum (canonical values)
| Value | Full name | Dataset format |
|-------|-----------|---------------|
| sft | Supervised Fine-Tuning | instruction/response pairs |
| dpo | Direct Preference Optimization | prompt/chosen/rejected triples |
| rlhf | Reinforcement Learning from Human Feedback | prompts + reward model |
| orpo | Odds Ratio Preference Optimization | prompt/chosen/rejected triples |
| reward_modeling | Reward Model Training | preference pairs with scores |

## Framework Enum (canonical values)
| Value | Notes |
|-------|-------|
| transformers | HuggingFace Trainer; most flexible |
| trl | HuggingFace TRL; SFTTrainer, DPOTrainer |
| axolotl | YAML-first config; great for QLoRA |
| unsloth | Optimized QLoRA; fastest on consumer GPUs |
| llamafactory | Multi-model, multi-task; good for non-English |

## Metadata

```yaml
id: bld_config_finetune_config
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld_config_finetune_config.md
```
