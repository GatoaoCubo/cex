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
related:
  - bld_examples_fintech_vertical
  - bld_instruction_fintech_vertical
  - p10_mem_fintech_vertical_builder
  - fintech-vertical-builder
  - p03_sp_fintech_vertical_builder
  - bld_knowledge_card_fintech_vertical
  - p01_qg_ecommerce_vertical
  - bld_tools_fintech_vertical
  - p03_sp_ecommerce_vertical_builder
  - kc_ecommerce_vertical
---

## Quality Gate

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

## Examples

## Golden Example (fintech vertical artifact)
```markdown  
---  
title: "Fintech Vertical: SOC2+PCI-DSS, KYC/AML, Fraud Detection"  
description: "Integration of compliance, identity verification, and fraud prevention tools for a digital banking platform."  
use_cases:  
  - Real-time transaction monitoring  
  - Onboarding of enterprise clients  
  - Cross-border payment validation  
compliance_standards:  
  - SOC2 Type II  
  - PCI-DSS v4.0  
tools:  
  - **Compliance**: AWS Artifact (SOC2), Stripe (PCI-DSS)  
  - **KYC/AML**: Trulio (KYC), Elliptic (AML)  
  - **Fraud Detection**: Sift (fraud scoring), Feedzai (AI-based detection)  
vendor: "DigitalBank Inc."  
---  
Body:  
DigitalBank Inc. leverages AWS Artifact for SOC2 compliance, ensuring data integrity and confidentiality. Stripe handles PCI-DSS requirements for payment processing. Trulio automates KYC checks using ID verification and sanctions list screening. Elliptic integrates distributed-ledger AML monitoring for crypto transactions. Sift and Feedzai analyze user behavior and transaction patterns to detect fraud in real time. This stack ensures compliance, reduces onboarding time, and minimizes fraud losses.  
```  

## Anti-Example 1: Incomplete Compliance Tooling  
```markdown  
---  
title: "Fintech Vertical: SOC2+PCI-DSS, KYC/AML, Fraud Detection"  
description: "Basic setup with missing compliance layers."  
use_cases:  
  - "Basic user onboarding"  
compliance_standards:  
  - "SOC2 (unverified)"  
tools:  
  - **KYC/AML**: Onfido (no AML integration)  
  - **Fraud Detection**: None  
vendor: "QuickPay Ltd."  
---  
Body:  
QuickPay Ltd. uses Onfido for ID verification but lacks AML checks or fraud detection. SOC2 compliance is not formally validated. This leaves the platform vulnerable to money laundering and undetected fraud.  
## Why it fails  
No AML tooling or fraud detection violates core compliance and security requirements. SOC2 claims without verification are invalid.  
```  

## Anti-Example 2: Over-Reliance on Single Vendor  
```markdown  
---  
title: "Fintech Vertical: SOC2+PCI-DSS, KYC/AML, Fraud Detection"  
description: "Single-vendor solution with no redundancy."  
use_cases:  
  - "Internal audit"  
tools:  
  - **All**: "ComplyX (proprietary tool)"  
vendor: "SecureFin Co."  
---  
Body:  
SecureFin Co. uses ComplyX for SOC2, PCI-DSS, KYC, and fraud detection. However, ComplyX lacks third-party validation and has no backup systems.  
## Why it fails  
Over-reliance on a single vendor increases risk of outages, compliance gaps, and lack of independent audits. No redundancy violates best practices for critical fintech systems.  
```

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
