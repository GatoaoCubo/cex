---
kind: quality_gate
id: p01_qg_ecommerce_vertical
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for ecommerce_vertical
quality: null
title: "Quality Gate Ecommerce Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [ecommerce_vertical, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for ecommerce_vertical"
domain: "ecommerce_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
(Table: metric, threshold, operator, scope)  
| metric | threshold | operator | scope |  
|---|---|---|---|  
| checkout_success_rate | 95% | >= | all |  
| pci_compliance_status | 100% | == | all |  
| fraud_detection_rate | 90% | >= | all |  
| recommendation_accuracy | 85% | >= | all |  
| use_case_coverage | 100% | == | all |  

## HARD Gates  
(Table: ID | Check | Fail Condition)  
| ID | Check | Fail Condition |  
|---|---|---|  
| H01 | YAML frontmatter valid | invalid YAML syntax |  
| H02 | ID matches ^p01_ev_[a-z][a-z0-9_]+.md$ | invalid schema ID pattern |  
| H03 | kind field matches 'ecommerce_vertical' | kind field mismatch |  
| H04 | PCI-DSS compliance achieved | PCI-DSS audit fails |  
| H05 | checkout latency <= 2s | latency exceeds 2s |  
| H06 | fraud detection rate >= 90% | rate below 90% |  
| H07 | recommendation engine accuracy >= 85% | accuracy below 85% |  
| H08 | use case coverage == 100% | missing use cases |  

## SOFT Scoring  
(Table: Dim | Dimension | Weight | Scoring Guide)  
| Dim | Dimension | Weight | Scoring Guide |  
|---|---|---|---|  
| D01 | Checkout experience | 0.15 | 1.0 = seamless, 0.0 = broken |  
| D02 | Security (PCI-DSS) | 0.20 | 1.0 = fully compliant, 0.0 = non-compliant |  
| D03 | Fraud prevention | 0.15 | 1.0 = 100% detection, 0.0 = 0% detection |  
| D04 | Recommendation quality | 0.15 | 1.0 = 100% accuracy, 0.0 = 0% accuracy |  
| D05 | Use case coverage | 0.10 | 1.0 = 100% coverage, 0.0 = 0% coverage |  
| D06 | Performance (latency) | 0.10 | 1.0 = <=2s, 0.0 = >5s |  
| D07 | Error rate | 0.15 | 1.0 = 0% errors, 0.0 = >5% errors |  

## Actions  
(Table: Score | Action)  
| Score | Action |  
|---|---|  
| GOLDEN | >=9.5 | Auto-approve and deploy |  
| PUBLISH | >=8.0 | Publish with no changes |  
| REVIEW | >=7.0 | Manual review required |  
| REJECT | <7.0 | Reject and fix |  

## Bypass  
(Table: conditions, approver, audit trail)  
| conditions | approver | audit trail |  
|---|---|---|  
| Critical bug fix | CTO | documented in JIRA |  
| Regulatory override | CISO | signed waiver |  
| Performance exception | CPO | load test report |
