---
kind: quality_gate
id: p01_qg_edtech_vertical
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for edtech_vertical
quality: null
title: "Quality Gate Edtech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [edtech_vertical, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for edtech_vertical"
domain: "edtech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
| Metric | Threshold | Operator | Scope |  
|---|---|---|---|  
| FERPA Compliance | 100% | Must be | Student data handling |  
| COPPA Compliance | 100% | Must be | Under-13 user data |  
| LTI Integration | Valid | Must pass | LMS compatibility |  
| Data Encryption | AES-256 | Must use | Student data at rest |  
| Privacy Policy | Exists | Must be | Publicly accessible |  

## HARD Gates  
| ID | Check | Fail Condition |  
|---|---|---|  
| H01 | YAML frontmatter valid | Invalid syntax or missing fields |  
| H02 | ID matches ^p01_etv_[a-z][a-z0-9_]+.md$ | Invalid schema ID pattern |  
| H03 | kind field matches 'edtech_vertical' | Incorrect or missing kind |  
| H04 | LTI integration conforms to IMS standards | Non-compliant LTI endpoints |  
| H05 | Student data access logs auditable | Missing audit trails for data access |  
| H06 | COPPA opt-in mechanisms implemented | No explicit parental consent flows |  
| H07 | FERPA data minimization enforced | Unnecessary student data collected |  

## SOFT Scoring  
| Dim | Dimension | Weight | Scoring Guide |  
|---|---|---|---|  
| D01 | Data Privacy Practices | 0.15 | 1.0 = Full compliance |  
| D02 | LTI Integration Quality | 0.12 | 1.0 = Seamless LMS compatibility |  
| D03 | COPPA/FERPA Alignment | 0.15 | 1.0 = Full regulatory adherence |  
| D04 | Use Case Relevance | 0.10 | 1.0 = Direct alignment with education needs |  
| D05 | Performance | 0.10 | 1.0 = <100ms latency for critical flows |  
| D06 | Scalability | 0.10 | 1.0 = 1M+ concurrent users supported |  
| D07 | Security | 0.10 | 1.0 = Zero critical vulnerabilities |  
| D08 | User Experience | 0.18 | 1.0 = 95%+ user satisfaction |  

## Actions  
| Score | Action |  
|---|---|  
| GOLDEN (>=9.5) | Auto-publish with no review |  
| PUBLISH (>=8.0) | Auto-publish with minimal checks |  
| REVIEW (>=7.0) | Manual review by edtech compliance team |  
| REJECT (<7.0) | Block deployment; require fixes |  

## Bypass  
| Conditions | Approver | Audit Trail |  
|---|---|---|  
| Legal exemption for pilot programs | CTO | Documented risk assessment |  
| Emergency use case with 72h deadline | CISO | Time-stamped approval |  
| Third-party audit override | Legal Counsel | Signed waiver + audit report |
