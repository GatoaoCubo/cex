---
id: p12_wf_lily_marketing_nucleus
kind: workflow
pillar: P12
version: "1.0.0"
created: "2023-10-01"
updated: "2023-10-01"
author: "workflow-builder"
title: "Lily Marketing Nucleus Workflow"
steps_count: 5
execution: mixed
satellites: [content_creator, strategist, analyst]
timeout: 600000
retry_policy: per_step
depends_on: []
signals: [complete, error]
spawn_configs: [p12_spawn_content_creator, p12_spawn_strategist, p12_spawn_analyst]
domain: "marketing"
quality: null
tags: [workflow, marketing, lily]
tldr: "5-step mixed workflow for orchestrating Lily Marketing Nucleus tasks."
density_score: 0.90
---
## Purpose
This workflow orchestrates the marketing processes for the Lily Marketing Nucleus, ensuring structured execution across content creation, strategy planning, and data analysis. It is designed to streamline marketing efforts by leveraging parallel and sequential task coordination.

## Steps

### Step 1: Create_Content [content_creator]
- **Agent**: Content Creator
- **Action**: Develop engaging content based on the marketing brief.
- **Input**: Marketing brief; audience data.
- **Output**: Draft content pieces.
- **Signal**: content_creation_complete
- **Depends on**: none

### Step 2: Plan_Strategy [strategist]
- **Agent**: Strategist
- **Action**: Formulate marketing strategy using received content.
- **Input**: Draft content from Step 1.
- **Output**: Marketing strategy document.
- **Signal**: strategy_planning_complete
- **Depends on**: Step 1

### Step 3: Analyze_Data [analyst]
- **Agent**: Analyst
- **Action**: Conduct data analysis to assess audience engagement.
- **Input**: Audience interaction metrics.
- **Output**: Audience analysis report.
- **Signal**: data_analysis_complete
- **Depends on**: none

### Step 4: Integrate_Insights [strategist]
- **Agent**: Strategist
- **Action**: Integrate analytical insights into strategy.
- **Input**: Marketing strategy document; audience analysis report.
- **Output**: Revised strategy with integrated insights.
- **Signal**: integration_complete
- **Depends on**: Steps 2, 3

### Step 5: Finalize_Campaign [orchestrator]
- **Agent**: Orchestrator
- **Action**: Finalize the marketing campaign and prepare for launch.
- **Input**: Revised strategy document.
- **Output**: Final campaign plan.
- **Signal**: workflow_complete
- **Depends on**: Step 4

## Dependencies
- Content creation is essential before strategy planning.
- Audience analysis must be conducted concurrently and integrated later.

## Signals
- **On step complete**: Specific signal emitted by the respective satellite (see signal-builder)
- **On workflow complete**: workflow_complete
- **On error**: Step-specific error signal, retry once, then escalate to orchestrator.

## References
- p12_spawn_content_creator
- p12_spawn_strategist
- p12_spawn_analyst
---
