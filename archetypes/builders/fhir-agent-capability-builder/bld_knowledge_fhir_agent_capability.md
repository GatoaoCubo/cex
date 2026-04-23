---
kind: knowledge_card
id: bld_knowledge_card_fhir_agent_capability
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for fhir_agent_capability production
quality: 9.2
title: "Knowledge Card FHIR Agent Capability"
version: "1.0.0"
author: n06_wave7
tags: [fhir_agent_capability, builder, knowledge_card, fhir, hl7, smart-on-fhir, healthcare]
tldr: "Domain knowledge for fhir_agent_capability production"
domain: "fhir_agent_capability construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - fhir-agent-capability-builder
  - p03_sp_fhir_agent_capability_builder
  - bld_instruction_fhir_agent_capability
  - bld_tools_fhir_agent_capability
  - kc_fhir_agent_capability
  - bld_collaboration_fhir_agent_capability
  - p10_lr_fhir_agent_capability_builder
  - bld_output_template_fhir_agent_capability
  - bld_schema_fhir_agent_capability
  - p10_mem_healthcare_vertical_builder
---

## Domain Overview
FHIR (Fast Healthcare Interoperability Resources) R5 is the HL7 standard for healthcare data exchange. The HL7 AI Office (launched 2025) introduced the Agent-as-Resource pattern: representing AI agents as first-class FHIR resources with declared capabilities, authorization scopes, and PHI-handling policies. A fhir_agent_capability artifact is the FHIR-native analog of CEX's agent_card, specialized for healthcare AI regulatory compliance and EHR system integration.

SMART on FHIR (Substitutable Medical Applications and Reusable Technologies) provides OAuth2-based authorization for healthcare apps and agents. SMART v2 (2021+) adds granular resource-level scopes, contextual launch parameters, and token introspection -- critical for AI agent least-privilege access.

CDS Hooks is the HL7 standard for EHR-integrated clinical decision support. AI agents register as CDS services and respond to hook invocations (patient-view, order-select, order-sign) with FHIR-structured guidance cards.

## Key Concepts
| Concept | Definition | Source |
|---------|-----------|--------|
| Agent-as-Resource | FHIR resource representing an AI agent with capabilities, scopes, and PHI policy | HL7 AI Office WG 2026 |
| SMART on FHIR v2 | OAuth2 framework for healthcare app/agent authorization with resource-level scopes | HL7 SMART App Launch 2.0 |
| CDS Hooks | EHR-native hook system for real-time AI clinical decision support | CDS Hooks v2.0 specification |
| PHI | Protected Health Information under HIPAA: individually identifiable health data | HIPAA 45 CFR 164 |
| FHIR CapabilityStatement | Machine-readable declaration of what a FHIR server/client can do | FHIR R5 spec |
| AuditEvent | FHIR resource recording who accessed what PHI, when, and why | FHIR R5 AuditEvent resource |
| AI Transparency | HL7 extension for logging AI influence on clinical decisions in FHIR | HL7 AI Transparency project 2025 |
| Da Vinci | HL7 project: payer-provider FHIR workflows (prior auth, coverage, claims) | HL7 Da Vinci WG |
| ICD-10/CPT Coding | Clinical coding: diagnosis (ICD-10) and procedure (CPT) classification | WHO ICD-10 / AMA CPT |
| PHI De-identification | Removing 18 HIPAA identifiers from data for research/analytics use | HIPAA Safe Harbor method |

## Industry Standards
- HL7 FHIR R5: `hl7.org/fhir/R5/` (canonical resource definitions)
- SMART on FHIR v2: `hl7.org/fhir/smart-app-launch/` (OAuth2 scopes spec)
- CDS Hooks v2.0: `cds-hooks.org` (EHR hook invocation protocol)
- HL7 AI Office: `confluence.hl7.org/display/AIO` (AI agent governance 2025)
- HIPAA 45 CFR 164: PHI definition, minimum necessary standard, audit requirements
- ISO 27799: Health informatics security management (complements ISO 27001)
- GDPR Article 9: Special category health data processing requirements (EU)

## Common Patterns
1. Declare minimum-privilege SMART scopes before writing the capability body.
2. Use session-only data retention for real-time CDS to minimize PHI risk.
3. Register every AI-influenced clinical decision with AuditEvent-AI-influence extension.
4. CDS Hooks prefetch keys should mirror the SMART scopes (no fetching beyond declared scopes).
5. AI Transparency extension is mandatory per HL7 AI Office 2025 -- include model_id and training_data_statement.
6. Validate against FHIR CapabilityStatement of the target EHR system before onboarding.

## Pitfalls
- Declaring wildcard SMART scopes (system/*.read) -- violates minimum-privilege, blocked by most EHRs.
- Forgetting audit_log_resource when phi_handling=full-phi -- HIPAA violation risk.
- Using FHIR R4 patterns -- AI extensions (Agent-as-Resource, AI Transparency) require R4B or R5.
- Conflating CDS Hooks (EHR-integrated) with standalone API calls (no hook context).
- Missing AI Transparency extension -- HL7 AI Office 2025 rejects capabilities without it.
- Stale CapabilityStatement reference -- EHR systems update FHIR servers; verify URL at onboarding time.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[fhir-agent-capability-builder]] | downstream | 0.78 |
| [[p03_sp_fhir_agent_capability_builder]] | downstream | 0.74 |
| [[bld_instruction_fhir_agent_capability]] | downstream | 0.70 |
| [[bld_tools_fhir_agent_capability]] | downstream | 0.68 |
| [[kc_fhir_agent_capability]] | sibling | 0.65 |
| [[bld_collaboration_fhir_agent_capability]] | downstream | 0.57 |
| [[p10_lr_fhir_agent_capability_builder]] | downstream | 0.57 |
| [[bld_output_template_fhir_agent_capability]] | downstream | 0.54 |
| [[bld_schema_fhir_agent_capability]] | downstream | 0.54 |
| [[p10_mem_healthcare_vertical_builder]] | downstream | 0.53 |
