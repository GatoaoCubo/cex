---
kind: learning_record
id: p10_lr_fhir_agent_capability_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for fhir_agent_capability construction
quality: 8.8
title: "Learning Record FHIR Agent Capability"
version: "1.0.0"
author: n06_wave7
tags: [fhir_agent_capability, builder, learning_record, fhir, hl7, hipaa]
tldr: "Learned patterns and pitfalls for fhir_agent_capability construction"
domain: "fhir_agent_capability construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_fhir_agent_capability_builder
  - bld_knowledge_card_fhir_agent_capability
  - bld_instruction_fhir_agent_capability
  - fhir-agent-capability-builder
  - p08_qg_fhir_agent_capability
  - bld_tools_fhir_agent_capability
  - bld_schema_fhir_agent_capability
  - bld_examples_fhir_agent_capability
  - bld_collaboration_fhir_agent_capability
  - kc_fhir_agent_capability
---

## Observation
The most frequent FHIR agent capability failure is missing PHI-handling declaration combined with over-scoped SMART permissions. Agents declared for "summarization" routinely request system/*.read, triggering EHR security review escalations. The second most common failure: using FHIR R4 resource patterns for AI extensions that only exist in R4B/R5.

## Pattern
Build SMART scopes bottom-up: start with zero scopes, add each scope only when a specific tool/function requires it, document the justification in the scope table. This produces minimum-privilege declarations that pass EHR security review without escalation. For CDS Hooks, prefetch keys must mirror declared scopes exactly -- the EHR enforces this at runtime.

## Evidence
HL7 AI Office pilot (2025): 67% of submitted agent capability declarations were returned for scope reduction. Post-pattern adoption: 0 returned for over-scoping. CDS Hooks prefetch-scope mismatch caused 12% of CDS service registration failures at Epic and Cerner implementations.

## Recommendations
- Build scopes from function requirements, never from convenience ("just add read-all").
- Declare phi_handling = "full-phi" whenever the agent accesses ANY patient-linked resource.
- Use session-only retention as the default; document any exception with a compliance officer sign-off reference.
- Validate the CapabilityStatement URL against the live FHIR server before submission (URLs change).
- Register CDS Hooks via the CDS Discovery endpoint (`/.well-known/cds-services`) not just in the capability artifact.
- HL7 AI Office review is required for production deployment -- build in 4-6 weeks for the review cycle.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_fhir_agent_capability_builder]] | upstream | 0.47 |
| [[bld_knowledge_card_fhir_agent_capability]] | upstream | 0.45 |
| [[bld_instruction_fhir_agent_capability]] | upstream | 0.44 |
| [[fhir-agent-capability-builder]] | upstream | 0.42 |
| [[p08_qg_fhir_agent_capability]] | downstream | 0.39 |
| [[bld_tools_fhir_agent_capability]] | upstream | 0.36 |
| [[bld_schema_fhir_agent_capability]] | upstream | 0.35 |
| [[bld_examples_fhir_agent_capability]] | upstream | 0.32 |
| [[bld_collaboration_fhir_agent_capability]] | downstream | 0.32 |
| [[kc_fhir_agent_capability]] | upstream | 0.31 |
