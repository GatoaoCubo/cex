---
kind: collaboration
id: bld_collaboration_memory_architecture
pillar: P12
llm_function: COLLABORATE
purpose: How memory_architecture-builder works in crews with other CEX builders
quality: 9.1
title: "Collaboration: memory_architecture-builder"
version: "2.0.0"
author: n06_commercial
tags: [memory_architecture, builder, collaboration]
tldr: "memory_architecture-builder coordinates with consolidation-policy-builder (eviction rules), procedural-memory-builder (skill schema), retriever-config-builder (retrieval config), and agent-builder (parent agent spec)"
domain: "LLM agent memory systems"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
related:
  - bld_collaboration_consolidation_policy
  - bld_collaboration_procedural_memory
  - memory-architecture-builder
  - bld_collaboration_agent
  - bld_architecture_kind
  - p03_sp_memory_architecture_builder
  - bld_collaboration_system_prompt
  - bld_collaboration_memory_scope
  - agent-builder
  - agent_card_n04
---

## Crew Role
Defines the structural blueprint for how an LLM agent manages context across sessions.
Acts as the parent specification that consolidation_policy, procedural_memory, and
retriever_config artifacts operate within. Informs agent-builder of memory capabilities
available per commercial tier.

## Receives From
| Builder | What | Format |
|---------|------|--------|
| agent-builder | Agent type, domain, target tier | YAML frontmatter |
| knowledge-card-builder | Domain knowledge about memory systems | .md knowledge card |
| retriever-config-builder | Retrieval config (embedding model, top-k, reranker) | YAML |

## Produces For
| Builder | What | Format |
|---------|------|--------|
| consolidation-policy-builder | Layer definitions + retention policies to enforce | memory_architecture artifact |
| procedural-memory-builder | Procedural layer backend spec and skill schema | memory_architecture artifact |
| retriever-config-builder | Which layers need retrieval + context injection points | Spec section |
| agent-builder | Memory capabilities table for system prompt injection | Tier matrix table |

## Boundary
Does NOT produce:
- Consolidation rules or eviction algorithms (-> consolidation_policy kind)
- Skill schemas or versioning protocols (-> procedural_memory kind)
- Retrieval configs, embedding models, or reranker configs (-> retriever_config kind)
- Agent routing or tool call configs (-> agent kind, P02)

## Dispatch Pattern
In a grid dispatch building a complete agent memory system:
1. N06 (commercial) builds `memory_architecture` first (tier matrix, layer definitions)
2. N04 (knowledge) builds `consolidation_policy` using the architecture as input
3. N04 (knowledge) builds `procedural_memory` using the architecture as input
4. N01 (intelligence) builds `retriever_config` for the episodic/semantic layers
5. N07 consolidates: all four artifacts form the complete memory system spec

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_consolidation_policy]] | sibling | 0.58 |
| [[bld_collaboration_procedural_memory]] | sibling | 0.54 |
| [[memory-architecture-builder]] | upstream | 0.41 |
| [[bld_collaboration_agent]] | sibling | 0.40 |
| [[bld_architecture_kind]] | upstream | 0.36 |
| [[p03_sp_memory_architecture_builder]] | upstream | 0.35 |
| [[bld_collaboration_system_prompt]] | sibling | 0.34 |
| [[bld_collaboration_memory_scope]] | sibling | 0.34 |
| [[agent-builder]] | upstream | 0.34 |
| [[agent_card_n04]] | upstream | 0.34 |
