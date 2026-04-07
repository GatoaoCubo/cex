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
