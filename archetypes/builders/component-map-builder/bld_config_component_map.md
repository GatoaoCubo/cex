---
pillar: P00
id: bld_config_component_map
kind: config
parent: component-map-builder
version: 1.0.0
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Component Map"
author: n03_builder
tags: [component_map, builder, examples]
tldr: "Golden and anti-examples for component map construction, demonstrating ideal structure and common pitfalls."
domain: "component map construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: CONSTRAIN
---
# Config — component-map-builder
## Naming Conventions
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p08_cmap_{scope_slug}.yaml` | `p08_cmap_brain_infrastructure.yaml` |
| Builder directory | kebab-case | `component-map-builder/` |
| Frontmatter fields | snake_case | `component_count`, `connection_count` |
| Scope slug | lowercase + underscores | `brain_infrastructure` |
| Component names | Title Case | `BM25 Index`, `brain_query API` |
NOTE: machine_format is yaml (not md). Output extension is `.yaml`, not `.md`.
## File Paths
| Purpose | Path |
|---------|------|
| Output artifacts | `cex/P08_architecture/examples/p08_cmap_{scope_slug}.yaml` |
| Schema reference | `cex/P08_architecture/_schema.yaml` |
| Builder files | `cex/archetypes/builders/component-map-builder/` |
| Seed bank | `cex/archetypes/SEED_BANK.yaml` |
## Size Limits
| Limit | Value |
|-------|-------|
| Body max bytes | 3072 |
| Total artifact | ~4200 bytes |
| Density minimum | 0.80 |
| tldr max chars | 160 |
| tags minimum | 3 |
| keywords minimum | 2 |
## Component-Map-Specific Constraints
| Constraint | Rule |
|-----------|------|
| Format | YAML frontmatter + markdown body sections |
| Extension | `.yaml` (despite having markdown body) |
| component_count | Must match actual rows in Components table |
| connection_count | Must match actual rows in Connections table |
| Component fields | Every row: name, role, owner, status |
| Connection fields | Every row: from, to, type, direction |
| Orphan components | FORBIDDEN — every component >= 1 connection |
| Scope field | Must state what is included AND excluded |
| quality field | ALWAYS null — never a number |
## Scope Slug Rules
- All lowercase
- Words separated by underscores
- No hyphens, no spaces, no special characters
- Descriptive but concise (2-4 words)
Valid: `brain_infrastructure`, `agent_group_network`, `api_layer`, `hook_system`
Invalid: `Brain-Infrastructure`, `brain infrastructure`, `b`, `the_entire_cex_system_components`
## Seeds Reference (from SEED_BANK.yaml P08_component_map)
Primary seeds: scope, components, connections, dependencies, data_flow, ownership, health, versioning, interfaces, boundaries
Contexts: architecture_review, debugging, planning, onboarding
