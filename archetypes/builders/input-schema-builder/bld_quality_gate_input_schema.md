---
id: p11_qg_input_schema
kind: quality_gate
pillar: P11
title: "Gate: Input Schema"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "input_schema — unilateral entry contracts defining required fields, types, and coercion rules"
quality: 9.0
tags: [quality-gate, input-schema, contract, fields, validation, coercion]
tldr: "Gates ensuring input_schema artifacts define complete, typed, unambiguous entry contracts with defaults, coercion rules, and at least one example."
density_score: 0.89
llm_function: GOVERN
---
# Gate: Input Schema
## Definition
| Field     | Value |
|-----------|-------|
| metric    | weighted soft score + all hard gates pass |
| threshold | 7.0 to publish; 8.0 for pool; 9.5 for golden |
| operator  | AND (all hard) + weighted average (soft) |
| scope     | any artifact with `kind: input_schema` |
## HARD Gates
All must pass. Any failure = immediate reject.
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error on any field |
| H02 | ID matches `^[a-z][a-z0-9_-]+$` | Uppercase, spaces, or leading digit |
| H03 | ID equals filename stem | `id: create_input` in file `edit_input.md` |
| H04 | Kind equals literal `input_schema` | Any other kind value |
| H05 | Quality field is `null` | Any non-null value |
| H06 | All required fields present | Missing: fields, required, version, or owner |
| H07 | Every field entry has `type` and `description` | Any field missing type or description |
| H08 | All fields listed in `required` exist in `fields` | Required list names a field not defined in fields |
## SOFT Scoring
Total weights sum to 100%.
| ID  | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|-----|-----------|--------|--------|-------|-------|
| S01 | Type precision | 1.0 | Types use constrained vocabulary (string, integer, float, boolean, list, object, enum) | Types present but use freeform labels | Types missing or `any` used |
| S02 | Default coverage | 1.0 | All optional fields have explicit `default` values | Most optionals have defaults | No defaults on optional fields |
| S03 | Coercion rules | 1.0 | Fields that accept coercion list source types and target type explicitly | Coercion mentioned but unspecified | No coercion documentation |
| S04 | Constraint documentation | 1.0 | Fields with constraints (min, max, pattern, enum values) fully documented | Some constraints documented | Constraints implied but not stated |
| S05 | Error messages | 0.5 | Per-field error message or error code defined | Generic error messages only | No error documentation |
| S06 | Examples | 1.0 | At least 2 complete examples (one valid, one invalid input) | One example present | No examples |
| S07 | Required vs optional clarity | 0.5 | All fields unambiguously classified in `required` list | Mostly clear with minor gaps | Mixed required/optional with no list |
| S08 | Unilaterality enforced | 1.0 | Schema defines input only; no output fields included | Mostly unilateral; minor output leakage | Bilateral — mixes input and output |
| S09 | Naming convention | 0.5 | All field names are snake_case | Mostly snake_case with exceptions | camelCase or mixed throughout |
| S10 | Owner linkage | 0.5 | `owner` field references a specific agent or service | Owner field present but generic | No owner |
**Score = sum(pts * weight) / sum(max_pts * weight) * 10**
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | Golden | Publish to pool as golden input contract |
| >= 8.0 | Skilled | Publish to pool + log pattern |
| >= 7.0 | Learning | Use but flag for improvement |
| < 7.0 | Rejected | Return to author with gate report |
## Bypass
| Field | Value |
|-------|-------|
| Conditions | Rapidly evolving API where field set is not yet stable; schema explicitly marked `draft` |
| Approver | Owner agent lead |
| Audit trail | `bypass_reason` + `draft: true` both required in frontmatter |
| Expiry | Draft status expires after 14 days; must reach H-gate compliance or be deprecated |
