---
kind: collaboration
id: bld_collaboration_workflow_run_crate
pillar: P12
llm_function: COLLABORATE
purpose: How workflow_run_crate-builder works in crews with other builders
quality: 8.9
title: "Collaboration Workflow Run Crate"
version: "1.0.0"
author: n04_wave7
tags: [workflow_run_crate, builder, collaboration, RO-Crate, Galaxy, ORCID, FAIR]
tldr: "How workflow_run_crate-builder works in crews with other builders"
domain: "workflow_run_crate construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - workflow-run-crate-builder
  - p03_sp_workflow_run_crate_builder
  - bld_knowledge_card_workflow_run_crate
  - bld_architecture_workflow_run_crate
  - bld_collaboration_workflow_node
  - bld_collaboration_workflow
  - workflow-builder
  - p10_lr_workflow_run_crate_builder
  - bld_collaboration_visual_workflow
  - bld_collaboration_vc_credential
---

## Crew Role
Packages scientific workflow execution provenance as FAIR-compliant RO-Crate 1.2 artifacts, enabling reproducibility verification and cross-platform workflow provenance sharing.

## Receives From
| Builder                   | What                               | Format        |
|---------------------------|------------------------------------|---------------|
| workflow-builder (P12)    | Workflow definition file           | .ga/.nf/.cwl  |
| dataset-card-builder (P01)| Input dataset metadata + checksums | YAML          |
| N05 operations nucleus    | Execution logs, run parameters     | JSON/text     |
| vc-credential-builder     | Researcher ORCID VC for agent field| JSON-LD       |

## Produces For
| Builder                  | What                               | Format        |
|--------------------------|------------------------------------|---------------|
| WorkflowHub.eu registry  | RO-Crate for workflow registry     | ZIP + JSON-LD |
| Zenodo data repository   | FAIR dataset deposit               | ZIP           |
| compliance-framework     | Provenance audit record            | JSON-LD       |
| research reproducibility | Full execution package             | RO-Crate ZIP  |

## Boundary
Does NOT handle: Galaxy workflow definition creation (use workflow-builder), raw dataset collection (use dataset_card), software container builds (use sandbox_config), or W3C agent identity credentials (use vc-credential-builder). Focus is strictly execution provenance packaging.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[workflow-run-crate-builder]] | upstream | 0.49 |
| [[p03_sp_workflow_run_crate_builder]] | upstream | 0.39 |
| [[bld_knowledge_card_workflow_run_crate]] | upstream | 0.37 |
| [[bld_architecture_workflow_run_crate]] | upstream | 0.36 |
| [[bld_collaboration_workflow_node]] | sibling | 0.33 |
| [[bld_collaboration_workflow]] | sibling | 0.31 |
| [[workflow-builder]] | related | 0.30 |
| [[p10_lr_workflow_run_crate_builder]] | upstream | 0.29 |
| [[bld_collaboration_visual_workflow]] | sibling | 0.29 |
| [[bld_collaboration_vc_credential]] | sibling | 0.28 |
