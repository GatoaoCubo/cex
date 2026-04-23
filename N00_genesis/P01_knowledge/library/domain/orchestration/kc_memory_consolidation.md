---
id: p01_kc_memory_consolidation
kind: knowledge_card
type: domain
pillar: P01
title: "Memory Consolidation — Long-Term Learning for Agents"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: orchestration
quality: 9.1
tags: [memory, consolidation, learning, long-term, knowledge-management]
tldr: "Short-term (session) → working (handoff) → long-term (KC/learning record). Consolidate learnings across sessions into persistent knowledge."
when_to_use: "Designing agent memory systems that persist across sessions"
keywords: [memory, consolidation, learning, persistence, session-to-permanent]
density_score: 0.92
updated: "2026-04-07"
related:
  - p01_kc_memory_persistence
  - p01_kc_anti_full_context
  - p02_memory_scope
  - atom_22_memory_taxonomy
  - p01_kc_memory_scope
  - p01_kc_anti_isolated_sessions
  - bld_memory_session_state
  - bld_collaboration_memory_summary
  - p03_sp_session_state_builder
  - p01_kc_session_backend
---

# Memory Consolidation

## Memory Tiers

| Tier | Scope | Persistence | Example |
|------|-------|-------------|---------|
| Ephemeral | Current turn | None | Intermediate reasoning |
| Short-term | Current session | Context window | Conversation history |
| Working | Cross-session | Files | Handoffs, plans, manifests |
| Long-term | Permanent | KCs, learning records | Pattern learned, skill acquired |

## Consolidation Flow
```
SESSION (ephemeral + short-term)
  → HANDOFF (working: what happened, what's next)
  → LEARNING RECORD (long-term: what was learned)
  → KNOWLEDGE CARD (permanent: reusable knowledge)
```

## CEX Memory Architecture
- **Ephemeral**: conversation in LLM context window
- **Short-term**: `.cex/runtime/handoffs/` (per-session task state)
- **Working**: `.cex/runtime/decisions/`, plans, signals
- **Long-term**: `.cex/learning_records/`, builder memory files
- **Permanent**: `P01_knowledge/library/` (KCs), `archetypes/builders/` (specs)

## When to Consolidate
- Session ending (auto-handoff)
- Pattern discovered (create KC)
- Error fixed (learning record)
- Process improved (update workflow)

## Quality Criteria

| Dimension | Requirement | Weight |
|-----------|------------|--------|
| Factual accuracy | Verifiable claims only | 0.25 |
| Atomicity | One concept per card | 0.20 |
| Actionability | Reader knows next steps | 0.20 |
| Density | No filler sentences | 0.20 |
| Searchability | Tags enable retrieval | 0.15 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_memory_persistence]] | sibling | 0.34 |
| [[p01_kc_anti_full_context]] | sibling | 0.33 |
| [[p02_memory_scope]] | downstream | 0.31 |
| [[atom_22_memory_taxonomy]] | sibling | 0.31 |
| [[p01_kc_memory_scope]] | sibling | 0.30 |
| [[p01_kc_anti_isolated_sessions]] | sibling | 0.28 |
| [[bld_memory_session_state]] | downstream | 0.28 |
| [[bld_collaboration_memory_summary]] | downstream | 0.28 |
| [[p03_sp_session_state_builder]] | downstream | 0.28 |
| [[p01_kc_session_backend]] | sibling | 0.28 |
