---
kind: config
id: bld_config_runtime_rule
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Runtime Rule"
version: "1.0.0"
author: n03_builder
tags: [runtime_rule, builder, examples]
tldr: "Golden and anti-examples for runtime rule construction, demonstrating ideal structure and common pitfalls."
domain: "runtime rule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_memory_scope
  - bld_examples_runtime_rule
  - bld_schema_runtime_rule
  - p03_ins_runtime_rule
  - bld_config_retriever_config
  - bld_config_prompt_version
  - bld_config_output_validator
  - bld_config_chunk_strategy
  - bld_config_effort_profile
  - bld_config_handoff_protocol
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_memory_scope]] | sibling | 0.34 |
| [[bld_examples_runtime_rule]] | upstream | 0.33 |
| [[bld_schema_runtime_rule]] | upstream | 0.33 |
| [[p03_ins_runtime_rule]] | related | 0.32 |
| [[bld_config_retriever_config]] | sibling | 0.31 |
| [[bld_config_prompt_version]] | sibling | 0.31 |
| [[bld_config_output_validator]] | sibling | 0.31 |
| [[bld_config_chunk_strategy]] | sibling | 0.30 |
| [[bld_config_effort_profile]] | sibling | 0.30 |
| [[bld_config_handoff_protocol]] | sibling | 0.29 |
