---
kind: collaboration
id: bld_collaboration_cohort_analysis
pillar: P12
llm_function: COLLABORATE
purpose: How cohort_analysis-builder works in crews with other builders
quality: 8.9
title: "Collaboration Cohort Analysis"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [cohort_analysis, builder, collaboration]
tldr: "How cohort_analysis-builder works in crews with other builders"
domain: "cohort_analysis construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_collaboration_subscription_tier
  - bld_collaboration_reward_model
  - bld_collaboration_integration_guide
  - bld_collaboration_reranker_config
  - bld_collaboration_eval_metric
  - bld_collaboration_white_label_config
  - bld_collaboration_agentic_rag
  - bld_collaboration_sandbox_spec
  - bld_collaboration_product_tour
  - bld_collaboration_ab_test_config
---

## Crew Role  
Defines and analyzes user cohorts to identify trends and patterns, providing actionable insights for product and marketing teams.  

## Receives From  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Data Warehouse| Raw user event data   | CSV/Parquet |  
| Product Team  | Cohort definition rules | JSON      |  
| Analyst       | Analysis parameters   | SQL         |  

## Produces For  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Product Team  | Cohort trend reports  | PDF/Excel   |  
| Marketing Team| Engagement metrics    | JSON        |  
| Data Team     | Visualization assets  | PNG         |  

## Boundary  
Does NOT handle model evaluation (benchmark-builder) or billing data (usage_report-builder). Data pipeline issues are handled by data engineering.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_subscription_tier]] | sibling | 0.35 |
| [[bld_collaboration_reward_model]] | sibling | 0.34 |
| [[bld_collaboration_integration_guide]] | sibling | 0.33 |
| [[bld_collaboration_reranker_config]] | sibling | 0.31 |
| [[bld_collaboration_eval_metric]] | sibling | 0.30 |
| [[bld_collaboration_white_label_config]] | sibling | 0.30 |
| [[bld_collaboration_agentic_rag]] | sibling | 0.30 |
| [[bld_collaboration_sandbox_spec]] | sibling | 0.29 |
| [[bld_collaboration_product_tour]] | sibling | 0.29 |
| [[bld_collaboration_ab_test_config]] | sibling | 0.28 |
