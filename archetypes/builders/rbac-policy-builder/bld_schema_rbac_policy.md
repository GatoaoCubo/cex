---
kind: schema
id: bld_schema_rbac_policy
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for rbac_policy
quality: 9.1
title: "Schema Rbac Policy"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [rbac_policy, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for rbac_policy"
domain: "rbac_policy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field     | Type   | Required | Default | Notes                              |  
|-----------|--------|----------|---------|------------------------------------|  
| id        | string | yes      |         | Must match ID Pattern              |  
| kind      | string | yes      |         | Always "rbac_policy"               |  
| pillar    | string | yes      |         | Always "P09"                       |  
| title     | string | yes      |         | Policy name                        |  
| version   | string | yes      | "1.0"   | Semantic versioning                |  
| created   | date   | yes      |         | ISO 8601                           |  
| updated   | date   | yes      |         | ISO 8601                           |  
| author    | string | yes      |         | Owner                              |  
| domain    | string | yes      |         | Policy scope (e.g., "finance")     |  
| quality   | null   | yes      | null    | Never self-score; peer review assigns |  
| tags      | list   | yes      | []      | Keywords (e.g., "access", "audit") |  
| tldr      | string | yes      |         | One-sentence policy summary        |  
| roles     | list   | yes      | []      | Defined roles (e.g., "admin")      |  
| resources | list   | yes      | []      | Protected resources (e.g., "db")   |  

### Recommended  
| Field         | Type   | Notes                          |  
|---------------|--------|--------------------------------|  
| description   | string | Detailed policy explanation    |  
| references    | list   | Linked documents or standards  |  
| examples      | list   | Use-case scenarios             |  

## ID Pattern  
^p09_rbac_[a-z][a-z0-9_]+.yaml$  

## Body Structure  
1. **Policy Overview**  
   - Purpose, scope, and stakeholders.  
2. **Roles and Permissions**  
   - Role definitions and associated actions.  
3. **Resource Scope**  
   - Resources protected by the policy.  
4. **Enforcement Rules**  
   - Conditions for access control.  
5. **Audit Trail**  
   - Logging and monitoring requirements.  

## Constraints  
- File size must not exceed 4096 bytes.  
- Role names must be unique within the domain.  
- Resources must follow hierarchical naming conventions.  
- Permissions must align with least-privilege principles.  
- All policies must include a valid `tldr` summary.  
- ID must conform to the specified regex pattern.
