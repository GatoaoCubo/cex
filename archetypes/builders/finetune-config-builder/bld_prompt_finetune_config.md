---
kind: instruction
id: bld_instruction_finetune_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for finetune_config
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 8.8
title: "Instruction Finetune Config"
version: "1.0.0"
author: n03_builder
tags: [finetune_config, builder, instruction, P02]
tldr: "3-phase process: research base model + adapter + dataset, compose all sections, validate gates."
domain: "finetune_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_instruction_training_method
  - bld_instruction_retriever_config
  - p03_sp_finetune_config_builder
  - bld_instruction_eval_dataset
  - bld_instruction_chunk_strategy
  - bld_instruction_output_validator
  - bld_instruction_env_config
  - bld_instruction_memory_scope
  - bld_instruction_experiment_config
  - bld_instruction_trace_config
---

# Instructions: How to Produce a finetune_config
## Phase 1: RESEARCH
1. Identify the target task: instruction following, chat, code generation, classification, preference alignment (SFT/DPO/RLHF/ORPO)
2. Select base model: model ID (HuggingFace hub or local path), architecture family (Llama, Mistral, Qwen, Phi, Gemma), parameter count
3. Determine adapter type based on compute budget:
   - Full GPU farm (A100 80GB+): consider full fine-tune
   - Single GPU (24GB): LoRA or prefix_tuning
   - Consumer GPU (8-16GB VRAM): QLoRA (4-bit quantization)
4. Catalog dataset: source path or identifier, size (rows), format (Alpaca/ShareGPT/custom), field names, language
5. Determine hyperparameters: start from documented baselines for the base model family
6. Define evaluation strategy: metrics (eval_loss, BLEU, ROUGE, accuracy), eval frequency, held-out split size
7. Check existing finetune_configs via brain_query [IF MCP] -- do not duplicate a config that already covers this base model + task
## Phase 2: COMPOSE
1. Read SCHEMA.md -- source of truth for all fields
2. Read OUTPUT_TEMPLATE.md -- fill the template following SCHEMA constraints
3. Fill all required frontmatter fields; set `quality: null` -- never self-score
4. Write **Overview** section: target task, base model choice rationale, adapter type justification (1 sentence each)
5. Write **Base Model** section: table with model_id, architecture, param_count, license, quantization (if any)
6. Write **Dataset** section: table with path/identifier, size, format, field_mapping (instruction/input/output or user/assistant), language, preprocessing steps
7. Write **Adapter Config** section: all adapter parameters in table -- for LoRA: rank, alpha, dropout, target_modules; for QLoRA: add bits, quantization_type
8. Write **Hyperparameters** section: table with all training hyperparameters and their values
9. Write **Evaluation** section: table with eval metrics, checkpoint strategy, save_total_limit, early_stopping (if any)
10. Confirm body <= 4096 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md -- verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm `id` matches `^p02_ft_[a-z][a-z0-9_]+$`
4. Confirm adapter_type is from the allowed enum (lora, qlora, full, prefix_tuning, p_tuning)
5. Confirm all required hyperparameters have explicit numeric values (no TBD or null)
6. Confirm LoRA/QLoRA configs include rank, alpha, dropout, target_modules
7. Confirm dataset section includes format and field_mapping
8. Confirm at least one eval_metric is specified
9. Confirm no credentials, API keys, or tokens appear in any field
10. Confirm `quality` is null
11. Confirm body <= 4096 bytes
12. Cross-check: is this a training specification? If this configures runtime API routing it belongs in `model_provider`. If it documents a trained model it belongs in `model_card`. If it starts a provider it belongs in `boot_config`. This artifact specifies HOW to train/adapt, not HOW to serve.
13. If score < 8.0: revise in the same pass before outputting


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_training_method]] | sibling | 0.48 |
| [[bld_instruction_retriever_config]] | sibling | 0.40 |
| [[p03_sp_finetune_config_builder]] | related | 0.39 |
| [[bld_instruction_eval_dataset]] | sibling | 0.39 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.39 |
| [[bld_instruction_output_validator]] | sibling | 0.39 |
| [[bld_instruction_env_config]] | sibling | 0.38 |
| [[bld_instruction_memory_scope]] | sibling | 0.38 |
| [[bld_instruction_experiment_config]] | sibling | 0.37 |
| [[bld_instruction_trace_config]] | sibling | 0.37 |
