---
kind: output_template
id: bld_output_template_finetune_config
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a finetune_config artifact
pattern: every field here exists in SCHEMA.md -- template derives, never invents
quality: 9.1
title: "Output Template Finetune Config"
version: "1.0.0"
author: n03_builder
tags: [finetune_config, builder, template, P02]
tldr: "Fill-in template for finetune_config: base model, adapter, dataset, hyperparameters, eval."
domain: "finetune_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_examples_finetune_config
  - p11_qg_finetune_config
  - bld_instruction_finetune_config
  - p03_sp_finetune_config_builder
  - bld_knowledge_card_finetune_config
  - bld_schema_finetune_config
  - p01_kc_finetune_config
  - bld_config_finetune_config
  - bld_tools_finetune_config
  - bld_architecture_finetune_config
---

# Output Template: finetune_config
```yaml
id: p02_ft_{{name}}
kind: finetune_config
pillar: P02
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
base_model: "{{huggingface_model_id_or_local_path}}"
adapter_type: {{lora|qlora|full|prefix_tuning|p_tuning}}
dataset: "{{dataset_identifier_or_path}}"
quality: null
tags: [finetune_config, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_adaptation_achieves_max_200ch}}"
task_type: {{sft|dpo|rlhf|orpo|reward_modeling}}
framework: {{transformers|axolotl|unsloth|llamafactory|trl}}
compute: "{{gpu_requirement_summary}}"
eval_metrics:
  - {{metric_1}}
  - {{metric_2}}
```
## Overview
`{{target_task_one_sentence}}`
`{{base_model_choice_rationale_one_sentence}}`
`{{adapter_type_justification_one_sentence}}`
## Base Model
| Field | Value |
|-------|-------|
| model_id | `{{huggingface_id_or_path}}` |
| architecture | {{llama3|mistral|qwen2|phi3|gemma|other}} |
| param_count | {{7B|13B|70B|etc}} |
| license | {{apache-2.0|llama3|mit|other}} |
| quantization | {{none|4bit|8bit}} |
## Dataset
| Field | Value |
|-------|-------|
| path | `{{dataset_path_or_hf_identifier}}` |
| size | `{{N_rows}}` rows |
| format | {{alpaca|sharegpt|custom|preference}} |
| field_mapping | {{instruction/input/output or user/assistant}} |
| language | {{en|pt|multilingual}} |
| preprocessing | {{none|tokenize_only|filter_max_len|etc}} |
## Adapter Config
### LoRA / QLoRA
| Parameter | Value |
|-----------|-------|
| r (rank) | {{4|8|16|32|64}} |
| lora_alpha | {{16|32|64}} |
| lora_dropout | {{0.05|0.1}} |
| target_modules | {{q_proj,v_proj|all-linear}} |
| bias | {{none|lora_only|all}} |
| task_type | {{CAUSAL_LM|SEQ_CLS}} |
| bits (QLoRA only) | {{4|8}} |
| quant_type (QLoRA only) | {{nf4|fp4}} |
| double_quant (QLoRA only) | {{true|false}} |
## Hyperparameters
| Parameter | Value |
|-----------|-------|
| learning_rate | {{2e-4|1e-4|5e-5}} |
| per_device_train_batch_size | {{1|2|4|8}} |
| gradient_accumulation_steps | {{4|8|16}} |
| num_train_epochs | {{1|2|3}} |
| max_steps | {{-1 or N}} |
| warmup_ratio | {{0.03|0.05}} |
| lr_scheduler_type | {{cosine|linear|constant_with_warmup}} |
| weight_decay | {{0.0|0.01}} |
| max_grad_norm | {{1.0}} |
| fp16 | {{true|false}} |
| bf16 | {{true|false}} |
| gradient_checkpointing | {{true|false}} |
| optim | {{adamw_torch|paged_adamw_8bit|adamw_bnb_8bit}} |
| max_seq_length | {{512|1024|2048|4096}} |
## Evaluation
| Parameter | Value |
|-----------|-------|
| eval_strategy | {{steps|epoch}} |
| eval_steps | `{{N or null}}` |
| save_strategy | {{steps|epoch}} |
| save_steps | `{{N or null}}` |
| save_total_limit | {{2|3|5}} |
| load_best_model_at_end | {{true|false}} |
| metric_for_best_model | {{eval_loss|accuracy}} |
| early_stopping_patience | `{{N or null}}` |
## References
- `{{base_model_paper_or_hf_page}}`
- `{{dataset_source}}`
- `{{framework_docs}}`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_finetune_config]] | downstream | 0.53 |
| [[p11_qg_finetune_config]] | downstream | 0.39 |
| [[bld_instruction_finetune_config]] | upstream | 0.34 |
| [[p03_sp_finetune_config_builder]] | upstream | 0.34 |
| [[bld_knowledge_card_finetune_config]] | upstream | 0.32 |
| [[bld_schema_finetune_config]] | downstream | 0.31 |
| [[p01_kc_finetune_config]] | upstream | 0.29 |
| [[bld_config_finetune_config]] | downstream | 0.29 |
| [[bld_tools_finetune_config]] | upstream | 0.27 |
| [[bld_architecture_finetune_config]] | downstream | 0.24 |
