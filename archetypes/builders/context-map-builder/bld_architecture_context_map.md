---
kind: architecture
id: bld_architecture_context_map
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of context_map -- inventory, dependencies, and architectural position
quality: null
title: "Architecture Context Map"
version: "1.0.0"
author: n03_builder
tags: [context_map, builder, architecture]
tldr: "Component map: contexts list, relationships (U/D, ACL, OHS), integration_type, team_coupling. External: bounded_context, component_map."
domain: "context map construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| contexts | List of bounded contexts in scope | context_map | required |
| relationships | Directed relationships between context pairs | context_map | required |
| relationship.upstream | Context that defines the model/protocol | relationship | required |
| relationship.downstream | Context that consumes/adapts the model | relationship | required |
| relationship.pattern | Integration pattern (ACL/OHS/Conformist/Partnership/Shared_Kernel) | relationship | required |
| relationship.integration_type | sync/async/batch | relationship | recommended |
| relationship.translation_layer | ACL description if pattern is ACL | relationship | conditional |
| team_coupling | Team ownership implications per relationship | context_map | recommended |
| bounded_context | Single BC definition (separate kind, referenced here) | P08 (separate kind) | external |
| component_map | Deployment topology (separate concern) | P08 (separate kind) | external |

## DDD Integration Pattern Reference

| Pattern | Abbrev | Upstream Role | Downstream Role | Team Coupling |
|---------|--------|---------------|-----------------|---------------|
| Anti-Corruption Layer | ACL | Publishes own model | Translates to local model | Low -- protected |
| Open Host Service | OHS | Publishes protocol/API | Uses standard protocol | Low -- formalized |
| Conformist | CF | Publishes own model | Adopts upstream model | HIGH -- dependent |
| Partnership | P | Co-evolves model | Co-evolves model | HIGH -- synchronized |
| Shared Kernel | SK | Shares code/model | Shares code/model | VERY HIGH -- merged |
| Customer/Supplier | C/S | Negotiates with U | Requests features from U | Medium -- negotiated |
| Published Language | PL | Publishes formal language | Consumes formal language | Low -- documented |

## Relationship Diagram Structure

```
Context A (U) --------[pattern]---------  Context B (D)
                                           |
                          if ACL: [Translation Layer]
                          if OHS: [Published Language/API]
                          if CF:  [Direct model adoption]
```

## Boundary Table

| context_map IS | context_map IS NOT |
|----------------|--------------------|
| BC relationship diagram with integration patterns | Single BC definition (that is bounded_context) |
| Upstream/downstream coupling documentation | Service deployment topology (that is component_map) |
| Team coupling and API translation map | Code architecture (that is diagram) |
| Strategic design artifact | Infrastructure diagram (that is component_map) |

## Layer Map

| Layer | Components | Purpose |
|-------|-----------|---------|
| inventory | contexts | List all BCs in scope |
| relationships | upstream, downstream, pattern | Document directed coupling |
| translation | translation_layer, integration_type | Describe how models cross boundaries |
| team | team_coupling | Organizational implications |
