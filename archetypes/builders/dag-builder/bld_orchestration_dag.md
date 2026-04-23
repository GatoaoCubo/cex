---
kind: collaboration
id: bld_collaboration_dag
pillar: P12
llm_function: COLLABORATE
purpose: How dag-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Dag"
version: "1.0.0"
author: n03_builder
tags: [dag, builder, examples]
tldr: "Golden and anti-examples for dag construction, demonstrating ideal structure and common pitfalls."
domain: "dag construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_dispatch_rule
  - bld_architecture_dag
  - bld_collaboration_handoff
  - bld_collaboration_component_map
  - dag-builder
  - bld_collaboration_builder
  - bld_collaboration_signal
  - bld_collaboration_workflow
  - bld_collaboration_golden_test
  - bld_collaboration_handoff_protocol
---

# Collaboration: dag-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what depends on what, and in what order can tasks execute?"
I do not execute tasks. I do not define routing policies.
I model dependency structures so orchestrators can determine execution order and parallelism.
## Crew Compositions
### Crew: "Orchestration Design"
```
  1. component-map-builder -> "system component inventory"
  2. dag-builder -> "dependency graph with topological order"
  3. dispatch-rule-builder -> "routing rules for each node"
  4. handoff-builder -> "delegation instructions per task"
```
### Crew: "Pipeline Architecture"
```
  1. dag-builder -> "execution dependency graph"
  2. chain-builder -> "prompt chains for sequential nodes"
  3. e2e-eval-builder -> "end-to-end test of the full pipeline"
```
## Handoff Protocol
### I Receive
- seeds: task list with dependency relationships
- optional: parallelism hints, critical path constraints, timeout per node
### I Produce
- dag artifact (.yaml with nodes, edges, topological order)
- committed to: `cex/P12/examples/p12_dag_{scope}.yaml`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- component-map-builder: provides component inventory to model as DAG nodes
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| dispatch-rule-builder | Routes tasks to targets based on DAG position |
| handoff-builder | Creates delegation for each DAG node |
| e2e-eval-builder | Tests pipeline following DAG execution order |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_dispatch_rule]] | sibling | 0.52 |
| [[bld_architecture_dag]] | upstream | 0.48 |
| [[bld_collaboration_handoff]] | sibling | 0.48 |
| [[bld_collaboration_component_map]] | sibling | 0.46 |
| [[dag-builder]] | related | 0.45 |
| [[bld_collaboration_builder]] | sibling | 0.41 |
| [[bld_collaboration_signal]] | sibling | 0.41 |
| [[bld_collaboration_workflow]] | sibling | 0.39 |
| [[bld_collaboration_golden_test]] | sibling | 0.37 |
| [[bld_collaboration_handoff_protocol]] | sibling | 0.37 |
