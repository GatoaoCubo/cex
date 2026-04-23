---
quality: 8.0
quality: 7.6
id: n00_personality_manifest
kind: knowledge_card
pillar: P02
nucleus: n00
title: "Personality -- Canonical Manifest"
version: 1.0.0
tags: [manifest, personality, p02, n00, archetype, template, hermes_origin, hot_swap, soul_md]
density_score: 0.92
related:
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - bld_schema_benchmark_suite
  - bld_schema_voice_pipeline
  - bld_schema_agent_profile
  - bld_schema_integration_guide
  - bld_schema_tts_provider
  - bld_schema_quickstart_guide
  - bld_schema_eval_metric
updated: "2026-04-22"
---

<!-- 8F: F1=knowledge_card P02 F2=personality-builder F3=kc_hermes+spec_hermes F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A personality stores a hot-swappable voice/tone/values overlay that can be applied to
any agent at runtime via the `/personality [name]` activation command. It implements
the HERMES SOUL.md pattern (NousResearch/hermes-agent): a lightweight persona spec
that injects register, verbosity, humor, core values, tone examples, and anti-patterns
without altering agent capabilities, memory, or routing.

## Pillar
P02 -- model

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique persona identifier (`per_{{name}}`) |
| kind | string | yes | Always `personality` |
| pillar | string | yes | Always `P02` |
| title | string | yes | Human-readable persona label |
| name | string | yes | Persona slug (snake_case or hyphen, <= 30 chars) |
| voice.register | enum | yes | formal, casual, technical, playful |
| voice.verbosity | enum | yes | terse, balanced, verbose |
| voice.humor | enum | yes | off, dry, warm |
| values | list[string] | yes | 3-5 core values driving persona behavior |
| tone_examples | list[string] | yes | >= 3 verbatim sample phrases |
| anti_patterns | list[string] | yes | >= 3 phrases this persona NEVER says |
| activation_cue | string | yes | Hot-swap trigger (default: `/personality {{name}}`) |
| deactivation_cue | string | yes | Return to default (default: `/personality default`) |
| hot_swap_compatible | bool | yes | Can swap at runtime without agent reload |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | null until peer-reviewed |

## When to use
- When an agent must adapt voice for different audiences (technical vs. casual)
- When building multi-persona systems (researcher mode, coach mode, hacker mode)
- When implementing the HERMES SOUL.md-style persona override
- When separating "who the agent is" (agent kind) from "how it speaks right now"

## Builder
`archetypes/builders/personality-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind personality --execute`

## Template variables (open for instantiation)
- `{{name}}` -- persona slug identifier
- `{{register}}` -- formal | casual | technical | playful
- `{{verbosity}}` -- terse | balanced | verbose
- `{{humor}}` -- off | dry | warm
- `{{NUCLEUS_ROLE}}` -- which nucleus activates this persona most often

## Example (minimal)
```yaml
---
id: per_researcher
kind: personality
pillar: P02
title: "Personality: researcher"
name: researcher
voice:
  register: technical
  verbosity: verbose
  humor: dry
values:
  - epistemic rigor
  - source transparency
  - precision over brevity
tone_examples:
  - "Based on the evidence available (confidence: 0.72), the most defensible interpretation is..."
  - "I should flag a limitation: the sample size may not support generalization."
  - "Let me distinguish between what the data shows versus what I am inferring."
anti_patterns:
  - "Everyone knows that..."
  - "Obviously..."
  - "I'm pretty sure..."
activation_cue: "/personality researcher"
deactivation_cue: "/personality default"
hot_swap_compatible: true
version: 1.0.0
quality: null
tags: [personality, hermes_origin, hot_swap, researcher]
---
```

## Related kinds
- `agent` (P02) -- full agent spec with capabilities; personality is the voice layer only
- `agent_profile` (P08) -- runtime AI configuration; personality is persona-of-the-moment
- `system_prompt` (P03) -- full prompt context; personality is one injected voice layer
- `lens` (P02) -- domain perspective with routing rules; personality is communication style
- `user_model` (P10) -- tracks user's preferred personality over time

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | downstream | 0.42 |
| [[bld_schema_usage_report]] | downstream | 0.42 |
| [[bld_schema_dataset_card]] | downstream | 0.41 |
| [[bld_schema_benchmark_suite]] | downstream | 0.40 |
| [[bld_schema_voice_pipeline]] | downstream | 0.40 |
| [[bld_schema_agent_profile]] | downstream | 0.40 |
| [[bld_schema_integration_guide]] | downstream | 0.40 |
| [[bld_schema_tts_provider]] | downstream | 0.40 |
| [[bld_schema_quickstart_guide]] | downstream | 0.40 |
| [[bld_schema_eval_metric]] | downstream | 0.40 |
