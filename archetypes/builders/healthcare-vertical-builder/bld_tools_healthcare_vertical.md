---
kind: tools
id: bld_tools_healthcare_vertical
pillar: P04
llm_function: CALL
purpose: Tools available for healthcare_vertical production
quality: 8.9
title: "Tools Healthcare Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [healthcare_vertical, builder, tools]
tldr: "Tools available for healthcare_vertical production"
domain: "healthcare_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_legal_vertical
  - bld_tools_fhir_agent_capability
  - fhir-agent-capability-builder
  - bld_architecture_fhir_agent_capability
  - bld_collaboration_fhir_agent_capability
  - bld_knowledge_card_fhir_agent_capability
  - bld_tools_fintech_vertical
  - bld_tools_github_issue_template
  - p03_sp_fhir_agent_capability_builder
  - bld_tools_pricing_page
---

## Production Tools
| Tool | Purpose (healthcare context) | When |
|---|---|---|
| cex_compile.py | Compile healthcare_vertical artifact to YAML + validate frontmatter | After authoring |
| cex_score.py | Score artifact against H01-H10 gates and 8D SOFT dimensions | Before publish |
| cex_retriever.py | Retrieve similar HIPAA/FHIR artifacts from knowledge library | During research |
| cex_doctor.py | Health-check builder ISO completeness and frontmatter validity | QA pass |

## Validation Tools
| Tool | Purpose | When |
|---|---|---|
| cex_wave_validator.py | Validate all 13 ISOs in builder directory | Post-build |
| cex_hygiene.py | Enforce naming, frontmatter, ASCII rules | Pre-commit |

## External References
- HL7 FHIR R4 Validator (https://validator.fhir.org/) -- conformance testing
- SMART on FHIR -- EHR app authorization
- CDC PHIN VADS -- vocabulary server for SNOMED-CT/LOINC lookups

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_legal_vertical]] | sibling | 0.49 |
| [[bld_tools_fhir_agent_capability]] | sibling | 0.46 |
| [[fhir-agent-capability-builder]] | downstream | 0.37 |
| [[bld_architecture_fhir_agent_capability]] | downstream | 0.35 |
| [[bld_collaboration_fhir_agent_capability]] | downstream | 0.34 |
| [[bld_knowledge_card_fhir_agent_capability]] | upstream | 0.34 |
| [[bld_tools_fintech_vertical]] | sibling | 0.32 |
| [[bld_tools_github_issue_template]] | sibling | 0.32 |
| [[p03_sp_fhir_agent_capability_builder]] | upstream | 0.31 |
| [[bld_tools_pricing_page]] | sibling | 0.31 |
