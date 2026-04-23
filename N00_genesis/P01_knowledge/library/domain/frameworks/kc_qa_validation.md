---
id: p01_kc_qa_validation
kind: knowledge_card
type: domain
pillar: P01
title: "QA Validation Framework"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: frameworks
quality: 9.1
tags: [framework, architecture, llm]
tldr: "Multi-layer validation: schema (compile), structural (doctor), behavioral (tests), quality (score), brand (audit)."
keywords: [qa, validation, gates, checklist, automated]
density_score: 0.92
updated: "2026-04-07"
related:
  - p01_kc_input_hydration
  - p01_kc_context_scoping
  - p01_kc_workflow_orchestration
  - p01_kc_spawn_patterns
  - p01_kc_test_automation
  - p01_kc_schema_validation
  - ex_knowledge_card_rag_fundamentals
  - p01_kc_output_formatting
  - knowledge-card-builder
  - p01_kc_governance_patterns
---

# QA Validation Framework

## Validation Layers
| Layer | What | Tool | Blocking |
|-------|------|------|----------|
| Schema | YAML valid, fields present | cex_compile.py | Yes |
| Structural | Builder complete (13 specs) | cex_doctor.py | Yes |
| Behavioral | Functions work correctly | pytest | Yes |
| Quality | Score >= 8.0 | cex_score.py | For publish |
| Brand | Consistency >= 0.85 | brand_audit.py | For N06 |
| Security | No secrets, no PII | wf_auto_security | For deploy |

## When to Run
- After every F6 PRODUCE: schema + structural
- After every commit: behavioral (pre-commit hook)
- Before dispatch: structural + behavioral
- Before publish: all layers

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_qa_validation`
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
- **Artifact ID**: `p01_kc_qa_validation`
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
query: "QA Validation Framework"
kind_filter: knowledge_card
threshold: 0.7
```

```bash
# CLI retrieval
python _tools/cex_retriever.py "QA Validation Framework" --top 5
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_input_hydration]] | sibling | 0.49 |
| [[p01_kc_context_scoping]] | sibling | 0.47 |
| [[p01_kc_workflow_orchestration]] | sibling | 0.43 |
| [[p01_kc_spawn_patterns]] | sibling | 0.41 |
| [[p01_kc_test_automation]] | sibling | 0.37 |
| [[p01_kc_schema_validation]] | sibling | 0.34 |
| [[ex_knowledge_card_rag_fundamentals]] | sibling | 0.32 |
| [[p01_kc_output_formatting]] | sibling | 0.31 |
| [[knowledge-card-builder]] | downstream | 0.28 |
| [[p01_kc_governance_patterns]] | sibling | 0.27 |
