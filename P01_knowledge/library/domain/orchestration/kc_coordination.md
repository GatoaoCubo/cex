---
id: p01_kc_coordination
kind: knowledge_card
type: domain
pillar: P01
title: "Multi-Agent Coordination Patterns"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: orchestration
quality: 9.1
tags: [coordination, multi-agent, orchestration, consensus, handoff]
tldr: "How multiple LLM agents coordinate: orchestrator pattern, blackboard, market-based, pipeline, consensus. CEX uses orchestrator (N07) + shared filesystem."
when_to_use: "Designing systems where multiple agents must work together on shared goals"
keywords: [coordination, multi-agent, orchestrator, blackboard, pipeline]
density_score: 0.93
updated: "2026-04-07"
---

# Multi-Agent Coordination

## Patterns

| Pattern | How | Best For |
|---------|-----|----------|
| **Orchestrator** | Central agent delegates and collects | Clear hierarchy, sequential deps |
| **Blackboard** | Shared state, agents read/write freely | Collaborative, loosely coupled |
| **Pipeline** | Output of agent A → input of agent B | Linear workflows |
| **Market** | Agents bid on tasks, best fit wins | Large task pools, many agents |
| **Consensus** | Agents vote on decisions | High-stakes, need agreement |

## CEX Architecture: Orchestrator + Blackboard Hybrid
- **N07** = orchestrator (plans, dispatches, monitors)
- **Filesystem** = blackboard (`.cex/runtime/`, `P01_knowledge/`)
- **Signals** = coordination primitive (signal_writer.py)
- **Handoffs** = structured task delegation
- **Decision Manifest** = shared decisions

## Coordination Primitives
1. **Signal**: "I'm done, quality X" (async notification)
2. **Handoff**: "Here's your task + context" (structured delegation)
3. **Manifest**: "User decided X, Y, Z" (shared decisions)
4. **Brand config**: "We all speak this voice" (shared identity)

## Retrieval Example

```yaml
# Query this card via cex_retriever.py
query: "Multi-Agent Coordination Patterns"
kind_filter: knowledge_card
threshold: 0.7
```

```bash
# CLI retrieval
python _tools/cex_retriever.py "Multi-Agent Coordination Patterns" --top 5
```

## Quality Criteria

| Dimension | Requirement | Weight |
|-----------|------------|--------|
| Factual accuracy | Verifiable claims only | 0.25 |
| Atomicity | One concept per card | 0.20 |
| Actionability | Reader knows next steps | 0.20 |
| Density | No filler sentences | 0.20 |
| Searchability | Tags enable retrieval | 0.15 |
