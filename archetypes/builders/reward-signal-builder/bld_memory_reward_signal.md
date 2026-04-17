---
id: p10_lr_reward_signal_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
observation: "Reward signals with a single scoring criterion caused measurable reward hacking in 3 of 5 RLHF experiments reviewed: models maximized the single dimension (e.g. length, confidence markers, or keyword density) while quality on unmeasured dimensions degraded. Signals with >= 3 weighted criteria and a baseline calibrated to human P25 showed no reward hacking in the same review set."
pattern: "Always decompose into >= 2 criteria with explicit weights. Set baseline at human P20-P25 of gold outputs. Validate LLM-judge reliability with Spearman >= 0.75 against human holdout before deploying. Use min aggregation for safety dimensions."
evidence: "5 RLHF experiments: 3/3 single-criterion signals showed reward hacking; 0/5 multi-criterion signals showed reward hacking. Baseline drift detected in 2 cases where baseline was not tied to human percentile."
confidence: 0.75
outcome: SUCCESS
domain: reward_signal
tags: [reward-signal, reward-hacking, criteria-decomposition, baseline-calibration, rlhf, lm-as-judge]
tldr: "Multi-criteria ofcomposition prevents reward hacking. Baseline must be human-percentile-anchored. LLM-judge needs Spearman >= 0.75 validation before production use."
impact_score: 8.0
decay_rate: 0.04
agent_group: edison
keywords: [reward signal, reward hacking, criteria, baseline, rlhf, dpo, lm as judge, preference, scalar, calibration]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.0
title: "Memory Reward Signal"
density_score: 0.90
llm_function: INJECT
---
## Summary
Reward signals are the most consequential design decision in an RLHF pipeline. A miscalibrated signal does not produce a neutral outcome — it actively degrades the model by reinforcing the wrong behaviors. The two most common failure modes are reward hacking (single criterion) and baseline drift (uncalibrated threshold).

Reward hacking occurs when the model maximizes a proxy (response length, hedging phrases, citation count) without improving actual quality. Fix: decompose into >= 2 criteria so no single axis can be gamed. Baseline drift occurs when the threshold is set arbitrarily rather than anchored to the human quality distribution. Recalibrate baseline every training cycle.

## Pattern
**Multi-criteria ofcomposition + human-percentile baseline + LLM-judge validation.**

Criteria design:
- Minimum 2 dimensions (3+ preferred); weights sum to 1.0
- Each dimension needs a concrete low/high example — not just a label
- Safety dimensions: `min` aggregation — weakest link gates overall score
- Style dimensions: `weighted_mean` — small deficits acceptable

Baseline calibration:
1. Collect 200 human-rated gold outputs
2. Set baseline = P20-P25 of human scores
3. Re-anchor after each major training cycle

LLM-judge validation:
- Score 100 held-out outputs with both LLM-judge and human raters
- Accept if Spearman >= 0.75; recalibrate if lower
- Check positional bias (swap A/B, average scores) and verbosity bias

## Anti-Pattern
- Single-criterion scalar: model maximizes proxy while unmeasured quality degrades.
- Arbitrary baseline set at round number without reference to human distribution.
- LLM-judge deployed without calibration: positional/verbosity biases corrupt training.
- Using reward_signal as quality_gate: continuous scores carry gradient; thresholding wastes it.
- Static criteria across training cycles: refresh dimensions each cycle as model improves.
