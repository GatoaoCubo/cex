---
id: ex_knowledge_card_prompt_caching
kind: knowledge_card
pillar: P01
title: "Prompt Caching Strategies"
tags: [cache, performance, cost, optimization, llm]
tldr: "Cache static prompt components to reduce LLM costs by 60-90%. Cache system prompts (BECOME) and KCs (INJECT), never cache user prompts. Invalidate on content change."
references:
  - tpl_knowledge_card
  - ex_knowledge_card_rag_fundamentals
quality: 9.0
related:
  - bld_collaboration_prompt_cache
  - prompt-cache-builder
  - bld_knowledge_card_prompt_cache
  - p01_kc_prompt_cache
  - spec_token_budget_optimization
  - p01_kc_caching
  - p03_sp_prompt_cache_builder
  - bld_examples_knowledge_card
  - bld_tools_prompt_cache
  - p10_lr_prompt_cache_builder
---

# Prompt Caching Strategies

## Core Principle
LLM prompts have layers with different change frequencies. Cache the stable layers, recompute the dynamic ones.

## Cache Tiers

| Layer | 8F Function | Change Frequency | Cache? | Savings |
|-------|-------------|-----------------|--------|---------|
| System prompt | F2 BECOME | Monthly | **Yes** (long TTL) | ~20% tokens |
| Builder ISOs | F1-F3 | Weekly | **Yes** (medium TTL) | ~30% tokens |
| Knowledge cards | F3 INJECT | Weekly | **Yes** (per-KC hash) | ~25% tokens |
| User intent | F6 PRODUCE | Every request | **Never** | 0% |
| Retry feedback | F7 GOVERN | Per-retry | **Never** | 0% |

## Implementation Pattern
```python
# Hash-based cache key
import hashlib
def cache_key(system_prompt: str, isos: str) -> str:
    content = system_prompt + isos
    return hashlib.sha256(content.encode()).hexdigest()[:16]

# Check cache before LLM call
cached = cache.get(cache_key(sp, isos))
if cached:
    prompt = cached + user_intent  # Append dynamic part
else:
    prompt = build_full_prompt(sp, isos, user_intent)
    cache.set(cache_key(sp, isos), sp + isos, ttl=3600)
```

## Provider-Specific Caching

| Provider | Feature | How to Use |
|----------|---------|------------|
| Anthropic | Prompt caching (beta) | Set `cache_control` on system message blocks |
| OpenAI | Automatic prefix caching | Same prefix across calls = auto-cached |
| Local | Manual | Redis/in-memory with hash key |

## Invalidation Rules
- **On builder ISO change**: Invalidate all caches for that kind
- **On KC update**: Invalidate caches containing that KC's hash
- **On model change**: Invalidate everything (token counts differ)
- **TTL safety net**: Max 24h even if no explicit invalidation

## Cost Impact
| Scenario | Without Cache | With Cache | Savings |
|----------|---------------|------------|---------|
| Single build | ~8K tokens | ~8K tokens | 0% (cold start) |
| 10 builds same kind | ~80K tokens | ~25K tokens | 69% |
| 100 builds mixed | ~800K tokens | ~200K tokens | 75% |

## Quality Gate
- [ ] Static layers identified and cached
- [ ] Dynamic layers (user intent) NEVER cached
- [ ] Invalidation rules cover ISO changes
- [ ] TTL safety net prevents stale cache

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_prompt_cache]] | downstream | 0.43 |
| [[prompt-cache-builder]] | downstream | 0.43 |
| [[bld_knowledge_card_prompt_cache]] | sibling | 0.42 |
| [[p01_kc_prompt_cache]] | sibling | 0.40 |
| [[spec_token_budget_optimization]] | downstream | 0.40 |
| [[p01_kc_caching]] | sibling | 0.37 |
| [[p03_sp_prompt_cache_builder]] | downstream | 0.36 |
| [[bld_examples_knowledge_card]] | downstream | 0.34 |
| [[bld_tools_prompt_cache]] | downstream | 0.34 |
| [[p10_lr_prompt_cache_builder]] | downstream | 0.34 |
