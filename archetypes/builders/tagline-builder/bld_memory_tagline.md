---
id: bld_memory_tagline
kind: memory
pillar: P09
builder: tagline-builder
version: 1.0.0
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.0
title: "Memory Tagline"
author: n03_builder
tags: [tagline, builder, examples]
tldr: "Golden and anti-examples for tagline construction, demonstrating ideal structure and common pitfalls."
domain: "tagline construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: INJECT
---
# Memory: Tagline Builder

## What to Remember
1. User's preferred tone/style from previous tagline requests
2. Rejected taglines and WHY (never suggest again)
3. Approved taglines (maintain consistency in future requests)
4. Brand voice evolution over time
5. Competitor taglines encountered (avoid similarity)

## Memory Types
1. PREFERENCE: user's tone choice (formal vs casual, emotional vs functional)
2. CORRECTION: "don't use puns", "shorter is better", specific word avoidance
3. CONVENTION: brand language rules (always use X word, never use Y)
4. CONTEXT: industry norms, competitor landscape, cultural considerations

## Metadata

```yaml
id: bld_memory_tagline
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-tagline.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P09 |
| Domain | tagline construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
