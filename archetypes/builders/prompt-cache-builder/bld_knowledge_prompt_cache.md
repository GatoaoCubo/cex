---
kind: knowledge_card
id: bld_knowledge_card_prompt_cache
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for prompt_cache production
sources: kc_prompt_cache.md, provider documentation, caching best forctices
quality: 9.0
title: "Knowledge Card Prompt Cache"
version: "1.0.0"
author: n03_builder
tags: [prompt_cache, builder, examples]
tldr: "Golden and anti-examples for prompt cache construction, demonstrating ideal structure and common pitfalls."
domain: "prompt cache construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p01_kc_prompt_cache
  - prompt-cache-builder
  - p10_lr_prompt_cache_builder
  - bld_collaboration_prompt_cache
  - p03_sp_prompt_cache_builder
  - bld_output_template_prompt_cache
  - ex_knowledge_card_prompt_caching
  - p01_kc_caching
  - bld_examples_prompt_cache
  - bld_config_prompt_cache
---

# Domain Knowledge: prompt_cache
## Executive Summary
Prompt caches store LLM prompt/completion pairs to reduce latency and cost for repeated or similar queries. They configure TTL, eviction strategy, cache key computation, invalidation triggers, and storage backends. Critical for high-volume agents, shared-context systems, and cost-sensitive deployments.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P10 (Memory) |
| LLM Function | GOVERN |
| Max bytes | 2048 |
| Naming | p10_pc_{name}.yaml |
| Core | false |
| Eviction strategies | lru, lfu, fifo |
| Key methods | hash_full, hash_prefix, semantic |
| Storage backends | memory, redis, sqlite |
## Provider Caching Comparison
| Provider | Type | Min Tokens | Write Cost | Read Discount | TTL |
|----------|------|-----------|------------|---------------|-----|
| Anthropic | Explicit | 1024 | 1.25x | 90% | 5 min |
| OpenAI | Automatic | 1024 | 1.0x | 50% | 5-60 min |
| Google | Explicit | 32768 | 1.0x | 75% | configurable |
| vLLM | KV-cache | — | — | — | session |
| SGLang | RadixAttention | — | — | — | auto |
## Patterns
- **Prefix caching**: System prompts + static context reused across requests
- **Semantic dedup**: Similar queries share cache (threshold >= 0.95)
- **Tiered TTL**: Different TTLs per prompt type (system=3600, query=300)
- **Shared cache**: Multi-agent with Redis backend, namespace per agent
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Cache everything | Unique queries pollute cache |
| No invalidation | Stale completions after knowledge update |
| TTL too long | Outdated completions |
| No namespace | Agent cross-pollution |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_prompt_cache]] | sibling | 0.65 |
| [[prompt-cache-builder]] | downstream | 0.55 |
| [[p10_lr_prompt_cache_builder]] | downstream | 0.49 |
| [[bld_collaboration_prompt_cache]] | downstream | 0.46 |
| [[p03_sp_prompt_cache_builder]] | downstream | 0.43 |
| [[bld_output_template_prompt_cache]] | downstream | 0.42 |
| [[ex_knowledge_card_prompt_caching]] | sibling | 0.39 |
| [[p01_kc_caching]] | sibling | 0.38 |
| [[bld_examples_prompt_cache]] | downstream | 0.37 |
| [[bld_config_prompt_cache]] | downstream | 0.35 |
