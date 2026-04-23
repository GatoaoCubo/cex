---
kind: schema
id: bld_schema_backpressure_policy
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for backpressure_policy
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 8.9
title: "Schema Backpressure Policy"
version: "1.0.0"
author: n03_builder
tags: [backpressure_policy, builder, schema]
tldr: "Schema for backpressure_policy: overflow_strategy, buffer_size, shed_threshold, watermarks, request_batch_size."
domain: "backpressure policy construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_schema_golden_test
  - bld_schema_retriever_config
  - bld_schema_action_prompt
  - bld_schema_smoke_eval
  - bld_schema_output_validator
  - bld_schema_reranker_config
  - bld_schema_unit_eval
  - bld_schema_runtime_state
  - bld_schema_handoff_protocol
  - bld_schema_effort_profile
---

# Schema: backpressure_policy

## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_bp_{slug}) | YES | - | Namespace compliance |
| kind | literal "backpressure_policy" | YES | - | Type integrity |
| pillar | literal "P09" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| overflow_strategy | enum | YES | - | DROP_LATEST, DROP_OLDEST, BUFFER, THROTTLE, ERROR |
| buffer_size | integer | YES | - | Max items buffered before overflow |
| shed_threshold | float 0.0-1.0 | YES | - | Fraction of buffer to start shedding |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "backpressure_policy" |
| tldr | string <= 160ch | YES | - | Dense summary |
| high_watermark | integer | REC | - | Queue depth triggering active backpressure |
| low_watermark | integer | REC | - | Queue depth at which normal flow resumes |
| request_batch_size | integer | REC | - | Items per Reactive Streams demand signal |
| monitored_queue | string | REC | - | Queue/channel/topic this policy governs |

## Overflow Strategy Enum
| Value | Semantics | Use When |
|-------|-----------|---------|
| DROP_LATEST | Discard newest incoming items | Freshness matters less than stability |
| DROP_OLDEST | Discard oldest buffered items | Recency more important than completeness |
| BUFFER | Accumulate up to buffer_size | Bursty traffic with recoverable lag |
| THROTTLE | Slow producer to consumer rate | Producer rate can be controlled |
| ERROR | Raise exception | Caller must handle overflow explicitly |

## ID Pattern
Regex: `^p09_bp_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)
1. `## Overview` -- producer-consumer context and why backpressure matters
2. `## Strategy` -- overflow_strategy with rationale
3. `## Thresholds` -- buffer_size, shed_threshold, watermarks
4. `## Flow` -- request_batch_size, demand signaling protocol

## Constraints
- max_bytes: 2048 (body only)
- overflow_strategy MUST be one of the 5 enum values
- buffer_size MUST be positive integer
- shed_threshold MUST be float in [0.0, 1.0]
- quality: null always
- NOT circuit_breaker (no state machine), NOT rate_limit_config (no RPM/TPM)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_golden_test]] | sibling | 0.58 |
| [[bld_schema_retriever_config]] | sibling | 0.57 |
| [[bld_schema_action_prompt]] | sibling | 0.57 |
| [[bld_schema_smoke_eval]] | sibling | 0.57 |
| [[bld_schema_output_validator]] | sibling | 0.56 |
| [[bld_schema_reranker_config]] | sibling | 0.56 |
| [[bld_schema_unit_eval]] | sibling | 0.56 |
| [[bld_schema_runtime_state]] | sibling | 0.56 |
| [[bld_schema_handoff_protocol]] | sibling | 0.56 |
| [[bld_schema_effort_profile]] | sibling | 0.56 |
