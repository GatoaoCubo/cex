---
kind: knowledge_card
id: bld_knowledge_card_compliance_checklist
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for compliance_checklist production
quality: 9.2
title: "Knowledge Card Compliance Checklist"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [compliance_checklist, builder, knowledge_card]
tldr: "Domain knowledge for compliance_checklist production"
domain: "compliance_checklist construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_instruction_compliance_checklist
  - compliance-checklist-builder
  - kc_ai_compliance_gdpr
  - p10_mem_compliance_checklist_builder
  - p03_sp_compliance_checklist_builder
  - kc_compliance_framework
  - kc_compliance_checklist
  - bld_output_template_compliance_framework
  - p09_kc_data_residency
  - audit-log-builder
---

## Domain Overview  
Compliance checklists are structured artifacts used to validate adherence to regulatory and industry-specific requirements during audits. For SOC2, GDPR, HIPAA, and the EU AI Act, these checklists ensure organizations meet standards for data protection, privacy, security, and AI governance. SOC2 focuses on trust services criteria (security, availability, processing integrity, confidentiality, and privacy) for cloud service providers. GDPR mandates strict data subject rights and breach notification protocols for EU data processing. HIPAA enforces safeguards for protected health information (PHI) in healthcare. The EU AI Act introduces risk-based requirements for AI systems, including transparency and human oversight. Checklists help map controls to these frameworks, ensuring audit readiness.  

## Key Concepts  
| Concept | Definition | Source |  
|-------|------------|------|  
| Data Protection Impact Assessment (DPIA) | Evaluation of data processing risks under GDPR | GDPR Art. 35 |  
| Access Controls | Restricting system access to authorized users | SOC2 Trust Services Criteria |  
| Breach Notification | Mandatory disclosure of data breaches within 72 hours | GDPR Art. 33 |  
| HIPAA Administrative Safeguards | Policies and procedures to manage PHI | HIPAA Privacy Rule |  
| AI Risk Assessment | Identifying harms from high-risk AI systems | EU AI Act Art. 13 |  
| Encryption Requirements | Protecting data at rest and in transit | NIST SP 800-53 |  
| Consent Management | Explicit user consent for data processing | GDPR Art. 7 |  
| Audit Trail Logging | Recording system activities for forensic analysis | SOC2 Trust Services Criteria |  

## Industry Standards  
- SOC2 Trust Services Criteria (AICPA)  
- GDPR Regulation (EU) 2016/679  
- HIPAA Privacy and Security Rules (45 CFR 160, 162, 164)  
- EU AI Act (2024/1614)  
- ISO/IEC 27001:2022 (Information Security Management)  
- NIST SP 800-53 (Security and Privacy Controls)  
- RFC 7258 (Privacy Considerations for IoT)  
- OECD AI Principles (2019)  

## Common Patterns  
1. Map data flows to regulatory scope (e.g., GDPR Article 3).  
2. Use automated tools for continuous compliance monitoring.  
3. Document policies aligned with specific framework requirements.  
4. Conduct regular third-party vendor assessments.  
5. Embed audit trails for all critical system interactions.  
6. Perform role-based access control (RBAC) reviews quarterly.  

## Pitfalls  
- Assuming generic controls apply to all regulations without customization.  
- Overlooking GDPR’s “right to be forgotten” in data retention policies.  
- Failing to update HIPAA breach notification procedures for cloud storage.  
- Ignoring EU AI Act’s transparency requirements for high-risk AI.  
- Not aligning audit checklists with the latest regulatory amendments.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_compliance_checklist]] | downstream | 0.54 |
| [[compliance-checklist-builder]] | downstream | 0.52 |
| [[kc_ai_compliance_gdpr]] | sibling | 0.45 |
| [[p10_mem_compliance_checklist_builder]] | downstream | 0.43 |
| [[p03_sp_compliance_checklist_builder]] | downstream | 0.43 |
| [[kc_compliance_framework]] | sibling | 0.40 |
| [[kc_compliance_checklist]] | sibling | 0.39 |
| [[bld_output_template_compliance_framework]] | downstream | 0.37 |
| [[p09_kc_data_residency]] | sibling | 0.34 |
| [[audit-log-builder]] | downstream | 0.33 |
