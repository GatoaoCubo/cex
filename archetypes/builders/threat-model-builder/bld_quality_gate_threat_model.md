---
kind: quality_gate
id: p11_qg_threat_model
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for threat_model
quality: null
title: "Quality Gate Threat Model"
version: "1.0.0"
author: wave1_builder_gen
tags: [threat_model, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for threat_model"
domain: "threat_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Definition  
| metric | threshold | operator | scope |  
|---|---|---|---|  
| completeness | 90% | >= | AI system's attack surface |  

## HARD Gates  
| ID | Check | Fail Condition |  
|---|---|---|  
| H01 | YAML valid | Invalid syntax or structure |  
| H02 | ID matches pattern | ID does not follow `THREAT-XXXX` format |  
| H03 | kind matches | `threat_model` not specified |  
| H04 | Risk categories defined | Missing critical, high, medium, low |  
| H05 | Threat actors identified | No explicit threat actor enumeration |  
| H06 | Mitigation strategies present | Missing or incomplete mitigation plans |  
| H07 | Validation method documented | No peer review or simulation evidence |  

## SOFT Scoring  
| Dim | Dimension | Weight | Scoring Guide |  
|---|---|---|---|  
| D1 | Completeness | 0.15 | 100% coverage = 1.0 |  
| D2 | Depth | 0.15 | Detailed analysis = 1.0 |  
| D3 | Clarity | 0.10 | Unambiguous language = 1.0 |  
| D4 | Alignment with standards | 0.10 | ISO/IEC 23894 compliance = 1.0 |  
| D5 | Threat actor coverage | 0.10 | All relevant actors = 1.0 |  
| D6 | Mitigation effectiveness | 0.10 | Feasible and actionable = 1.0 |  
| D7 | Validation | 0.10 | Peer-reviewed = 1.0 |  
| D8 | Documentation | 0.10 | Full traceability = 1.0 |  

## Actions  
| Score | Action |  
|---|---|  
| GOLDEN | >=9.5 | Approve and deploy |  
| PUBLISH | >=8.0 | Peer review required |  
| REVIEW | >=7.0 | Revisions mandatory |  
| REJECT | <7.0 | Discard and rework |  

## Bypass  
| conditions | approver | audit trail |  
|---|---|---|  
| Emergency fix required | CTO | Log entry with timestamp |  
| Legacy system exemption | CTO | Legacy system approval form |
