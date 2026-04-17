---
kind: collaboration
id: bld_collaboration_context_map
pillar: P12
llm_function: COLLABORATE
purpose: How context-map-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: null
title: "Collaboration Context Map"
version: "1.0.0"
author: n03_builder
tags: [context_map, builder, collaboration]
tldr: "DDD strategic design specialist. Upstream of interface and workflow. Downstream of bounded context definition."
domain: "context map construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---
# Collaboration: context-map-builder
## My Role in Crews
| Responsibility | What I Answer | What I DON'T Do |
|----------------|---------------|-----------------|
| STRATEGIC DESIGN SPECIALIST | "How do BCs relate and what are the coupling implications?" | Define single BCs |
| DDD context mapping | Upstream/downstream, ACL, OHS, team coupling | Design deployment topology |
| Relationship documentation | Integration patterns + team risks | Write code architecture |
## Crew Compositions
### Crew: "DDD Architecture Review"
```
  1. bounded-context-builder  -> "individual BC definitions"
  2. context-map-builder      -> "BC relationship diagram with DDD patterns"
  3. decision-record-builder  -> "architectural decisions about integration patterns"
  4. interface-builder        -> "formal interfaces for ACL and OHS boundaries"
```
### Crew: "System Design Package"
```
  1. context-map-builder      -> "strategic design: BC relationships"
  2. component-map-builder    -> "tactical design: deployment topology"
  3. openapi-spec-builder     -> "API contracts for OHS boundaries"
  4. agent-builder            -> "agents respecting context boundaries"
```
### Crew: "Integration Hardening"
```
  1. context-map-builder      -> "identify ACL and OHS boundaries"
  2. openapi-spec-builder     -> "formalize OHS APIs"
  3. data-contract-builder    -> "producer-consumer SLAs at boundaries"
  4. circuit-breaker-builder  -> "fault isolation per integration"
```
## Handoff Protocol
### I Receive
| Input | Type | Notes |
|-------|------|-------|
| System description | string | What the system does |
| Team structure | table | Teams and their domains |
| Existing services | list | Service names + responsibilities |
| Integration pain points | list | Where coupling causes problems |
### I Produce
| Output | Format | Destination |
|--------|--------|-------------|
| context_map artifact | .md with YAML frontmatter + tables | N0X_{domain}/P08_architecture/ |
| Compilation signal | complete with quality score | .cex/runtime/signals/ |
## Builders I Depend On
| Builder | Why | Dependency Type |
|---------|-----|----------------|
| bounded-context-builder | Individual BC definitions feed into map inventory | optional |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| interface-builder | ACL and OHS boundaries become formal interface definitions |
| workflow-builder | Cross-context workflows reference the context map |
| openapi-spec-builder | OHS boundaries become formalized API contracts |
| decision-record-builder | Integration pattern decisions documented as ADRs |
## Quality Checklist Before Signal
| Check | Pass Condition |
|-------|---------------|
| id pattern | ^p08_cm_[a-z][a-z0-9_]+$ |
| relationships | all have upstream/downstream/pattern |
| patterns | valid DDD names (ACL/OHS/Conformist/Partnership) |
| contexts_count | matches body BC count |
| team_coupling | declared for all relationships |
| ACL | translation_layer identified |
| OHS | protocol/API reference declared |
