---
id: con_permission_n07
kind: permission
8f: F1_constrain
pillar: P09
nucleus: n07
title: "Orchestrator Permission Rules"
version: 1.0
quality: 8.9
tags: [permission, orchestration, rbac, dispatch, filesystem]
scope: "N07 orchestrator access to CEX runtime, sibling nuclei, tools, and processes"
roles: [n07_orchestrator, n07_autonomous, n07_consolidate]
read: "allow"
write: "conditional"
execute: "conditional"
tldr: "N07 has broad read access (all pillars, all nuclei) and narrow write access (runtime/, own fractal, task files only)."
domain: "orchestration, dispatch, wave planning, mission control"
created: "2026-04-17"
updated: "2026-04-17"
author: "permission-builder"
density_score: 0.88
inheritance: "n07_consolidate < n07_autonomous < n07_orchestrator"
escalation: "No escalation path -- N07 is top-level orchestrator. Cross-nuclei write requires explicit user GDP."
linked_artifacts:
  primary: "N07_admin/P08_architecture/nucleus_def_n07.md"
  related: [".claude/rules/n07-orchestrator.md", ".claude/rules/n07-autonomous-lifecycle.md", ".claude/rules/guided-decisions.md"]
related:
  - bld_knowledge_card_permission
  - bld_schema_permission
  - bld_memory_permission
  - bld_examples_permission
  - p03_sp_permission_builder
  - p11_qg_permission
  - bld_config_permission
  - p01_kc_permission
  - p03_sp_toolkit_builder
  - bld_knowledge_card_toolkit
---
<!-- 8F: F1=P09/permission F2=permission-builder F3=nucleus_def_n07+n07-orchestrator F4=reason F5=call F6=produce F7=govern F8=collaborate -->

## Purpose

N07 (Orchestrating Sloth) reads everything, writes narrowly. This permission document
defines the exact access boundary for N07 across filesystem paths, CEX tools, and
process management. The sin lens (Orchestrating Sloth) encodes this asymmetry:
maximum situational awareness, minimum footprint. Deny-by-default applies to all
resources not listed in the Allow List below.

## Scope

N07 controls: dispatch, wave planning, handoff injection, signal reading, GDP manifest
writing, and consolidation. It does NOT build artifacts (N03 domain), does NOT write
to sibling nuclei directories, and does NOT self-score. Any write outside own fractal
and runtime/ paths requires explicit user authorization via GDP.

## Filesystem Permissions

| Path Pattern | Read | Write | Execute | Rationale |
|---|---|---|---|---|
| .cex/runtime/handoffs/ | allow | allow | deny | N07 writes handoffs for nuclei pre-dispatch |
| .cex/runtime/signals/ | allow | deny | deny | N07 reads completion signals; nuclei write them |
| .cex/runtime/pids/ | allow | allow | deny | N07 tracks spawn PIDs per session |
| .cex/runtime/decisions/ | allow | allow | deny | N07 writes GDP decision manifest |
| .cex/runtime/plans/ | allow | allow | deny | N07 writes mission wave plans |
| .cex/runtime/archive/ | allow | allow | deny | N07 archives completed wave signals |
| .cex/config/ | allow | deny | deny | Config is read-only at runtime |
| .cex/kinds_meta.json | allow | deny | deny | Kind registry is read-only |
| N07_admin/ | allow | allow | deny | Own fractal -- full read/write |
| n07_task.md | allow | allow | deny | Boot task file for own session |
| n0{1-6}_task.md | allow | allow | deny | Task file injection for sibling nuclei |
| N0{1-6}_*/ | allow | deny | deny | Read sibling nuclei, never write |
| N00_genesis/ | allow | deny | deny | Archetype layer -- read-only |
| archetypes/ | allow | deny | deny | Builder ISOs -- read-only reference |
| _spawn/ | allow | deny | allow | Execute dispatch.sh scripts |
| _tools/ | allow | deny | allow | Execute CEX Python tools |
| _docs/ | allow | deny | deny | Specs and docs -- read-only |
| .claude/rules/ | allow | deny | deny | Rules are read-only at runtime |
| .cex/runtime/ (other) | allow | deny | deny | Unlisted runtime paths: deny write |

## Tool Permissions

| Tool | Allowed | Conditions | Rationale |
|---|---|---|---|
| dispatch.sh solo/grid/status/stop | yes | own session only | Primary dispatch mechanism |
| cex_doctor.py | yes | read + report only | Health checks post-consolidation |
| cex_compile.py | yes | own artifacts only | Compile handoffs and plans |
| cex_score.py | no | never | N07 never self-scores; peer review only |
| cex_evolve.py | yes | invoke only, not target | Trigger improvement loop on artifacts |
| signal_writer.py | yes | orchestrator signals only | Write completion/start signals |
| cex_mission_runner.py | yes | invoke + monitor | Autonomous mission orchestration |
| cex_signal_watch.py | yes | headless/background only | Never block interactive session |
| cex_intent_resolver.py | yes | read output only | Input transmutation at F1 |
| cex_router.py | yes | query only | Provider routing decisions |
| cex_quota_check.py | yes | pre-dispatch probe only | Quota pre-flight before grid |
| cex_prompt_cache.py | yes | read only | Load pre-compiled builder context |
| cex_crew.py | yes | list/show/run | Composable crew orchestration |
| cex_hooks.py | yes | post-tool-use, stop | Native hook entrypoints |
| cex_hygiene.py | no | never direct | Hygiene delegated to N05 |
| brand_*.py | yes | read/validate only | Brand context injection at F3 |

