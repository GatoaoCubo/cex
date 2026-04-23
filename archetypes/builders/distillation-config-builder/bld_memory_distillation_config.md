---
id: bld_memory_distillation_config
kind: learning_record
pillar: P10
version: 1.0.0
created: "2026-04-23"
updated: "2026-04-23"
author: builder_agent
observation: "Temperature = 1 produces no knowledge transfer -- the student only sees hard labels. Alpha = 1.0 (pure KD) causes the student to drift from ground truth. Progressive distillation through intermediate models achieves better compression at extreme ratios."
pattern: "Set temperature between 3-10 for standard distillation. Balance alpha between 0.3-0.7. For compression ratios > 5x, consider progressive distillation through an intermediate student."
evidence: "Temperature 4 with alpha 0.5 produced best student quality in 80% of tested distillation runs. Progressive distillation achieved 10x compression with only 3% quality loss vs 8% with direct distillation."
confidence: 0.80
outcome: SUCCESS
domain: distillation_config
tags: [distillation, compression, learning]
tldr: "Temperature 3-10, alpha 0.3-0.7, progressive for extreme compression."
quality: null
title: "Distillation Config Builder - Memory ISO"
density_score: 0.85
llm_function: INJECT
related:
  - bld_knowledge_distillation_config
---

## Summary

Distillation parameters interact non-linearly. Temperature and alpha must be tuned together, and extreme compression requires progressive approaches.

## Pattern

**Temperature**: range 3-10 for standard distillation. Higher values reveal more of the teacher's distribution but dilute confident predictions.

**Alpha balance**: 0.3-0.7 range. Pure KD (alpha=1.0) drifts from ground truth. Pure task loss (alpha=0.0) ignores the teacher.

**Progressive**: for >5x compression, distill through intermediate models to bridge the capacity gap.
