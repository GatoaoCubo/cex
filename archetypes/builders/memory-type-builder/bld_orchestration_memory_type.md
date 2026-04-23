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
related:
  - bld_collaboration_memory_scope
  - bld_manifest_memory_type
  - memory-scope-builder
  - bld_config_memory_type
  - p10_lr_memory_scope_builder
  - bld_tools_memory_type
  - p01_kc_memory_scope
  - bld_instruction_memory_type
  - bld_config_memory_scope
  - bld_knowledge_card_memory_scope
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_memory_scope]] | sibling | 0.57 |
| [[bld_manifest_memory_type]] | upstream | 0.55 |
| [[memory-scope-builder]] | upstream | 0.47 |
| [[bld_config_memory_type]] | upstream | 0.44 |
| [[p10_lr_memory_scope_builder]] | upstream | 0.36 |
| [[bld_tools_memory_type]] | upstream | 0.35 |
| [[p01_kc_memory_scope]] | upstream | 0.34 |
| [[bld_instruction_memory_type]] | upstream | 0.33 |
| [[bld_config_memory_scope]] | upstream | 0.32 |
| [[bld_knowledge_card_memory_scope]] | upstream | 0.32 |
