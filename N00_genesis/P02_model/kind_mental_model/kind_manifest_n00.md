---
id: n00_mental_model_manifest
kind: knowledge_card
pillar: P02
nucleus: n00
title: "Mental Model -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, mental_model, p02, n00, archetype, template]
density_score: 1.0
updated: "2026-04-17"
---

<!-- 8F: F1=knowledge_card P02 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Mental Model defines an agent's internal framework for routing decisions, resolving ambiguity, and reasoning under uncertainty. It is the "how I think" complement to agent_profile's "who I am" and agent's "what I can do". Mental models encode decision trees, priority hierarchies, and heuristics that an agent applies before taking action.

## Pillar
P02 -- Model

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `mental_model` |
| pillar | string | yes | Always `P02` |
| title | string | yes | Model name and agent |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| nucleus | string | yes | Owning nucleus |
| decision_framework | enum | yes | if-then\|priority-queue\|cost-benefit\|axiom-first |
| routing_rules | list | yes | Ordered routing conditions and actions |
| ambiguity_resolution | string | yes | Strategy when input is unclear |
| escalation_trigger | string | yes | Condition that routes to user or N07 |

## When to use
- When encoding the routing and decision logic for a nucleus
- When creating structured reasoning frameworks for autonomous agents
- When formalizing how an agent handles edge cases

## Builder
`archetypes/builders/mental_model-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind mental_model --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA shaping the decision framework
- `{{TARGET_AUDIENCE}}` -- the agent and N07 orchestrator
- `{{DOMAIN_CONTEXT}}` -- operational domain for routing decisions

## Example (minimal)
```yaml
---
id: mental_model_n07_dispatch_routing
kind: mental_model
pillar: P02
nucleus: n07
title: "N07 Dispatch Routing Model"
version: 1.0
quality: null
---
nucleus: n07
decision_framework: priority-queue
routing_rules:
  - if: "task involves building artifact" -> dispatch: n03
  - if: "task involves research" -> dispatch: n01
  - if: "task involves code/deploy" -> dispatch: n05
ambiguity_resolution: "Present top-2 options via GDP, user chooses"
escalation_trigger: "Quality gate < 7.0 after 2 retries"
```

## Related kinds
- `agent_profile` (P02) -- persona this mental model belongs to
- `axiom` (P02) -- non-negotiable principles the model enforces
- `router` (P02) -- runtime routing artifact built from this model
