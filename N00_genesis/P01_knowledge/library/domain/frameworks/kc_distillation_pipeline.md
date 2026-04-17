---
id: p01_kc_distillation_pipeline
kind: knowledge_card
type: domain
pillar: P01
title: "Distillation Pipeline"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: frameworks
quality: 9.0
tags: [framework, architecture, llm]
tldr: "Transform raw sources into KCs through a pipeline: collect > filter > structure > compress > validate > publish."
keywords: [distillation, pipeline, raw-to-kc, compression]
density_score: 0.92
updated: "2026-04-07"
---

# Distillation Pipeline

## Pipeline Steps
```
COLLECT → FILTER → STRUCTURE → COMPRESS → VALIDATE → PUBLISH
  raw      signal    frontmatter   density    compile    P01/
  sources   only      + sections    >= 0.85    + doctor   library/
```

## Input Sources
| Source | Example | Typical Output |
|--------|---------|---------------|
| Conversation | User explains domain | Domain KC |
| Code | Implementation patterns | Pattern KC |
| Docs | API documentation | Platform KC |
| Error log | Recurring failures | Anti-pattern KC |
| Competition | Market research | Competitive KC |

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
