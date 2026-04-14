---
kind: quality_gate
id: p11_qg_ab_test_config
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for ab_test_config
quality: null
title: "Quality Gate Ab Test Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [ab_test_config, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for ab_test_config"
domain: "ab_test_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
| metric | threshold | operator | scope |  
|---|---|---|---|  
| Config validity | 100% | == | All fields |  

## HARD Gates  
| ID | Check | Fail Condition |  
|---|---|---|  
| H01 | YAML frontmatter valid | Missing or invalid YAML frontmatter |  
| H02 | ID matches pattern ^p11_abt_[a-z][a-z0-9_]+.yaml$ | ID does not conform to schema |  
| H03 | kind field matches 'ab_test_config' | kind field is incorrect |  
| H04 | experiment_name present | Missing experiment_name |  
| H05 | variant_groups defined with ≥2 variants | <2 variants or invalid structure |  
| H06 | metrics defined with valid types (e.g., conversion_rate) | Missing or invalid metric types |  
| H07 | duration ≥ 7 days | Duration <7 days |  
| H08 | traffic_split percentages sum to 100% | Sum ≠ 100% or negative values |  

## SOFT Scoring  
| Dim | Dimension | Weight | Scoring Guide |  
|---|---|---|---|  
| D1 | Objective clarity | 0.15 | Clear, measurable goals (1.0) |  
| D2 | Statistical power | 0.12 | ≥80% power (1.0) |  
| D3 | Sample size | 0.10 | Adequate for confidence (1.0) |  
| D4 | Variant alignment | 0.15 | Variants logically distinct (1.0) |  
| D5 | Metric relevance | 0.10 | Metrics directly tied to goals (1.0) |  
| D6 | Duration合理性 | 0.10 | Aligns with business cycle (1.0) |  
| D7 | Rollout strategy | 0.10 | Safe, reversible (1.0) |  
| D8 | Audit trail completeness | 0.18 | Full approval history (1.0) |  

## Actions  
| Score | Action |  
|---|---|  
| ≥9.5 | GOLDEN: Auto-publish |  
| ≥8.0 | PUBLISH: Deploy |  
| ≥7.0 | REVIEW: QA check |  
| <7.0 | REJECT: Fix required |  

## Bypass  
| conditions | approver | audit trail |  
|---|---|---|  
| Emergency fix | Senior PM + Data Scientist | "Bypassed due to critical issue" |
