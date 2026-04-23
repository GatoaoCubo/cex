---
kind: quality_gate
id: p09_qg_data_residency
pillar: P09
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for data_residency
quality: 9.1
title: "Quality Gate Data Residency"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [data_residency, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for data_residency"
domain: "data_residency construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_data_residency
  - p09_kc_data_residency
  - bld_output_template_data_residency
  - p11_qg_compliance_checklist
  - bld_knowledge_card_data_residency
  - p01_qg_healthcare_vertical
  - bld_instruction_data_residency
  - kc_ai_compliance_gdpr
  - p11_qg_audit_log
  - data-residency-builder
---

## Quality Gate

## Definition
| metric         | threshold | operator | scope         |
|----------------|-----------|----------|---------------|
| Compliance     | 100%      | =        | All data      |

## HARD Gates
| ID        | Check                          | Fail Condition                                      |
|-----------|--------------------------------|-----------------------------------------------------|
| H01       | YAML frontmatter valid         | Missing or invalid frontmatter                      |
| H02       | ID matches pattern             | ID does not match ^p09_dr_[a-z][a-z0-9_]+.md$      |
| H03       | kind field matches 'data_residency' | kind field is not 'data_residency'               |
| H04       | Data stored in allowed regions | Data resides in regions not permitted by policy     |
| H05       | Encryption applied             | Data not encrypted at rest or in transit            |
| H06       | Access controls enforced       | Unauthorized access to data in prohibited regions   |
| H07       | Audit logs maintained          | No audit trail for data residency configuration     |
| H08       | Data transfer compliance       | Cross-border transfers lack legal basis or safeguards |

## SOFT Scoring
| Dim | Dimension               | Weight | Scoring Guide                                      |
|-----|-------------------------|--------|----------------------------------------------------|
| D1  | GDPR compliance         | 0.15   | 100% compliance = 1.0; 50% = 0.5; 0% = 0.0          |
| D2  | Data encryption         | 0.15   | AES-256 or equivalent = 1.0; partial = 0.5; none = 0 |
| D3  | Access controls         | 0.15   | Role-based access = 1.0; weak = 0.5; none = 0        |
| D4  | Audit trails            | 0.10   | Full logs = 1.0; partial = 0.5; none = 0             |
| D5  | Data transfer policies  | 0.15   | Legal basis documented = 1.0; missing = 0.5          |
| D6  | Storage location accuracy | 0.10   | 100% accurate = 1.0; 50% = 0.5; 0% = 0               |
| D7  | Incident response       | 0.10   | Plan exists and tested = 1.0; missing = 0.5          |
| D8  | Employee training       | 0.10   | Annual training = 1.0; none = 0.5                    |

## Actions
| Score     | Action                              |
|-----------|-------------------------------------|
| GOLDEN    | Automated approval                  |
| PUBLISH   | Manual review by compliance team    |
| REVIEW    | Escalate to legal for verification  |
| REJECT    | Block deployment; remediate first   |

## Bypass
| conditions                          | approver | audit trail                |
|-------------------------------------|----------|----------------------------|
| Emergency data migration with CTO approval | CTO      | Documented in incident log |

## Examples

## Golden Example
```yaml
kind: data_residency
name: eu_gdpr_compliance
labels:
  region: EU
  compliance: GDPR
spec:
  data_storage:
    provider: AWS
    regions: ["eu-west-1", "eu-central-1"]
  data_processing:
    provider: Azure
    regions: ["westeurope", "northeurope"]
  encryption:
    at_rest: AES-256
    in_transit: TLS-1.2
  legal:
    dpa: "https://aws.amazon.com/compliance/gdpr/"
    audit_logs: "https://azure.microsoft.com/en-us/compliance/audit-logs/"
```

## Anti-Example 1: Vague Region Specification
```yaml
kind: data_residency
name: generic_eu_setup
labels:
  region: EU
spec:
  data_storage:
    provider: Google Cloud
    regions: ["EU"]
```
## Why it fails
GDPR requires specific member state locations (e.g., "de" for Germany), not generic "EU" labels. Vague region definitions fail to meet legal requirements for data localization.

## Anti-Example 2: Missing Encryption Requirements
```yaml
kind: data_residency
name: us_compliance
labels:
  region: US
spec:
  data_storage:
    provider: AWS
    regions: ["us-east-1"]
```
## Why it fails
The spec omits encryption standards for data at rest/in transit, which are mandatory for GDPR and regional compliance. Data residency alone is insufficient without proper cryptographic protections.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
