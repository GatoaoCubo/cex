---
id: n00_spawn_config_manifest
kind: knowledge_card
pillar: P12
nucleus: n00
title: "Spawn Config -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, spawn_config, p12, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P12 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A spawn_config defines the configuration for spawning nucleus processes in solo, grid, or continuous modes, specifying the CLI, model, dispatch mode, session isolation, PID tracking, and process management settings. It is the declarative infrastructure spec that `dispatch.sh` and `spawn_grid.ps1` read to launch nuclei with consistent and reproducible settings.

## Pillar
P12 -- orchestration

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `spawn_config` |
| pillar | string | yes | Always `P12` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| dispatch_mode | enum | yes | solo \| grid \| swarm \| continuous |
| cli | enum | yes | claude \| codex \| gemini \| ollama \| auto |
| model | string | yes | Model identifier for the spawned nucleus |
| max_concurrent | integer | yes | Maximum parallel nucleus processes |
| session_isolation | boolean | yes | Whether each spawn gets an isolated session ID |
| worktree | boolean | no | Whether to spawn in a git worktree |
| pid_tracking | boolean | yes | Whether to write PIDs to spawn_pids.txt |

## When to use
- When configuring how N07 spawns nuclei for a specific mission type
- When adding a new CLI provider to the dispatch layer
- When setting up swarm mode for parallel same-kind spawning

## Builder
`archetypes/builders/spawn_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind spawn_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: sc_grid_claude_opus
kind: spawn_config
pillar: P12
nucleus: n07
title: "Example Spawn Config"
version: 1.0
quality: null
---
# Spawn Config: Grid / Claude Opus
dispatch_mode: grid
cli: claude
model: claude-opus-4-6
max_concurrent: 6
session_isolation: true
pid_tracking: true
```

## Related kinds
- `dispatch_rule` (P12) -- routing rules that reference this spawn config
- `signal` (P12) -- signals monitored after this config spawns processes
- `handoff` (P12) -- handoff files read by nuclei spawned with this config
