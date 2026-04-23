---
id: p10_lr_prompt_cache_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n04_knowledge
observation: "Prompt caches that fail most often cache everything (unique queries pollute, waste memory), have no invalidation (stale completions after knowledge update), or use TTL too long (outdated answers for evolving contexts)."
pattern: "Filter caching to prompts with >2 expected repeats. Tie invalidation to knowledge artifact versions. Default TTL 300s; justify any longer TTL. Namespace keys per agent. quality:null always."
evidence: "Initial pattern from KC analysis — no production log yet."
confidence: 0.70
outcome: PENDING
domain: prompt_cache
tags: [prompt-cache, ttl, eviction, invalidation, caching, cost]
tldr: "Don't cache everything. Tie invalidation to content versions. TTL 300s default. Namespace keys. quality:null."
impact_score: 7.0
decay_rate: 0.05
agent_group: n04_knowledge
keywords: [prompt_cache, ttl, eviction, invalidation, cache_key, storage_backend]
memory_scope: project
observation_types: [user, feedback, project, reference]
llm_function: INJECT
quality: 8.8
title: Memory ISO - prompt_cache
density_score: 0.98
related:
  - bld_knowledge_card_prompt_cache
  - p01_kc_prompt_cache
  - prompt-cache-builder
  - p03_sp_prompt_cache_builder
  - ex_knowledge_card_prompt_caching
  - bld_output_template_prompt_cache
  - bld_collaboration_prompt_cache
  - p11_qg_prompt_cache
  - bld_examples_knowledge_card
  - p01_kc_caching
---
## Summary
Prompt caches reduce LLM latency and cost by reusing prompt/completion pairs. Primary failures are caching everything (pollution), no invalidation (stale), and excessive TTL (outdated).
## Pattern
1. **Filter candidates** — only cache prompts with >2 expected repeats
2. **Invalidation** — tie to knowledge artifact versions, not just TTL
3. **TTL default 300s** — match provider defaults (Anthropic 5min)
4. **Namespace isolation** — key per agent_id + domain to prevent pollution
## Anti-Pattern
- Cache everything: unique queries pollute, waste memory
- No invalidation: stale completions after knowledge update
- TTL too long: 24h TTL for evolving context
- No namespace: Agent A's cache pollutes Agent B's results

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_prompt_cache]] | upstream | 0.58 |
| [[p01_kc_prompt_cache]] | related | 0.55 |
| [[prompt-cache-builder]] | related | 0.42 |
| [[p03_sp_prompt_cache_builder]] | upstream | 0.38 |
| [[ex_knowledge_card_prompt_caching]] | upstream | 0.37 |
| [[bld_output_template_prompt_cache]] | upstream | 0.32 |
| [[bld_collaboration_prompt_cache]] | downstream | 0.31 |
| [[p11_qg_prompt_cache]] | downstream | 0.29 |
| [[bld_examples_knowledge_card]] | upstream | 0.26 |
| [[p01_kc_caching]] | upstream | 0.26 |
