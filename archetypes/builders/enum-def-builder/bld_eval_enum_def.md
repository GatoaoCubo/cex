---
kind: quality_gate
id: p11_qg_enum_def
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of enum_def artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: enum_def"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, enum-def, P06, enumeration, finite-values, schema]
tldr: "Pass/fail gate for enum_def artifacts: value completeness, per-value descriptions, extensibility declaration, and framework representation accuracy."
domain: "enumeration definition — finite named value sets with per-value descriptions and framework representations"
created: "2026-03-29"
updated: "2026-03-29"
density_score: 0.90
related:
  - bld_instruction_enum_def
  - p03_sp_enum_def_builder
  - bld_knowledge_card_enum_def
  - bld_architecture_enum_def
  - bld_schema_enum_def
  - bld_examples_enum_def
  - p11_qg_chunk_strategy
  - p10_lr_enum_def_builder
  - bld_config_enum_def
  - p11_qg_constraint_spec
---

## Quality Gate

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

## Examples

# Examples: enum-def-builder
## Golden Example
INPUT: "Create enum for CEX artifact publication status"
OUTPUT:
```yaml
id: p06_enum_publication_status
kind: enum_def
pillar: P06
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
name: "Publication Status"
values:
  - draft
  - review
  - published
  - deprecated
  - archived
default: "draft"
extensible: false
deprecated: []
quality: 8.8
tags: [enum_def, publication, status, P06]
tldr: "5-value publication lifecycle enum: draft->review->published->deprecated->archived"
description: "Lifecycle states for CEX artifacts from initial creation through archival"
descriptions:
  draft: "Initial state — artifact is being authored, not yet ready for review"
  review: "Artifact submitted for quality gate evaluation; no edits until review complete"
  published: "Artifact passed quality gates and is available in the pool"
  deprecated: "Artifact superseded by a newer version; retained for compatibility"
  archived: "Artifact removed from active use; preserved for historical reference only"
representations:
  json_schema: '{"enum": ["draft", "review", "published", "deprecated", "archived"]}'
  pydantic: "class PublicationStatus(str, Enum): DRAFT = 'draft'"
  zod: 'z.enum(["draft", "review", "published", "deprecated", "archived"])'
  graphql: "enum PublicationStatus { DRAFT REVIEW PUBLISHED DEPRECATED ARCHIVED }"
  typescript: 'type PublicationStatus = "draft" | "review" | "published" | "deprecated" | "archived";'
```
## Overview
Lifecycle states for CEX artifacts progressing from authoring through archival. Used by pool indexers, quality gate runners, and routing systems to filter by readiness.
## Values
### draft
Initial state. Artifact is being authored. Quality gates not run. Not visible in pool.
### review
Submitted for quality gate evaluation. No edits permitted until review complete.
### published
Passed all HARD gates and met score threshold. Available in pool for routing.
### deprecated
Superseded by newer version. Retained for backward compatibility; do not route new requests here.
### archived
Removed from active routing. Preserved for historical reference and audit trail only.
## Usage
JSON Schema: `{"enum": ["draft", "review", "published", "deprecated", "archived"]}`
Pydantic: `class PublicationStatus(str, Enum): DRAFT = "draft"`
Zod: `z.enum(["draft", "review", "published", "deprecated", "archived"])`
TypeScript: `type PublicationStatus = "draft" | "review" | "published" | "deprecated" | "archived";`
## Constraints
Default: draft. Extensible: no. Deprecated: none.

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p06_enum_ pattern (H02 pass)
- kind: enum_def (H04 pass)
- values list matches ## Values section names exactly (H08 pass)
- 5 values >= 2 minimum (H07 pass)
- deprecated: [] subset of values (H09 pass)
- default "draft" in values list (H10 pass)
- all required fields present (H06 pass)
## Anti-Example
INPUT: "Create enum for order status"
BAD OUTPUT:
```yaml
id: OrderStatus
kind: type_def
pillar: schema
name: Order Status
values: [active]
quality: 8.5
tags: [order]
```
Order statuses for the system.
FAILURES:
1. id: "OrderStatus" has uppercase and no `p06_enum_` prefix -> H02 FAIL
2. kind: "type_def" not "enum_def" -> H04 FAIL
3. pillar: "schema" not "P06" -> H06 FAIL
4. quality: 8.5 (not null) -> H05 FAIL
5. values: [active] — only 1 value, that is a constant -> H07 FAIL
6. Missing fields: version, created, updated, author, tldr -> H06 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
