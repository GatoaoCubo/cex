---
id: con_path_config_n07
kind: path_config
pillar: P09
nucleus: n07
title: "Orchestrator Path Registry"
version: 1.0
quality: 8.7
tags: [path-config, orchestration, dispatch, runtime, filesystem]
scope: n07_orchestrator
paths:
  - handoffs_dir
  - signals_dir
  - pids_file
  - decision_manifest
  - plans_dir
  - archive_dir
  - n07_root
  - nuclei_roots
  - spawn_dir
  - boot_dir
  - tools_dir
  - kind_kcs_dir
  - builders_dir
  - kinds_meta
  - nucleus_models_config
  - task_files
platform: all
base_dir: "{{CEX_ROOT}}"
dir_count: 12
file_count: 4
author: path-config-builder
created: "2026-04-17"
updated: "2026-04-17"
tldr: "All filesystem paths N07 reads/writes for dispatch, signals, PIDs, decisions, plans, and knowledge."
description: "N07 orchestrator path registry: runtime coordination paths, nucleus roots, tools, builders, knowledge, task files."
related:
  - p01_kc_orchestration_best_practices
  - p02_bc_builder_nucleus
  - p09_path_{{SCOPE_SLUG}}
  - bld_schema_nucleus_def
  - p03_sp_orchestration_nucleus
  - bld_schema_path_config
  - bld_schema_model_provider
  - p01_ctx_cex_project
  - bld_schema_quickstart_guide
  - bld_schema_sandbox_config
---
<!-- 8F: F1=P09/path_config F2=path-config-builder F3=nucleus_def_n07 F4=reason F5=call F6=produce F7=govern F8=collaborate -->

## Overview

N07 (Orchestrating Sloth) must know where everything lives so it never searches.
This registry is the single source of truth for all filesystem paths N07 reads,
writes, or references during orchestration, dispatch, signal polling, and consolidation.
Consumers: N07 itself (read/write), boot scripts (read), dispatch.sh (read/write).

## Path Catalog: Runtime

| Path | Alias | Type | Default | Required | Created By | Read By | Notes |
|------|-------|------|---------|----------|------------|---------|-------|
| `.cex/runtime/handoffs/` | `handoffs_dir` | dir | `{{CEX_ROOT}}/.cex/runtime/handoffs/` | yes | N07 | N01-N06 | Nucleus task handoff files; one per dispatch |
| `.cex/runtime/signals/` | `signals_dir` | dir | `{{CEX_ROOT}}/.cex/runtime/signals/` | yes | N01-N06 | N07 | Completion signals; poll pattern: `signal_*_*.json` |
| `.cex/runtime/pids/spawn_pids.txt` | `pids_file` | file | `{{CEX_ROOT}}/.cex/runtime/pids/spawn_pids.txt` | yes | `dispatch.sh` | N07 | Format: `{wrapper_pid} {nucleus} {cli} {session_id} {ts} {worker_pids}` |
| `.cex/runtime/decisions/decision_manifest.yaml` | `decision_manifest` | file | `{{CEX_ROOT}}/.cex/runtime/decisions/decision_manifest.yaml` | yes | N07 (GDP) | N01-N06 | Subjective decisions locked before dispatch; nuclei read, never re-ask |
| `.cex/runtime/plans/` | `plans_dir` | dir | `{{CEX_ROOT}}/.cex/runtime/plans/` | yes | N07 | N07 | Mission plans per run; consumed by `cex_mission_runner.py` |
| `.cex/runtime/archive/` | `archive_dir` | dir | `{{CEX_ROOT}}/.cex/runtime/archive/` | yes | N07 | audit | Post-consolidation storage for completed signals and handoffs |

## Path Catalog: Nucleus Roots

