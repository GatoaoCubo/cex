---
kind: examples
id: bld_examples_prompt_cache
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of prompt_cache artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.1
title: "Examples Prompt Cache"
version: "1.0.0"
author: n03_builder
tags: [prompt_cache, builder, examples]
tldr: "Golden and anti-examples for prompt cache construction, demonstrating ideal structure and common pitfalls."
domain: "prompt cache construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: prompt-cache-builder
## Golden Example
INPUT: "Create prompt cache config for RAG agent with shared system prompts"
OUTPUT:
```yaml
---
id: p10_pc_rag_agent_shared
kind: prompt_cache
pillar: P10
title: "RAG Agent Shared Prompt Cache"
version: "1.0.0"
created: "2026-04-07"
updated: "2026-04-07"
author: "prompt-cache-builder"
ttl_seconds: 3600
eviction_strategy: lru
max_entries: 5000
cache_key_method: hash_prefix
invalidation_trigger: content_change
storage_backend: redis
domain: rag_pipeline
quality: null
tags: [prompt_cache, rag, shared, prefix-caching]
tldr: "RAG shared cache: prefix hashing, 1h TTL, LRU eviction, Redis backend for multi-agent reuse"
---
# Prefix caching: system_prompt + few-shot cached (stable), RAG context varies.
# Expected hit rate: ~60% (shared system prefix across agents).
# Invalidation: content_change triggers flush when KB artifacts update.
```
WHY THIS IS GOLDEN:
1. quality: null
2. All required fields present with valid enum values
3. cache_key_method=hash_prefix matches use case (shared system prompts)
4. storage_backend=redis for multi-agent sharing
5. invalidation_trigger=content_change (accurate for RAG)

## Anti-Example
BAD OUTPUT:
```yaml
id: cache_config
ttl_seconds: 999999
eviction_strategy: random
cache_key_method: whatever
quality: 9.5
```
FAILURES:
1. id: no p10_pc_ prefix
2. ttl: unreasonably high (11.5 days)
3. eviction: "random" not valid enum
4. cache_key_method: "whatever" not valid enum
5. quality: not null

## Properties

| Property | Value |
|----------|-------|
| Kind | `examples` |
| Pillar | P07 |
| Domain | prompt cache construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
