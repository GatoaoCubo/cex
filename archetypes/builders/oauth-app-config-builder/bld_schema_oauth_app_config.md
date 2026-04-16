---
kind: schema
id: bld_schema_oauth_app_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for oauth_app_config
quality: 9.1
title: "Schema Oauth App Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [oauth_app_config, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for oauth_app_config"
domain: "oauth_app_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|------|------|----------|---------|-------|
| id | string | yes | null | Must match ID Pattern |
| kind | string | yes | null | Always "oauth_app_config" |
| pillar | string | yes | null | Always "P09" |
| title | string | yes | null | Human-readable name |
| version | string | yes | "1.0" | Semantic versioning |
| created | datetime | yes | null | ISO 8601 format |
| updated | datetime | yes | null | ISO 8601 format |
| author | string | yes | null | Responsible party |
| domain | string | yes | null | OAuth provider domain |
| quality | null | yes | null | Never self-score; peer review assigns |
| tags | list | yes | [] | Categorization |
| tldr | string | yes | null | Summary of purpose |
| client_id | string | yes | null | OAuth client identifier |
| client_secret | string | yes | null | Confidential secret |

### Recommended
| Field | Type | Notes |
|------|------|-------|
| description | string | Detailed purpose |
| expiration | datetime | Token lifespan |
| environment | string | Deployment context |

## ID Pattern
^p09_oauth_[a-z][a-z0-9_]+.yaml$

## Body Structure
1. **Configuration Overview**
   Define app metadata, redirect URIs, and scope requirements.

2. **Security Parameters**
   Specify encryption standards, secret storage, and access controls.

3. **Authorization Flow**
   Document grant types, token endpoints, and refresh mechanisms.

4. **Metadata Schema**
   Include JSON structure for dynamic client registration.

## Constraints
- All required fields must be present and valid
- ID must match exact regex pattern
- client_id must be unique per domain
- client_secret must be encrypted at rest
- scopes must conform to OAuth 2.0 specifications
- version must follow semantic versioning (e.g., 1.0.0)
