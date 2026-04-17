---
id: n00_skill_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "Skill -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, skill, p04, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A skill is a reusable capability unit with a defined trigger condition and execution phases that an agent activates when specific conditions are met. In CEX, skills are auto-firing lazy capabilities (cross_wave_cleanup, shared_file_proposal, auto_accept_handoff) that load only when their trigger is detected. The output is a skill definition that the Skill tool loads and executes, extending agent behavior without modifying the core system prompt.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `skill` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| trigger | string | yes | Condition that activates the skill (slash command, pattern match) |
| phases | list | yes | Ordered execution phases with instructions per phase |
| lazy | boolean | yes | Whether skill loads only on trigger (true) or at boot (false) |
| cross_runtime | boolean | no | Whether skill is mirrored to .cex/skills/ for non-Claude runtimes |

## When to use
- When building a reusable agent capability that fires on a specific slash command or condition
- When adding a new lazy skill to the .claude/skills/ directory for auto-fire behavior
- When the user types a slash command that needs a structured multi-phase execution protocol

## Builder
`archetypes/builders/skill-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind skill --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: skill_cross_wave_cleanup
kind: skill
pillar: P04
nucleus: n07
title: "Cross-Wave Cleanup Skill"
version: 1.0
quality: null
---
trigger: "post-wave completion detected"
lazy: true
cross_runtime: true
phases:
  - phase: 1
    name: scan
    instruction: "List all orphan processes and stale task files"
  - phase: 2
    name: clean
    instruction: "Kill orphans with taskkill /T, archive task files"
```

## Related kinds
- `action_paradigm` (P04) -- execution paradigm that skills operate within
- `hook` (P04) -- alternative trigger mechanism for skill-like behaviors
- `plugin` (P04) -- heavier extension that skills replace when lifecycle is simple
- `instruction` (P03) -- step-by-step instructions that skill phases reference
