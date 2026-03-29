---
id: p12_wf_shaka_research_nucleus
kind: workflow
pillar: P12
version: "1.0.0"
created: "2023-10-08"
updated: "2023-10-08"
author: "workflow-builder"
title: "Shaka Research Nucleus Workflow"
steps_count: 3
execution_mode: mixed
satellites: [shaka]
timeout_ms: 600000
retry_policy: per_step
depends_on: []
signals: [shaka_complete, shaka_error]
spawn_configs: [p12_spawn_shaka_solo_research]
domain: "orchestration"
quality: null
tags: [workflow, research, intelligence]
tldr: "3-step workflow for Shaka to conduct market intelligence research."
density_score: 0.92
---

## Purpose
This workflow orchestrates the Shaka Research Nucleus to collect and analyze market intelligence. The workflow organizes the research tasks into steps that deploy the Shaka agent to conduct research, analyze findings, and report results. These steps are designed to execute efficiently with a mix of parallel and sequential execution.

## Steps
### Step 1: collect_market_data [shaka]
- **Agent**: shaka
- **Action**: Gather market data using targeted web scraping tools.
- **Input**: Research brief providing data requirements and targets.
- **Output**: Raw data files stored in records/raw_data/.
- **Signal**: shaka_data_collected
- **Depends on**: none

### Step 2: analyze_collected_data [shaka]
- **Agent**: shaka
- **Action**: Analyze raw data using machine learning models for trend identification.
- **Input**: Raw data files from Step 1.
- **Output**: Analytical report summarizing trends and insights.
- **Signal**: shaka_analysis_complete
- **Depends on**: Step 1

### Step 3: report_results [shaka]
- **Agent**: shaka
- **Action**: Compile insights into a presentation-ready format for stakeholders.
- **Input**: Analytical report from Step 2.
- **Output**: Presentation file saved to reports/presentations/.
- **Signal**: shaka_report_complete
- **Depends on**: Step 2

## Dependencies
- Proper configuration of web scraping tools.
- Access to machine learning models for data analysis.

## Signals
- **On step complete**: shaka_complete signal emitted by each step upon successful completion.
- **On workflow complete**: shaka_report_complete indicates the entire workflow has successfully finished.
- **On error**: shaka_error signal emitted if any step encounters a failure, triggering a retry up to the maximum number allowed.