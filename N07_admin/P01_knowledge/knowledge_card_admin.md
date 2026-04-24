---
id: p01_kc_orchestration
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Orchestration — Multi-CLI Dispatch"
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: orchestration
quality: 9.1
tags: [orchestration, dispatch, multi-cli, N07, spawn, knowledge]
tldr: "N07 orchestrates 6 nuclei via bash dispatch.sh — solo (1 builder) or grid (up to 6 parallel)."
when_to_use: "When understanding how CEX dispatches tasks across nuclei and CLI providers."
keywords: [orchestration, dispatch, spawn, solo, grid, signal, handoff, nucleus]
long_tails:
  - "how does N07 dispatch tasks to builders"
  - "what CLI does each nucleus use"
  - "how to launch parallel builders in CEX"
axioms:
  - "ALWAYS use bash _spawn/dispatch.sh — NEVER raw PowerShell or cmd from bash"
  - "NEVER dispatch below quality 8.0 — return to builder with feedback"
  - "IF multi-domain mission THEN use grid dispatch with per-nucleus handoffs"
linked_artifacts:
  primary: "N07_admin/P02_model/agent_admin.md"
  related: [N07_admin/P12_orchestration/dispatch_rule_admin.md, N07_admin/P12_orchestration/spawn_config_admin.md]
density_score: 1.0
data_source: "N07_admin/P12_orchestration/spawn_config_admin.md"
related:
  - dispatch
  - p02_agent_admin_orchestrator
  - p12_wf_admin_orchestration
  - p03_sp_admin_orchestrator
  - p08_ac_admin_orchestrator
  - p01_kc_orchestration_best_practices
  - p03_sp_orchestration_nucleus
  - p08_ac_orchestrator
  - p12_wf_orchestration_pipeline
  - p12_ho_admin_template
---

# CEX Orchestration — Multi-CLI Dispatch

## Quick Reference

```yaml
orchestrator: N07 (pi + claude opus xhigh)
nuclei_count: 6 (N01-N06)
dispatch_modes: solo, grid, continuous
signal_path: .cex/runtime/signals/
handoff_path: .cex/runtime/handoffs/
quality_threshold: 8.0
```

## Key Concepts

- **Multi-CLI Architecture**: Each nucleus uses the optimal LLM provider — opus for complex construction, gemini for 1M context knowledge, codex for code review, sonnet for creative writing
- **Dispatch Modes**: Solo (1 builder, new terminal) for single tasks; Grid (up to 6 parallel) for missions
- **Signal Protocol**: Builders emit JSON signals (complete/error/progress) to `.cex/runtime/signals/` on task completion
- **Handoff Contract**: Structured .md files with task, context, scope fence, commit convention, and signal instructions

## Routing Table

| Domain | Nucleus | CLI | Model | Context |
|--------|---------|-----|-------|---------|
| Build/scaffold | N03 | claude | opus | 200K |
| Research/analysis | N01 | gemini | 2.5-pro | 1M |
| Marketing/copy | N02 | claude | sonnet | 200K |
| Knowledge/docs | N04 | gemini | 2.5-pro | 1M |
| Code/test/deploy | N05 | codex | GPT-5.4 | 192K |
| Sales/pricing | N06 | claude | sonnet | 200K |

## Dispatch Commands

```bash
# Solo — single builder in new window
bash _spawn/dispatch.sh solo n03 "Leia .cex/runtime/handoffs/HANDOFF.md e execute."

# Grid — up to 6 parallel builders
bash _spawn/dispatch.sh grid MISSION_NAME

# Monitor active builders
bash _spawn/dispatch.sh status

# Stop all builders
bash _spawn/dispatch.sh stop
```

## Signal Protocol

```json
{
  "agent_group": "n03",
  "status": "complete",
  "quality_score": 9.0,
  "timestamp": "2026-03-30T14:00:00Z",
  "task": "bootstrap_f1",
  "artifacts": ["N07_admin/P02_model/agent_admin.md"],
  "artifacts_count": 1
}
```

## Golden Rules

- N07 NEVER builds artifacts — always dispatches to appropriate nucleus
- Quality gate: reject any builder output below 8.0, return with feedback
- Handoff before dispatch: always write `.cex/runtime/handoffs/{mission}_{nucleus}.md` first
- Signal before pause: builders must commit and signal before any interruption

## Quality Tiers

| Tier | Score | Action |
|------|-------|--------|
| GOLDEN | >= 9.5 | Reference example |
| PUBLISH | >= 8.0 | Standard publication |
| REVIEW | >= 7.0 | Needs revision |
| REJECT | < 7.0 | Redo from scratch |

## References

- Spawn config: N07_admin/P12_orchestration/spawn_config_admin.md
- Fallback chain: N07_admin/P02_model/fallback_chain_admin.md
- Mission plan: N07_admin/P12_orchestration/mission_bootstrap_2026Q1.md


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[dispatch]] | downstream | 0.57 |
| [[p02_agent_admin_orchestrator]] | downstream | 0.56 |
| [[p12_wf_admin_orchestration]] | downstream | 0.56 |
| [[p03_sp_admin_orchestrator]] | downstream | 0.55 |
| [[p08_ac_admin_orchestrator]] | downstream | 0.55 |
| [[p01_kc_orchestration_best_practices]] | sibling | 0.51 |
| [[p03_sp_orchestration_nucleus]] | downstream | 0.47 |
| [[p08_ac_orchestrator]] | downstream | 0.37 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.36 |
| [[p12_ho_admin_template]] | downstream | 0.36 |
