---
kind: quality_gate
id: p11_qg_decision_record
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of decision_record artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: decision_record"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, decision-record, P08, ADR, architecture, status-lifecycle]
tldr: "Pass/fail gate for decision_record artifacts: context completeness, options coverage, consequence honesty, and status lifecycle integrity."
domain: "architecture decision record — single significant choice documented with context, options, rationale, and consequences"
created: "2026-03-29"
updated: "2026-03-29"
density_score: 0.90
related:
  - bld_examples_decision_record
  - bld_architecture_decision_record
  - bld_instruction_decision_record
  - p03_sp_decision_record_builder
  - p11_qg_chunk_strategy
  - bld_schema_decision_record
  - decision-record-builder
  - bld_knowledge_card_decision_record
  - p11_qg_function_def
  - p10_lr_decision_record_builder
---

## Quality Gate

# Gate: decision_record
## Definition
| Field | Value |
|---|---|
| metric | decision_record artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: decision_record` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error |
| H02 | ID matches `^p08_adr_[a-z][a-z0-9_]+$` | Uppercase, hyphens, or missing prefix |
| H03 | ID equals filename stem | ID/filename mismatch |
| H04 | Kind equals literal `decision_record` | Any other value |
| H05 | Quality field is null | Any non-null value |
| H06 | Required fields present: id, title, status, context, decision | Any missing or empty |
| H07 | Status is one of: proposed, accepted, deprecated, superseded | Unrecognized value |
| H08 | Body contains all 4 required sections | Missing Context, Options, Decision, or Consequences |
| H09 | At least 2 options in ## Options Considered | Only 1 or empty |
| H10 | If status == superseded: superseded_by populated | superseded_by null or absent |
## SOFT Scoring
| Dimension | Weight | Criteria |
|---|---|---|
| Context quality | 1.5 | Forces and constraints clear; reader understands why a decision was needed |
| Options completeness | 1.5 | Each option has name, description, pros, cons |
| Decision clarity | 1.5 | Chosen option stated first; rationale references options |
| Consequence honesty | 1.5 | >= 1 negative consequence; consequences are specific |
| Status accuracy | 1.0 | Status matches actual state; supersession links traversable |
| Tradeoff specificity | 1.0 | Concrete effects named, not vague claims |
| Options count | 0.5 | 3+ signals thorough evaluation; 2 is minimum |
| Deciders documented | 0.5 | deciders field populated |
| Related ADRs linked | 0.5 | related_to populated where dependencies exist |
| Boundary clarity | 1.0 | Explicitly not a law, not a pattern, not a diagram |
| Domain specificity | 1.0 | Context/decision/consequences specific to declared domain |
| Future guidance | 0.5 | Consequences give signal to decide whether to revisit |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference ADR |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Provisional ADR under time pressure; full review within 7 days |
| approver | Author self-certification with expiry date in frontmatter comment |
| expiry | 7d — must reach >= 7.0 or be deprecated |
| never_bypass | H01 (breaks tooling), H05 (corrupts metrics), H07 (breaks lifecycle tooling) |

## Examples

# Examples: decision-record-builder
## Golden Example
INPUT: "Document the decision to use PostgreSQL instead of MongoDB for the CEX artifact store"
OUTPUT:
```yaml
id: p08_adr_artifact_store_database
kind: decision_record
pillar: P08
title: "Use PostgreSQL for CEX artifact store"
status: accepted
context: "CEX artifacts have structured frontmatter (YAML) and require queries by pillar, kind, status, and tag. Early prototypes used MongoDB for schema flexibility, but artifact schemas stabilized in v2 and relational queries became the dominant access pattern."
decision: "Use PostgreSQL with JSONB columns for artifact storage, replacing the MongoDB prototype."
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
quality: 8.9
tags: [decision_record, database, P08, storage, postgresql]
tldr: "Chose PostgreSQL over MongoDB for CEX artifact store: stable schema + relational queries outweigh document store flexibility."
consequences: "Relational queries are fast and type-safe. Schema migrations required for frontmatter changes. MongoDB expertise on team becomes less relevant."
options:
  - "PostgreSQL with JSONB"
  - "MongoDB"
  - "SQLite (embedded)"
deciders: ["builder_agent", "operations_agent"]
date_decided: "2026-03-29"
```
## Context
CEX artifacts have stable YAML frontmatter. Primary access: filter by kind/pillar, full-text search on tldr. MongoDB prototype v1 provided no benefit once schemas stabilized; operational tooling is PostgreSQL-native on Railway.
## Options Considered
- **A: PostgreSQL with JSONB** — native relational queries, JSONB for optional fields, team already operates on Railway. Con: schema migrations for new required fields.
- **B: MongoDB** — schema-free, natural JSON storage. Con: no relational joins, additional ops complexity, limited team experience.
- **C: SQLite** — zero infra cost, in-process. Con: no concurrent writes, not suitable for Railway horizontal scaling.
## Decision
Use Option A: PostgreSQL with JSONB. Relational queries match primary access patterns; team already operates it; schema stable for two versions.
## Consequences
**Positive:** artifact queries by pillar/kind/status in single indexed SQL query; operational runbook exists.
**Negative:** new required frontmatter fields require migration; MongoDB prototype (~400 lines) must be replaced.
**Neutral:** JSONB handles optional fields; MongoDB expertise less relevant.

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p08_adr_ pattern with snake_case slug (H02 pass)
- kind: decision_record (H04 pass)
- All 5 required frontmatter fields present and non-empty (H06 pass)
- status: accepted — valid enum value (H07 pass)
- All 4 body sections present (H08 pass)
- 3 options with pros/cons (H09 pass)
- Consequences include negative effects (SOFT: consequence honesty pass)
- Decision states chosen option in first sentence (SOFT: decision clarity pass)

## Anti-Example
INPUT: "Document the decision to use microservices"
BAD OUTPUT:
```yaml
id: microservices-decision
kind: adr
status: active
decision: "Use microservices"
quality: 8.5
tags: [architecture]
```
We decided to use microservices because they are scalable.
FAILURES:
1. id: "microservices-decision" has hyphens and no `p08_adr_` prefix -> H02 FAIL
2. kind: "adr" not "decision_record" -> H04 FAIL
3. status: "active" not in enum (proposed/accepted/deprecated/superseded) -> H07 FAIL
4. quality: 8.5 (not null) -> H05 FAIL
5. Missing required fields: title, context, version, created, updated, author, tldr -> H06 FAIL
6. Body missing ## Context, ## Options Considered, ## Consequences -> H08 FAIL
7. No options considered — only decision stated -> H09 FAIL
8. "Because they are scalable" — no tradeoffs or alternatives -> SOFT: consequence honesty FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
