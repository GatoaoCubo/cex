---
kind: quality_gate
id: p11_qg_regression_check
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of regression_check artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: regression_check"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, regression-check, P07, evals, baseline, threshold]
tldr: "Pass/fail gate for regression_check artifacts: baseline_ref resolvability, threshold semantics, metric coverage, and fail_action definition."
domain: "baseline comparison configuration — current vs prior experiment for detecting quality regressions in LLM pipelines"
created: "2026-03-29"
updated: "2026-03-29"
density_score: 0.90
related:
  - bld_examples_regression_check
  - bld_instruction_regression_check
  - regression-check-builder
  - p03_sp_regression_check_builder
  - bld_knowledge_card_regression_check
  - bld_schema_regression_check
  - p10_lr_regression_check_builder
  - p11_qg_function_def
  - p11_qg_chunk_strategy
  - bld_collaboration_regression_check
---

## Quality Gate

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

## Examples

# Examples: regression-check-builder
## Golden Example
INPUT: "Create regression check for the summarization pipeline comparing against last week's production experiment"
OUTPUT:
```yaml
id: p07_rc_summarization_prod_weekly
kind: regression_check
pillar: P07
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
name: "Summarization Pipeline Weekly Regression"
baseline_ref: "experiment/summarization-prod-2026-03-22"
threshold: 5.0
metrics:
  - accuracy
  - faithfulness
  - latency_p95
  - cost_per_call
quality: 8.9
tags: [regression_check, summarization, production, P07]
tldr: "Weekly regression check for summarization pipeline vs prod baseline. 5% threshold. Blocks deploy on accuracy/faithfulness drop."
description: "Compares current summarization pipeline against last production experiment on accuracy, faithfulness, latency, and cost"
tool: braintrust
comparison_mode: relative
fail_action: block
notify: [ml-team-slack, oncall-pager]
cadence: on_deploy
scope: "summarization-pipeline-v2"
```
## Overview
Weekly regression gate for the summarization pipeline. Runs on every deployment attempt; blocks release if any metric drops beyond threshold vs the prior production experiment.
## Baseline
**baseline_ref**: `experiment/summarization-prod-2026-03-22` — production experiment captured after v2.1 release passed QA. Represents the stable production quality bar. Rotate baseline after each successful production deployment.
## Metrics
| Metric | Method | Threshold | Direction |
|--------|--------|-----------|-----------|
| accuracy | Braintrust LLM-judge vs source | 5.0% relative drop | Decrease = regression |
| faithfulness | Claim decomposition scorer | 3.0% relative drop | Decrease = regression |
| latency_p95 | Braintrust timing metadata | 20.0% relative increase | Increase = regression |
| cost_per_call | Model provider billing | 15.0% relative increase | Increase = regression |
## Failure Protocol
- **fail_action**: block. Notify #ml-team-slack + oncall-pager (accuracy/faithfulness only).
- **Remediation**: Check recent prompt changes, model version, dataset distribution shifts.
- **Escalation**: If unresolved within 2h of deploy attempt, escalate to ML lead.
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p07_rc_ pattern (H02 pass)
- kind: regression_check (H04 pass)
- baseline_ref is a concrete experiment ID (H07 pass)
- threshold is numeric > 0 (H08 pass)
- metrics list has 4 items (H09 pass)
- body has all 4 sections: Overview, Baseline, Metrics, Failure Protocol
- tool specified (Braintrust) with measurement method per metric
- fail_action: block with notify channels and remediation steps
- tldr: 130 chars <= 160 (S01 pass)

## Anti-Example
INPUT: "Create regression check for the chatbot"
BAD OUTPUT:
```yaml
id: chatbot-regression
kind: eval
baseline_ref: previous
threshold: good
quality: 8.5
tags: [regression]
```
Checks if chatbot got worse.
FAILURES:
1. id: "chatbot-regression" has hyphens and no `p07_rc_` prefix -> H02 FAIL
2. kind: "eval" not "regression_check" -> H04 FAIL
3. quality: 8.5 (not null) -> H05 FAIL
4. baseline_ref: "previous" is not resolvable -> H07 FAIL
5. threshold: "good" is not numeric -> H08 FAIL
6. Missing fields: metrics, pillar, version, created, updated, author, name, tldr -> H06 FAIL
7. tags: only 1 item, missing "regression_check" -> SOFT FAIL
8. Body missing ## Baseline, ## Metrics, ## Failure Protocol sections
9. No metrics defined — nothing to compare -> H09 FAIL
10. No fail_action — regression detected but nothing happens -> SOFT FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
