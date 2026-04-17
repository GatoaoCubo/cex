---
kind: collaboration
id: bld_collaboration_prospective_memory
pillar: P12
llm_function: COLLABORATE
purpose: How prospective-memory-builder works in crews with other builders
quality: null
title: "Collaboration Prospective Memory"
version: "1.0.0"
author: n03_builder
tags: [prospective_memory, builder, collaboration]
tldr: "prospective-memory-builder provides future-action stores for agent crews."
domain: "prospective memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
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
