---
kind: architecture
id: bld_architecture_prompt_cache
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of prompt_cache — inventory, dependencies, architectural position
quality: 9.0
title: "Architecture Prompt Cache"
version: "1.0.0"
author: n03_builder
tags: [prompt_cache, builder, examples]
tldr: "Golden and anti-examples for prompt cache construction, demonstrating ideal structure and common pitfalls."
domain: "prompt cache construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - prompt-cache-builder
  - p03_sp_prompt_cache_builder
  - bld_output_template_prompt_cache
  - p01_kc_prompt_cache
  - bld_examples_prompt_cache
  - bld_collaboration_prompt_cache
  - bld_schema_prompt_cache
  - bld_knowledge_card_prompt_cache
  - p11_qg_prompt_cache
  - bld_instruction_prompt_cache
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| ttl_seconds | Cache entry lifetime | author | required |
| eviction_strategy | Which entries removed first | author | required |
| max_entries | Cache capacity limit | author | required |
| cache_key_method | How keys are computed | author | required |
| invalidation_trigger | What forces eviction | author | required |
| storage_backend | Where cache persists | author | required |
## Dependency Graph
```
system_prompt, prompt_template --> [prompt_cache] --> runtime_state, agent_card
                                        |
                                  model_provider, env_config, token_budget
```
| From | To | Type | Data |
|------|----|------|------|
| system_prompt | prompt_cache | data_flow | stable prefix for caching |
| prompt_template | prompt_cache | data_flow | template structure for key hashing |
| prompt_cache | runtime_state | data_flow | cache hit/miss metrics |
| prompt_cache | agent_card | data_flow | caching config for deployment |
## Boundary Table
| prompt_cache IS | prompt_cache IS NOT |
|-----------------|---------------------|
| Cache config for prompt/completion pairs | Session context (session_state) |
| TTL/eviction/invalidation rules | Conversation history (memory_summary) |
| Storage backend selection | Runtime variables (runtime_state) |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Timing | ttl_seconds, invalidation_trigger | When cache expires |
| Capacity | max_entries, eviction_strategy | How cache manages space |
| Identity | cache_key_method | How entries are matched |
| Storage | storage_backend | Where cache persists |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[prompt-cache-builder]] | downstream | 0.53 |
| [[p03_sp_prompt_cache_builder]] | upstream | 0.48 |
| [[bld_output_template_prompt_cache]] | upstream | 0.46 |
| [[p01_kc_prompt_cache]] | downstream | 0.45 |
| [[bld_examples_prompt_cache]] | upstream | 0.42 |
| [[bld_collaboration_prompt_cache]] | downstream | 0.41 |
| [[bld_schema_prompt_cache]] | upstream | 0.41 |
| [[bld_knowledge_card_prompt_cache]] | upstream | 0.34 |
| [[p11_qg_prompt_cache]] | downstream | 0.33 |
| [[bld_instruction_prompt_cache]] | upstream | 0.31 |
