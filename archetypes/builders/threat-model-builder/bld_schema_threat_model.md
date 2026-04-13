---
kind: schema
id: bld_schema_threat_model
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for threat_model
quality: null
title: "Schema Threat Model"
version: "1.0.0"
author: wave1_builder_gen
tags: [threat_model, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for threat_model"
domain: "threat_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Frontmatter Fields  
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
1. **Overview**  
   - Purpose, scope, and context of the threat model.  
2. **Threat Agents**  
   - List of potential adversaries and their capabilities.  
3. **Vulnerabilities**  
   - Identified weaknesses and attack vectors.  
4. **Mitigations**  
   - Controls and countermeasures in place.  
5. **Impact Analysis**  
   - Potential consequences of successful attacks.  
6. **References**  
   - Links to related documents, tools, or standards.  

## Constraints  
- All required fields must be present and valid.  
- ID must conform to the regex pattern.  
- Version must follow semantic versioning (e.g., "1.0.0").  
- Threat_level must be an integer between 1-5.  
- TLDR must be ≤256 characters and in plain text.  
- Domain-specific fields must align with the defined schema.
