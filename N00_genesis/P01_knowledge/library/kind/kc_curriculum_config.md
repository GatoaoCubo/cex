---
id: kc_curriculum_config
kind: knowledge_card
8f: F3_inject
title: Curriculum Config -- Training Data Ordering and Adaptive Pacing
version: 1.0.0
quality: null
pillar: P01
tags:
  - curriculum-learning
  - training
  - data-ordering
  - adaptive-pacing
  - P07
related:
  - kc_training_method
  - kc_dataset_card
  - kc_finetune_config
  - kc_synthetic_data_config
  - kc_eval_metric
  - kc_distillation_config
tldr: "Training data ordering and pacing strategy with difficulty scheduling and competency gates"
when_to_use: "When model training benefits from structured data presentation order rather than random shuffling"
---

# Curriculum Config

A curriculum config defines the order, pacing, and mixing strategy for training data presentation during model training. Just as human students learn arithmetic before calculus, language models benefit from structured exposure to training data -- starting with simpler examples and progressively introducing harder ones.

## Description

Standard training shuffles data randomly and presents it uniformly across epochs. Curriculum learning challenges this assumption: the order in which a model sees data affects what it learns and how quickly it converges. A curriculum config replaces random shuffling with deliberate sequencing.

The config governs: difficulty scheduling (how to order examples from easy to hard), data mixing ratios (how to balance different data sources or domains), epoch-based transitions (when to shift from one curriculum phase to the next), self-paced mechanisms (letting the model's loss signal control pacing), and competency thresholds (measurable gates between curriculum stages).

Curriculum learning is distinct from training_method (which defines the optimization algorithm -- SGD, Adam, learning rate schedule) and from dataset_card (which documents what data exists, not how to present it). The curriculum config answers: given this data and this training method, in what order and at what pace should the model see examples?

## Key Concepts

| Concept | Definition | Design Choice |
|---------|-----------|---------------|
| Difficulty Scheduling | Ordering examples from easy to hard based on a difficulty metric | Linear ramp, exponential ramp, or step-function transitions |
| Difficulty Metric | How to measure example difficulty (loss-based, length-based, annotated) | Model-based metrics adapt; heuristic metrics are cheaper |
| Data Mixing Ratio | Proportion of each data source in each training batch | Static ratios (60/20/20) or dynamic ratios that shift per phase |
| Epoch-based Curriculum | Changing the data composition at fixed epoch boundaries | Simple to implement; may not match model readiness |
| Self-paced Learning | Model's own loss determines which examples it sees next | Avoids too-easy and too-hard examples; higher implementation cost |
| Competency Threshold | Measurable gate (eval score, loss plateau) that triggers phase transition | Prevents advancing before the model has learned the current phase |
| Anti-curriculum | Presenting hard examples first (the inverse strategy) | Useful for robustness training and adversarial fine-tuning |
| Data Replay | Re-introducing earlier examples during later phases to prevent forgetting | Critical for multi-phase curricula; without replay, early skills degrade |

## Related Kinds

| Kind | Pillar | Relationship |
|------|--------|-------------|
| training_method | P02 | Sibling -- training_method defines how to optimize; curriculum_config defines what to optimize on when |
| dataset_card | P01 | Upstream -- documents the data that the curriculum orders |
| finetune_config | P02 | Consumer -- fine-tuning benefits from curriculum-ordered data |
| synthetic_data_config | P01 | Upstream -- synthetic data can be generated at specific difficulty levels for curriculum phases |
| eval_metric | P07 | Tool -- metrics determine competency thresholds between phases |
| distillation_config | P02 | Complementary -- progressive distillation can follow a curriculum (easy teacher tasks first) |
| benchmark | P07 | Downstream -- measures whether curriculum training outperformed random shuffling |

## Anti-Patterns

- **Difficulty without measurement**: Ordering examples by assumed difficulty (e.g., shorter = easier) without validating against actual model loss. A 10-word example can be harder than a 100-word example if it requires rare reasoning.
- **No baseline comparison**: Implementing curriculum learning without measuring whether it outperforms random shuffling. On well-curated datasets, random order is often competitive. Curriculum adds value primarily on noisy, heterogeneous, or multi-domain data.
- **Phase transitions without replay**: Moving from phase 1 to phase 2 and never revisiting phase 1 data. The model forgets early patterns (catastrophic forgetting). Always mix a fraction of earlier phases into later batches.
- **Static mixing for dynamic data**: Using fixed mixing ratios when data sources have different convergence rates. The model may overfit on the easy source while underfitting on the hard source. Use loss-weighted dynamic mixing.
- **Curriculum for single-domain data**: Applying curriculum learning to a homogeneous dataset where all examples have similar difficulty. The overhead of difficulty scoring and phased training adds complexity without benefit.
- **Competency thresholds too strict**: Setting phase-transition gates so high that the model loops on early phases indefinitely. Thresholds should be calibrated against the model's expected performance trajectory, with a timeout fallback.

## Properties

| Property | Value |
|----------|-------|
| Kind | knowledge_card |
| Pillar | P01 (knowledge domain), P07 (evaluation domain) |
| Domain | Training methodology, data engineering |
| Pipeline | 8F (F1-F8) |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_training_method]] | sibling | 0.44 |
| [[kc_dataset_card]] | upstream | 0.40 |
| [[kc_finetune_config]] | consumer | 0.38 |
| [[kc_synthetic_data_config]] | upstream | 0.35 |
| [[kc_eval_metric]] | tool | 0.32 |
| [[kc_distillation_config]] | complementary | 0.30 |
| [[kc_benchmark_suite]] | downstream | 0.27 |
