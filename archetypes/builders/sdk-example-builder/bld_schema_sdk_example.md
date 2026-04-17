---
kind: schema
id: bld_schema_sdk_example
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for sdk_example
quality: 9.1
title: "Schema Sdk Example"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sdk_example, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for sdk_example"
domain: "sdk_example construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields (sdk example schema)
### Required fields for an sdk example  
| Field     | Type   | Required | Default | Notes                              |  
|-----------|--------|----------|---------|------------------------------------|  
| id        | string | yes      | null    | Must match ID Pattern              |  
| kind      | string | yes      | null    | Always "sdk_example"               |  
| pillar    | string | yes      | null    | Always "P04"                       |  
| title     | string | yes      | null    | Descriptive SDK name               |  
| version   | string | yes      | null    | Semantic versioning (e.g., 1.0.0)  |  
| created   | date   | yes      | null    | ISO 8601 format                    |  
| updated   | date   | yes      | null    | ISO 8601 format                    |  
| author    | string | yes      | null    | Maintainer name                    |  
| domain    | string | yes      | null    | SDK target domain (e.g., "payments") |  
| quality   | null   | yes      | null    | Never self-score; peer review assigns |  
| tags      | array  | yes      | null    | Keywords for discovery             |  
| tldr      | string | yes      | null    | One-sentence SDK purpose           |  
| language  | string | yes      | null    | Primary programming language       |  
| dependencies | array | yes | null | Required libraries/dependencies  |  

### Recommended  
| Field              | Type   | Notes                          |  
|--------------------|--------|--------------------------------|  
| example_usage      | string | Code snippet demonstrating SDK |  
| license            | string | Open-source license type       |  

## ID Pattern  
^p04_sdk_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Overview**  
   - Purpose, target audience, and use cases.  
2. **Key Features**  
   - Core functionalities and differentiators.  
3. **Installation**  
   - Step-by-step setup instructions.  
4. **Usage Examples**  
   - Code samples for common tasks.  
5. **Dependencies**  
   - External libraries and system requirements.  
6. **Compatibility**  
   - Supported platforms, languages, and versions.  

## Constraints  
- ID must strictly follow ^p04_sdk_[a-z][a-z0-9_]+.md$  
- All required fields must be present and valid  
- Version must adhere to semantic versioning (e.g., 1.2.3)  
- Language must be a valid programming language name  
- Dependencies must list exact package names and versions  
- TLDR must be ≤ 200 characters and actionable
