---
id: n00_prompt_compiler_manifest
kind: knowledge_card
pillar: P03
nucleus: n00
title: "Prompt Compiler -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, prompt_compiler, p03, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P03 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A prompt_compiler is an intent-to-artifact transmutation ruleset that maps natural language user input to the structured CEX taxonomy tuple {kind, pillar, nucleus, verb}. It is the F1 CONSTRAIN layer of the 8F pipeline and the canonical source of truth for intent resolution across all 257 kinds in PT+EN. The output enables any nucleus to deterministically convert vague user input into precise builder dispatch without additional clarification rounds.

## Pillar
P03 -- prompt

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `prompt_compiler` |
| pillar | string | yes | Always `P03` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| pattern_table | list | yes | PT+EN phrase -> {kind, pillar, nucleus, verb} mapping rows |
| confidence_threshold | float | yes | Minimum confidence to auto-resolve (default 0.60) |
| ambiguity_resolution | string | yes | present_top3_gdp or auto_pick_highest |
| verb_map | map | yes | User verb -> canonical action + primary 8F function |

## When to use
- As the F1 CONSTRAIN gate for every 8F pipeline run
- When building new nuclei that need intent routing from user natural language
- When extending the kind registry with new kinds that require resolution rules

## Builder
`archetypes/builders/prompt_compiler-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind prompt_compiler --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: pc_cex_universal_v2
kind: prompt_compiler
pillar: P03
nucleus: n07
title: "CEX Universal Prompt Compiler"
version: 2.0
quality: null
---
confidence_threshold: 0.60
ambiguity_resolution: present_top3_gdp
pattern_table:
  - phrase_pt: "criar agente"
    phrase_en: "create agent"
    kind: agent
    pillar: P02
    nucleus: n03
    verb: create
```

## Related kinds
- `intent_resolution` (P01) -- knowledge layer backing the compiler's pattern table
- `system_prompt` (P03) -- identity definition that activates once intent is resolved
- `prompt_template` (P03) -- template hydrated after compiler resolves kind and pillar
- `reasoning_strategy` (P03) -- strategy applied when confidence falls below threshold
