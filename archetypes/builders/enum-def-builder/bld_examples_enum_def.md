---
kind: examples
id: bld_examples_enum_def
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of enum_def artifacts
pattern: few-shot learning — LLM reads these before producing
---

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
author: "EDISON"
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
quality: null
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
Lifecycle states for CEX artifacts progressing from authoring through archival.
Used by pool indexers, quality gate runners, and routing systems to filter by readiness.
## Values
### draft
Initial state. Artifact is being authored. Quality gates have not been run. Not visible in pool.
### review
Artifact submitted for quality gate evaluation. No edits permitted until review completes.
### published
Artifact passed all HARD gates and met score threshold. Available in pool for routing.
### deprecated
Artifact has been superseded. Retained in pool for backward compatibility; do not route new requests here.
### archived
Artifact removed from active routing. Preserved for historical reference and audit trail only.
## Usage
JSON Schema: `{"enum": ["draft", "review", "published", "deprecated", "archived"]}`
Pydantic: `class PublicationStatus(str, Enum): DRAFT = "draft"`
Zod: `z.enum(["draft", "review", "published", "deprecated", "archived"])`
GraphQL: `enum PublicationStatus { DRAFT REVIEW PUBLISHED DEPRECATED ARCHIVED }`
TypeScript: `type PublicationStatus = "draft" | "review" | "published" | "deprecated" | "archived";`
## Constraints
Default: draft
Extensible: no — set is closed; state machine transitions are fixed
Deprecated: none
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p06_enum_ pattern (H02 pass)
- kind: enum_def (H04 pass)
- values list matches ## Values section names exactly (H08 pass)
- 5 values >= 2 minimum (H07 pass)
- deprecated: [] subset of values (H09 pass)
- default "draft" in values list (H10 pass)
- all required fields present (H06 pass)
- per-value descriptions in frontmatter + body (S02 pass)
- extensible declared (S03 pass)
- 4 framework representations (S06 pass)
- tldr: 62 chars <= 160 (S10 pass)
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
7. tags: only 1 item, missing "enum_def" -> SOFT FAIL
8. No descriptions per value -> SOFT FAIL
9. No extensible declaration -> SOFT FAIL
10. No ## Usage section with framework representations -> SOFT FAIL
11. No ## Constraints section -> SOFT FAIL
12. Body missing ## Values, ## Usage, ## Constraints sections -> SOFT FAIL
