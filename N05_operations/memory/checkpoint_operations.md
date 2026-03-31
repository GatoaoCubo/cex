---
id: p10_ck_operations_release_gate
kind: checkpoint
pillar: P10
version: 3.0.0
created: 2026-03-30
updated: 2026-03-31
author: n05_operations
name: Operations Release Gate Checkpoint
workflow_ref: p12_wf_operations_nucleus
step: checkpoint_release_state
quality: null
tags: [checkpoint, N05, operations, release, rollback, validation]
tldr: Resume-safe checkpoint that captures operational evidence, validation status, rollback posture, and remaining risk before completion.
description: Stores the state required to resume an interrupted N05 review, debug, or deploy task without losing command history or release context.
state:
  task_scope: string
  changed_files: list[string]
  evidence_sources: list[string]
  failing_surface: string
  remediation_summary: string
  validation_commands: list[string]
  validation_status: string
  rollback_notes: string
  observability_notes: string
  residual_risk: string
resumable: true
ttl: 72h
parent_checkpoint: null
retry_count: 0
error: null
domain: operations-engineering
density_score: 0.95
---

# Overview

This checkpoint freezes the release state after remediation and validation work
so N05 can resume safely before compile, commit, signal, or deploy guidance.

## State Contract

| Key | Type | Description |
|-----|------|-------------|
| `task_scope` | string | short description of the review target or defect |
| `changed_files` | list[string] | files on the critical path for the task |
| `evidence_sources` | list[string] | tests, logs, workflow files, traces, or diffs used to reason |
| `failing_surface` | string | failing test, job, service, endpoint, or release gate |
| `remediation_summary` | string | concise description of the change made or finding established |
| `validation_commands` | list[string] | exact commands used to validate |
| `validation_status` | string | one of `pending`, `partial`, `passed`, `blocked`, `failed` |
| `rollback_notes` | string | how to reverse or contain the change |
| `observability_notes` | string | metrics, logs, alerts, or smoke checks to watch |
| `residual_risk` | string | unresolved uncertainty or follow-up risk |

## Resume Procedure

1. Load `p10_ck_operations_release_gate`.
2. Re-check git state and confirm `changed_files` still match the intended scope.
3. Re-run `validation_commands` if the worktree changed or `validation_status` is not `passed`.
4. Re-confirm rollback and observability notes for the current diff.
5. Continue with compile, commit, signal, and final operational summary.

## Lifecycle

- TTL: `72h`
- Cleanup trigger: successful completion signal or TTL expiry
- Safe to overwrite: yes, if it is the same task scope and same commit window
