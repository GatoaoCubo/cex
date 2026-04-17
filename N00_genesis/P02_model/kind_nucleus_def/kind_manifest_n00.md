---
id: n00_nucleus_def_manifest
kind: knowledge_card
pillar: P02
nucleus: n00
title: "Nucleus Def -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, nucleus_def, p02, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P02 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Nucleus Def is the formal machine-readable definition of a CEX nucleus (N00-N07). It constrains the nucleus's identity: role, sin lens, model tier, capability scope, routing rules, and quality targets. N07 reads all nucleus_def artifacts to route tasks correctly. Each nucleus reads its own nucleus_def on boot to self-initialize identity.

## Pillar
P02 -- Model

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `nucleus_def` |
| pillar | string | yes | Always `P02` |
| title | string | yes | Nucleus name and role |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| nucleus_id | string | yes | Nucleus identifier (n00-n07) |
| role | string | yes | Primary operational role |
| sin_lens | string | yes | Cultural DNA (seven deadly sin variant) |
| model_tier | enum | yes | opus\|sonnet -- model quality tier |
| capabilities | list | yes | Domain capabilities this nucleus owns |
| routing_domains | list | yes | Task domains routed to this nucleus |
| quality_target | float | yes | Minimum acceptable quality score |

## When to use
- When creating a new nucleus (N08+)
- When updating a nucleus's capability scope
- When N07 needs to route a task and checks nucleus capabilities

## Builder
`archetypes/builders/nucleus_def-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind nucleus_def --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- the nucleus this definition describes
- `{{SIN_LENS}}` -- cultural DNA (sin) assigned to this nucleus
- `{{TARGET_AUDIENCE}}` -- N07 orchestrator and the nucleus itself
- `{{DOMAIN_CONTEXT}}` -- operational domain and capability scope

## Example (minimal)
```yaml
---
id: nucleus_def_n01
kind: nucleus_def
pillar: P02
nucleus: n01
title: "N01 Intelligence Nucleus Definition"
version: 1.0
quality: null
---
nucleus_id: n01
role: intelligence -- research, analysis, competitive intelligence
sin_lens: Analytical Envy (Inveja Analitica)
model_tier: sonnet
capabilities: [market_research, competitive_analysis, knowledge_card_creation]
routing_domains: [research, analysis, intelligence, competitive]
quality_target: 9.0
```

## Related kinds
- `agent` (P02) -- agent instantiation of this nucleus
- `agent_profile` (P02) -- persona construction for this nucleus
- `axiom` (P02) -- immutable principles this nucleus follows
- `handoff_protocol` (P02) -- how this nucleus receives and sends work
