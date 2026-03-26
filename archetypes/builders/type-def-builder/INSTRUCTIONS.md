---
id: type-def-builder-instructions
kind: instructions
pillar: P03
llm_function: REASON
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
tags: [instructions, type-def, P03, execution-protocol]
---

## Execution Protocol

### Phase 1: DISCOVER (6 steps)

1. Extract the type name from the request and convert to `snake_case` for `type_slug`
2. Identify the domain context — which pillar, system, or module owns this type
3. Determine the `base_type`: primitive (`string`, `integer`, `boolean`, `number`, `array`, `object`, `enum`) or composite (`union`, `intersection`, `tuple`, `record`)
4. List all known constraints on this type (min/max, pattern, format, allowed values, cardinality)
5. Check if this type extends or composes another existing type_def — note its `id` for `inheritance`
6. Run `brain_query "type_def {type_name} constraints domain"` [IF MCP] to surface related artifacts

### Phase 2: COMPOSE (8 steps)

1. Set `id` to `p06_td_{type_slug}` — validate it matches the regex `^p06_td_[a-z][a-z0-9_]*$`
2. Set `kind: type_def`, `pillar: P06`, `layer: spec`
3. Set `type_name` to the canonical PascalCase name of the type
4. Assign `base_type` from the controlled vocabulary determined in DISCOVER step 3
5. Populate `constraints` as a structured object — each constraint key maps to its value or rule
6. If the type is composed of other types, populate `composition` with `mode` and `members` list
7. Set `nullable: false` unless domain evidence requires null membership — if nullable, document `nil_semantics`
8. Write `tldr` as one sentence: "A [base_type] representing [domain concept] with [key constraint]"

### Phase 3: VALIDATE (5 steps)

1. Verify `id` matches pattern `p06_td_[a-z][a-z0-9_]*` — reject if it contains uppercase or spaces
2. Count artifact bytes — must be <= 3072 (P06 `max_bytes` constraint)
3. Confirm every field in SCHEMA.md Required section is present and non-null (except `quality`)
4. Confirm `kind: type_def` and `pillar: P06` are set — hard reject if either is wrong
5. Confirm at least one entry exists in the `examples` section of the body
