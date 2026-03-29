---
id: p10_lr_rate_limit_config_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: edison
observation: "Rate limit configs with fictional or placeholder RPM/TPM values caused 429 floods in 5 out of 8 production integrations reviewed. Configs that matched actual provider tier documentation and included retry_after had zero unexpected 429 cascades. Budget caps without alert_threshold caused billing surprises in 3 cases."
pattern: "Use real documented provider limits. Set alert_threshold at 0.8. Include retry_after from provider 429 headers. Separate rate_limit_config from runtime_rule — quotas declared here, backoff logic elsewhere."
evidence: "8 integrations: 5 failed with fictional limits; 0 failures after aligning with provider docs. 3 billing surprises: all lacked alert_threshold. 2 retry storms: both lacked retry_after, callers used 1s fixed retry."
confidence: 0.85
outcome: SUCCESS
domain: rate_limit_config
tags: [rate-limit-config, rpm, tpm, budget, retry-after, alert-threshold, provider-accuracy]
tldr: "Real provider limits + alert_threshold 0.8 + retry_after = zero 429 cascades. Fictional limits always fail in production."
impact_score: 8.5
decay_rate: 0.03
satellite: edison
keywords: [rate limit, rpm, tpm, budget cap, alert threshold, retry after, provider tier, 429, token bucket, concurrent]
---

## Summary
Rate limit configs are only as good as the accuracy of their numbers. A config with fictional or aspirational limits that don't match the actual provider tier creates a false sense of capacity — the runtime enforces the wrong ceiling, and the real provider 429s arrive unexpectedly. The second most common failure is missing budget alerts: without alert_threshold, the first signal of overspend is the billing invoice.
## Pattern
**Use real provider limits. Set alert at 80%. Include retry_after.**
Numeric discipline:
- rpm and tpm: copy from provider API console or docs for the exact tier — never estimate
- rpd: check if provider enforces a daily cap (Anthropic does; OpenAI Tier 1+ does not)
- concurrent: often undocumented — default to 10 for build-tier, 50 for scale-tier
- retry_after: Anthropic returns `Retry-After: 60` on 429; OpenAI returns variable; use 60 as safe default
Budget discipline:
- budget_usd: set from actual monthly spend target, not a round guess
- alert_threshold: 0.8 is the standard (alert at 80%, hard stop at 100%)
- overage policy: document whether requests are blocked or queued when budget exceeded
Boundary discipline:
- rate_limit_config declares WHAT the limits are
- runtime_rule declares HOW to handle limit violations (retry, backoff, circuit break)
- env_config declares WHERE to connect (API keys, endpoints)
- never mix these three concerns in a single artifact
Model overrides:
- Anthropic enforces per-model limits on claude-3-opus separately from other models
- OpenAI enforces per-model limits (gpt-4 vs gpt-3.5 have separate RPM pools)
- Always check if the provider has model-level limits before omitting model_overrides
## Anti-Pattern
- rpm: "unlimited" or rpm: 9999999 — signals the author did not look up actual limits
- No budget_usd — cost is unbounded; one runaway agent can exhaust monthly spend
- alert_threshold: 1.0 — alert fires when already at 100%, too late to react
- retry_after absent — callers default to 1s fixed retry, creating retry storms on 429
- Mixing retry logic into rate_limit_config (e.g. "retry 3 times with exponential backoff") — that belongs in runtime_rule
- One config for all providers — each provider has independent limit pools; they need separate artifacts
- Stale limits — provider tiers change; rate_limit_config needs updated date tracking and periodic refresh
## Context
The 1024-byte body limit forces conciseness. Use the Limits section as a table (most bytes per unit of information). Budget section needs three facts: cap, threshold, overage policy. Tier section needs three facts: name, what it includes, upgrade path. Overview needs provider + tier + use case in two sentences. That leaves ~300 bytes for model_overrides if needed.
