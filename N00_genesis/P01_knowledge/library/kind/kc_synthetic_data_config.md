---
id: kc_synthetic_data_config
kind: knowledge_card
8f: F3_inject
title: Synthetic Data Config -- Training Data Generation Pipeline
version: 1.0.0
quality: null
pillar: P01
tags:
  - synthetic-data
  - data-generation
  - training
  - data-centric
  - P01
related:
  - kc_dataset_card
  - kc_eval_dataset
  - kc_finetune_config
  - kc_chunk_strategy
  - kc_embedding_config
  - kc_curriculum_config
---

# Synthetic Data Config

A synthetic data config defines the pipeline for generating artificial training data from seed examples. In the data-centric AI paradigm, model performance is bounded by data quality more than architecture -- synthetic data generation is the systematic approach to breaking that bound by manufacturing high-quality training examples at scale.

## Description

Real-world training data is expensive, biased, sparse in edge cases, and often legally encumbered. Synthetic data generation addresses all four constraints: it scales cheaply, can be deliberately balanced, targets underrepresented scenarios, and carries no privacy burden (when done correctly).

The config governs the full pipeline: seed selection (what real examples bootstrap the generator), augmentation strategies (how to create variants), quality filtering (how to reject bad generations), deduplication (how to prevent memorization amplifiers), and format templates (how to structure the output for the training framework).

The core insight from data-centric AI: spending 10x on data quality beats spending 10x on model size. A synthetic data config operationalizes that insight.

## Key Concepts

| Concept | Definition | Importance |
|---------|-----------|------------|
| Seed Data | Real-world examples that bootstrap the generation process | High -- seed quality upper-bounds synthetic quality |
| Augmentation Strategy | Method for creating variants (paraphrase, backtranslation, perturbation) | High -- determines diversity of output |
| Quality Filter | Automated gate that rejects low-quality generations | Critical -- unfiltered synthetic data poisons training |
| Deduplication | Near-duplicate and exact-duplicate removal across the synthetic corpus | High -- duplicates cause memorization, not generalization |
| Format Template | Structural schema for generated examples (instruction/response, QA, etc.) | Medium -- must match the training framework's input spec |
| Temperature Sweep | Generating at multiple temperatures to balance diversity and coherence | Medium -- single temperature creates monotone distributions |
| Self-Consistency Check | Validating that generated answers are consistent across rephrasings | High -- inconsistent data teaches the model to be unreliable |
| Contamination Guard | Ensuring synthetic data does not leak test set information | Critical -- invalidates all downstream evaluation |

## Related Kinds

| Kind | Pillar | Relationship |
|------|--------|-------------|
| dataset_card | P01 | Sibling -- dataset_card documents a dataset; synthetic_data_config creates one |
| eval_dataset | P07 | Downstream -- synthetic data must never contaminate eval datasets |
| finetune_config | P02 | Downstream -- consumes the synthetic dataset for training |
| curriculum_config | P07 | Downstream -- orders the synthetic data for progressive training |
| chunk_strategy | P01 | Upstream -- chunking affects what seed data is available |
| prompt_template | P03 | Tool -- generation prompts drive the synthetic pipeline |
| quality_gate | P11 | Tool -- gates filter synthetic output |

## Anti-Patterns

- **Generate-and-ship**: Producing synthetic data without quality filtering. Even large language models generate nonsense, contradictions, and formatting errors at non-trivial rates.
- **Seed leakage**: Using test set examples as seeds. The synthetic data inherits test-set patterns, making evaluation meaningless.
- **Monoculture generation**: Using a single model at a single temperature. The synthetic distribution collapses to the generator's mode, teaching the student model to parrot one style.
- **No deduplication**: Near-duplicates cause the model to memorize specific phrasings rather than learn the underlying pattern. Use embedding-based dedup, not just exact string matching.
- **Ignoring provenance**: Not tracking which seed produced which synthetic examples. When downstream performance degrades, you cannot diagnose whether the problem is seed quality or augmentation strategy.

## Properties

| Property | Value |
|----------|-------|
| Kind | knowledge_card |
| Pillar | P01 |
| Domain | Training data engineering |
| Pipeline | 8F (F1-F8) |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_dataset_card]] | sibling | 0.42 |
| [[kc_finetune_config]] | downstream | 0.40 |
| [[kc_eval_dataset]] | sibling | 0.38 |
| [[kc_curriculum_config]] | downstream | 0.35 |
| [[kc_chunk_strategy]] | upstream | 0.32 |
| [[kc_prompt_template]] | tool | 0.30 |
| [[kc_quality_gate]] | tool | 0.28 |
| [[kc_embedding_config]] | related | 0.25 |
