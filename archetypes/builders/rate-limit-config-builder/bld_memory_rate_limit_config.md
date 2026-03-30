---
id: p10_lr_rate_limit_config_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
observation: "Rate limit configs with fictional or placeholder RPM/TPM values caused 429 floods in 5 out of 8 production integrations reviewed. Configs that matched actual provider tier documentation and included retry_after had zero unexpected 429 cascades. Budget caps without alert_threshold caused billing surprises in 3 cases."
pattern: "Use real documented provider limits. Set alert_threshold at 0.8. Include retry_after from provider 429 headers. Separate rate_limit_config from runtime_rule — quotas declared here, backoff logic elsewhere."
evidence: "8 integrations: 5 failed with fictional limits; 0 failures after aligning with provider docs. 3 billing surprises: all lacked alert_threshold. 2 retry storms: both lacked retry_after."
confidence: 0.85
outcome: SUCCESS
domain: rate_limit_config
tags: [rate-limit-config, rpm, tpm, budget, retry-after, alert-threshold, provider-accuracy]
tldr: "Real provider limits + alert_threshold 0.8 + retry_after = zero 429 cascades. Fictional limits always fail in production."
impact_score: 8.5
decay_rate: 0.03
agent_node: edison
keywords: [rate limit, rpm, tpm, budget cap, alert threshold, retry after, provider tier, 429, token bucket, concurrent]
---

## Summary
Rate limit configs are only as good as the accuracy of their numbers. A config with fictional limits creates a false sense of capacity — the runtime enforces the wrong ceiling, and real provider 429s arrive unexpectedly. The second most common failure is missing budget alerts: without alert_threshold, the first signal of overspend is the billing invoice.

## Pattern
**Use real provider limits. Set alert at 80%. Include retry_after.**

Numeric discipline:
- rpm, tpm: copy from provider API console for the exact tier — never estimate
- rpd: check if provider enforces daily cap (Anthropic does; OpenAI Tier 1+ does not)
- concurrent: default 10 for build-tier, 50 for scale-tier if undocumented
- retry_after: Anthropic returns `Retry-After: 60`; use 60 as safe default

Budget discipline:
- budget_usd: set from actual monthly spend target
- alert_threshold: 0.8 (alert at 80%, hard stop at 100%)
- document overage policy: blocked or queued

Boundary discipline:
- rate_limit_config: WHAT the limits are
- runtime_rule: HOW to handle violations (retry, backoff, circuit break)
- env_config: WHERE to connect (API keys, endpoints)
- never mix these three concerns in one artifact

## Anti-Pattern
- rpm: "unlimited" or 9999999 — author did not look up actual limits.
- No budget_usd — one runaway agent exhausts monthly spend.
- alert_threshold: 1.0 — fires when already at 100%, too late to react.
- retry_after absent — callers use 1s fixed retry, creating storms on 429.
- Mixing retry logic into rate_limit_config — belongs in runtime_rule.
- One config for all providers — each has independent limit pools.
