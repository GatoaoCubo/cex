---
kind: knowledge_card
id: bld_knowledge_synthetic_data_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for synthetic_data_config production -- synthetic dataset generation configuration
sources: Self-Instruct (Wang 2023), Alpaca, Evol-Instruct, distillation literature
quality: null
title: "Synthetic Data Config Builder - Knowledge ISO"
version: "1.0.0"
author: n03_builder
tags: [synthetic_data_config, builder, knowledge]
tldr: "Domain knowledge for building synthetic data configs covering generation methods, quality filtering, and decontamination."
domain: "synthetic data generation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_model_synthetic_data_config
  - bld_schema_synthetic_data_config
---

# Domain Knowledge: synthetic_data_config

## Executive Summary

Synthetic data configs define how to generate artificial training data for LLM fine-tuning, evaluation, or augmentation. They specify the generation method (self-instruct, evol-instruct, backtranslation), source model, output format, quality filters, and decontamination rules. A synthetic_data_config is a P01 artifact -- it configures the DATA GENERATION process, not the model training itself.

## Spec Table

| Property | Value |
|----------|-------|
| Pillar | P01 (knowledge) |
| Generation methods | self-instruct, evol-instruct, backtranslation, paraphrase, seed-expand |
| Quality filters | perplexity, dedup, length, toxicity, relevance |
| Output formats | JSONL, Alpaca, ShareGPT, ChatML |
| Decontamination | n-gram overlap removal against eval sets |

## Patterns

- **Self-Instruct** -- LLM generates instruction-response pairs from seed examples; cost-effective but quality varies
- **Evol-Instruct** -- iteratively increase complexity of instructions; produces harder training examples
- **Seed expansion** -- start with N human-written examples, expand to 10x-100x via LLM generation
- **Quality filtering** -- always filter generated data; perplexity threshold removes incoherent samples
- **Decontamination** -- mandatory before evaluation; remove overlap with benchmark test sets
- **Diversity** -- track topic/format distribution to avoid mode collapse in generated data

## Anti-Patterns

| Anti-Pattern | Why it fails |
|-------------|-------------|
| No quality filter | Generated data contains noise that degrades fine-tuned model |
| No decontamination | Benchmark scores inflated by training on test data |
| Single seed example | Generated data lacks diversity, overfits to seed style |
| No format validation | Malformed outputs break training pipeline |
| Ignoring source model bias | Generated data inherits and amplifies source model weaknesses |
| No cost tracking | Generation costs accumulate without budget awareness |
