---
kind: examples
id: bld_examples_decision_record
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of decision_record artifacts
pattern: few-shot learning — LLM reads these before producing
---

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
author: "EDISON"
quality: null
tags: [decision_record, database, P08, storage, postgresql]
tldr: "Chose PostgreSQL over MongoDB for CEX artifact store: stable schema + relational queries outweigh document store flexibility."
consequences: "Relational queries are fast and type-safe. Schema migrations required for frontmatter changes. MongoDB expertise on team becomes less relevant."
options:
  - "PostgreSQL with JSONB"
  - "MongoDB"
  - "SQLite (embedded)"
deciders: ["EDISON", "ATLAS"]
date_decided: "2026-03-29"
```
## Context
CEX artifacts have a stable YAML frontmatter structure with well-defined fields (id, kind, pillar, status, tags). The primary access patterns are: filter by kind, filter by pillar, full-text search on tldr, and join between artifacts and quality scores. A MongoDB prototype was built in v1 but the document model provided no benefit once schemas stabilized. The team's operational tooling (Railway, migrations, backups) is already PostgreSQL-native.
## Options Considered
### Option A: PostgreSQL with JSONB
Stores artifact frontmatter as structured columns with JSONB overflow for optional fields.
Pros:
- Native support for relational queries (filter by pillar + kind + status in one query)
- JSONB indexing handles semi-structured optional fields efficiently
- Team already operates PostgreSQL on Railway — no new operational surface
Cons:
- Schema migrations required when new required frontmatter fields are added
- Less flexible for highly variable artifact structures (not a concern given stable schema)
### Option B: MongoDB
Document store where each artifact is a BSON document.
Pros:
- Schema-free: new frontmatter fields require no migration
- Natural fit for JSON/YAML document storage
Cons:
- No relational join support — cross-artifact queries require application-side joins
- Additional operational complexity (separate MongoDB instance vs. existing PostgreSQL)
- Team has limited MongoDB operational experience
### Option C: SQLite (embedded)
Embedded relational database, zero operational overhead.
Pros:
- Zero infrastructure cost; runs in-process
Cons:
- No concurrent write support for multi-satellite environments
- Not suitable for Railway deployment with horizontal scaling
## Decision
We will use Option A: PostgreSQL with JSONB. PostgreSQL's relational query capabilities match the primary access patterns, the team already operates it on Railway, and the schema has been stable for two versions. The JSONB column handles optional frontmatter fields without requiring column-per-field proliferation.
## Consequences
**Positive:**
- Artifact queries by pillar, kind, and status execute in a single indexed SQL query
- Operational runbook already exists — no new infrastructure to learn
- Type-safe migrations enforce schema discipline at the database layer
**Negative:**
- Adding new required frontmatter fields requires a schema migration — cannot be done ad hoc
- MongoDB prototype code (approximately 400 lines) must be replaced before launch
**Neutral:**
- JSONB overflow column handles optional fields without schema changes for optional additions
- MongoDB expertise on the team becomes less relevant for this project

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p08_adr_ pattern with snake_case slug (H02 pass)
- kind: decision_record (H04 pass)
- All 5 required frontmatter fields present and non-empty (H06 pass)
- status: accepted — valid enum value (H07 pass)
- All 4 body sections present (H08 pass)
- 3 options documented with pros/cons (H09 pass — exceeds minimum of 2)
- Consequences include negative effects (SOFT: consequence honesty pass)
- Decision states chosen option in first sentence (SOFT: decision clarity pass)
- Context explains forces without stating the decision (SOFT: context quality pass)

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
6. tags: only 1 item, missing "decision_record" -> SOFT FAIL
7. Body missing ## Context, ## Options Considered, ## Consequences sections -> H08 FAIL
8. No options considered — only decision stated -> H09 FAIL
9. "Because they are scalable" is not a rationale — no tradeoffs or alternatives -> SOFT: consequence honesty FAIL
10. context field absent — reader cannot evaluate if decision still applies -> H06 FAIL
