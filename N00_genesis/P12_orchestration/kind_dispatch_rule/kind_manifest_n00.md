---
id: n00_dispatch_rule_manifest
kind: knowledge_card
pillar: P12
nucleus: n00
title: "Dispatch Rule -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, dispatch_rule, p12, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P12 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A dispatch_rule maps keywords, intent signals, or artifact kinds to agent groups, specifying the routing logic that determines which nucleus receives a task when N07 receives an ambiguous or multi-domain request. It is the declarative routing table that operationalizes the N07 input transmutation protocol without requiring LLM inference for every routing decision.

## Pillar
P12 -- orchestration

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `dispatch_rule` |
| pillar | string | yes | Always `P12` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| rule_type | enum | yes | keyword \| kind \| pillar \| intent_score \| composite |
| conditions | array | yes | Match conditions (keywords, kind patterns, pillar codes) |
| target_nucleus | string | yes | Nucleus to dispatch to when conditions match |
| priority | integer | yes | Rule priority (lower = higher priority, checked first) |
| fallback_nucleus | string | no | Nucleus to dispatch to if target is unavailable |
| dispatch_mode | enum | yes | solo \| grid \| crew |

## When to use
- When configuring the CEX intent router for a new domain or kind
- When adding a new nucleus and defining what tasks it should receive
- When optimizing routing by replacing LLM-based routing with rule-based routing

## Builder
`archetypes/builders/dispatch_rule-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind dispatch_rule --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: dr_build_create_to_n03
kind: dispatch_rule
pillar: P12
nucleus: n07
title: "Example Dispatch Rule"
version: 1.0
quality: null
---
# Dispatch Rule: Build/Create -> N03
rule_type: keyword
conditions: [build, create, scaffold, generate, make]
target_nucleus: n03
priority: 1
dispatch_mode: solo
fallback_nucleus: n04
```

## Related kinds
- `spawn_config` (P12) -- spawn configuration referenced by dispatch rules
- `workflow` (P12) -- workflow that may override dispatch rules for specific tasks
- `collaboration_pattern` (P12) -- pattern that shapes how the dispatched nucleus works
