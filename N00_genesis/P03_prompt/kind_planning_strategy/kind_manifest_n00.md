---
id: n00_planning_strategy_manifest
kind: knowledge_card
pillar: P03
nucleus: n00
title: "Planning Strategy -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, planning_strategy, p03, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P03 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A planning_strategy defines an agent's planning approach: how it decomposes goals into subtasks, selects execution order, allocates tools, and adapts when steps fail. It codifies the reasoning methodology (ReAct, tree-of-thought, plan-and-execute) and the decision criteria for branching. The output is a reusable planning protocol that makes agent behavior predictable and auditable.

## Pillar
P03 -- prompt

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `planning_strategy` |
| pillar | string | yes | Always `P03` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| methodology | string | yes | ReAct, ToT, plan-execute, reflexion, or custom |
| decomposition_rules | list | yes | How to break goals into atomic subtasks |
| replanning_trigger | string | yes | Condition under which the agent replans |
| max_depth | integer | no | Maximum subtask nesting depth |

## When to use
- When an agent needs a defined planning protocol rather than ad-hoc reasoning
- When the task complexity requires tree-of-thought or multi-step plan-before-execute patterns
- When building N07 orchestration logic that dispatches waves based on dependency analysis

## Builder
`archetypes/builders/planning_strategy-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind planning_strategy --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: ps_n07_mission_planner
kind: planning_strategy
pillar: P03
nucleus: n07
title: "N07 Mission Planning Strategy"
version: 1.0
quality: null
---
methodology: plan-execute
decomposition_rules:
  - "Identify artifact kinds required"
  - "Map kinds to nuclei by routing table"
  - "Resolve dependencies into waves"
replanning_trigger: "signal_timeout > 45min OR quality_gate_fail"
max_depth: 3
```

## Related kinds
- `reasoning_strategy` (P03) -- reasoning technique applied within each planning step
- `workflow` (P12) -- the execution container that planning_strategy populates
- `dispatch_rule` (P12) -- rules that translate the plan into actual dispatch calls
- `decision_record` (P08) -- records why a specific planning approach was chosen
