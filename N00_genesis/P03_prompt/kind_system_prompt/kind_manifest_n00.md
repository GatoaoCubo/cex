---
id: n00_system_prompt_manifest
kind: knowledge_card
pillar: P03
nucleus: n00
title: "System Prompt -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, system_prompt, p03, n00, archetype, template]
density_score: 0.96
---

<!-- 8F: F1=knowledge_card P03 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A system_prompt defines an agent's identity, operational rules, sin lens, and behavioral constraints at the start of every session. It is the F2 BECOME artifact: the builder reads it to transform itself from a generic LLM into a specialized nucleus with a specific role, domain authority, and cultural DNA. The output is a complete identity definition that persists through all turns of the conversation without repetition.

## Pillar
P03 -- prompt

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `system_prompt` |
| pillar | string | yes | Always `P03` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| nucleus_id | string | yes | Which nucleus this identity belongs to (n01-n07) |
| sin_lens | string | yes | Cultural DNA: the sin that drives this nucleus |
| role_definition | string | yes | What this nucleus is and what it does |
| behavioral_rules | list | yes | Hard rules that govern nucleus behavior |

## When to use
- When bootstrapping a new nucleus that needs a defined identity before any task runs
- When the F2 BECOME step loads the builder's self-definition
- When creating the 13 ISOs for a new builder kind that includes a system_prompt ISO

## Builder
`archetypes/builders/system_prompt-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind system_prompt --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: sp_n03_engineering_identity
kind: system_prompt
pillar: P03
nucleus: n03
title: "N03 Engineering Nucleus Identity"
version: 1.0
quality: null
---
nucleus_id: n03
sin_lens: "Inventive Pride (Soberba Inventiva)"
role_definition: "N03 is the builder nucleus. It creates, architects, and scaffolds all technical artifacts."
behavioral_rules:
  - "Always run 8F pipeline. No shortcuts."
  - "Never publish quality below 8.0."
  - "Compile every artifact after writing."
```

## Related kinds
- `agent` (P02) -- the agent definition that embeds this system_prompt
- `nucleus_def` (P08) -- machine-readable nucleus identity that system_prompt narrates
- `instruction` (P03) -- procedural layer that executes after system_prompt establishes identity
- `prompt_version` (P03) -- version snapshots of system_prompt evolution over time
