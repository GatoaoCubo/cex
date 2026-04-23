---
kind: collaboration
id: bld_collaboration_usage_report
pillar: P12
llm_function: COLLABORATE
purpose: How usage_report-builder works in crews with other builders
quality: 8.9
title: "Collaboration Usage Report"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [usage_report, builder, collaboration]
tldr: "How usage_report-builder works in crews with other builders"
domain: "usage_report construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_collaboration_cohort_analysis
  - bld_collaboration_action_paradigm
  - bld_collaboration_agentic_rag
  - bld_config_usage_report
  - bld_collaboration_dataset_card
  - usage-report-builder
  - p03_sp_usage_report_builder
  - bld_collaboration_app_directory_entry
  - bld_collaboration_experiment_tracker
  - bld_collaboration_content_filter
---

## Crew Role  
Aggregates, normalizes, and formats usage analytics data into actionable reports for stakeholders. Focuses on query patterns, resource consumption, and user activity metrics.  

## Receives From  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Data Collector| Raw usage logs        | JSON        |  
| API Gateway   | Request metadata      | Protobuf    |  
| Analytics DB  | Pre-aggregated metrics| Parquet     |  

## Produces For  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Dashboard     | Interactive reports   | HTML/JS     |  
| BI Tool       | Exported datasets     | CSV         |  
| Alert System  | Anomaly summaries     | JSON        |  

## Boundary  
Does NOT enforce cost limits (handled by cost_analyzer) or configure telemetry (handled by trace_collector). Excludes infrastructure health or error tracking.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_cohort_analysis]] | sibling | 0.26 |
| [[bld_collaboration_action_paradigm]] | sibling | 0.26 |
| [[bld_collaboration_agentic_rag]] | sibling | 0.25 |
| [[bld_config_usage_report]] | upstream | 0.25 |
| [[bld_collaboration_dataset_card]] | sibling | 0.25 |
| [[usage-report-builder]] | upstream | 0.25 |
| [[p03_sp_usage_report_builder]] | upstream | 0.25 |
| [[bld_collaboration_app_directory_entry]] | sibling | 0.24 |
| [[bld_collaboration_experiment_tracker]] | sibling | 0.24 |
| [[bld_collaboration_content_filter]] | sibling | 0.24 |
