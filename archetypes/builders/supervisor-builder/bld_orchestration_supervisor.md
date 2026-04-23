---
kind: collaboration
id: bld_collaboration_supervisor
pillar: P12
llm_function: COLLABORATE
purpose: How supervisor-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Supervisor"
version: "1.0.0"
author: n03_builder
tags: [supervisor, builder, examples]
tldr: "Golden and anti-examples for supervisor construction, demonstrating ideal structure and common pitfalls."
domain: "supervisor construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_director_builder
  - supervisor-builder
  - bld_collaboration_dispatch_rule
  - bld_architecture_supervisor
  - bld_collaboration_builder
  - p11_qg_director
  - bld_collaboration_agent
  - bld_collaboration_workflow
  - bld_instruction_supervisor
  - bld_architecture_kind
---

# Collaboration: supervisor-builder
## My Role in Crews
I am a COORDINATOR. I answer ONE question: "who are the builders, how are they dispatched, what signals are checked, and what happens on failure?"
I do not execute tasks. I do not produce content artifacts. I do not define builders.
I produce supervisor definitions so dispatch systems can coordinate multi-builder missions.
## Crew Compositions
### Crew: "Mission Planning End-to-End"
```
  1. knowledge-card-builder -> "domain knowledge for mission context"
  2. agent-builder -> "builder definitions (persona + capabilities)"
  3. supervisor-builder -> "orchestration plan (waves + dispatch + signals)"
  4. workflow-builder -> "execution sequence wrapping the supervisor"
  5. spawn-config-builder -> "provider-specific launch parameters"
```
### Crew: "Multi-Agent Dispatch Stack"
```
  1. supervisor-builder -> "coordination plan with wave topology"
  2. dispatch-rule-builder -> "routing rules for conditional dispatch"
  3. guardrail-builder -> "safety boundaries for orchestration behavior"
```
## Handoff Protocol
### I Receive
- seeds: mission goal, builder list, dependency map, dispatch preference (sequential/parallel)
- optional: existing wave topology draft, timeout values, fallback preferences
### I Produce
- supervisor artifact with wave topology, dispatch config, and fallback chains
- committed to: `P08_architecture/examples/ex_director_{topic}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- agent-builder: provides builder identities that the supervisor will dispatch
- knowledge-card-builder: provides domain context that shapes mission scope
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| workflow-builder | Wraps supervisor plan into executable workflow graph |
| spawn-config-builder | Needs dispatch targets and modes for launch config |
| handoff-builder | Creates per-builder handoff files from supervisor wave topology |
| signal-builder | Configures signal protocol matching supervisor expectations |
| interface-builder | Defines contracts between supervisor and dispatched builders |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_director_builder]] | upstream | 0.53 |
| [[supervisor-builder]] | upstream | 0.53 |
| [[bld_collaboration_dispatch_rule]] | sibling | 0.47 |
| [[bld_architecture_supervisor]] | upstream | 0.47 |
| [[bld_collaboration_builder]] | sibling | 0.45 |
| [[p11_qg_director]] | upstream | 0.43 |
| [[bld_collaboration_agent]] | sibling | 0.43 |
| [[bld_collaboration_workflow]] | sibling | 0.43 |
| [[bld_instruction_supervisor]] | upstream | 0.42 |
| [[bld_architecture_kind]] | upstream | 0.40 |
