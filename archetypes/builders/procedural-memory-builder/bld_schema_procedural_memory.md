---
kind: schema
id: bld_schema_procedural_memory
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for procedural_memory
quality: null
title: "Schema Procedural Memory"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [procedural_memory, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for procedural_memory"
domain: "procedural_memory construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field     | Type   | Required | Default | Notes                          |  
|-----------|--------|----------|---------|--------------------------------|  
| id        | string | yes      | null    | Unique identifier              |  
| kind      | string | yes      | null    | Must be "procedural_memory"    |  
| pillar    | string | yes      | null    | Must be "P10"                  |  
| title     | string | yes      | null    | Descriptive title              |  
| version   | string | yes      | "1.0"   | Schema version                 |  
| created   | date   | yes      | null    | ISO 8601 format                |  
| updated   | date   | yes      | null    | ISO 8601 format                |  
| author    | string | yes      | null    | Creator name                   |  
| domain    | string | yes      | null    | Application domain             |  
| quality   | null   | yes      | null    | Never self-score; peer review assigns |  
| tags      | list   | yes      | []      | Keywords                       |  
| tldr      | string | yes      | null    | Summary (max 256 chars)        |  
| steps     | list   | yes      | []      | Ordered procedural steps       |  
| conditions| list   | yes      | []      | Preconditions/trigger events   |  

### Recommended  
| Field       | Type   | Notes                  |  
|-------------|--------|------------------------|  
| outcome     | string | Expected result        |  
| validation  | string | Verification method    |  
| examples    | list   | Use-case illustrations |  
| dependencies| list   | Required prerequisites |  

## ID Pattern  
^p10_pm_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Introduction**  
   - Purpose and scope of the procedural memory.  
2. **Steps**  
   - Detailed, ordered sequence of actions.  
3. **Conditions**  
   - Triggers, inputs, or environmental requirements.  
4. **Outcome**  
   - Measurable result or state change.  
5. **Validation**  
   - Criteria for confirming correctness.  
6. **Examples**  
   - Real-world or hypothetical use cases.  

## Constraints  
- Steps must be ordered and unambiguous.  
- Conditions must be testable and specific.  
- Outcome must align with domain goals.  
- Validation must reference measurable metrics.  
- File size must not exceed 4096 bytes.  
- Tags must use lowercase alphanumeric and underscores.
