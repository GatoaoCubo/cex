---
kind: collaboration
id: bld_collaboration_retriever_config
pillar: P12
llm_function: COLLABORATE
purpose: How retriever-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Retriever Config"
version: "1.0.0"
author: n03_builder
tags: [retriever_config, builder, examples]
tldr: "Golden and anti-examples for retriever config construction, demonstrating ideal structure and common pitfalls."
domain: "retriever config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_chunk_strategy
  - bld_collaboration_memory_scope
  - retriever-config-builder
  - bld_collaboration_embedding_config
  - bld_collaboration_retriever
  - bld_collaboration_output_validator
  - bld_collaboration_prompt_version
  - bld_collaboration_handoff_protocol
  - bld_collaboration_hook_config
  - bld_config_retriever_config
---

# Collaboration: retriever-config-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what are the parameters and constraints for this retriever config?"
I specify retriever config configurations so agents and pipelines can use them.
## Crew Compositions
### Crew: "RAG Pipeline"
```
  1. chunk-strategy-builder -> chunking
  2. embedding-config-builder -> vectors
  3. retriever-config-builder -> search config
```
### Crew: "Search System"
```
  1. retriever-config-builder -> retrieval params
  2. knowledge-index-builder -> index infra
  3. formatter-builder -> result formatting
```

## Handoff Protocol
### I Receive
1. seeds: retriever config purpose, target system, constraints
2. optional: specific parameter values, upstream artifact references
### I Produce
1. retriever_config artifact (.md + .yaml frontmatter)
2. committed to: `cex/P01_knowledge/examples/p01_retr_{name}.md`
### I Signal
1. signal: complete (with quality score from QUALITY_GATES)
2. if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
| chunk-strategy-builder | Upstream dependency |
| embedding-config-builder | Upstream dependency |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| knowledge-index-builder | Downstream consumer |

## Properties

| Property | Value |
|----------|-------|
| Kind | `collaboration` |
| Pillar | P12 |
| Domain | retriever config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_chunk_strategy]] | sibling | 0.57 |
| [[bld_collaboration_memory_scope]] | sibling | 0.51 |
| [[retriever-config-builder]] | upstream | 0.49 |
| [[bld_collaboration_embedding_config]] | sibling | 0.45 |
| [[bld_collaboration_retriever]] | sibling | 0.43 |
| [[bld_collaboration_output_validator]] | sibling | 0.43 |
| [[bld_collaboration_prompt_version]] | sibling | 0.41 |
| [[bld_collaboration_handoff_protocol]] | sibling | 0.41 |
| [[bld_collaboration_hook_config]] | sibling | 0.40 |
| [[bld_config_retriever_config]] | upstream | 0.39 |
