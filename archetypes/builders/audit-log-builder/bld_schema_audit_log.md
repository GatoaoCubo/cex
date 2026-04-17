---
kind: schema
id: bld_schema_audit_log
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for audit_log
quality: 9.1
title: "Schema Audit Log"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [audit_log, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for audit_log"
domain: "audit_log construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field     | Type   | Required | Default | Notes                              |  
|-----------|--------|----------|---------|------------------------------------|  
| id        | string | yes      | null    | Unique identifier                  |  
| kind      | string | yes      | null    | Must be `audit_log`                |  
| pillar    | string | yes      | null    | Must be `P11`                      |  
| title     | string | yes      | null    | Descriptive title                  |  
| version   | string | yes      | null    | Semantic version (e.g., 1.0.0)     |  
| created   | string | yes      | null    | ISO 8601 timestamp                 |  
| updated   | string | yes      | null    | ISO 8601 timestamp                 |  
| author    | string | yes      | null    | Responsible party                  |  
| domain    | string | yes      | null    | Audit domain (e.g., compliance)    |  
| quality   | null   | yes      | null    | Never self-score; peer review assigns |  
| tags      | list   | yes      | null    | Keywords for categorization        |  
| tldr      | string | yes      | null    | Summary of audit findings        |  
| event_type | string | yes | null | Type of audit event (e.g., login, transaction) |  
| log_level | string | yes | null | Severity (e.g., info, warning, error) |  

### Recommended  
| Field         | Type   | Notes                          |  
|---------------|--------|--------------------------------|  
| reference_id  | string | Link to related audit trail    |  
| impacted_user | string | User affected by the event     |  

## ID Pattern  
^p11_al_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Audit Trail**  
   - Sequence of events with timestamps and actors.  
2. **Event Details**  
   - Description, category, and outcome of the event.  
3. **Metadata**  
   - System context (e.g., IP address, module name).  
4. **Compliance Info**  
   - Regulatory references and policy violations.  

## Constraints  
- Max file size: 3072 bytes.  
- ID must match `^p11_al_[a-z][a-z0-9_]+.md$`.  
- `event_type` and `log_level` must be predefined enums.  
- `created` and `updated` must be valid ISO 8601 timestamps.  
- `version` must follow semantic versioning (e.g., 1.2.3).
