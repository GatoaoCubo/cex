---
id: schedule
kind: instruction
pillar: P12
description: "Create, list, update scheduled agents (cron). Usage: /schedule <cron> <command>"
quality: 9.1
title: "Schedule"
version: "1.0.0"
author: n03_builder
tags: [instruction, command, scheduling, cron, boris_merge]
tldr: "Register recurring remote agents via CronCreate, with cross-runtime fallback."
domain: "CEX system"
created: "2026-04-15"
updated: "2026-04-15"
density_score: 0.88
---

# /schedule — Recurring Remote Agents

> Harness-native via `CronCreate`/`CronList`/`CronDelete` in Claude Code.
> Falls back to OS cron / Task Scheduler for codex/gemini/ollama runtimes.

## Usage

| Form | Action |
|------|--------|
| `/schedule "0 3 * * *" /mission evolve` | Daily 03:00 -- evolve sweep |
| `/schedule "*/30 * * * *" /consolidate` | Every 30 min -- consolidation |
| `/schedule list` | Show registered triggers |
| `/schedule delete <trigger-id>` | Remove a trigger |
| `/schedule run <trigger-id>` | Fire once now |

## Difference from /loop

| /loop | /schedule |
|-------|-----------|
| Same session, wake-up + resume | Remote agent, fresh session each fire |
| Cache-warm pacing (60-270s) | Cron-precise timing (minute resolution) |
| Dies with session | Survives session end |
| Good for polling | Good for scheduled jobs (nightly evolve, weekly reports) |

## Runtime Bridges

| Runtime | Mechanism |
|---------|-----------|
| Claude Code | native `CronCreate` tool -- managed remote agent |
| Codex | invoke via `schtasks` (Windows) / `cron` (Linux) with wrapper |
| Gemini | `cron` + `boot/n0X_gemini.ps1` |
| Ollama | `cron` + `python _tools/cex_8f_runner.py --model ollama/<model>` |

Bridge script: `_tools/cex_schedule_bridge.py` (emits platform-appropriate
cron/schtasks entries; reads/writes `.cex/runtime/schedules/registry.yaml`).

## Trigger Format

Cron 5-field (`min hour dom mon dow`). Validated before register.
For Windows Task Scheduler, bridge translates cron -> schtasks `/SC`.

## Invocation

When user types `/schedule`, invoke the harness skill:

```
Skill(skill="schedule", args="$ARGUMENTS")
```

## Registry

All scheduled agents live in `.cex/runtime/schedules/registry.yaml`:

```yaml
triggers:
  - id: nightly_evolve
    cron: "0 3 * * *"
    command: "/mission evolve"
    runtime: claude
    created: 2026-04-15T16:30:00-03:00
    last_fired: null
    enabled: true
```

## Guardrails

1. Max 20 active triggers per project.
2. Triggers firing >12/hour require `--high-frequency` flag.
3. `/schedule delete` always confirms before removal.
4. Disabled trigger remains in registry (audit trail).

## Example: autonomous evolution

```
/schedule "0 */4 * * *" /mission evolve
-> trigger registered: evolve_q4h
-> every 4h: fresh N07 session evolves artifacts below 9.0
-> logs: .cex/runtime/schedules/logs/evolve_q4h_*.log
```
