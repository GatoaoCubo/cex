---
kind: collaboration
id: bld_collaboration_hook_config
pillar: P12
llm_function: COLLABORATE
purpose: How hook-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Hook Config"
version: "1.0.0"
author: n03_builder
tags: [hook_config, builder, examples]
tldr: "Golden and anti-examples for hook config construction, demonstrating ideal structure and common pitfalls."
domain: "hook config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - hook-config-builder
  - bld_collaboration_hook
  - bld_collaboration_retriever_config
  - bld_examples_hook_config
  - bld_collaboration_builder
  - bld_collaboration_lifecycle_rule
  - hook-builder
  - bld_collaboration_quality_gate
  - p03_sp_hook_config_builder
  - bld_collaboration_memory_scope
---

# Collaboration: hook-config-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "which hooks fire at each build phase and under what conditions?"
I declare hook lifecycle configurations so builders and pipelines can bind events.
## Crew Compositions
### Crew: "Builder Pipeline"
```
  1. hook-config-builder -> hook lifecycle ofclaration
  2. quality-gate-builder -> quality scoring rules
  3. lifecycle-rule-builder -> archive/promote policy
```
### Crew: "Execution Framework"
```
  1. hook-config-builder -> event bindings
  2. plugin-builder -> extension modules
  3. agent-builder -> agent execution config
```

## Handoff Protocol
### I Receive
1. seeds: target builder, pipeline phases, hook requirements
2. optional: specific event bindings, upstream artifact references
### I Produce
1. hook_config artifact (.md + .yaml frontmatter)
2. committed to: `cex/P04_execution/examples/p04_hookconf_{name}.md`
### I Signal
1. signal: complete (with quality score from QUALITY_GATES)
2. if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0).
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| hook-builder | Implements hooks declared by this config |
| quality-gate-builder | May bind quality-fail hooks |
| lifecycle-rule-builder | May bind archive/promote hooks |

## Properties

| Property | Value |
|----------|-------|
| Kind | `collaboration` |
| Pillar | P12 |
| Domain | hook config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[hook-config-builder]] | upstream | 0.49 |
| [[bld_collaboration_hook]] | sibling | 0.48 |
| [[bld_collaboration_retriever_config]] | sibling | 0.46 |
| [[bld_examples_hook_config]] | upstream | 0.43 |
| [[bld_collaboration_builder]] | sibling | 0.42 |
| [[bld_collaboration_lifecycle_rule]] | sibling | 0.40 |
| [[hook-builder]] | upstream | 0.40 |
| [[bld_collaboration_quality_gate]] | sibling | 0.39 |
| [[p03_sp_hook_config_builder]] | upstream | 0.39 |
| [[bld_collaboration_memory_scope]] | sibling | 0.39 |
