---
kind: quality_gate
id: p11_qg_runtime_rule
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of runtime_rule artifacts
pattern: "few-shot learning \u2014 LLM reads these before producing"
quality: 9.0
title: 'Gate: Runtime Rule'
version: 1.0.0
author: builder
tags:
- eval
- P11
- quality_gate
- examples
tldr: 'Quality gate for runtime behavior specs: verifies rule type, numeric parameters
  with units, scope declaration, and recovery behavior.'
domain: runtime_rule
created: '2026-03-27'
updated: '2026-03-27'
density_score: 0.85
related:
  - p11_qg_quality_gate
  - p11_qg_response_format
  - p11_qg_runtime_state
  - p03_ins_runtime_rule
  - p11_qg_router
  - bld_knowledge_card_runtime_rule
  - p11_qg_prompt_template
  - bld_examples_runtime_rule
  - p11_qg_creation_artifacts
  - p11_qg_thinking_config
---

## Quality Gate

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

## Examples

# Examples: runtime-rule-builder
## Golden Example
INPUT: "Define retry rules for the API client connecting to external payment provider"
OUTPUT:
```yaml
id: p09_rr_payment_api_retry
kind: runtime_rule
pillar: P09
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
rule_name: "payment_api_retry"
rule_type: retry
scope: "payment_connector"
quality: 8.9
tags: [runtime_rule, retry, payment, P09, api, resilience]
tldr: "Payment API retry: exponential backoff 500ms base, 3 max, jitter, 5s total budget"
description: "Retry strategy for external payment API calls with exponential backoff and jitter"
fallback: "Return payment_unavailable error after 3 retries exhausted"
severity: critical
```
## Rule Specification
| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| max_retries | 3 | count | After 3 failures, stop retrying |
| base_delay | 500 | ms | Initial wait before first retry |
| strategy | exponential_jitter | - | base * 2^attempt + random(0, 250ms) |
| max_delay | 4000 | ms | Cap on any single retry delay |
| total_budget | 5000 | ms | Max total time for all retries |
| retryable_codes | [408, 429, 500, 502, 503] | HTTP | Only retry on transient errors |
## Trigger Behavior
When max_retries exhausted: return `payment_unavailable` error to caller.
When rate-limited (429): respect Retry-After header if present, else use backoff.
When total_budget exceeded: abort remaining retries, return timeout error.
Log every retry attempt with: attempt number, wait duration, error code.
## Tuning Guide
- base_delay: increase to 1000ms if payment provider has strict rate limits
- max_retries: do not exceed 5 (risk of duplicate payments)
- Monitor: retry_count metric, success_after_retry_rate, total_budget_exceeded_count
- Safe range: base_delay 200-2000ms, max_retries 1-5, total_budget 3000-15000ms
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p09_rr_ pattern (H02 pass)
- kind: runtime_rule (H04 pass)
- 19 required+recommended fields present (H06 pass)
- body has all 3 sections: Rule Specification, Trigger Behavior, Tuning Guide (H07 pass)
- rule_type: retry (valid enum) (H08 pass)
- All values have units (ms, count, HTTP) (H09 pass)
- No vague terms — all concrete numbers (S05 pass)
- tldr: 75 chars <= 160 (S01 pass)
- tags: 6 items, includes "runtime_rule" (S02 pass)
## Anti-Example
INPUT: "Create retry rules"
BAD OUTPUT:
```yaml
id: retry-rules
kind: rule
pillar: runtime
rule_name: Retry
rule_type: general
timeout: fast
retries: some
quality: 8.5
tags: [retry]
```
Retry when things fail. Wait a bit between retries.
FAILURES:
1. id: "retry-rules" uses hyphens, no `p09_rr_` prefix -> H02 FAIL
2. kind: "rule" not "runtime_rule" -> H04 FAIL
3. pillar: "runtime" not "P09" -> H06 FAIL
4. rule_type: "general" not in enum [timeout, retry, rate_limit, circuit_breaker, concurrency] -> H08 FAIL
5. quality: 8.5 (not null) -> H05 FAIL
6. timeout: "fast" — vague, no numeric value with units -> H09 FAIL
7. retries: "some" — vague, no numeric value -> H09 FAIL
8. Missing fields: version, created, updated, author, scope, tldr -> H06 FAIL
9. tags: only 1 item, missing "runtime_rule" -> S02 FAIL
10. Body missing ## Rule Specification, ## Trigger Behavior, ## Tuning Guide -> H07 FAIL
11. No fallback behavior defined -> S06 FAIL
12. "Wait a bit" is vague — no concrete delay values -> S05 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
