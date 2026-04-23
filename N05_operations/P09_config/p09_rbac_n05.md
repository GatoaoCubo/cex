---
id: p09_rbac_n05
kind: rbac_policy
pillar: P09
title: "CEX Operations RBAC Policy (N05)"
version: "1.0"
created: "2026-04-17"
updated: "2026-04-17"
author: rbac-policy-builder
domain: operations access control
quality: 9.1
tags: [rbac, access_control, n05, operations, security, least_privilege]
tldr: "RBAC policy for CEX ops: defines read/write/execute/dispatch/stop rights across artifact files, config, runtime signals, PID files, git, and tools for 5 roles."
roles: [n07_orchestrator, nucleus_n01_n06, operator_human, ci_pipeline, guest_readonly]
resources: [artifact_files, config_files, runtime_signals, pid_files, git_operations, tool_execution]
references:
  - NIST SP 800-182
  - N05_operations/P09_config/con_permission_n05.md
density_score: 1.0
related:
  - p01_kc_orchestration_best_practices
  - p03_sp_permission_builder
  - bld_knowledge_card_permission
  - bld_examples_permission
  - p01_kc_cex_orchestration_architecture
  - p03_sp_orchestration_nucleus
  - p12_wf_auto_review
  - bld_memory_permission
  - p03_ins_permission
  - p11_qg_permission
---

## Policy Overview

Scope: N05_operations + all system shared resources.
Model: deny-by-default; each nucleus is an isolated tenant.
Lens: Gating Wrath -- every boundary is a hard gate; violations log and halt.

---

## Roles and Permissions

| Role | artifact_files | config_files | runtime_signals | pid_files | git_operations | tool_execution |
|---|---|---|---|---|---|---|
| n07_orchestrator | rw (N07_ only) | r | rwd | rwd | r | dispatch, stop, status, compile, doctor |
| nucleus_n01_n06 | rw (own N0X_ only) | r | rw (own only) | r | r, commit (own) | compile, signal |
| operator_human | rw (all) | rw | rwd | rwd | r, commit, push | all + force-stop, config-change |
| ci_pipeline | r | r | r | r | r | compile, doctor, system_test, sanitize |
| guest_readonly | r | r | none | none | r | none |

r=read, w=write, d=delete

---

## Resource Scope

| Resource | Path Pattern |
|---|---|
| artifact_files | `N0[0-7]_*/**/*.md` |
| config_files | `.cex/config/**`, `N0X_*/P09_config/**` |
| runtime_signals | `.cex/runtime/signals/**` |
| pid_files | `.cex/runtime/pids/**` |
| git_operations | `.git/**` (via CLI) |
| tool_execution | `_tools/*.py`, `_spawn/*.sh` |

---

## Deny Rules

| Rule ID | Subject | Resource | Condition | Action | Effect |
|---|---|---|---|---|---|
| deny_cross_nucleus_write | nucleus_n01_n06 | artifact_files | path outside own N0X_ dir | write | DENY |
| deny_self_score | nucleus, n07, ci | artifact_files | quality set non-null | write | DENY |
| deny_skip_f7 | nucleus, n07 | tool_execution | F7 GOVERN not executed | execute | DENY |
| deny_guest_mutate | guest_readonly | any mutable resource | always | write/delete/execute/dispatch/stop | DENY |
| deny_ci_mutate | ci_pipeline | artifact_files, config, signals, pids | always | write/delete/dispatch/stop | DENY |
| deny_nucleus_stop | nucleus_n01_n06 | tool_execution | always | stop | DENY |

**Rationale:**
- `deny_cross_nucleus_write`: nucleus tenant isolation -- hard boundary per N0X_ dir.
- `deny_self_score`: `quality: null` is invariant -- only peer review assigns scores.
- `deny_skip_f7`: F7 GOVERN is a non-negotiable gate; no artifact reaches F8 without it.
- `deny_guest_mutate`: guest surface is read-only, zero exceptions.
- `deny_ci_mutate`: CI validates; it never mutates production state.
- `deny_nucleus_stop`: process termination is exclusive to orchestrator and operator.

---

## Audit Trail

| Event | Severity | Log |
|---|---|---|
| Cross-nucleus write attempt | CRITICAL | `.cex/runtime/signals/rbac_violation.log` |
| Self-score attempt | HIGH | `.cex/runtime/signals/rbac_violation.log` |
| F7 skip attempt | HIGH | `.cex/runtime/signals/rbac_violation.log` |
| Unauthorized force-stop | HIGH | `.cex/runtime/signals/rbac_violation.log` |
| Config write by non-operator | MEDIUM | `.cex/runtime/signals/rbac_violation.log` |

Violations halt current operation. Log is append-only; archived quarterly.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_orchestration_best_practices]] | upstream | 0.29 |
| [[p03_sp_permission_builder]] | upstream | 0.27 |
| [[bld_knowledge_card_permission]] | upstream | 0.26 |
| [[bld_examples_permission]] | upstream | 0.26 |
| [[p01_kc_cex_orchestration_architecture]] | upstream | 0.26 |
| [[p03_sp_orchestration_nucleus]] | upstream | 0.25 |
| [[p12_wf_auto_review]] | downstream | 0.24 |
| [[bld_memory_permission]] | downstream | 0.23 |
| [[p03_ins_permission]] | upstream | 0.23 |
| [[p11_qg_permission]] | downstream | 0.23 |
