---
id: p11_qg_batch_config
kind: quality_gate
pillar: P11
title: "Gate: batch_config"
version: "1.0.0"
created: "2026-04-13"
updated: "2026-04-13"
author: "builder_agent"
domain: "batch_config -- async bulk API job configuration with cost controls, retry policy, and I/O format"
quality: 9.1
tags: [quality-gate, batch-config, async-api, cost-controls, P11]
tldr: "Gates for batch_config artifacts: validates provider, cost cap, completion window, retry policy, credential hygiene, and body section completeness."
density_score: 0.92
llm_function: GOVERN
---
# Gate: batch_config

## Definition

| Field | Value |
|-------|-------|
| metric | Composite score from SOFT dimensions + all HARD gates pass |
| threshold | >= 7.0 to publish; >= 9.5 golden |
| operator | AND (all HARD) + weighted_sum (SOFT) |
| scope | All artifacts where `kind: batch_config` |

## HARD Gates

All must pass. Any single failure = REJECT regardless of SOFT score.

| ID | Check | Failure message |
|----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | "Frontmatter YAML syntax error" |
| H02 | `id` matches `^p09_bc_[a-z][a-z0-9_]+$` | "ID fails batch_config namespace regex" |
| H03 | `id` value equals filename stem | "ID does not match filename" |
| H04 | `kind` equals literal `"batch_config"` | "Kind is not 'batch_config'" |
| H05 | `quality` field is `null` | "Quality must be null at authoring time" |
| H06 | All required fields present: id, kind, pillar, provider, model, endpoint, version, created, author, tags | "Missing required field(s)" |
| H07 | Body contains all 5 required sections: Overview, Job Parameters, Cost Controls, Retry and Error Policy, Input/Output Format | "Body missing required section(s)" |
| H08 | `completion_window` is >= 1h (batch is async; sub-hour = wrong kind) | "completion_window too short -- use runtime_rule for sync timeouts" |
| H09 | `cost_cap_usd` is set and is a positive number | "cost_cap_usd missing -- financial control gate failure" |
| H10 | No actual API keys, tokens, or credentials appear in any field | "Credential detected in artifact -- security violation" |

## SOFT Scoring

Dimensions sum to 100%. Score each 0.0-10.0; multiply by weight.

| Dimension | Weight | What to assess |
|-----------|--------|----------------|
| Cost control completeness | 1.5 | cost_cap_usd, max_requests, token_budget, alert threshold all specified |
| Retry policy specificity | 1.5 | max_retries, backoff type, partial_failure behavior, dead_letter path defined |
| Provider accuracy | 1.0 | Provider enum valid, model confirmed batch-eligible, endpoint path correct |
| Completion window rationale | 1.0 | Window matches provider SLA, downstream use documented |
| I/O format clarity | 1.0 | JSONL schema summary for both input and output, storage paths specified |
| Credential hygiene | 1.0 | Env var name referenced, no embedded values, storage guidance noted |
| Boundary clarity | 0.5 | Explicitly not schedule (cron), not workflow (multi-step), not runtime_rule |
| Concurrency specification | 0.5 | concurrency value set and reasonable for provider limits |
| Monitoring/alerting | 0.5 | Alert threshold defined, monitoring approach noted |
| Documentation density | 0.5 | tldr names provider, model, and scale; description is informative |

Weight sum: 1.5+1.5+1.0+1.0+1.0+1.0+0.5+0.5+0.5+0.5 = 9.0 (normalized to 100%)

## Actions

| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool as golden exemplar |
| >= 8.0 | PUBLISH | Publish to pool |
| >= 7.0 | REVIEW | Flag for human review before publish |
| < 7.0 | REJECT | Return to author with failure report |

## Bypass

| Field | Value |
|-------|-------|
| conditions | Early-stage batch integration where provider SLA is unknown |
| approver | Engineering lead approval required (written); cost_cap_usd and credential hygiene gates never bypassed |
