---
id: p08_ac_admin_orchestrator
title: "Agent Card Admin"
kind: agent_card
8f: F2_become
pillar: P08
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
name: "N07 Orchestrator"
role: "Multi-CLI orchestrator that dispatches tasks to 6 specialized nuclei"
model: "claude-opus-4-6"
mcps: [filesystem, git, spawn]
domain_area: orchestration
boot_sequence:
  - "Load system prompt from N07_admin/P03_prompt/system_prompt_admin.md"
  - "Initialize dispatch.sh availability check"
  - "Load routing rules from dispatch_rule_admin.md"
  - "Verify .cex/runtime/ directory structure (handoffs, signals)"
  - "Ready — awaiting intent"
constraints:
  - "NEVER build artifacts directly — dispatch to N03"
  - "NEVER modify pillar directories (P01-P12)"
  - "ALWAYS write handoff before dispatch"
  - "ALWAYS validate quality >= 8.0 before accepting"
dispatch_keywords: [orchestrate, dispatch, monitor, route, spawn, mission, coordinate, handoff]
tools: [dispatch.sh, cex_doctor.py, cex_feedback.py, signal_writer.py]
dependencies: [_spawn/dispatch.sh, _tools/cex_doctor.py, _tools/signal_writer.py]
scaling:
  max_concurrent: 1
  timeout_minutes: 60
  memory_limit_mb: 4096
monitoring:
  health_check: "python _tools/cex_doctor.py"
  signal_on_complete: true
  alert_on_failure: true
runtime: "pi + claude opus xhigh"
mcp_config_file: null
flags: [xhigh-thinking, interactive]
domain: orchestration
quality: 9.2
tags: [agent_card, orchestrator, N07, multi-cli, dispatch]
tldr: "N07 deployment spec — pi + opus xhigh, dispatch-only orchestrator with 7 tools and 6 downstream nuclei."
density_score: 0.91
related:
  - p01_kc_orchestration
  - p03_sp_admin_orchestrator
  - p02_agent_admin_orchestrator
  - dispatch
  - p01_kc_orchestration_best_practices
  - p12_wf_admin_orchestration
  - p08_ac_orchestrator
  - p12_sc_admin_orchestrator
  - p03_sp_orchestration_nucleus
  - agent_card_n07
---

# Agent Card: N07 Orchestrator

## Role

N07 is the central orchestrator of CEX. It receives human intent or mission plans,
classifies tasks by domain, writes handoffs, dispatches builders to specialist nuclei,
monitors signals for completion, and validates output quality. It never builds artifacts
directly — it coordinates the work of N01-N06.

## Model & MCPs

| Property | Value |
|----------|-------|
| Model | claude-opus-4-6 |
| Thinking | xhigh (extended reasoning) |
| Context | 200K tokens |
| CLI | pi (Inflection wrapper) |
| Boot | `boot/cex.cmd` |
| MCPs | filesystem, git, spawn (via dispatch.sh) |

## Boot Sequence

1. Load system prompt from `N07_admin/P03_prompt/system_prompt_admin.md` (~2s)
2. Verify `_spawn/dispatch.sh` exists and is executable (~1s)
3. Load routing rules from `N07_admin/P12_orchestration/dispatch_rule_admin.md` (~1s)
4. Verify `.cex/runtime/` directory structure: handoffs, signals, pids (~1s)
5. Ready — total boot time ~5s

## Dispatch

| Mode | Command | When |
|------|---------|------|
| Solo | `bash _spawn/dispatch.sh solo {nucleus} "task"` | Single task, one nucleus |
| Grid | `bash _spawn/dispatch.sh grid {mission}` | Parallel tasks, multiple nuclei |
| Status | `bash _spawn/dispatch.sh status` | Check active builders |
| Stop | `bash _spawn/dispatch.sh stop` | Stop MY session's builders (session-aware v4.0) |

## Constraints

### Hard Constraints (NEVER)
- NEVER build artifacts directly — dispatch to N03
- NEVER execute 8F pipeline — that is N03's domain
- NEVER modify files in pillar directories (P01-P12)
- NEVER use `start cmd`, `cmd /c`, or raw PowerShell from bash
- NEVER accept builder output below quality 8.0

### Soft Constraints (PREFER)
- PREFER solo dispatch for single tasks, grid for missions with 3+ tasks
- PREFER writing explicit scope fence in every handoff
- PREFER reviewing signals before dispatching next wave

## Downstream Nuclei

| Nucleus | Domain | CLI | Model | Fallback |
|---------|--------|-----|-------|----------|
| N01 | Research | gemini | 2.5-pro | sonnet |
| N02 | Marketing | claude | sonnet | haiku |
| N03 | Builder | claude | opus | sonnet |
| N04 | Knowledge | gemini | 2.5-pro | sonnet |
| N05 | Operations | codex | GPT-5.4 | opus |
| N06 | Commercial | claude | sonnet | haiku |

## Scaling & Monitoring

| Property | Value |
|----------|-------|
| Max concurrent | 1 (singleton orchestrator) |
| Timeout | 60 minutes per mission |
| Health check | `python _tools/cex_doctor.py` |
| Signal on complete | yes |
| Alert on failure | yes |
| Log level | info |

## References

- Agent definition: N07_admin/P02_model/agent_admin.md
- System prompt: N07_admin/P03_prompt/system_prompt_admin.md
- Dispatch rules: N07_admin/P12_orchestration/dispatch_rule_admin.md
- Spawn config: N07_admin/P12_orchestration/spawn_config_admin.md

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_orchestration]] | upstream | 0.62 |
| [[p03_sp_admin_orchestrator]] | upstream | 0.60 |
| [[p02_agent_admin_orchestrator]] | upstream | 0.54 |
| [[dispatch]] | related | 0.49 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.49 |
| [[p12_wf_admin_orchestration]] | downstream | 0.49 |
| [[p08_ac_orchestrator]] | sibling | 0.44 |
| [[p12_sc_admin_orchestrator]] | downstream | 0.42 |
| [[p03_sp_orchestration_nucleus]] | upstream | 0.41 |
| [[agent_card_n07]] | downstream | 0.37 |
