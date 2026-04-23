---
kind: schema
id: bld_schema_finetune_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for finetune_config
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 8.9
title: "Schema Finetune Config"
version: "1.0.0"
author: n03_builder
tags: [finetune_config, builder, schema, P02, training]
tldr: "Schema for finetune_config artifacts: training job specs with base model, adapter, dataset, hyperparameters, and eval metrics."
domain: "finetune_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_output_validator
  - bld_schema_eval_dataset
  - bld_schema_handoff_protocol
  - bld_schema_memory_scope
  - bld_schema_chunk_strategy
  - bld_schema_constraint_spec
  - bld_schema_prompt_version
  - bld_schema_golden_test
  - bld_schema_smoke_eval
---

# Schema: finetune_config
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p02_ft_{name}) | YES | - | Namespace compliance |
| kind | literal "finetune_config" | YES | - | Type integrity |
| pillar | literal "P02" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| base_model | string | YES | - | HuggingFace model ID or local path |
| adapter_type | enum: lora, qlora, full, prefix_tuning, p_tuning | YES | - | Adaptation method |
| dataset | string | YES | - | Dataset identifier or path |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "finetune_config" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What this fine-tune achieves |
| task_type | enum: sft, dpo, rlhf, orpo, reward_modeling | REC | sft | Training paradigm |
| framework | enum: transformers, axolotl, unsloth, llamafactory, trl | REC | transformers | Training framework |
| compute | string | REC | - | GPU/TPU requirement summary |
| eval_metrics | list[string] | REC | - | Metrics tracked during training |
## ID Pattern
Regex: `^p02_ft_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` -- what model is being adapted, why, target task
2. `## Base Model` -- model ID, architecture, parameter count, licensing
3. `## Dataset` -- dataset path, size, format, preprocessing steps
4. `## Adapter Config` -- adapter type with all type-specific parameters
5. `## Hyperparameters` -- learning rate, batch size, epochs, scheduler, warmup
6. `## Evaluation` -- metrics, eval frequency, checkpointing strategy
## Constraints
- max_bytes: 4096 (body only)
- naming: p02_ft_{name}.yaml
- machine_format: yaml (compiled artifact)
- id == filename stem
- quality: null always
- adapter_type MUST be from the allowed enum
- All numeric hyperparameters MUST have explicit values (no TBD or null for required params)
- NEVER include API keys, access tokens, or credentials in any field

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.64 |
| [[bld_schema_output_validator]] | sibling | 0.63 |
| [[bld_schema_eval_dataset]] | sibling | 0.62 |
| [[bld_schema_handoff_protocol]] | sibling | 0.62 |
| [[bld_schema_memory_scope]] | sibling | 0.62 |
| [[bld_schema_chunk_strategy]] | sibling | 0.62 |
| [[bld_schema_constraint_spec]] | sibling | 0.61 |
| [[bld_schema_prompt_version]] | sibling | 0.61 |
| [[bld_schema_golden_test]] | sibling | 0.61 |
| [[bld_schema_smoke_eval]] | sibling | 0.61 |
