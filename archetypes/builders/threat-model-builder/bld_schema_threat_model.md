---
kind: schema
id: bld_schema_threat_model
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for threat_model
quality: 9.2
title: "Schema Threat Model"
version: "1.1.0"
author: n05_ops
tags: [threat_model, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for threat_model"
domain: "threat_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Frontmatter Fields  

This ISO records a threat model: the assets worth protecting and the attacker profiles that target them.
### Required  
| Field      | Type   | Required | Default | Notes                          |  
|------------|--------|----------|---------|--------------------------------|  
| id         | string | yes      | -       | Unique identifier              |  
| kind       | string | yes      | "threat_model" | CEX kind                 |  
| pillar     | string | yes      | "P11"    | Pillar                         |  
| title      | string | yes      | -       | Threat model name              |  
| version    | string | yes      | "1.0"   | Schema version                 |  
| created    | date   | yes      | -       | Creation date                  |  
| updated    | date   | yes      | -       | Last update date               |  
| author     | string | yes      | -       | Author                         |  
| domain     | string | yes      | -       | Domain of application          |  
| quality    | string | yes      | "draft" | Quality status                 |  
| tags       | list   | yes      | []      | Keywords                       |  
| tldr       | string | yes      | -       | Summary (≤256 chars)           |  
| threat_level | int  | yes      | 0       | 1-5 severity                   |  
| mitigation_status | string | yes | "unaddressed" | Status of mitigations |  

### Recommended  
| Field              | Type   | Notes                          |  
|--------------------|--------|--------------------------------|  
| description        | string | Detailed threat model summary  |  
| reference          | string | External documentation link    |  
| status             | string | "active", "deprecated", etc.   |  

## ID Pattern  
^p11_tm_[a-zA-Z0-9_-]+\.md$  

## Body Structure  
1. **Scope and System Description** -- boundaries, stakeholders, out-of-scope items  
2. **Asset Inventory** -- assets with sensitivity classification and owner  
3. **Threat Actors** -- actor table with motivation, capability, access level  
4. **STRIDE Threat Analysis** -- one subsection per STRIDE category (S/T/R/I/D/E), each with threat table and mitigations  
5. **Risk Priority Matrix** -- all threats ranked by risk score (likelihood x impact)  
6. **Mitigation Strategies** -- controls mapped to threats with NIST CSF/ISO 27001 references  
7. **AI-Specific Threat Addendum** -- MITRE ATLAS threats if ML pipeline in scope  
8. **Assumptions and Limitations** -- what was assumed or excluded  
9. **Open Issues** -- unresolved risks with owner and due date  
10. **References** -- STRIDE, MITRE ATT&CK, MITRE ATLAS, NIST AI RMF, ISO/IEC 23894  

## Constraints  
- All required fields must be present and valid.  
- ID must conform to the regex pattern.  
- Version must follow semantic versioning (e.g., "1.0.0").  
- Threat_level must be an integer between 1-5.  
- TLDR must be ≤256 characters and in plain text.  
- Domain-specific fields must align with the defined schema.
