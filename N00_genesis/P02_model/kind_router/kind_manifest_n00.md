---
id: n00_router_manifest
kind: knowledge_card
pillar: P02
nucleus: n00
title: "Router -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, router, p02, n00, archetype, template]
density_score: 1.0
updated: "2026-04-17"
---

<!-- 8F: F1=knowledge_card P02 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Router defines a task-to-agent-group routing rule that maps incoming task signatures to the appropriate nucleus or agent group. It encodes the REASON function (F4) of the 8F pipeline: given a classified intent, which agent(s) should handle it? Routers can be static (rule-based), dynamic (ML-scored), or hierarchical (multi-level delegation).

## Pillar
P02 -- Model

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `router` |
| pillar | string | yes | Always `P02` |
| title | string | yes | Router name and scope |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| routing_type | enum | yes | rule-based\|ml-scored\|hybrid\|hierarchical |
| scope | enum | yes | nucleus\|agent\|crew -- granularity of routing |
| rules | list | yes | Ordered routing rules (condition -> target) |
| fallback_target | string | yes | Default target if no rule matches |
| confidence_threshold | float | no | Minimum score for ML routing (0-1) |

## When to use
- When configuring how N07 dispatches tasks to nuclei
- When building a multi-provider routing layer (cex_router.py)
- When defining domain-specific routing for a crew orchestrator

## Builder
`archetypes/builders/router-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind router --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N07)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- N07 and dispatch infrastructure
- `{{DOMAIN_CONTEXT}}` -- routing scope and task taxonomy

## Example (minimal)
```yaml
---
id: router_n07_nucleus_dispatch
kind: router
pillar: P02
nucleus: n07
title: "N07 Nucleus Dispatch Router"
version: 1.0
quality: null
---
routing_type: rule-based
scope: nucleus
rules:
  - condition: "kind in [agent, software_project, landing_page]"
    target: n03
  - condition: "kind in [knowledge_card, context_doc]"
    target: n04
  - condition: "kind in [mcp_server, env_config, webhook]"
    target: n05
fallback_target: n03
```

## Related kinds
- `mental_model` (P02) -- reasoning framework the router implements
- `fallback_chain` (P02) -- provider fallback used within routing
- `nucleus_def` (P02) -- target nucleus definitions in routing rules
