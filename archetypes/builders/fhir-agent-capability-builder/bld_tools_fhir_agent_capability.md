---
kind: tools
id: bld_tools_fhir_agent_capability
pillar: P04
llm_function: CALL
purpose: Tools available for fhir_agent_capability production
quality: 9.0
title: "Tools FHIR Agent Capability"
version: "1.0.0"
author: n06_wave7
tags: [fhir_agent_capability, builder, tools, fhir, hl7, smart-on-fhir]
tldr: "Tools available for fhir_agent_capability production"
domain: "fhir_agent_capability construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - fhir-agent-capability-builder
  - bld_knowledge_card_fhir_agent_capability
  - p03_sp_fhir_agent_capability_builder
  - bld_instruction_fhir_agent_capability
  - bld_tools_healthcare_vertical
  - kc_fhir_agent_capability
  - bld_architecture_fhir_agent_capability
  - bld_collaboration_fhir_agent_capability
  - bld_output_template_fhir_agent_capability
  - p10_mem_healthcare_vertical_builder
---

## Production Tools
| Tool              | Purpose                                         | When                      |
|-------------------|-------------------------------------------------|---------------------------|
| cex_compile.py    | Compile capability YAML from Markdown           | After F6 PRODUCE          |
| cex_score.py      | Peer-review quality scoring (HIPAA gates)       | F7 GOVERN                 |
| cex_retriever.py  | Find similar FHIR capability artifacts          | F3 INJECT / duplicate check|
| cex_doctor.py     | Builder health + schema diagnostics             | Pre-build validation      |
| cex_validator.py  | H01-H08 HARD gate compliance check              | F7 GOVERN                 |

## Validation Tools
| Tool                    | Purpose                                    | When                      |
|-------------------------|--------------------------------------------|---------------------------|
| fhir_validator_cli      | HL7 FHIR R5 resource structure validation  | Phase 3 VALIDATE          |
| smart_scope_linter      | SMART on FHIR v2 scope format check        | Phase 2 COMPOSE           |
| cds_hooks_validator     | CDS Hooks service registration check       | Post-compose              |
| phi_audit_scanner       | Detects over-scoped PHI access             | Phase 3 VALIDATE          |
| hipaa_compliance_check  | Validates audit_log_resource presence      | F7 GOVERN                 |

## External References
- FHIR R5 Validator: `validator.fhir.org` (official HL7 resource validator)
- SMART on FHIR v2 Spec: `hl7.org/fhir/smart-app-launch/` (scope format reference)
- CDS Hooks v2.0: `cds-hooks.org` (hook registration protocol)
- HL7 AI Office: `confluence.hl7.org/display/AIO` (AI agent governance requirements)
- HAPI FHIR: `hapifhir.io` (open-source FHIR server for local testing)
- Inferno Test Suite: `inferno.healthit.gov` (ONC-certified SMART/FHIR conformance testing)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[fhir-agent-capability-builder]] | downstream | 0.62 |
| [[bld_knowledge_card_fhir_agent_capability]] | upstream | 0.61 |
| [[p03_sp_fhir_agent_capability_builder]] | upstream | 0.56 |
| [[bld_instruction_fhir_agent_capability]] | upstream | 0.56 |
| [[bld_tools_healthcare_vertical]] | sibling | 0.55 |
| [[kc_fhir_agent_capability]] | upstream | 0.52 |
| [[bld_architecture_fhir_agent_capability]] | downstream | 0.50 |
| [[bld_collaboration_fhir_agent_capability]] | downstream | 0.49 |
| [[bld_output_template_fhir_agent_capability]] | downstream | 0.43 |
| [[p10_mem_healthcare_vertical_builder]] | downstream | 0.42 |
