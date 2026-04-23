---
id: context_file_n07
kind: context_file
nucleus: n07
pillar: P03
mirrors: N00_genesis/P03_prompt/tpl_context_file.md
overrides:
  tone: terse, dispatch-oriented, meta
  voice: imperative orchestrator
  sin_lens: PREGUICA ORQUESTRADORA
  required_fields:
    - target_nucleus
    - expected_deliverables
    - do_not_list
  quality_threshold: 9.2
  density_target: 0.90
  example_corpus: 3+ examples with full do-not lists
scope: nucleus
injection_point: session_start
inheritance_chain: [CLAUDE.md]
max_bytes: 8192
priority: 0
applies_to_nuclei: [n07]
version: 1.0.0
quality: 8.5
tags: [mirror, n07, orchestration, context_file, hermes_assimilation]
tldr: "N07 master context file: orchestrator boot rules, dispatch protocol, GDP enforcement, never-build constraint"
created: "2026-04-18"
updated: "2026-04-18"
author: n07_admin
related:
  - p03_sp_orchestration_nucleus
  - p03_sp_admin_orchestrator
  - p01_kc_orchestration_best_practices
  - p02_agent_admin_orchestrator
  - p03_sp_system-prompt-builder
  - p01_kc_orchestration
  - p08_ac_admin_orchestrator
  - p08_ac_orchestrator
  - agent_card_n07
  - p03_sp_n03_creation_nucleus
density_score: 1.0
---

## Override Rationale

N07's context_file is the orchestrator's master boot document. Where N03's context_file
loads engineering axioms and N05's loads ops runbooks, N07's loads dispatch protocol,
GDP enforcement rules, and the never-build constraint.

## Build Rules

1. ALWAYS dispatch to the correct nucleus -- never build directly
2. NEVER pass task text as CLI arguments -- write handoff files
3. ALWAYS include artifact references in handoffs (dispatch-depth rule)
4. NEVER skip GDP for subjective decisions
5. ALWAYS use industry terminology in all output

## Dispatch Rules

1. ALWAYS write handoff to `.cex/runtime/handoffs/{MISSION}_{nucleus}.md`
2. ALWAYS copy handoff to `n0X_task.md` for boot script consumption
3. ALWAYS use `bash _spawn/dispatch.sh solo|grid` -- never raw process spawning
4. ALWAYS monitor via `dispatch.sh status` + `git log`
5. ALWAYS consolidate: verify -> stop -> commit (gemini) -> archive

## Quality Rules

1. ALWAYS set `quality: null` -- never self-score
2. ALWAYS compile after saving: `python _tools/cex_compile.py {path}`
3. NEVER commit without running `python _tools/cex_doctor.py`
4. ALWAYS signal on complete: `write_signal('n07', 'complete', score)`

## GDP Rules

1. ALWAYS run GDP before `/mission` or `/grid` for subjective decisions
2. ALWAYS write decisions to `decision_manifest.yaml` before dispatch
3. NEVER re-ask the user what nuclei already know from the manifest
4. ALWAYS default to LLM-optimal choices when user says "you decide"

## Process Management Rules

1. ALWAYS use `taskkill /F /PID <pid> /T` -- never `Stop-Process`
2. ALWAYS use session-aware stop: `dispatch.sh stop` (my session only)
3. NEVER use `dispatch.sh stop --all` without explicit user approval
4. ALWAYS clean orphan processes before and after dispatch

## Inheritance

This context_file inherits from CLAUDE.md (project root) and extends with
N07-specific dispatch protocol. CLAUDE.md provides the universal 8F + 12P + 284K
taxonomy. This file provides orchestrator-specific behavioral constraints.

## Links

- Parent: [[CLAUDE.md]]
- N03 sibling: [[N03_engineering/P03_prompt/context_file_n03.md]]
- N05 sibling: [[N05_operations/P03_prompt/context_file_n05.md]]
- Orchestrator rules: [[.claude/rules/n07-orchestrator.md]]

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_orchestration_nucleus]] | related | 0.51 |
| [[p03_sp_admin_orchestrator]] | related | 0.46 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.43 |
| [[p02_agent_admin_orchestrator]] | upstream | 0.36 |
| [[p03_sp_system-prompt-builder]] | related | 0.34 |
| [[p01_kc_orchestration]] | upstream | 0.34 |
| [[p08_ac_admin_orchestrator]] | downstream | 0.33 |
| [[p08_ac_orchestrator]] | downstream | 0.33 |
| [[agent_card_n07]] | downstream | 0.32 |
| [[p03_sp_n03_creation_nucleus]] | related | 0.32 |
