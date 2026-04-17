---
id: p11_qg_regression_check
kind: quality_gate
pillar: P11
title: "Gate: regression_check"
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
domain: "baseline comparison configuration — current vs prior experiment for detecting quality regressions in LLM pipelines"
quality: 9.0
tags: [quality-gate, regression-check, P07, evals, baseline, threshold]
tldr: "Pass/fail gate for regression_check artifacts: baseline_ref resolvability, threshold semantics, metric coverage, and fail_action definition."
density_score: 0.90
llm_function: GOVERN
---
# Gate: regression_check
## Definition
| Field | Value |
|---|---|
| metric | regression_check artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: regression_check` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p07_rc_[a-z][a-z0-9_]+$` | ID contains uppercase, spaces, hyphens, or wrong prefix |
| H03 | ID equals filename stem | `id: p07_rc_my_check` but file is `p07_rc_other.md` |
| H04 | Kind equals literal `regression_check` | `kind: eval` or `kind: benchmark` or any other value |
| H05 | Quality field is null | `quality: 8.0` or any non-null value |
| H06 | All required fields present | Missing `baseline_ref`, `threshold`, or `metrics` |
| H07 | baseline_ref is a non-empty concrete string | `baseline_ref: ""` or null or vague string like "previous" |
| H08 | threshold is numeric and > 0 | `threshold: 0` without justification comment; threshold is string |
| H09 | metrics list has at least one entry | `metrics: []` or metrics field absent |
| H10 | Artifact is a comparison config, not an absolute measurement | Body describes absolute targets only with no baseline_ref usage |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Baseline clarity | 1.0 | baseline_ref is a resolvable ID with capture context documented |
| Threshold justification | 1.0 | Threshold value explained; units documented |
| Metric coverage | 1.0 | accuracy, latency, cost at minimum for production systems |
| Per-metric thresholds | 0.5 | Different tolerance per metric where apownte |
| Tool specification | 1.0 | Comparison tool identified with invocation pattern |
| fail_action definition | 1.0 | fail_action is block/warn/log with rationale |
| Notification config | 0.5 | Owner or channel defined for regression alerts |
| Cadence definition | 0.5 | When check runs aligned with deployment frequency |
| Baseline update policy | 1.0 | When and how baseline_ref is rotated |
| Boundary clarity | 1.0 | Explicitly not a benchmark, unit_eval, or golden_test |
| Remediation guidance | 1.0 | Failure protocol describes investigation steps |
| Scope definition | 0.5 | Which prompt, model, or pipeline is under test |
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
| conditions | Experimental check for new metric type under active development |
| approver | Author self-certification with comment explaining experimental scope |
| audit_trail | Bypass note in frontmatter comment with expiry date |
| expiry | 14d — experimental checks must be promoted to >= 7.0 or removed |
| never_bypass | H01 (unparseable YAML), H05 (self-scored gates corrupt metrics), H07 (unresolvable baseline_ref) |
