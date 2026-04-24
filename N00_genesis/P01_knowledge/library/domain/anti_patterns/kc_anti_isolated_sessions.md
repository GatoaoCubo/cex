---
id: p01_kc_anti_isolated_sessions
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Anti-Pattern: Isolated Sessions"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: anti_patterns
quality: 9.1
tags: [anti-pattern, isolated, sessions, continuity, handoff]
tldr: "Sessions that don't share state. Each starts from zero. No learning carries over. Fix: shared filesystem, signals, handoffs."
when_to_use: "Designing multi-session or multi-agent workflows"
keywords: [anti-pattern, isolation, continuity, shared-state, handoff]
density_score: 0.91
updated: "2026-04-07"
related:
  - p01_kc_anti_full_context
  - p01_kc_anti_file_storage
  - p01_kc_coordination
  - p01_kc_operational_laws
  - p01_kc_memory_consolidation
  - runtime-state-builder
  - bld_memory_runtime_state
  - skill
  - p01_kc_distillation_pipeline
  - p01_kc_pattern_extraction
---

# Anti-Pattern: Isolated Sessions

## The Problem
Each session/agent starts from scratch. No memory of previous sessions. No shared state between agents. Work is repeated.

## Symptoms
1. Agent re-discovers what was already known
2. Parallel agents produce contradictory output
3. No improvement over time
4. User repeats context every session

## Fix
1. Shared filesystem as state (`.cex/runtime/`, `P01_knowledge/`)
2. Signals between agents (`signal_writer.py`)
3. Handoff documents (`.cex/runtime/handoffs/`)
4. Decision manifests (`.cex/runtime/decisions/`)
5. Learning records (`.cex/learning_records/`)
6. Brand config as shared identity (`.cex/brand/brand_config.yaml`)

## Retrieval Example

```yaml
# Query this card via cex_retriever.py
query: "Anti-Pattern: Isolated Sessions"
kind_filter: knowledge_card
threshold: 0.7
```

```bash
# CLI retrieval
python _tools/cex_retriever.py "Anti-Pattern: Isolated Sessions" --top 5
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
| [[p01_kc_anti_full_context]] | sibling | 0.48 |
| [[p01_kc_anti_file_storage]] | sibling | 0.35 |
| [[p01_kc_coordination]] | sibling | 0.34 |
| [[p01_kc_operational_laws]] | sibling | 0.29 |
| [[p01_kc_memory_consolidation]] | sibling | 0.26 |
| [[runtime-state-builder]] | downstream | 0.25 |
| [[bld_memory_runtime_state]] | downstream | 0.24 |
| [[skill]] | downstream | 0.24 |
| [[p01_kc_distillation_pipeline]] | sibling | 0.23 |
| [[p01_kc_pattern_extraction]] | sibling | 0.23 |
