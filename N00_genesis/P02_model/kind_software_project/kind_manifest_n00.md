---
id: n00_software_project_manifest
kind: knowledge_card
pillar: P02
nucleus: n00
title: "Software Project -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, software_project, p02, n00, archetype, template]
density_score: 1.0
related:
  - p01_kc_software_project
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - bld_schema_quickstart_guide
  - bld_schema_search_strategy
  - bld_schema_benchmark_suite
  - bld_schema_voice_pipeline
  - bld_schema_action_paradigm
---

<!-- 8F: F1=knowledge_card P02 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Software Project defines a complete software project specification: goals, architecture overview, technology stack, team structure, milestones, and quality gates. It serves as the BECOME artifact for N03 when building complete software systems. One software_project artifact gives N03 full context to scaffold, build, and deliver a production-ready codebase.

## Pillar
P02 -- Model

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `software_project` |
| pillar | string | yes | Always `P02` |
| title | string | yes | Project name and version |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| language | list | yes | Primary programming languages |
| framework | list | no | Key frameworks used |
| architecture | enum | yes | monolith\|microservices\|serverless\|agent-native |
| deployment_target | enum | yes | cloud\|local\|hybrid\|edge |
| test_coverage_target | int | yes | Minimum test coverage % |
| milestones | list | yes | Named milestones with deliverables |

## When to use
- When specifying a new software system for N03 to build
- When documenting an existing codebase for agent consumption
- When defining quality and architecture constraints for a project

## Builder
`archetypes/builders/software_project-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind software_project --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N03)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact (Inventive Pride)
- `{{TARGET_AUDIENCE}}` -- N03 builder and engineering stakeholders
- `{{DOMAIN_CONTEXT}}` -- project domain and technical constraints

## Example (minimal)
```yaml
---
id: software_project_cex_sdk_v3
kind: software_project
pillar: P02
nucleus: n03
title: "CEX SDK v3"
version: 1.0
quality: null
---
language: [python]
framework: [pydantic, typer, httpx]
architecture: agent-native
deployment_target: local
test_coverage_target: 80
milestones:
  - name: "Core 8F Motor"
    deliverables: [cex_8f_motor.py, cex_8f_runner.py]
```

## Related kinds
- `repo_map` (P01) -- codebase context extraction for this project
- `changelog` (P01) -- version history of this project
- `model_architecture` (P02) -- AI components in this project

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_software_project]] | sibling | 0.43 |
| [[bld_schema_reranker_config]] | downstream | 0.43 |
| [[bld_schema_integration_guide]] | downstream | 0.42 |
| [[bld_schema_usage_report]] | downstream | 0.40 |
| [[bld_schema_dataset_card]] | downstream | 0.40 |
| [[bld_schema_quickstart_guide]] | downstream | 0.40 |
| [[bld_schema_search_strategy]] | downstream | 0.39 |
| [[bld_schema_benchmark_suite]] | downstream | 0.39 |
| [[bld_schema_voice_pipeline]] | downstream | 0.39 |
| [[bld_schema_action_paradigm]] | downstream | 0.38 |
