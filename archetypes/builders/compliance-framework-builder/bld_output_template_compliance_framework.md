---
kind: output_template
id: bld_output_template_compliance_framework
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for compliance_framework production
quality: 9.1
title: "Output Template Compliance Framework"
version: "1.1.0"
author: n05_ops
tags: [compliance_framework, builder, output_template, gdpr, ai-act, nist, iso42001]
tldr: "Regulatory mapping template with article-level traceability, gap analysis, and signed attestation"
domain: "compliance_framework construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

```yaml
id: p11_cfw_{{name}}
kind: compliance_framework
pillar: P11
title: "Compliance Framework: {{framework_name}}"
version: "{{version}}"
created: "{{datetime_iso8601}}"
updated: "{{datetime_iso8601}}"
author: "{{compliance_officer}}"
domain: "{{domain_eg_healthcare_finance_saas}}"
quality: null
regulatory_scope: "{{jurisdictions_and_regulations}}"
enforcement_mechanisms: "{{fines_audits_sanctions_description}}"
tags: [{{regulation_tags}}]
tldr: "{{one_sentence_scope_and_primary_regulation}}"
```

## 1. Executive Overview

**System/Product:** `{{system_name}}`
**Applicable Regulations:** `{{comma_separated_regulations}}`
**Jurisdictions:** `{{eg_EU_US_Brazil}}`
**Risk Classification:** {{High-risk AI|Limited risk|Minimal risk|Not AI-Act-applicable}}
**Compliance Officer:** `{{name_and_contact}}`
**Last Review:** `{{date}}`
**Next Audit Due:** `{{date}}`

{{2-3 sentence description of what this framework covers and who it protects}}

## 2. Regulatory Scope Matrix

| Regulation | Version/Year | Applicability | Reason | Primary Articles |
|-----------|-------------|--------------|--------|-----------------|
| GDPR | 2018 | Applicable | Processes EU personal data | Art. 5, 13, 22, 25, 30, 32, 33 |
| EU AI Act | 2024 | Applicable | High-risk AI system | Art. 9, 10, 13, 14, 15, 61 |
| NIST AI RMF | 2023 | Applicable | Voluntary risk management | GOVERN, MAP, MEASURE, MANAGE |
| ISO/IEC 42001 | 2023 | Applicable | AI management system | Clause 6, 8, 9, 10 |
| `{{other_regulation}}` | {{year}} | Applicable/Not Applicable | {{reason}} | `{{articles}}` |

## 3. Regulatory Mapping Table

| System Component | Regulation | Article/Clause | Requirement | Implementation | Evidence | Status |
|-----------------|-----------|----------------|-------------|---------------|----------|--------|
| `{{component_1}}` | GDPR | Art. 30 | Records of processing activities | Processing register v`{{ver}}` | Audit log | Compliant |
| `{{component_2}}` | EU AI Act | Art. 13 | Transparency for high-risk AI | User disclosure UI (v`{{ver}}`) | Screenshot + consent log | Compliant |
| `{{component_3}}` | GDPR | Art. 22 | Right to object to automated decisions | Manual override feature | Test report `{{id}}` | Compliant |
| `{{component_4}}` | EU AI Act | Art. 9 | Risk management system | Risk register `{{doc_id}}` | Internal audit | In Progress |
| `{{component_5}}` | EU AI Act | Art. 10 | Data governance requirements | Data lineage doc | DPO sign-off | Compliant |

## 4. Gap Analysis

| Requirement | Regulation/Article | Current State | Gap Description | Remediation Plan | Owner | Target Date |
|------------|-------------------|--------------|----------------|-----------------|-------|-------------|
| `{{requirement}}` | {{reg + article}} | Partial/Missing | {{gap}} | {{action}} | {{team}} | `{{date}}` |

**Summary:**
- Total requirements mapped: `{{N}}`
- Fully compliant: `{{N}}`
- Partially compliant (remediation in progress): `{{N}}`
- Non-compliant (remediation required): `{{N}}`
- Not applicable: `{{N}}`

## 5. Data Protection Provisions (GDPR/CCPA/LGPD)

| Data Subject Right | Legal Basis | Mechanism | SLA | Tested |
|-------------------|------------|-----------|-----|--------|
| Right to access (GDPR Art. 15) | `{{legal_basis}}` | `{{API_or_UI_endpoint}}` | 30 days | Yes/No |
| Right to erasure (GDPR Art. 17) | `{{legal_basis}}` | `{{mechanism}}` | 30 days | Yes/No |
| Right to portability (GDPR Art. 20) | `{{legal_basis}}` | `{{export_feature}}` | 30 days | Yes/No |
| Opt-out of automated decisions (GDPR Art. 22) | `{{legal_basis}}` | `{{override_mechanism}}` | Immediate | Yes/No |

