---
id: p01_kc_workflow_orchestration
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Workflow Orchestration Framework"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: frameworks
quality: 9.1
tags: [framework, architecture, llm]
tldr: "How to sequence multi-step workflows: DAG dependencies, wave execution, signal-based coordination, error handling."
keywords: [orchestration, workflow, dag, sequencing, dependencies]
density_score: 0.92
updated: "2026-04-07"
related:
  - p01_kc_spawn_patterns
  - p01_kc_qa_validation
  - p01_kc_input_hydration
  - p01_kc_context_scoping
  - p01_kc_batching
  - workflow-builder
  - p01_kc_schema_validation
  - p01_kc_output_formatting
  - ex_knowledge_card_rag_fundamentals
  - p01_kc_test_automation
---

# Workflow Orchestration Framework

## Orchestration Patterns
| Pattern | Description |
|---------|-------------|
| Sequential | A → B → C (each waits for previous) |
| Parallel | A + B + C (no dependencies) |
| Wave | Group 1 (parallel) → Group 2 (parallel) → ... |
| DAG | Arbitrary dependencies, topological sort |
| Event-driven | Signal triggers next step |

## CEX Orchestration
- /plan: creates DAG of tasks with dependencies
- /grid: executes waves (parallel groups)
- Signals: event-driven coordination between nuclei
- Handoffs: structured task delegation
- Manifest: shared decisions across all tasks

## Error in Orchestration
If step fails: retry → fallback → skip (if optional) → abort wave → escalate
Never let one failure cascade to unrelated steps.

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_workflow_orchestration`
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
- **Artifact ID**: `p01_kc_workflow_orchestration`
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
query: "Workflow Orchestration Framework"
kind_filter: knowledge_card
threshold: 0.7
```

```bash
# CLI retrieval
python _tools/cex_retriever.py "Workflow Orchestration Framework" --top 5
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_spawn_patterns]] | sibling | 0.48 |
| [[p01_kc_qa_validation]] | sibling | 0.46 |
| [[p01_kc_input_hydration]] | sibling | 0.44 |
| [[p01_kc_context_scoping]] | sibling | 0.44 |
| [[p01_kc_batching]] | sibling | 0.33 |
| [[workflow-builder]] | downstream | 0.31 |
| [[p01_kc_schema_validation]] | sibling | 0.31 |
| [[p01_kc_output_formatting]] | sibling | 0.30 |
| [[ex_knowledge_card_rag_fundamentals]] | sibling | 0.29 |
| [[p01_kc_test_automation]] | sibling | 0.28 |
