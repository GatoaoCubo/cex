---
id: p11_qg_fallback_chain
kind: quality_gate
pillar: P11
title: "Gate: fallback_chain"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "fallback_chain — model degradation sequences with timeouts, circuit breakers, and cost controls"
quality: 9.0
tags: [quality-gate, fallback-chain, resilience, model-degradation, P11]
tldr: "Validates fallback_chain artifacts: step sequence integrity, timeout/threshold coverage, and cost-aware degradation design."
density_score: 0.92
llm_function: GOVERN
---
# Gate: fallback_chain
## Definition
| Field     | Value |
|-----------|-------|
| metric    | composite score across SOFT dimensions |
| threshold | >= 7.0 to publish; >= 9.5 for golden |
| operator  | weighted average after all HARD gates pass |
| scope     | all artifacts where `kind: fallback_chain` |
All HARD gates are AND-logic: one failure rejects the artifact regardless of SOFT score.
## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Any YAML syntax error |
| H02 | ID matches `^p02_fc_[a-z][a-z0-9_]+$` | Wrong format or namespace |
| H03 | ID equals filename stem (no extension) | Mismatch between id field and file name |
| H04 | Kind equals literal `fallback_chain` | Any other value |
| H05 | `quality` field is null | Any non-null value |
| H06 | Required fields present: id, kind, pillar, version, created, updated, author, steps_count, timeout_per_step_ms, quality_threshold, domain, quality, tags, tldr | Any missing field |
| H07 | `steps_count` matches rows in Chain table AND `steps_count` >= 2 | Mismatch or single-step chain |
| H08 | Steps ordered by decreasing capability (primary model first, minimum-cost last) | Degradation inverted or flat |
| H09 | Each step declares `timeout_per_step_ms` > 0 | Missing or zero timeout on any step |
| H10 | Circuit breaker threshold defined (not zero, not absent) | Missing circuit breaker spec |
## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| S01 | `tldr` <= 160 chars, non-empty, names the degradation path | 0.10 | Accurate + concise=1.0, vague=0.4, absent=0.0 |
| S02 | Tags list len >= 3, includes `fallback_chain` | 0.05 | Met=1.0, partial=0.5 |
| S03 | Chain table has all columns filled per step | 0.10 | All filled=1.0, gaps=0.5 |
| S04 | Degradation Logic section: trigger conditions per step | 0.12 | All triggers=1.0, partial=0.5, absent=0.0 |
| S05 | Circuit Breaker section: open/half-open/closed thresholds and recovery | 0.12 | Fully specified=1.0, partial=0.5, absent=0.0 |
| S06 | Cost Analysis section: per-step cost implications | 0.10 | All steps costed=1.0, partial=0.5, absent=0.0 |
| S07 | Each step names a valid provider (anthropic, openai, google, local) | 0.08 | All valid=1.0, unknown provider=0.3 |
| S08 | Final fallback is a safe static or cached response | 0.10 | Present=1.0, absent=0.0 |
| S09 | Retry policy distinct from fallback trigger (not conflated) | 0.08 | Clearly separated=1.0, conflated=0.2 |
| S10 | `density_score` >= 0.80 | 0.08 | Met=1.0, below=0.0 |
| S11 | No filler phrases ("robust mechanism", "gracefully handles") | 0.07 | Clean=1.0, filler present=0.0 |
**Weight sum: 1.00**
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — reference artifact for fallback_chain calibration |
| >= 8.0 | PUBLISH — pool-eligible; circuit breaker and cost docs present |
| >= 7.0 | REVIEW — usable but missing threshold detail or cost analysis |
| < 7.0  | REJECT — redo; likely missing circuit breaker or step ordering |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Emergency hotfix only; chain replaces a failing production route with no time to complete all gates |
| approver | Senior engineer with model cost authority |
| audit trail | Required: incident link, timestamp, approver ID |
| expiry | 48 hours; full gate review must follow |
| never bypass | H01 (corrupt YAML breaks all parsing), H05 (self-scored quality is invalid data) |
