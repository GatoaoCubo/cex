---
id: p09_rate_limit_config_create_knowledge_card_about_api_rate_limiting_and_retry_patt
kind: knowledge_card
type: kind
pillar: P01
title: "API Rate Limiting and Retry Patterns"
version: 1.1.0
created: "2026-04-02"
updated: "2026-04-02"
author: "rate-limit-config-builder"
domain: rate_limit_config
quality: 9.1
tags: [knowledge_card, rate_limit_config, rpm, tpm, retry, 429, provider, budget, backoff, api-limits, token-bucket, sliding-window]
tldr: "RPM/TPM/RPD ceilings per provider tier; honour Retry-After on 429 with exponential backoff; budget_usd + alert_threshold: 0.8 prevents billing surprises."
when_to_use: "When designing LLM API integrations, configuring rate_limit_config artifacts, or implementing retry/backoff strategies against provider 429 responses"
keywords: [rate limit, rpm, tpm, rpd, budget, tier, retry, 429, backoff, anthropic, openai, litellm, token bucket, sliding window, concurrent, alert threshold]
density_score: 1.0
---
# API Rate Limiting and Retry Patterns

## Core Concept

Rate limits are provider-enforced ceilings on API consumption: **RPM** (requests per minute), **TPM** (tokens per minute), **RPD** (requests per day), **concurrent** (parallel in-flight). Two algorithms enforce them independently: **token bucket** (TPM — continuous refill, burst to bucket cap) and **sliding window** (RPM — rolling 60s count). Both can bind simultaneously — 10 RPM ≠ 10 concurrent; each constrains through a different axis.

`rate_limit_config` **declares** these ceilings as a static artifact. Enforcement logic belongs in `runtime_rule`. Spend caps live in `budget_usd`. Keeping these three concerns in separate artifacts prevents config changes from breaking retry logic.

## Provider Limits by Tier

| Provider | Tier | RPM | TPM | RPD | Concurrent | Retry-After |
|----------|------|----:|----:|----:|----------:|------------|
| Anthropic | Free | 5 | 20,000 | 50 | 5 | 60 s |
| Anthropic | Build | 50 | 80,000 | 1,000 | 10 | 60 s |
| Anthropic | Scale | 4,000 | 400,000 | 100,000 | 50 | 60 s |
| OpenAI | Free | 3 | 40,000 | — | 3 | header |
| OpenAI | Tier 1 | 500 | 200,000 | — | 20 | header |
| OpenAI | Tier 2 | 5,000 | 2,000,000 | — | 50 | header |
| OpenAI | Tier 5 | 10,000 | 10,000,000 | — | 100 | header |
| LiteLLM | Proxy | configurable | configurable | configurable | configurable | passthrough |

Unlock gates: Anthropic Build after $5 spend; OpenAI Tier 1 after $5, Tier 2 after $50, Tier 5 after $1,000. Anthropic enforces RPD hard; OpenAI Tier 1+ does not.

## Retry Patterns on 429

**Priority order**: (1) read `Retry-After` response header, (2) exponential backoff with jitter, (3) fixed wait as last resort.

| Strategy | Formula | Base | Cap | Provider |
|----------|---------|-----:|----:|----------|
| Header-first | wait = `Retry-After` value | — | — | Anthropic (always 60 s) |
| Exponential + jitter | `min(base × 2ⁿ, cap) + rand(0, base)` | 2 s | 64 s | OpenAI, no header |
| Fixed | constant | 5 s | — | Low-volume, simple clients |

Jitter prevents thundering herd when multiple callers hit the same rate window simultaneously. Max retries: 3–5. After max attempts, surface the error — never loop indefinitely on 429.

**TPM 429 vs RPM 429**: TPM exhaustion clears as tokens refill (~1 s); RPM exhaustion requires waiting out the 60 s window. Distinguish by checking `error.type` in the provider response body.

## Budget Controls

```yaml
budget_usd: 200.0
alert_threshold: 0.8    # alert at $160 — 20% reaction window before hard stop
overage_policy: block   # requests blocked at $200; reset at billing cycle start
```

`alert_threshold: 1.0` fires at 100% — no reaction window. `0.8` gives time to throttle parallel agents before the hard stop hits. One runaway parallel agent on Anthropic Scale tier can exhaust $200 in under 10 minutes without a budget cap.

## When to Use / When NOT

**Use `rate_limit_config`** for: declaring provider quotas for a specific tier, communicating RPM/TPM to downstream callers, establishing cost guardrails.

**Route elsewhere**: retry logic and backoff strategies → `runtime_rule`; API keys and endpoints → `env_config`; execution timeouts and circuit breakers → `guardrail`.

## Anti-Patterns

| Anti-Pattern | Failure Mode |
|-------------|-------------|
| `rpm: 9999999` or `"unlimited"` | Runtime enforces wrong ceiling → unexpected 429 floods in production |
| No `budget_usd` | Runaway parallel agents exhaust monthly budget before anyone notices |
| `alert_threshold: 1.0` | Alert fires at 100% — invoice arrives before anyone acts |
| No `retry_after` | Fixed 1 s retry creates 429 storms; amplifies backoff for all callers |
| Retry logic inside rate_limit_config | Config change re-requires backoff testing; violates single-responsibility |
| One config for all providers | Each provider has independent limit pools — shared config applies wrong ceilings |
| Per-model overrides absent | GPT-4o and GPT-3.5 have different RPM pools; shared config mis-throttles cheaper model |

## CEX Integration

```yaml
kind: rate_limit_config   # declares limits
pillar: P09
id: p09_rl_{provider}_{tier}
```

**Consumed by**: `runtime_rule` (reads `retry_after` to size backoff windows), `client` (enforces RPM/TPM via request queue), `guardrail` (cost circuit breaker uses `budget_usd`), `agent` (parallel task throttling uses `concurrent`).

**Built by**: `rate-limit-config-builder` via N03 nucleus (8F pipeline, F1→F8).

**Dependency order**: `rate_limit_config` (layer 0, no deps) → `runtime_rule` → `client` → `agent`.