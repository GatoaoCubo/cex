---
kind: instruction
id: bld_instruction_healthcare_vertical
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for healthcare_vertical
quality: null
title: "Instruction Healthcare Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [healthcare_vertical, builder, instruction]
tldr: "Step-by-step production process for healthcare_vertical"
domain: "healthcare_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Study HIPAA compliance requirements for data encryption and access controls.  
2. Analyze HL7/FHIR standards for interoperability in EHR systems.  
3. Map PHI (Protected Health Information) handling workflows in clinical settings.  
4. Identify use cases for secure data exchange between hospitals and insurers.  
5. Evaluate risks in non-compliant data processing for healthcare applications.  
6. Review industry benchmarks for healthcare data privacy and security.  

## Phase 2: COMPOSE  
1. Align artifact structure with SCHEMA.md's healthcare-specific data models.  
2. Define PHI fields using FHIR resources (e.g., Patient, Encounter).  
3. Implement HIPAA-compliant encryption protocols in data transmission layers.  
4. Write use cases for telemedicine and remote patient monitoring.  
5. Reference HL7 v2.x messaging formats for legacy system integration.  
6. Embed audit logging requirements per HIPAA audit controls.  
7. Use OUTPUT_TEMPLATE.md to format artifact with metadata headers.  
8. Validate terminology against SNOMED-CT and LOINC standards.  
9. Finalize artifact with compliance checklists and versioning metadata.  

## Phase 3: VALIDATE  
- [ ] ✅ Confirm HIPAA compliance in data storage and transmission.  
- [ ] ✅ Verify HL7/FHIR conformance using FHIR Validator tool.  
- [ ] ✅ Ensure PHI fields are anonymized in sample datasets.  
- [ ] ✅ Test use cases against SCHEMA.md's validation rules.  
- [ ] ✅ Cross-check artifact against OUTPUT_TEMPLATE.md structure.