| Path | Alias | Type | Default | Required | Notes |
|------|-------|------|---------|----------|-------|
| `N07_admin/` | `n07_root` | dir | `{{CEX_ROOT}}/N07_admin/` | yes | N07 own fractal root; 12 pillars mirrored from N00_genesis |
| `N01_intelligence/` | `nuclei_roots` | dir | `{{CEX_ROOT}}/N01_intelligence/` | yes | Sibling nucleus; research domain |
| `N02_marketing/` | `nuclei_roots` | dir | `{{CEX_ROOT}}/N02_marketing/` | yes | Sibling nucleus; marketing/copy domain |
| `N03_engineering/` | `nuclei_roots` | dir | `{{CEX_ROOT}}/N03_engineering/` | yes | Sibling nucleus; build/create domain |
| `N04_knowledge/` | `nuclei_roots` | dir | `{{CEX_ROOT}}/N04_knowledge/` | yes | Sibling nucleus; knowledge/docs domain |
| `N05_operations/` | `nuclei_roots` | dir | `{{CEX_ROOT}}/N05_operations/` | yes | Sibling nucleus; code/test/deploy domain |
| `N06_commercial/` | `nuclei_roots` | dir | `{{CEX_ROOT}}/N06_commercial/` | yes | Sibling nucleus; commercial/pricing domain |

## Path Catalog: Dispatch and Boot

| Path | Alias | Type | Default | Required | Notes |
|------|-------|------|---------|----------|-------|
| `_spawn/` | `spawn_dir` | dir | `{{CEX_ROOT}}/_spawn/` | yes | Contains `dispatch.sh`, `spawn_grid.ps1`, `spawn_solo.ps1` |
| `boot/` | `boot_dir` | dir | `{{CEX_ROOT}}/boot/` | yes | `cex.ps1` (N07), `n01.ps1`-`n06.ps1` (siblings); never pass task as CLI arg |
| `_tools/` | `tools_dir` | dir | `{{CEX_ROOT}}/_tools/` | yes | 152 CEX tools; `cex_compile.py`, `cex_doctor.py`, `cex_mission_runner.py`, etc. |

## Path Catalog: Knowledge

| Path | Alias | Type | Default | Required | Notes |
|------|-------|------|---------|----------|-------|
| `N00_genesis/P01_knowledge/library/kind/` | `kind_kcs_dir` | dir | `{{CEX_ROOT}}/N00_genesis/P01_knowledge/library/kind/` | yes | 424 kind KCs; loaded at F3 INJECT per build |
| `archetypes/builders/` | `builders_dir` | dir | `{{CEX_ROOT}}/archetypes/builders/` | yes | 259 builder directories, 13 ISOs each; F2 BECOME source |
| `.cex/kinds_meta.json` | `kinds_meta` | file | `{{CEX_ROOT}}/.cex/kinds_meta.json` | yes | 257-kind registry; F1 CONSTRAIN resolution source |
| `.cex/config/nucleus_models.yaml` | `nucleus_models_config` | file | `{{CEX_ROOT}}/.cex/config/nucleus_models.yaml` | yes | Per-nucleus fallback_chain; routing config for all 4 runtimes |

## Path Catalog: Task Files

| Path | Alias | Type | Default | Required | Notes |
|------|-------|------|---------|----------|-------|
| `n01_task.md` | `task_files` | file | `{{CEX_ROOT}}/n01_task.md` | yes | N01 task input; boot script reads at launch |
| `n02_task.md` | `task_files` | file | `{{CEX_ROOT}}/n02_task.md` | yes | N02 task input |
| `n03_task.md` | `task_files` | file | `{{CEX_ROOT}}/n03_task.md` | yes | N03 task input |
| `n04_task.md` | `task_files` | file | `{{CEX_ROOT}}/n04_task.md` | yes | N04 task input |
| `n05_task.md` | `task_files` | file | `{{CEX_ROOT}}/n05_task.md` | yes | N05 task input |
| `n06_task.md` | `task_files` | file | `{{CEX_ROOT}}/n06_task.md` | yes | N06 task input |

## Directory Hierarchy

