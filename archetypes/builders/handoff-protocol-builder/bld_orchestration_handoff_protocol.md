---
kind: collaboration
id: bld_collaboration_handoff_protocol
pillar: P12
llm_function: COLLABORATE
purpose: How handoff-protocol-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Handoff Protocol"
version: "1.0.0"
author: n03_builder
tags: [handoff_protocol, builder, examples]
tldr: "Golden and anti-examples for handoff protocol construction, demonstrating ideal structure and common pitfalls."
domain: "handoff protocol construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - handoff-protocol-builder
  - bld_collaboration_memory_scope
  - bld_collaboration_handoff
  - bld_collaboration_dispatch_rule
  - bld_collaboration_retriever_config
  - bld_collaboration_agent
  - bld_collaboration_output_validator
  - bld_collaboration_prompt_version
  - bld_collaboration_builder
  - bld_config_handoff_protocol
---

# Collaboration: handoff-protocol-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what are the parameters and constraints for this handoff protocol?"
I specify handoff protocol configurations so agents and pipelines can use them.
## Crew Compositions
### Crew: "Multi-Agent System"
```
  1. handoff-protocol-builder -> inter-agent protocol
  2. agent-builder -> agent definitions
  3. router-builder -> task routing
```
### Crew: "Orchestration"
```
  1. handoff-protocol-builder -> handoff contracts
  2. dispatch-rule-builder -> keyword routing
  3. workflow-builder -> multi-step flows
```

## Handoff Protocol
### I Receive
1. seeds: handoff protocol purpose, target system, constraints
2. optional: specific parameter values, upstream artifact references
### I Produce
1. handoff_protocol artifact (.md + .yaml frontmatter)
2. committed to: `cex/P02_model/examples/p02_handoff_{name}.md`
### I Signal
1. signal: complete (with quality score from QUALITY_GATES)
2. if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
| agent-builder | Upstream dependency |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| workflow-builder | Downstream consumer |
| dispatch-rule-builder | Downstream consumer |

## Properties

| Property | Value |
|----------|-------|
| Kind | `collaboration` |
| Pillar | P12 |
| Domain | handoff protocol construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[handoff-protocol-builder]] | upstream | 0.59 |
| [[bld_collaboration_memory_scope]] | sibling | 0.50 |
| [[bld_collaboration_handoff]] | sibling | 0.50 |
| [[bld_collaboration_dispatch_rule]] | sibling | 0.47 |
| [[bld_collaboration_retriever_config]] | sibling | 0.46 |
| [[bld_collaboration_agent]] | sibling | 0.45 |
| [[bld_collaboration_output_validator]] | sibling | 0.44 |
| [[bld_collaboration_prompt_version]] | sibling | 0.44 |
| [[bld_collaboration_builder]] | sibling | 0.42 |
| [[bld_config_handoff_protocol]] | upstream | 0.39 |
