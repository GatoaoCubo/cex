---
id: n00_env_config_manifest
kind: knowledge_card
pillar: P09
nucleus: n00
title: "Env Config -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, env_config, p09, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An env_config documents and governs environment variables required by a nucleus or tool: their names, expected values, default values, and which are required vs. optional. It serves as the single source of truth for environment setup, enabling cex_setup_validator.py to check readiness and boot scripts to validate prerequisites before launching.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `env_config` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable config name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| scope | string | yes | Which nucleus or system this covers |
| variables | list | yes | List of environment variable definitions |
| variables[].name | string | yes | Variable name (SCREAMING_SNAKE_CASE) |
| variables[].required | boolean | yes | Whether absence should fail boot |
| variables[].default | string | no | Default value if not set |
| variables[].description | string | yes | What this variable configures |
| variables[].secret | boolean | no | If true, never log or display value |

## When to use
- Defining required environment for a new nucleus boot script
- Documenting which API keys and paths must be set before cex_setup_validator runs
- Capturing per-environment overrides (dev vs. prod vs. CI)

## Builder
`archetypes/builders/env_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind env_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: env_config_n05
kind: env_config
pillar: P09
nucleus: n05
title: "N05 Operations Environment Config"
version: 1.0
quality: null
---
scope: n05
variables:
  - name: ANTHROPIC_API_KEY
    required: true
    description: Anthropic API key for Claude calls
    secret: true
  - name: CEX_NUCLEUS
    required: true
    default: n05
    description: Active nucleus identifier
```

## Related kinds
- `secret_config` (P09) -- secrets referenced in env_config as variable values
- `path_config` (P09) -- file system paths often set via environment variables
- `feature_flag` (P09) -- feature flags sometimes use env vars as backend
