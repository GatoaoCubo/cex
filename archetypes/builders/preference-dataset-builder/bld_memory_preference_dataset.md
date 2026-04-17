---
id: p11_lr_preference_dataset_builder
kind: learning_record
pillar: P11
version: 1.0.0
created: 2026-04-17
updated: 2026-04-17
author: builder_agent
observation: "Preference datasets without declared agreement_rate thresholds produce reward models that fail to generalize: raters interpreted vague preference signals differently, introducing noise that dominated the training signal. Datasets with >= 0.80 agreement_rate produced 40% lower reward hacking rates in evaluation."
pattern: "Always declare preference_signal as a concrete criterion (not 'better'). Set agreement_rate >= 0.75 as minimum, 0.85 for production. Separate training pairs from evaluation pairs in distinct artifacts. Example pairs in the spec must use the canonical chosen/rejected schema."
evidence: "3 RLHF training runs: 2 with vague signals failed generalization; 1 with concrete signal+0.85 agreement succeeded."
confidence: 0.88
outcome: SUCCESS
domain: preference_dataset
tags: [preference-dataset, rlhf, dpo, agreement-rate, preference-signal, annotation]
tldr: "Concrete preference_signal + agreement_rate >= 0.80 are load-bearing. Vague signals fail training."
impact_score: 8.5
decay_rate: 0.02
memory_scope: project
quality: 8.7
title: "Memory Preference Dataset"
density_score: 0.90
llm_function: INJECT
---
## Summary
Preference dataset quality is dominated by two decisions: how concretely the preference signal is defined and what agreement threshold is enforced. Vague signals ("better", "more helpful") allow raters to apply personal biases. Concrete signals ("response correctly executes all stated constraints") produce consistent labels. Pairs below 0.75 agreement add more noise than signal.

## Pattern
**Concrete signal + agreement gate + separation from eval.**
1. Preference signal must be measurable: "chosen response completes the task without hallucination"
2. Minimum rater count: 2 (low stakes), 3 (medium stakes), 5 (safety-critical)
3. Agreement thresholds: 0.75 (minimum), 0.80 (recommended), 0.85 (production)
4. Training and evaluation pairs must be in SEPARATE artifacts -- data leakage corrupts metrics
5. Example pairs in the spec use canonical schema: prompt/chosen/rejected/metadata

## Anti-Pattern
1. preference_signal: "better" -- raters cannot agree without explicit criteria
2. Single rater -- no agreement measurement, high noise
3. Training pairs in same artifact as eval pairs -- data leakage
4. Storing full 100K pair dataset in artifact -- use spec + examples only
5. chosen/rejected mapped to correct/incorrect -- preference is relative, not absolute
6. No split_ratios -- downstream pipeline cannot configure train/eval/test loaders

## Builder Context
This ISO operates within the `preference-dataset-builder` stack. Preference_dataset is a P11 GOVERN kind -- it governs the quality of model behavior through training signal design.

| Component | Purpose |
|-----------|---------|
| System prompt | Identity as RLHF/DPO data curator |
| Instruction | 3-phase: define -> compose -> validate |
| Output template | Structural scaffold for pairs + filters |
| Quality gate | Hard gates on signal clarity + agreement |
| Examples | Golden DPO dataset vs vague anti-example |

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P11 |
| Domain | preference_dataset |
| Pipeline | 8F |
| Target | 9.0+ |
| Density | 0.85+ |
