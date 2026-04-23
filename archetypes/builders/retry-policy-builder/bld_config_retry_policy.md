---
quality: 8.4
quality: 8.0
kind: config
id: bld_config_retry_policy
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: low
max_turns: 20
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
title: "Config Retry Policy"
version: "1.0.0"
author: n03_builder
tags: [retry_policy, builder, config]
tldr: "Naming: p09_rtp_{slug}.md. Max 2048 bytes. max_attempts 3-5. jitter: FULL or DECORRELATED. Never retry 400/401/403."
domain: "retry policy construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_examples_runtime_rule
  - bld_memory_runtime_rule
  - p03_ins_runtime_rule
  - p01_kc_api_rate_limiting_retry_patterns
  - p01_kc_runtime_rule
  - runtime-rule-builder
  - bld_schema_client
  - p01_kc_error_recovery
  - bld_instruction_input_schema
  - bld_config_runtime_rule
---

# Config: retry_policy Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p09_rtp_{operation_slug}.md` | `p09_rtp_anthropic_api.md` |
| Builder directory | kebab-case | `retry-policy-builder/` |
| Frontmatter fields | snake_case | `max_attempts`, `initial_interval` |
| Operation slug | snake_case, lowercase | `anthropic_api`, `postgres_write` |

Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.

## File Paths

- Output: `N0X_{domain}/P09_config/p09_rtp_{operation_slug}.md`
- Compiled: `N0X_{domain}/P09_config/compiled/p09_rtp_{operation_slug}.yaml`

## Size Limits

- Body: max 2048 bytes (compact config, not documentation)
- Density: >= 0.80 (tables)

## Recommended Ranges

| Parameter | Recommended Range | Typical Default |
|-----------|-----------------|-----------------|
| max_attempts | 3-5 | 4 |
| initial_interval | 100-2000ms | 1000ms |
| backoff_multiplier | 1.5-3.0 | 2.0 |
| max_interval | 10000-60000ms | 30000ms |
| retry_budget | 5-20 | 10 |

## Error Classification Rules

| Error Category | Action | Examples |
|----------------|--------|---------|
| 5xx server errors (503/504) | RETRY | Service unavailable, gateway timeout |
| 429 rate limited | RETRY | Too many requests |
| Network errors | RETRY | ConnectionError, TimeoutError |
| 4xx client errors | FAIL IMMEDIATELY | 400/401/403/404 |
| Validation errors | FAIL IMMEDIATELY | InvalidRequestError, SchemaError |
| Auth errors | FAIL IMMEDIATELY | 401 Unauthorized, 403 Forbidden |

## Jitter Selection Guide

| Concurrency | Jitter | Reason |
|-------------|--------|--------|
| High (> 100 clients) | DECORRELATED | Best distribution, AWS recommended |
| Medium (10-100 clients) | FULL | Good distribution, simpler |
| Low (< 10 clients) | EQUAL | Slight predictability |
| Single client | NONE | No thundering herd risk |

## Backoff Strategy Comparison

| Strategy | Formula | Initial=100ms at attempt 3 |
|----------|---------|---------------------------|
| exponential | initial * multiplier^attempt | 100 * 2^3 = 800ms |
| linear | initial * attempt | 100 * 3 = 300ms |
| fixed | initial (constant) | 100ms |
| decorrelated | min(max, rand(initial, prev*3)) | rand(100, prev*3) |

## Operation Type Recommendations

| Operation Type | max_attempts | initial_interval | Notes |
|----------------|-------------|-----------------|-------|
| User-facing API call | 3-4 | 500-1000ms | User waiting; fail fast |
| Background job | 5-7 | 1000-2000ms | User not waiting |
| Idempotent write | 4-5 | 1000ms | Safe to retry |
| Non-idempotent write | 2-3 | 2000ms | Risk of duplicate |

## Required Frontmatter Fields

| Field | Type | Constraint |
|-------|------|------------|
| operation | string | Operation being protected |
| max_attempts | integer | 3-10 range |
| initial_interval | integer ms | > 0 |
| max_interval | integer ms | >= initial_interval |
| backoff_multiplier | float | 1.5-3.0 |
| jitter | enum | FULL or DECORRELATED (not NONE) |
| retryable_errors | list | Excludes 400/401/403 |
| non_retryable_errors | list | Includes 400/401/403 |
| retry_budget | integer | Limits total retries across concurrent requests |
| timeout | string (ms) | Total operation timeout including all retries |
| deadline | string (ms) | Hard deadline before circuit breaker kicks in |
| description | string | Human-readable purpose of this retry policy |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_runtime_rule]] | upstream | 0.31 |
| [[bld_memory_runtime_rule]] | downstream | 0.26 |
| [[p03_ins_runtime_rule]] | related | 0.26 |
| [[p01_kc_api_rate_limiting_retry_patterns]] | upstream | 0.23 |
| [[p01_kc_runtime_rule]] | related | 0.23 |
| [[runtime-rule-builder]] | related | 0.22 |
| [[bld_schema_client]] | upstream | 0.22 |
| [[p01_kc_error_recovery]] | upstream | 0.22 |
| [[bld_instruction_input_schema]] | upstream | 0.21 |
| [[bld_config_runtime_rule]] | sibling | 0.21 |
