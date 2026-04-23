---
kind: knowledge_card
id: bld_knowledge_curriculum_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for curriculum_config production -- training curriculum and data scheduling
sources: curriculum learning (Bengio 2009), data mixing, multi-task scheduling, annealing
quality: null
title: "Curriculum Config Builder - Knowledge ISO"
version: "1.0.0"
author: n03_builder
tags: [curriculum_config, builder, knowledge]
tldr: "Domain knowledge for curriculum config: training data ordering, difficulty progression, and data mixing strategies."
domain: "training curriculum"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_model_curriculum_config
  - bld_schema_curriculum_config
---

# Domain Knowledge: curriculum_config

## Executive Summary

Curriculum configs define the order and proportion in which training data is presented to a model during fine-tuning or pretraining. They specify difficulty progression, data mixing ratios, task scheduling, and annealing strategies. A curriculum_config is a P07 artifact -- it defines the TRAINING SCHEDULE, not the model architecture or data content.

## Spec Table

| Property | Value |
|----------|-------|
| Pillar | P07 (evaluation) |
| Strategies | easy-to-hard, self-paced, competence-based, data mixing |
| Scheduling | linear, exponential, step-wise, cosine annealing |
| Key parameters | difficulty metric, mixing ratios, warmup fraction, annealing schedule |

## Patterns

- **Easy-to-hard** -- present simpler examples first, gradually increase difficulty; accelerates convergence
- **Self-paced** -- model selects training examples based on current loss; adapts to model capacity
- **Competence-based** -- unlock harder data when model demonstrates competence on easier data
- **Data mixing** -- blend multiple data sources in specified ratios; ratios may shift over training
- **Annealing** -- gradually shift data distribution from general to domain-specific toward end of training
- **Multi-task scheduling** -- cycle through tasks in specified proportions per training step

## Anti-Patterns

| Anti-Pattern | Why it fails |
|-------------|-------------|
| Random ordering only | Misses curriculum benefits; wastes training compute on noise early |
| No difficulty metric | Cannot implement curriculum without defining what "hard" means |
| Fixed mixing forever | Optimal ratios change as model learns; static mixing suboptimal |
| No warmup | Jumping to hard examples early causes training instability |
| Ignoring data quality | Curriculum on noisy data amplifies noise in the chosen order |
