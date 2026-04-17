---
kind: schema
id: bld_schema_course_module
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for course_module
quality: 9.2
title: "Schema Course Module"
version: "1.0.0"
author: n03_builder
tags: [course_module, builder, schema]
tldr: "Canonical course module schema aligned with Bloom's taxonomy, Kirkpatrick evaluation, SCORM 2004, xAPI, and WCAG 2.2 AA."
domain: "course_module construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.88
---

## Frontmatter Fields

### Required
| Field | Type | Required | Default | Notes |
|---|---|---|---|---|
| id | string | yes | null | Must match ID Pattern |
| kind | string | yes | "course_module" | Fixed value |
| pillar | string | yes | "P05" | Fixed value |
| title | string | yes | null | Human-readable module name |
| version | string | yes | "1.0.0" | Semantic versioning |
| created | date | yes | null | ISO 8601 |
| updated | date | yes | null | ISO 8601 |
| author | string | yes | null | Instructional designer |
| domain | string | yes | null | Subject area (e.g., "python", "statistics", "product_management") |
| quality | null | yes | null | Never self-score; peer review assigns |
| tags | list | yes | [] | Keywords for search |
| tldr | string | yes | null | Summary <= 250 chars |
| learning_outcomes | list | yes | [] | Bloom-verb-prefixed statements `{verb, bloom_level, statement}` |
| bloom_levels | list | yes | [] | Subset of [Remember, Understand, Apply, Analyze, Evaluate, Create] |
| prerequisites | list | yes | [] | Referenced course_module IDs, not free text |
| assessment_items | list | yes | [] | `{id, type, bloom_level, outcome_ref}` items |
| duration_minutes | integer | yes | null | Estimated time; 5-60 recommended for micro-learning |

### Recommended
| Field | Type | Notes |
|---|---|---|
| difficulty | string | "beginner" \| "intermediate" \| "advanced" |
| content_format | list | Subset of [text, video, interactive, simulation, reading, code] |
| kirkpatrick_level | integer | 1=Reaction, 2=Learning, 3=Behavior, 4=Results; declare measured level |
| scorm_version | string | "1.2" \| "2004_3ed" \| "2004_4ed" \| "none" |
| xapi_enabled | bool | True when xAPI (Tin Can) statements emitted |
| wcag_level | string | "A" \| "AA" \| "AAA" -- AA is minimum |
| cohort_mode | string | "self_paced" \| "cohort_based" \| "blended" |
| instructor_led | bool | Requires live facilitator? |

## ID Pattern
`^p05_cm_[a-z][a-z0-9_]+\.md$`

## Body Structure
1. **Overview** -- purpose, target learner, context.
2. **Learning Outcomes** -- Bloom-verb statements mapped to bloom_levels.
3. **Prerequisites** -- module IDs learner must complete first.
4. **Content Sequence** -- lessons (5-10 min chunks) with formative checks.
5. **Assessments** -- formative + summative items, each mapped to an outcome.
6. **Accessibility** -- WCAG 2.2 AA compliance notes, captions, alt-text.
7. **Evaluation** -- Kirkpatrick measurement plan (L1-L4).

## Constraints
- File size <= 8192 bytes.
- Every `assessment_items[i].outcome_ref` MUST match a `learning_outcomes[j].id` (1:1+ coverage).
- Every assessment item's `bloom_level` MUST equal its referenced outcome's `bloom_level` (no drift).
- Learning outcome verbs MUST be Bloom taxonomy verbs (reject "know", "understand", "learn" without qualifier).
- Prerequisites MUST reference existing course_module IDs (schema-validated against registry).
- `duration_minutes` MUST be > 0; warn if > 45 (micro-learning threshold).
- Quality field MUST be null (peer review assigns).
