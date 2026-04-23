---
quality: 8.2
quality: 7.8
kind: collaboration
id: bld_collaboration_prospective_memory
pillar: P12
llm_function: COLLABORATE
purpose: How prospective-memory-builder works in crews with other builders
title: "Collaboration Prospective Memory"
version: "1.0.0"
author: n03_builder
tags: [prospective_memory, builder, collaboration]
tldr: "prospective-memory-builder provides future-action stores for agent crews."
domain: "prospective memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_collaboration_memory_scope
  - bld_collaboration_memory_type
  - bld_collaboration_agent
  - bld_collaboration_schedule
  - memory-scope-builder
  - bld_collaboration_system_prompt
  - bld_collaboration_handoff_protocol
  - bld_manifest_memory_type
  - bld_collaboration_builder
  - bld_collaboration_boot_config
---

# Collaboration: prospective-memory-builder

## My Role in Crews
I store the FUTURE INTENTIONS of an agent -- what it commits to do later.
I do not schedule workflow jobs (that is schedule P12). I do not hold current task state (working_memory). I do not record what happened (episodic_memory).

## Crew Compositions

### Crew: "Agent Memory System"
```
  1. working-memory-builder -> "active task state"
  2. episodic-memory-builder -> "past interaction history"
  3. prospective-memory-builder -> "future action intentions"
  4. entity-memory-builder -> "persistent entity facts"
```

## Handoff Protocol

### I Receive
- seeds: owner agent/nucleus, list of future actions and their triggers

### I Produce
- prospective_memory artifact (.md)
- committed to: `N0x_{domain}/P10_memory/p10_pm_{scope}.md`

## Builders I Depend On
| Builder | Why |
|---------|-----|
| agent-builder | Agent definition declares which tools the action_payloads reference |
| episodic-memory-builder | Completed reminders are recorded as episodes |

## Conflict Resolution
| Scenario | Resolution |
|----------|-----------|
| prospective_memory vs schedule | prospective = agent intention. schedule = workflow config. Different pillars (P10 vs P12). |
| Future action vs current task | Future -> prospective_memory. Current -> working_memory. |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_memory_scope]] | sibling | 0.50 |
| [[bld_collaboration_memory_type]] | sibling | 0.40 |
| [[bld_collaboration_agent]] | sibling | 0.39 |
| [[bld_collaboration_schedule]] | sibling | 0.32 |
| [[memory-scope-builder]] | upstream | 0.30 |
| [[bld_collaboration_system_prompt]] | sibling | 0.30 |
| [[bld_collaboration_handoff_protocol]] | sibling | 0.29 |
| [[bld_manifest_memory_type]] | upstream | 0.29 |
| [[bld_collaboration_builder]] | sibling | 0.29 |
| [[bld_collaboration_boot_config]] | sibling | 0.29 |
