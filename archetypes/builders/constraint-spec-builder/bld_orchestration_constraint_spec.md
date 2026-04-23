---
kind: collaboration
id: bld_collaboration_constraint_spec
pillar: P12
llm_function: COLLABORATE
purpose: How constraint-spec-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Constraint Spec"
version: "1.0.0"
author: n03_builder
tags: [constraint_spec, builder, examples]
tldr: "Golden and anti-examples for constraint spec construction, demonstrating ideal structure and common pitfalls."
domain: "constraint spec construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_prompt_version
  - bld_collaboration_output_validator
  - constraint-spec-builder
  - bld_collaboration_memory_scope
  - bld_collaboration_retriever_config
  - bld_collaboration_action_prompt
  - bld_collaboration_system_prompt
  - bld_collaboration_builder
  - p10_lr_constraint_spec_builder
  - bld_collaboration_handoff_protocol
---

# Collaboration: constraint-spec-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what are the parameters and constraints for this constraint spec?"
I specify constraint spec configurations so agents and pipelines can use them.
## Crew Compositions
### Crew: "Structured Generation"
```
  1. constraint-spec-builder -> decode constraint
  2. prompt-template-builder -> prompt with constraint
  3. output-validator-builder -> post-gen validation
```
### Crew: "Prompt Engineering"
```
  1. constraint-spec-builder -> output constraint
  2. system-prompt-builder -> agent identity
  3. prompt-version-builder -> version tracking
```

## Handoff Protocol
### I Receive
1. seeds: constraint spec purpose, target system, constraints
2. optional: specific parameter values, upstream artifact references
### I Produce
1. constraint_spec artifact (.md + .yaml frontmatter)
2. committed to: `cex/P03_prompt/examples/p03_constraint_{name}.md`
### I Signal
1. signal: complete (with quality score from QUALITY_GATES)
2. if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0).
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| prompt-template-builder | Downstream consumer |
| output-validator-builder | Downstream consumer |

## Properties

| Property | Value |
|----------|-------|
| Kind | `collaboration` |
| Pillar | P12 |
| Domain | constraint spec construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_prompt_version]] | sibling | 0.62 |
| [[bld_collaboration_output_validator]] | sibling | 0.62 |
| [[constraint-spec-builder]] | upstream | 0.52 |
| [[bld_collaboration_memory_scope]] | sibling | 0.41 |
| [[bld_collaboration_retriever_config]] | sibling | 0.40 |
| [[bld_collaboration_action_prompt]] | sibling | 0.40 |
| [[bld_collaboration_system_prompt]] | sibling | 0.39 |
| [[bld_collaboration_builder]] | sibling | 0.39 |
| [[p10_lr_constraint_spec_builder]] | upstream | 0.39 |
| [[bld_collaboration_handoff_protocol]] | sibling | 0.39 |
