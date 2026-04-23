---
id: p01_kc_operational_laws
kind: knowledge_card
type: domain
pillar: P01
title: "Operational Laws"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: frameworks
quality: 9.0
tags: [framework, architecture, llm]
tldr: "System invariants that must ALWAYS hold. 8F mandatory, quality:null on creation, N07 never builds, GDP before dispatch."
keywords: [laws, invariants, constraints, non-negotiable, rules]
density_score: 0.92
updated: "2026-04-07"
related:
  - p01_kc_anti_file_storage
  - p01_kc_anti_full_context
  - p01_kc_anti_isolated_sessions
  - bld_memory_invariant
  - p01_kc_distillation_pipeline
  - bld_collaboration_invariant
  - skill
  - p01_kc_qa_validation
  - p01_kc_coordination
  - p01_kc_knowledge_distillation
---

# Operational Laws

## CEX Operational Laws (4 Rules)
1. **8F mandatory** — every artifact passes F1-F8
2. **GDP before dispatch** — subjective decisions with user first
3. **N07 never builds** — only plans, specs, dispatches, consolidates
4. **quality:null** — never self-score, peer-review assigns quality

## Properties of Good Operational Laws
1. **Invariant**: always true, no exceptions
2. **Testable**: can verify compliance automatically
3. **Short**: fits in working memory (max 5-7 rules)
4. **Justified**: each exists because violating it caused real problems

## Retrieval Example

```yaml
# Query this card via cex_retriever.py
query: "Operational Laws"
kind_filter: knowledge_card
threshold: 0.7
```

```bash
# CLI retrieval
python _tools/cex_retriever.py "Operational Laws" --top 5
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
| Domain | frameworks |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_anti_file_storage]] | sibling | 0.32 |
| [[p01_kc_anti_full_context]] | sibling | 0.32 |
| [[p01_kc_anti_isolated_sessions]] | sibling | 0.30 |
| [[bld_memory_invariant]] | downstream | 0.28 |
| [[p01_kc_distillation_pipeline]] | sibling | 0.24 |
| [[bld_collaboration_invariant]] | downstream | 0.23 |
| [[skill]] | downstream | 0.22 |
| [[p01_kc_qa_validation]] | sibling | 0.21 |
| [[p01_kc_coordination]] | sibling | 0.21 |
| [[p01_kc_knowledge_distillation]] | sibling | 0.20 |
