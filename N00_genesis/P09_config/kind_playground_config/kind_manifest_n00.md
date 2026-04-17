---
id: n00_playground_config_manifest
kind: knowledge_card
pillar: P09
nucleus: n00
title: "Playground Config -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, playground_config, p09, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A playground_config defines the parameters for an interactive product evaluation environment where prospects or internal users can try CEX capabilities in a sandboxed, cost-controlled setting. It configures session limits, available tools, model access, and UX constraints to provide a safe, repeatable evaluation experience.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `playground_config` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable config name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| max_session_tokens | integer | yes | Token budget per evaluation session |
| max_session_duration_min | integer | yes | Session time limit in minutes |
| available_nuclei | list | yes | Which nuclei are accessible in playground |
| available_tools | list | no | Tool allowlist for playground sessions |
| persist_artifacts | boolean | yes | Whether artifacts survive session end |
| watermark | boolean | no | Add playground watermark to outputs |
| rate_limit | integer | no | Max requests per minute per user |

## When to use
- Setting up a prospect evaluation environment for enterprise sales demos
- Creating an internal sandbox for developers to test new nucleus capabilities
- Configuring a limited-access trial for CEX as a service offering

## Builder
`archetypes/builders/playground_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind playground_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: playground_prospect_demo
kind: playground_config
pillar: P09
nucleus: n06
title: "Enterprise Prospect Playground"
version: 1.0
quality: null
---
max_session_tokens: 50000
max_session_duration_min: 30
available_nuclei: [n01, n03]
persist_artifacts: false
watermark: true
rate_limit: 10
```

## Related kinds
- `sandbox_config` (P09) -- technical sandbox backing the playground environment
- `usage_quota` (P09) -- quota enforcement for playground session budgets
- `white_label_config` (P09) -- branded playgrounds for white-label deployments
