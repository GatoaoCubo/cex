---
kind: schema
id: bld_schema_circuit_breaker
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for circuit_breaker
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: null
title: "Schema Circuit Breaker"
version: "1.0.0"
author: n03_builder
tags: [circuit_breaker, builder, schema]
tldr: "Schema for circuit_breaker: state machine thresholds, cooldown, probe count, fallback response."
domain: "circuit breaker construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Schema: circuit_breaker

## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_cb_{slug}) | YES | - | Namespace compliance |
| kind | literal "circuit_breaker" | YES | - | Type integrity |
| pillar | literal "P09" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| service | string | YES | - | Protected dependency name |
| failure_rate_threshold | integer 1-100 | YES | - | % failures that trip breaker |
| cooldown_duration | integer (seconds) | YES | - | Seconds in OPEN state |
| probe_count | integer | YES | - | Half-open test calls |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "circuit_breaker" |
| tldr | string <= 160ch | YES | - | Dense summary |
| sliding_window_type | enum: COUNT_BASED, TIME_BASED | REC | COUNT_BASED | Window type |
| sliding_window_size | integer | REC | - | Count or seconds |
| minimum_number_of_calls | integer | REC | - | Min calls before rate computed |
| slow_call_threshold_ms | integer | REC | - | Slow call duration in ms |
| slow_call_rate_threshold | integer 1-100 | REC | - | % slow calls to trip breaker |
| fallback_response | string | REC | - | Response while OPEN |
| monitored_exceptions | list[string] | REC | - | Error types counted as failures |

## ID Pattern
Regex: `^p09_cb_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)
1. `## Overview` -- what dependency is protected and why
2. `## State Machine` -- CLOSED/OPEN/HALF-OPEN transitions and thresholds
3. `## Cooldown` -- duration, probe count, recovery policy
4. `## Fallback` -- response during OPEN state

## Constraints
- max_bytes: 3072 (body only)
- failure_rate_threshold MUST be integer in [1, 100]
- cooldown_duration MUST be positive integer (seconds)
- probe_count MUST be positive integer
- quality: null always
- NOT rate_limit_config (no RPM/TPM), NOT fallback_chain (no provider list)
