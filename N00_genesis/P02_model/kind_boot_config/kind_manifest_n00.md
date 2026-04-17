---
id: n00_boot_config_manifest
kind: knowledge_card
pillar: P02
nucleus: n00
title: "Boot Config -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, boot_config, p02, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P02 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Boot Config defines the startup configuration for a nucleus or agent per LLM provider. It specifies the CLI invocation parameters, environment variables, model flags, and pre-flight checks required to boot a nucleus correctly in a given provider's runtime (Claude, Codex, Gemini, Ollama). One boot_config per nucleus per provider.

## Pillar
P02 -- Model

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `boot_config` |
| pillar | string | yes | Always `P02` |
| title | string | yes | Nucleus + provider + environment |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| nucleus | string | yes | Target nucleus (n01-n07) |
| provider | enum | yes | claude\|codex\|gemini\|ollama |
| cli_command | string | yes | Base CLI invocation |
| model_flag | string | yes | Model selection flag and value |
| env_vars | map | no | Required environment variables |
| preflight_checks | list | no | Commands to verify before boot |

## When to use
- When adding support for a new provider to an existing nucleus
- When configuring per-environment boot parameters (dev, staging, prod)
- When troubleshooting nucleus boot failures

## Builder
`archetypes/builders/boot_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind boot_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA of the booting nucleus
- `{{TARGET_AUDIENCE}}` -- DevOps and operator teams
- `{{DOMAIN_CONTEXT}}` -- deployment environment and provider

## Example (minimal)
```yaml
---
id: boot_config_n03_claude
kind: boot_config
pillar: P02
nucleus: n03
title: "N03 Claude Boot Config"
version: 1.0
quality: null
---
nucleus: n03
provider: claude
cli_command: "claude"
model_flag: "--model claude-opus-4-6"
env_vars:
  CEX_NUCLEUS: n03
  CEX_CONTEXT: 1000000
preflight_checks:
  - "claude --version"
  - "python _tools/cex_setup_validator.py"
```

## Related kinds
- `fallback_chain` (P02) -- provider fallback sequence if this config fails
- `model_card` (P02) -- model specification referenced in this config
- `agent_package` (P02) -- package that uses this boot config
