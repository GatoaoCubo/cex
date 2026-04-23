---
kind: collaboration
id: bld_collaboration_fhir_agent_capability
pillar: P12
llm_function: COLLABORATE
purpose: How fhir_agent_capability-builder works in crews with other builders
quality: 8.9
title: "Collaboration FHIR Agent Capability"
version: "1.0.0"
author: n06_wave7
tags: [fhir_agent_capability, builder, collaboration, fhir, hl7]
tldr: "How fhir_agent_capability-builder works in crews with other builders"
domain: "fhir_agent_capability construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - fhir-agent-capability-builder
  - p03_sp_fhir_agent_capability_builder
  - bld_architecture_fhir_agent_capability
  - bld_collaboration_agent
  - bld_knowledge_card_fhir_agent_capability
  - bld_tools_fhir_agent_capability
  - bld_collaboration_agent_computer_interface
  - bld_collaboration_llm_evaluation_scenario
  - bld_architecture_kind
  - agent-builder
---

## Crew Role
Composes FHIR-native AI agent capability declarations for EHR onboarding. Specializes the general agent definition for HL7 healthcare compliance requirements.

## Receives From
| Builder                    | What                              | Format    |
|----------------------------|-----------------------------------|-----------|
| agent-builder              | General agent definition          | Markdown  |
| N01 Intelligence           | HL7 AI Office research            | Markdown  |
| Healthcare compliance team | PHI policy + HIPAA requirements   | YAML      |
| EHR vendor team            | CapabilityStatement + SMART config| JSON      |

## Produces For
| Builder / Consumer          | What                              | Format    |
|-----------------------------|-----------------------------------|-----------|
| workflow-builder            | Agent reference for Da Vinci flows| Markdown  |
| handoff_protocol-builder    | FHIR-native protocol adaptation   | YAML      |
| FHIR server registry        | Serialized capability declaration | FHIR JSON |
| N05 Operations              | Deployment + compliance checklist | Markdown  |

## Boundary
Does NOT produce general agent definitions (use `agent-builder`).
Does NOT configure OAuth2 app registration (use `oauth_app_config-builder`).
Does NOT build FHIR workflow specs (use `workflow-builder`).
PHI legal review and IRB approval are outside this builder's scope.
EHR vendor certification testing is coordinated by N05 Operations, not this builder.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[fhir-agent-capability-builder]] | upstream | 0.44 |
| [[p03_sp_fhir_agent_capability_builder]] | upstream | 0.42 |
| [[bld_architecture_fhir_agent_capability]] | upstream | 0.39 |
| [[bld_collaboration_agent]] | sibling | 0.39 |
| [[bld_knowledge_card_fhir_agent_capability]] | upstream | 0.34 |
| [[bld_tools_fhir_agent_capability]] | upstream | 0.32 |
| [[bld_collaboration_agent_computer_interface]] | sibling | 0.32 |
| [[bld_collaboration_llm_evaluation_scenario]] | sibling | 0.32 |
| [[bld_architecture_kind]] | upstream | 0.31 |
| [[agent-builder]] | upstream | 0.31 |
