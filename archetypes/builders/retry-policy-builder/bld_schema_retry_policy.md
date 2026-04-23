---
quality: 8.9
quality: 8.2
kind: schema
id: bld_schema_retry_policy
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for retry_policy
pattern: TEMPLATE derives from this. CONFIG restricts this.
title: "Schema Retry Policy"
version: "1.0.0"
author: n03_builder
tags: [retry_policy, builder, schema]
tldr: "Schema for retry_policy: max_attempts, initial_interval, backoff_strategy, jitter, retryable_errors."
domain: "retry policy construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_golden_test
  - bld_schema_action_prompt
  - bld_schema_quickstart_guide
  - bld_schema_output_validator
  - bld_schema_handoff_protocol
  - bld_schema_unit_eval
  - bld_schema_retriever_config
  - bld_schema_smoke_eval
---

# Schema: retry_policy

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_rtp_{slug}) | YES | - | Namespace compliance |
| kind | literal "retry_policy" | YES | - | Type integrity |
| pillar | literal "P09" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact version |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| operation | string | YES | - | Operation being retried |
| max_attempts | integer >= 1 | YES | - | Max retry attempts |
| initial_interval | integer (ms) | YES | - | First retry delay in ms |
| backoff_strategy | enum | YES | exponential | exponential/linear/fixed/decorrelated |
| max_interval | integer (ms) | YES | - | Max delay cap in ms |
| jitter | enum | REC | FULL | FULL/EQUAL/DECORRELATED/NONE |
| backoff_multiplier | float > 1 | conditional | 2.0 | Required if backoff_strategy=exponential |
| retry_budget | integer | REC | - | Max concurrent retries |
| retryable_errors | list[string] | YES | - | Error types to retry |
| non_retryable_errors | list[string] | REC | - | Error types to fail immediately |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "retry_policy" |
| tldr | string <= 160ch | YES | - | Dense summary |

## ID Pattern

Regex: `^p09_rtp_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)

1. `## Retry Behavior` -- configuration table with all fields
2. `## Backoff Calculation` -- formula and example delays per attempt
3. `## Error Classification` -- retryable vs non-retryable errors

## Constraints

- max_bytes: 2048 (body only -- compact config artifact)
- max_attempts MUST be positive integer
- initial_interval MUST be positive integer (milliseconds)
- quality: null always
- NOT circuit_breaker (no state machine), NOT rate_limit_config (no inbound throttle)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | sibling | 0.64 |
| [[bld_schema_usage_report]] | sibling | 0.64 |
| [[bld_schema_golden_test]] | sibling | 0.63 |
| [[bld_schema_action_prompt]] | sibling | 0.63 |
| [[bld_schema_quickstart_guide]] | sibling | 0.63 |
| [[bld_schema_output_validator]] | sibling | 0.62 |
| [[bld_schema_handoff_protocol]] | sibling | 0.62 |
| [[bld_schema_unit_eval]] | sibling | 0.62 |
| [[bld_schema_retriever_config]] | sibling | 0.62 |
| [[bld_schema_smoke_eval]] | sibling | 0.62 |
