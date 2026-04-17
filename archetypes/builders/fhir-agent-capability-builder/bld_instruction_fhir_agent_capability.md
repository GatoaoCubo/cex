---
kind: instruction
id: bld_instruction_fhir_agent_capability
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for fhir_agent_capability
quality: 8.9
title: "Instruction FHIR Agent Capability"
version: "1.0.0"
author: n06_wave7
tags: [fhir_agent_capability, builder, instruction, fhir, hl7]
tldr: "Step-by-step production process for fhir_agent_capability"
domain: "fhir_agent_capability construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH
1. Identify clinical AI use case: CDS, summarization, coding (ICD/CPT), documentation, or scheduling.
2. Map use case to HL7 FHIR capability category using AI Office 2025 taxonomy.
3. Determine FHIR resource access requirements: which resources the agent reads/writes (Patient, Observation, Condition, MedicationRequest, etc.).
4. Identify SMART on FHIR authorization scopes required for each resource access (e.g., `patient/Patient.read`).
5. Audit PHI exposure: does the agent process, retain, or transmit Protected Health Information?
6. Check CDS Hooks integration: does the agent expose hooks (patient-view, order-select, order-sign)?
7. Review HL7 AI Office transparency requirements for the declared capability.

## Phase 2: COMPOSE
1. Reference SCHEMA.md for required fields (agent_id, fhir_version, capability_category, smart_scopes).
2. Declare capability_category: CDS / summarization / coding / documentation / scheduling.
3. Specify SMART on FHIR scopes as minimum-privilege list (principle of least privilege).
4. Define PHI-handling declaration: data_retention_policy, de_identification_standard, audit_log_resource.
5. Specify CDS Hooks: hook_id, context_resources, prefetch_keys (if applicable).
6. Map agent tools to FHIR resource operations (read, write, search, create).
7. Reference AI Transparency extension: model_id, training_data_statement, explainability_method.
8. Validate authorization_scopes are consistent with SMART on FHIR v2 specification.
9. Include FHIR CapabilityStatement reference (the FHIR server this agent is certified for).

## Phase 3: VALIDATE
- [ ] agent_id follows pattern `p08_fhir_[capability_slug].md`
- [ ] fhir_version is "R5" (or explicitly R4B with migration note)
- [ ] capability_category is from HL7 taxonomy: CDS/summarization/coding/documentation/scheduling
- [ ] smart_scopes follow SMART on FHIR v2 format: `{{system}}/{{resource}}.{{action}}`
- [ ] PHI-handling declaration present if agent processes patient data
- [ ] audit_log_resource references a valid FHIR AuditEvent extension
- [ ] CDS Hooks declared if agent provides EHR-integrated decision support
- [ ] AI Transparency extension present (HL7 AI Office requirement)
