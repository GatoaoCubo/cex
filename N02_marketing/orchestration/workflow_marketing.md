---
id: p12_wf_marketing_campaign
kind: workflow
pillar: P12
version: "1.0.0"
created: "2023-10-18"
updated: "2023-10-18"
author: "workflow-builder"
title: "Marketing Campaign Execution"
steps_count: 4
execution: mixed
satellites: [marketing_manager, content_creator, data_analyst, campaign_coordinator]
timeout: 720000
retry_policy: per_step
depends_on: []
signals: [campaign_complete, campaign_error]
spawn_configs: [p12_spawn_marketing_manager, p12_spawn_content_creation, p12_spawn_data_analysis, p12_spawn_campaign_coordination]
domain: "marketing"
quality: null
tags: [workflow, campaign, execution]
tldr: "4-step mixed workflow: content creation, analysis, execution, and evaluation for a marketing campaign."
density_score: 0.95
---

## Purpose
This workflow orchestrates a marketing campaign execution involving content creation, data analysis, campaign execution, and post-campaign evaluation. It ensures collaborative execution by different agents while handling dependencies and ensuring efficient execution.

## Steps
### Step 1: Create Content [content_creator]
- **Agent**: content_creator
- **Action**: Develop marketing content for the campaign
- **Input**: Campaign brief from marketing_manager
- **Output**: Published content in content repository
- **Signal**: content_creation_complete
- **Depends on**: none (first step)

### Step 2: Analyze Market Data [data_analyst]
- **Agent**: data_analyst
- **Action**: Analyze market data and audience trends
- **Input**: Market data feed
- **Output**: Market insights report
- **Signal**: data_analysis_complete
- **Depends on**: none (independent step)

### Step 3: Execute Campaign [campaign_coordinator]
- **Agent**: campaign_coordinator
- **Action**: Execute marketing campaign using created content
- **Input**: Published content, market insights report
- **Output**: Campaign performance metrics
- **Signal**: campaign_execution_complete
- **Depends on**: Steps 1, 2

### Step 4: Evaluate Campaign [marketing_manager]
- **Agent**: marketing_manager
- **Action**: Evaluate campaign performance and generate report
- **Input**: Campaign performance metrics
- **Output**: Campaign evaluation report
- **Signal**: campaign_evaluation_complete
- **Depends on**: Step 3

## Dependencies
- Campaign brief must be available before the workflow starts
- All required agents must be properly spawned with referenced configurations

## Signals
- **On step complete**: {step}_complete signal emitted by respective agent (see signal-builder)
- **On workflow complete**: campaign_complete signal emitted
- **On error**: {step}_error signal emitted, retry per step (max 2), then escalate to orchestrator for resolution

## References
- Signal Builder for signal conventions
- Spawn Config Builder for satellite configurations