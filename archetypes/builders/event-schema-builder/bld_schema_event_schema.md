---
kind: schema
id: bld_schema_event_schema
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for event_schema
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 8.7
title: "Schema Event Schema"
version: "1.0.0"
author: n03_builder
tags: [event_schema, builder, schema]
tldr: "Schema for event_schema: event_type (reverse-DNS), payload JSON Schema, schema_version, CloudEvents attributes."
domain: "event schema construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_search_strategy
  - bld_schema_dataset_card
  - bld_schema_integration_guide
  - bld_schema_quickstart_guide
  - bld_schema_audit_log
  - bld_schema_pitch_deck
  - bld_schema_benchmark_suite
  - bld_schema_voice_pipeline
---

# Schema: event_schema

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p06_evs_{slug}) | YES | - | Namespace compliance |
| kind | literal "event_schema" | YES | - | Type integrity |
| pillar | literal "P06" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact version |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| event_type | string (reverse-DNS) | YES | - | CloudEvents type attribute |
| schema_version | semver string | YES | "1.0.0" | Schema version for consumers |
| source | string (URI) | YES | - | Producing service URI |
| datacontenttype | literal "application/json" | YES | - | Payload MIME type |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "event_schema" |
| tldr | string <= 160ch | YES | - | Dense summary |

## ID Pattern

Regex: `^p06_evs_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Event Type Pattern

Format: `{reverse_dns_domain}.{aggregate}.{event}.v{major}`
Example: `com.example.order.created.v1`
Rule: MUST include version suffix for schema evolution.

## Body Structure (required sections)

1. `## CloudEvents Attributes` -- envelope field table
2. `## Payload Schema` -- JSON Schema for data field
3. `## Versioning` -- schema evolution strategy
4. `## Consumers` -- who subscribes to this event

## Constraints

- max_bytes: 4096 (body only)
- event_type MUST follow reverse-DNS naming with version suffix
- schema_version MUST be semver
- quality: null always
- NOT data_contract (no SLA), NOT event_stream (no infrastructure config)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | sibling | 0.64 |
| [[bld_schema_usage_report]] | sibling | 0.64 |
| [[bld_schema_search_strategy]] | sibling | 0.63 |
| [[bld_schema_dataset_card]] | sibling | 0.63 |
| [[bld_schema_integration_guide]] | sibling | 0.62 |
| [[bld_schema_quickstart_guide]] | sibling | 0.62 |
| [[bld_schema_audit_log]] | sibling | 0.61 |
| [[bld_schema_pitch_deck]] | sibling | 0.61 |
| [[bld_schema_benchmark_suite]] | sibling | 0.61 |
| [[bld_schema_voice_pipeline]] | sibling | 0.61 |
