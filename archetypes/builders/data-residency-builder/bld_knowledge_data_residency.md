---
kind: knowledge_card
id: bld_knowledge_card_data_residency
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for data_residency production
quality: 9.2
title: "Knowledge Card Data Residency"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [data_residency, builder, knowledge_card]
tldr: "Domain knowledge for data_residency production"
domain: "data_residency construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - data-residency-builder
  - p09_kc_data_residency
  - p03_sp_data_residency_builder
  - bld_instruction_data_residency
  - p10_mem_data_residency_builder
  - kc_ai_compliance_gdpr
  - p09_qg_data_residency
  - bld_schema_data_residency
  - bld_collaboration_data_residency
  - bld_tools_data_residency
---

## Domain Overview
Data residency ensures data is stored, processed, and transferred in compliance with regional laws like GDPR, which mandates data processing within the EU or under adequate safeguards. It addresses legal risks from cross-border data flows, sovereignty requirements, and penalties for non-compliance. Cloud providers and enterprises must configure residency policies to align with data localization laws, such as China’s PIPL or the EU’s GDPR Article 3, which restrict data transfers outside regions with insufficient protections.

Residency specs define technical and operational constraints, such as geographic storage boundaries, data encryption at rest, and audit trails for data movement. These configurations are critical for multinational organizations to avoid legal exposure, fines, or service disruptions. They often integrate with compliance frameworks like ISO/IEC 27001 and NIST SP 800-188, which emphasize data governance and jurisdictional controls.

## Key Concepts
| Concept | Definition | Source |
|--------|------------|--------|
| Data Localization | Requirement to store data within specific geographic boundaries | GDPR Article 3 |
| Data Processing Agreement (DPA) | Contractual obligation between data controllers and processors for residency compliance | GDPR Article 28 |
| Data Sovereignty | Legal principle that data is subject to the laws of the jurisdiction where it resides | NIST SP 800-188 |
| Cross-Border Transfer Mechanism | Legal framework (e.g., SCCs) for transferring data outside the EU | GDPR Article 45 |
| Data Residency Boundary | Geographic or legal scope defining where data can be stored/processed | ISO/IEC 27001 |
| Data Replication Policy | Rules for replicating data across regions while maintaining residency compliance | RFC 8199 |
| Jurisdictional Scope | Legal authority over data based on its physical or logical location | EU-US Privacy Shield (invalidated) |
| Data Residency Audit | Verification process to ensure compliance with residency policies | APRA Prudential Standard |

## Industry Standards
- GDPR (General Data Protection Regulation)
- ISO/IEC 27001:2022 (Information Security Management)
- NIST SP 800-188 (Data Residency and Sovereignty)
- RFC 8199 (Data Sovereignty and Cloud Computing)
- EU-US Privacy Shield (replaced by SCCs)
- APRA Prudential Standard CPS 230 (Australia)
- PIPL (Personal Information Protection Law, China)

## Common Patterns
1. **Region-based storage** – Assign data to specific geographic zones based on legal requirements.
2. **Data replication with residency checks** – Replicate data across regions while enforcing residency rules.
3. **Dynamic residency enforcement** – Use automated policies to block non-compliant data transfers.
4. **Jurisdictional tagging** – Label data with legal metadata to enforce residency during processing.
5. **Hybrid cloud residency** – Combine on-premises and cloud storage while adhering to regional laws.

## Pitfalls
- Assuming cloud provider regions map directly to legal jurisdictions (e.g., AWS “EU” regions may not satisfy GDPR).
- Overlooking data transfer clauses in third-party contracts (e.g., SCCs for EU data exports).
- Failing to account for data movement during processing (e.g., analytics workflows crossing borders).
- Hardcoding residency rules without future-proofing for regulatory changes.
- Ignoring data residency in disaster recovery or backup configurations.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[data-residency-builder]] | downstream | 0.59 |
| [[p09_kc_data_residency]] | sibling | 0.58 |
| [[p03_sp_data_residency_builder]] | downstream | 0.48 |
| [[bld_instruction_data_residency]] | downstream | 0.43 |
| [[p10_mem_data_residency_builder]] | downstream | 0.41 |
| [[kc_ai_compliance_gdpr]] | sibling | 0.38 |
| [[p09_qg_data_residency]] | downstream | 0.37 |
| [[bld_schema_data_residency]] | downstream | 0.34 |
| [[bld_collaboration_data_residency]] | downstream | 0.34 |
| [[bld_tools_data_residency]] | downstream | 0.33 |
