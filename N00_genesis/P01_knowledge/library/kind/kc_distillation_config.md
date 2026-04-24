---
id: kc_distillation_config
kind: knowledge_card
8f: F3_inject
title: Distillation Config -- Teacher-Student Knowledge Transfer
version: 1.0.0
quality: null
pillar: P01
tags:
  - distillation
  - knowledge-transfer
  - model-compression
  - teacher-student
  - P02
related:
  - kc_finetune_config
  - kc_quantization_config
  - kc_model_provider
  - kc_inference_config
  - kc_eval_metric
  - kc_curriculum_config
---

# Distillation Config

A distillation config defines the knowledge transfer pipeline from a large, capable teacher model to a smaller, efficient student model. Knowledge distillation compresses the teacher's learned representations into a student that approximates the teacher's behavior at a fraction of the computational cost.

## Description

The core insight behind distillation: a teacher model's soft probability distribution over outputs contains far more information than hard labels alone. When a teacher assigns 70% probability to the correct answer and 20% to a plausible alternative, that 20% signal teaches the student about the structure of the problem space -- something binary labels cannot convey.

A distillation config governs: teacher model selection (which model to distill from), student architecture (how small can the student be), temperature scaling (how much to soften probability distributions), loss function (how to measure student-teacher divergence), and layer matching (which internal representations to align).

Distillation is distinct from fine-tuning (which trains on data, not on another model's behavior) and from quantization (which reduces numerical precision without changing the model's learned weights). Distillation changes what the model knows; quantization changes how precisely it stores what it knows.

## Key Concepts

| Concept | Definition | Design Choice |
|---------|-----------|---------------|
| Teacher Model | The large, pre-trained model whose knowledge is being transferred | Larger teachers produce better students, but diminishing returns past ~10x size ratio |
| Student Architecture | The smaller model that learns to mimic the teacher | Must balance capacity (can it learn?) with efficiency (is it fast enough?) |
| Temperature Scaling | Softmax temperature applied to teacher logits before KL divergence | Higher T (2-20) reveals more structure; too high collapses to uniform |
| KL Divergence Loss | Measures how the student's distribution diverges from the teacher's | Primary distillation signal; combined with task loss |
| Task Loss | Standard cross-entropy on ground truth labels | Anchors the student to correct answers, not just teacher behavior |
| Alpha (Loss Weight) | Balance between distillation loss and task loss | Typical: 0.5-0.9 distillation, 0.1-0.5 task |
| Layer Matching | Aligning intermediate representations between teacher and student layers | Enables deep knowledge transfer beyond output logits |
| Feature Projection | Linear layer mapping student hidden dims to teacher hidden dims | Required when teacher and student have different hidden sizes |

## Related Kinds

| Kind | Pillar | Relationship |
|------|--------|-------------|
| finetune_config | P02 | Sibling -- fine-tuning trains on data; distillation trains on teacher behavior |
| quantization_config | P09 | Sibling -- quantization reduces precision; distillation reduces model size |
| model_provider | P02 | Upstream -- the teacher model source |
| inference_config | P09 | Downstream -- the student's inference parameters |
| eval_metric | P07 | Downstream -- measures student quality vs teacher baseline |
| curriculum_config | P07 | Complementary -- progressive distillation can follow a curriculum |
| training_method | P02 | Parent -- distillation is a specialization of training |

## Anti-Patterns

- **Teacher-student size mismatch**: Distilling a model with 100B parameters into a model with 100M parameters. The capacity gap is too large; the student cannot represent what the teacher knows. Typical effective ratio is 4-10x.
- **Temperature = 1.0**: Using the default temperature for distillation. The whole point of temperature scaling is to soften the distribution and reveal the teacher's uncertainty. T=1 makes distillation equivalent to label training.
- **Ignoring task loss entirely**: Setting alpha=1.0 (pure distillation, no task loss). The student learns to mimic teacher errors. Always blend distillation loss with ground-truth task loss.
- **Single-layer distillation**: Only matching output logits. Intermediate layer matching transfers structural knowledge that output-only distillation misses.
- **No evaluation against teacher**: Measuring student performance in isolation. The student's quality must be benchmarked as a percentage of teacher performance on the same eval set to quantify the compression-quality tradeoff.

## Properties

| Property | Value |
|----------|-------|
| Kind | knowledge_card |
| Pillar | P01 (knowledge domain), P02 (model domain) |
| Domain | Model compression, knowledge transfer |
| Pipeline | 8F (F1-F8) |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_finetune_config]] | sibling | 0.46 |
| [[kc_quantization_config]] | sibling | 0.42 |
| [[kc_model_provider]] | upstream | 0.38 |
| [[kc_inference_config]] | downstream | 0.35 |
| [[kc_eval_metric]] | downstream | 0.32 |
| [[kc_curriculum_config]] | complementary | 0.30 |
| [[kc_training_method]] | parent | 0.28 |
