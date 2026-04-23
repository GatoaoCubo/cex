---
kind: quality_gate
id: p11_qg_compliance_checklist
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for compliance_checklist
quality: 8.9
title: "Quality Gate Compliance Checklist"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [compliance_checklist, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for compliance_checklist"
domain: "compliance_checklist construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_compliance_checklist
  - bld_instruction_compliance_checklist
  - compliance-checklist-builder
  - p10_mem_compliance_checklist_builder
  - p09_qg_data_residency
  - kc_compliance_checklist
  - bld_knowledge_card_compliance_checklist
  - p01_qg_healthcare_vertical
  - audit-log-builder
  - p11_qg_audit_log
---

## Quality Gate

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| compliance_coverage | 100% | >= | all audits |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | invalid YAML syntax |
| H02 | ID matches pattern ^p11_cc_[a-z][a-z0-9_]+.md$ | invalid ID format |
| H03 | kind field matches 'compliance_checklist' | incorrect kind value |
| H04 | SOC2 controls documented | missing control descriptions |
| H05 | GDPR data subject rights implemented | incomplete DSAR process |
| H06 | HIPAA encryption policies enforced | unencrypted sensitive data |
| H07 | EU AI Act audit trails complete | missing audit logs for AI systems |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D1 | Data protection | 0.20 | 1.00 (full encryption) |
| D2 | Audit readiness | 0.15 | 1.00 (complete logs) |
| D3 | Documentation | 0.15 | 1.00 (all policies documented) |
| D4 | GDPR compliance | 0.15 | 1.00 (DSARs handled) |
| D5 | HIPAA adherence | 0.15 | 1.00 (controls met) |
| D6 | AI Act compliance | 0.10 | 1.00 (audit trails valid) |
| D7 | Third-party reviews | 0.10 | 1.00 (all vendors audited) |

## Actions
| Score | Action |
|---|---|
| >=9.5 | GOLDEN |
| >=8.0 | PUBLISH |
| >=7.0 | REVIEW |
| <7.0 | REJECT |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| legal exception | CTO | signed waiver |
| urgent regulatory change | CEO | emergency audit |

## Examples

## Golden Example
```markdown
---
title: Compliance Checklist for SOC2, GDPR, HIPAA, EU AI Act
vendor: AWS
product: AWS CloudTrail + AWS Config
version: 1.0
---

### SOC2
- [ ] Data encryption at rest (AES-256) (Evidence: AWS KMS logs)
- [ ] Access control policies (Evidence: IAM role audits)
- [ ] Incident response plan (Evidence: SOC2 Type II report)

### GDPR
- [ ] Data subject access request (DSAR) process (Evidence: OneTrust integration logs)
- [ ] Data breach notification protocol (Evidence: GDPR compliance dashboard)
- [ ] Third-party vendor assessments (Evidence: TrustArc audit reports)

### HIPAA
- [ ] PHI data storage encryption (Evidence: AWS CloudHSM audit trails)
- [ ] HIPAA-compliant business associate agreements (Evidence: Protenus contract reviews)
- [ ] Audit logging for all PHI access (Evidence: AWS Config rules)

### EU AI Act
- [ ] High-risk AI system impact assessment (Evidence: IBM AI Fairness 360 reports)
- [ ] Data governance for training datasets (Evidence: Google Cloud Data Loss Prevention logs)
- [ ] Human oversight mechanisms (Evidence: Azure AI governance policies)
```

## Anti-Example 1: Missing Specific Controls
```markdown
---
title: Compliance Checklist
vendor: ExampleCorp
product: Generic Compliance Tool
version: 0.1
---

### SOC2
- [ ] "Basic security measures" (Evidence: ???)
- [ ] "Data protection" (Evidence: ???)
```
## Why it fails
Vague controls like "basic security measures" lack specificity required for audit validation. No evidence types or responsible parties are defined, making it impossible to verify compliance.

## Anti-Example 2: Vague Evidence Requirements
```markdown
---
title: Compliance Checklist
vendor: SomeCompany
product: Compliance Framework
version: 2.0
---

### GDPR
- [ ] Data encryption (Evidence: "Documents available")
- [ ] DSAR handling (Evidence: "Process exists")
```
## Why it fails
"Documents available" and "process exists" are too generic. Auditors need specific evidence types (e.g., encryption certificates, DSAR response templates) and verification methods to confirm compliance.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