**Data Protection Impact Assessment (DPIA):** {{required|not required}} -- `{{doc_reference}}`
**Data Protection Officer:** `{{name_and_contact}}`
**Legal basis for processing:** {{consent|contract|legitimate_interest|legal_obligation}}

## 6. AI-Specific Obligations (EU AI Act High-Risk)

_(Complete only if AI Act Art. 6 classification applies)_

| Obligation | Article | Implementation | Evidence | Compliant |
|-----------|---------|---------------|----------|-----------|
| Risk management system | Art. 9 | `{{doc_ref}}` | Risk register | Yes/No |
| Data governance | Art. 10 | `{{doc_ref}}` | Data lineage | Yes/No |
| Technical documentation | Art. 11 | `{{doc_ref}}` | Tech doc package | Yes/No |
| Transparency to users | Art. 13 | `{{UI_disclosure}}` | Screenshot | Yes/No |
| Human oversight capability | Art. 14 | `{{override_mechanism}}` | Test evidence | Yes/No |
| Accuracy and robustness | Art. 15 | `{{test_results_ref}}` | Test report | Yes/No |
| Post-market monitoring | Art. 61 | `{{monitoring_plan}}` | Dashboard | Yes/No |

## 7. Bias Mitigation and Fairness

| Metric | Baseline | Threshold | Current Value | Method | Audited By |
|--------|---------|-----------|---------------|--------|------------|
| `{{fairness_metric}}` | {{value}} | {{acceptable_range}} | {{current}} | {{method}} | `{{auditor}}` |

**Bias Audit Report:** `{{doc_reference_or_pending}}`
**Protected attributes monitored:** {{list: age, gender, race, etc.}}

## 8. Audit and Monitoring

| Audit Type | Frequency | Methodology | Last Conducted | Next Due | Auditor |
|-----------|-----------|------------|----------------|----------|---------|
| Internal compliance review | {{quarterly/annual}} | Self-assessment vs. checklist | `{{date}}` | {{date}} | `{{team}}` |
| Third-party audit | Annual | ISO 42001 / SOC 2 Type II | `{{date}}` | {{date}} | `{{certified_body}}` |
| Automated policy scan | Continuous | CI/CD compliance gate | Ongoing | - | cex_compliance_scanner |

## 9. Enforcement and Remediation

| Violation Type | Consequence | Notification Required | Remediation SLA |
|---------------|-------------|----------------------|-----------------|
| GDPR Art. 83(5) severe | Up to EUR 20M or 4% global revenue | DPA within 72h (Art. 33) | Immediate |
| GDPR Art. 83(4) minor | Up to EUR 10M or 2% global revenue | Internal + DPA | 30 days |
| EU AI Act non-conformity | Market withdrawal + fines | Notified body | As directed |

## 10. Version Control and Change Management

| Version | Date | Author | Change Description | Approved By |
|---------|------|--------|-------------------|-------------|
| 1.0.0 | `{{date}}` | {{author}} | Initial framework | `{{approver}}` |
| `{{ver}}` | {{date}} | {{author}} | {{change}} | `{{approver}}` |

## 11. Attestation

> I, `{{compliance_officer_name}}`, `{{title}}`, hereby attest that this compliance framework
> accurately reflects the current state of `{{system_name}}`'s regulatory obligations as of `{{date}}`.
> All mapped requirements have been verified against source regulatory texts.
> Outstanding gaps are documented in Section 4 with committed remediation plans.

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Compliance Officer | {{name}} | `{{signature}}` | `{{date}}` |
| Data Protection Officer | {{name}} | `{{signature}}` | `{{date}}` |
| Legal Counsel | {{name}} | `{{signature}}` | `{{date}}` |
| Engineering Lead | {{name}} | `{{signature}}` | `{{date}}` |

## References

- GDPR: Regulation (EU) 2016/679 -- https://gdpr.eu
- EU AI Act: Regulation (EU) 2024/1689
- NIST AI RMF 1.0: https://airc.nist.gov/Home
- ISO/IEC 42001:2023 AI Management Systems
- ISO/IEC 27001:2022 Information Security Management
- NIST SP 800-188 De-Identification of Government Datasets
