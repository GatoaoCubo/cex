---
kind: schema
id: bld_schema_workflow_run_crate
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for workflow_run_crate
quality: 9.2
title: "Schema Workflow Run Crate"
version: "1.0.0"
author: n04_wave7
tags: [workflow_run_crate, builder, schema, RO-Crate, workflow-run, CreateAction, ORCID, provenance-graph]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for workflow_run_crate"
domain: "workflow_run_crate construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - bld_schema_reranker_config
  - bld_schema_search_strategy
  - bld_schema_benchmark_suite
  - bld_schema_pitch_deck
  - bld_schema_sandbox_config
  - bld_schema_quickstart_guide
  - bld_schema_multimodal_prompt
  - bld_schema_rl_algorithm
---

## Frontmatter Fields
### Required
| Field              | Type    | Required | Default | Notes |
|--------------------|---------|----------|---------|-------|
| id                 | string  | yes      |         | p10_wrc_{{name}}.md |
| kind               | string  | yes      |         | Must be "workflow_run_crate" |
| pillar             | string  | yes      |         | P10 |
| title              | string  | yes      |         | Workflow name + run identifier |
| version            | string  | yes      |         | Semantic version |
| created            | date    | yes      |         | ISO 8601 date |
| updated            | date    | yes      |         | ISO 8601 date |
| author             | string  | yes      |         | Generating nucleus or agent |
| domain             | string  | yes      |         | Scientific domain (bioinformatics, genomics, ai-ml) |
| quality            | null    | yes      | null    | Never self-score; peer review assigns |
| tags               | array   | yes      |         | Must include: RO-Crate, workflow-run, provenance-graph |
| tldr               | string  | yes      |         | One-line description of workflow and run |
| workflow_language  | string  | yes      |         | Galaxy, Nextflow, CWL, Snakemake, WDL |
| run_id             | string  | yes      |         | Unique execution identifier |
| agent_orcid        | string  | yes      |         | ORCID URL of executing researcher |
| input_count        | integer | yes      |         | Number of input datasets |
| output_count       | integer | yes      |         | Number of output datasets |

### Recommended
| Field             | Type   | Notes |
|-------------------|--------|-------|
| start_time        | string | ISO 8601 execution start |
| end_time          | string | ISO 8601 execution end |
| container_image   | string | Docker/Singularity image reference |
| license           | string | SPDX license identifier |
| galaxy_run_url    | string | Galaxy instance run URL |

## ID Pattern
^p10_wrc_[a-z][a-z0-9_]+\.md$

## Body Structure
1. **RO-Crate Metadata** - ro-crate-metadata.json root descriptor
2. **Workflow Entity** - ComputationalWorkflow with BioSchemas metadata
3. **Provenance Graph** - CreateAction linking inputs, workflow, outputs, agent
4. **Input Datasets** - Dataset entities with checksums and licenses
5. **Output Datasets** - Dataset entities with checksums and creation dates
6. **Software Environment** - SoftwareApplication entities per tool
7. **Author Attribution** - Person entities with ORCID IDs and affiliations

## Constraints
- All required fields must be present and valid.
- id must match the regex pattern exactly.
- agent_orcid must be a full ORCID URL (https://orcid.org/XXXX-XXXX-XXXX-XXXX).
- workflow_language must be a recognized scientific workflow engine.
- run_id must be unique within the domain.
- input_count and output_count must match actual entity counts in Body.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.65 |
| [[bld_schema_dataset_card]] | sibling | 0.64 |
| [[bld_schema_reranker_config]] | sibling | 0.64 |
| [[bld_schema_search_strategy]] | sibling | 0.63 |
| [[bld_schema_benchmark_suite]] | sibling | 0.63 |
| [[bld_schema_pitch_deck]] | sibling | 0.63 |
| [[bld_schema_sandbox_config]] | sibling | 0.63 |
| [[bld_schema_quickstart_guide]] | sibling | 0.62 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.62 |
| [[bld_schema_rl_algorithm]] | sibling | 0.61 |
