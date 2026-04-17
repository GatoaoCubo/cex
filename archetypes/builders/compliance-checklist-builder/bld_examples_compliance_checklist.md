---
kind: examples
id: bld_examples_compliance_checklist
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of compliance_checklist artifacts
quality: 8.9
title: "Examples Compliance Checklist"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [compliance_checklist, builder, examples]
tldr: "Golden and anti-examples of compliance_checklist artifacts"
domain: "compliance_checklist construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

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
