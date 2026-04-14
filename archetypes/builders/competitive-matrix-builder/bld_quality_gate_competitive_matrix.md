---
kind: quality_gate
id: p01_qg_competitive_matrix
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for competitive_matrix
quality: null
title: "Quality Gate Competitive Matrix"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [competitive_matrix, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for competitive_matrix"
domain: "competitive_matrix construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
(Table: metric, threshold, operator, scope)  
- metric: completeness, threshold: 100%, operator: >=, scope: all features  
- metric: accuracy, threshold: 95%, operator: >=, scope: data sources  

## HARD Gates  
(Table: ID | Check | Fail Condition)  
H01: YAML frontmatter valid  
H02: ID matches pattern ^p01_cm_[a-z][a-z0-9_]+.md$  
H03: kind field matches 'competitive_matrix'  
H04: All competitors listed in matrix  
H05: Data sources cited and up-to-date  
H06: Metrics aligned with business goals  
H07: Matrix consistent across departments  
H08: Clear differentiation vs. competitors  

## SOFT Scoring  
(Table: Dim | Dimension | Weight | Scoring Guide)  
Dim1: Completeness | 0.15 | 100% coverage  
Dim2: Accuracy | 0.15 | 95%+ verified data  
Dim3: Relevance | 0.10 | 80%+ aligned to use cases  
Dim4: Clarity | 0.10 | 90%+ understandable  
Dim5: Differentiation | 0.15 | 85%+ unique value  
Dim6: Strategy alignment | 0.10 | 90%+ aligned to goals  
Dim7: Usability | 0.10 | 85%+ actionable  
Dim8: Consistency | 0.15 | 95%+ cross-departmental  

## Actions  
(Table: Score | Action)  
GOLDEN: >=9.5 | Auto-publish  
PUBLISH: >=8.0 | Review by PM  
REVIEW: >=7.0 | Flag for QA  
REJECT: <7.0 | Revise and resubmit  

## Bypass  
(Table: conditions, approver, audit trail)  
- conditions: Urgent business need, approver: CTO, audit trail: email log
