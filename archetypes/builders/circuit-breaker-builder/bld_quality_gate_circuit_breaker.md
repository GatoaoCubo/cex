---
id: p11_qg_circuit_breaker
kind: quality_gate
pillar: P11
title: "Gate: circuit_breaker"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "builder_agent"
domain: "circuit breaker -- resilience pattern for dependency fault isolation"
quality: null
tags: [quality-gate, circuit-breaker, P09, resilience, fault-tolerance]
tldr: "Pass/fail gate for circuit_breaker artifacts: failure threshold validity, cooldown positivity, probe count, state machine completeness."
density_score: 0.90
llm_function: GOVERN
---
# Gate: circuit_breaker

## Definition
| Field | Value |
|---|---|
| metric | circuit_breaker artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: circuit_breaker` |

## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p09_cb_[a-z][a-z0-9_]+$` | ID contains uppercase, hyphens, or missing prefix |
| H03 | ID equals filename stem | id: p09_cb_foo but file is p09_cb_bar.md |
| H04 | Kind equals literal `circuit_breaker` | kind: breaker or any other value |
| H05 | Quality field is null | quality: 8.0 or any non-null value |
| H06 | All required fields present | Missing service, failure_rate_threshold, cooldown_duration, probe_count |
| H07 | failure_rate_threshold is integer in [1, 100] | 0, -1, "high", 101, absent |
| H08 | cooldown_duration is positive integer | -30, 0, "30s", absent |
| H09 | probe_count is positive integer | 0, -1, "three", absent |
| H10 | Body has all 4 required sections | Missing ## Overview, ## State Machine, ## Cooldown, or ## Fallback |

## SOFT Scoring
| Dimension | Weight | Criteria |
|---|---|---|
| Failure threshold specificity | 1.0 | Threshold is based on real dependency SLA or observed failure rate |
| State machine completeness | 1.0 | All 3 states (CLOSED/OPEN/HALF-OPEN) documented with transitions |
| Cooldown rationale | 1.0 | Cooldown duration justified (e.g. matches service restart time) |
| Probe strategy | 1.0 | probe_count reflects real recovery confidence level |
| Fallback quality | 1.0 | fallback_response is actionable (not just "error") |
| Exception coverage | 1.0 | monitored_exceptions covers all realistic failure modes |
| Slow call detection | 0.5 | slow_call_threshold_ms present when latency is a concern |
| Sliding window tuning | 1.0 | window type and size appropriate for traffic volume |
| Boundary clarity | 1.0 | Explicitly NOT rate_limit_config, NOT fallback_chain, NOT runtime_rule |
| tldr quality | 1.0 | tldr <= 160ch, includes service + thresholds |

## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
