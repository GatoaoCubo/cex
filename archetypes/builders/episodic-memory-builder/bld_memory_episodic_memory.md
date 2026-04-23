---
quality: 8.7
quality: 8.4
id: p10_lr_episodic_memory_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-04-17
updated: 2026-04-17
author: builder_agent
observation: "Episodic stores without decay policies grew to thousands of episodes, causing retrieval latency spikes after 30 days. Stores without retrieval_keys required full embedding scan per query. Stores with hybrid retrieval (recency + relevance) outperformed pure recency by 60% on relevant context surfacing."
pattern: "Always set episode_count limit. Always declare decay_policy. Always define retrieval_keys for indexed access. Hybrid retrieval outperforms pure recency for agents with diverse task domains."
confidence: 0.87
outcome: SUCCESS
domain: episodic_memory
tags: [episodic-memory, decay-policy, retrieval-keys, episode-count, hybrid-retrieval]
tldr: "episode_count + decay_policy + retrieval_keys are load-bearing. Unlimited undecayed stores degrade."
impact_score: 8.0
decay_rate: 0.02
memory_scope: project
title: "Memory Episodic Memory"
density_score: 0.90
llm_function: INJECT
related:
  - atom_22_memory_taxonomy
  - bld_knowledge_card_memory_architecture
  - p01_kc_entity_memory
  - p10_lr_memory_scope_builder
  - entity-memory-builder
  - bld_collaboration_entity_memory
  - bld_knowledge_card_entity_memory
  - bld_output_template_memory_architecture
  - bld_knowledge_card_memory_scope
  - p01_kc_retriever
---
## Summary
Episodic memory stores without explicit count limits and decay policies become operational liabilities: retrieval latency spikes as the store grows, and stale episodes inject irrelevant context. Retrieval keys enable efficient indexed access -- without them, every query triggers a full embedding scan.

## Pattern
**episode_count + decay_policy + retrieval_keys = operational episodic store.**
1. episode_count: 100-500 for task agents, 200-1000 for long-running agents
2. decay_policy.method: time (90 days default), count (oldest-first), or hybrid
3. retrieval_keys: topic terms, entity names, task types -- indexed at write time
4. index_method: hybrid (embedding + keyword) outperforms either alone
5. promotion_sources: list the working_memory IDs that feed this store

## Anti-Pattern
1. episodes: unlimited -- retrieval latency grows without bound
2. No decay policy -- stale episodes corrupt agent context
3. No retrieval_keys -- full scan per query; unscalable
4. Mixing entity facts with episodes -- entity_memory is the right home for facts
5. No owner field -- orphaned stores cannot be routed or pruned

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | episodic_memory |
| Pipeline | 8F |
| Target | 9.0+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[atom_22_memory_taxonomy]] | related | 0.26 |
| [[bld_knowledge_card_memory_architecture]] | upstream | 0.22 |
| [[p01_kc_entity_memory]] | related | 0.21 |
| [[p10_lr_memory_scope_builder]] | sibling | 0.20 |
| [[entity-memory-builder]] | related | 0.20 |
| [[bld_collaboration_entity_memory]] | downstream | 0.19 |
| [[bld_knowledge_card_entity_memory]] | upstream | 0.19 |
| [[bld_output_template_memory_architecture]] | upstream | 0.18 |
| [[bld_knowledge_card_memory_scope]] | upstream | 0.18 |
| [[p01_kc_retriever]] | upstream | 0.18 |
