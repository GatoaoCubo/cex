---
id: p12_wf_operations_nucleus
kind: workflow
pillar: P12
version: 3.0.0
created: 2026-03-30
updated: 2026-03-31
author: n05_operations
title: Operations Nucleus Workflow
steps_count: 7
execution_mode: sequential_with_validation_loops
error_recovery: retry_then_checkpoint_then_escalate
max_retries: 2
timeout_ms: 5400000
spawn_delay_ms: 1000
quality: null
tags: [workflow, N05, operations, testing, ci-cd, deployment]
tldr: End-to-end execution workflow for review, test, debug, CI/CD repair, and release validation with checkpoints and signal discipline.
density_score: 0.97
agent_nodes: [operations_nucleus]
signals: [triage_complete, evidence_captured, remediation_ready, validation_complete, checkpoint_saved, release_ready, error]
spawn_configs: [spawn_config_operations]
domain: operations-engineering
---

# Purpose

This workflow governs how N05 handles operational work where a wrong answer can
ship regressions, preserve flaky failures, or approve unsafe releases.

## Steps

### Step 1: intake_and_scope [operations_nucleus]

- **Action**: read handoff, inspect git status, identify target files, configs, and runtime surfaces
- **Input**: user request, handoff, repo state
- **Output**: bounded task scope and initial risk classification
- **Signal**: `triage_complete`
- **Depends on**: none

### Step 2: gather_evidence [operations_nucleus]

- **Action**: run review inspection or reproduction commands, collect failing tests, logs, workflow context, and config evidence
- **Input**: scoped target
- **Output**: confirmed failure mode, review findings, or explicit non-reproducibility record
- **Signal**: `evidence_captured`
- **Depends on**: Step 1

### Step 3: isolate_failure_surface [operations_nucleus]

- **Action**: narrow to the smallest relevant unit: function, test, workflow job, service, container, or deploy step
- **Input**: gathered evidence
- **Output**: remediation hypothesis and minimal-change plan
- **Signal**: `remediation_ready`
- **Depends on**: Step 2

### Step 4: remediate [operations_nucleus]

- **Action**: apply the smallest viable code, config, or workflow change
- **Input**: isolated failure surface
- **Output**: patch tied to the verified failure mode
- **Signal**: `fix_complete`
- **Depends on**: Step 3

### Step 5: validate_target_path [operations_nucleus]

- **Action**: run targeted tests, static checks, build validation, workflow sanity checks, or container verification that exercise the affected path
- **Input**: remediation patch
- **Output**: pass/fail evidence plus residual risk
- **Signal**: `validation_complete`
- **Depends on**: Step 4

### Step 6: checkpoint_release_state [operations_nucleus]

- **Action**: persist resumable operational state including commands, rollback, and unresolved risks
- **Input**: validated or partially validated state
- **Output**: checkpoint artifact ready for interruption-safe resume
- **Signal**: `checkpoint_saved`
- **Depends on**: Step 5

### Step 7: commit_compile_signal [operations_nucleus]

- **Action**: compile artifacts if applicable, review diff, commit required changes, emit completion signal, and summarize readiness
- **Input**: checkpointed state
- **Output**: committed and signaled operational outcome
- **Signal**: `release_ready`
- **Depends on**: Step 6

## Failure Handling

- Retry once for transient command or environment failures.
- If reproduction fails but the review surface is still clear, proceed in review mode and state the evidence gap.
- If validation depends on inaccessible infra or secrets, checkpoint the blocked state and report exact next commands.
- Never skip Step 5 on deploy-affecting changes without recording a blocker and rollback posture.
