---
kind: schema
id: bld_schema_code_of_conduct
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for code_of_conduct
quality: 9.1
title: "Schema Code of Conduct"
version: "1.0.0"
author: n04_knowledge
tags: [code_of_conduct, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for code_of_conduct"
domain: "code_of_conduct construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
---

## Frontmatter Fields

### Required
| Field          | Type   | Required | Default | Notes |
|----------------|--------|----------|---------|-------|
| id             | string | yes      |         | Must match naming pattern |
| kind           | string | yes      |         | Must be "code_of_conduct" |
| pillar         | string | yes      |         | Must be "P05" |
| title          | string | yes      |         | Human-readable CoC title |
| version        | string | yes      |         | SemVer string |
| created        | date   | yes      |         | ISO 8601 date |
| updated        | date   | yes      |         | ISO 8601 date |
| author         | string | yes      |         | Maintainer or team name |
| domain         | string | yes      |         | "community governance" |
| quality        | null   | yes      | null    | Never self-score; peer review assigns |
| tags           | array  | yes      |         | Min 3 tags |
| tldr           | string | yes      |         | One-line summary |
| contact_email  | string | yes      |         | Reporting channel email |
| enforcement_version | string | yes |        | CoC base version (e.g., "2.1") |

### Recommended
| Field         | Type   | Notes |
|---------------|--------|-------|
| scope         | string | "online_and_offline" or "online_only" |
| response_sla  | string | e.g., "48h" for acknowledgement |
| attribution   | string | Source URL for base CoC |

## ID Pattern
^p05_coc_[a-z][a-z0-9_]+.md$

## Body Structure
1. **Our Pledge** -- Commitment statement from members, contributors, and leaders.
2. **Our Standards** -- Positive behaviors encouraged; unacceptable behaviors listed.
3. **Enforcement Responsibilities** -- Who enforces and how.
4. **Scope** -- Which spaces this CoC covers (online + offline).
5. **Enforcement** -- How to report; enforcement ladder (Correction, Warning, Temp Ban, Perm Ban).
6. **Attribution** -- Reference to Contributor Covenant version.

## Constraints
- All required fields must be present and valid.
- `id` must match the regex pattern exactly.
- `enforcement_version` must reference a real CoC version (default: "2.1").
- `contact_email` must be a valid email address pattern.
- Body must contain all 6 required sections in order.
