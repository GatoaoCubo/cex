---
id: p12_spawn_railway_superintendent
kind: spawn_config
pillar: P12
version: 4.0.0
created: 2026-04-01
updated: 2026-04-01
author: n05_operations
title: Railway Backend Superintendent Spawn Config
mode: solo
agent_group: railway_superintendent
model: opus
flags:
  - --model
  - opus
  - --reasoning-effort
  - high
mcp_config: .mcp-n05.json
timeout_seconds: 7200
prompt_inline: false
handoff_path: .cex/runtime/handoffs/n05_task.md
quality: 9.1
tags: [spawn_config, railway, superintendent, opus, fastapi, postgresql]
tldr: Railway Superintendent spawn on Claude Opus with railway/postgresql MCPs for FastAPI deployment lifecycle and 4-service topology management.
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
| `agent_group` | `operations_nucleus` | routes directly to the N05 operational persona |
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

## Quality Metrics

| Metric | Value | Threshold |
|--------|-------|-----------|
| Structural completeness | High | ≥ 8.5 |
| Domain specificity | operations | Verified |
| Cross-reference density | Adequate | ≥ 3 refs |
| Actionability | Verified | Pass |

### Key Principles

- Operations artifacts follow CEX 8F pipeline from intent to publication
- Quality gates enforce minimum 8.0 threshold for all published artifacts
- Cross-nucleus references use explicit id-based linking, not path-based
- Version tracking enables rollback to any previous artifact state

