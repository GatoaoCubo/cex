---
kind: examples
id: bld_examples_collaboration_pattern
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of collaboration_pattern artifacts
quality: 9.1
title: "Examples Collaboration Pattern"
version: "1.0.0"
author: wave1_builder_gen
tags: [collaboration_pattern, builder, examples]
tldr: "Golden and anti-examples of collaboration_pattern artifacts"
domain: "collaboration_pattern construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example
```markdown
---
title: "Search and Rescue Coordination"
agents: [RescueBot, Mapper, CommandCenter]
topology: "Mesh"
---
**Coordination Rules**:
- RescueBot shares real-time sensor data with Mapper via a shared channel.
- Mapper updates the CommandCenter with terrain maps every 30s.
- CommandCenter broadcasts mission priorities to all agents using a priority queue.
**Communication Channels**:
- `sensor_data`: Bidirectional between RescueBot and Mapper.
- `map_updates`: Unidirectional from Mapper to CommandCenter.
- `mission_orders`: Broadcast from CommandCenter to all.
```

## Anti-Example 1: Workflow Confusion
```markdown
---
title: "Incorrect Workflow"
agents: [AgentA, AgentB]
topology: "Linear"
---
**Steps**:
1. AgentA performs task X.
2. AgentB performs task Y after receiving a signal from AgentA.
```
## Why it fails
This defines a *workflow* (sequential execution) rather than a *collaboration pattern*. It lacks structural rules for concurrent coordination and doesn't describe how agents interact beyond a linear handoff.

## Anti-Example 2: Missing Communication
```markdown
---
title: "Role List Only"
agents: [Harvester, Analyzer, Storage]
topology: "Unknown"
---
**Roles**:
- Harvester collects data.
- Analyzer processes data.
- Storage archives data.
```
## Why it fails
The example only lists agent roles without defining *how* they coordinate. No communication channels, synchronization rules, or structural topology are specified, making the pattern incomplete and unactionable.

## Properties

| Property | Value |
|----------|-------|
| Kind | `examples` |
| Pillar | P07 |
| Domain | collaboration_pattern construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
