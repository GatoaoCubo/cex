---
id: p12_spawn_builder_construction
kind: spawn_config
pillar: P12
title: "Spawn Configuration — N03 Builder"
version: 2.0.0
created: 2026-04-07
updated: 2026-04-07
author: builder_agent
domain: construction
quality: 8.9
tags: [spawn-config, builder, N03, cli, model, dispatch]
tldr: "Spawn configuration for N03 Builder -- claude CLI with opus-4-6, 1M context, interactive mode."
density_score: 0.92
linked_artifacts:
  primary: "N03_builder/orchestration/dispatch_rule_builder.md"
  related:
    - .cex/config/nucleus_models.yaml
    - N07_admin/orchestration/spawn_config_admin.md
---

# Spawn Configuration — N03 Builder

## Purpose

Defines the exact CLI, model, and launch parameters for spawning N03 Builder
in a new terminal window. Used by `_spawn/dispatch.sh` when N07 dispatches
construction tasks.

## Configuration

```yaml
nucleus: N03
name: builder
cli: claude
model: opus-4-6
context_window: 1000000
mode: interactive
color:
  bg: DarkBlue
  fg: White
  accent: Blue
icon: "★"
sin: soberba
```

## Launch Command

```bash
# Solo dispatch (used by dispatch.sh)
bash _spawn/dispatch.sh solo n03 "Leia .cex/runtime/handoffs/n03_task.md e execute."

# What dispatch.sh executes internally:
start "N03 Builder ★" cmd /k "claude --model opus-4-6 --prompt 'Read .cex/runtime/handoffs/n03_task.md and execute.'"
```

## Environment

| Variable | Value | Purpose |
|----------|-------|---------|
| `CEX_NUCLEUS` | N03 | Identifies active nucleus |
| `CEX_SIN` | soberba | Sin lens for prompt injection |
| `CEX_MODEL` | opus-4-6 | Model selection |
| `CEX_CONTEXT` | 1000000 | Context window size |

## Terminal Settings

- **Title**: `N03 Builder ★`
- **Color scheme**: Blue background (DarkBlue), white text
- **Working directory**: Repository root (`C:\Users\PC\Documents\GitHub\cex`)
- **Mode**: Interactive (reads handoff, executes, signals)

## Model Rationale

opus-4-6 selected for N03 because:
1. **Complex construction**: 8F pipeline requires deep reasoning
2. **Large ISOs**: 13 ISOs per kind need full context understanding
3. **Quality floor 9.0**: Requires the strongest model for consistent quality
4. **Schema validation**: Complex frontmatter rules need precise generation

## Fallback Chain

If opus-4-6 is unavailable:
1. Try opus-4-6 (primary)
2. Fall back to sonnet-4-6 (reduced quality)
3. Signal error if no model available

## References

- Model config: `.cex/config/nucleus_models.yaml`
- N07 spawn config: N07_admin/orchestration/spawn_config_admin.md
- Dispatch script: `_spawn/dispatch.sh`
