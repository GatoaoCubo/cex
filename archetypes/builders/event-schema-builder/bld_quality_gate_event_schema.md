---
id: p11_qg_event_schema
kind: quality_gate
pillar: P11
title: "Gate: event_schema"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "builder_agent"
domain: "event schema -- CloudEvents/AsyncAPI payload schema for event-driven systems"
quality: null
tags: [quality-gate, event-schema, P06, cloudevents, asyncapi]
tldr: "Pass/fail gate for event_schema: id pattern, event_type versioning, JSON Schema payload, schema_version, all 4 sections."
density_score: 0.90
llm_function: GOVERN
---

# Gate: event_schema

## Definition

| Field | Value |
|---|---|
| metric | event_schema artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: event_schema` |

## HARD Gates

All must pass (AND logic). Any single failure = REJECT.

| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p06_evs_[a-z][a-z0-9_]+$` | ID contains uppercase, hyphens, or missing prefix |
| H03 | ID equals filename stem | id: p06_evs_foo but file is p06_evs_bar.md |
| H04 | Kind equals literal `event_schema` | kind: event or any other value |
| H05 | Quality field is null | quality: 8.0 or any non-null value |
| H06 | event_type includes version suffix (.v{N}) | "com.acme.order.created" without version |
| H07 | schema_version is semver | "v1" instead of "1.0.0" |
| H08 | datacontenttype is "application/json" | Missing or non-JSON content type |
| H09 | Payload Schema is JSON Schema format | Field list instead of JSON Schema |
| H10 | Body has all 4 required sections | Missing CloudEvents Attributes, Payload Schema, Versioning, or Consumers |

## SOFT Scoring

| Dimension | Weight | Criteria |
|---|---|---|
| Payload schema completeness | 1.0 | All fields typed; required fields explicit |
| CloudEvents attributes documented | 1.0 | All 7 CloudEvents attributes covered |
| Versioning strategy | 1.0 | ADDITIVE_ONLY or VERSIONED_TYPE declared with rules |
| Consumer table | 1.0 | At least one consumer identified with action |
| event_type naming convention | 0.5 | Follows reverse-DNS pattern |
| Breaking change policy | 1.0 | Clear rules for what triggers new version |
| subject field usage | 0.5 | Subject attribute identifies entity |
| Boundary clarity | 1.0 | Explicitly NOT data_contract, NOT event_stream |
| tldr quality | 0.5 | tldr <= 160ch, includes event name and version |

## Actions

| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
