---
kind: architecture
id: bld_architecture_compliance_framework
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of compliance_framework -- inventory, dependencies
quality: 8.9
title: "Architecture Compliance Framework"
version: "1.1.0"
author: n05_ops
tags: [compliance_framework, builder, architecture]
tldr: "Component map of compliance_framework -- inventory, dependencies"
domain: "compliance_framework construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Component Inventory  
| Name | Role | Owner | Status |  
|------|------|-------|--------|  
| Policy Engine | Core compliance logic | Compliance Team | Active |  
| Rule Validator | Validates rules against standards | DevOps | In Development |  
| Audit Logger | Logs compliance events | Security | Active |  
| Data Store | Stores compliance data | DB Team | Active |  
| User Interface | Configures framework | UX Team | In Development |  
| Compliance Reporter | Generates reports | Analytics | Active |  
| Configuration Manager | Manages framework settings | DevOps | Active |  

## Dependencies  
| From | To | Type |  
|------|----|------|  
| Policy Engine | Rule Validator | Validation |  
| Rule Validator | Data Store | Storage |  
| Audit Logger | Data Store | Storage |  
| User Interface | Policy Engine | Control |  
| Compliance Reporter | Audit Logger | Reporting |  

## Architectural Position  
The compliance_framework-builder sits within CEX's P11 Feedback pillar as the external regulatory mapping module. It consumes outputs from threat_model (risk exposure data), incident_report (breach notifications triggering GDPR Art. 33 obligations), and safety_policy (internal rules to cross-reference). It produces compliance attestations consumed by audit processes, legal teams, and external regulators. Covers GDPR, EU AI Act, NIST AI RMF, ISO 42001, HIPAA, and sector-specific regulations. Does NOT enforce runtime safety (guardrail) or detect threats (threat_model).
