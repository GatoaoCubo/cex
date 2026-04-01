---
id: p12_wf_intelligence_pipeline
kind: workflow
pillar: P12
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "workflow-builder"
title: "Intelligence Pipeline Workflow"
steps_count: 5
execution: mixed
agent_nodes: [shaka, edison, maxwell, tesla]
timeout: 7200
retry_policy: per_step
depends_on: []
signals: [collection_complete, analysis_complete, synthesis_complete, report_complete, pipeline_complete, error]
spawn_configs: [p12_spawn_shaka_research, p12_spawn_edison_analysis, p12_spawn_maxwell_synthesis, p12_spawn_tesla_reporting]
domain: "intelligence"
quality: 8.7
tags: [workflow, intelligence, pipeline, research, analysis]
tldr: "5-step mixed intelligence workflow: parallel data collection, sequential analysis/synthesis, report generation with distribution"
density_score: 0.88
---
## Purpose
Orchestrates end-to-end intelligence gathering and processing pipeline. Wave 1 executes parallel data collection from multiple sources. Wave 2 performs sequential analysis, synthesis, and reporting. Designed for repeatable intelligence operations with quality gates at each stage.

## Steps

### Step 1: OSINT Collection [shaka]
- **Agent**: shaka (research specialist)
- **Action**: Gather open-source intelligence from web sources, databases, and public repositories
- **Input**: collection targets and keywords from mission brief
- **Output**: raw intelligence artifacts in records/intelligence/raw/
- **Signal**: osint_collection_complete
- **Depends on**: none

### Step 2: HUMINT Collection [edison]
- **Agent**: edison (analysis specialist)
- **Action**: Collect human intelligence through surveys, interviews, and social media analysis
- **Input**: target entities and contact lists from mission brief
- **Output**: human intelligence reports in records/intelligence/humint/
- **Signal**: humint_collection_complete
- **Depends on**: none

### Step 3: Technical Analysis [maxwell]
- **Agent**: maxwell (synthesis specialist)
- **Action**: Analyze collected intelligence for patterns, threats, and opportunities
- **Input**: raw intelligence from Steps 1-2
- **Output**: analysis reports with confidence scores in records/intelligence/analysis/
- **Signal**: technical_analysis_complete
- **Depends on**: Step 1, Step 2

### Step 4: Intelligence Synthesis [tesla]
- **Agent**: tesla (reporting specialist)
- **Action**: Synthesize analysis into actionable intelligence briefings
- **Input**: analysis reports from Step 3
- **Output**: executive briefings and recommendation documents
- **Signal**: intelligence_synthesis_complete
- **Depends on**: Step 3

### Step 5: Distribution [shaka]
- **Agent**: shaka (research specialist)
- **Action**: Package and distribute intelligence products to stakeholders
- **Input**: synthesized intelligence from Step 4
- **Output**: distributed reports via secure channels, archive copies
- **Signal**: pipeline_complete
- **Depends on**: Step 4

## Dependencies
- Mission brief with collection targets, keywords, and stakeholder list must exist
- Access credentials for OSINT sources and databases required
- Secure distribution channels configured and tested
- Intelligence classification guidelines and handling procedures established

## Signals
- **On collection complete**: osint_collection_complete, humint_collection_complete signals from parallel collectors
- **On analysis complete**: technical_analysis_complete signal with quality metrics
- **On synthesis complete**: intelligence_synthesis_complete signal with briefing confidence scores
- **On pipeline complete**: pipeline_complete signal with distribution confirmation
- **On error**: collection_error, analysis_error, synthesis_error, or distribution_error with retry recommendations