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
