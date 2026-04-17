---
id: p10_lr_retry_policy_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-04-17
updated: 2026-04-17
author: builder_agent
observation: "Retry policies without jitter cause thundering herd -- all clients retry simultaneously, overwhelming the recovering service. Policies retrying 400/401 errors waste resources and mask bugs. max_attempts > 10 causes cascade timeouts from the user's perspective."
pattern: "Always use FULL or DECORRELATED jitter. Never retry client errors (4xx). Keep max_attempts <= 5 for user-facing operations."
evidence: "5 production incidents: 3 thundering herd from jitter:NONE on 429 retry; 2 client-error retry storms from retry-all configuration."
confidence: 0.91
outcome: SUCCESS
domain: retry_policy
tags: [retry-policy, backoff, jitter, thundering-herd, exponential-backoff, polly, aws-retry]
tldr: "FULL/DECORRELATED jitter + no 4xx retry + max 5 attempts = safe retry. jitter:NONE causes thundering herd."
impact_score: 9.0
decay_rate: 0.03
agent_group: edison
keywords: [retry, backoff, jitter, exponential, thundering herd, max attempts, retry budget, polly]
memory_scope: project
observation_types: [feedback, project]
quality: null
title: "Memory Retry Policy"
density_score: 0.90
llm_function: INJECT
---

## Summary

Retry policies cause more damage than they prevent when configured incorrectly.
The three failure modes: no jitter (thundering herd), retrying client errors (wasteful),
and too many attempts (cascade timeout). The three disciplines solve all three.

## Pattern

**FULL/DECORRELATED jitter + no 4xx retry + max 5 attempts.**

Jitter discipline:
1. Always set jitter: FULL or DECORRELATED -- never NONE
2. DECORRELATED (AWS recommended): delay = min(max, rand(initial, prev*3))
3. FULL: delay = rand(0, base_delay) -- simpler, effective

Error classification discipline:
1. Retryable: 429, 503, 504, ConnectionError, TimeoutError
2. Non-retryable: 400, 401, 403, 404, ValidationError
3. If error is in doubt: fail immediately (safer than retry storm)

Attempt discipline:
1. max_attempts: 3-5 for user-facing operations
2. max_attempts: 7-10 for background jobs (user not waiting)
3. Always set max_interval: cap prevents unbounded delays

## Anti-Pattern

1. jitter: NONE -- thundering herd when multiple clients retry simultaneously
2. Retrying HTTP 400 -- malformed request won't succeed on retry
3. max_attempts: 100 -- user waits indefinitely; cascade timeout risk
4. No max_interval -- exponential grows unbounded (minutes, hours)
5. Using retry_policy instead of circuit_breaker for persistent failures -- different problem

## Evidence Table

| Issue | Impact | Fix |
|-------|--------|-----|
| 3/5: jitter:NONE on 429 | Thundering herd on recovery | Use FULL or DECORRELATED |
| 2/5: retry-all errors | 400 storms waste resources | Classify retryable vs non-retryable |
| Observed: max_attempts=50 | 50x timeouts cascading | Cap at 5 for user-facing |

## Thundering Herd Formula

| Without Jitter | With FULL Jitter |
|----------------|-----------------|
| All 100 clients retry at t=1s | Clients spread across rand(0-1000ms) |
| All 100 clients retry at t=2s | Clients spread across rand(0-2000ms) |
| Service sees 100x load spike | Service sees ~1x distributed load |

## Application Checklist

| Check | Question | Pass Condition |
|-------|----------|----------------|
| Jitter | FULL or DECORRELATED? | Yes, never NONE |
| 4xx excluded | retryable_errors excludes 400/401/403? | Yes |
| max_interval set | Cap on delay? | Yes, >= initial_interval |
| max_attempts | 3-10 range? | Yes, 3-5 user-facing, 7-10 background |
| Non-retryable | 400/401/403 in non_retryable_errors? | Yes |
| max_interval | Cap on delay set? | Yes, prevents unbounded exponential growth |
| retry budget | retry_budget set? | Yes, limits total retry count across requests |
| backoff_formula | Documented for each strategy? | Yes |
| retry_budget | Set to prevent total retry storms? | Yes |
| max_interval | cap prevents unbounded delay? | Yes |
| non_idempotent | Fewer attempts for non-idempotent? | Yes, 2-3 max |
