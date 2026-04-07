---
kind: knowledge_card
id: bld_knowledge_card_prompt_cache
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for prompt_cache production
sources: kc_prompt_cache.md, provider documentation, caching best practices
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
