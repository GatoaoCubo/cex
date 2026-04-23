---
kind: tools
id: bld_tools_workflow_run_crate
pillar: P04
llm_function: CALL
purpose: Tools available for workflow_run_crate production
quality: 8.9
title: "Tools Workflow Run Crate"
version: "1.0.0"
author: n04_wave7
tags: [workflow_run_crate, builder, tools, RO-Crate, Galaxy, rocrate-py, FAIR]
tldr: "Tools available for workflow_run_crate production"
domain: "workflow_run_crate construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_knowledge_card_workflow_run_crate
  - workflow-run-crate-builder
  - p10_lr_workflow_run_crate_builder
  - bld_architecture_workflow_run_crate
  - bld_examples_workflow_run_crate
  - p03_sp_workflow_run_crate_builder
  - bld_instruction_workflow_run_crate
  - bld_collaboration_workflow_run_crate
  - p10_qg_workflow_run_crate
  - bld_output_template_workflow_run_crate
---

## Production Tools
| Tool             | Purpose                                  | When                          |
|------------------|------------------------------------------|-------------------------------|
| cex_compile.py   | Compile crate YAML to JSON-LD            | After draft produced          |
| cex_score.py     | Score crate against quality gates        | Post-production validation    |
| cex_retriever.py | Fetch similar workflow run crate examples| During context assembly       |
| cex_doctor.py    | Validate crate structure and fields      | Pre-commit check              |
| cex_validator.py | JSON-LD context and entity validation    | Schema compliance check       |

## Validation Tools
| Tool               | Purpose                                  | When                          |
|--------------------|------------------------------------------|-------------------------------|
| rocrate-py         | Python RO-Crate library + validator      | Crate creation and validation |
| ro-crate-validator | JSON-LD schema conformance checker       | Profile conformance check     |
| Galaxy export      | Built-in History -> RO-Crate export      | Galaxy run provenance capture |
| WorkflowHub upload | Registry submission + validation         | FAIR publication              |
| orcid_resolver     | Validate ORCID URL format and existence  | Author entity validation      |

## External References
- RO-Crate 1.2 spec: https://www.researchobject.org/ro-crate/specification/1.2/
- Workflow Run Crate: https://w3id.org/ro/terms/workflow-run
- rocrate-py: https://github.com/researchobject/ro-crate-py
- WorkflowHub.eu: https://workflowhub.eu
- Galaxy: https://galaxyproject.org
- BioSchemas ComputationalWorkflow: https://bioschemas.org/profiles/ComputationalWorkflow/

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_workflow_run_crate]] | upstream | 0.66 |
| [[workflow-run-crate-builder]] | downstream | 0.58 |
| [[p10_lr_workflow_run_crate_builder]] | downstream | 0.58 |
| [[bld_architecture_workflow_run_crate]] | downstream | 0.57 |
| [[bld_examples_workflow_run_crate]] | downstream | 0.56 |
| [[p03_sp_workflow_run_crate_builder]] | upstream | 0.48 |
| [[bld_instruction_workflow_run_crate]] | upstream | 0.46 |
| [[bld_collaboration_workflow_run_crate]] | downstream | 0.41 |
| [[p10_qg_workflow_run_crate]] | downstream | 0.41 |
| [[bld_output_template_workflow_run_crate]] | downstream | 0.41 |
