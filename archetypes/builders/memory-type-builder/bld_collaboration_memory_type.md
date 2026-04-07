---
kind: collaboration
id: bld_collaboration_memory_type
pillar: P12
llm_function: COLLABORATE
quality: 9.0
title: "Collaboration Memory Type"
version: "1.0.0"
author: n03_builder
tags: [memory_type, builder, examples]
tldr: "Golden and anti-examples for memory type construction, demonstrating ideal structure and common pitfalls."
domain: "memory type construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Collaboration: memory_type

## Produces For
1. entity-memory-builder: memory types classify entity observations
2. memory-scope-builder: type informs scope (correction=global, context=session)
3. memory-summary-builder: type determines summarization strategy

## Consumes From
1. agent-builder: agent definitions include memory preferences
2. system-prompt-builder: identity prompts reference memory behavior

## Metadata

```yaml
id: bld_collaboration_memory_type
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-collaboration-memory-type.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `collaboration` |
| Pillar | P12 |
| Domain | memory type construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
