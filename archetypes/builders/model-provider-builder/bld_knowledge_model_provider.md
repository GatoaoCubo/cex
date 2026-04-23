---
kind: knowledge_card
id: bld_knowledge_card_model_provider
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for model_provider production — atomic searchable facts
sources: model-provider-builder SCHEMA + MANIFEST, provider API docs, CEX router
quality: 9.1
title: "Knowledge Card Model Provider"
version: "1.0.0"
author: n03_builder
tags: [model_provider, builder, examples]
tldr: "Golden and anti-examples for model provider construction, demonstrating ideal structure and common pitfalls."
domain: "model provider construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_memory_model_provider
  - p03_sp_model_provider_builder
  - model-provider-builder
  - p03_ins_model_provider
  - bld_examples_model_provider
  - bld_collaboration_model_provider
  - bld_config_model_provider
  - p01_kc_model_provider
  - p11_qg_model_provider
  - bld_output_template_model_provider
---

# Domain Knowledge: model_provider
## Executive Summary
Model provider configs are connection and routing artifacts for LLM APIs — they encode provider authentication, tiered model selection (fast/balanced/quality), rate limits (RPM/TPM), fallback chains, retry logic, and health tracking into a structured config. The model tier assignment determines cost-quality tradeoff for every LLM call. The fallback chain determines system resilience during provider outages. These configs differ from model_card (which documents LLM specs), embedder_provider (which configures embedding models), and agent (which defines behavior and identity).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P02 (model layer) |
| Kind | `model_provider` (exact literal) |
| ID pattern | `p02_mp_{provider}` |
| Required frontmatter | 22+ fields |
| Quality gates | 10 HARD + 12 SOFT |
| Max body | 4096 bytes |
| Density minimum | >= 0.85 |
| Quality field | always `null` |
| Domain field | always `llm_routing` |
| Model tiers | 3: fast, balanced, quality |
| Rate limits | RPM (requests/min), TPM (tokens/min) |
| Provider enum | anthropic, openai, google, ollama, groq, mistral, together, fireworks, deepseek, other |
## Patterns
| Pattern | Application |
|---------|-------------|
| Tiered model selection | fast (cheap/fast), balanced (default), quality (expensive/capable) |
| Cross-provider fallback | Primary provider unavailable -> switch to alternative provider |
| Versioned model IDs | Use full version strings to avoid silent alias changes |
| Environment variable auth | api_key_env points to env var name, never the key itself |
| Exponential backoff | base=1s, max=60s, jitter=random, prevents retry storms |
| Circuit breaker | open (no calls) -> half-open (test call) -> closed (normal) |
| Cost-aware routing | Route simple tasks to fast tier, complex to quality tier |
| Rate limit headroom | Set operational limit to 80% of provider maximum |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Unversioned model alias (`gpt-4`) | Resolves to different models over time; breaks assumptions |
| Rate limit from wrong tier | Free tier limits on pro account = waste; pro limits on free = 429 |
| Single provider, no fallback | One outage takes down entire system |
| Retry without backoff | Amplifies rate limit pressure, extends cooldown period |
| Hardcoded API key | Security violation; breaks rotation, CI/CD, and team sharing |
| One model for all tasks | Quality model on simple tasks wastes 10x budget |
| Health check every 5s | Wastes rate limit budget on health pings instead of real work |
| Ignoring TPM alongside RPM | 10 requests at 100K tokens each can exhaust TPM while RPM is fine |
## Application
1. Set `id: p02_mp_{provider}` — must equal filename stem
2. Populate all required frontmatter fields; set `quality: null`
3. Set `models` with three tiers using current, versioned model IDs
4. Set `rate_limit_rpm` and `rate_limit_tpm` for the user's actual account tier
5. Set `fallback` to a different provider for resilience
6. Write `## Provider Matrix` with Value + Source URL per row
7. Write `## Model Tiers` with pricing and use case per tier
8. Validate: body <= 4096 bytes, all configs sourced, 10 HARD + 12 SOFT gates
## References
- Anthropic API: https://docs.anthropic.com/en/api
- OpenAI API: https://platform.openai.com/docs
- Google Gemini: https://ai.google.dev/gemini-api/docs
- CEX router: cex_router.py
- CEX crew runner: cex_crew_runner.py

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_memory_model_provider]] | downstream | 0.63 |
| [[p03_sp_model_provider_builder]] | downstream | 0.60 |
| [[model-provider-builder]] | downstream | 0.59 |
| [[p03_ins_model_provider]] | downstream | 0.59 |
| [[bld_examples_model_provider]] | downstream | 0.56 |
| [[bld_collaboration_model_provider]] | downstream | 0.55 |
| [[bld_config_model_provider]] | downstream | 0.53 |
| [[p01_kc_model_provider]] | sibling | 0.51 |
| [[p11_qg_model_provider]] | downstream | 0.45 |
| [[bld_output_template_model_provider]] | downstream | 0.44 |
