---
id: p11_qg_spawn_config
kind: quality_gate
pillar: P12
title: "Gate: Spawn Config"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: spawn_config
quality: 9.0
density_score: 0.85
tags:
  - quality-gate
  - spawn-config
  - orchestration
  - P12
tldr: "Validates agent_group spawn configurations for mode, CLI flags, model pairing, and runtime safety."
llm_function: GOVERN
---
## Definition
A spawn config defines how a agent_group process is launched: execution mode (solo, grid, or continuous), CLI flags passed to the runtime, the model driving the agent_group, and how prompts and recovery are handled. This gate ensures every spawn config is safe to execute without human intervention and unambiguous to the launch runtime.
## HARD Gates
Failure on any HARD gate causes immediate REJECT. No score is computed.
| ID  | Check | Rule |
|-----|-------|------|
| H01 | Frontmatter parses | YAML frontmatter is valid and complete with no syntax errors |
| H02 | ID matches namespace | `id` matches pattern `^p12_sc_[a-z][a-z0-9_]+$` |
| H03 | ID equals filename | `id` slug matches the parent directory or filename stem |
| H04 | Kind matches literal | `kind` is exactly `spawn_config` |
| H05 | Quality is null | `quality` field is `null` (not yet scored) |
| H06 | Required fields present | `mode`, `agent_group`, `model`, `cli_flags`, `prompt` all defined and non-empty |
| H07 | Mode is valid enum | `mode` is one of: `solo`, `grid`, `continuous` |
| H08 | CLI flags defined | `cli_flags` is a non-empty list with at least one entry |
| H09 | Agent_group-model pairing | `agent_group` and `model` are both non-empty strings |
| H10 | Prompt size within limits | Inline `prompt` is <= 200 characters; longer prompts reference a handoff file path |
## SOFT Scoring
Score each dimension 0 or 10. Multiply by weight. Divide total by sum of weights, scale to 0-10.
| Dimension | Weight | Pass Condition |
|-----------|--------|----------------|
| Density >= 0.80 | 1.0 | Config is concise; no redundant or placeholder fields |
| Timeout policies per mode | 1.0 | Each mode defines a `timeout_ms` or `timeout_per_step_ms` |
| MCP config path validated | 1.0 | If `mcp_config` is set, path follows `.mcp-{sat}.json` pattern |
| Interactive mode documented | 0.5 | `interactive` flag is explicit (true/false, not omitted) |
| Tags include spawn-config | 0.5 | `tags` list contains `"spawn-config"` |
| Handoff file reference | 0.5 | If task is complex, `handoff_file` field points to an existing `.md` path |
| Resource limits defined | 1.0 | `max_terminals` or equivalent concurrency cap is present |
| Error recovery documented | 1.0 | `on_failure` field describes retry or skip behavior |
| Wave ordering for grid mode | 1.0 | Grid and continuous configs include `wave_order` or explicit dependency list |
| Spawn delay documented | 0.5 | `spawn_delay_ms` is defined when mode is `grid` or `continuous` |
| No task instructions in body | 1.0 | Config contains parameters only; no prose task instructions |
Sum of weights: 9.0. `soft_score = sum(weight * gate_score) / 9.0 * 10`
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — archive to pool as reference spawn config |
| >= 8.0 | PUBLISH — safe for production agent_group dispatch |
| >= 7.0 | REVIEW — usable but missing safety or recovery detail |
| < 7.0 | REJECT — do not execute; incomplete or unsafe config |
## Bypass
| Field | Value |
|-------|-------|
| condition | Emergency agent_group launch during active incident where config cannot be revised before deploy |
| approver | Lead engineer on duty (human, not automated) |
| audit_log | Entry required in `.claude/bypasses/spawn_config_{date}.md` with written justification |
| expiry | 24 hours; config must reach PUBLISH score before next planned launch |
H01 (frontmatter parses) and H05 (quality is null) cannot be bypassed under any condition.
