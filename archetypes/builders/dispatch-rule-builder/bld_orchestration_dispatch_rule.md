---
kind: collaboration
id: bld_collaboration_dispatch_rule
pillar: P12
llm_function: COLLABORATE
purpose: How dispatch-rule-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Dispatch Rule"
version: "1.0.0"
author: n03_builder
tags: [dispatch_rule, builder, examples]
tldr: "Golden and anti-examples for dispatch rule construction, demonstrating ideal structure and common pitfalls."
domain: "dispatch rule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_handoff
  - bld_collaboration_fallback_chain
  - bld_collaboration_handoff_protocol
  - bld_collaboration_router
  - dispatch-rule-builder
  - bld_collaboration_dag
  - bld_collaboration_signal
  - bld_collaboration_builder
  - bld_collaboration_component_map
  - bld_collaboration_memory_scope
---

# Collaboration: dispatch-rule-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "which target should receive this kind of task, and under what conditions?"
I do not execute tasks. I do not define handoff instructions.
I produce routing policies so orchestrators can dispatch work to the correct target.
## Crew Compositions
### Crew: "Full Dispatch Setup"
```
  1. dispatch-rule-builder -> "routing rules (keywords -> target -> fallback)"
  2. fallback-chain-builder -> "degradation path when primary target fails"
  3. dag-builder -> "execution order for multi-target dispatch"
  4. handoff-builder -> "delegation instructions for each target"
```
### Crew: "Routing Table Construction"
```
  1. component-map-builder -> "inventory of available targets"
  2. dispatch-rule-builder -> "routing rule per domain scope"
  3. interface-builder -> "contracts between router and targets"
```
## Handoff Protocol
### I Receive
- seeds: domain scope, target agent/service, keywords (5-12)
- optional: model preference, priority, confidence threshold, fallback target
### I Produce
- dispatch_rule artifact (.yaml frontmatter + .md body, max 3072 bytes)
- committed to: `cex/P12/examples/p12_dr_{scope}.yaml`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- component-map-builder: provides target inventory for routing decisions
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| handoff-builder | Creates delegation instructions for dispatched targets |
| fallback-chain-builder | Defines degradation when dispatch target fails |
| dag-builder | Models dispatch dependencies in execution graphs |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_handoff]] | sibling | 0.52 |
| [[bld_collaboration_fallback_chain]] | sibling | 0.49 |
| [[bld_collaboration_handoff_protocol]] | sibling | 0.45 |
| [[bld_collaboration_router]] | sibling | 0.44 |
| [[dispatch-rule-builder]] | related | 0.43 |
| [[bld_collaboration_dag]] | sibling | 0.42 |
| [[bld_collaboration_signal]] | sibling | 0.38 |
| [[bld_collaboration_builder]] | sibling | 0.38 |
| [[bld_collaboration_component_map]] | sibling | 0.38 |
| [[bld_collaboration_memory_scope]] | sibling | 0.38 |