## Process Permissions

| Action | Allowed | Scope | Conditions | Rationale |
|---|---|---|---|---|
| spawn nucleus | yes | own session only | Max 6 parallel per grid | Grid dispatch limit |
| kill process | yes | own session PIDs only | taskkill /F /T required | Tree-kill prevents orphans |
| kill all nuclei | conditional | all sessions | Requires explicit --all flag | Dangerous -- affects other N07s |
| kill --dry-run | yes | preview only | No destruction | Safe audit before kill |
| read git log | yes | full repo | No limit | Wave completion detection |
| git add + commit | yes | own artifacts + consolidation | Never force-push | Post-consolidation only |
| git push | deny | — | Never | User initiates push |
| read process list | yes | full system | For orphan detection | PID tree walking |
| write PID file | yes | .cex/runtime/pids/ | Own session entries only | Session-tagged tracking |

## Access Matrix

| Role | Read (all paths) | Write (runtime+own) | Execute (tools) | Conditions |
|---|---|---|---|---|
| n07_orchestrator | allow | allow | allow | GDP decisions gate subjective writes |
| n07_autonomous | allow | allow | allow | Manifest must exist; no user prompts |
| n07_consolidate | allow | conditional | allow | Write only to archive + consolidation commit |

## Allow List

1. n07_orchestrator: read all N0{1-6} artifacts -- situational awareness for dispatch planning
2. n07_orchestrator: write .cex/runtime/handoffs/ -- task injection is the primary N07 output
3. n07_orchestrator: write n0{1-6}_task.md -- boot task delivery to sibling nuclei
4. n07_orchestrator: write .cex/runtime/decisions/ -- GDP manifest persists user decisions
5. n07_autonomous: execute _spawn/dispatch.sh -- grid dispatch requires execute permission
6. n07_autonomous: execute _tools/*.py -- CEX tools are safe to invoke
7. n07_consolidate: read .cex/runtime/signals/ -- detect nucleus completion before consolidating
8. n07_consolidate: write .cex/runtime/archive/ -- archive completed wave signals post-consolidation
9. n07_consolidate: git add + commit -- own artifacts and consolidation report only

## Deny List

1. ALL roles: write N0{1-6}_*/ -- sibling nuclei own their fractals; N07 never modifies them
2. ALL roles: write archetypes/ -- builder ISOs are version-controlled, never runtime-modified
3. ALL roles: write N00_genesis/ -- archetype layer is immutable at runtime
4. ALL roles: execute cex_score.py on own output -- self-scoring violates quality gate integrity
5. ALL roles: git push -- push is always a human decision
6. ALL roles: write .cex/config/ -- config is locked at session start
7. ALL roles: write .claude/rules/ -- rules are governance artifacts, not runtime state
8. n07_consolidate: spawn new nuclei -- consolidation phase is termination, not dispatch

## Audit

| Event | Logged | Retention | Alert |
|---|---|---|---|
| Handoff written to .cex/runtime/handoffs/ | yes | 30 days | none |
| Task file (n0X_task.md) overwritten | yes | 30 days | if overwrite within active session |
| GDP manifest written | yes | 90 days | none |
| Nucleus spawned (PID recorded) | yes | session lifetime | none |
| Process killed (taskkill) | yes | 30 days | if PID not in own session |
| Write attempted to denied path | yes | 60 days | immediate -- violation signal |
| cex_score.py invoked on own output | yes | 60 days | immediate -- quality gate breach |
| --all flag used for kill | yes | 90 days | always -- cross-session impact |

## Escalation Rules

| Situation | Escalation Path | Approver | Duration |
|---|---|---|---|
| Write needed to sibling nucleus | GDP decision point -- ask user | User | per-session |
| Write needed to archetypes/ | full PR review + manual merge | User + peer reviewer | permanent |
| Kill across sessions (--all) | explicit user command required | User | one-time |
| Expand tool execute list | update this artifact + compile | User via GDP | permanent |

N07 has no escalation recipient above itself. All boundary expansions require explicit
user authorization via GDP before execution. Document expansions in
`.cex/runtime/decisions/decision_manifest.yaml`.

## Rationale

The Orchestrating Sloth sin lens encodes the principle: N07's leverage comes from
coordination, not production. Wide read access enables accurate dispatch decisions.
Narrow write access prevents accidental clobbering of sibling work. The asymmetry is
structural: a nucleus that writes everywhere is an orchestrator that can corrupt any
artifact in the system. Deny-by-default on write preserves the integrity of the
eight-nucleus trust model.

## Properties

| Property | Value |
|---|---|
| Kind | permission |
| Pillar | P09 |
| Nucleus | N07 |
| Domain | orchestration, dispatch, wave planning |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Quality target | peer-reviewed |
| Density target | 0.85+ |
| Max bytes | 3072 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_permission]] | upstream | 0.52 |
| [[bld_schema_permission]] | upstream | 0.49 |
| [[bld_memory_permission]] | downstream | 0.48 |
| [[bld_examples_permission]] | upstream | 0.48 |
| [[p03_sp_permission_builder]] | upstream | 0.40 |
| [[p11_qg_permission]] | downstream | 0.38 |
| [[bld_config_permission]] | related | 0.33 |
| [[p01_kc_permission]] | related | 0.31 |
| [[p03_sp_toolkit_builder]] | upstream | 0.30 |
| [[bld_knowledge_card_toolkit]] | upstream | 0.28 |
