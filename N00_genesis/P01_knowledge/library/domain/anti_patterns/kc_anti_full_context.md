---
id: p01_kc_anti_full_context
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Anti-Pattern: Full Context Dependency"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: anti_patterns
quality: 9.1
tags: [anti-pattern, context-window, memory, session]
tldr: "Don't rely on conversation history as the only state. Context windows overflow, sessions end, models change. Persist state to files."
when_to_use: "Designing agent memory and state management"
keywords: [anti-pattern, context-dependency, state-persistence, session-loss]
density_score: 0.91
updated: "2026-04-07"
related:
  - p01_kc_anti_isolated_sessions
  - p01_kc_anti_file_storage
  - p01_kc_operational_laws
  - p01_kc_memory_consolidation
  - bld_memory_session_state
  - p01_kc_context_overflow
  - session-state-builder
  - p01_kc_pattern_extraction
  - p01_kc_distillation_pipeline
  - p03_sp_session_state_builder
---

# Anti-Pattern: Full Context Dependency

## The Problem
Assuming the entire conversation history is always available. Context windows have limits (200K tokens max). Sessions end. Models switch. History is lost.

## Symptoms
1. "It forgot what we discussed earlier"
2. Breaking when context exceeds window
3. Can't resume work across sessions
4. Agent quality degrades over long conversations

## Fix
1. Write state to files (manifests, handoffs, plans)
2. Use `.cex/runtime/` for persistent state
3. Write learning records after important discoveries
4. Design for session-less operation: any session can pick up from files
5. `wf_auto_handoff.md` saves state before session ends

## Retrieval Example

```yaml
# Query this card via cex_retriever.py
query: "Anti-Pattern: Full Context Dependency"
kind_filter: knowledge_card
threshold: 0.7
```

```bash
# CLI retrieval
python _tools/cex_retriever.py "Anti-Pattern: Full Context Dependency" --top 5
```

## Quality Criteria

| Dimension | Requirement | Weight |
|-----------|------------|--------|
| Factual accuracy | Verifiable claims only | 0.25 |
| Atomicity | One concept per card | 0.20 |
| Actionability | Reader knows next steps | 0.20 |
| Density | No filler sentences | 0.20 |
| Searchability | Tags enable retrieval | 0.15 |

## Artifact Properties

| Property | Value |
|----------|-------|
| Kind | `knowledge_card` |
| Pillar | P01 |
| Domain | anti_patterns |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_anti_isolated_sessions]] | sibling | 0.47 |
| [[p01_kc_anti_file_storage]] | sibling | 0.43 |
| [[p01_kc_operational_laws]] | sibling | 0.29 |
| [[p01_kc_memory_consolidation]] | sibling | 0.27 |
| [[bld_memory_session_state]] | downstream | 0.27 |
| [[p01_kc_context_overflow]] | sibling | 0.25 |
| [[session-state-builder]] | downstream | 0.25 |
| [[p01_kc_pattern_extraction]] | sibling | 0.24 |
| [[p01_kc_distillation_pipeline]] | sibling | 0.24 |
| [[p03_sp_session_state_builder]] | downstream | 0.23 |
