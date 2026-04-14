---
id: bld_schema_type_def
kind: schema
pillar: P06
llm_function: CONSTRAIN
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder
tags: [schema, type-def, P06, source-of-truth]
quality: 9.1
title: "Schema Type Def"
tldr: "Golden and anti-examples for type def construction, demonstrating ideal structure and common pitfalls."
domain: "type def construction"
density_score: 0.90
---

## Frontmatter Fields
### Required
| Field | Type | Pattern / Allowed Values | Notes |
|---|---|---|---|
| `id` | string | `^p06_td_[a-z][a-z0-9_]*$` | Derived from type_name in snake_case |
| `kind` | enum | `type_def` | Fixed — no other value valid |
| `pillar` | enum | `P06` | Fixed — spec layer pillar |
| `layer` | enum | `spec` | Fixed |
| `version` | string | `^\d+\.\d+\.\d+$` | SemVer |
| `created` | string | `YYYY-MM-DD` | ISO 8601 date |
| `updated` | string | `YYYY-MM-DD` | ISO 8601 date |
| `author` | string | any | Agent_group or agent ID |
| `type_name` | string | PascalCase | Canonical name of the type |
| `base_type` | enum | `string`, `integer`, `number`, `boolean`, `array`, `object`, `enum`, `union`, `intersection`, `tuple`, `record` | Root primitive or composite |
| `domain` | string | snake_case | Owning domain or module |
| `nullable` | boolean | `true` / `false` | Explicit null membership |
| `quality` | null | `null` | Set null on draft; governance assigns |
| `tags` | array[string] | any | Minimum 2 tags |
| `tldr` | string | single sentence | One-line description |
### Recommended
| Field | Type | Notes |
|---|---|---|
| `composition` | object | Required when `base_type` is `union`, `intersection`, or `tuple` |
| `inheritance` | object | Present when type extends another type_def |
| `generics` | array[object] | Present when type is parameterized |
| `serialization` | object | Wire format, encoding, field options |
| `examples` | array[object] | At least one concrete value with note |
| `keywords` | array[string] | Discovery terms beyond tags |
| `density_score` | number | 0.0–1.0; assigned post-production |
## Complex Objects
### `constraints` object
```yaml
constraints:
  min_length: integer          # for string base_type
  max_length: integer          # for string base_type
  pattern: string              # regex string
  format: string               # e.g. uuid, email, uri, date-time
  minimum: number              # for numeric base_type
  maximum: number              # for numeric base_type
  exclusive_minimum: number    # for numeric base_type
  exclusive_maximum: number    # for numeric base_type
  min_items: integer           # for array base_type
  max_items: integer           # for array base_type
  unique_items: boolean        # for array base_type
  allowed_values: array        # for enum base_type
  required_keys: array         # for object/record base_type
```
### `composition` object
```yaml
composition:
  mode: union | intersection | tuple | discriminated_union
  discriminant_field: string   # only for discriminated_union
  members:
    - type_ref: string         # id of member type_def OR inline base_type
      label: string            # optional human label
```
### `inheritance` object
```yaml
inheritance:
  extends: string              # id of parent type_def (p06_td_*)
  overrides: array[string]     # constraint keys overridden in this child
```
### `generics` array item
```yaml
- name: string                 # type parameter name e.g. T, K, V
  bound: string                # upper bound type_ref or "any"
  default: string              # optional default type_ref
```
## ID Pattern
```
p06_td_{type_slug}
  type_slug = type_name converted to snake_case, lowercase
  Examples:
    TypeName    -> p06_td_type_name
    UserId      -> p06_td_user_id
    HTTPStatus  -> p06_td_http_status
```
Regex: `^p06_td_[a-z][a-z0-9_]*$`
## Body Structure
Four sections in order:
1. **Definition** — prose description of what the type represents and its domain role
2. **Constraints** — structured constraint key-value pairs (mirrors `constraints` frontmatter object)
3. **Examples** — at least one concrete value with explanatory note
4. **Keywords** — comma-separated discovery terms
Optional sections (append after Keywords when applicable):
