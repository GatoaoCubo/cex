---
id: p12_wf_research_nucleus
kind: workflow
pillar: P12
version: "1.0.0"
created: "2023-10-10"
updated: "2023-10-10"
author: "workflow-builder"
title: "Research Nucleus Workflow"
steps_count: 3
execution: mixed
satellites: [sat_research_1, sat_analysis_1]
timeout: 7200
retry_policy: per_step
depends_on: []
signals: [complete, error]
spawn_configs: [p12_spawn_research, p12_spawn_analysis]
domain: "orchestration"
quality: null
tags: [workflow, research, orchestration]
tldr: "3-step mixed workflow: research, analysis, synthesis"
density_score: 0.92
---

## Purpose
Orchestrates a research-oriented mission where initial data is collected, analyzed, and then synthesized into a comprehensive report. The steps are organized to maximize efficiency by combining parallel data gathering with sequential analysis and reporting.

## Steps
### Step 1: collect_data [sat_research_1]
- **Agent**: sat_research_1
- **Action**: Gather data from predefined sources
- **Input**: Source list from initial setup
- **Output**: Raw data files
- **Signal**: collect_data_complete
- **Depends on**: none

### Step 2: analyze_data [sat_analysis_1]
- **Agent**: sat_analysis_1
- **Action**: Analyze collected data for insights
- **Input**: Raw data files from collect_data
- **Output**: Analyzed insights document
- **Signal**: analyze_data_complete
- **Depends on**: Step 1

### Step 3: synthesize_report [sat_analysis_1]
- **Agent**: sat_analysis_1
- **Action**: Generate final research report from insights
- **Input**: Analyzed insights document
- **Output**: Final report
- **Signal**: synthesize_report_complete
- **Depends on**: Step 2

## Dependencies
- Initial setup completed with source list available for sat_research_1
- spawn_configs for sat_research_1 and sat_analysis_1 should be valid

## Signals
- **On step complete**: {step}_complete signal emitted by satellite
- **On workflow complete**: workflow_complete signal with report quality
- **On error**: {step}_error signal, retry on step (max 2), escalate if persistent

## References
- Signal Builder conventions for complete/error signals
- Spawn Config Builder for satellite configurations