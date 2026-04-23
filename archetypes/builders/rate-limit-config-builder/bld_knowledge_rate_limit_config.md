---
kind: knowledge_card
id: bld_knowledge_card_rate_limit_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for rate_limit_config production — LLM API rate limiting
sources: Anthropic docs, OpenAI docs, LiteLLM docs, token bucket algorithm
quality: 9.1
title: "Knowledge Card Rate Limit Config"
version: "1.0.0"
author: n03_builder
tags: [rate_limit_config, builder, examples]
tldr: "Golden and anti-examples for rate limit config construction, demonstrating ideal structure and common pitfalls."
domain: "rate limit config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_examples_rate_limit_config
  - bld_collaboration_rate_limit_config
  - rate-limit-config-builder
  - p03_sp_rate_limit_config_builder
  - p01_kc_rate_limit_config
  - bld_tools_rate_limit_config
  - bld_instruction_rate_limit_config
  - p01_kc_api_rate_limiting_retry_patterns
  - bld_config_rate_limit_config
  - bld_output_template_rate_limit_config
---

# Domain Knowledge: rate_limit_config

This ISO encodes a rate limit policy -- throttle bounds, quota windows, and backoff behavior.
## Executive Summary
Rate limit configs declare the quota boundaries for LLM API providers: how many requests per minute (RPM), tokens per minute (TPM), and the monthly budget cap. They are static configuration artifacts — they declare limits, not enforcement logic. Enforcement belongs in the runtime layer (runtime_rule). Rate limits are provider-tier-specific and change as providers update their pricing.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P09 (Config) |
| llm_function | CONSTRAIN (limits what callers can do) |
| Layer | runtime |
| Machine format | yaml |
| Core | true |
| Max bytes | 1024 |
| ID prefix | p09_rl |
## Provider Reference (authoritative limits)
### Anthropic
| Tier | RPM | TPM | RPD | Notes |
|------|-----|-----|-----|-------|
| Free | 5 | 20,000 | 50 | claude.ai accounts |
| Build | 50 | 80,000 | 1,000 | API key after $5 spend |
| Scale | 4,000 | 400,000 | 100,000 | Custom agreement |
### OpenAI
| Tier | RPM | TPM | Notes |
|------|-----|-----|-------|
| Free | 3 | 40,000 | Trial |
| Tier 1 | 500 | 200,000 | $5 spent |
| Tier 2 | 5,000 | 2,000,000 | $50 spent |
| Tier 5 | 10,000 | 10,000,000 | $1,000 spent |
### LiteLLM
- Proxy aggregating multiple providers with unified rate limiting
- Supports per-model, per-user, per-team limits
- Rate limits configured via proxy config.yaml or database
- Passes through provider 429s with optional retry layer
## Patterns
- **Token bucket**: each RPM/TPM slot refills at a fixed rate; burst allowed up to the bucket size
- **Sliding window**: limits tracked over rolling 60s window; smoother than fixed windows
- **Per-model overrides**: some providers enforce separate limits per model (e.g. GPT-4 vs GPT-3.5)
- **Budget caps**: hard USD stop vs soft alert — alert_threshold triggers notification, budget_usd stops requests
- **Concurrent limits**: separate from RPM — caps parallel in-flight requests regardless of per-minute rate
| Pattern | Example | When to use |
|---------|---------|-------------|
| Tier-based | anthropic build: 50 RPM | Standard provider integration |
| Per-model | gpt-4o: 500 RPM, gpt-3.5: 3500 RPM | Mixed-model workflows |
| Budget-gated | budget_usd: 200, alert: 0.8 | Cost-controlled production |
| Proxy unified | litellm aggregating 3 providers | Multi-provider load balancing |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No budget_usd cap | Runaway costs with no ceiling |
| Ignoring 429 retry-after header | Repeated hammering amplifies backoff |
| No alert_threshold | Budget exceeded before anyone notices |
| Confusing RPM with concurrent | 10 RPM != 10 concurrent; both can bind independently |
| Fictional limit values | Config drifts from reality; callers get unexpected 429s |
| Hardcoding limits in code | Config change requires redeploy; use declarative artifact |
## Application
1. Identify provider and tier from API dashboard
2. Record RPM, TPM, RPD from provider documentation
3. Set budget_usd from monthly spend target
4. Set alert_threshold at 0.8 (80% of limit triggers alert)
5. Document retry_after from provider 429 response headers (typically 1–60s)
6. Add model_overrides for any model with different limits than the tier default
## References
- Anthropic: docs.anthropic.com/en/api/rate-limits
- OpenAI: platform.openai.com/docs/guides/rate-limits
- LiteLLM: docs.litellm.ai/docs/proxy/rate_limit

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_rate_limit_config]] | downstream | 0.60 |
| [[bld_collaboration_rate_limit_config]] | downstream | 0.58 |
| [[rate-limit-config-builder]] | downstream | 0.57 |
| [[p03_sp_rate_limit_config_builder]] | downstream | 0.54 |
| [[p01_kc_rate_limit_config]] | sibling | 0.54 |
| [[bld_tools_rate_limit_config]] | downstream | 0.53 |
| [[bld_instruction_rate_limit_config]] | downstream | 0.52 |
| [[p01_kc_api_rate_limiting_retry_patterns]] | sibling | 0.51 |
| [[bld_config_rate_limit_config]] | downstream | 0.49 |
| [[bld_output_template_rate_limit_config]] | downstream | 0.49 |
