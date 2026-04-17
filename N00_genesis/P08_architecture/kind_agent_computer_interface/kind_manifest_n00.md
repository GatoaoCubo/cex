---
id: n00_agent_computer_interface_manifest
kind: knowledge_card
pillar: P08
nucleus: n00
title: "Agent Computer Interface -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, agent_computer_interface, p08, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P08 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An agent_computer_interface (ACI) defines the protocol by which an agent interacts with GUI applications and terminal environments. It specifies the interaction primitives (click, type, scroll, screenshot), the coordinate system, error recovery strategies, and rate-limit guards that allow an agent to operate desktop software safely and repeatably.

## Pillar
P08 -- architecture

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `agent_computer_interface` |
| pillar | string | yes | Always `P08` |
| title | string | yes | Human-readable interface name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| interface_type | enum | yes | gui \| terminal \| browser \| hybrid |
| primitives | list | yes | Allowed actions: click, type, scroll, screenshot, key |
| coordinate_system | enum | yes | absolute \| relative \| semantic |
| screenshot_interval_ms | integer | no | How often to capture screen state |
| max_retries | integer | no | Retries per action before abort |
| error_recovery | enum | no | retry \| abort \| fallback |

## When to use
- Defining how an agent should control a desktop application (e.g. browser automation)
- Specifying terminal interaction for agents running CLI workflows
- Establishing safety guards for computer-use agents (rate limits, retry policies)

## Builder
`archetypes/builders/agent_computer_interface-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind agent_computer_interface --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: aci_browser_n05
kind: agent_computer_interface
pillar: P08
nucleus: n05
title: "Browser ACI for N05 Operations"
version: 1.0
quality: null
---
interface_type: browser
primitives: [click, type, scroll, screenshot]
coordinate_system: semantic
max_retries: 3
error_recovery: retry
```

## Related kinds
- `browser_tool` (P04) -- the tool that executes ACI primitives
- `agent_card` (P08) -- declares this ACI as a capability of the agent
- `runtime_rule` (P09) -- governs timeouts and retry policies at runtime
