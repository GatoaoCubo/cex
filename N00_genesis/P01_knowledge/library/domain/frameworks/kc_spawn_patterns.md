---
id: p01_kc_spawn_patterns
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Spawn Patterns — Multi-Agent Process Management"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: frameworks
quality: 9.0
tags: [framework, architecture, llm]
tldr: "Patterns for launching parallel agent processes: solo (1 nucleus), grid (up to 6), wave (sequential groups)."
keywords: [spawn, process, multi-agent, parallel, grid]
density_score: 0.92
updated: "2026-04-07"
related:
  - p01_kc_workflow_orchestration
  - p01_kc_qa_validation
  - p01_kc_context_scoping
  - p01_kc_input_hydration
  - p01_kc_schema_validation
  - p01_kc_output_formatting
  - ex_knowledge_card_rag_fundamentals
  - p01_kc_batching
  - p01_kc_test_automation
  - p01_kc_governance_patterns
---

# Spawn Patterns

## Spawn Strategies
| Strategy | When | Parallelism |
|----------|------|-------------|
| Solo | Single task, 1 nucleus | 1 |
| Grid | Independent tasks | Up to 6 |
| Wave | Sequential dependencies | Groups |
| Pipeline | A output feeds B | Chained |

## CEX Spawn Architecture
- spawn_solo.ps1: 1 nucleus in positioned window
- spawn_grid.ps1: up to 6 parallel windows
- dispatch.sh: bash wrapper (solo/grid/status/stop)
- PID tracking: .cex/runtime/pids/
- Signal collection: .cex/runtime/signals/

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_spawn_patterns`
- **Tags**: [framework, architecture, llm]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_spawn_patterns`
- **Tags**: [framework, architecture, llm]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Retrieval Example

```yaml
# Query this card via cex_retriever.py
query: "Spawn Patterns — Multi-Agent Process Management"
kind_filter: knowledge_card
threshold: 0.7
```

```bash
# CLI retrieval
python _tools/cex_retriever.py "Spawn Patterns — Multi-Agent Process Management" --top 5
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_workflow_orchestration]] | sibling | 0.48 |
| [[p01_kc_qa_validation]] | sibling | 0.46 |
| [[p01_kc_context_scoping]] | sibling | 0.45 |
| [[p01_kc_input_hydration]] | sibling | 0.45 |
| [[p01_kc_schema_validation]] | sibling | 0.34 |
| [[p01_kc_output_formatting]] | sibling | 0.32 |
| [[ex_knowledge_card_rag_fundamentals]] | sibling | 0.32 |
| [[p01_kc_batching]] | sibling | 0.31 |
| [[p01_kc_test_automation]] | sibling | 0.31 |
| [[p01_kc_governance_patterns]] | sibling | 0.29 |
