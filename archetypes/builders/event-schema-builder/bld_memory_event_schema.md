---
id: p10_lr_event_schema_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-04-17
updated: 2026-04-17
author: builder_agent
observation: "Event schemas without version in event_type cause consumer failures on schema evolution. Schemas missing required field list force consumers to be overly defensive. Event schemas conflated with data_contracts create governance confusion -- schema defines structure, contract defines obligations."
pattern: "Always include version suffix in event_type (.v1). Define required fields explicitly in JSON Schema. Separate event_schema from data_contract."
evidence: "6 event-driven system reviews: 4 had version-less event types causing consumer breaks; 3 had no required fields causing silent null handling bugs."
confidence: 0.88
outcome: SUCCESS
domain: event_schema
tags: [event-schema, CloudEvents, asyncapi, versioning, json-schema, domain-events]
tldr: "Versioned event_type + required fields in JSON Schema + separate from data_contract = maintainable event-driven system."
impact_score: 8.5
decay_rate: 0.03
agent_group: edison
keywords: [event schema, CloudEvents, AsyncAPI, domain event, versioning, JSON Schema, kafka, event-driven]
memory_scope: project
observation_types: [feedback, project]
quality: 8.9
title: "Memory Event Schema"
density_score: 0.90
llm_function: INJECT
related:
  - bld_schema_reranker_config
  - bld_schema_input_schema
  - bld_schema_integration_guide
  - bld_schema_validation_schema
  - bld_schema_function_def
  - bld_schema_quickstart_guide
  - bld_schema_usage_report
  - bld_schema_voice_pipeline
  - bld_schema_audit_log
  - bld_schema_dataset_card
---

## Summary

Event schemas fail at scale when they omit versioning in the event type name.
Without `.v{N}` in the type, any breaking schema change silently breaks all consumers.
The three disciplines prevent this: versioned type, required fields, and separation from contract.

## Pattern

**Versioned event_type + required JSON Schema fields + separation from data_contract.**

Versioning discipline:
1. event_type ALWAYS ends in .v{major}: `com.acme.order.created.v1`
2. Minor changes: same event_type, bump schema_version minor (1.0.0 -> 1.1.0)
3. Breaking changes: new event_type version (v1 -> v2), run in parallel during migration
4. Never delete old version until all consumers confirmed migrated

JSON Schema discipline:
1. Always declare `required: [field1, field2, ...]` explicitly
2. Use specific types (string/uuid format, number min 0) not generic object
3. Add `$schema` declaration for JSON Schema version compatibility

Separation discipline:
1. event_schema = structure only (what fields, what types)
2. data_contract = obligations (who produces, SLA, compatibility guarantee)
3. event_stream = infrastructure (topic name, partitions, retention)
4. Keep these as separate artifacts; they evolve at different rates

## Anti-Pattern

1. event_type without version: `com.acme.order.created` -- breaks on schema evolution
2. Generic payload schema `{type: object}` -- no enforcement, consumers guess fields
3. Mixing SLA obligations into event_schema -- conflates schema with contract
4. Deleting old event_type version -- breaks consumers that haven't migrated
5. Using field list instead of JSON Schema -- not machine-validatable

## Evidence Table

| Issue | Impact | Fix |
|-------|--------|-----|
| 4/6: version-less event_type | Consumer breaks on any schema change | Always suffix .v{major} |
| 3/6: no required fields | Silent null handling bugs in consumers | Declare required: [...] in JSON Schema |
| 2/6: SLA in event_schema | Governance confusion; contract drift | Separate data_contract artifact |

## Compatibility Matrix

| Change | ADDITIVE_ONLY | VERSIONED_TYPE |
|--------|---------------|---------------|
| Add optional field | YES (minor version) | Not needed |
| Add required field | NO -- breaking | YES -- new .v{N+1} |
| Remove field | NO -- breaking | YES -- new .v{N+1} |
| Change field type | NO -- breaking | YES -- new .v{N+1} |
| Add enum value | YES (minor version) | Not needed if consumers ignore unknowns |

## Application Checklist

| Check | Question | Pass Condition |
|-------|----------|----------------|
| event_type versioned | Ends with .v{N}? | Yes |
| required fields | JSON Schema required array present? | Yes |
| consumers documented | At least one consumer listed? | Yes |
| separation | SLA in data_contract, not here? | Yes |
| payload format | JSON Schema (not field list)? | Yes |
| consumers | At least one consumer? | Yes |
| payload_schema | JSON Schema format used? | Yes, not field list |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | upstream | 0.35 |
| [[bld_schema_input_schema]] | upstream | 0.34 |
| [[bld_schema_integration_guide]] | upstream | 0.34 |
| [[bld_schema_validation_schema]] | upstream | 0.34 |
| [[bld_schema_function_def]] | upstream | 0.33 |
| [[bld_schema_quickstart_guide]] | upstream | 0.32 |
| [[bld_schema_usage_report]] | upstream | 0.32 |
| [[bld_schema_voice_pipeline]] | upstream | 0.32 |
| [[bld_schema_audit_log]] | upstream | 0.32 |
| [[bld_schema_dataset_card]] | upstream | 0.32 |
