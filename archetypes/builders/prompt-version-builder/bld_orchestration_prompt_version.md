---
kind: collaboration
id: bld_collaboration_prompt_version
pillar: P12
llm_function: COLLABORATE
purpose: How prompt-version-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Prompt Version"
version: "1.0.0"
author: n03_builder
tags: [prompt_version, builder, examples]
tldr: "Golden and anti-examples for prompt version construction, demonstrating ideal structure and common pitfalls."
domain: "prompt version construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - prompt-version-builder
  - bld_collaboration_action_prompt
  - bld_collaboration_constraint_spec
  - bld_collaboration_prompt_template
  - bld_collaboration_golden_test
  - bld_collaboration_output_validator
  - bld_collaboration_memory_scope
  - bld_collaboration_retriever_config
  - bld_collaboration_system_prompt
  - bld_collaboration_response_format
---

# Collaboration: prompt-version-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what are the parameters and constraints for this prompt version?"
I specify prompt version configurations so agents and pipelines can use them.
## Crew Compositions
### Crew: "Prompt Lifecycle"
```
  1. prompt-template-builder -> mutable template
  2. prompt-version-builder -> immutable snapshot
  3. few-shot-example-builder -> examples
```
### Crew: "Prompt Optimization"
```
  1. prompt-version-builder -> version tracking
  2. constraint-spec-builder -> output constraints
  3. e2e-eval-builder -> version evaluation
```

## Handoff Protocol
### I Receive
1. seeds: prompt version purpose, target system, constraints
2. optional: specific parameter values, upstream artifact references
### I Produce
1. prompt_version artifact (.md + .yaml frontmatter)
2. committed to: `cex/P03_prompt/examples/p03_pv_{name}.md`
### I Signal
1. signal: complete (with quality score from QUALITY_GATES)
2. if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
| prompt-template-builder | Upstream dependency |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| e2e-eval-builder | Downstream consumer |
| smoke-eval-builder | Downstream consumer |

## Properties

| Property | Value |
|----------|-------|
| Kind | `collaboration` |
| Pillar | P12 |
| Domain | prompt version construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[prompt-version-builder]] | upstream | 0.50 |
| [[bld_collaboration_action_prompt]] | sibling | 0.50 |
| [[bld_collaboration_constraint_spec]] | sibling | 0.49 |
| [[bld_collaboration_prompt_template]] | sibling | 0.44 |
| [[bld_collaboration_golden_test]] | sibling | 0.43 |
| [[bld_collaboration_output_validator]] | sibling | 0.41 |
| [[bld_collaboration_memory_scope]] | sibling | 0.41 |
| [[bld_collaboration_retriever_config]] | sibling | 0.41 |
| [[bld_collaboration_system_prompt]] | sibling | 0.40 |
| [[bld_collaboration_response_format]] | sibling | 0.39 |
