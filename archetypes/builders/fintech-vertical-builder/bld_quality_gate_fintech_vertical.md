---
kind: quality_gate
id: p01_qg_fintech_vertical
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for fintech_vertical
quality: null
title: "Quality Gate Fintech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [fintech_vertical, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for fintech_vertical"
domain: "fintech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
| metric | threshold | operator | scope |  
|---|---|---|---|  
| Fintech industry vertical | SOC2+PCI-DSS, KYC/AML, fraud detection, use cases | must meet | entire system |  

## HARD Gates  
| ID | Check | Fail Condition |  
|---|---|---|  
| H01 | YAML frontmatter valid | Invalid or missing YAML frontmatter |  
| H02 | ID matches pattern ^p01_fv_[a-z][a-z0-9_]+.md$ | ID does not conform to schema |  
| H03 | kind field matches 'fintech_vertical' | kind field is incorrect |  
| H04 | SOC2+PCI-DSS compliance | Missing or failed compliance audit |  
| H05 | KYC/AML processes implemented | No automated KYC/AML checks |  
| H06 | Fraud detection system active | Fraud detection module not deployed |  
| H07 | Data encryption at rest and in transit | Missing encryption protocols |  
| H08 | Audit trail logging enabled | No tamper-proof audit logs |  

## SOFT Scoring  
| Dim | Dimension | Weight | Scoring Guide |  
|---|---|---|---|  
| D01 | SOC2+PCI-DSS compliance | 0.20 | 1.00 = fully compliant |  
| D02 | KYC/AML automation | 0.15 | 1.00 = 100% automated checks |  
| D03 | Fraud detection accuracy | 0.15 | 1.00 = <0.1% false positives |  
| D04 | Data security | 0.15 | 1.00 = AES-256 and TLS 1.3 |  
| D05 | Audit trail completeness | 0.10 | 1.00 = 100% traceable events |  
| D06 | Third-party compliance | 0.10 | 1.00 = all vendors SOC2 certified |  
| D07 | User onboarding speed | 0.10 | 1.00 = <5s KYC verification |  

## Actions  
| Score | Action |  
|---|---|  
| GOLDEN | >=9.5 | Auto-publish with CTO approval |  
| PUBLISH | >=8.0 | Publish after QA sign-off |  
| REVIEW | >=7.0 | Escalate to compliance team |  
| REJECT | <7.0 | Block deployment, fix required |  

## Bypass  
| conditions | approver | audit trail |  
|---|---|---|  
| Emergency hotfix | CTO | Documented in incident report |
