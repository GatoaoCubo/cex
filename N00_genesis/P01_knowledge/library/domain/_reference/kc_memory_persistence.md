---
id: p01_kc_memory_persistence
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Memory & Persistence — Learning Records, Session State, Runtime State, Entity Memory, Summaries"
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: memory_persistence
origin: manual
quality: 9.1
tags: [memory, persistence, learning, session, state, entity, summary, lifecycle]
tldr: "Memory persistence covers the full lifecycle from ephemeral session state through entity graphs to compressed long-term summaries"
when_to_use: "Designing memory systems, session management, entity tracking, conversation compression, or long-term learning"
keywords: [memory, learning-record, session-state, runtime-state, entity-memory, summary, zep, mem0]
long_tails:
  - "How to design memory lifecycle from session capture through consolidation to long-term recall"
  - "Which patterns govern entity graph construction and conversation compression in agent memory"
axioms:
  - "Memory has a lifecycle — capture, consolidate, compress, recall — each stage has distinct storage and retrieval patterns"
  - "Entity memory is graph-structured — relationships between entities carry as much value as the entities themselves"
linked_artifacts:
  primary: null
  related: [p01_kc_langchain_patterns, p01_kc_crewai_patterns, p01_kc_feedback_loops]
feeds_kinds:
  - learning_record    # Validated insights from task execution, success/failure patterns with scores
  - session_state      # Conversation snapshots, turn history, active context windows
  - runtime_state      # Process status, checkpoint data, in-flight task state
  - entity_memory      # Named entity graphs, relationship maps, attribute tracking
  - memory_summary     # Compressed conversation summaries, periodic consolidation outputs
density_score: 0.87
related:
  - bld_collaboration_entity_memory
  - memory-summary-builder
  - p01_kc_memory_scope
  - entity-memory-builder
  - bld_knowledge_card_memory_scope
  - bld_collaboration_memory_type
  - bld_knowledge_card_entity_memory
  - bld_collaboration_memory_summary
  - p01_kc_memory_summary
  - memory-scope-builder
---

# Memory & Persistence

## Quick Reference
```yaml
topic: Memory Persistence (learning, sessions, state, entities, summaries)
scope: Memory lifecycle, session snapshots, entity graphs, conversation compression
source: manual (Zep, Mem0, LangChain memory, CrewAI memory patterns)
criticality: high
```

## Key Concepts

| Concept | Domain | CEX Kind | Role |
|---------|--------|----------|------|
| Learning Record | Long-term | learning_record | Validated insight with confidence score, persists across sessions |
| Session Snapshot | Ephemeral | session_state | Full conversation state at a point in time, expires with session |
| Runtime Checkpoint | Transient | runtime_state | In-flight process state for recovery (task progress, retries) |
| Entity Graph | Structured | entity_memory | Named entities with typed relationships (person-owns-project) |
| Conversation Summary | Compressed | memory_summary | Periodic compression of verbose history into key facts |

## Patterns

| Trigger | Action |
|---------|--------|
| Task completes with score >= 8.0 | Create `learning_record` with patterns, anti-patterns, and confidence |
| New conversation turn | Update `session_state` with turn content and active context window |
| Long-running task checkpoint | Write `runtime_state` with progress, partial results, retry count |
| New entity mentioned | Upsert `entity_memory` node, link relationships to existing graph |
| Context window > 80% full | Generate `memory_summary` from oldest turns, replace originals |

## Memory Lifecycle

```text
[session_state] -> [runtime_state] -> [entity_memory] -> [memory_summary] -> [learning_record]
  Ephemeral          Transient          Structured          Compressed          Permanent
  (per-turn)         (per-task)         (per-entity)        (periodic)          (validated)
```

## Anti-Patterns

- Storing raw conversation history without compression (context window exhaustion)
- Treating all memories as equal priority (learning records >> session state)
- Entity memory without relationship types (flat list instead of graph)
- Missing expiration on session_state (stale data pollutes future sessions)
- Learning records without confidence scores (no basis for recall ranking)

## Integration Points

| System | Memory Type | Pattern |
|--------|-------------|---------|
| Zep | entity_memory, memory_summary | Automatic entity extraction + summary generation |
| Mem0 | learning_record, entity_memory | Cross-session memory with user/agent scoping |
| LangChain | session_state, memory_summary | BaseChatMessageHistory + ConversationSummaryMemory |
| CrewAI | learning_record, entity_memory | Short-term, long-term, and entity memory layers |
| organization | learning_record | memory_bridge.py syncs to MEMORY.md with score filtering |

## References

- related: p01_kc_langchain_patterns, p01_kc_crewai_patterns
- patterns: Zep memory server, Mem0 platform, LangChain memory, organization memory bridge

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_entity_memory]] | downstream | 0.44 |
| [[memory-summary-builder]] | downstream | 0.43 |
| [[p01_kc_memory_scope]] | sibling | 0.43 |
| [[entity-memory-builder]] | downstream | 0.41 |
| [[bld_knowledge_card_memory_scope]] | sibling | 0.39 |
| [[bld_collaboration_memory_type]] | downstream | 0.39 |
| [[bld_knowledge_card_entity_memory]] | sibling | 0.38 |
| [[bld_collaboration_memory_summary]] | downstream | 0.38 |
| [[p01_kc_memory_summary]] | sibling | 0.37 |
| [[memory-scope-builder]] | downstream | 0.35 |
