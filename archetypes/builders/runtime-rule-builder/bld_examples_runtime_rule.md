---
kind: examples
id: bld_examples_runtime_rule
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of runtime_rule artifacts
pattern: few-shot learning — LLM reads these before producing
---

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
quality: null
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
