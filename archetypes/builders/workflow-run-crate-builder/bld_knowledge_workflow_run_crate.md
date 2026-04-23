---
kind: knowledge_card
id: bld_knowledge_card_workflow_run_crate
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for workflow_run_crate production
quality: 9.2
title: "Knowledge Card Workflow Run Crate"
version: "1.0.0"
author: n04_wave7
tags: [workflow_run_crate, builder, knowledge_card, RO-Crate, workflow-run, research-object, provenance-graph, ORCID, Galaxy, input-dataset, output-dataset, metadata]
tldr: "Domain knowledge for workflow_run_crate production"
domain: "workflow_run_crate construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - workflow-run-crate-builder
  - bld_examples_workflow_run_crate
  - p03_sp_workflow_run_crate_builder
  - bld_tools_workflow_run_crate
  - p10_lr_workflow_run_crate_builder
  - bld_instruction_workflow_run_crate
  - bld_collaboration_workflow_run_crate
  - bld_architecture_workflow_run_crate
  - p10_qg_workflow_run_crate
  - bld_output_template_workflow_run_crate
---

## Domain Overview
RO-Crate (Research Object Crate) is a community specification for packaging research data with structured metadata, built on schema.org and JSON-LD. The Workflow Run Crate profile (stable as of 2025) extends RO-Crate to document the execution provenance of computational workflows: which inputs were used, which workflow ran, what outputs were produced, who executed it (ORCID), and what software environment was active.

Developed as part of the EuroScienceGateway project (Horizon Europe), Workflow Run Crate is natively supported by Galaxy (the scientific workflow platform used by >200K researchers), WorkflowHub.eu, and Snakemake. It enables reproducibility, FAIR data principles, and cross-platform workflow provenance interoperability.

## Key Concepts
| Concept | Definition | Source |
|---------|-----------|--------|
| RO-Crate | Research Object packaging spec with JSON-LD metadata | researchobject.org/ro-crate |
| Workflow Run Crate | RO-Crate profile for workflow execution provenance | w3id.org/ro/terms/workflow-run |
| ro-crate-metadata.json | Root metadata file; required in every RO-Crate | RO-Crate 1.2 Spec |
| CreateAction | schema.org action recording workflow execution event | schema.org/CreateAction |
| ComputationalWorkflow | BioSchemas type for workflow definition entity | bioschemas.org/ComputationalWorkflow |
| ORCID | Open Researcher and Contributor ID; persistent author identifier | orcid.org |
| FAIR | Findable, Accessible, Interoperable, Reusable data principles | GO FAIR Initiative |
| FAIR Signposting | Link header pattern for web-accessible resource discovery | signposting.org |
| Galaxy | Open-source scientific workflow platform | galaxyproject.org |
| WorkflowHub | European workflow registry for FAIR workflow sharing | workflowhub.eu |

## RO-Crate 1.2 Required Entities
| Entity Type | @type | Required Fields |
|-------------|-------|-----------------|
| Metadata file descriptor | CreativeWork | about, conformsTo |
| Root Dataset | Dataset | name, description, datePublished, license |
| Computational Workflow | File + SoftwareSourceCode + ComputationalWorkflow | name, programmingLanguage |
| Execution Action | CreateAction | instrument, object, result, agent, startTime, endTime |
| Author | Person | @id (ORCID URL), name |
| Input/Output | Dataset or File | name, sha256, encodingFormat |

## Workflow Language @id References
| Engine | @id IRI | Notes |
|--------|---------|-------|
| Galaxy | https://galaxyproject.org | .ga format |
| Nextflow | https://www.nextflow.io | .nf format |
| CWL | https://w3id.org/cwl/v1.2 | .cwl format |
| Snakemake | https://snakemake.readthedocs.io | Snakefile |
| WDL | https://openwdl.org | .wdl format |

## Industry Standards
- RO-Crate 1.2: https://www.researchobject.org/ro-crate/specification/1.2/
- Workflow Run Crate 1.0: https://w3id.org/ro/terms/workflow-run
- BioSchemas ComputationalWorkflow: https://bioschemas.org/profiles/ComputationalWorkflow/
- FAIR Principles (Wilkinson et al. 2016, Nature Scientific Data)
- ORCID Standard: https://orcid.org/
- schema.org/CreateAction: https://schema.org/CreateAction

## Common Patterns
1. Galaxy run export: Galaxy generates invocation JSON -> convert to Workflow Run Crate.
2. Nextflow run: .nextflow.log + params.json -> CreateAction + input/output Dataset entities.
3. Multi-step workflow: one CreateAction per step, nested within parent CreateAction.
4. Container provenance: SoftwareApplication entity per Docker image used in workflow.

## Pitfalls
- Omitting CreateAction entity (most common error; breaks provenance graph entirely).
- Using local IDs for Person @id instead of ORCID URLs (breaks FAIR Signposting).
- Missing sha256 on input/output datasets (defeats reproducibility verification).
- Using old RO-Crate context URL (1.1 vs 1.2 context URLs differ).
- Confusing Workflow RO-Crate (executable package) with Workflow Run Crate (execution provenance).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[workflow-run-crate-builder]] | downstream | 0.70 |
| [[bld_examples_workflow_run_crate]] | downstream | 0.68 |
| [[p03_sp_workflow_run_crate_builder]] | downstream | 0.65 |
| [[bld_tools_workflow_run_crate]] | downstream | 0.61 |
| [[p10_lr_workflow_run_crate_builder]] | downstream | 0.58 |
| [[bld_instruction_workflow_run_crate]] | downstream | 0.55 |
| [[bld_collaboration_workflow_run_crate]] | downstream | 0.55 |
| [[bld_architecture_workflow_run_crate]] | downstream | 0.53 |
| [[p10_qg_workflow_run_crate]] | downstream | 0.48 |
| [[bld_output_template_workflow_run_crate]] | downstream | 0.45 |
