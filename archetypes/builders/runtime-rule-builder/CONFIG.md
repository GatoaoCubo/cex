---
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: runtime_rule Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p09_rr_{rule_slug}.yaml` | `p09_rr_payment_api_retry.yaml` |
| Builder directory | kebab-case | `runtime-rule-builder/` |
| Frontmatter fields | snake_case | `rule_name`, `rule_type` |
| Rule slug | snake_case, lowercase, no hyphens | `payment_api_retry`, `brain_query_timeout` |

Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.

## File Paths
- Output: `cex/P09_config/examples/p09_rr_{rule_slug}.yaml`
- Compiled: `cex/P09_config/compiled/p09_rr_{rule_slug}.yaml`

## Size Limits (aligned with SCHEMA)
- Body: max 3072 bytes
- Total (frontmatter + body): ~4500 bytes
- Density: >= 0.80 (no filler)

## Rule Type Reference

| Type | Core parameters | Typical scope |
|------|----------------|---------------|
| timeout | duration (ms/s), connect_timeout, read_timeout | API calls, DB queries |
| retry | max_retries, base_delay, strategy, max_delay, total_budget | Network calls, transient failures |
| rate_limit | requests_per_second, burst_size, window, algorithm | API endpoints, external services |
| circuit_breaker | failure_threshold, recovery_timeout, half_open_requests | Service dependencies |
| concurrency | max_parallel, queue_size, rejection_policy | Worker pools, batch processing |

## Unit Conventions

| Unit | Abbreviation | When to use |
|------|-------------|-------------|
| milliseconds | ms | Timeouts < 10s, retry delays |
| seconds | s | Timeouts >= 10s, recovery windows |
| minutes | min | Long recovery, measurement windows |
| requests/second | req/s | Rate limits |
| count | count | Retries, thresholds, queue sizes |
