---
kind: instruction
id: bld_instruction_training_method
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for training_method
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 8.9
title: "Instruction Training Method"
version: "1.0.0"
author: n05_builder
tags: [training_method, builder, instruction, P02]
tldr: "3-phase process: research paradigm + compute + dataset, compose all sections, validate gates."
domain: "training_method construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_instruction_finetune_config
  - training-method-builder
  - p02_qg_training_method
  - bld_instruction_retriever_config
  - bld_instruction_output_validator
  - bld_instruction_memory_scope
  - bld_schema_training_method
  - bld_instruction_chunk_strategy
  - bld_instruction_context_doc
  - p03_sp_training_method_builder
---

# Instructions: How to Produce a training_method
## Phase 1: RESEARCH
1. Identify the learning paradigm: supervised, unsupervised, self-supervised, reinforcement learning, transfer learning, or hybrid
2. Determine compute intensity based on model scale:
   - Low (CPU or single GPU): small models, classic ML, linear/tree-based
   - Medium (1-4 GPU): mid-scale neural nets, BERT-scale, LoRA fine-tunes
   - High (multi-GPU/TPU): LLM pre-training, large vision models, foundation models
3. Catalog dataset requirements: source, size, label format, preprocessing pipeline
4. Identify key hyperparameters for the chosen paradigm (optimizer, LR, batch size, epochs)
5. Define evaluation strategy: metrics, validation frequency, convergence criteria
6. Check existing training_method artifacts via retriever -- avoid duplicating a spec that covers the same paradigm and domain
## Phase 2: COMPOSE
1. Read bld_schema_training_method.md -- source of truth for all required fields
2. Read bld_output_template_training_method.md -- fill the template following schema constraints
3. Fill all required frontmatter: id, kind, pillar, title, version, learning_paradigm, compute_intensity, quality: null
4. Write **Overview** section: paradigm choice rationale, target model type, compute justification (1 sentence each)
5. Write **Learning Paradigm** section: table with paradigm type, objective function, label requirements, typical use cases
6. Write **Compute Profile** section: table with compute_intensity, hardware target, memory requirements, typical training time
7. Write **Hyperparameters** section: table with all key hyperparameters and recommended ranges
8. Write **Dataset Requirements** section: table with source, size, format, preprocessing, label schema
9. Write **Evaluation** section: table with metrics, validation strategy, convergence criteria
10. Confirm body <= 4096 bytes
## Phase 3: VALIDATE
1. Check bld_quality_gate_training_method.md -- verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm `id` matches naming pattern (e.g., `p02_tm_[a-z][a-z0-9_]+`)
4. Confirm `learning_paradigm` is from allowed enum: supervised, unsupervised, reinforcement, self_supervised, transfer, hybrid
5. Confirm `compute_intensity` is from allowed enum: low, medium, high
6. Confirm all required hyperparameters have documented values or ranges
7. Confirm dataset section includes format and preprocessing steps
8. Confirm at least one evaluation metric is specified
9. Confirm no credentials, API keys, or tokens appear in any field
10. Confirm `quality` is null
11. Confirm body <= 4096 bytes
12. Cross-check: is this a training paradigm specification? If it specifies a fine-tuning job it belongs in `finetune_config`. If it documents a trained model it belongs in `model_card`. If it defines an RL reward signal it belongs in `reward_model`.
13. If score < 8.0: revise in the same pass before outputting


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_finetune_config]] | sibling | 0.49 |
| [[training-method-builder]] | upstream | 0.40 |
| [[p02_qg_training_method]] | downstream | 0.40 |
| [[bld_instruction_retriever_config]] | sibling | 0.39 |
| [[bld_instruction_output_validator]] | sibling | 0.39 |
| [[bld_instruction_memory_scope]] | sibling | 0.38 |
| [[bld_schema_training_method]] | downstream | 0.38 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.38 |
| [[bld_instruction_context_doc]] | sibling | 0.38 |
| [[p03_sp_training_method_builder]] | related | 0.38 |
