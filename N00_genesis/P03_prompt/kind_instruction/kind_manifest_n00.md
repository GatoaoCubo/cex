---
id: n00_instruction_manifest
kind: knowledge_card
pillar: P03
nucleus: n00
title: "Instruction -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, instruction, p03, n00, archetype, template]
density_score: 0.98
related:
  - instruction-builder
  - bld_schema_kind
  - p01_kc_instruction
  - bld_collaboration_instruction
  - bld_architecture_instruction
  - p03_sp_instruction_builder
  - bld_architecture_kind
  - tpl_instruction
  - bld_schema_action_prompt
  - bld_schema_instruction
---

<!-- 8F: F1=knowledge_card P03 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An instruction is a step-by-step execution directive for agents or pipelines, specifying the exact sequence of operations, conditions, and outputs expected at each step. Unlike a system_prompt that defines identity, an instruction defines procedure: what to do, in what order, and how to handle edge cases. The output is a deterministic execution protocol that reduces agent hallucination and drift.

## Pillar
P03 -- prompt

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `instruction` |
| pillar | string | yes | Always `P03` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| steps | list | yes | Ordered list of discrete steps with expected outputs |
| preconditions | list | no | Conditions that must be true before execution begins |
| error_handling | map | no | Error type -> recovery action mapping |
| idempotent | boolean | no | Whether re-running produces same result safely |

## When to use
- When an agent needs a deterministic, repeatable procedure with no ambiguity
- When onboarding new nuclei that must follow a specific execution protocol
- When building builder ISOs (instruction is one of the 13 ISO types in every builder)

## Builder
`archetypes/builders/instruction-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind instruction --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: instr_build_knowledge_card
kind: instruction
pillar: P03
nucleus: n04
title: "Build Knowledge Card Instruction"
version: 1.0
quality: null
---
preconditions:
  - kind resolved via kinds_meta.json
  - KC template loaded from P01
steps:
  - step: 1
    action: "Read builder ISOs from archetypes/builders/knowledge_card-builder/"
    output: builder_loaded
  - step: 2
    action: "Inject kc_{kind}.md from P01_knowledge/library/kind/"
    output: context_assembled
```

## Related kinds
- `action_prompt` (P03) -- the trigger that activates an instruction sequence
- `system_prompt` (P03) -- identity definition that precedes instruction execution
- `planning_strategy` (P03) -- determines which instruction branch to follow
- `workflow` (P12) -- orchestrates multiple instructions across nuclei

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[instruction-builder]] | related | 0.41 |
| [[bld_schema_kind]] | downstream | 0.41 |
| [[p01_kc_instruction]] | sibling | 0.38 |
| [[bld_collaboration_instruction]] | downstream | 0.37 |
| [[bld_architecture_instruction]] | downstream | 0.37 |
| [[p03_sp_instruction_builder]] | related | 0.37 |
| [[bld_architecture_kind]] | downstream | 0.36 |
| [[tpl_instruction]] | related | 0.36 |
| [[bld_schema_action_prompt]] | downstream | 0.35 |
| [[bld_schema_instruction]] | downstream | 0.34 |
