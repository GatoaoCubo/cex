---
id: p01_kc_context_scoping
kind: knowledge_card
type: domain
pillar: P01
title: "Context Scoping Framework"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: frameworks
quality: 9.1
tags: [framework, architecture, llm]
tldr: "Each nucleus has a bounded context. N01 does research, not code. N05 deploys, not designs. Scoping prevents god-agents."
keywords: [scoping, context, boundaries, nucleus, separation]
density_score: 0.92
updated: "2026-04-07"
related:
  - p01_kc_qa_validation
  - p01_kc_input_hydration
  - p01_kc_workflow_orchestration
  - p01_kc_spawn_patterns
  - p01_kc_schema_validation
  - ex_knowledge_card_rag_fundamentals
  - p01_kc_output_formatting
  - p01_kc_test_automation
  - p03_sp_knowledge_nucleus
  - p01_kc_governance_patterns
---

# Context Scoping Framework

## Nucleus Scopes
| Nucleus | IN scope | OUT of scope |
|---------|----------|-------------|
| N01 | Research, analysis | Code, deploy |
| N02 | Frontend, copy, design | Backend, infra |
| N03 | Build artifacts | Research, deploy |
| N04 | Documentation, knowledge | Code, sales |
| N05 | Deploy, ops, infra | Design, content |
| N06 | Brand, pricing, revenue | Code, research |
| N07 | Plan, dispatch, consolidate | Build (anything) |

## Cross-Scope Communication
When a nucleus needs something out of scope: signal + handoff to correct nucleus.
Never expand scope. Always delegate.

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_context_scoping`
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
- **Artifact ID**: `p01_kc_context_scoping`
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
query: "Context Scoping Framework"
kind_filter: knowledge_card
threshold: 0.7
```

```bash
# CLI retrieval
python _tools/cex_retriever.py "Context Scoping Framework" --top 5
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_qa_validation]] | sibling | 0.49 |
| [[p01_kc_input_hydration]] | sibling | 0.47 |
| [[p01_kc_workflow_orchestration]] | sibling | 0.43 |
| [[p01_kc_spawn_patterns]] | sibling | 0.43 |
| [[p01_kc_schema_validation]] | sibling | 0.32 |
| [[ex_knowledge_card_rag_fundamentals]] | sibling | 0.30 |
| [[p01_kc_output_formatting]] | sibling | 0.30 |
| [[p01_kc_test_automation]] | sibling | 0.29 |
| [[p03_sp_knowledge_nucleus]] | downstream | 0.28 |
| [[p01_kc_governance_patterns]] | sibling | 0.28 |
