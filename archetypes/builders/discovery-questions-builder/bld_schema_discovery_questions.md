---
kind: schema
id: bld_schema_discovery_questions
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for discovery_questions
quality: 9.1
title: "Schema Discovery Questions"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [discovery_questions, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for discovery_questions"
domain: "discovery_questions construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|---|---|---|---|---|
| id | string | yes | null | Must match ID Pattern |
| kind | string | yes | "discovery_questions" | Fixed value |
| pillar | string | yes | "P01" | Fixed value |
| title | string | yes | null | Concise question summary |
| version | string | yes | "1.0" | Schema version |
| created | datetime | yes | null | ISO 8601 format |
| updated | datetime | yes | null | ISO 8601 format |
| author | string | yes | null | Author name |
| domain | string | yes | null | Domain of question (e.g., "security") |
| quality | null | yes | null | Peer-reviewed score |
| tags | list | yes | [] | Keywords for categorization |
| tldr | string | yes | null | One-sentence summary |
| question_type | string | yes | null | E.g., "open-ended", "yes/no" |
| target_audience | string | yes | null | E.g., "executives", "developers" |

### Recommended
| Field | Type | Notes |
|---|---|---|
| related_questions | list | Links to related discovery questions |
| sensitivity_level | string | E.g., "low", "high" |

## ID Pattern
^p01_dq_[a-z][a-z0-9_]+.md$

## Body Structure
1. **Purpose**
   Define the objective of the discovery question.

2. **Scope**
   Clarify boundaries and limitations of the question.

3. **Question Formulation**
   Provide the exact wording and context.

4. **Target Audience**
   Specify who should answer the question.

5. **Expected Outcomes**
   Describe anticipated insights or data.

6. **Review Process**
   Detail peer-review steps for quality validation.

## Constraints
- ID must match ^p01_dq_[a-z][a-z0-9_]+.md$ exactly.
- Quality field must be assigned by peer review, not self-scored.
- Domain-specific fields (question_type, target_audience) are mandatory.
- All datetime fields must use ISO 8601 format.
- Total file size must not exceed 4096 bytes.
- Tags must be lowercase, alphanumeric, and underscore-separated.
