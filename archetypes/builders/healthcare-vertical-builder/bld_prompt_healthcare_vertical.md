---
kind: instruction
id: bld_instruction_healthcare_vertical
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for healthcare_vertical
quality: 8.9
title: "Instruction Healthcare Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [healthcare_vertical, builder, instruction]
tldr: "Step-by-step production process for healthcare_vertical"
domain: "healthcare_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_knowledge_card_healthcare_vertical
  - p03_sp_healthcare_vertical_builder
  - healthcare-vertical-builder
  - p01_qg_healthcare_vertical
  - p10_mem_healthcare_vertical_builder
  - bld_examples_healthcare_vertical
  - kc_healthcare_vertical
  - bld_knowledge_card_fhir_agent_capability
  - kc_fhir_agent_capability
  - p03_sp_fhir_agent_capability_builder
---

## Phase 1: RESEARCH  
1. Study HIPAA compliance requirements for data encryption and access controls.  
2. Analyze HL7/FHIR standards for interoperability in EHR systems.  
3. Map PHI (Protected Health Information) handling workflows in clinical settings.  
4. Identify use cases for secure data exchange between hospitals and insurers.  
5. Evaluate risks in non-compliant data processing for healthcare applications.  
6. Review industry benchmarks for healthcare data privacy and security.  

## Phase 2: COMPOSE
1. Align artifact structure with bld_schema_healthcare_vertical.md's data models.
2. Define PHI fields using FHIR resources (e.g., Patient, Encounter, Observation).
3. Implement HIPAA-compliant encryption protocols (AES-256 at rest, TLS 1.2+ in transit).
4. Write use cases for telemedicine, remote patient monitoring, and clinical decision support.
5. Reference HL7 v2.x messaging formats (ADT, ORU) for legacy system integration.
6. Embed audit logging requirements per HIPAA Security Rule (45 CFR 164.312(b)).
7. Use bld_output_template_healthcare_vertical.md to format artifact with metadata headers.
8. Validate terminology against SNOMED-CT and LOINC standards.
9. Finalize artifact with BAA requirements, Safe Harbor de-identification, and versioning metadata.

## Phase 3: VALIDATE
- [ ] [OK] Confirm HIPAA Privacy + Security Rule compliance (45 CFR 164).
- [ ] [OK] Verify HL7/FHIR R4 conformance using FHIR Validator tool.
- [ ] [OK] Ensure PHI de-identification follows Safe Harbor (18 identifiers removed per 45 CFR 164.514(b)).
- [ ] [OK] Test use cases against bld_schema_healthcare_vertical.md validation rules.
- [ ] [OK] Cross-check artifact against bld_output_template_healthcare_vertical.md structure.
- [ ] [OK] Verify BAA requirements documented if covered entity relationship exists.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_healthcare_vertical]] | upstream | 0.47 |
| [[p03_sp_healthcare_vertical_builder]] | related | 0.45 |
| [[healthcare-vertical-builder]] | upstream | 0.41 |
| [[p01_qg_healthcare_vertical]] | downstream | 0.40 |
| [[p10_mem_healthcare_vertical_builder]] | downstream | 0.38 |
| [[bld_examples_healthcare_vertical]] | downstream | 0.36 |
| [[kc_healthcare_vertical]] | upstream | 0.33 |
| [[bld_knowledge_card_fhir_agent_capability]] | upstream | 0.32 |
| [[kc_fhir_agent_capability]] | upstream | 0.32 |
| [[p03_sp_fhir_agent_capability_builder]] | related | 0.28 |
