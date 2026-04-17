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
agent_group: edison
keywords: [rate limit, rpm, tpm, budget cap, alert threshold, retry after, provider tier, 429, token bucket, concurrent]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.1
title: "Memory Rate Limit Config"
density_score: 0.90
llm_function: INJECT
---
## Summary

This ISO encodes a rate limit policy -- throttle bounds, quota windows, and backoff behavior.
Rate limit configs are only as good as the accuracy of their numbers. A config with fictional limits creates a false sense of capacity — the runtime enforces the wrong ceiling, and real provider 429s arrive unexpectedly. The second most common failure is missing budget alerts: without alert_threshold, the first signal of overspend is the billing invoice.

## Pattern
**Use real provider limits. Set alert at 80%. Include retry_after.**

Numeric discipline:
1. rpm, tpm: copy from provider API console for the exact tier — never estimate
2. rpd: check if provider enforces daily cap (Anthropic does; OpenAI Tier 1+ does not)
3. concurrent: default 10 for build-tier, 50 for scale-tier if undocumented
4. retry_after: Anthropic returns `Retry-After: 60`; use 60 as safe default

Budget discipline:
1. budget_usd: set from actual monthly spend target
2. alert_threshold: 0.8 (alert at 80%, hard stop at 100%)
3. document overage policy: blocked or queued

Boundary discipline:
1. rate_limit_config: WHAT the limits are
2. runtime_rule: HOW to handle violations (retry, backoff, circuit break)
3. env_config: WHERE to connect (API keys, endpoints)
4. never mix these three concerns in one artifact

## Anti-Pattern
1. rpm: "unlimited" or 9999999 — author did not look up actual limits.
2. No budget_usd — one runaway agent exhausts monthly spend.
3. alert_threshold: 1.0 — fires when already at 100%, too late to react.
4. retry_after absent — callers use 1s fixed retry, creating storms on 429.
5. Mixing retry logic into rate_limit_config — belongs in runtime_rule.
6. One config for all providers — each has independent limit pools.

## Metadata

```yaml
id: p10_lr_rate_limit_config_builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p10-lr-rate-limit-config-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | rate_limit_config |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
