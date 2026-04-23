---
quality: 8.6
quality: 8.0
kind: collaboration
id: bld_collaboration_episodic_memory
pillar: P12
llm_function: COLLABORATE
purpose: How episodic-memory-builder works in crews with other builders
title: "Collaboration Episodic Memory"
version: "1.0.0"
author: n03_builder
tags: [episodic_memory, builder, collaboration]
tldr: "episodic-memory-builder is the long-term episode store in P10 memory crews."
domain: "episodic memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_collaboration_entity_memory
  - bld_collaboration_memory_scope
  - bld_collaboration_memory_type
  - atom_22_memory_taxonomy
  - p01_kc_memory_persistence
  - bld_collaboration_knowledge_graph
  - bld_collaboration_memory_summary
  - entity-memory-builder
  - bld_knowledge_card_memory_scope
  - bld_knowledge_card_memory_architecture
---

# Collaboration: episodic-memory-builder

## My Role in Crews
I am a SPECIALIST. I design the long-term episode store for an agent's interaction history.
I do not store entity facts. I do not compress context. I do not hold current task state.
I provide the temporally-indexed episode schema that enables agents to recall what happened in past interactions.

## Crew Compositions

### Crew: "P10 Memory System"
```
  1. working-memory-builder -> "task context (promotes episodes here on complete)"
  2. episodic-memory-builder -> "long-term episode store"
  3. entity-memory-builder -> "long-term entity facts (parallel store)"
  4. memory-summary-builder -> "compressed context from this episode store"
```

## Handoff Protocol

### I Receive
- seeds: owner (agent/nucleus ID), expected interaction domain, episode retention needs

### I Produce
- episodic_memory artifact (.md)
- committed to: `N0x_{domain}/P10_memory/p10_ep_{scope}.md`

## Builders I Depend On
| Builder | Why |
|---------|-----|
| working-memory-builder | Defines promotion sources that feed this store |
| entity-memory-builder | Entity facts are sibling kind; coordinate to avoid duplication |

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| memory-summary-builder | Compresses accumulated episodes into shorter context blocks |
| agent-builder | Agents declare episodic_memory as a context source |
| instruction-builder | Instructions may reference past episode outcomes |

## Conflict Resolution
| Scenario | Resolution |
|----------|-----------|
| Episode vs entity fact | Episodes are temporal events; entity facts are timeless attributes. Keep separate. |
| Episode vs memory_summary | Episodes = raw records; memory_summary = compressed output of episodes. Sequential, not competing. |
| Episode store vs session_state | episodic = long-term, persists across sessions. session_state = in-session only. |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_entity_memory]] | sibling | 0.41 |
| [[bld_collaboration_memory_scope]] | sibling | 0.41 |
| [[bld_collaboration_memory_type]] | sibling | 0.39 |
| [[atom_22_memory_taxonomy]] | related | 0.34 |
| [[p01_kc_memory_persistence]] | upstream | 0.33 |
| [[bld_collaboration_knowledge_graph]] | sibling | 0.33 |
| [[bld_collaboration_memory_summary]] | sibling | 0.32 |
| [[entity-memory-builder]] | upstream | 0.31 |
| [[bld_knowledge_card_memory_scope]] | upstream | 0.31 |
| [[bld_knowledge_card_memory_architecture]] | upstream | 0.31 |
