---
kind: schema
id: bld_schema_agent_computer_interface
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for agent_computer_interface
quality: 9.0
title: "Schema Agent Computer Interface"
version: "1.0.0"
author: n01_review
tags: [agent_computer_interface, builder, schema]
tldr: "Formal schema for agent_computer_interface: required frontmatter, body sections, size limits, and naming."
domain: "agent_computer_interface construction"
created: "2026-04-13"
updated: "2026-04-14"
density_score: 0.88
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
| :--- | :--- | :--- | :--- | :--- |
| id | string | Y | "" | Pattern: p08_aci_[a-z][a-z0-9_]+ |
| kind | string | Y | "agent_computer_interface" | Always agent_computer_interface |
| pillar | string | Y | "P08" | Always P08 |
| title | string | Y | "" | Human-readable interface name |
| version | string | Y | "1.0.0" | SemVer |
| created | datetime | Y | now() | ISO 8601 |
| updated | datetime | Y | now() | ISO 8601 |
| author | string | Y | "system" | Creator name or nucleus |
| domain | string | Y | "" | terminal / browser / gui / api / file_system / code_execution |
| protocol | string | Y | "" | json_rpc / cli / rest / grpc / mcp |
| quality | null | Y | null | Never self-score |
| tags | list | Y | [] | Include domain + protocol tags |
| tldr | string | Y | "" | One-sentence description <= 160 chars |

### Recommended
| Field | Type | Notes |
| :--- | :--- | :--- |
| transport | string | unix_socket / http / stdio / tcp |
| auth_method | string | none / token / mtls / api_key |
| rate_limit | integer | Max requests per minute |

## Body Sections
| Section | Required | Content |
| :--- | :--- | :--- |
| Overview | Y | Interface type, protocol, transport, auth, scope as table |
| Action Space | Y | Table: action, input schema, output schema, error states |
| Observation Schema | Y | Table: field, type, source, notes |
| Error Protocol | Y | Table: code, meaning, recovery |
| Security & Sandboxing | Y | Table: constraint, value, enforcement |

## Size Constraints
| Component | Limit |
| :--- | :--- |
| Body | 5120 bytes |
| Total with frontmatter | 7168 bytes |
| Min density | 0.85 |

## Naming Convention
| Component | Pattern | Example |
| :--- | :--- | :--- |
| Artifact ID | p08_aci_[domain] | p08_aci_bash_executor |
| File name | p08_aci_[domain].md | p08_aci_bash_executor.md |
| Directory | P08_architecture/aci/ | standard pillar location |
