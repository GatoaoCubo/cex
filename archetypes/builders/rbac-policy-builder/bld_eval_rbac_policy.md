---
kind: quality_gate
id: p09_qg_rbac_policy
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for rbac_policy
quality: 9.0
title: "Quality Gate Rbac Policy"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [rbac_policy, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for rbac_policy"
domain: "rbac_policy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_rbac_policy
  - p10_mem_rbac_policy_builder
  - bld_knowledge_card_rbac_policy
  - kc_rbac_policy
  - bld_instruction_rbac_policy
  - p09_qg_marketplace_app_manifest
  - p03_sp_rbac_policy_builder
  - rbac-policy-builder
  - p11_qg_audit_log
  - p09_qg_sandbox_spec
---

## Quality Gate

## Definition
| metric         | threshold | operator | scope      |
|----------------|-----------|----------|------------|
| Policy Count   | ≥1        | ≥         | per tenant |

## HARD Gates
| ID  | Check                          | Fail Condition                                      |
|-----|--------------------------------|-----------------------------------------------------|
| H01 | YAML frontmatter valid         | Missing or invalid frontmatter                      |
| H02 | ID matches pattern             | ID does not match ^p09_rbac_[a-z][a-z0-9_]+.yaml$ |
| H03 | kind field matches 'rbac_policy' | kind ≠ 'rbac_policy'                               |
| H04 | role field present             | role missing                                        |
| H05 | resource field present         | resource missing                                  |
| H06 | action field present           | action missing                                    |
| H07 | tenant isolation enforced      | tenant field missing or wildcard used             |
| H08 | no wildcard permissions        | action contains '*' or resource contains '*'      |

## SOFT Scoring
| Dim       | Dimension             | Weight | Scoring Guide                                      |
|-----------|-----------------------|--------|----------------------------------------------------|
| D01       | Completeness          | 0.20   | All required fields present (role, resource, action)|
| D02       | Isolation             | 0.20   | Tenant-specific isolation enforced                 |
| D03       | Specificity           | 0.15   | No wildcard permissions                            |
| D04       | Syntax                | 0.15   | Valid YAML and field formatting                    |
| D05       | Clarity               | 0.10   | Descriptive role/resource/action names             |
| D06       | Coverage              | 0.10   | Policies cover all critical operations             |
| D07       | Consistency           | 0.10   | Uniform naming and structure across policies       |

## Actions
| Score   | Action       |
|---------|--------------|
| ≥9.5    | GOLDEN       |
| ≥8.0    | PUBLISH      |
| ≥7.0    | REVIEW       |
| <7.0    | REJECT       |

## Bypass
| conditions                          | approver   | audit trail         |
|-------------------------------------|------------|---------------------|
| Critical tenant isolation override  | CTO        | documented in JIRA  |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
