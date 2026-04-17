---
id: n00_supervisor_manifest
kind: knowledge_card
pillar: P08
nucleus: n00
title: "Supervisor -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, supervisor, p08, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P08 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A supervisor is a crew orchestrator that composes and coordinates multiple builders within a single crew. Unlike N07 which orchestrates across nuclei at the mission level, a supervisor operates within a single crew instance: it sequences roles, passes handoff artifacts between them, enforces the charter quality gate, and escalates failures. It is the inner-crew coordination layer.

## Pillar
P08 -- architecture

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `supervisor` |
| pillar | string | yes | Always `P08` |
| title | string | yes | Human-readable supervisor name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| crew_template_ref | string | yes | Path to the crew_template this supervises |
| process | enum | yes | sequential \| hierarchical \| consensus |
| roles | list | yes | Ordered list of role_assignment references |
| gate | object | yes | Charter-level quality gate |
| gate.min_score | float | yes | Minimum output quality (default 8.0) |
| gate.on_fail | enum | yes | retry \| escalate \| abort |
| handoff_protocol | enum | no | a2a_task \| file \| signal |
| max_delegation_depth | integer | no | Max sub-delegation levels in hierarchical mode |

## When to use
- Instantiating a crew that requires coordinated role sequencing with handoffs
- Enforcing a quality gate on the crew output before signaling N07
- Implementing hierarchical crews where a manager role delegates to worker roles

## Builder
`archetypes/builders/supervisor-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind supervisor --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: supervisor_product_launch
kind: supervisor
pillar: P08
nucleus: n02
title: "Product Launch Crew Supervisor"
version: 1.0
quality: null
---
crew_template_ref: N02_marketing/crews/p12_ct_product_launch.md
process: sequential
roles: [research_role, copy_role, design_role, qa_role]
gate:
  min_score: 8.5
  on_fail: retry
handoff_protocol: a2a_task
```

## Related kinds
- `crew_template` (P12) -- the recipe this supervisor executes
- `role_assignment` (P02) -- role bindings the supervisor coordinates
- `dual_loop_architecture` (P08) -- the supervisor is the inner loop for crew execution
