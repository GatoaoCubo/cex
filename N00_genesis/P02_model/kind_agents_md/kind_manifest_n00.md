---
id: n00_agents_md_manifest
kind: knowledge_card
pillar: P02
nucleus: n00
title: "Agents MD -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, agents_md, p02, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P02 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Agents MD is an AAIF/OpenAI AGENTS.md project-root manifest that declares all available agents in a repository for agent discovery. It follows the emerging AGENTS.md convention where a project root file lists agent capabilities, entry points, and protocols so that orchestrators and multi-agent frameworks can discover and invoke them without prior configuration.

## Pillar
P02 -- Model

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `agents_md` |
| pillar | string | yes | Always `P02` |
| title | string | yes | Project name and agent roster |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| project | string | yes | Repository or project identifier |
| agents | list | yes | List of declared agent entries |
| discovery_protocol | enum | yes | aaif\|openai\|custom -- discovery standard |
| root_path | string | yes | Repository root where AGENTS.md lives |

## When to use
- When setting up a multi-agent project repository
- When enabling agent discovery for an orchestration framework
- When publishing available agents for external consumption

## Builder
`archetypes/builders/agents_md-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind agents_md --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N07)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- orchestration frameworks, multi-agent systems
- `{{DOMAIN_CONTEXT}}` -- project type and agent roster

## Example (minimal)
```yaml
---
id: agents_md_cex_repo
kind: agents_md
pillar: P02
nucleus: n07
title: "CEX Repository Agent Manifest"
version: 1.0
quality: null
---
project: cex
discovery_protocol: aaif
root_path: "C:/Users/CEX/Documents/GitHub/cex"
agents:
  - id: n01_intelligence
    entry: boot/n01.ps1
    capabilities: [research, analysis, competitive-intel]
  - id: n07_orchestrator
    entry: boot/cex.ps1
    capabilities: [orchestration, dispatch, mission-planning]
```

## Related kinds
- `agent` (P02) -- individual agents listed in this manifest
- `nucleus_def` (P02) -- formal nucleus definitions backing agents
- `boot_config` (P02) -- runtime boot parameters per agent
