---
id: p01_kc_orchestration_runtime
kind: knowledge_card
type: domain
pillar: P01
title: "Orchestration Runtime — DAGs, Spawn Configs, Schedules, RAG Sources"
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: orchestration_runtime
origin: manual
quality: 9.1
tags: [orchestration, dag, spawn, schedule, rag, runtime, airflow, prefect, cron]
tldr: "Orchestration runtime covers DAG-based workflow execution, process spawning, cron scheduling, and external knowledge source management for agent systems"
when_to_use: "Designing multi-step workflows, spawning agent_group processes, scheduling recurring tasks, or managing RAG knowledge sources"
keywords: [dag, spawn-config, schedule, rag-source, orchestration, airflow, prefect, cron, workflow]
long_tails:
  - "How to model multi-agent workflows as DAGs with dependency resolution and failure handling"
  - "Which patterns govern agent_group spawn configuration and cron-based task scheduling"
axioms:
  - "DAGs are the universal workflow primitive — every multi-step process can be modeled as a directed acyclic graph"
  - "Spawn configs are declarative — they describe WHAT to run, not HOW to run it (runtime resolves the how)"
linked_artifacts:
  primary: null
  related: [p01_kc_infra_config, p01_kc_routing_resilience, p01_kc_a2a_protocol]
feeds_kinds:
  - dag              # Directed acyclic graphs for workflow execution with dependency edges
  - spawn_config     # Process spawn declarations: agent_group, model, MCP profile, flags
  - schedule         # Cron expressions, interval triggers, calendar-aware scheduling
  - rag_source       # External knowledge source definitions: URL, scrape config, refresh policy
density_score: 0.89
---

# Orchestration Runtime

## Quick Reference
```yaml
topic: Orchestration Runtime (DAGs, spawns, schedules, RAG sources)
scope: Workflow execution, process spawning, task scheduling, knowledge source management
source: manual (Airflow, Prefect, organization spawn system, RAG pipelines)
criticality: high
```

## Key Concepts

| Concept | Domain | CEX Kind | Role |
|---------|--------|----------|------|
| Workflow DAG | Execution | dag | Directed graph of tasks with dependency edges and failure modes |
| Spawn Config | Process Mgmt | spawn_config | Declarative agent_group/agent spawn: model, MCP, flags, timeout |
| Schedule | Timing | schedule | Cron/interval triggers with calendar awareness and timezone |
| RAG Source | Knowledge | rag_source | External data source with scrape config, refresh policy, format |

## DAG Patterns

```text
[TASK_A] -> [TASK_B] -> [TASK_D]
    \                      /
     -> [TASK_C] ---------
```

| Pattern | Description | Use Case |
|---------|-------------|----------|
| Sequential | A -> B -> C (linear chain) | Step-by-step processing |
| Fan-out | A -> {B, C, D} (parallel) | Independent subtasks |
| Fan-in | {B, C, D} -> E (join) | Aggregate parallel results |
| Diamond | A -> {B, C} -> D | Parallel with sync point |
| Conditional | A -> B if condition else C | Branch on result |

## Spawn Config Structure

```yaml
agent_group: builder_agent
model: opus
mcp_profile: .mcp-edison.json
flags: [--dangerously-skip-permissions, --no-chrome, -p]
timeout: 3600
handoff: .claude/handoffs/MISSION_edison.md
prompt_max_chars: 200
spawn_delay: 5s
max_concurrent: 3
```

## Schedule Patterns

| Type | Expression | Example |
|------|-----------|---------|
| Cron | `0 9 * * 1-5` | Weekdays at 9am |
| Interval | `every 30m` | Every 30 minutes |
| Calendar | `first Monday of month` | Monthly maintenance |
| Event-driven | `on signal:complete` | After agent_group signals done |
| Dependency | `after DAG:extract completes` | Chained DAG execution |

## RAG Source Definition

```yaml
source_id: src_framework_taxonomy
url: "https://docs.example.com/api"
scrape_method: firecrawl    # firecrawl | static | api
format: markdown            # markdown | json | html
refresh_policy:
  interval: 7d
  on_change: true
  stale_after: 30d
budget_per_scrape: 3        # Firecrawl credits
topics: [langchain, llamaindex]
```

## Patterns

| Trigger | Action |
|---------|--------|
| Multi-agent_group mission | Create `dag` with agent_group tasks as nodes, dependencies as edges |
| Launch agent_group | Resolve `spawn_config` to command: model, MCP, flags, handoff path |
| Recurring maintenance | Define `schedule` with cron expression, timezone, and failure policy |
| New knowledge source | Register `rag_source` with URL, scrape method, refresh interval |
| DAG task fails | Check retry policy, execute fallback branch, or mark DAG as partial |
| Source becomes stale | Trigger re-scrape based on `refresh_policy.stale_after` threshold |

## Anti-Patterns

- Cyclic dependencies in DAGs (deadlocks — validate acyclicity before execution)
- Spawn configs with hardcoded paths (breaks across environments — use path_config)
- Schedules without timezone awareness (cron in UTC but expecting BRT)
- RAG sources without staleness checks (serving outdated knowledge as current)
- Missing failure modes in DAG nodes (one failure cascades to entire workflow)
- Spawning > 3 concurrent agent_groups (BSOD risk on Windows — enforce max_concurrent)

## organization Integration

| Component | Role | Kind |
|-----------|------|------|
| spawn_grid.ps1 | Multi-agent_group DAG execution | dag + spawn_config |
| spawn_solo.ps1 | Single agent_group spawn | spawn_config |
| spawn_monitor.ps1 | DAG progress tracking | dag |
| signal_writer.py | Node completion signals | dag |
| Firecrawl integration | RAG source scraping | rag_source |
| orchestrator dispatch | DAG composition from user request | dag + spawn_config |
| continuous_batching | Auto-refill slots from queue | dag + schedule |

## References

- related: p01_kc_infra_config, p01_kc_a2a_protocol, p01_kc_routing_resilience
- patterns: Airflow, Prefect, organization spawn system, Firecrawl, orchestrator dispatch
