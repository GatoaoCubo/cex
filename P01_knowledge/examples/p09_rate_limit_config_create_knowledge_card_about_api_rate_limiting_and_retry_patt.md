---
id: p01_kc_api_rate_limiting_retry_patterns
kind: knowledge_card
type: infrastructure
pillar: P01
title: "API Rate Limiting and Retry Patterns"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "builder_agent"
domain: rate_limit_config
quality: 9.1
tags: [knowledge_card, rate-limiting, retry-patterns, api, rpm, tpm, 429, backoff, budget, llm]
tldr: "RPM/TPM ceilings, token-bucket enforcement, exponential backoff with jitter, and alert-gated budget caps prevent 429 floods and runaway spend in LLM API integrations."
when_to_use: "When building any LLM API integration that must respect provider rate limits, implement fault-tolerant 429 recovery, and enforce monthly budget guardrails."
keywords: [rate limit, rpm, tpm, rpd, concurrent, 429, retry, exponential backoff, jitter, budget cap, token bucket, retry_after, provider tier, alert threshold]
density_score: 0.92
---
# API Rate Limiting and Retry Patterns

## Core Concept
LLM API providers enforce three orthogonal quota axes: **RPM** (requests per minute), **TPM** (tokens per minute), and **RPD** (requests per day). A request can fail on any axis independently — batch jobs saturate TPM while staying within RPM; chatbots hit RPM while far below TPM. **Concurrent** slots cap parallel in-flight requests regardless of per-minute rate.

Providers implement limits via token-bucket or sliding-window algorithms. A token bucket refills at a fixed rate; burst is allowed up to bucket size. When any limit is exceeded the provider returns HTTP 429 with a `Retry-After` header (Anthropic: 60s; OpenAI: varies by tier). Hammering with immediate retries burns the same quota window and amplifies delays exponentially.

## Provider Reference
| Provider | Tier | RPM | TPM | RPD | Concurrent |
|----------|------|-----|-----|-----|------------|
| Anthropic | Free | 5 | 20,000 | 50 | — |
| Anthropic | Build | 50 | 80,000 | 1,000 | 10 |
| Anthropic | Scale | 4,000 | 400,000 | 100,000 | 50 |
| OpenAI | Free | 3 | 40,000 | — | — |
| OpenAI | Tier 1 | 500 | 200,000 | — | — |
| OpenAI | Tier 2 | 5,000 | 2,000,000 | — | — |
| LiteLLM | Proxy | configurable | configurable | configurable | configurable |

## Retry Patterns
| Pattern | When to Use | Rule |
|---------|-------------|------|
| **Respect Retry-After** | Always on 429 | Sleep exactly the header value; never shorter |
| **Exponential backoff** | Persistent 429s | `wait = base × 2^attempt`, cap at 60s |
| **Full jitter** | Concurrent callers | Add `random(0, wait)` — desynchronizes retry waves |
| **Circuit breaker** | Sustained limit hits | Open after N failures; half-open after cooldown |
| **Pre-throttle queue** | High-throughput batch | Rate-limit outbound to 90% of RPM ceiling proactively |

Backoff and retry count belong in `runtime_rule` — not here. `rate_limit_config` declares the quota seed values (`retry_after`, `rpm`, `tpm`) that `runtime_rule` consumes.

## Budget Management
```yaml
budget_usd: 200.0          # hard monthly stop — requests blocked at 100%
alert_threshold: 0.8       # notify at 80% ($160) — reaction time before hard stop
overage_policy: block      # never silently queue; fail fast and surface the cap
```

Alert at 80%, not 100%. By the time a 100% alert fires, a runaway agent has already exhausted the budget. An 80% alert gives time to investigate before the hard stop.

## When to Use / When NOT
- **Use**: Production LLM integrations; multi-agent parallel workers; cost-controlled batch pipelines; any system with > 1 concurrent caller
- **Don't use**: Single-request scripts under manual oversight; internal load tests with a dedicated key and no cost concern

## Anti-Patterns
| Anti-Pattern | Failure Mode |
|-------------|-------------|
| Fictional RPM/TPM values | False capacity signal → unexpected 429 floods in production |
| Immediate retry on 429 | Burns retries from same quota window; amplifies delay |
| `alert_threshold: 1.0` | Fires when already at limit; no reaction window |
| No `budget_usd` cap | One runaway agent exhausts monthly spend |
| Retry logic inside `rate_limit_config` | Conflates quota declaration with enforcement — `runtime_rule` owns backoff |
| One config for all providers | Each provider maintains independent quota pools; always separate |

## CEX Integration
- `rate_limit_config` (P09) — declares the numeric limits; this KC explains the theory
- `runtime_rule` (P09) — owns retry count, backoff multiplier, circuit-breaker thresholds
- `guardrail` (P11) — references `budget_usd` for cost circuit breakers
- `agent` (P02) — reads `rate_limit_config` to enforce quotas during parallel task execution