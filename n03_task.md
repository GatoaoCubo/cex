---
id: kc_fhir_agent_capability
kind: knowledge_card
title: FHIR Agent Capability Declaration
version: 1.0.0
quality: null
pillar: P01
---

# HL7 FHIR R5 AI Agent Capability Declaration

## SMART on FHIR Scopes
AI agents must declare requested SMART scopes (launch context, read/write access) using FHIR CapabilityStatement resources. This enables secure, context-aware interactions with EHR systems.

## PHI Handling
Compliance with HIPAA and GDPR requires explicit declaration of:
- Data access levels (read/write)
- Anonymization protocols
- Consent management mechanisms
- Audit trail requirements

## CDS Hooks Integration
Support for Clinical Decision Support (CDS) Hooks through:
- `launch-context` for context-aware recommendations
- `event` hooks for real-time clinical decision support
- `subscription` management for persistent alerts

## AI Transparency Extension
Mandatory inclusion of:
- Model metadata (training data, version)
- Bias mitigation strategies
- Explainability mechanisms
- Human oversight protocols

## Summary
This capability declaration ensures safe, compliant AI interactions with health systems through standardized FHIR resources, transparent operations, and strict data governance.
