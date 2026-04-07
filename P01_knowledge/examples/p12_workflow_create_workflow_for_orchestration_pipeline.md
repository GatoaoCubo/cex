---
id: p12_wf_orchestration_pipeline
kind: workflow
pillar: P12
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "workflow-builder"
title: "Orchestration Pipeline"
steps_count: 5
execution: mixed
agent_groups: [orchestrator, n01, n02, n03, n04, n05, n06]
timeout: 7200
retry_policy: per_step
depends_on: []
signals: [complete, error]
spawn_configs: [p12_spawn_n03_solo_build, p12_spawn_n01_solo_research, p12_spawn_n02_solo_marketing, p12_spawn_n04_solo_knowledge, p12_spawn_n05_solo_ops, p12_spawn_n06_solo_commercial]
domain: "orchestration"
quality: 9.0
tags: [workflow, orchestration, pipeline, multi-nucleus, gdp, mission]
tldr: "5-step mixed workflow: plan mission → gather decisions → generate spec → dispatch nuclei in parallel waves → consolidate results"
density_score: 0.91
---
## Purpose

Defines the end-to-end orchestration pipeline executed by N07 for any multi-nucleus mission. The workflow enforces GDP before dispatch (subjective decisions resolved before autonomous execution begins), fans out tasks to domain-specific nuclei in parallel waves, and consolidates outputs into a verified, committed deliverable. Steps 1–3 are strictly sequential (each step's output is the next step's input). Step 4 fans out to up to six nuclei in parallel waves. Step 5 runs only after all dispatched nuclei emit completion signals.

## Steps

### Step 1: Mission Planning [orchestrator]
- **Agent**: orchestrator (N07, opus)
- **Action**: Decompose the mission goal into discrete domain tasks and assign each to the appropriate nucleus (N01–N06) using the routing table
- **Input**: Mission goal string from user or handoff file at `.cex/runtime/handoffs/{MISSION}_n07.md`
- **Output**: Task decomposition written to `.cex/runtime/handoffs/{MISSION}_{nucleus}.md` for each assigned nucleus; `mission_planned` signal with task count
- **Signal**: `mission_planned`
- **Depends on**: none
- **On failure**: abort
- **Timeout**: 300s

### Step 2: Guided Decision Protocol [orchestrator]
- **Agent**: orchestrator (N07, opus)
- **Action**: Identify all subjective decision points in the mission (tone, audience, style, format), present them to the user as Decision Points, collect answers, and write `decision_manifest.yaml`
- **Input**: Task decomposition from Step 1; user in co-pilot session
- **Output**: `.cex/runtime/decisions/decision_manifest.yaml` with all resolved Decision Points; `decisions_committed` signal
- **Signal**: `decisions_committed`
- **Depends on**: Step 1
- **On failure**: abort (manifest is required; no autonomous execution without it)
- **Timeout**: 600s

### Step 3: Spec Generation [orchestrator]
- **Agent**: orchestrator (N07, opus)
- **Action**: Synthesize task decomposition and decision manifest into a spec blueprint — exact artifact IDs, pillar assignments, quality targets, and inter-artifact dependencies
- **Input**: Handoff files from Step 1; `decision_manifest.yaml` from Step 2
- **Output**: Spec file at `.cex/runtime/specs/{MISSION}_spec.md` listing all artifacts to produce; `spec_ready` signal
- **Signal**: `spec_ready`
- **Depends on**: Steps 1, 2
- **On failure**: abort
- **Timeout**: 300s

### Step 4: Nucleus Dispatch — Parallel Execution Wave [n01–n06]
- **Agent**: assigned nucleus per task (N01=research, N02=marketing, N03=build, N04=knowledge, N05=ops, N06=commercial)
- **Action**: Each nucleus reads its handoff file and `decision_manifest.yaml`, executes the full 8F pipeline for its assigned artifacts, commits outputs, and emits a completion signal
- **Input**: Per-nucleus handoff at `.cex/runtime/handoffs/{MISSION}_{nucleus}.md`; `decision_manifest.yaml`
- **Output**: Committed artifacts in `N0x_*/` directories; `{nucleus}_complete` signal with quality scores per nucleus
- **Signal**: `{nucleus}_complete` (one per active nucleus; wave completes when all active nuclei signal)
- **Depends on**: Step 3
- **On failure**: retry (per_step, max 1); if retry fails → skip failed nucleus and flag in consolidation report
- **Timeout**: 5400s (90 min; covers up to six parallel nuclei)

### Step 5: Consolidation [orchestrator]
- **Agent**: orchestrator (N07, opus)
- **Action**: Verify all nucleus outputs with `cex_doctor.py`, commit Gemini nucleus files (N01/N04 cannot git), score artifacts with `cex_score.py`, archive handoffs, and push final state
- **Input**: `{nucleus}_complete` signals from Step 4; `git log`; nucleus output directories
- **Output**: Consolidation report at `.cex/runtime/archive/{MISSION}_consolidation.md`; `workflow_complete` signal with aggregate quality; archived handoffs
- **Signal**: `workflow_complete`
- **Depends on**: Step 4
- **On failure**: retry (max 1); partial failure logged but does not block archive
- **Timeout**: 600s

## Dependencies

- Handoff file must exist at `.cex/runtime/handoffs/{MISSION}_n07.md` before workflow starts
- `.cex/runtime/decisions/` directory must be writable (Step 2 writes manifest)
- All referenced `spawn_configs` must be valid and present in `P12_orchestration/`
- Active nuclei (N01–N06) must be launchable via `bash _spawn/dispatch.sh solo|grid`
- N07 must have git credentials; Gemini nuclei (N01, N04) commit via N07 consolidation in Step 5

## Signals

- **`mission_planned`** — emitted by orchestrator after Step 1; payload: `{task_count, nucleus_assignments}`
- **`decisions_committed`** — emitted by orchestrator after Step 2; payload: `{decision_points_count, manifest_path}`
- **`spec_ready`** — emitted by orchestrator after Step 3; payload: `{artifact_count, spec_path}`
- **`{nucleus}_complete`** — emitted by each active nucleus after Step 4; payload: `{nucleus_id, artifacts_committed, quality_scores}`; Gemini nuclei signal is emitted by N07 during Step 5 consolidation
- **`workflow_complete`** — emitted by orchestrator after Step 5; payload: `{total_artifacts, avg_quality, failed_steps, archive_path}`
- **On error**: `{nucleus}_error` emitted on step failure; orchestrator retries once then skips and flags in consolidation report

## References

- Signal conventions: `signal-builder` (P12)
- Spawn configuration: `spawn-config-builder` (P12)
- Decision manifest: `.cex/runtime/decisions/decision_manifest.yaml`
- Dispatch command: `bash _spawn/dispatch.sh solo|grid`
- Consolidation protocol: `.claude/rules/n07-orchestrator.md` § Consolidate Protocol