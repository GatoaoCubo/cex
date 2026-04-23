---
kind: collaboration
id: bld_collaboration_output_validator
pillar: P12
llm_function: COLLABORATE
purpose: How output-validator-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Output Validator"
version: "1.0.0"
author: n03_builder
tags: [output_validator, builder, examples]
tldr: "Golden and anti-examples for output validator construction, demonstrating ideal structure and common pitfalls."
domain: "output validator construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_constraint_spec
  - bld_collaboration_validation_schema
  - bld_collaboration_retriever_config
  - output-validator-builder
  - bld_collaboration_memory_scope
  - bld_collaboration_prompt_version
  - bld_collaboration_builder
  - bld_collaboration_golden_test
  - bld_collaboration_handoff_protocol
  - bld_collaboration_quality_gate
---

# Collaboration: output-validator-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what are the parameters and constraints for this output validator?"
I specify output validator configurations so agents and pipelines can use them.
## Crew Compositions
### Crew: "Validation Pipeline"
```
  1. constraint-spec-builder -> decode constraint
  2. output-validator-builder -> post-gen validation
  3. quality-gate-builder -> scoring
```
### Crew: "Output Quality"
```
  1. output-validator-builder -> structural validation
  2. formatter-builder -> output formatting
  3. parser-builder -> output extraction
```

## Handoff Protocol
### I Receive
1. seeds: output validator purpose, target system, constraints
2. optional: specific parameter values, upstream artifact references
### I Produce
1. output_validator artifact (.md + .yaml frontmatter)
2. committed to: `cex/P05_output/examples/p05_oval_{name}.md`
### I Signal
1. signal: complete (with quality score from QUALITY_GATES)
2. if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
| constraint-spec-builder | Upstream dependency |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| quality-gate-builder | Downstream consumer |
| formatter-builder | Downstream consumer |

## Properties

| Property | Value |
|----------|-------|
| Kind | `collaboration` |
| Pillar | P12 |
| Domain | output validator construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_constraint_spec]] | sibling | 0.52 |
| [[bld_collaboration_validation_schema]] | sibling | 0.44 |
| [[bld_collaboration_retriever_config]] | sibling | 0.44 |
| [[output-validator-builder]] | upstream | 0.43 |
| [[bld_collaboration_memory_scope]] | sibling | 0.42 |
| [[bld_collaboration_prompt_version]] | sibling | 0.42 |
| [[bld_collaboration_builder]] | sibling | 0.41 |
| [[bld_collaboration_golden_test]] | sibling | 0.40 |
| [[bld_collaboration_handoff_protocol]] | sibling | 0.39 |
| [[bld_collaboration_quality_gate]] | sibling | 0.38 |
