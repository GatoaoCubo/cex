---
id: p11_qg_retry_policy
kind: quality_gate
pillar: P11
title: "Gate: retry_policy"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "builder_agent"
domain: "retry policy -- backoff and jitter config for retrying failed operations"
quality: null
tags: [quality-gate, retry-policy, P09, backoff, jitter]
tldr: "Pass/fail gate for retry_policy: id pattern, max_attempts range, jitter not NONE, no 4xx in retryable_errors, all 3 sections."
density_score: 0.90
llm_function: GOVERN
---

# Gate: retry_policy

## Definition

| Field | Value |
|---|---|
| metric | retry_policy artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: retry_policy` |

## HARD Gates

All must pass (AND logic). Any single failure = REJECT.

| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p09_rtp_[a-z][a-z0-9_]+$` | ID contains uppercase, hyphens, or missing prefix |
| H03 | ID equals filename stem | id: p09_rtp_foo but file is p09_rtp_bar.md |
| H04 | Kind equals literal `retry_policy` | kind: retry or any other value |
| H05 | Quality field is null | quality: 8.0 or any non-null value |
| H06 | max_attempts is positive integer | 0, -1, "many", absent |
| H07 | initial_interval is positive integer (ms) | 0, -100, "1s", absent |
| H08 | max_interval is positive integer >= initial_interval | max_interval < initial_interval |
| H09 | retryable_errors does NOT include 400/401/403 | Client errors in retry list |
| H10 | Body has all 3 required sections | Missing Retry Behavior, Backoff Calculation, or Error Classification |

## SOFT Scoring

| Dimension | Weight | Criteria |
|---|---|---|
| Jitter configuration | 1.0 | jitter is FULL or DECORRELATED (not NONE) |
| max_attempts in safe range | 1.0 | max_attempts in [3, 10] |
| Backoff calculation table | 1.0 | Per-attempt delays calculated and shown |
| Error classification completeness | 1.0 | Both retryable and non-retryable defined |
| retry_budget declared | 1.0 | Prevents retry storm |
| backoff_strategy explained | 0.5 | Rationale for chosen strategy |
| Boundary clarity | 1.0 | Explicitly NOT circuit_breaker, NOT rate_limit_config |
| tldr quality | 0.5 | tldr <= 160ch, includes operation, max_attempts, jitter |

## Actions

| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
