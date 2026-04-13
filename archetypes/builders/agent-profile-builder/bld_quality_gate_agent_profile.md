---
kind: quality_gate
id: p02_qg_agent_profile
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for agent_profile
quality: null
title: "Quality Gate Agent Profile"
version: "1.0.0"
author: wave1_builder_gen
tags: [agent_profile, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for agent_profile"
domain: "agent_profile construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Definition  
(Table: metric, threshold, operator, scope)  
| Metric | Threshold | Operator | Scope |  
|---|---|---|---|  
| Completeness of agent persona | 100% | = | agent_profile |  

## HARD Gates  
(Table: ID | Check | Fail Condition)  
| ID | Check | Fail Condition |  
|---|---|---|  
| H01 | YAML valid | Invalid YAML syntax |  
| H02 | ID matches pattern | ID does not conform to `agent-[a-z0-9]{8}` |  
| H03 | kind matches | kind is not `agent_profile` |  
| H04 | Persona defined | Missing `persona` field |  
| H05 | Identity method specified | Missing `identity_construction_method` |  
| H06 | ID uniqueness | Duplicate ID in scope |  
| H07 | Kind validity | Kind not in allowed enum |  
| H08 | Required fields present | Missing `name`, `role`, `credentials` |  
| H09 | Data source valid | Invalid `data_source` reference |  
| H10 | Consistency check | Mismatch between `persona` and `role` |  

## SOFT Scoring  
(Table: Dim | Dimension | Weight | Scoring Guide)  
| Dim | Dimension | Weight | Scoring Guide |  
|---|---|---|---|  
| D01 | Completeness | 0.15 | 100% complete = 1.0 |  
| D02 | Consistency | 0.15 | No contradictions = 1.0 |  
| D03 | Uniqueness | 0.10 | Unique ID = 1.0 |  
| D04 | Validity | 0.10 | All fields valid = 1.0 |  
| D05 | Clarity | 0.10 | Clear persona description = 1.0 |  
| D06 | Policy alignment | 0.10 | Aligns with CEX policies = 1.0 |  
| D07 | Data source reliability | 0.10 | Trusted source = 1.0 |  
| D08 | Scalability | 0.05 | Supports future expansion = 1.0 |  
| D09 | Usability | 0.05 | Easy to interpret = 1.0 |  

## Actions  
(Table: Score | Action)  
| Score | Action |  
|---|---|  
| GOLDEN | >=9.5 | Auto-approve for production |  
| PUBLISH | >=8.0 | Deploy to staging |  
| REVIEW | >=7.0 | Request manual review |  
| REJECT | <7.0 | Block deployment |  

## Bypass  
(Table: conditions, approver, audit trail)  
| Conditions | Approver | Audit Trail |  
|---|---|---|  
| Urgent deployment required | Senior Manager | Requires written approval and timestamp |
