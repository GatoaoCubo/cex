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
