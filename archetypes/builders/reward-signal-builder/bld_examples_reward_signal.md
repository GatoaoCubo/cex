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
author: "builder_agent"
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
Measures whether agent responses in customer support resolve the user's problem with clarity, appropriate tone, and completeness. Consumed by the monthly RLHF training cycle.
## Signal Design
- Type: scalar — weighted 0-1 score from LLM-judge; simpler than preference pairs since resolution is measurable
- Scale: 0.0 = fails to help, 0.5 = partial help, 1.0 = complete resolution with ideal tone
- Model: claude-sonnet-4-6 — verified >= 0.78 Spearman correlation against human raters on 200-sample holdout
- Aggregation: weighted_mean — problem_resolution weighted 2x others (primary success criterion)
## Criteria
| Dimension | Weight | Low (0-0.3) | High (0.8-1.0) |
|-----------|--------|-------------|----------------|
| problem_resolution | 0.40 | Ignores or misidentifies problem | Fully resolved with clear steps |
| clarity | 0.20 | Jargon-heavy, ambiguous | Simple language, unambiguous |
| tone | 0.20 | Cold, dismissive | Warm, empathetic |
| completeness | 0.20 | Partial answer only | All sub-questions addressed |

Baseline: 0.70 (P25 of human-rated gold responses) — below baseline excluded from RLHF chosen set.
## Application
- RLHF loop: scores above baseline = chosen; below = rejected; preference pairs constructed monthly
- Consumer: training pipeline uses pairs with score differential > 0.15 to avoid noisy pairs
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches ^p11_rs_ pattern (H02 pass)
- kind: reward_signal (H04 pass)
- signal_type: scalar (valid enum) (H07 pass)
- baseline 0.70 within scale 0-1 (H08 pass)
- tags includes "reward_signal" (H09 pass)
- all 4 body sections present (H10 pass)
- 4 criteria with weights summing to 1.0 (S03 pass)
- model selection justified with calibration evidence (S05 pass)
- RLHF application loop fully described (S08 pass)

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
