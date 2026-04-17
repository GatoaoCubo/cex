---
id: n00_rbac_policy_manifest
kind: knowledge_card
pillar: P09
nucleus: n00
title: "RBAC Policy -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, rbac_policy, p09, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An rbac_policy (Role-Based Access Control policy) composes multiple permission rules into a named policy set for multi-tenant isolation. It binds roles (admin, editor, viewer, nucleus) to permission bundles and enables enterprise deployments to enforce strict data separation between customers, teams, and environments.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `rbac_policy` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable policy name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| tenant | string | yes | Tenant or deployment this policy governs |
| roles | list | yes | Named role definitions |
| roles[].name | string | yes | Role identifier (admin, editor, viewer) |
| roles[].permissions | list | yes | List of permission artifact IDs |
| roles[].inherits | list | no | Parent roles whose permissions are inherited |
| default_role | string | no | Role assigned to new users by default |
| deny_override | boolean | no | Whether deny rules always override allow (default true) |

## When to use
- Setting up multi-tenant CEX deployments where customers must not access each other's data
- Defining nucleus-level access control (only N05 may modify P09 artifacts)
- Establishing enterprise pilot access tiers before full production rollout

## Builder
`archetypes/builders/rbac_policy-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind rbac_policy --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: rbac_cex_enterprise
kind: rbac_policy
pillar: P09
nucleus: n05
title: "CEX Enterprise RBAC Policy"
version: 1.0
quality: null
---
tenant: enterprise_default
roles:
  - name: orchestrator
    permissions: [perm_n07_dispatch_only, perm_global_read]
  - name: builder
    permissions: [perm_artifact_write, perm_compile_execute]
  - name: viewer
    permissions: [perm_global_read]
default_role: viewer
deny_override: true
```

## Related kinds
- `permission` (P09) -- individual permission rules that compose into this policy
- `sso_config` (P09) -- SSO authentication that assigns roles to authenticated users
- `data_residency` (P09) -- RBAC policies must align with data residency requirements
