---
kind: quality_gate
id: p01_qg_govtech_vertical
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for govtech_vertical
quality: null
title: "Quality Gate Govtech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [govtech_vertical, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for govtech_vertical"
domain: "govtech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
(Table: metric, threshold, operator, scope)  
| metric | threshold | operator | scope |  
|---|---|---|---|  
| Govtech compliance | 100% | = | System |  

## HARD Gates  
(Table: ID | Check | Fail Condition)  
| ID | Check | Fail Condition |  
|---|---|---|  
| H01 | YAML frontmatter valid | Invalid YAML syntax |  
| H02 | ID matches pattern ^p01_gv_[a-z][a-z0-9_]+.md$ | Invalid schema ID |  
| H03 | kind field matches 'govtech_vertical' | Incorrect kind value |  
| H04 | FedRAMP compliance achieved | Missing FedRAMP authorization |  
| H05 | FISMA compliance achieved | Missing FISMA certification |  
| H06 | CJIS compliance achieved | Data handling fails CJIS standards |  
| H07 | Section 508 accessibility met | Non-compliant UI/UX elements |  
| H08 | GSA approval secured | No GSA contract alignment |  

## SOFT Scoring  
(Table: Dim | Dimension | Weight | Scoring Guide)  
| Dim | Dimension | Weight | Scoring Guide |  
|---|---|---|---|  
| D01 | FedRAMP alignment | 0.20 | 1.0 = full compliance |  
| D02 | FISMA alignment | 0.15 | 1.0 = full compliance |  
| D03 | CJIS alignment | 0.15 | 1.0 = full compliance |  
| D04 | Section 508 alignment | 0.10 | 1.0 = full compliance |  
| D05 | GSA alignment | 0.15 | 1.0 = approved use case |  
| D06 | Use case coverage | 0.10 | 1.0 = 100% use case met |  
| D07 | Data encryption | 0.10 | 1.0 = AES-256 applied |  
| D08 | Audit trail completeness | 0.15 | 1.0 = full traceability |  

## Actions  
(Table: Score | Action)  
| Score | Action |  
|---|---|  
| >=9.5 | GOLDEN: Deploy immediately |  
| >=8.0 | PUBLISH: Release with no changes |  
| >=7.0 | REVIEW: QA review required |  
| <7.0 | REJECT: Major fixes required |  

## Bypass  
(Table: conditions, approver, audit trail)  
| conditions | approver | audit trail |  
|---|---|---|  
| Emergency use case | CIO | Bypass logged with justification |
