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
