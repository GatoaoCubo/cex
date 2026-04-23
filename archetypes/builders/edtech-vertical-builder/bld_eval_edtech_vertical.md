---
kind: quality_gate
id: p01_qg_edtech_vertical
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for edtech_vertical
quality: 9.0
title: "Quality Gate Edtech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [edtech_vertical, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for edtech_vertical"
domain: "edtech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_edtech_vertical
  - p10_mem_edtech_vertical_builder
  - bld_instruction_edtech_vertical
  - p03_sp_edtech_vertical_builder
  - edtech-vertical-builder
  - bld_tools_edtech_vertical
  - bld_output_template_edtech_vertical
  - bld_knowledge_card_edtech_vertical
  - p09_qg_data_residency
  - kc_ai_compliance_gdpr
---

## Quality Gate

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
|-----|-----------|--------|---------------|
| D01 | FERPA data minimization specificity | 0.20 | Named records + purpose limitation cited = 1.0, general reference = 0.5, absent = 0 |
| D02 | LTI 1.3 integration depth | 0.20 | OAuth 2.0 + IMS Security Framework v1.0 cited = 1.0, LTI 1.3 named = 0.5, absent = 0 |
| D03 | COPPA consent mechanism detail | 0.15 | Parental consent flow described + FTC guidelines cited = 1.0, referenced = 0.5, absent = 0 |
| D04 | 1EdTech standards coverage | 0.15 | xAPI or Caliper cited for analytics = 1.0, referenced = 0.5, absent = 0 |
| D05 | District procurement path | 0.15 | State ed-tech approval list or ISTE certification cited = 1.0, generic = 0.5, absent = 0 |
| D06 | Use case specificity (K-12 vs Higher Ed vs vocational) | 0.15 | Target demographic + scenario named = 1.0, partial = 0.5, none = 0 |

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

## Examples

## Golden Example  
```yaml  
title: EdTech Vertical Integration with LTI and Privacy Compliance  
kind: edtech_vertical  
description: Secure student data management with LTI integration and FERPA/COPPA compliance  
tools:  
  - LMS: Canvas LMS  
  - Data Privacy: Google Workspace for Education (with encryption at rest and in transit)  
  - LTI Provider: Microsoft Teams for Education (LTI 1.3 compliant)  
use_cases:  
  - Student performance analytics with anonymized data  
  - Parental consent workflows for COPPA-compliant data collection  
  - Seamless grade sync between LMS and external assessment tools  
compliance:  
  - FERPA: Data access restricted to authorized educational purposes  
  - COPPA: Age verification and opt-in mechanisms for under-13 users  
```  

## Anti-Example 1: Missing LTI Compliance  
```yaml  
title: EdTech Vertical Integration (Incomplete)  
kind: edtech_vertical  
description: Student data management without LTI integration  
tools:  
  - LMS: Moodle  
  - Data Privacy: Custom in-house solution (no third-party audits)  
use_cases:  
  - Manual data transfer between systems  
  - No student consent tracking  
compliance:  
  - FERPA: Not explicitly addressed  
  - COPPA: Not applicable (no under-13 user handling)  
```  
## Why it fails  
Lacks LTI integration, leading to insecure data silos and non-compliant manual workflows. No third-party audits or encryption mechanisms violate FERPA/COPPA requirements.  

## Anti-Example 2: Overlooking COPPA Scope  
```yaml  
title: EdTech Vertical for K-12  
kind: edtech_vertical  
description: LMS integration with student data collection  
tools:  
  - LMS: Schoology  
  - Data Privacy: Third-party analytics tool (no COPPA certification)  
use_cases:  
  - Real-time student behavior tracking  
  - Automated reporting to school admins  
compliance:  
  - FERPA: Partially addressed  
  - COPPA: Ignored (tool collects data from under-13 users without consent)  
```  
## Why it fails  
The analytics tool collects data from minors without COPPA-compliant consent mechanisms, exposing the organization to legal risks and data breaches.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
