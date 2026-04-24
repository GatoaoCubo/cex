---
id: p01_kc_knowledge_distillation
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Knowledge Distillation — Compressing Expertise into KCs"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: patterns
quality: 9.0
tags: [distillation, knowledge, compression, kc, expertise]
tldr: "Transform verbose sources (docs, conversations, code) into dense, structured KCs. Keep signal, remove noise. Target: 1-2KB that replaces 10KB+ of raw source."
keywords: [distillation, compression, knowledge-card, signal-to-noise, density]
density_score: 0.92
updated: "2026-04-07"
related:
  - p01_kc_distillation_pipeline
  - p01_kc_pattern_extraction
  - knowledge-card-builder
  - bld_knowledge_card_knowledge_card
  - p01_kc_zero_touch
  - p01_kc_meta_bootstrap
  - p01_kc_anti_full_context
  - p01_kc_quality_gates
  - p07_rubric_knowledge
  - p01_kc_anti_file_storage
---

# Knowledge Distillation

## Process
```
RAW SOURCE (10KB+ docs, conversations, code)
  → EXTRACT signal (concepts, patterns, decisions)
  → STRUCTURE (frontmatter + sections + tables)
  → COMPRESS (remove redundancy, increase density)
  → VALIDATE (does 1KB KC replace 10KB source?)
  → OUTPUT: knowledge_card (1-2KB, density >= 0.85)
```

## Distillation Heuristics
| Keep | Remove |
|------|--------|
| Definitions, boundaries | Verbose explanations |
| Decision criteria (when/when-not) | Historical context |
| Tables, structured data | Prose paragraphs |
| Anti-patterns | Obvious best practices |
| Provider-specific differences | Generic advice |

## Key Principles

1. Domain-specific knowledge must be verifiable and traceable
2. Artifacts reference this card via `tags` matching
3. Updates trigger re-scoring of dependent artifacts
4. Card freshness tracked via `created`/`updated` timestamps
5. Cross-references validated by `cex_compile.py`

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
| [[p01_kc_distillation_pipeline]] | sibling | 0.57 |
| [[p01_kc_pattern_extraction]] | sibling | 0.33 |
| [[knowledge-card-builder]] | downstream | 0.27 |
| [[bld_knowledge_card_knowledge_card]] | sibling | 0.27 |
| [[p01_kc_zero_touch]] | sibling | 0.27 |
| [[p01_kc_meta_bootstrap]] | sibling | 0.25 |
| [[p01_kc_anti_full_context]] | sibling | 0.24 |
| [[p01_kc_quality_gates]] | sibling | 0.24 |
| [[p07_rubric_knowledge]] | downstream | 0.24 |
| [[p01_kc_anti_file_storage]] | sibling | 0.23 |
