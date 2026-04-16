---
kind: examples
id: bld_examples_rbac_policy
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of rbac_policy artifacts
quality: 8.9
title: "Examples Rbac Policy"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [rbac_policy, builder, examples]
tldr: "Golden and anti-examples of rbac_policy artifacts"
domain: "rbac_policy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```yaml
kind: rbac_policy
name: multi_tenant_rbac
spec:
  tenants:
    - name: "acme_corp"
      roles:
        - name: "database_admin"
          permissions:
            - "read:acme_corp/databases/*"
            - "write:acme_corp/databases/*"
        - name: "developer"
          permissions:
            - "read:acme_corp/databases/*"
    - name: "initech_inc"
      roles:
        - name: "data_viewer"
          permissions:
            - "read:initech_inc/datasets/*"
```

## Anti-Example 1: Global Permissions
```yaml
kind: rbac_policy
name: bad_global_rbac
spec:
  tenants:
    - name: "all_tenants"
      roles:
        - name: "super_admin"
          permissions:
            - "read:*/*"
            - "write:*/*"
```
## Why it fails
Lacks tenant isolation by using a wildcard (`*/*`) permission scope, allowing a single role to access resources across all tenants. Violates multi-tenant security principles by eliminating boundary enforcement.

## Anti-Example 2: Role Overlap
```yaml
kind: rbac_policy
name: overlapping_roles
spec:
  tenants:
    - name: "cloudnine"
      roles:
        - name: "analyst"
          permissions:
            - "read:cloudnine/reports/*"
            - "write:cloudnine/reports/*"
        - name: "manager"
          permissions:
            - "read:cloudnine/reports/*"
            - "write:cloudnine/reports/*"
```
## Why it fails
Duplicates permissions between roles (`analyst` and `manager`) without differentiation. Creates ambiguity in access control and increases risk of accidental over-privilege due to redundant role definitions.
