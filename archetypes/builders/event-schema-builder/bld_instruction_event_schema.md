---
kind: instruction
id: bld_instruction_event_schema
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for event_schema
pattern: 3-phase pipeline (define -> compose -> validate)
quality: null
title: "Instruction Event Schema"
version: "1.0.0"
author: n03_builder
tags: [event_schema, builder, instruction]
tldr: "3-phase: define event type and source, design JSON Schema payload, document versioning and consumers."
domain: "event schema construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Instructions: How to Produce an event_schema

## Phase 1: DEFINE

1. Identify the domain event name and producing service
2. Construct event_type using reverse-DNS + version: `{reverse_domain}.{aggregate}.{event}.v{major}`
3. Identify the source URI (producing service endpoint or name)
4. Design the payload data structure: what fields does this event carry?
5. Classify fields: required vs optional
6. Define field types using JSON Schema primitives (string, number, integer, boolean, array, object)
7. Identify subject: what is the primary entity identifier in this event?
8. Identify consumers: who subscribes to this event and what do they do with it?
9. Decide evolution strategy: ADDITIVE_ONLY or VERSIONED_TYPE for breaking changes

## Phase 2: COMPOSE

1. Read SCHEMA.md and OUTPUT_TEMPLATE.md
2. Fill frontmatter: all required fields (quality: null)
3. Set id: `p06_evs_{event_slug}` -- verify pattern `^p06_evs_[a-z][a-z0-9_]+$`
4. Write CloudEvents Attributes section: envelope fields table
5. Write Payload Schema section: JSON Schema for data field (full schema, not field list)
6. Write Versioning section: compatibility strategy, breaking change policy, migration path
7. Write Consumers section: who subscribes and what action they take
8. Verify body <= 4096 bytes

## Phase 3: VALIDATE

1. Confirm id matches `^p06_evs_[a-z][a-z0-9_]+$`
2. Confirm kind == event_schema
3. Confirm event_type follows reverse-DNS naming with .v{N} suffix
4. Confirm schema_version is semver
5. Confirm datacontenttype is "application/json"
6. Confirm all 4 sections present
7. Confirm payload is JSON Schema format (not field list)
8. Cross-check: not data_contract (no SLA), not event_stream (no infrastructure)
9. Confirm quality: null
10. Revise if score < 8.0
