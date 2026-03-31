---
id: p12_spawn_operations_nucleus
kind: spawn_config
pillar: P12
version: 3.0.0
created: 2026-03-30
updated: 2026-03-31
author: n05_operations
title: Operations Nucleus Spawn Config
mode: solo
agent_node: operations_nucleus
model: gpt-5.4
flags:
  - --dangerously-skip-permissions
  - --model
  - gpt-5.4
  - --reasoning-effort
  - high
mcp_config: .mcp-n05.json
timeout_seconds: 5400
prompt_inline: false
handoff_path: .cex/runtime/handoffs/n05_task.md
quality: null
tags: [spawn_config, N05, operations, codex, ci-cd]
tldr: Spawn contract for N05 on Codex with mandatory handoff-first behavior and enough runtime budget for review, test, debug, and deploy validation loops.
domain: operations-engineering
density_score: 0.94
---

# Spawn Command

```powershell
codex --dangerously-skip-permissions --model gpt-5.4 --reasoning-effort high
```

## Parameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| `mode` | `solo` | repository execution tasks typically require single-owner control of the worktree |
| `agent_node` | `operations_nucleus` | routes directly to the N05 operational persona |
| `model` | `gpt-5.4` | strongest fit for review, debugging, CI/CD diagnosis, and patching |
| `mcp_config` | `.mcp-n05.json` | reserved for GitHub Actions, Docker, pytest, and linter integrations |
| `timeout_seconds` | `5400` | allows long test suites, compile loops, and release validation work |
| `handoff_path` | `.cex/runtime/handoffs/n05_task.md` | standard intake for operational missions |

## Mandatory Behaviors

- Read the handoff before any substantive action.
- Use the local repository and runtime evidence as source of truth.
- Preserve unrelated changes in dirty worktrees.
- If the handoff demands commit and signal, perform both before pausing.

## Recommended Use Cases

- code review with executable validation
- failing or flaky test repair
- debugging with logs or traces
- CI workflow repair
- deployment or rollback readiness checks
