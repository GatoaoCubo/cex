---
id: n00_permission_manifest
kind: knowledge_card
8f: F3_inject
pillar: P09
nucleus: n00
title: "Permission -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, permission, p09, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_permission
  - bld_schema_rbac_policy
  - permission-builder
  - p09_perm_{{SCOPE_SLUG}}
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - bld_schema_sandbox_config
  - bld_schema_sandbox_spec
  - bld_schema_dataset_card
  - bld_schema_quickstart_guide
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A permission defines a read/write/execute access rule for a resource within CEX: which nucleus or agent may access a pillar, tool, file path, or external API. Permissions are the building blocks of rbac_policy and are checked at F1 CONSTRAIN to prevent unauthorized operations before a build begins.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `permission` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable permission name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| resource | string | yes | What is being protected (path, tool, api, pillar) |
| actions | list | yes | Allowed actions: read, write, execute, delete, create |
| subjects | list | yes | Who may perform these actions (nucleus ids, roles) |
| conditions | list | no | Additional conditions (e.g. must_have_manifest, dry_run_only) |
| effect | enum | yes | allow \| deny |
| priority | integer | no | Higher priority wins on conflict (default 0) |

## When to use
- Restricting which nuclei may write to sensitive pillars (e.g. only N05 writes P09)
- Granting a sub-agent read-only access to a knowledge card library
- Defining allow/deny rules that compose into an rbac_policy

## Builder
`archetypes/builders/permission-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind permission --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: perm_n07_dispatch_only
kind: permission
pillar: P09
nucleus: n05
title: "N07 dispatch.sh execute permission"
version: 1.0
quality: null
---
resource: _spawn/dispatch.sh
actions: [execute]
subjects: [n07]
effect: allow
conditions: [must_have_handoff_file]
```

## Related kinds
- `rbac_policy` (P09) -- composes multiple permissions into role-based access policies
- `invariant` (P08) -- permissions that are non-negotiable become invariants
- `guardrail` (P11) -- runtime enforcement of permission rules during agent execution

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_permission]] | upstream | 0.55 |
| [[bld_schema_rbac_policy]] | upstream | 0.44 |
| [[permission-builder]] | related | 0.44 |
| [[p09_perm_{{SCOPE_SLUG}}]] | related | 0.40 |
| [[bld_schema_reranker_config]] | upstream | 0.40 |
| [[bld_schema_integration_guide]] | upstream | 0.40 |
| [[bld_schema_sandbox_config]] | upstream | 0.40 |
| [[bld_schema_sandbox_spec]] | upstream | 0.39 |
| [[bld_schema_dataset_card]] | upstream | 0.39 |
| [[bld_schema_quickstart_guide]] | upstream | 0.39 |
