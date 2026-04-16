---
kind: quality_gate
id: p05_qg_integration_guide
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for integration_guide
quality: 8.9
title: "Quality Gate Integration Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [integration_guide, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for integration_guide"
domain: "integration_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
(Table: metric, threshold, operator, scope)  
metric | threshold | operator | scope  
--- | --- | --- | ---  
Completeness | 100% | equals | all platform partners  

## HARD Gates  
(Table: ID | Check | Fail Condition)  
ID | Check | Fail Condition  
--- | --- | ---  
H01 | YAML frontmatter valid | invalid YAML syntax  
H02 | ID matches pattern ^p05_ig_[a-z][a-z0-9_]+.md$ | invalid filename pattern  
H03 | kind field matches 'integration_guide' | incorrect kind value  
H04 | API endpoint coverage ≥ 95% | missing critical endpoints  
H05 | Error handling examples ≥ 3 | insufficient error scenarios  
H06 | Authentication methods ≥ 2 | missing required auth protocols  
H07 | Sample code in ≥ 2 languages | no code examples  
H08 | Versioning documented | no versioning info  
H09 | Partner onboarding steps ≥ 5 | incomplete onboarding process  
H10 | Compliance info (KYC/AML) included | missing regulatory details  

## SOFT Scoring  
(Table: Dim | Dimension | Weight | Scoring Guide)  
Dim | Dimension | Weight | Scoring Guide  
--- | --- | --- | ---  
D01 | Clarity | 0.15 | 1.0 (clear) to 0.0 (ambiguous)  
D02 | Completeness | 0.15 | 1.0 (full) to 0.0 (incomplete)  
D03 | Technical accuracy | 0.15 | 1.0 (correct) to 0.0 (errors)  
D04 | Compliance alignment | 0.10 | 1.0 (compliant) to 0.0 (non-compliant)  
D05 | Usability | 0.10 | 1.0 (user-friendly) to 0.0 (poor)  
D06 | Code example quality | 0.10 | 1.0 (working) to 0.0 (non-functional)  
D07 | Partner onboarding flow | 0.10 | 1.0 (smooth) to 0.0 (broken)  
D08 | Versioning clarity | 0.10 | 1.0 (clear) to 0.0 (confusing)  
D09 | Language support | 0.05 | 1.0 (≥3 languages) to 0.0 (none)  

## Actions  
(Table: Score | Action)  
Score | Action  
--- | ---  
GOLDEN | ≥9.5 | Auto-publish and notify partners  
PUBLISH | ≥8.0 | Publish to platform  
REVIEW | ≥7.0 | Flag for QA review  
REJECT | <7.0 | Reject and request revisions  

## Bypass  
(Table: conditions, approver, audit trail)  
conditions | approver | audit trail  
--- | --- | ---  
Urgent partner request | CTO | ticket #12345  
Regulatory exception | Legal team | legal review #67890
