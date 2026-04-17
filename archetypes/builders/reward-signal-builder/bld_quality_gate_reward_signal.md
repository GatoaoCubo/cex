---
id: p11_qg_reward_signal
kind: quality_gate
pillar: P11
title: "Gate: reward_signal"
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
domain: "reward signals — continuous quality scores for agent improvement via RLHF, DPO, critique, or implicit feedback"
quality: 9.0
tags: [quality-gate, reward-signal, P11, feedback, rlhf, scoring]
tldr: "Pass/fail gate for reward_signal artifacts: signal_type validity, scale consistency, baseline calibration, criteria completeness, and application loop documentation."
density_score: 0.90
llm_function: GOVERN
---
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
