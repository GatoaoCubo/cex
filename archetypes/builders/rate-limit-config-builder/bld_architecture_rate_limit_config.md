---
kind: architecture
id: bld_architecture_rate_limit_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of rate_limit_config — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Rate Limit Config"
version: "1.0.0"
author: n03_builder
tags: [rate_limit_config, builder, examples]
tldr: "Golden and anti-examples for rate limit config construction, demonstrating ideal structure and common pitfalls."
domain: "rate limit config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

## Component Inventory

This ISO encodes a rate limit policy -- throttle bounds, quota windows, and backoff behavior.
| Name | Role | Owner | Status |
|------|------|-------|--------|
| rpm | Requests-per-minute quota — hard ceiling on call frequency | rate_limit_config | required |
| tpm | Tokens-per-minute quota — hard ceiling on token throughput | rate_limit_config | required |
| rpd | Requests-per-day quota — daily hard cap beyond RPM | rate_limit_config | required |
| concurrent | Max parallel in-flight requests at any instant | rate_limit_config | required |
| tier | Provider-defined service level controlling all limits | rate_limit_config | required |
| budget_usd | Monthly USD spend cap — cost guardrail | rate_limit_config | recommended |
| alert_threshold | Fraction of limit that triggers proactive notification | rate_limit_config | recommended |
| retry_after | Seconds to wait after receiving a 429 response | rate_limit_config | recommended |
| model_overrides | Per-model rpm/tpm when provider enforces model-level limits | rate_limit_config | optional |
| runtime_rule | Retry logic, backoff strategy, timeout policy | P09 (separate kind) | external |
| env_config | Generic environment variables (API keys, endpoints) | P09 (separate kind) | external |
| guardrail | Execution constraints beyond rate limits | P11 | external |
| client | API consumer that reads rate_limit_config at runtime | P04 | consumer |
| agent | Orchestrator that enforces limits during task execution | P02 | consumer |
## Dependency Graph
```
tier          --produces--> rpm
tier          --produces--> tpm
tier          --produces--> rpd
tier          --produces--> concurrent
budget_usd    --produces--> alert_threshold
rpm           --constrains--> client
tpm           --constrains--> client
concurrent    --constrains--> client
retry_after   --informs-->  runtime_rule
model_overrides --overrides--> rpm
model_overrides --overrides--> tpm
agent         --reads-->    rate_limit_config
guardrail     --depends-->  rate_limit_config
```
| From | To | Type | Data |
|------|----|------|------|
| tier | rpm | produces | tier-defined RPM ceiling |
| tier | tpm | produces | tier-defined TPM ceiling |
| budget_usd | alert_threshold | produces | fractional alert trigger |
| rpm | client | constrains | max call frequency |
| tpm | client | constrains | max token throughput |
| retry_after | runtime_rule | informs | suggested wait time after 429 |
| model_overrides | rpm | overrides | per-model ceiling replaces tier default |
| agent | rate_limit_config | reads | enforces quotas during execution |
## Boundary Table
| rate_limit_config IS | rate_limit_config IS NOT |
|----------------------|--------------------------|
| Declarative quota spec for provider/tier | Retry logic or backoff strategy (that is runtime_rule) |
| RPM, TPM, RPD, concurrent numeric limits | Generic env vars like API_KEY or BASE_URL (that is env_config) |
| Budget cap with alert threshold | Execution timeouts or circuit breakers (that is guardrail) |
| Static config artifact consumed by callers | API consumer code (that is client) |
| Provider-specific, tier-specific limits | Universal limits applying across all providers |
| read-only declarative spec | mutable runtime state tracker |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| quota | rpm, tpm, rpd, concurrent | Declare hard numeric ceilings from provider |
| cost | budget_usd, alert_threshold | Declare financial guardrails |
| policy | tier, retry_after | Declare tier level and 429 recovery hint |
| override | model_overrides | Per-model exceptions to tier defaults |
| external | runtime_rule, env_config, guardrail | Adjacent concerns handled by other kinds |
| consumers | client, agent | Runtime actors that enforce these limits |
