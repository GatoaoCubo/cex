---
kind: collaboration
id: bld_collaboration_memory_scope
pillar: P12
llm_function: COLLABORATE
purpose: How memory-scope-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Memory Scope"
version: "1.0.0"
author: n03_builder
tags: [memory_scope, builder, examples]
tldr: "Golden and anti-examples for memory scope construction, demonstrating ideal structure and common pitfalls."
domain: "memory scope construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - memory-scope-builder
  - bld_collaboration_retriever_config
  - bld_collaboration_memory_type
  - bld_collaboration_handoff_protocol
  - bld_collaboration_output_validator
  - bld_collaboration_prompt_version
  - bld_collaboration_agent
  - bld_collaboration_builder
  - bld_manifest_memory_type
  - bld_collaboration_knowledge_card
---

# Collaboration: memory-scope-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what are the parameters and constraints for this memory scope?"
I specify memory scope configurations so agents and pipelines can use them.
## Crew Compositions
### Crew: "Agent Design"
```
  1. memory-scope-builder -> memory config
  2. agent-builder -> agent definition
  3. mental-model-builder -> routing/decisions
```
### Crew: "Memory System"
```
  1. memory-scope-builder -> scope config
  2. knowledge-index-builder -> search index
  3. session-state-builder -> runtime state
```

## Handoff Protocol
### I Receive
1. seeds: memory scope purpose, target system, constraints
2. optional: specific parameter values, upstream artifact references
### I Produce
1. memory_scope artifact (.md + .yaml frontmatter)
2. committed to: `cex/P02_model/examples/p02_memscope_{name}.md`
### I Signal
1. signal: complete (with quality score from QUALITY_GATES)
2. if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
| agent-builder | Upstream dependency |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| knowledge-index-builder | Downstream consumer |
| session-state-builder | Downstream consumer |

## Properties

| Property | Value |
|----------|-------|
| Kind | `collaboration` |
| Pillar | P12 |
| Domain | memory scope construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[memory-scope-builder]] | upstream | 0.50 |
| [[bld_collaboration_retriever_config]] | sibling | 0.49 |
| [[bld_collaboration_memory_type]] | sibling | 0.48 |
| [[bld_collaboration_handoff_protocol]] | sibling | 0.43 |
| [[bld_collaboration_output_validator]] | sibling | 0.40 |
| [[bld_collaboration_prompt_version]] | sibling | 0.40 |
| [[bld_collaboration_agent]] | sibling | 0.40 |
| [[bld_collaboration_builder]] | sibling | 0.39 |
| [[bld_manifest_memory_type]] | upstream | 0.38 |
| [[bld_collaboration_knowledge_card]] | sibling | 0.37 |
