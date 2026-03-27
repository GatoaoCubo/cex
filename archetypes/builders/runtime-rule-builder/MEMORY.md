---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: runtime-rule-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Using hyphens in id slug (must be underscores: p09_rr_api_timeout not p09_rr_api-timeout)
2. Setting quality to a number instead of null (H05 rejects any non-null value)
3. Timeout without units: "timeout: 30" (30 what? ms? s? min?)
4. Vague values: "retries: some", "timeout: fast" (must be concrete numbers)
5. rule_type: "general" or "mixed" (must be one of: timeout, retry, rate_limit, circuit_breaker, concurrency)
6. Confusing runtime_rule with law (P08): rules are configurable, laws are inviolable
7. Missing fallback behavior (what happens when timeout hits? when retries exhaust?)
8. No tuning guide (operators need safe ranges and metrics to monitor)
9. Mixing multiple rule types in one artifact (one rule_type per artifact)
10. Missing Trigger Behavior section (required — defines what happens when rule activates)

### Rule Type Defaults
| Type | Typical Base Value | Typical Max |
|------|-------------------|-------------|
| timeout | 5000ms (API), 30000ms (DB) | 120000ms |
| retry | 3 attempts, 500ms base | 5 attempts, 30s budget |
| rate_limit | 100 req/s (internal), 10 req/s (external) | 1000 req/s |
| circuit_breaker | 5 failures threshold, 30s recovery | 50% failure rate |
| concurrency | 10 parallel (default) | 100 parallel |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | unit omission, vague terms, boundary drift toward law/lifecycle |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a runtime_rule, update:
- New common mistake (if encountered)
- New rule type default (if discovered)
- Production counter increment
