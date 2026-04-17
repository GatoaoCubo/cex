---
id: bld_schema_value_object
kind: schema
pillar: P06
title: "Value Object Builder -- Schema"
version: 1.0.0
quality: 6.6
tags: [builder, value_object, schema]
llm_function: CONSTRAIN
density_score: 1.0
updated: "2026-04-17"
---
# Schema: value_object
## Frontmatter Fields
### Required
| Field | Type | Notes |
|-------|------|-------|
| id | string `p06_vo_{slug}` | namespace + slug |
| kind | literal `value_object` | type integrity |
| pillar | literal `P06` | pillar assignment |
| title | string | human label |
| version | semver | versioning |
| attributes | list[{name, type, constraint}] | at least 1 attribute |
| equality | literal `structural` | always structural for value objects |
| quality | null | never self-score |
| tags | list[string] >= 3 | searchability |
| tldr | string <= 160ch | dense summary |
### Recommended
| Field | Type | Notes |
|-------|------|-------|
| used_in | list[string] | aggregate_root or entity that uses this |
| transformations | list[string] | operations returning new instances |
| language_examples | list[string] | code snippets in target language |
| hashable | bool | whether usable as dict key / set member |
## ID Pattern
Regex: `^p06_vo_[a-z][a-z0-9_]+$`
## Body Structure
1. `## Attributes` -- field table: name, type, constraint, valid range
2. `## Equality` -- structural equality contract definition
3. `## Validation` -- what makes an instance valid (and invalid examples)
4. `## Transformations` -- methods that return new instances, never mutate
5. `## Usage` -- which aggregates or entities use this value object
## Constraints
- max_bytes: 2048
- naming: p06_vo_{slug}.md
- NO identity fields (id, uuid, pk)
- NO mutation methods
- equality MUST be structural
- quality: null always
