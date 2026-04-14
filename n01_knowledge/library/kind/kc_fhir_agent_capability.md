---
id: kc_fhir_agent_capability
kind: knowledge_card
title: HL7 FHIR R5 AI Agent Capability Declaration
version: 1.0.0
quality: null
pillar: P01
---

# HL7 FHIR R5 AI Agent Capability Declaration

## SMART on FHIR Scopes
Declare supported scopes:  
- Read (patient data access)  
- Write (data modification)  
- Execute (clinical actions)  
- Manage (access control)  

## PHI Handling
Specify data policies:  
- De-identified data only  
- Anonymized data only  
- Limited PHI access (with consent)  
- Retention periods defined  

## CDS Hooks Integration
Support for:  
- Pre-authorization hooks  
- Order entry hooks  
- Diagnostic suggestion hooks  
- Medication reconciliation hooks  

## AI Transparency Extension
Mandatory metadata:  
- Model version (e.g., v1.2.3)  
- Training data sources  
- Bias mitigation methods  
- Explainability protocols (SHAP, LIME)  
- Audit trail for decisions  

## Purpose
Enables:  
1. FHIR-compliant interoperability  
2. HIPAA/GDPR compliance  
3. Transparent clinical AI operations  
4. Secure healthcare data processing
```