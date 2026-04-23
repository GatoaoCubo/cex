---
kind: collaboration
id: bld_collaboration_competitive_matrix
pillar: P12
llm_function: COLLABORATE
purpose: How competitive_matrix-builder works in crews with other builders
quality: 8.9
title: "Collaboration Competitive Matrix"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [competitive_matrix, builder, collaboration]
tldr: "How competitive_matrix-builder works in crews with other builders"
domain: "competitive_matrix construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_collaboration_customer_segment
  - bld_collaboration_cohort_analysis
  - p02_agent_competitor_tracker
  - competitive-matrix-builder
  - bld_collaboration_compliance_framework
  - bld_collaboration_eval_metric
  - bld_collaboration_sales_playbook
  - bld_collaboration_discovery_questions
  - bld_collaboration_memory_benchmark
  - bld_collaboration_subscription_tier
---

## Crew Role  
Analyzes competitor data, structures features/benefits, and generates visual comparison matrices for strategic decision-making.  

## Receives From  
| Builder         | What               | Format     |  
|----------------|--------------------|------------|  
| market_research| Competitor list    | CSV        |  
| product_specs  | Feature definitions| JSON       |  
| sales_team     | Market trends      | API        |  

## Produces For  
| Builder         | What                  | Format     |  
|----------------|-----------------------|------------|  
| strategy_team  | Competitive matrix    | Markdown   |  
| product_team   | Gap analysis report   | PDF        |  
| sales_team     | Benchmarking data     | CSV        |  

## Boundary  
Does NOT handle customer segment analysis (ICP) or narrative content (pitch_deck). Handled by customer_segment_builder and pitch_deck_builder respectively.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_customer_segment]] | sibling | 0.40 |
| [[bld_collaboration_cohort_analysis]] | sibling | 0.26 |
| [[p02_agent_competitor_tracker]] | upstream | 0.24 |
| [[competitive-matrix-builder]] | upstream | 0.24 |
| [[bld_collaboration_compliance_framework]] | sibling | 0.24 |
| [[bld_collaboration_eval_metric]] | sibling | 0.24 |
| [[bld_collaboration_sales_playbook]] | sibling | 0.23 |
| [[bld_collaboration_discovery_questions]] | sibling | 0.23 |
| [[bld_collaboration_memory_benchmark]] | sibling | 0.23 |
| [[bld_collaboration_subscription_tier]] | sibling | 0.23 |
