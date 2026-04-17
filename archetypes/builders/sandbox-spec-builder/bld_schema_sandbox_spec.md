---
kind: schema
id: bld_schema_sandbox_spec
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for sandbox_spec
quality: 9.1
title: "Schema Sandbox Spec"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sandbox_spec, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for sandbox_spec"
domain: "sandbox_spec construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields
### Required
| Field      | Type   | Required | Default | Notes |
|------------|--------|----------|---------|-------|
| id         | string | yes      | null    | Must match ID Pattern |
| kind       | string | yes      | null    | Always "sandbox_spec" |
| pillar     | string | yes      | null    | Always "P09" |
| title      | string | yes      | null    | Human-readable name |
| version    | string | yes      | null    | Semver format (e.g., 1.0.0) |
| created    | date   | yes      | null    | ISO 8601 format |
| updated    | date   | yes      | null    | ISO 8601 format |
| author     | string | yes      | null    | Maintainer email |
| domain     | string | yes      | null    | "sandbox" |
| quality    | null   | yes      | null    | Never self-score; peer review assigns |
| tags       | list   | yes      | []      | Keywords for discovery |
| tldr       | string | yes      | null    | One-sentence summary |
| sandbox_type | string | yes | null | "dev" or "prod" |
| resource_limits | object | yes | {} | CPU/Memory/Storage constraints |

### Recommended
| Field          | Type   | Notes |
|----------------|--------|-------|
| sandbox_image  | string | Docker image reference |
| network_config | object | VPC/ACL definitions |

## ID Pattern
^p09_sb_[a-z][a-z0-9_]+.yaml$

## Body Structure
1. **Overview**
   Brief description of the sandbox's purpose and scope.

2. **Configuration**
   Detailed parameters for setup (e.g., environment variables, dependencies).

3. **Security**
   Access controls, isolation mechanisms, and compliance requirements.

4. **Resource Limits**
   Maximum CPU, memory, and storage allocations.

5. **Usage Examples**
   Sample commands or workflows for common tasks.

## Constraints
- ID must match exact regex pattern
- File size must not exceed 4096 bytes
- All required fields must be present and valid
- Version must follow semver (e.g., 1.2.3)
- sandbox_type must be "dev" or "prod"
