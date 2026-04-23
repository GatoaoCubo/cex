---
id: n00_effort_profile_manifest
kind: knowledge_card
pillar: P09
nucleus: n00
title: "Effort Profile -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, effort_profile, p09, n00, archetype, template]
density_score: 1.0
related:
  - p03_sp_effort_profile_builder
  - bld_schema_effort_profile
  - bld_schema_thinking_config
  - effort-profile-builder
  - bld_schema_reranker_config
  - bld_schema_kind
  - bld_schema_integration_guide
  - bld_schema_usage_report
  - bld_schema_sandbox_spec
  - bld_schema_benchmark_suite
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An effort_profile configures the thinking level and computational effort for a builder's execution: how deeply to reason, how many tokens to allocate for extended thinking, and whether to use fast/cheap or slow/thorough modes. It enables cost-quality trade-off decisions to be made per-task rather than per-nucleus, allowing the same nucleus to run in both quick-draft and production-quality modes.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `effort_profile` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable profile name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| level | enum | yes | minimal \| standard \| thorough \| exhaustive |
| thinking_tokens | integer | no | Budget tokens for extended thinking (0 = disabled) |
| max_iterations | integer | no | Max 8F retry loops at F7 |
| context_sources | integer | no | Max knowledge sources to inject at F3 |
| draft_mode | boolean | no | Skip F7 governance for speed (default false) |
| target_quality | float | no | Minimum quality score to accept output |

## When to use
- Running quick exploratory drafts where time beats quality
- Configuring exhaustive mode for production artifacts that must score 9.0+
- Setting different effort profiles per wave in a multi-wave mission

## Builder
`archetypes/builders/effort_profile-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind effort_profile --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: effort_profile_production
kind: effort_profile
pillar: P09
nucleus: n03
title: "Production Build Effort Profile"
version: 1.0
quality: null
---
level: thorough
thinking_tokens: 10000
max_iterations: 2
context_sources: 10
draft_mode: false
target_quality: 9.0
```

## Related kinds
- `thinking_config` (P09) -- extended thinking settings that effort_profile references
- `cost_budget` (P09) -- effort levels directly impact token spend
- `quality_gate` (P07) -- target_quality in effort_profile aligns with quality_gate threshold

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_effort_profile_builder]] | related | 0.40 |
| [[bld_schema_effort_profile]] | upstream | 0.40 |
| [[bld_schema_thinking_config]] | upstream | 0.37 |
| [[effort-profile-builder]] | related | 0.36 |
| [[bld_schema_reranker_config]] | upstream | 0.34 |
| [[bld_schema_kind]] | upstream | 0.33 |
| [[bld_schema_integration_guide]] | upstream | 0.33 |
| [[bld_schema_usage_report]] | upstream | 0.32 |
| [[bld_schema_sandbox_spec]] | upstream | 0.32 |
| [[bld_schema_benchmark_suite]] | upstream | 0.32 |
