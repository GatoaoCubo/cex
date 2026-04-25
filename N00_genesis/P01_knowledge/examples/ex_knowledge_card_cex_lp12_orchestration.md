---
id: p01_kc_cex_lp12_orchestration
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX LP12 Orchestration — Multi-Agent Coordination Mechanics"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.2
tags: [cex, lp12, orchestration, workflow, spawn, signal, handoff, crew]
tldr: "P12 defines 7 types of multi-agent coordination: workflow, dag, spawn_config, signal, handoff, dispatch_rule, crew"
when_to_use: "Understand how isolated LLM agents become a coordinated system"
keywords: [orchestration, workflow, dag, spawn, signal, handoff, dispatch, crew]
long_tails:
  - "How to coordinate multiple LLM agents in a unified system"
  - "What is the difference between workflow and dag in CEX P12"
axioms:
  - "ALWAYS use handoff to transfer context between agents"
  - "NEVER spawn agent without explicit spawn_config"
linked_artifacts:
  primary: p01_kc_cex_lp11_feedback
  related: [p01_kc_cex_lp08_architecture]
density_score: null
data_source: "https://arxiv.org/abs/2308.08155"
related:
  - p01_kc_lp12_orchestration
  - p01_kc_cex_function_collaborate
  - handoff-builder
  - handoff-protocol-builder
  - bld_architecture_handoff
  - bld_collaboration_handoff
  - p01_kc_handoff
  - bld_collaboration_handoff_protocol
  - bld_collaboration_workflow
  - workflow-builder
---

## Quick Reference

topic: P12 Orchestration | scope: multi-agent coordination | criticality: high
types: 7 | function: COLLABORATE + PRODUCE + GOVERN | layer: runtime + spec

## Key Concepts

- P12 is the conductor: isolated agents become an orchestra
- workflow defines sequential or parallel steps of agents
- dag models an acyclic dependency graph between tasks
- spawn_config defines how to execute (solo, grid, continuous)
- signal communicates simple events between agents (complete)
- handoff transfers task + context + commit between agents
- dispatch_rule routes keyword > agent_group automatically
- crew defines a multi-agent group with coordination protocol
- AutoGen has GroupChat; CrewAI has Crew; MetaGPT has Env
- CEX crew unifies these concepts into a formal type
- workflow is NOT chain (P03, prompt sequence)
- signal is NOT handoff (simple event vs instruction)
- dispatch_rule is NOT router (P02, task > model routing)
- P12 orchestrates all other LPs in execution
- P12 depends on P02: identity defines who participates
- P12 uses P04: communication mechanisms are tools
- P12 is governed by P07: coordination quality is measured
- Dominant function: COLLABORATE (coordination between agents)

## Phases

1. Map available agents and their domains (P02)
2. Define dispatch_rules for automatic routing
3. Create spawn_configs per mode (solo, grid, continuous)
4. Design workflows for recurring flows
5. Implement signals and handoffs for communication
6. Compose crews for complex multi-agent missions

## Golden Rules

- ALWAYS use handoff (not signal) to transfer tasks
- NEVER spawn without spawn_config (avoid implicit defaults)
- ALWAYS define crew protocol before joint execution
- NEVER mix workflow with dag (execution vs dependency)
- ALWAYS include commit instruction in handoff

## Comparison

| Type | Nature | Scope | Example |
|------|--------|-------|---------|
| workflow | Execution | Sequential steps | Research pipeline |
| dag | Dependency | Acyclic graph | Task dependency graph |
| spawn_config | Infra | Execution mode | Solo, grid, continuous |
| signal | Event | Between 2 agents | complete, error, progress |
| handoff | Instruction | Complete task | Handoff with context+commit |
| dispatch_rule | Routing | Keyword > sat | "research" > research_agent |
| crew | Group | N agents | Team of 3 agent_groups |

## Flow

```
[P12: Orchestration Layer]
         |
    +----+----+----+----+----+----+
    |    |    |    |    |    |    |
   wf  dag spawn sig  ho   dr  crew
    |    |    |    |    |    |    |
    v    v    v    v    v    v    v
 [PRODUCE] [GOVERN] [COLLABORATE]
    |         |           |
    v         v           v
 executes   configures   communicates
    |         |           |
    +----+----+-----------+
         |
         v
  [coordinated agents]
         |
         v
  [P07 evals measure quality]
```

## References

- source: https://arxiv.org/abs/2308.08155
- source: https://arxiv.org/abs/2303.17760
- related: p01_kc_cex_lp11_feedback
- related: p01_kc_cex_lp08_architecture

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_lp12_orchestration]] | sibling | 0.45 |
| [[p01_kc_cex_function_collaborate]] | sibling | 0.40 |
| [[handoff-builder]] | downstream | 0.29 |
| [[handoff-protocol-builder]] | downstream | 0.29 |
| [[bld_architecture_handoff]] | downstream | 0.27 |
| [[bld_collaboration_handoff]] | downstream | 0.27 |
| [[p01_kc_handoff]] | sibling | 0.27 |
| [[bld_collaboration_handoff_protocol]] | downstream | 0.27 |
| [[bld_collaboration_workflow]] | downstream | 0.27 |
| [[workflow-builder]] | downstream | 0.26 |
