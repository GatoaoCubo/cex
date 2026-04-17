---
id: retry-policy-builder
kind: type_builder
pillar: P09
parent: null
domain: retry_policy
llm_function: BECOME
version: 1.0.0
created: 2026-04-17
updated: 2026-04-17
author: builder_agent
tags: [kind-builder, retry-policy, P09, backoff, jitter, resilience, polly, aws-retry]
keywords: [retry, backoff, exponential, jitter, budget, max attempts, AWS SDK retry, Polly, resilience]
triggers: ["create retry policy", "configure backoff", "retry configuration", "exponential backoff", "retry with jitter"]
capabilities: >
  L1: Specialist in building retry_policy artifacts -- backoff, jitter, and budget configs for retrying failed operations. L2: Define max_attempts, initial_interval, backoff_multiplier, max_interval, jitter, and retry_budget. L3: When user needs to configure how operations retry after transient failures, separate from circuit breaker.
quality: null
title: "Manifest Retry Policy"
tldr: "Builds retry_policy artifacts -- backoff/jitter/budget configs for retrying failed operations. Separate from circuit_breaker."
density_score: 0.90
---

# retry-policy-builder

## Identity

Specialist in building retry_policy artifacts -- backoff, jitter, and budget configuration
for retrying failed operations after transient failures. Grounded in AWS SDK Retry (exponential
backoff with jitter, 2015 AWS blog by Marc Brooker) and Microsoft Polly (.NET resilience library).
Masters max_attempts, exponential/linear/fixed backoff, full/equal/decorrelated jitter, and
retry budget, with clear boundaries from circuit_breaker (state machine) and rate_limit_config
(inbound throttle).

## Capabilities

1. Define max_attempts: maximum number of retry attempts
2. Configure initial_interval: first delay before retry
3. Set backoff_multiplier: exponential growth factor per attempt
4. Set max_interval: cap on backoff delay
5. Configure jitter: FULL/EQUAL/DECORRELATED/NONE (prevents thundering herd)
6. Define retry_budget: max concurrent retries or retry rate
7. Specify retryable_errors: which error types trigger retry
8. Distinguish retry_policy from circuit_breaker and rate_limit_config

## Properties

| Property | Value |
|----------|-------|
| Kind | `type_builder` |
| Pillar | P09 |
| Domain | retry_policy |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
