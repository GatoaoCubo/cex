---
kind: schema
id: bld_schema_personality
pillar: P02
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for personality
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 8.9
title: "Schema: personality"
version: "1.0.0"
author: n03_builder
tags: [personality, builder, schema, hermes_origin, P02, hot_swap]
tldr: "Formal field spec for personality: name, voice (register/verbosity/humor), values, tone_examples, anti_patterns, hot-swap cues."
domain: "persona construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.91
related:
  - bld_schema_reranker_config
  - bld_schema_quickstart_guide
  - bld_schema_usage_report
  - bld_schema_enum_def
  - bld_schema_benchmark_suite
  - bld_schema_integration_guide
  - bld_schema_search_strategy
  - bld_schema_dataset_card
  - bld_schema_tts_provider
  - bld_schema_sandbox_config
---

# Schema: personality

## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (per_{{name}}) | YES | - | Namespace compliance |
| kind | literal "personality" | YES | - | Type integrity |
| pillar | literal "P02" | YES | - | Pillar assignment |
| title | string | YES | - | Human-readable persona label |
| name | string | YES | - | Persona identifier slug (snake_case or hyphen, <= 30 chars) |
| voice.register | enum | YES | - | formal, casual, technical, playful |
| voice.verbosity | enum | YES | "balanced" | terse, balanced, verbose |
| voice.humor | enum | YES | "off" | off, dry, warm |
| values | list[string], 3-5 items | YES | - | Core values driving persona |
| tone_examples | list[string], >= 3 items | YES | - | Verbatim sample phrases |
| anti_patterns | list[string], >= 3 items | YES | - | Phrases persona NEVER says |
| activation_cue | string | YES | "/personality {{name}}" | Hot-swap trigger command |
| deactivation_cue | string | YES | "/personality default" | Return to default persona |
| hot_swap_compatible | bool | YES | true | Can swap at runtime without agent reload |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "personality" and "hermes_origin" |
| tldr | string <= 160ch | YES | - | Dense summary |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| description | string <= 200ch | REC | - | What persona this is |

## ID Pattern
Regex: `^per_[a-z][a-z0-9_-]+$`
Rule: id MUST equal filename stem.

## Voice Register Enum
| Value | Meaning | When to use |
|-------|---------|-------------|
| formal | Precise, structured, no contractions | Professional, academic, legal contexts |
| casual | Friendly, approachable, uses contractions | Daily conversation, support |
| technical | Jargon-rich, assumes domain knowledge | Dev, engineering, science |
| playful | Wit-forward, light, pun-tolerant | Entertainment, creative, social |

## Voice Verbosity Enum
| Value | Meaning |
|-------|---------|
| terse | Short direct answers, no elaboration |
| balanced | Normal length, explains when needed |
| verbose | Thorough explanations, examples included |

## Voice Humor Enum
| Value | Meaning |
|-------|---------|
| off | No humor, strictly informative |
| dry | Subtle irony, understatement |
| warm | Genuine friendliness, light jokes |

## Body Structure (required sections)
1. `## Voice Profile` -- 3-column table: dimension, value, notes
2. `## Values` -- bullet list of 3-5 values with 1-sentence rationale
3. `## Tone Examples` -- numbered list of 3+ verbatim sample phrases with context
4. `## Anti-Patterns` -- numbered list of 3+ forbidden phrases with reason
5. `## Activation` -- activation_cue, deactivation_cue, hot_swap_compatible
6. `## Related Personalities` -- sibling personas and contrast notes (optional but recommended)

## Constraints
- max_bytes: 3072 (voice layer, not a full agent spec)
- naming: `p02_per_{{name}}.md`
- machine_format: yaml (compiled artifact)
- id == filename stem
- values list MUST have 3-5 items
- tone_examples list MUST have >= 3 items
- anti_patterns list MUST have >= 3 items
- hot_swap_compatible: true unless documented reason for false
- quality: null always
- NO tool definitions, capability lists, or memory config in body

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | sibling | 0.62 |
| [[bld_schema_quickstart_guide]] | sibling | 0.60 |
| [[bld_schema_usage_report]] | sibling | 0.60 |
| [[bld_schema_enum_def]] | sibling | 0.59 |
| [[bld_schema_benchmark_suite]] | sibling | 0.58 |
| [[bld_schema_integration_guide]] | sibling | 0.58 |
| [[bld_schema_search_strategy]] | sibling | 0.58 |
| [[bld_schema_dataset_card]] | sibling | 0.58 |
| [[bld_schema_tts_provider]] | sibling | 0.58 |
| [[bld_schema_sandbox_config]] | sibling | 0.57 |
