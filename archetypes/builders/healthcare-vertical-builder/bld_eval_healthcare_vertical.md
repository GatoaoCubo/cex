---
kind: quality_gate
id: p01_qg_healthcare_vertical
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for healthcare_vertical
quality: 9.0
title: "Quality Gate Healthcare Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [healthcare_vertical, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for healthcare_vertical"
domain: "healthcare_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_healthcare_vertical
  - healthcare-vertical-builder
  - p10_mem_healthcare_vertical_builder
  - bld_instruction_healthcare_vertical
  - bld_knowledge_card_healthcare_vertical
  - p03_sp_healthcare_vertical_builder
  - p08_qg_fhir_agent_capability
  - bld_knowledge_card_fhir_agent_capability
  - kc_healthcare_vertical
  - bld_collaboration_fhir_agent_capability
---

## Quality Gate

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
| H04 | HIPAA Privacy + Security Rule compliance section present | Missing HIPAA compliance section |
| H05 | PHI handling procedures defined including de-identification method (Safe Harbor or Expert Determination) | No PHI handling or de-identification guidelines |
| H06 | HL7 v2.x or FHIR R4 interoperability documented | No interoperability standard referenced |
| H07 | Use case mapped to specific clinical workflow (not generic IT) | Use cases not healthcare-specific |
| H08 | Data encryption specification present (AES-256 at rest, TLS 1.2+ in transit) | Missing encryption specification |
| H09 | Audit logging requirements documented per 45 CFR 164.312(b) | No audit trail requirements |
| H10 | Role-based access control (RBAC) documented | No access control specification |

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

## Examples

## Golden Example  
```markdown  
---  
title: "Secure Patient Data Exchange Using FHIR"  
kind: healthcare_vertical  
vendor: Epic Systems  
tool: Epic EHR Platform  
standard: HL7 FHIR R4  
use_case: Interoperable patient record sharing between hospitals  
description:  
  - Implements HIPAA-compliant PHI encryption (AES-256) at rest and TLS 1.2+ in transit  
  - Integrates with HL7 FHIR API for real-time lab result sharing  
  - Audits all PHI access via AWS CloudTrail with role-based access controls  
  - Uses Athenahealth's patient portal for consumer-facing data access  
  - Complies with ONC 21st Century Cures Final Rule for data blocking  
```  

## Anti-Example 1: Missing HIPAA Compliance  
```markdown  
---  
title: "Basic Lab Result API"  
kind: healthcare_vertical  
vendor: MedTech Inc.  
tool: Legacy Lab API v1.0  
standard: HL7 v2.x  
use_case: Lab result transmission  
description:  
  - No explicit encryption or audit logging for PHI  
  - Uses unauthenticated HTTP endpoints for data transfer  
  - No mention of HIPAA or PHI handling protocols  
```  
## Why it fails  
Lacks fundamental HIPAA requirements (encryption, access controls) and uses deprecated HL7 v2.x without FHIR interoperability, violating modern healthcare data standards.  

## Anti-Example 2: Ignoring FHIR Standards  
```markdown  
---  
title: "Custom EHR Module"  
kind: healthcare_vertical  
vendor: HealthSoft LLC  
tool: Proprietary EHR Module  
standard: Custom HL7 v2.x  
use_case: Internal provider documentation  
description:  
  - No FHIR API integration  
  - Stores PHI in unencrypted flat files  
  - No audit trails for data access  
```  
## Why it fails  
Fails to adopt HL7 FHIR (required for interoperability) and lacks HIPAA-mandated encryption and audit controls, creating compliance and interoperability risks.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
