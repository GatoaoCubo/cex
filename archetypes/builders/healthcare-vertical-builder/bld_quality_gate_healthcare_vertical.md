---
kind: quality_gate
id: p01_qg_healthcare_vertical
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for healthcare_vertical
quality: null
title: "Quality Gate Healthcare Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [healthcare_vertical, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for healthcare_vertical"
domain: "healthcare_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
| metric | threshold | operator | scope |  
|---|---|---|---|  
| Healthcare vertical compliance | 100% | = | All healthcare-related content |  

## HARD Gates  
| ID | Check | Fail Condition |  
|---|---|---|  
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing fields |  
| H02 | ID matches pattern ^p01_hv_[a-z][a-z0-9_]+.md$ | ID does not conform to schema |  
| H03 | kind field matches 'healthcare_vertical' | kind field is incorrect |  
| H04 | HIPAA compliance documented | Missing HIPAA compliance proof |  
| H05 | PHI handling procedures defined | No PHI handling guidelines |  
| H06 | HL7/FHIR standards adhered | Non-compliant with HL7/FHIR |  
| H07 | Use case alignment verified | Use cases not mapped to healthcare needs |  
| H08 | Data encryption enforced | PHI data not encrypted at rest/transit |  
| H09 | Audit logging implemented | No audit trails for PHI access |  
| H10 | Access controls enforced | Role-based access not configured |  

## SOFT Scoring  
| Dim | Dimension | Weight | Scoring Guide |  
|---|---|---|---|  
| D01 | HIPAA compliance | 0.15 | 100% = 1.0, 50% = 0.5 |  
| D02 | PHI handling | 0.15 | 100% = 1.0, 50% = 0.5 |  
| D03 | HL7/FHIR adherence | 0.12 | 100% = 1.0, 75% = 0.75 |  
| D04 | Use case coverage | 0.12 | 100% = 1.0, 75% = 0.75 |  
| D05 | Data encryption | 0.10 | 100% = 1.0, 50% = 0.5 |  
| D06 | Audit logging | 0.10 | 100% = 1.0, 50% = 0.5 |  
| D07 | Access controls | 0.10 | 100% = 1.0, 50% = 0.5 |  
| D08 | Documentation completeness | 0.16 | 100% = 1.0, 50% = 0.5 |  

## Actions  
| Score | Action |  
|---|---|  
| GOLDEN | >=9.5 | Auto-approve for production |  
| PUBLISH | >=8.0 | Manual review required |  
| REVIEW | >=7.0 | Escalate to compliance team |  
| REJECT | <7.0 | Block deployment |  

## Bypass  
| conditions | approver | audit trail |  
|---|---|---|  
| Emergency fix with CTO approval | CTO | Documented in Jira |  
| Regulatory change with legal sign-off | Legal team | Signed waiver |
