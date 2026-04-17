---
quality: 7.6
kind: spec
pillar: P08
created: 2026-04-15
author: N03
mission: BORIS_MERGE
density_score: 1.0
updated: "2026-04-17"
---

# Spec: Multi-Runtime Feature Coverage

## Purpose

Every feature added to CEX MUST work on the 4 supported runtimes. This spec
is the compatibility contract. If a feature cannot be made runtime-agnostic
it must be documented as a gap and paired with a per-runtime fallback.

## The 4 runtimes

| Runtime | Binary | Auth | Strengths |
|---------|--------|------|-----------|
| **claude** | `claude` (Anthropic CLI) | Max subscription | Native hooks, skills, slash commands, 1M context |
| **codex** | `codex` (OpenAI) | API key | Long ctx, strong reasoning, MCP |
| **gemini** | `gemini` (Google) | API key | Free tier, MCP, multimodal |
| **ollama** | local via `ollama run` | none | Offline, free, latency-sensitive |

## Compatibility matrix

| Feature family | claude | codex | gemini | ollama | Gap fallback |
|----------------|--------|-------|--------|--------|--------------|
| Skills (`.claude/skills/`) | native | mirror `.cex/skills/` | mirror `.cex/skills/` | mirror `.cex/skills/` | YAML + body loader |
| Hooks | native `settings.json` | boot-wrapper call | boot-wrapper call | boot-wrapper call | `cex_hooks_native.py` is the common entrypoint |
| Slash commands | native | skill-as-prompt | skill-as-prompt | skill-as-prompt | commands wrap skills |
| MCP servers | `.mcp.json` | `.mcp.json` | `.mcp.json` | n/a (no MCP) | ollama uses direct tools |
| Worktree isolation | `-w` flag | `-w` flag | `-w` flag | `-w` flag | via `boot/_shared/worktree_helpers.ps1` |
| `--auto-accept` handoff | CEX_AUTO_ACCEPT env | CEX_AUTO_ACCEPT env | CEX_AUTO_ACCEPT env | CEX_AUTO_ACCEPT env | same env flag, every wrapper reads it |
| `/schedule` cron | CronCreate native | host cron | host cron | host cron | `cex_schedule.py` wraps both |
| `/loop` dynamic pacing | ScheduleWakeup native | `cron` + `cex_mission_runner` | same | same | common runner for 3 non-native |
| `/swarm N builders` | `dispatch.sh swarm` | `dispatch.sh swarm` | `dispatch.sh swarm` | `dispatch.sh swarm` | shared shell wrapper |

## Rule of thumb

1. **Author once**: write the feature's *logic* in a python `_tools/cex_*.py`
2. **Wire once**: add a skill in `.claude/skills/` AND mirror in `.cex/skills/`
3. **Call uniformly**: all 4 boot wrappers invoke the same python script
4. **Hook uniformly**: `cex_hooks_native.py` is the single event entrypoint
5. **Detect runtime**: python reads `CEX_RUNTIME` env (`claude|codex|gemini|ollama`)

## Anti-patterns (BLOCKED)

- Claude-only feature without mirror -- skills MUST be in both `.claude/skills/`
  (for native) and `.cex/skills/` (for others).
- Hard-coded CLI binary -- use `nucleus_models.yaml` `fallback_chain`.
- Hook that calls a Claude-Code-only API -- use `cex_hooks_native.py`.
- Slash command with no skill -- commands are thin wrappers over skills.

## Verification

`python _tools/cex_multiruntime_audit.py` (future) walks every feature and
flags the ones without mirror/fallback. Part of `cex_doctor.py`.

## Properties

| Property | Value |
|----------|-------|
| Kind | `spec` |
| Pillar | P08 |
| Domain | multi-runtime architecture |
| Pipeline | 8F (F1-F8) |
| Quality target | 9.0+ |
| Density target | 0.85+ |
