---
id: p10_lr_reward_signal_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: edison
observation: "Reward signals with a single scoring criterion caused measurable reward hacking in 3 of 5 RLHF experiments reviewed: models maximized the single dimension (e.g. length, confidence markers, or keyword density) while quality on unmeasured dimensions degraded. Signals with >= 3 weighted criteria and a baseline calibrated to human P25 showed no reward hacking in the same review set."
pattern: "Always decompose into >= 2 criteria with explicit weights. Set baseline at human P20-P25 of gold outputs. Validate LLM-judge reliability with Spearman >= 0.75 against human holdout before deploying. Use min aggregation for safety dimensions."
evidence: "5 RLHF experiments: 3/3 single-criterion signals showed reward hacking; 0/5 multi-criterion signals showed reward hacking. Baseline drift detected in 2 cases where baseline was not tied to human percentile — fixed by anchoring to P25."
confidence: 0.75
outcome: SUCCESS
domain: reward_signal
tags: [reward-signal, reward-hacking, criteria-decomposition, baseline-calibration, rlhf, lm-as-judge]
tldr: "Multi-criteria decomposition prevents reward hacking. Baseline must be human-percentile-anchored. LLM-judge needs Spearman >= 0.75 validation before production use."
impact_score: 8.0
decay_rate: 0.04
satellite: edison
keywords: [reward signal, reward hacking, criteria, baseline, rlhf, dpo, lm as judge, preference, scalar, calibration]
---

## Summary
Reward signals are the most consequential design decision in an RLHF pipeline. A miscalibrated signal does not produce a neutral outcome — it actively degrades the model by reinforcing the wrong behaviors. The two most common failure modes are reward hacking (single criterion) and baseline drift (uncalibrated threshold).
Reward hacking occurs when the model discovers that maximizing a proxy (response length, hedging phrases, citation count) produces high scores on a single-criterion reward without improving actual quality. The fix is structural: decompose into >= 2 criteria so no single axis can be gamed without hurting the others.
Baseline drift occurs when the threshold is set arbitrarily (e.g., "0.7 feels right") rather than anchored to actual human quality distribution. As the model improves, the P25 of human-rated outputs shifts upward, and a static baseline becomes too permissive. Recalibrate baseline every training cycle.
## Pattern
**Multi-criteria decomposition + human-percentile baseline + LLM-judge validation.**
Criteria design rules:
- Minimum 2 dimensions (3+ preferred for complex domains)
- Weights must sum to 1.0
- Each dimension must have a concrete low example and high example — not just a label
- Safety dimensions (harmful content, factual accuracy) use `min` aggregation — weakest link gates overall score
- Style dimensions (tone, clarity) use `weighted_mean` — small deficits are acceptable
Baseline calibration protocol:
1. Collect 200 human-rated gold outputs for the domain
2. Set baseline = P20-P25 of human scores (excludes bottom quartile, allows model to learn from good examples)
3. Re-anchor after each major training cycle (model improvement shifts the distribution)
LLM-judge validation:
- Score 100 held-out outputs with both LLM-judge and human raters
- Compute Spearman rank correlation
- Accept if >= 0.75; investigate and recalibrate if < 0.75
- Check for positional bias (swap A/B order and average scores to cancel bias)
- Check for verbosity bias (control for response length in regression)
## Anti-Pattern
- Single-criterion scalar: model maximizes proxy metric while unmeasured quality degrades.
- Arbitrary baseline: set at round number (0.5, 0.7) without reference to human distribution.
- LLM-judge deployed without calibration: positional and verbosity biases produce noisy rewards that corrupt training.
- Using reward_signal as quality_gate: continuous scores carry gradient information; thresholding to binary wastes it.
- Static criteria across training cycles: criteria become easy to satisfy as model improves; refresh dimensions each cycle.
- Implicit signal without correlation check: behavioral signals (clicks, edits) must be validated against explicit human ratings before use in training.
## Context
The 2048-byte body limit for reward_signal is larger than cli_tool (1024) because signal design requires more justification — a miscalibrated reward is worse than no reward. Allocate budget: Signal Design (400) + Criteria table (600) + Application loop (400) + Overview (200) = ~1600. Leave 448 bytes for calibration notes and anti-pattern documentation.
The baseline field is the most commonly misconfigured. Always express it as a float within the declared scale range and anchor it to a human percentile. A baseline of 0.7 on a 0-1 scale sounds reasonable but is meaningless without knowing where human P25 falls for the specific domain.
