---
id: p11_qg_enum_def
kind: quality_gate
pillar: P11
title: "Gate: enum_def"
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
domain: "enumeration definition — finite named value sets with per-value descriptions and framework representations"
quality: 9.0
tags: [quality-gate, enum-def, P06, enumeration, finite-values, schema]
tldr: "Pass/fail gate for enum_def artifacts: value completeness, per-value descriptions, extensibility declaration, and framework representation accuracy."
density_score: 0.90
llm_function: GOVERN
---
# Gate: enum_def
## Definition
| Field | Value |
|---|---|
| metric | enum_def artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: enum_def` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p06_enum_[a-z][a-z0-9_]+$` | ID contains uppercase, spaces, hyphens, or missing prefix |
| H03 | ID equals filename stem | `id: p06_enum_status` but file is `p06_enum_state.md` |
| H04 | Kind equals literal `enum_def` | `kind: type_def` or `kind: schema` or any other value |
| H05 | Quality field is null | `quality: 8.0` or any non-null value |
| H06 | All required fields present | Missing `values`, `name`, `version`, `tldr`, or `tags` |
| H07 | At least 2 values defined | `values: [SINGLE]` or `values: []` — single value is a constant |
| H08 | Values list in frontmatter matches ## Values body section names | Frontmatter has VALUE_A but body has no `### VALUE_A` section |
| H09 | All deprecated values also appear in values list | `deprecated: [OLD_VAL]` but `OLD_VAL` not in `values` |
| H10 | Default value (if set) appears in values list | `default: UNKNOWN` but UNKNOWN not in `values` |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Value coverage | 1.0 | All meaningful domain values represented; no obvious omissions |
| Per-value descriptions | 1.0 | Each value has a clear description explaining meaning and when to use |
| Extensibility declaration | 1.0 | extensible field present and accurate for the domain |
| Default documentation | 0.5 | Default value documented if the field has a natural default |
| Deprecation clarity | 0.5 | Deprecated values listed with reason; migration path noted |
| Framework representations | 1.0 | Usage section covers at least JSON Schema + one of: Pydantic, Zod, TypeScript |
| Boundary clarity | 1.0 | Explicitly not a type_def, input_schema, or validator — finite value set stated |
| Domain specificity | 1.0 | Values specific to the declared domain; no generic placeholder values |
| Naming consistency | 0.5 | All values follow same case convention (SCREAMING_SNAKE or lowercase) |
| Tldr density | 0.5 | tldr <= 160 chars and includes value count + domain context |
| Testability | 1.0 | Each value testsble — consumer can validate "is X in this enum?" |
| Deprecation safety | 1.0 | Deprecated values retained in list; removal only in major version bump |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Internal scratch enum used only during development, never referenced by other artifacts |
| approver | Author self-certification with comment explaining transient scope |
| audit_trail | Bypass note in frontmatter comment with expiry date |
| expiry | 14d — scratch enums must be promoted to >= 7.0 or removed |
| never_bypass | H01 (unparseable YAML breaks all tooling), H05 (self-scored gates corrupt quality metrics), H07 (single-value enum is a constant — wrong kind) |
