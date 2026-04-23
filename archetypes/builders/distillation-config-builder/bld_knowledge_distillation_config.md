---
kind: knowledge_card
id: bld_knowledge_distillation_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for distillation_config production -- model distillation configuration
sources: Hinton 2015 (knowledge distillation), DistilBERT, TinyLLaMA, pruning literature
quality: null
title: "Distillation Config Builder - Knowledge ISO"
version: "1.0.0"
author: n03_builder
tags: [distillation_config, builder, knowledge]
tldr: "Domain knowledge for distillation config: teacher-student training, temperature, loss functions, and compression."
domain: "model distillation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_model_distillation_config
  - bld_schema_distillation_config
---

# Domain Knowledge: distillation_config

## Executive Summary

Distillation configs define how to train a smaller student model to mimic a larger teacher model. They specify teacher/student model pairs, temperature scaling, loss function composition (KD loss + task loss), training parameters, and compression targets. A distillation_config is a P02 artifact -- it configures the DISTILLATION PROCESS, not the model architecture.

## Spec Table

| Property | Value |
|----------|-------|
| Pillar | P02 (model) |
| Methods | knowledge distillation, logit matching, feature distillation, progressive |
| Key parameters | temperature, alpha (KD weight), student architecture |
| Loss functions | KL divergence (soft targets) + cross-entropy (hard targets) |
| Compression targets | 2x-10x parameter reduction, <5% quality loss |

## Patterns

- **Temperature scaling** -- higher T (3-20) softens teacher logits, revealing dark knowledge; T=1 is no softening
- **Alpha weighting** -- balances KD loss (soft targets) vs task loss (hard targets); alpha=0.5 is a common starting point
- **Student architecture** -- smaller version of teacher (fewer layers/heads) or different architecture entirely
- **Progressive distillation** -- distill in stages (large -> medium -> small) for extreme compression
- **Data requirements** -- distillation works with unlabeled data; teacher provides soft labels

## Anti-Patterns

| Anti-Pattern | Why it fails |
|-------------|-------------|
| Temperature = 1 | No knowledge transfer beyond hard labels; defeats distillation purpose |
| Student too small | Capacity gap too large; student cannot learn teacher distribution |
| No task loss | Pure KD loss without task anchoring drifts from ground truth |
| Wrong teacher | Distilling from a poorly performing teacher propagates errors |
| No eval during training | Cannot detect training divergence or mode collapse |
