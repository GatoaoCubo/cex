---
kind: collaboration
id: bld_collaboration_spawn_config
pillar: P12
llm_function: COLLABORATE
purpose: How spawn-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Spawn Config"
version: "1.0.0"
author: n03_builder
tags: [spawn_config, builder, examples]
tldr: "Golden and anti-examples for spawn config construction, demonstrating ideal structure and common pitfalls."
domain: "spawn config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_workflow
  - bld_architecture_spawn_config
  - spawn-config-builder
  - bld_collaboration_agent_card
  - workflow-builder
  - bld_collaboration_system_prompt
  - bld_knowledge_card_spawn_config
  - bld_collaboration_builder
  - p11_qg_spawn_config
  - bld_collaboration_validation_schema
---

# Collaboration: spawn-config-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how should this agent_group be spawned, with what flags and settings?"
I configure CLI flags, MCP profiles, timeout policies, prompt sizing, and handoff file references for automated agent_group launch. I do NOT design what happens after spawn (workflow-builder), emit runtime signals (signal-builder), or write the task instructions the agent_group receives.
## Crew Compositions
### Crew: "Multi-Agent_group Mission Setup"
```
  1. workflow-builder -> "defines which agent_groups run, in what order, with what dependencies"
  2. spawn-config-builder -> "produces spawn_config for each agent_group referenced in the workflow"
  3. signal-builder -> "defines completion/error signals emitted at the end of each agent_group run"
```
### Crew: "New Agent_group Onboarding"
```
  1. system-prompt-builder -> "defines the agent_group identity, rules, and response format"
  2. spawn-config-builder -> "produces the spawn_config: mode, flags, MCP profile, timeout"
  3. validation-schema-builder -> "enforces the spawn_config output contract post-generation"
```
## Handoff Protocol
### I Receive
- seeds: agent_group name, spawn mode (solo/grid/continuous), task domain description
- optional: timeout override, interactive flag, handoff file path, MCP requirements, model preference
### I Produce
- spawn_config artifact (YAML, frontmatter 19 fields, max 120 lines)
- committed to: `cex/P12_orchestration/examples/p12_spawn_{mode_slug}.yaml`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- None. spawn-config is infrastructure-level and requires no upstream builder artifacts.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| workflow-builder | references spawn_config per agent_group step to know how to launch each agent |
| validation-schema-builder | may enforce spawn_config field contracts post-generation |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_workflow]] | sibling | 0.64 |
| [[bld_architecture_spawn_config]] | upstream | 0.50 |
| [[spawn-config-builder]] | related | 0.49 |
| [[bld_collaboration_agent_card]] | sibling | 0.48 |
| [[workflow-builder]] | related | 0.43 |
| [[bld_collaboration_system_prompt]] | sibling | 0.39 |
| [[bld_knowledge_card_spawn_config]] | related | 0.39 |
| [[bld_collaboration_builder]] | sibling | 0.38 |
| [[p11_qg_spawn_config]] | related | 0.38 |
| [[bld_collaboration_validation_schema]] | sibling | 0.38 |