```text
{{CEX_ROOT}}/
  .cex/
    runtime/
      handoffs/          -- nucleus task files (N07 writes, N01-N06 read)
      signals/           -- completion signals (N01-N06 write, N07 polls)
      pids/
        spawn_pids.txt   -- session-tagged process tracking
      decisions/
        decision_manifest.yaml  -- GDP locked decisions
      plans/             -- mission wave plans
      archive/           -- post-consolidation storage
    config/
      nucleus_models.yaml
    kinds_meta.json
  N00_genesis/
    P01_knowledge/
      library/
        kind/            -- 424 kind KCs
  N01_intelligence/      -- sibling nucleus root
  N02_marketing/         -- sibling nucleus root
  N03_engineering/       -- sibling nucleus root
  N04_knowledge/         -- sibling nucleus root
  N05_operations/        -- sibling nucleus root
  N06_commercial/        -- sibling nucleus root
  N07_admin/             -- own fractal root
  archetypes/
    builders/            -- 259 builder directories (13 ISOs each)
  _spawn/                -- dispatch.sh, spawn scripts
  _tools/                -- 152 CEX tools
  boot/                  -- boot scripts (cex.ps1, n01-n06.ps1)
  n01_task.md            -- per-nucleus task files (root, read at launch)
  n02_task.md
  n03_task.md
  n04_task.md
  n05_task.md
  n06_task.md
```

## Resolution Rules

| Rule | Description |
|------|-------------|
| `CEX_ROOT` expansion | Resolved to the repo root at runtime; default is git worktree root |
| Forward slashes | All paths stored with `/`; runtime normalizes to OS separator |
| Task file hygiene | N07 MUST clean `n0{1-6}_task.md` before and after dispatch to prevent stale task reads |
| Handoff mirroring | Handoff written to `handoffs/` AND copied to `n0X_task.md`; boot scripts read the task file |
| PID session tagging | `spawn_pids.txt` format: `{wrapper_pid} {nucleus} {cli} {session_id} {ts} {worker_pids}`; `stop` targets own session only |
| Signal polling | Non-blocking: `git log --since` + `dispatch.sh status`; NEVER block on `cex_signal_watch.py` in interactive N07 |
| Archive trigger | Signals and handoffs archived after wave consolidation; keeps `signals/` clean for next wave |
| Existence policy | `runtime/` subdirs: create-if-missing on first write; `kinds_meta.json` and `nucleus_models.yaml`: must-exist (crash if absent) |

## Rationale

N07 operates with Orchestrating Sloth as sin lens: expend zero effort searching for paths.
Every path is pre-registered here. At F3 INJECT, N07 loads this config and resolves all
references before producing handoffs. Missing paths signal a system configuration error,
not a search opportunity.

| Rationale | Detail |
|-----------|--------|
| Runtime separation | `.cex/runtime/` isolates volatile state from stable source; safe to wipe between missions |
| Task file at root | Boot scripts use simple relative reads; no path discovery overhead at nucleus boot |
| Builder ISOs in `archetypes/` | Shared across all nuclei; N07 references but never modifies |
| Session-tagged PIDs | Multiple N07 instances on same machine; `stop` kills only own session's children |
| Decision manifest bridge | GDP decisions captured once by N07, read by all dispatched nuclei; eliminates re-asking |

## Properties

| Property | Value |
|----------|-------|
| Kind | `path_config` |
| Pillar | P09 |
| Nucleus | N07 |
| Domain | orchestration, dispatch, runtime |
| Platform | all (Windows + Unix) |
| Pipeline | 8F (F1-F8) |
| Compiler | `_tools/cex_compile.py` |
| Quality target | peer-reviewed |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_orchestration_best_practices]] | upstream | 0.33 |
| [[p02_bc_builder_nucleus]] | upstream | 0.32 |
| [[p09_path_{{SCOPE_SLUG}}]] | sibling | 0.31 |
| [[bld_schema_nucleus_def]] | upstream | 0.31 |
| [[p03_sp_orchestration_nucleus]] | upstream | 0.31 |
| [[bld_schema_path_config]] | upstream | 0.30 |
| [[bld_schema_model_provider]] | upstream | 0.29 |
| [[p01_ctx_cex_project]] | upstream | 0.29 |
| [[bld_schema_quickstart_guide]] | upstream | 0.28 |
| [[bld_schema_sandbox_config]] | upstream | 0.28 |
