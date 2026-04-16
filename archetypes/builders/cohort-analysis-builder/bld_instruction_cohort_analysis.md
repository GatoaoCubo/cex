---
kind: instruction
id: bld_instruction_cohort_analysis
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for cohort_analysis
quality: 8.9
title: "Instruction Cohort Analysis"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [cohort_analysis, builder, instruction]
tldr: "Step-by-step production process for cohort_analysis"
domain: "cohort_analysis construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Define retention cohort criteria (e.g., user acquisition date, engagement thresholds).  
2. Identify data sources for user behavior (e.g., CRM, app analytics, transaction logs).  
3. Determine LTV modeling variables (e.g., revenue per user, churn rate, cohort size).  
4. Perform exploratory analysis to detect anomalies in cohort survival curves.  
5. Validate alignment with business KPIs (e.g., 30-day retention, 12-month LTV).  
6. Document assumptions and edge cases (e.g., overlapping cohorts, missing data).  

## Phase 2: COMPOSE  
1. Align artifact structure with bld_schema_cohort_analysis.md (cohort definition, metrics, methodology).
2. Specify cohort parameters (e.g., start date, segmentation rules).
3. Write objective section: "Measure retention and LTV for [product/service] users."
4. Detail data pipeline: ETL steps for cohort identification and metric aggregation.
5. Populate survival analysis section with formulae (e.g., retention rate = active / total).
6. Embed LTV calculation logic (e.g., CLV = average revenue x retention period).
7. Reference bld_output_template_cohort_analysis.md for visualization placement (e.g., cohort heatmaps).
8. Add governance controls: data quality checks, cohort validation rules.
9. Finalize with appendices: schema diagrams, data dictionary, and calculation proofs.

## Phase 3: VALIDATE
- [ ] [OK] Cohort definitions match bld_schema_cohort_analysis.md and business requirements
- [ ] [OK] Retention/LTV metrics align with domain-specific KPIs
- [ ] [OK] Survival curves and LTV projections pass statistical validity tests
- [ ] [OK] Visualizations (heatmaps, trend lines) reflect accurate data transformations
- [ ] [OK] Artifact complies with governance standards (data provenance, audit trails)
