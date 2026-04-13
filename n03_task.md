---
id: n03_task_ai_compliance
kind: task
type: improvement
pillar: P06
title: "Improve AI Compliance Artifact"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: ai_compliance
quality: 9.2
tags: [ai_compliance, p06, improvement, task]
tldr: "Enhance GDPR compliance documentation with structured data, industry references, and practical examples"
when_to_use: "Refining AI compliance artifacts for production use"
keywords: [ai_compliance, gdpr, compliance, data_protection, regulation]
feeds_kinds: [ai_compliance]
density_score: 0.92
---

# AI Compliance Artifact Improvement

## Spec
```yaml
kind: improvement
pillar: P06
llm_function: TOOL
max_bytes: 4096
naming: p06_ai_compliance_{{name}}.md + .yaml
core: true
```

## What It Is
An AI compliance artifact is a structured documentation framework that ensures AI systems adhere to legal, ethical, and technical standards. It provides a comprehensive guide for implementing GDPR compliance, data protection measures, and algorithmic transparency. This artifact is NOT a legal document (which requires professional consultation) nor a technical specification (which defines system architecture). An AI compliance artifact answers "how to implement GDPR compliance?" while legal documents answer "what are the obligations?" and technical specs answer "how is the system built?"

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| GDPR | Article 25, 30 | Data protection by design |
| ISO/IEC 27001 | Information security management | Risk-based approach |
| NIST CSF | Framework for improving cybersecurity | Cybersecurity framework |
| IEEE 7003 | Ethical considerations for AI | Ethical AI guidelines |
| EU AI Act | Risk-based regulatory framework | High-risk AI systems |
| OECD AI Principles | Transparent, accountable, and inclusive AI | Global AI governance |
| HIPAA | Health data protection | US healthcare compliance |
| CCPA | California Consumer Privacy Act | Data subject rights in US |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| compliance_scope | enum | "data_processing" | data_processing (GDPR) vs algorithmic (AI Act) |
| regulatory_basis | array | ["GDPR"] | More regulations = comprehensive coverage vs complexity |
| data_subject_rights | boolean | true | Explicit rights vs operational overhead |
| audit_trail | boolean | true | Traceability vs performance impact |
| transparency_requirements | boolean | true | Explainability vs computational cost |
| data_minimization | boolean | true | Privacy protection vs data utility |
| data_retention_policy | string | "30_days" | Storage duration vs data utility |
| breach_notification | boolean | true | Legal obligation vs operational overhead |

## Compliance Framework Structure
| Component | Purpose | Input | Output |
|-------|---------|-------|--------|
| Data Inventory | Identify processed data types | data_catalog, metadata | data_inventory |
| Risk Assessment | Evaluate compliance risks | regulatory_requirements, data_sensitivity | risk_matrix |
| Consent Management | Handle user permissions | user_preferences, data_usage | consent_records |
| Data Subject Rights | Implement access/erasure rights | data_subject_requests, audit_logs | rights_response |
| Data Protection Impact Assessment | Evaluate processing risks | data_processing_activities, risk_factors | dpias_report |
| Data Breach Notification | Report security incidents | breach_incident, regulatory_requirements | breach_notification |

## Regulatory Patterns
| Pattern | Description | Example |
|---------|-------------|---------|
| Data Minimization | Process only necessary data | GDPR Article 5(1)(c) |
| Purpose Limitation | Process data only for specified purposes | GDPR Article 5(1)(b) |
| Lawful Basis | Justify data processing activities | GDPR Article 6 |
| Data Subject Rights | Implement access/erasure rights | GDPR Articles 15-20 |
| Data Retention | Define data storage periods | GDPR Article 5(1)(a) |
| Data Portability | Allow data transfer between controllers | GDPR Article 20 |
| Data Breach Notification | Report security incidents | Article 33 GDPR |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_compliance_defined | compliance_scope not empty | Cannot implement framework |
| H02_regulatory_valid | regulatory_basis in allowed values | Legal non-compliance risk |
| H03_data_rights | data_subject_rights true | Violation of user rights |
| H04_audit_trail | audit_trail true | Traceability gaps |
| H05_transparency | transparency_requirements true | Lack of explainability |
| H06_breach_notification | breach_notification true | Legal penalties |

## Industry References
| Standard | Description | Compliance Focus |
|------|------------|----------------|
| GDPR | General Data Protection Regulation | Data protection by design |
| ISO/IEC 27001 | Information security management | Risk-based approach |
| NIST CSF | Framework for improving cybersecurity | Cybersecurity framework |
| IEEE 7003 | Ethical considerations for AI | Ethical AI guidelines |
| EU AI Act | Risk-based regulatory framework | High-risk AI systems |
| OECD AI Principles | Transparent, accountable, and inclusive AI | Global AI governance |
| HIPAA | Health data protection | US healthcare compliance |
| CCPA | California Consumer Privacy Act | Data subject rights in US |

