---
id: bld_knowledge_card_context_map
kind: knowledge_card
pillar: P01
nucleus: n00
domain: kind-taxonomy
quality: 8.8
title: "Context Map Builder -- Knowledge Card"
llm_function: INJECT
tags: [context_map, ddd, bounded-context, P08, strategic-design]
tldr: "context_map: DDD BC relationship diagram with upstream/downstream, ACL, OHS, and conformist patterns. NOT bounded_context nor component_map."
created: "2026-04-17"
updated: "2026-04-17"
version: "1.0.0"
author: n03_builder
density_score: 0.90
related:
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_quickstart_guide
  - bld_schema_pitch_deck
  - bld_schema_bugloop
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - bld_schema_context_window_config
  - bld_schema_sandbox_config
  - bld_schema_action_paradigm
---

# Knowledge Card: context_map

## Definition

A `context_map` is a Domain-Driven Design (DDD) artifact that documents the relationships and
integration patterns between bounded contexts (BCs) in a system. It captures upstream/downstream
coupling, translation mechanisms (ACL, OHS), team coordination patterns, and the strategic design
intent connecting different domain models. Introduced by Eric Evans in "Domain-Driven Design" (2003)
as a mandatory strategic design exercise for complex multi-team systems.

## Origin

- **Eric Evans** -- "Domain-Driven Design: Tackling Complexity in the Heart of Software" (2003)
- **Vaughn Vernon** -- "Implementing Domain-Driven Design" (2013): expanded pattern catalog
- **Alberto Brandolini** -- EventStorming (2014): complements context mapping with event flow
- **CEX pillar**: P08 (Architecture) -- strategic design documentation

## DDD Integration Patterns

| Pattern | Symbol | Meaning | Team Coupling |
|---------|--------|---------|---------------|
| Anti-Corruption Layer | ACL | Downstream protects itself from upstream model | Low |
| Open Host Service | OHS | Upstream exposes formal protocol/API | Low |
| Conformist | CF | Downstream adopts upstream model as-is | High |
| Partnership | P | Two teams co-evolve their models together | Very High |
| Shared Kernel | SK | Two contexts share a subset of the domain model | Very High |
| Customer/Supplier | C/S | Downstream negotiates requirements with upstream | Medium |
| Published Language | PL | Formal, documented shared language | Low |

## Key Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | YES | p08_cm_{system_slug} |
| system_name | string | YES | Name of system being mapped |
| contexts_count | integer | YES | Number of BCs |
| contexts | list | YES | BC names and owners |
| relationships | list | YES | Directed pairs with patterns |
| pattern | enum | YES | ACL/OHS/Conformist/Partnership/Shared_Kernel |
| integration_type | enum | REC | sync/async/batch |

## When to Use

| Scenario | Use context_map? |
|----------|-----------------|
| Multiple teams with separate domain models | YES |
| Service integration architecture review | YES |
| Identifying anti-corruption needs between legacy and new | YES |
| Onboarding new developers to system relationships | YES |
| Single bounded context documentation | NO -- use bounded_context |
| Service deployment/infrastructure diagram | NO -- use component_map |
| Code-level class/module dependencies | NO -- use diagram |

## Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| All relationships labeled "integration" | Pattern-less -- no coupling insight | Use ACL/OHS/Conformist etc. |
| Conformist everywhere | Upstream model lock-in -- painful coupling | Introduce ACL where models diverge |
| Missing integration_type | Async vs sync matters for fault tolerance | Always declare sync/async/batch |
| Conflating with component_map | Mixes strategic (DDD) with tactical (deployment) | Separate artifacts for each concern |

## Decision Tree

```
Documenting relationships between two BCs?
  YES: context_map
    Is downstream adopting upstream model directly?
      YES -> Conformist (HIGH coupling warning)
      NO:
        Does upstream expose formal API/protocol?
          YES -> OHS (or OHS+Published Language)
          NO:
            Is downstream building translation layer?
              YES -> ACL (recommended for legacy integration)
              NO -> Partnership (requires team alignment)
```

## Cross-Framework Map

| Framework/Method | Equivalent | Notes |
|-----------------|-----------|-------|
| Evans DDD (2003) | context_map | Origin -- the canonical reference |
| Team Topologies | Stream-aligned + platform team map | Organizational lens on same relationships |
| C4 Model (Context diagram) | context_map | C4 L1 = context map at system level |
| Microservices Architecture | Service dependency map | Technical implementation of DDD context map |
| Event-driven architecture | Event flow map | Complements context map with event routing |

## Integration Graph

```
context_map (P08)
  |
  |-- documents --> bounded_context (P08) -- each node in the map
  |-- influences --> agent (P02) -- agents respect context boundaries
  |-- informs --> interface (P08) -- ACL/OHS become formal interfaces
  |-- guides --> workflow (P12) -- workflows cross context boundaries
  |-- feeds --> decision_record (P08) -- architectural decisions
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_integration_guide]] | downstream | 0.33 |
| [[bld_schema_reranker_config]] | downstream | 0.33 |
| [[bld_schema_quickstart_guide]] | downstream | 0.32 |
| [[bld_schema_pitch_deck]] | downstream | 0.32 |
| [[bld_schema_bugloop]] | downstream | 0.32 |
| [[bld_schema_usage_report]] | downstream | 0.32 |
| [[bld_schema_dataset_card]] | downstream | 0.31 |
| [[bld_schema_context_window_config]] | downstream | 0.31 |
| [[bld_schema_sandbox_config]] | downstream | 0.31 |
| [[bld_schema_action_paradigm]] | downstream | 0.31 |
