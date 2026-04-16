---
kind: collaboration
id: bld_collaboration_consolidation_policy
pillar: P12
llm_function: COLLABORATE
purpose: How consolidation_policy-builder works in crews with other CEX builders
quality: 9.1
title: "Collaboration: consolidation_policy-builder"
version: "2.0.0"
author: n06_commercial
tags: [consolidation_policy, builder, collaboration]
tldr: "consolidation_policy-builder consumes memory_architecture (parent), produces lifecycle rules for use by procedural-memory-builder and retriever-config-builder"
domain: "LLM agent memory consolidation"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
---

## Crew Role

Governs the memory lifecycle within a complete agent memory system. Consumes the parent
memory_architecture artifact (which layers are active, what tier, what backends) and
produces the promotion + eviction rules that operate on those layers. Other builders
in the memory cluster reference consolidation_policy for TTL and retention guidance.

## Receives From

| Builder | What | Format |
|---------|------|--------|
| memory-architecture-builder | Active layers, tier, backend config | memory_architecture artifact |
| knowledge-card-builder | Domain research on MemGPT pipeline, eviction algorithms | knowledge_card artifact |

## Produces For

| Builder | What | Format |
|---------|------|--------|
| procedural-memory-builder | Skill TTL and versioning policy | consolidation_policy artifact |
| retriever-config-builder | Episodic memory TTL + eviction triggers for index management | consolidation_policy artifact |
| agent-builder | Memory lifecycle summary for system prompt | Tier + retention summary |
| N06 commercial review | Enterprise compliance config for tier validation | Compliance Config section |

## Boundary

Does NOT produce:
- Layer definitions or backend configs (-> memory_architecture kind)
- Skill schemas, versioning protocols, or skill namespace (-> procedural_memory kind)
- Retrieval configs, embedding models, or reranker settings (-> retriever_config kind)
- Access control policies or permission scopes (-> memory_scope kind)
- Token compression configs (-> compression_config kind)

## Dispatch Pattern

In a grid dispatch building a complete agent memory system:
1. N06 (commercial) builds `memory_architecture` first (establishes layers + tier)
2. N06 (commercial) builds `consolidation_policy` using memory_architecture as input
3. N04 (knowledge) builds `procedural_memory` referencing consolidation_policy for TTL
4. N01 (intelligence) builds `retriever_config` for episodic/semantic layers
5. N07 consolidates and cross-validates all four artifacts for consistency