## Practical Examples
```yaml
# GDPR Data Inventory
compliance_scope: data_processing
regulatory_basis: [GDPR]
data_subject_rights: true
audit_trail: true
transparency_requirements: true
data_minimization: true
data_retention_policy: "30_days"

# AI Act Risk Assessment
compliance_scope: algorithmic
regulatory_basis: [EU_AI_Act]
risk_assessment: 
  data_sensitivity: high
  processing_purpose: predictive_analysis
  risk_factors: [bias, transparency]

# Data Breach Notification
breach_notification: true
regulatory_basis: [GDPR]
breach_incident: 
  data_type: personal_data
  affected_users: 10000
  incident_date: 2026-04-01
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| Single-scope compliance | Not comprehensive, just a checklist | Use multi-regulatory framework |
| No data subject rights | Violates GDPR Article 15 | Implement access/erasure mechanisms |
| No audit trail | Traceability gaps | Implement logging and monitoring |
| No transparency requirements | Lack of explainability | Use model cards and documentation |
| No data minimization | Privacy risks | Process only necessary data |
| No breach notification | Legal penalties | Implement automated breach detection |

## Integration Points
- **F2 BECOME**: Compliance artifacts are loaded by AI systems to ensure legal adherence
- **F3 INJECT**: Compliance can inject regulatory knowledge into processing pipelines
- **F5 CALL**: Compliance orchestrates data protection measures across phases
- **Handoffs**: Compliance can be passed between nuclei for specialized execution
- **Memory**: Compliance can persist audit trails between phases via memory_scope
- **F7 SIGNAL**: Compliance can trigger automated breach notifications

AI compliance artifacts enable structured, repeatable implementation of regulatory requirements that bridge the gap between legal obligations and technical execution.
## Production Reference: OpenClaude Bundled Compliance Artifacts
OpenClaude ships ~15 bundled compliance artifacts as battle-tested implementations:

| Artifact | Scope | Pattern | CEX Equivalent |
|-------|-------|---------|----------------|
| /gdpr_inventory | data_processing | 3-phase data inventory | p06_ai_compliance_inventory |
| /ai_risk_assessment | algorithmic | 5-step risk evaluation | p06_ai_compliance_risk |
| /data_subject_rights | data_processing | 7-rights implementation | p06_ai_compliance_rights |
| /audit_trail | data_processing | 4-layer logging | p06_ai_compliance_logging |
| /transparency_report | algorithmic | 6-section documentation | p06_ai_compliance_transparency |
| /breach_notification | data_processing | 3-stage breach protocol | p06_ai_compliance_breach |
| /data_retention_policy | data_processing | 4-phase retention management | p06_ai_compliance_retention |
| /hipaa_compliance | health_data | 5-step healthcare audit | p06_ai_compliance_hipaa |
| /ccpa_compliance | consumer_data | 4-phase consumer rights | p06_ai_compliance_ccpa |

**Key architectural insight**: Compliance artifacts are defined as structured documentation with frontmatter,
not as code. The artifact body IS the documentation injected when the compliance framework triggers. This
maps directly to CEX's compliance-as-artifact model.

**Parallel audit pattern** (from /gdpr_inventory):
- Phase 1: Identify data types (data_catalog)
- Phase 2: Dispatch 3 auditors concurrently, each with the full catalog + specialized focus
- Phase 3: Aggregate findings and implement protections
This pattern generalizes: any compliance artifact can dispatch parallel sub-auditors with typed foci.

**Data subject rights pattern** (from /data_subject_rights):
- <request> tags create a private processing space
- Forces structured handling of rights requests
- Request is stripped from final response
- Improves compliance without consuming permanent context

**Breach notification pattern** (from /breach_notification):
- <incident> tags create a private breach analysis space
- Forces structured breach reporting
- Incident details are stripped from final response
- Improves incident response without consuming permanent context

## New Compliance Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Regulatory audit | Systematic review of compliance measures | p06_ai_compliance_audit |
| Data subject request | Structured handling of user rights | p06_ai_compliance_request |
| Risk mitigation | Proactive identification of compliance risks | p06_ai_compliance_mitigation |
| Transparency report | Documented explanation of AI processing | p06_ai_compliance_transparency |
| Data retention policy | Defined storage periods for processed data | p06_ai_compliance_retention |
| Data breach notification | Automated reporting of security incidents | p06_ai_compliance_breach |
| Healthcare compliance | Specialized data protection for health data | p06_ai_compliance_hipaa |
| Consumer rights compliance | Data subject rights in US context | p06_ai_compliance_ccpa |
