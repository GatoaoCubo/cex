---
kind: instruction
id: bld_instruction_retry_policy
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for retry_policy
pattern: 3-phase pipeline (define -> compose -> validate)
quality: null
title: "Instruction Retry Policy"
version: "1.0.0"
author: n03_builder
tags: [retry_policy, builder, instruction]
tldr: "3-phase: classify errors and set attempt limits, configure backoff and jitter, validate ranges and anti-patterns."
domain: "retry policy construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Instructions: How to Produce a retry_policy

## Phase 1: DEFINE

1. Identify the operation being retried (API call, DB query, HTTP request)
2. Classify errors: which are transient (retry) vs. permanent (fail immediately)?
   - Transient: 429, 503, 504, ConnectionError, TimeoutError
   - Permanent: 400, 401, 403, InvalidRequestError, ValidationError
3. Determine max_attempts: typically 3-5 (1 initial + 2-4 retries)
4. Choose backoff_strategy: exponential (default), linear, fixed, or decorrelated
5. Set initial_interval (ms): first retry delay (100-2000ms typical)
6. Set backoff_multiplier if exponential (2.0 standard)
7. Set max_interval (ms): cap delay (10000-60000ms typical)
8. Choose jitter: FULL or DECORRELATED (prevents thundering herd)
9. Set retry_budget: max concurrent retries (prevent retry storm)

## Phase 2: COMPOSE

1. Read SCHEMA.md and OUTPUT_TEMPLATE.md
2. Fill frontmatter: all required fields (quality: null)
3. Set id: `p09_rtp_{operation_slug}` -- verify pattern `^p09_rtp_[a-z][a-z0-9_]+$`
4. Write Retry Behavior section: parameter table
5. Write Backoff Calculation section: delay per attempt table with jitter
6. Write Error Classification section: retryable vs non-retryable table
7. Verify body <= 2048 bytes (compact config artifact)

## Phase 3: VALIDATE

1. Confirm id matches `^p09_rtp_[a-z][a-z0-9_]+$`
2. Confirm kind == retry_policy
3. Confirm max_attempts is positive integer (3-10 range recommended)
4. Confirm initial_interval is positive integer (milliseconds)
5. Confirm max_interval >= initial_interval
6. Confirm jitter is not NONE (thundering herd risk)
7. Confirm retryable_errors does NOT include 400/401/403
8. Confirm all 3 body sections present
9. Cross-check: not circuit_breaker (no state machine), not rate_limit_config
10. Confirm quality: null
11. Revise if score < 8.0
