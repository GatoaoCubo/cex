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
Declare supported SMART scopes:  
- Read (read patient data)  
- Write (modify patient data)  
- Execute (run clinical actions)  
- Manage (control access/permissions)  

## PHI Handling
Specify data usage policies:  
- De-identified data only  
- Anonymized data only  
- Limited PHI access (with consent)  
- Data retention periods  

## CDS Hooks Integration
Support for clinical decision support:  
- Pre-authorization hooks  
- Order entry hooks  
- Diagnostic suggestion hooks  
- Medication reconciliation hooks  

## AI Transparency Extension
Mandatory metadata requirements:  
- Model version (e.g., v1.2.3)  
- Training data sources  
- Bias mitigation methods  
- Explainability protocols (e.g., SHAP, LIME)  
- Audit trail for AI decisions  

## Purpose
This declaration enables:  
1. Interoperability with FHIR-compliant systems  
2. Trust establishment with healthcare providers  
3. Compliance with HIPAA and GDPR standards  
4. Transparent AI operations in clinical workflows  

