---
kind: collaboration
id: bld_collaboration_chunk_strategy
pillar: P12
llm_function: COLLABORATE
purpose: How chunk-strategy-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Chunk Strategy"
version: "1.0.0"
author: n03_builder
tags: [chunk_strategy, builder, examples]
tldr: "Golden and anti-examples for chunk strategy construction, demonstrating ideal structure and common pitfalls."
domain: "chunk strategy construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_retriever_config
  - chunk-strategy-builder
  - bld_collaboration_memory_scope
  - bld_collaboration_output_validator
  - bld_collaboration_embedding_config
  - bld_config_chunk_strategy
  - bld_collaboration_prompt_version
  - bld_collaboration_context_window_config
  - bld_collaboration_handoff_protocol
  - bld_collaboration_builder
---

# Collaboration: chunk-strategy-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what are the parameters and constraints for this chunk strategy?"
I specify chunk strategy configurations so agents and pipelines can use them.
## Crew Compositions
### Crew: "RAG Pipeline"
```
  1. chunk-strategy-builder -> chunking config
  2. embedding-config-builder -> vector model config
  3. retriever-config-builder -> search config
```
### Crew: "Document Processing"
```
  1. chunk-strategy-builder -> split strategy
  2. document-loader-builder -> ingestion
  3. parser-builder -> extraction
```

## Handoff Protocol
### I Receive
1. seeds: chunk strategy purpose, target system, constraints
2. optional: specific parameter values, upstream artifact references
### I Produce
1. chunk_strategy artifact (.md + .yaml frontmatter)
2. committed to: `cex/P01_knowledge/examples/p01_chunk_{name}.md`
### I Signal
1. signal: complete (with quality score from QUALITY_GATES)
2. if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0).
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| embedding-config-builder | Downstream consumer |
| retriever-config-builder | Downstream consumer |
| knowledge-index-builder | Downstream consumer |

## Properties

| Property | Value |
|----------|-------|
| Kind | `collaboration` |
| Pillar | P12 |
| Domain | chunk strategy construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_retriever_config]] | sibling | 0.70 |
| [[chunk-strategy-builder]] | upstream | 0.48 |
| [[bld_collaboration_memory_scope]] | sibling | 0.47 |
| [[bld_collaboration_output_validator]] | sibling | 0.42 |
| [[bld_collaboration_embedding_config]] | sibling | 0.41 |
| [[bld_config_chunk_strategy]] | upstream | 0.41 |
| [[bld_collaboration_prompt_version]] | sibling | 0.41 |
| [[bld_collaboration_context_window_config]] | sibling | 0.41 |
| [[bld_collaboration_handoff_protocol]] | sibling | 0.40 |
| [[bld_collaboration_builder]] | sibling | 0.40 |
