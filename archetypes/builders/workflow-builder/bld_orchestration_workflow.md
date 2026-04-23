---
kind: collaboration
id: bld_collaboration_workflow
pillar: P12
llm_function: COLLABORATE
purpose: How workflow-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Workflow"
version: "1.0.0"
author: n03_builder
tags: [workflow, builder, examples]
tldr: "Golden and anti-examples for workflow construction, demonstrating ideal structure and common pitfalls."
domain: "workflow construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - workflow-builder
  - bld_collaboration_spawn_config
  - bld_architecture_workflow
  - bld_collaboration_signal
  - p03_sp_workflow-builder
  - bld_knowledge_card_workflow
  - bld_collaboration_system_prompt
  - bld_memory_workflow
  - bld_collaboration_builder
  - bld_collaboration_agent_card
---

# Collaboration: workflow-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what agents run in what order, with what dependencies and signals?"
I design runtime orchestration: sequential and parallel steps, wave ordering, agent_group coordination, signal-based completion, and error recovery strategies. I do NOT handle prompt chaining (chain-builder), static dependency graphs without execution (dag-builder), or keyword routing (dispatch_rule-builder).
## Crew Compositions
### Crew: "Mission Planning"
```
  1. spawn-config-builder -> "produces spawn_config for each agent_group step in the workflow"
  2. signal-builder -> "defines completion/error signal schemas for each step"
  3. workflow-builder -> "assembles the runtime plan: steps, wave order, deps, recovery"
```
### Crew: "Full Dispatch Stack"
```
  1. system-prompt-builder -> "defines the identity of each agent that workflow steps invoke"
  2. spawn-config-builder -> "configures how each agent_group is launched per step"
  3. workflow-builder -> "composes the complete orchestration with agents, signals, and wave order"
```
## Handoff Protocol
### I Receive
- seeds: mission name, agent_group list, step descriptions, dependency constraints
- optional: spawn_config references, signal definitions, parallelism requirements, error recovery strategy
### I Produce
- workflow artifact (YAML frontmatter + markdown body, frontmatter 20 fields, max 150 lines)
- committed to: `cex/P12_orchestration/examples/p12_wf_{name_slug}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- spawn-config-builder: each agent_group step in the workflow references a spawn_config for launch parameters
- signal-builder: step completion events reference signal schemas to know what to emit and listen for
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| validation-schema-builder | workflow outputs may need post-generation schema enforcement |
| validator-builder | pre-commit validators check workflow structural correctness before execution |
| crew-builder | crew protocols may reference workflows as their execution plan |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[workflow-builder]] | related | 0.62 |
| [[bld_collaboration_spawn_config]] | sibling | 0.53 |
| [[bld_architecture_workflow]] | upstream | 0.46 |
| [[bld_collaboration_signal]] | sibling | 0.43 |
| [[p03_sp_workflow-builder]] | upstream | 0.43 |
| [[bld_knowledge_card_workflow]] | upstream | 0.39 |
| [[bld_collaboration_system_prompt]] | sibling | 0.39 |
| [[bld_memory_workflow]] | upstream | 0.39 |
| [[bld_collaboration_builder]] | sibling | 0.39 |
| [[bld_collaboration_agent_card]] | sibling | 0.38 |
