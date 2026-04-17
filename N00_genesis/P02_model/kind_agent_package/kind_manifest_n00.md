---
id: n00_agent_package_manifest
kind: knowledge_card
pillar: P02
nucleus: n00
title: "Agent Package -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, agent_package, p02, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P02 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Agent Package is a portable, self-contained AI agent bundle in ISO format. It packages all 13 ISOs (manifest, instructions, system prompt, tools, memory, examples, etc.) required to instantiate and run an agent in any supported runtime (Claude, Codex, Gemini, Ollama). Agent packages are the distribution unit for sharing agents across environments.

## Pillar
P02 -- Model

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `agent_package` |
| pillar | string | yes | Always `P02` |
| title | string | yes | Package name and target agent |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| agent_ref | string | yes | Reference to agent artifact being packaged |
| iso_count | int | yes | Number of ISOs included (target: 13) |
| runtimes | list | yes | Supported runtimes: claude, codex, gemini, ollama |
| entrypoint | string | yes | Path to boot script or main ISO |
| checksum | string | no | SHA256 hash of package contents |

## When to use
- When distributing an agent to a different environment or team
- When creating a deployable artifact from a developed agent
- When enabling multi-runtime portability for an agent

## Builder
`archetypes/builders/agent_package-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind agent_package --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA of the packaged agent
- `{{TARGET_AUDIENCE}}` -- deployment team or runtime operator
- `{{DOMAIN_CONTEXT}}` -- deployment environment and target use case

## Example (minimal)
```yaml
---
id: agent_package_n03_builder_v1
kind: agent_package
pillar: P02
nucleus: n03
title: "N03 Builder Agent Package v1"
version: 1.0
quality: null
---
agent_ref: agent_n03_engineer
iso_count: 13
runtimes: [claude, ollama]
entrypoint: boot/n03.ps1
```

## Related kinds
- `agent` (P02) -- the agent definition being packaged
- `boot_config` (P02) -- runtime boot configuration per provider
- `nucleus_def` (P02) -- formal nucleus this package implements
