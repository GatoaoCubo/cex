---
id: n00_role_assignment_manifest
kind: knowledge_card
pillar: P02
nucleus: n00
title: "Role Assignment -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, role_assignment, p02, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P02 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Role Assignment is a CrewAI Agent-style binding that connects a crew role name to a specific agent identifier with a defined goal, backstory, and tool set. It constrains which agent plays which role in a crew template, enabling reusable crew topologies where roles can be rebound to different agents without changing the crew structure.

## Pillar
P02 -- Model

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `role_assignment` |
| pillar | string | yes | Always `P02` |
| title | string | yes | Role name and bound agent |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| role_name | string | yes | Role label in the crew template |
| agent_ref | string | yes | Reference to agent artifact |
| goal | string | yes | Role-specific goal for this crew instance |
| backstory | string | yes | Role-specific context injected into agent |
| tools | list | yes | Tools available in this role |
| allow_delegation | bool | yes | Whether this role can delegate to sub-agents |

## When to use
- When composing a crew from existing agents
- When assigning specific roles in a sequential or hierarchical crew
- When binding a generic agent to a mission-specific role

## Builder
`archetypes/builders/role_assignment-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind role_assignment --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA of the assigned agent
- `{{TARGET_AUDIENCE}}` -- crew orchestrator (N07)
- `{{DOMAIN_CONTEXT}}` -- mission and crew topology

## Example (minimal)
```yaml
---
id: role_assignment_researcher_n01_product_launch
kind: role_assignment
pillar: P02
nucleus: n07
title: "Researcher Role -- Product Launch Crew"
version: 1.0
quality: null
---
role_name: researcher
agent_ref: agent_n01_research_analyst
goal: "Produce competitive landscape KC for product launch positioning"
backstory: "Deep researcher with obsessive attention to market signals"
tools: [cex_retriever, web_search, cex_query]
allow_delegation: false
```

## Related kinds
- `agent` (P02) -- agent being assigned to the role
- `nucleus_def` (P02) -- nucleus the agent belongs to
- `handoff_protocol` (P02) -- how this role hands off to the next
