---
id: n00_procedural_memory_manifest
kind: knowledge_card
pillar: P10
nucleus: n00
title: "Procedural Memory -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, procedural_memory, p10, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P10 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A procedural_memory stores learned skills and step-by-step procedures that an agent can retrieve and execute to accomplish recurring tasks. Unlike entity_memory (facts) or learning_record (outcomes), procedural_memory encodes HOW to do something -- the operational playbook the agent can call at inference time without re-deriving the approach.

## Pillar
P10 -- memory

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `procedural_memory` |
| pillar | string | yes | Always `P10` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| skill_name | string | yes | Short canonical name of the skill |
| trigger_conditions | array | yes | Conditions under which this skill activates |
| steps | array | yes | Ordered list of execution steps |
| tools_required | array | no | Tool names required to execute this skill |
| success_criteria | string | yes | How to know the skill executed successfully |
| rehearsal_count | integer | no | Number of times this skill has been successfully used |

## When to use
- When an agent repeatedly discovers the same multi-step procedure through trial and error
- When encoding expert workflows (e.g. 8F pipeline steps) as retrievable skills
- When building skill libraries for domain-specific agents

## Builder
`archetypes/builders/procedural_memory-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind procedural_memory --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: pm_8f_pipeline_execution
kind: procedural_memory
pillar: P10
nucleus: n00
title: "Example Procedural Memory"
version: 1.0
quality: null
---
# Skill: 8F Pipeline Execution
skill_name: run_8f_pipeline
trigger_conditions: ["any build task", "artifact creation request"]
steps: [F1_constrain, F2_become, F3_inject, F4_reason, F5_call, F6_produce, F7_govern, F8_collaborate]
success_criteria: artifact saved + compiled + committed + signaled
```

## Related kinds
- `learning_record` (P10) -- records that feed into procedural memory refinement
- `workflow` (P12) -- formal workflow that a procedural memory may instantiate
- `self_improvement_loop` (P11) -- loop that evolves procedural memories over time
