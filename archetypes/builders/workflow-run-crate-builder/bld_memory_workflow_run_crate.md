---
kind: learning_record
id: p10_lr_workflow_run_crate_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for workflow_run_crate construction
quality: 8.8
title: "Learning Record Workflow Run Crate"
version: "1.0.0"
author: n04_wave7
tags: [workflow_run_crate, builder, learning_record, RO-Crate, workflow-run, research-object, provenance-graph, ORCID, Galaxy]
tldr: "Learned patterns and pitfalls for workflow_run_crate construction"
domain: "workflow_run_crate construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - workflow-run-crate-builder
  - bld_knowledge_card_workflow_run_crate
  - p03_sp_workflow_run_crate_builder
  - bld_tools_workflow_run_crate
  - bld_architecture_workflow_run_crate
  - bld_instruction_workflow_run_crate
  - bld_examples_workflow_run_crate
  - p10_qg_workflow_run_crate
  - bld_collaboration_workflow_run_crate
  - bld_output_template_workflow_run_crate
---

## Observation
Most workflow provenance records use ad-hoc formats (log files, README.txt, spreadsheets). RO-Crate Workflow Run Crate standardizes this into a machine-readable, FAIR-compliant JSON-LD package. The most common error: generating a crate without the CreateAction entity, which removes the provenance graph spine entirely.

## Pattern
Always start with CreateAction: identify the workflow (instrument), inputs (object array), outputs (result array), and researcher (agent ORCID). Build Dataset entities around this spine. The crate is a star graph with CreateAction at center.

## Evidence
Galaxy EuroScienceGateway project (Horizon Europe, ended Aug 2025) produced 3000+ Workflow Run Crates. WorkflowHub.eu hosts 1200+ workflows with RO-Crate metadata. RO-Crate 1.2 stable spec released 2025. Workflow Run Crate profile now stable (was draft in 1.1 era).

## Recommendations
- Always build CreateAction first (it defines the provenance graph structure).
- Use ORCID URLs as Person @id -- never local IDs.
- Include sha256 checksums for all input/output datasets.
- Use RO-Crate 1.2 context URL (not 1.1 -- breaking context change).
- For Galaxy runs: use Galaxy's built-in RO-Crate export (History -> Export as RO-Crate) as baseline.
- For multi-step workflows: nest CreateAction entities (parent run -> step runs).
- Test validation with rocrate-py validate command before submission to WorkflowHub.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[workflow-run-crate-builder]] | related | 0.66 |
| [[bld_knowledge_card_workflow_run_crate]] | upstream | 0.65 |
| [[p03_sp_workflow_run_crate_builder]] | upstream | 0.62 |
| [[bld_tools_workflow_run_crate]] | upstream | 0.59 |
| [[bld_architecture_workflow_run_crate]] | upstream | 0.57 |
| [[bld_instruction_workflow_run_crate]] | upstream | 0.55 |
| [[bld_examples_workflow_run_crate]] | upstream | 0.53 |
| [[p10_qg_workflow_run_crate]] | downstream | 0.53 |
| [[bld_collaboration_workflow_run_crate]] | downstream | 0.49 |
| [[bld_output_template_workflow_run_crate]] | upstream | 0.37 |
