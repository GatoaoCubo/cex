---
kind: knowledge_card
id: bld_knowledge_card_type_def
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for type_def production — atomic searchable facts
sources: type-def-builder MANIFEST.md + SCHEMA.md
quality: 9.1
title: "Knowledge Card Type Def"
version: "1.0.0"
author: n03_builder
tags: [type_def, builder, examples]
tldr: "Golden and anti-examples for type def construction, demonstrating ideal structure and common pitfalls."
domain: "type def construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_ins_type_def
  - bld_schema_type_def
  - p03_sp_type-def-builder
  - bld_architecture_type_def
  - bld_config_type_def
  - p11_qg_type_def
  - type-def-builder
  - bld_output_template_type_def
  - bld_memory_type_def
  - bld_examples_type_def
---

# Domain Knowledge: type_def
## Executive Summary
A `type_def` (P06, spec layer) is a reusable named type declaration — the vocabulary other artifacts reference by `p06_td_*` ID. It differs from `input_schema` (concrete input contract), `validator` (executable pass/fail rule), and `validation_schema` (post-generation system contract) by being purely declarative and reusable across domains. It captures base type, constraints, composition rules, nullable semantics, generics, and serialization in machine-parseable YAML.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P06 (spec layer) |
| Kind | `type_def` |
| ID pattern | `^p06_td_[a-z][a-z0-9_]*$` |
| Naming | `p06_td_{type_slug}.yaml` |
| Max body | 3072 bytes |
| Machine format | yaml |
| Required frontmatter fields | 15 |
| Recommended fields | 7 |
| `quality` field | always `null` (governance assigns) |
| LLM function | GOVERN |
## Patterns
| Pattern | Rule |
|---------|------|
| PascalCase `type_name` | `UserId`, `HTTPStatus` — converted to snake_case for ID |
| `base_type` selection | Use most specific: `enum` > `string`, `record` > `object` |
| Nullable always explicit | Set `nullable: true/false` — never omit |
| Constraint mirroring | Frontmatter `constraints` object AND body Constraints section must match |
| Composition required | `union`/`intersection`/`tuple` MUST include `composition.mode` + `members` |
| Discriminated union | Add `discriminant_field` to `composition` for tagged sum types |
| Generics bound | Every generic param needs `bound` (use `"any"` if unconstrained) |
| Examples required | At least one concrete value + `note` in `examples` array |
**base_type allowed values**: `string`, `integer`, `number`, `boolean`, `array`, `object`, `enum`, `union`, `intersection`, `tuple`, `record`
**Constraint keys by base_type**:
| base_type | Applicable constraints |
|-----------|----------------------|
| string | `min_length`, `max_length`, `pattern`, `format` |
| integer / number | `minimum`, `maximum`, `exclusive_minimum`, `exclusive_maximum` |
| array | `min_items`, `max_items`, `unique_items` |
| enum | `allowed_values` |
| object / record | `required_keys` |
**Boundary — what type_def is NOT**:
| kind | Why NOT type_def |
|------|-----------------|
| `input_schema` | Concrete input contract for one artifact — not reusable vocabulary |
| `validator` | Executable pass/fail logic — not a declaration |
| `validation_schema` | Post-generation system contract — governs outputs, not types |
| `interface` | Bilateral runtime handshake — not a type declaration |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| `base_type: object` when enum suffices | Loses constraint expressiveness; breaks consumer validation |
| Omitting `composition` for union/intersection types | Schema-invalid; member resolution breaks downstream |
| PascalCase in `id` field | Regex `^p06_td_[a-z]...` rejects immediately |
| Overriding parent constraints without `overrides` list | Silent override corrupts inheritance chain |
| Setting `quality` to a score | Governance assigns quality; self-scoring is invalid |
| Embedding business logic in constraints | Types define shape, not behavior — use `validator` for logic |
| Skipping `serialization` on wire-crossing types | Consumers assume defaults; format mismatches at runtime |
## Application
1. Identify the canonical PascalCase `type_name` and its owning `domain`
2. Choose `base_type` — most specific fit from the allowed enum
3. Set `nullable: true/false` explicitly
4. Set `id` = `p06_td_{type_name_snake}`, `layer: spec`, `kind: type_def`
5. Define `constraints` object with keys matching the chosen `base_type`
6. If composite (`union`/`intersection`/`tuple`): add `composition` with `mode` + `members`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_type_def]] | downstream | 0.56 |
| [[bld_schema_type_def]] | downstream | 0.56 |
| [[p03_sp_type-def-builder]] | downstream | 0.50 |
| [[bld_architecture_type_def]] | downstream | 0.46 |
| [[bld_config_type_def]] | downstream | 0.41 |
| [[p11_qg_type_def]] | downstream | 0.41 |
| [[type-def-builder]] | downstream | 0.41 |
| [[bld_output_template_type_def]] | downstream | 0.37 |
| [[bld_memory_type_def]] | downstream | 0.36 |
| [[bld_examples_type_def]] | downstream | 0.32 |
