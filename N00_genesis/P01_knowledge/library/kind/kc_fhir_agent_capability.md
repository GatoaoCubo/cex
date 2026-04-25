---
id: kc_fhir_agent_capability
kind: knowledge_card
8f: F3_inject
title: HL7 FHIR R5 AI Agent Capability Declaration
version: 1.0.0
quality: 8.5
pillar: P01
tldr: "AI agent capability declaration for HL7 FHIR R5 with SMART scopes and PHI handling"
when_to_use: "When building AI agents that interact with healthcare FHIR systems under HIPAA/GDPR constraints"
density_score: 0.98
related:
  - fhir-agent-capability-builder
  - bld_knowledge_card_fhir_agent_capability
  - p03_sp_fhir_agent_capability_builder
  - bld_instruction_fhir_agent_capability
  - bld_tools_fhir_agent_capability
  - p03_sp_healthcare_vertical_builder
  - bld_architecture_fhir_agent_capability
  - healthcare-vertical-builder
  - bld_output_template_fhir_agent_capability
  - bld_instruction_healthcare_vertical
---

**HL7 FHIR R5 AI Agent Capability Declaration**

This card defines the technical capabilities required for AI agents to interact with FHIR R5 systems securely and effectively. Key components include:

1. **SMART on FHIR Scopes**  
   - OAuth 2.0 scopes for read/write access to FHIR resources  
   - Support for SMART Health Card standards  
   - Dynamic client registration capabilities

2. **PHI Handling**  
   - Compliance with HIPAA and GDPR regulations  
   - Anonymization techniques for protected health information  
   - Access control based on role-based permissions

3. **CDS Hooks Integration**  
   - Support for clinical decision support hooks  
   - Real-time interaction with EHR systems  
   - Context-aware recommendation generation

4. **AI Transparency Extension**  
   - Implementation of AI Transparency Extension for FHIR  
   - Metadata tracking for model inputs/outputs  
   - Audit trail for AI-generated clinical recommendations

5. **Security Requirements**  
   - TLS 1.2+ encryption for data in transit  
   - Token-based authentication with JWT support  
   - Regular security vulnerability assessments

**Use Cases**:  
- Clinical decision support systems  
- Patient data analysis tools  
- AI-powered diagnostic assistants  
- Interoperability testing frameworks

**Implementation Notes**:  
- Must include FHIR version 5.0+ compatibility  
- Requires SMART on FHIR implementation  
- Should support both RESTful and messaging interfaces

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[fhir-agent-capability-builder]] | downstream | 0.54 |
| [[bld_knowledge_card_fhir_agent_capability]] | sibling | 0.50 |
| [[p03_sp_fhir_agent_capability_builder]] | downstream | 0.50 |
| [[bld_instruction_fhir_agent_capability]] | downstream | 0.46 |
| [[bld_tools_fhir_agent_capability]] | downstream | 0.45 |
| [[p03_sp_healthcare_vertical_builder]] | downstream | 0.39 |
| [[bld_architecture_fhir_agent_capability]] | downstream | 0.37 |
| [[healthcare-vertical-builder]] | related | 0.36 |
| [[bld_output_template_fhir_agent_capability]] | downstream | 0.36 |
| [[bld_instruction_healthcare_vertical]] | downstream | 0.36 |
