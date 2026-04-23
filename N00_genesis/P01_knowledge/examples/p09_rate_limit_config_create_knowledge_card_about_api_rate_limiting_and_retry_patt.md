---
id: p01_kc_api_rate_limiting_retry_patterns
kind: knowledge_card
type: infrastructure
pillar: P01
title: "API Rate Limiting and Retry Patterns"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "rate-limit-config-builder"
domain: rate_limit_config
quality: 9.1
tags: [knowledge_card, rate-limiting, retry-patterns, rpm, tpm, api, 429, backoff, provider]
tldr: "RPM/TPM quotas prevent provider throttling; exponential backoff + jitter + retry-after header prevent 429 cascade storms across LLM APIs."
when_to_use: "Integrating with LLM APIs, designing retry logic, configuring provider quotas, debugging 429 floods, sizing concurrent request pools"
keywords: [rpm, tpm, rpd, rate-limit, retry, backoff, jitter, 429, token-bucket, sliding-window, anthropic, openai, litellm, concurrent]
density_score: 0.93
related:
  - bld_knowledge_card_rate_limit_config
  - bld_examples_rate_limit_config
  - bld_collaboration_rate_limit_config
  - rate-limit-config-builder
  - p03_sp_rate_limit_config_builder
  - p01_kc_rate_limit_config
  - bld_knowledge_card_model_provider
  - p10_lr_rate_limit_config_builder
  - bld_instruction_rate_limit_config
  - bld_architecture_rate_limit_config
---
# API Rate Limiting and Retry Patterns

## Core Concept

LLM API providers enforce **three orthogonal quota axes**: requests per minute (RPM), tokens per minute (TPM), and requests per day (RPD). A single call can hit any axis independently — a short 5-token request counts against RPM even if TPM headroom is abundant. Concurrent limits add a fourth axis: max parallel in-flight requests regardless of per-minute rate.

Rate limiting is **declarative** (what the limits are) and separate from retry logic (how to recover from violations). Conflating the two is the root cause of most 429 cascade incidents.

**Algorithms in use:**
- **Token bucket** (TPM): bucket refills at a fixed rate per second; bursts allowed up to bucket capacity
- **Sliding window** (RPM): requests counted over a rolling 60s window; smoother than fixed windows, harder to game
- **Daily hard cap** (RPD): resets at UTC midnight; Anthropic enforces this, OpenAI Tier 1+ does not

## Provider Reference

| Provider | Tier | RPM | TPM | RPD | Concurrent | retry_after |
|----------|------|-----|-----|-----|------------|-------------|
| Anthropic | Free | 5 | 20,000 | 50 | 5 | 60s |
| Anthropic | Build | 50 | 80,000 | 1,000 | 10 | 60s |
| Anthropic | Scale | 4,000 | 400,000 | 100,000 | 50 | 60s |
| OpenAI | Free | 3 | 40,000 | — | 3 | varies |
| OpenAI | Tier 1 | 500 | 200,000 | — | 10 | varies |
| OpenAI | Tier 2 | 5,000 | 2,000,000 | — | 50 | varies |
| OpenAI | Tier 5 | 10,000 | 10,000,000 | — | 100 | varies |
| LiteLLM | proxy | configurable | configurable | configurable | configurable | passthrough |

**Model overrides**: Anthropic Opus caps at 40K TPM on Build tier; Haiku allows 100K TPM. Always check per-model limits against the provider dashboard, not just tier defaults.

## Retry Patterns

**Rule 1 — Honor `Retry-After`**: Anthropic 429 responses include `Retry-After: 60`. Ignoring this header and using a shorter fixed retry causes exponential amplification of the initial spike.

**Rule 2 — Exponential backoff with full jitter**:
```
wait = min(cap, base * 2^attempt) * random(0, 1)
```
- `base`: 1s, `cap`: 60s for most providers
- Full jitter (multiply by `random(0,1)`) prevents thundering herd when multiple clients hit the limit simultaneously
- Equal jitter (`base/2 + random(0, base/2)`) is acceptable when minimum latency matters

**Rule 3 — Budget before retry**: Check `budget_usd` headroom before retrying. A 429 caused by budget exhaustion (not rate quota) will never succeed regardless of wait time.

**Pattern summary**:
| Pattern | When | Risk if skipped |
|---------|------|-----------------|
| Honor `Retry-After` | Always on 429 | Retry storm, amplified throttling |
| Exponential + jitter | Transient 429 | Synchronized retry flood |
| Max retry cap | All retries | Infinite loops on hard errors |
| Budget check pre-retry | Budget-gated 429 | Infinite retry against exhausted budget |
| Circuit breaker | Sustained 429 (>5 min) | Continuous waste during provider incident |

## When to Use / When NOT

**Use rate_limit_config + retry patterns when:**
- Integrating with any LLM provider API
- Running parallel agent workflows with shared quota
- Designing cost-controlled production deployments
- Debugging unexpected 429 floods in staging or prod

**Do NOT use for:**
- Timeout policies (→ `runtime_rule`)
- API key/endpoint configuration (→ `env_config`)
- Execution constraints beyond rate limits (→ `guardrail`)
- Client-side throttling code implementation (→ `client`)

## Anti-Patterns

| Anti-Pattern | Failure Mode |
|--------------|-------------|
| Fictional RPM/TPM values in config | False capacity ceiling; real 429s arrive unexpectedly |
| Fixed 1s retry without jitter | Thundering herd; all clients retry simultaneously |
| No `budget_usd` cap | Runaway agent exhausts monthly spend silently |
| `alert_threshold: 1.0` | Alert fires at 100% — too late to react |
| Sharing one config across multiple providers | Each provider has independent limit pools; shared config masks real headroom |
| Mixing retry logic into rate_limit_config | Concerns bleed; changes to retry policy require rate config edits |
| `rpd` absent when provider enforces daily cap | Daily cap hit midday with no config record of why |

## CEX Integration

- `rate_limit_config` (P09): declares RPM, TPM, RPD, budget, alert threshold — static quota spec
- `runtime_rule` (P09): implements retry logic, backoff strategy, circuit breaker — enforcement layer
- `env_config` (P09): API key, base URL, model selection — connection layer
- `guardrail` (P11): cost circuit breakers, execution hard stops — safety layer

**Canonical crew for provider integration**:
```
rate-limit-config-builder → quota declaration
runtime-rule-builder      → retry/backoff policy
env-config-builder        → API key + endpoint
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_rate_limit_config]] | sibling | 0.52 |
| [[bld_examples_rate_limit_config]] | downstream | 0.46 |
| [[bld_collaboration_rate_limit_config]] | downstream | 0.45 |
| [[rate-limit-config-builder]] | downstream | 0.44 |
| [[p03_sp_rate_limit_config_builder]] | downstream | 0.44 |
| [[p01_kc_rate_limit_config]] | sibling | 0.43 |
| [[bld_knowledge_card_model_provider]] | sibling | 0.40 |
| [[p10_lr_rate_limit_config_builder]] | downstream | 0.40 |
| [[bld_instruction_rate_limit_config]] | downstream | 0.39 |
| [[bld_architecture_rate_limit_config]] | downstream | 0.39 |
