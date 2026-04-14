---
id: p11_qg_runtime_rule
kind: quality_gate
pillar: P11
title: "Gate: Runtime Rule"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: runtime_rule
quality: 9.0
density_score: 0.85
tags:
  - quality-gate
  - runtime-rule
  - p11
  - reliability
  - behavior
tldr: "Quality gate for runtime behavior specs: verifies rule type, numeric parameters with units, scope declaration, and recovery behavior."
llm_function: GOVERN
---
## Definition
A runtime rule artifact specifies how a single operation behaves under load, failure, or resource pressure. It declares a rule type (timeout, retry, rate_limit, or circuit_breaker), the numeric parameters that govern the rule with explicit units, and the scope of operations the rule applies to. Every rule must define what happens when its threshold is breached — silent failure is not acceptable.
Scope: files with `kind: runtime_rule`. Does not apply to lifecycle rules (P09 sub-kind) or feature flags (P14), which govern activation rather than execution behavior.
## HARD Gates
Failure on any single gate means REJECT regardless of soft score.
| ID  | Predicate | How to test |
|-----|-----------|-------------|
| H01 | Frontmatter parses as valid YAML | `yaml.safe_load(frontmatter)` raises no error |
| H02 | `id` matches namespace `p09_rr_*` | `id.startswith("p09_rr_")` is true |
| H03 | `id` equals filename stem | `Path(file).stem == id` |
| H04 | `kind` equals literal `runtime_rule` | string equality check |
| H05 | `quality` is null at authoring time | `quality is None` |
| H06 | All required frontmatter fields present and non-empty | id, kind, pillar, title, version, created, updated, author, domain, tags, tldr, rule_type, scope all present |
| H07 | `rule_type` is one of: timeout, retry, rate_limit, circuit_breaker | enum membership check |
| H08 | All numeric parameter values include explicit units (ms, s, req/s, count, percent) | scan parameter table; every numeric value row has a unit column that is non-empty |
| H09 | `scope` field declares what operation or component this rule governs | `scope` field is non-empty string |
## SOFT Scoring
Score each dimension 0 (absent or fails) to 1 (present and passes). Weights are 0.5 or 1.0.
| #  | Dimension | Weight |
|----|-----------|--------|
| 1  | `density_score` field present and >= 0.80 | 1.0 |
| 2  | Retry strategy specified as fixed, exponential, or jitter (not just "retry") | 1.0 |
| 3  | Timeout values have units and are grounded in observed latency data or documented assumptions | 1.0 |
| 4  | Rate limit has a time window defined (per second, per minute, per hour) | 1.0 |
| 5  | Circuit breaker has a recovery behavior defined (half-open probe interval, reset condition) | 1.0 |
| 6  | Tags list includes `runtime-rule` | 0.5 |
| 7  | Default parameter values documented for each numeric field | 1.0 |
| 8  | Edge cases for parameter boundaries described (what happens at zero, at max) | 0.5 |
| 9  | Monitoring hooks or observable signals identified (metric name, alert condition) | 0.5 |
| 10 | Rule is compatible with the declared runtime environment | 0.5 |
| 11 | `tldr` is <= 160 characters | 0.5 |
**Formula**: `final_score = (sum of score_i * weight_i) / (sum of weight_i) * 10`
Weight total: 8.5. Each dimension contributes proportionally. Score range: 0.0 to 10.0.
## Actions
| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Publish to pool as golden; use as reference for reliability engineering |
| PUBLISH | >= 8.0 | Publish to pool; mark production-ready |
| REVIEW | >= 7.0 | Return to author with scored dimension feedback; one revision cycle allowed |
| REJECT | < 7.0 | Block from pool; full rewrite required before re-evaluation |
## Bypass
| Field | Value |
|-------|-------|
| condition | Rule governs a third-party dependency whose latency profile is not yet characterized |
| approver | Domain lead must approve in writing before bypass takes effect |
| audit_log | Record in `records/pool/audits/bypasses.md` with date, approver, and reason |
