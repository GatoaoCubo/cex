---
kind: quality_gate
id: p01_qg_fintech_vertical
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for fintech_vertical
quality: 9.0
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
| H04 | SOC2 Type II + PCI-DSS v4.0 framework section present in artifact | No compliance framework section |
| H05 | KYC/AML workflow documented including OFAC SDN screening and FinCEN CIP fields | Missing KYC/AML or OFAC section |
| H06 | Fraud detection methodology documented (behavioral scoring or ML approach) | No fraud detection methodology |
| H07 | Data encryption approach specified (AES-256 at rest, TLS 1.3 in transit) | Missing encryption specifications |
| H08 | Audit trail requirements documented | No audit trail section |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | SOC2+PCI-DSS coverage | 0.20 | 1.00 = SOC2 Type II + PCI-DSS v4.0 both addressed |
| D02 | KYC/AML completeness | 0.15 | 1.00 = CDD + OFAC + FinCEN CIP all present |
| D03 | Fraud detection specificity | 0.15 | 1.00 = vendor pattern (Sift/Sardine) or ML approach specified |
| D04 | Data security depth | 0.15 | 1.00 = AES-256 + TLS 1.3 + tokenization specified |
| D05 | Audit trail completeness | 0.10 | 1.00 = 100% traceable events documented |
| D06 | Regulatory breadth | 0.10 | 1.00 = ISO 20022 + SOX 404 + FFIEC CAT addressed |
| D07 | Integration specificity | 0.10 | 1.00 = specific API/platform patterns documented |
| D08 | Documentation completeness | 0.05 | 1.00 = all required frontmatter fields populated |

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
