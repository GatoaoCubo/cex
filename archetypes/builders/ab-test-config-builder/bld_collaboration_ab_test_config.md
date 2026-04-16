---
kind: collaboration
id: bld_collaboration_ab_test_config
pillar: P12
llm_function: COLLABORATE
purpose: How ab_test_config-builder works in crews with other builders
quality: 8.9
title: "Collaboration Ab Test Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [ab_test_config, builder, collaboration]
tldr: "How ab_test_config-builder works in crews with other builders"
domain: "ab_test_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role  
Creates and validates A/B test configurations, ensuring alignment with testing goals, statistical rigor, and technical feasibility.  

## Receives From  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Product Owner | Test hypotheses       | JSON        |  
| Data Scientist| User segment criteria | CSV         |  
| Engineer      | Technical constraints | YAML        |  

## Produces For  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| QA Team       | A/B test config file  | JSON        |  
| Analytics Team| Validation report     | Markdown    |  
| Deployment Team| Test plan            | YAML        |  

## Boundary  
Does NOT handle feature flag toggles (use `feature_flag_builder`) or ML experiment configs (use `experiment_config_builder`). Deployment and monitoring are handled by deployment and analytics teams.
