---
kind: quality_gate
id: p11_qg_reward_signal
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of reward_signal artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: reward_signal"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, reward-signal, P11, feedback, rlhf, scoring]
tldr: "Pass/fail gate for reward_signal artifacts: signal_type validity, scale consistency, baseline calibration, criteria completeness, and application loop documentation."
domain: "reward signals — continuous quality scores for agent improvement via RLHF, DPO, critique, or implicit feedback"
created: "2026-03-29"
updated: "2026-03-29"
density_score: 0.90
related:
  - bld_examples_reward_signal
  - p03_sp_reward_signal_builder
  - bld_architecture_reward_signal
  - bld_instruction_reward_signal
  - bld_output_template_reward_signal
  - p11_qg_llm_judge
  - p11_qg_chunk_strategy
  - reward-signal-builder
  - p11_qg_constraint_spec
  - bld_schema_reward_signal
---

## Quality Gate

# Gate: reward_signal
## Definition
| Field | Value |
|---|---|
| metric | reward_signal artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: reward_signal` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p11_rs_[a-z][a-z0-9_]+$` | ID contains uppercase, hyphens, spaces, or missing prefix |
| H03 | ID equals filename stem | `id: p11_rs_foo` but file is `p11_rs_bar.md` |
| H04 | Kind equals literal `reward_signal` | `kind: metric` or `kind: score` or any other value |
| H05 | Quality field is null | `quality: 8.0` or any non-null value |
| H06 | All required fields present | Missing `signal_type`, `scale`, `model`, `tags`, or `tldr` |
| H07 | signal_type is valid enum value | `signal_type: regression` or unrecognized value |
| H08 | baseline within declared scale range | `scale: "0-1"` but `baseline: 5.0` |
| H09 | tags includes "reward_signal" | Tags list exists but "reward_signal" not present |
| H10 | Body has all 4 required sections | Missing ## Overview, ## Signal Design, ## Criteria, or ## Application |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Signal type justification | 1.0 | Explains why chosen signal_type fits domain; not default-picked |
| Scale semantics | 1.0 | High/low values defined with concrete meaning; not just a number range |
| Criteria completeness | 1.0 | >= 2 scored dimensions with weights; each has low/high example |
| Baseline calibration | 1.0 | Baseline justified relative to scale; not arbitrary |
| Model selection rationale | 0.5 | Explains why specific model (or human) produces reliable reward |
| Frequency apownteness | 0.5 | Frequency matches task granularity; not over- or under-evaluated |
| Aggregation justification | 0.5 | Aggregation method explained; not default mean for all cases |
| Application loop clarity | 1.0 | Concrete improvement loop described (RLHF/DPO/filtering/monitoring) |
| Anti-pattern awareness | 1.0 | Addresses at least one anti-pattern (reward hacking, single-dim, no baseline) |
| Boundary clarity | 1.0 | Explicitly not quality_gate (pass/fail) nor scoring_rubric (define criteria) |
| Domain specificity | 1.0 | Criteria and scale tuned to declared domain; not generic |
| Testability | 0.5 | Example inputs and expected score range provided |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Experimental signal under active calibration, not yet deployed to any improvement loop |
| approver | Author self-certification with comment explaining calibration-phase scope |
| audit_trail | Bypass note in frontmatter comment with expiry date |
| expiry | 14d — experimental signals must reach >= 7.0 or be archived |
| never_bypass | H01 (unparseable YAML breaks all tooling), H05 (self-scored gates corrupt quality metrics), H08 (out-of-range baseline produces nonsense rewards) |

## Examples

# Examples: reward-signal-builder
## Golden Example
INPUT: "Create reward signal for measuring helpfulness of agent responses in a costmer support context"
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
tags: [reward_signal, helpfulness, costmer-support, P11]
tldr: "Scalar 0-1 reward for support response helpfulness: 4 weighted criteria, baseline 0.70, feeds RLHF reward model."
criteria:
  - "problem_resolution: did the response resolve the stated problem?"
  - "clarity: was the response clear and free of jargon?"
  - "tone: was the tone empathetic and professional?"
  - "completeness: were all sub-questions addressed?"
frequency: per_task
aggregation: weighted_mean
baseline: 0.70
description: "Continuous quality score for costmer support responses. Feeds RLHF reward model training monthly."
```
## Overview
Measures whether agent responses in costmer support resolve the user's problem with clarity, apownte tone, and completeness. Consumed by the monthly RLHF training cycle.
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
