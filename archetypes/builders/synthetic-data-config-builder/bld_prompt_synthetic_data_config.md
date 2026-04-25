---
kind: instruction
id: bld_prompt_synthetic_data_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for synthetic_data_config
pattern: 3-phase pipeline (research -> compose -> validate)
quality: null
title: "Synthetic Data Config Builder - Prompt ISO"
version: "1.0.0"
author: n03_builder
tags: [synthetic_data_config, builder, instruction]
tldr: "Step-by-step instructions for producing synthetic data config artifacts."
domain: "synthetic data generation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_model_synthetic_data_config
  - bld_schema_synthetic_data_config
---

# Instructions: How to Produce a synthetic_data_config

## Phase 1: RESEARCH

1. Identify the purpose: fine-tuning, evaluation augmentation, or data bootstrapping
2. Select generation method: self-instruct, evol-instruct, backtranslation, seed-expand
3. Determine source model for generation (teacher model)
4. Define seed example requirements: count, diversity, domain coverage
5. Identify target output format: JSONL, Alpaca, ShareGPT, ChatML
6. Check existing synthetic_data_config artifacts to avoid duplication

## Phase 2: COMPOSE

1. Read SCHEMA -- source of truth for all fields
2. Read OUTPUT TEMPLATE -- fill following schema constraints
3. Fill all frontmatter fields; set quality: null
4. Write Generation Method section: method, source model, temperature, sampling
5. Write Seed Examples section: count, format, diversity requirements
6. Write Quality Filters section: perplexity, dedup, length, toxicity thresholds
7. Write Decontamination section: eval set overlap removal methodology
8. Write Output Format section: schema, field names, validation rules

## Phase 3: VALIDATE

1. Check HARD gates: YAML parses, id matches pattern, kind correct
2. Verify generation method specified with parameters
3. Verify quality filters defined with numeric thresholds
4. Verify decontamination rules reference specific eval sets
5. Cross-check: this is GENERATION CONFIG, not training config or eval config
6. If score < 8.0: revise before outputting

## Token Budget

| Component | Allocation | Notes |
|-----------|-----------|-------|
| System prompt | 15%% | Builder identity + sin lens |
| Context (ISOs) | 40%% | 12 ISOs loaded per builder |
| Domain knowledge | 25%% | KCs + examples + memory |
| Generation headroom | 20%% | Artifact output space |

## Style Constraints

| Dimension | Guideline |
|-----------|-----------|
| Voice | Technical, precise, builder-appropriate |
| Structure | Tables over prose; data over description |
| Density | >= 0.85; every sentence adds information |
| References | Use canonical kind names, not synonyms |

## Properties

| Property | Value |
|----------|-------|
| Kind | `prompt` |
| Pillar | P03 |
| Domain | synthetic data config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
