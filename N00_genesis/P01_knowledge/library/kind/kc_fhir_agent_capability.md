---
id: kc_fhir_agent_capability
kind: knowledge_card
title: HL7 FHIR R5 AI Agent Capability Declaration
version: 1.0.0
quality: 8.5
pillar: P01
density_score: 0.98
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
