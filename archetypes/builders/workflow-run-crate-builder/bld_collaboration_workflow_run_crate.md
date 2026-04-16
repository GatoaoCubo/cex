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
