---
kind: schema
id: bld_schema_prompt_technique
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for prompt_technique
quality: 9.1
title: "Schema Prompt Technique"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [prompt_technique, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for prompt_technique"
domain: "prompt_technique construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|---|---|---|---|---|
| id | string | yes | null | Must match ID Pattern |
| kind | string | yes | "prompt_technique" | Fixed value |
| pillar | string | yes | "P03" | Fixed value |
| title | string | yes | null | Human-readable name |
| version | string | yes | "1.0" | Semantic versioning |
| created | datetime | yes | null | ISO 8601 format |
| updated | datetime | yes | null | ISO 8601 format |
| author | string | yes | null | Creator's identifier |
| domain | string | yes | "prompt_engineering" | Technical domain |
| quality | null | yes | null | Peer-reviewed score |
| tags | list | yes | [] | Keywords for categorization |
| tldr | string | yes | null | Summary in 1 sentence |
| example_use_case | string | yes | null | Practical application |
| technique_type | string | yes | null | Classification (e.g., "chain-of-thought") |

### Recommended
| Field | Type | Notes |
|---|---|---|
| related_techniques | list | Cross-references |
| difficulty_level | string | "beginner"/"intermediate"/"advanced" |

## ID Pattern
^p03_pt_[a-z][a-z0-9_]+.md$

## Body Structure
1. **Overview**
   Brief description of the technique's purpose and scope.

2. **Application Context**
   Scenarios where the technique is most effective.

3. **Example Use Case**
   Concrete implementation example with input/output.

4. **Best Practices**
   Guidelines for optimal usage and common pitfalls.

5. **Technical Considerations**
   System requirements, dependencies, or performance notes.

## Constraints
- IDs must be unique and follow the ID Pattern.
- All datetime fields must use ISO 8601 format.
- Quality field must be assigned by peer review, not self-assessed.
- Total file size must not exceed 4096 bytes.
- ASCII characters only; no Unicode or special symbols.
- Versioning must follow semantic versioning (e.g., 1.0.0).
