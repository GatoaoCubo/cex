---
id: p12_wf_york_commercial_nucleus
kind: workflow
pillar: P12
version: "1.0.0"
created: "2023-10-15"
updated: "2023-10-15"
author: "workflow-engineer"
title: "York Commercial Nucleus Workflow"
steps_count: 3
execution: mixed
satellites: [sat_york_a, sat_york_b]
timeout: 600000
retry_policy: per_step
depends_on: []
signals: [complete, error]
spawn_configs: [p12_spawn_york_a, p12_spawn_york_b]
domain: "commercial"
quality: null
tags: [workflow, york, commercial]
tldr: "A workflow orchestrating the York Commercial nucleus with sequential and parallel steps."
density_score: 0.88
---
## Purpose
This workflow orchestrates the York Commercial nucleus by coordinating tasks that involve both sequential and parallel execution steps. It aims to optimize execution time and efficiency while handling error recovery gracefully.

## Steps
### Step 1: Prepare Report [sat_york_a]
- **Agent**: sat_york_a
- **Action**: Assemble sales data and prepare an initial report
- **Input**: Raw data from sales database
- **Output**: Initial sales report
- **Signal**: report_prepared
- **Depends on**: none

### Step 2: Analyze Data [sat_york_b]
- **Agent**: sat_york_b
- **Action**: Perform detailed analysis on the prepared report
- **Input**: Initial sales report from Step 1
- **Output**: Analytical insights
- **Signal**: data_analyzed
- **Depends on**: Step 1

### Step 3: Consolidate Findings [sat_york_a]
- **Agent**: sat_york_a
- **Action**: Consolidate insights into a comprehensive report
- **Input**: Analytical insights from Step 2
- **Output**: Comprehensive commercial report
- **Signal**: findings_consolidated
- **Depends on**: Step 2

## Dependencies
- Access to sales database must be ensured before step execution
- Valid spawn configurations referenced

## Signals
- **On step complete**: A relevant step completion signal is emitted by the corresponding agent (see signal-builder)
- **On workflow complete**: A final workflow_complete signal
- **On error**: Emission of error signal, with per-step retry policy (max 2)

## References
- Signal Builder: archetypes/builders/signal-builder/
- Spawn Config Builder: archetypes/builders/spawn-config-builder/
---
