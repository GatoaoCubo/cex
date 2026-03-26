---
pillar: P06
llm_function: CONSTRAIN
purpose: Source of truth — field definitions and constraints for few_shot_example
---

# Schema: few_shot_example

SOURCE OF TRUTH. OUTPUT_TEMPLATE derives from here. CONFIG restricts from here.

## Required Fields (7)

| Field | Type | Rule |
|-------|------|------|
| id | string | Pattern: `^p01_fse_[a-z][a-z0-9_]+$` — must equal filename stem |
| kind | string | Literal: "few_shot_example" |
| input | string | Non-empty — the task/prompt being demonstrated |
| output | string | Non-empty — the ideal response showing format |
| quality | null | Always null — never self-score |
| tags | list[string] | >= 3 items, includes "few-shot" |
| tldr | string | <= 160 chars, non-empty |

## Recommended Fields

| Field | Type | Enum/Rule |
|-------|------|-----------|
| pillar | string | P01 |
| version | string | semver "1.0.0" |
| created | string | ISO date |
| updated | string | ISO date |
| author | string | who produced |
| domain | string | artifact kind being exemplified |
| difficulty | string | easy \| medium \| hard |
| edge_case | boolean | true if tests boundary condition |
| format | string | what format this exemplifies |
| explanation | string | why this pair teaches the format |
| keywords | list[string] | >= 3 search terms |

## ID Pattern
```
^p01_fse_[a-z][a-z0-9_]+$
```
Examples: `p01_fse_kc_frontmatter`, `p01_fse_validator_conditions`, `p01_fse_rag_source_yaml`

## Body Structure (3 required sections)
1. `## Explanation` — why this pair teaches the format
2. `## Variations` — 2-3 alternative inputs
3. `## Edge Cases` — boundary inputs with expected outputs

## Constraints
- max_bytes: 1024 (body, not frontmatter)
- naming: p01_fse_{topic}.md + p01_fse_{topic}.yaml
- id MUST equal filename stem
- input AND output MUST both be non-empty strings
- NO scoring rubric (that is golden_test P07)
- quality MUST be null

## Boundary Rule
few_shot_example SHOWS format. golden_test (P07) EVALUATES quality with scoring rubric.
If your artifact has a rubric or scores, it is NOT a few_shot_example.
