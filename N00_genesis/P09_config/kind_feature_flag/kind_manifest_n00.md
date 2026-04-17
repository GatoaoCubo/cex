---
id: n00_feature_flag_manifest
kind: knowledge_card
pillar: P09
nucleus: n00
title: "Feature Flag -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, feature_flag, p09, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A feature_flag is a runtime on/off switch or gradual rollout control that enables capabilities to be enabled, disabled, or progressively released without code changes. It allows new builder features, model upgrades, and experimental capabilities to be deployed safely with instant rollback capability.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `feature_flag` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable flag name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| flag_key | string | yes | Programmatic key used in code checks |
| enabled | boolean | yes | Default state (true=on, false=off) |
| rollout_pct | integer | no | Gradual rollout percentage (0-100, null=all-or-nothing) |
| target_segments | list | no | User/nucleus segments this flag applies to |
| description | string | yes | What capability this flag controls |
| expires_at | date | no | When this temporary flag should be removed |

## When to use
- Rolling out a new 8F pipeline step to a subset of nuclei before full deployment
- Disabling a feature for specific customer segments pending compliance review
- Enabling experimental model routing without affecting production traffic

## Builder
`archetypes/builders/feature_flag-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind feature_flag --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: ff_extended_thinking_n01
kind: feature_flag
pillar: P09
nucleus: n05
title: "Extended Thinking for N01"
version: 1.0
quality: null
---
flag_key: extended_thinking_n01
enabled: false
rollout_pct: 10
target_segments: [n01]
description: Enables extended thinking tokens for N01 intelligence builds
expires_at: 2026-06-01
```

## Related kinds
- `experiment_config` (P09) -- flags often gate experiment variants
- `thinking_config` (P09) -- feature flags can toggle extended thinking
- `runtime_rule` (P09) -- runtime rules that activate based on flag state
