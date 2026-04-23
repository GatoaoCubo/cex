---
quality: 8.4
quality: 8.0
kind: collaboration
id: bld_collaboration_event_schema
pillar: P12
llm_function: COLLABORATE
purpose: How event-schema-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
title: "Collaboration Event Schema"
version: "1.0.0"
author: n03_builder
tags: [event_schema, builder, collaboration]
tldr: "Event payload schema specialist. Upstream of agent event consumers and data contracts. Downstream of state machine and domain model."
domain: "event schema construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_collaboration_hook
  - bld_collaboration_webhook
  - p01_kc_signal
  - bld_collaboration_input_schema
  - bld_collaboration_validation_schema
  - bld_collaboration_builder
  - bld_architecture_kind
  - p03_sp_signal_builder
  - bld_collaboration_response_format
  - kind-builder
---
# Collaboration: event-schema-builder
## My Role in Crews
| Responsibility | What I Answer | What I DON'T Do |
|----------------|---------------|-----------------|
| EVENT PAYLOAD SCHEMA SPECIALIST | "What is the structure and versioning of this event?" | Define infrastructure (Kafka topics) |
| CloudEvents/AsyncAPI format | Payload schema, versioning, routing metadata | Define SLAs (data contracts) |
| Schema lifecycle | Versioning strategy, consumer compatibility | Handle REST API contracts |
## Crew Compositions
### Crew: "Domain Model Package"
```
  1. state-machine-builder    -> "entity lifecycle FSMs (emit events on transitions)"
  2. event-schema-builder     -> "domain event payload schemas"
  3. data-contract-builder    -> "producer-consumer SLAs on top of schemas"
  4. openapi-spec-builder     -> "REST endpoints alongside event API"
```
### Crew: "Event-Driven Integration"
```
  1. context-map-builder      -> "BC relationships and integration patterns"
  2. event-schema-builder     -> "event payload schemas per BC boundary"
  3. agent-builder            -> "event consumer agents"
  4. workflow-builder         -> "orchestration triggered by events"
```
### Crew: "API Surface Package"
```
  1. openapi-spec-builder     -> "REST API contract"
  2. event-schema-builder     -> "async event API contract"
  3. api-reference-builder    -> "unified human-readable API docs"
```
## Handoff Protocol
### I Receive
| Input | Type | Notes |
|-------|------|-------|
| Domain event name | string | What happened: OrderCreated, UserRegistered |
| Producing service name | string | Source URI |
| Entity identifier | string | Subject field value |
| Data fields | list | Fields the event carries |
| Consumer services | list | Who subscribes and what they do |
### I Produce
| Output | Format | Destination |
|--------|--------|-------------|
| event_schema artifact | .md with YAML frontmatter + JSON Schema | N0X_{domain}/P06_schema/ |
| Compilation signal | complete with quality score | .cex/runtime/signals/ |
## Builders I Depend On
| Builder | Why | Dependency Type |
|---------|-----|----------------|
| state-machine-builder | State transitions are the trigger for domain events | optional |
| context-map-builder | BC boundaries define event routing patterns | optional |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| agent-builder | Agents subscribe to and react to events |
| data-contract-builder | Data contract wraps event_schema with SLA obligations |
| workflow-builder | Event-triggered workflows reference event schema |
| openapi-spec-builder | Webhooks in REST APIs reference event schemas |
## Quality Checklist Before Signal
| Check | Pass Condition |
|-------|---------------|
| id pattern | ^p06_evs_[a-z][a-z0-9_]+$ |
| event_type | includes .v{N} version suffix |
| schema_version | valid semver |
| datacontenttype | "application/json" |
| payload | JSON Schema format with required fields |
| versioning strategy | ADDITIVE_ONLY or VERSIONED_TYPE declared |
| consumers | at least one consumer documented |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_hook]] | sibling | 0.37 |
| [[bld_collaboration_webhook]] | sibling | 0.35 |
| [[p01_kc_signal]] | related | 0.34 |
| [[bld_collaboration_input_schema]] | sibling | 0.34 |
| [[bld_collaboration_validation_schema]] | sibling | 0.33 |
| [[bld_collaboration_builder]] | sibling | 0.33 |
| [[bld_architecture_kind]] | upstream | 0.32 |
| [[p03_sp_signal_builder]] | upstream | 0.29 |
| [[bld_collaboration_response_format]] | sibling | 0.29 |
| [[kind-builder]] | upstream | 0.29 |
