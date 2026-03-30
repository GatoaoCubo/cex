---
id: p12_wf_knowledge_nucleus
kind: workflow
pillar: P12
version: "1.0.0"
created: "2023-10-10"
updated: "2023-10-10"
author: "workflow-builder"
title: "Knowledge Nucleus Workflow"
steps_count: 3
execution: mixed
agent_nodes: [oracle, curator]
timeout: 600000
retry_policy: per_step
depends_on: []
signals: [complete, error]
spawn_configs: [p12_spawn_oracle_insight, p12_spawn_curator_compile]
domain: "knowledge_management"
quality: null
tags: [workflow, knowledge_management, multi_agent]
tldr: "Orchestrates a multi-agent system to gather, analyze, and compile knowledge into actionable insights."
density_score: 0.95
---

## Purpose
This workflow orchestrates the asynchronous gathering of knowledge, curation of insights, and compilation of reports. It uses a multi-agent system to explore, analyze, and document knowledge resources, enhancing efficiency in information management tasks.

## Steps

### Step 1: Gather Insights [oracle]
- **Agent**: oracle
- **Action**: Explore various knowledge resources to gather relevant data.
- **Input**: Knowledge resource list.
- **Output**: Collection of data entries stored in the temporary database.
- **Signal**: oracle_complete
- **Depends on**: none

### Step 2: Analyze Data [curator]
- **Agent**: curator
- **Action**: Inspect the collected data entries and analyze for actionable insights.
- **Input**: Data entries from the temporary database.
- **Output**: Analyzed insights ready for report compilation.
- **Signal**: curator_complete
- **Depends on**: Step 1

### Step 3: Compile Report [oracle]
- **Agent**: oracle
- **Action**: Compile analyzed insights into a cohesive report.
- **Input**: Insights analyzed by curator.
- **Output**: Finalized report stored in the central repository.
- **Signal**: report_complete
- **Depends on**: Step 2

## Dependencies
- Appropriate data connection to the temporary database must be established.
- Verified access to knowledge resources for the oracle.

## Signals
- **On step complete**: Each agent emits a complete signal upon finishing their step (e.g., oracle_complete, curator_complete, report_complete).
- **On workflow complete**: report_complete signal with cumulative quality score.
- **On error**: Emit error signal, retry each step up to max retries (2), then escalate to orchestrator.

## References
- Signal-builder for completion and error signals.
- Spawn-config-builder for agent_node launch configurations.