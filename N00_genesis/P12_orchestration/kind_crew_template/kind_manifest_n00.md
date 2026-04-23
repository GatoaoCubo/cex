---
id: n00_crew_template_manifest
kind: knowledge_card
pillar: P12
nucleus: n00
title: "Crew Template -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, crew_template, p12, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_crew_template
  - bld_schema_reranker_config
  - bld_schema_nucleus_def
  - bld_schema_sandbox_spec
  - bld_schema_integration_guide
  - bld_schema_multimodal_prompt
  - bld_schema_rbac_policy
  - bld_schema_benchmark_suite
  - bld_schema_collaboration_pattern
  - bld_schema_playground_config
---

<!-- 8F: F1=knowledge_card P12 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A crew_template is a reusable CrewAI/AutoGen-style crew blueprint that defines the roles table, process topology, memory configuration, and handoff protocol for a multi-role team. It is instantiated with a team_charter for a specific mission, enabling N07 to assemble coherent multi-agent teams without rebuilding the coordination structure from scratch.

## Pillar
P12 -- orchestration

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `crew_template` |
| pillar | string | yes | Always `P12` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| process | enum | yes | sequential \| hierarchical \| consensus |
| roles | array | yes | Role definitions with role_name, nucleus, tools, and handoff_target |
| memory_config | object | no | Shared memory settings (short_term, long_term, entity) |
| verbose | boolean | yes | Whether to emit detailed role execution traces |
| max_rpm | integer | no | Maximum requests per minute across all roles |
| isolation | enum | no | none \| worktree (for heavy crews) |

## When to use
- When a mission requires N roles with explicit handoffs between them
- When a recurring multi-role workflow needs a reusable pattern
- When building a grid of crews where each cell uses the same template with different charters

## Builder
`archetypes/builders/crew_template-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind crew_template --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: ct_product_launch_v1
kind: crew_template
pillar: P12
nucleus: n02
title: "Example Crew Template"
version: 1.0
quality: null
---
# Crew Template: Product Launch
process: sequential
roles:
  - role_name: researcher, nucleus: n01, handoff_target: copywriter
  - role_name: copywriter, nucleus: n02, handoff_target: designer
  - role_name: qa_reviewer, nucleus: n05, handoff_target: null
verbose: true
```

## Related kinds
- `team_charter` (P12) -- mission contract that instantiates this template
- `role_assignment` (P02) -- role binding used by each entry in the roles table
- `collaboration_pattern` (P12) -- coordination topology this template implements

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_crew_template]] | upstream | 0.47 |
| [[bld_schema_reranker_config]] | upstream | 0.38 |
| [[bld_schema_nucleus_def]] | upstream | 0.37 |
| [[bld_schema_sandbox_spec]] | upstream | 0.37 |
| [[bld_schema_integration_guide]] | upstream | 0.36 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.36 |
| [[bld_schema_rbac_policy]] | upstream | 0.36 |
| [[bld_schema_benchmark_suite]] | upstream | 0.36 |
| [[bld_schema_collaboration_pattern]] | upstream | 0.36 |
| [[bld_schema_playground_config]] | upstream | 0.35 |
