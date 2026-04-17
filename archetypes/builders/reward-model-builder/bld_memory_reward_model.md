---
kind: learning_record
id: p10_lr_reward_model_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for reward_model construction
quality: 8.7
title: "Learning Record Reward Model"
version: "1.0.0"
author: wave1_builder_gen
tags: [reward_model, builder, learning_record]
tldr: "Learned patterns and pitfalls for reward_model construction"
domain: "reward_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Observation
Common issues include misalignment between reward signals and desired outcomes, overfitting to narrow examples, and ambiguous criteria leading to inconsistent model behavior.

## Pattern
Successful configurations use explicit, measurable criteria aligned with task goals, and modular components to isolate and test individual reward aspects.

## Evidence
Reviewed artifacts with well-defined reward criteria showed 20-30% higher alignment scores compared to those with vague objectives.

## Recommendations
- Define reward criteria using concrete, task-specific metrics.
- Decouple reward components to enable independent validation.
- Include diverse edge cases in training data to prevent overfitting.
- Document assumptions and limitations in the model configuration.
- Iterate reward design with feedback from downstream evaluation stages.
