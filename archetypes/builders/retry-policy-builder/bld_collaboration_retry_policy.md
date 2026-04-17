---
kind: collaboration
id: bld_collaboration_retry_policy
pillar: P12
llm_function: COLLABORATE
purpose: How retry-policy-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: null
title: "Collaboration Retry Policy"
version: "1.0.0"
author: n03_builder
tags: [retry_policy, builder, collaboration]
tldr: "Transient failure recovery specialist. Complements circuit_breaker and rate_limit_config. Upstream of agent and api_client."
domain: "retry policy construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---
# Collaboration: retry-policy-builder
## My Role in Crews
| Responsibility | What I Answer | What I DON'T Do |
|----------------|---------------|-----------------|
| TRANSIENT FAILURE RECOVERY | "When this fails transiently, how to retry?" | Disable dependencies |
| Backoff + jitter config | Max attempts, intervals, randomization | Throttle inbound requests |
| Error classification | Which errors to retry vs fail immediately | Choose backup providers |
## Crew Compositions
### Crew: "Resilient API Integration"
```
  1. rate-limit-config-builder -> "quota declaration (RPM, TPM, budget)"
  2. circuit-breaker-builder   -> "fault isolation (failure threshold, cooldown)"
  3. retry-policy-builder      -> "backoff and jitter for transient failures"
  4. env-config-builder        -> "API key, base URL, timeout"
```
### Crew: "Production Hardening"
```
  1. circuit-breaker-builder   -> "dependency fault isolation"
  2. retry-policy-builder      -> "transient failure recovery"
  3. fallback-chain-builder    -> "provider substitution on persistent failure"
  4. monitor-builder           -> "retry count and circuit state observability"
```
## Handoff Protocol
### I Receive
| Input | Type | Notes |
|-------|------|-------|
| Operation name | string | API call, DB query, HTTP request |
| Expected transient errors | list | 429, 503, ConnectionError |
| User-facing SLA | duration | How long can user wait? |
| Traffic volume | integer | Affects jitter choice |
### I Produce
| Output | Format | Destination |
|--------|--------|-------------|
| retry_policy artifact | .md with YAML frontmatter + tables | N0X_{domain}/P09_config/ |
| Compilation signal | complete with quality score | .cex/runtime/signals/ |
## Builders I Depend On
| Builder | Why | Dependency Type |
|---------|-----|----------------|
| None | Independent builder (layer 0) | -- |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| agent-builder | Agents wrap operations with retry policy |
| api-client-builder | HTTP clients use retry policy for transient failures |
| circuit-breaker-builder | Retry is first; circuit breaker trips after repeated failures |
| monitor-builder | Monitors track retry count as health metric |
## Quality Checklist Before Signal
| Check | Pass Condition |
|-------|---------------|
| id pattern | ^p09_rtp_[a-z][a-z0-9_]+$ |
| max_attempts | positive integer in [3, 10] |
| initial_interval | positive integer (ms) |
| max_interval | >= initial_interval |
| jitter | FULL or DECORRELATED (not NONE) |
| retryable_errors | excludes 400/401/403 |
| non_retryable_errors | includes 400/401/403 |
| body sections | Retry Behavior + Backoff Calculation + Error Classification |
