---
kind: architecture
id: bld_architecture_retry_policy
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of retry_policy -- inventory, dependencies, and architectural position
quality: null
title: "Architecture Retry Policy"
version: "1.0.0"
author: n03_builder
tags: [retry_policy, builder, architecture]
tldr: "Component map: max_attempts, initial_interval, backoff_multiplier, max_interval, jitter, retry_budget, retryable_errors. External: circuit_breaker, rate_limit_config."
domain: "retry policy construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| max_attempts | Maximum number of retry attempts before giving up | retry_policy | required |
| initial_interval | Delay before first retry (milliseconds) | retry_policy | required |
| backoff_strategy | Algorithm for calculating delay: exponential/linear/fixed | retry_policy | required |
| backoff_multiplier | Growth factor for exponential backoff (e.g. 2.0 = doubles) | retry_policy | conditional |
| max_interval | Maximum delay cap to prevent infinite backoff | retry_policy | required |
| jitter | Randomization to prevent thundering herd: FULL/EQUAL/DECORRELATED/NONE | retry_policy | recommended |
| retry_budget | Max concurrent retries or retry rate (prevents retry storms) | retry_policy | recommended |
| retryable_errors | Error types that trigger retry vs. fail immediately | retry_policy | required |
| non_retryable_errors | Error types that must NOT trigger retry | retry_policy | recommended |
| circuit_breaker | Open/closed state machine (separate concern) | P09 (separate kind) | external |
| rate_limit_config | Inbound request throttle (separate concern) | P09 (separate kind) | external |

## Backoff Strategy Comparison

| Strategy | Formula | Use When |
|----------|---------|----------|
| exponential | delay = initial * multiplier^attempt | Default -- most failures are transient |
| linear | delay = initial * attempt | Predictable, uniform growth |
| fixed | delay = initial (constant) | Known fixed recovery time |
| decorrelated | delay = min(max, rand(initial, prev * 3)) | AWS recommendation -- best jitter |

## Jitter Types (AWS Marc Brooker 2015)

| Jitter | Formula | Effect |
|--------|---------|--------|
| NONE | delay = base (no randomization) | Synchronized retries -- thundering herd |
| FULL | delay = rand(0, base) | Most spread -- good for high concurrency |
| EQUAL | delay = base/2 + rand(0, base/2) | Balanced -- some predictability |
| DECORRELATED | delay = min(max, rand(initial, prev*3)) | AWS recommended -- best distribution |

## Boundary Table

| retry_policy IS | retry_policy IS NOT |
|-----------------|---------------------|
| Backoff and jitter config for retrying | State machine that disables dependency (that is circuit_breaker) |
| Per-operation retry budget | Inbound request throttle (that is rate_limit_config) |
| Transient failure recovery config | Long-running process coordinator (that is process_manager) |
| Retry attempt count and intervals | Fallback to different provider (that is fallback_chain) |

## Layer Map

| Layer | Components | Purpose |
|-------|-----------|---------|
| attempt | max_attempts | How many times to try |
| timing | initial_interval, backoff_multiplier, max_interval | When to retry |
| distribution | jitter | Prevent synchronized retries |
| budget | retry_budget | Prevent retry storms |
| error filter | retryable_errors, non_retryable_errors | What to retry |
