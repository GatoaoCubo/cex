---
kind: examples
id: bld_examples_reward_signal
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of reward_signal artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: reward-signal-builder
## Golden Example
INPUT: "Create reward signal for measuring helpfulness of agent responses in a customer support context"
OUTPUT:
```yaml
id: p11_rs_support_helpfulness
kind: reward_signal
pillar: P11
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "EDISON"
name: "Support Response Helpfulness"
signal_type: scalar
scale: "0-1"
model: "claude-sonnet-4-6"
quality: null
tags: [reward_signal, helpfulness, customer-support, P11]
tldr: "Scalar 0-1 reward for support response helpfulness: 4 weighted criteria, baseline 0.70, feeds RLHF reward model."
criteria:
  - "problem_resolution: did the response resolve the stated problem?"
  - "clarity: was the response clear and free of jargon?"
  - "tone: was the tone empathetic and professional?"
  - "completeness: were all sub-questions addressed?"
frequency: per_task
aggregation: weighted_mean
baseline: 0.70
description: "Continuous quality score for customer support responses. Feeds RLHF reward model training monthly."
```
## Overview
Measures whether agent responses in customer support fully resolve the user's problem
with clarity, appropriate tone, and completeness. Consumed by the monthly RLHF training cycle.
## Signal Design
- Type: scalar — a single LLM-judge pass produces a weighted 0-1 score; simpler than preference pairs for this domain because ground truth (resolution) is measurable
- Scale: 0-1 — 0.0 = response fails to help, 0.5 = partial help with gaps, 1.0 = complete resolution with ideal tone
- Model: claude-sonnet-4-6 — selected for calibrated instruction-following; verified >= 0.78 Spearman correlation against human raters on 200-sample holdout
- Computation: judge model scores each criterion 0-1, weighted_mean applied (see Criteria), result rounded to 4 decimal places
- Frequency: per_task — evaluated after each complete support exchange (not per turn, as resolution requires full context)
- Aggregation: weighted_mean — problem_resolution weighted 2x others because it is the primary success criterion
## Criteria
| Dimension | Weight | Low Score (0-0.3) | High Score (0.8-1.0) |
|-----------|--------|-------------------|----------------------|
| problem_resolution | 0.40 | Response ignores or misidentifies the problem | Problem fully resolved with clear steps |
| clarity | 0.20 | Jargon-heavy, ambiguous, or contradictory | Simple language, unambiguous, scannable |
| tone | 0.20 | Cold, dismissive, or overly formal | Warm, empathetic, appropriately casual |
| completeness | 0.20 | Only partial answer; follow-up questions ignored | All sub-questions addressed explicitly |
Baseline: 0.70 — responses scoring below 0.70 are excluded from RLHF chosen set and flagged for human review. Threshold set at P25 of human-rated gold responses.
## Application
- Loop: RLHF — scores above baseline become "chosen" samples; scores below become "rejected" samples; preference pairs constructed monthly for reward model fine-tuning
- Consumer: training pipeline ingests (chosen, rejected) pairs from score differential > 0.15 to avoid noisy pairs
- Cadence: per-task scoring in production; batch collected weekly; reward model retrained monthly on accumulated pairs
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches ^p11_rs_ pattern (H02 pass)
- kind: reward_signal (H04 pass)
- signal_type: scalar (valid enum) (H07 pass)
- baseline 0.70 within scale 0-1 (H08 pass)
- tags includes "reward_signal" (H09 pass)
- all 4 body sections present (H10 pass)
- 4 criteria with weights summing to 1.0 (S03 pass)
- scale has semantic meaning at 0, 0.5, 1.0 (S02 pass)
- model selection justified with calibration evidence (S05 pass)
- RLHF application loop fully described (S08 pass)
- boundary stated: not quality_gate, not scoring_rubric (S10 pass)
## Anti-Example
INPUT: "Create reward signal for code quality"
BAD OUTPUT:
```yaml
id: code-quality-reward
kind: score
pillar: tools
name: Code Quality
signal_type: good
scale: high
quality: 9.0
tags: [code]
```
Scores code quality. High is good, low is bad.
FAILURES:
1. id: "code-quality-reward" has hyphens and no `p11_rs_` prefix -> H02 FAIL
2. kind: "score" not "reward_signal" -> H04 FAIL
3. pillar: "tools" not "P11" -> H06 FAIL
4. quality: 9.0 (not null) -> H05 FAIL
5. signal_type: "good" not a valid enum value -> H07 FAIL
6. scale: "high" not a recognized scale format -> H06 FAIL
7. Missing fields: model, baseline, version, created, updated, author, tldr -> H06 FAIL
8. tags: only 1 item, missing "reward_signal" -> H09 FAIL
9. Body missing all 4 required sections -> H10 FAIL
10. Single-criterion design — primary reward hacking anti-pattern -> S09 FAIL
11. No baseline defined — cannot filter or trigger retraining -> S04 FAIL
12. No application loop — signal has no consumer -> S08 FAIL
