---
id: p01_kc_workflow_orchestration
kind: knowledge_card
type: domain
pillar: P01
title: "Workflow Orchestration Framework"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: frameworks
quality: 8.6
tags: [framework, architecture, llm]
tldr: "How to sequence multi-step workflows: DAG dependencies, wave execution, signal-based coordination, error handling."
keywords: [orchestration, workflow, dag, sequencing, dependencies]
density_score: 0.92
---

# Workflow Orchestration Framework

## Orchestration Patterns
| Pattern | Description |
|---------|-------------|
| Sequential | A → B → C (each waits for previous) |
| Parallel | A + B + C (no dependencies) |
| Wave | Group 1 (parallel) → Group 2 (parallel) → ... |
| DAG | Arbitrary dependencies, topological sort |
| Event-driven | Signal triggers next step |

## CEX Orchestration
- /plan: creates DAG of tasks with dependencies
- /grid: executes waves (parallel groups)
- Signals: event-driven coordination between nuclei
- Handoffs: structured task delegation
- Manifest: shared decisions across all tasks

## Error in Orchestration
If step fails: retry → fallback → skip (if optional) → abort wave → escalate
Never let one failure cascade to unrelated steps.
