---
id: type-def-builder-memory
kind: memory
pillar: P10
llm_function: INJECT
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
tags: [memory, type-def, P10, patterns, anti-patterns]
---

## Common Mistakes

1. **Wrong kind** — writing `kind: type_definition` or `kind: schema` instead of `kind: type_def`; hard gate H02 rejects these immediately
2. **Free-text constraints** — writing `constraints: "must be between 0 and 10"` instead of a structured object; constraint values must be keyed, typed entries
3. **Author assigns quality** — setting `quality: 8.5` on draft output; only governance assigns quality; always set `quality: null`
4. **Non-SemVer version** — writing `v1` or `1.0` instead of `1.0.0`; pattern `^\d+\.\d+\.\d+$` required
5. **Missing nullable** — omitting `nullable` field entirely; it must be explicitly `true` or `false`, never absent
6. **Conflating with input_schema** — producing a type_def that contains operation-specific fields (`endpoint`, `method`, `required_params`); those belong in `input_schema`
7. **base_type outside vocabulary** — using `decimal`, `float`, `str`, `int`, `list`, `dict`; only controlled vocabulary values are valid (see CONFIG.md Base Type Enum)
8. **id not derived from type_name** — inventing an arbitrary id instead of converting `type_name` PascalCase to snake_case with `p06_td_` prefix

## Domain Patterns

| Pattern | When to Use | Example |
|---|---|---|
| Newtype | Wrap primitive with semantic identity | `p06_td_user_id` — base `string`, format `uuid` |
| Bounded numeric | Constrain number to domain range | `p06_td_score` — base `number`, min 0.0, max 10.0 |
| Discriminated union | Tagged sum type with kind field | `p06_td_artifact_ref` — mode `discriminated_union`, discriminant `kind` |
| Enum vocabulary | Fixed allowed values | `p06_td_log_level` — base `enum`, allowed_values [DEBUG, INFO, WARN, ERROR] |
| Nullable optional | Type that can be absent | `p06_td_optional_tag` — nullable `true`, nil_semantics documented |
| Generic container | Parameterized type | `p06_td_result` — generics T (success), E (error) |
| Recursive type | Self-referencing structure | `p06_td_tree_node` — composition references itself |
| Inherited type | Extends base type_def | `p06_td_admin_user` — inheritance.extends `p06_td_user` |

## Production Counter

| Metric | Value |
|---|---|
| Total type_defs produced | 0 |
| Golden promotions | 0 |
| Most common base_type | — |
| Most common domain | — |
| Average density_score | — |

*Counter updated by governance pipeline post-production.*
