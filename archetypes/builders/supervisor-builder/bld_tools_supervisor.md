---
kind: tools
id: bld_tools_supervisor
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for supervisor production
quality: 9.0
title: "Tools Supervisor"
version: "1.0.0"
author: n03_builder
tags: [supervisor, builder, examples]
tldr: "Golden and anti-examples for supervisor construction, demonstrating ideal structure and common pitfalls."
domain: "supervisor construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_supervisor
  - bld_architecture_supervisor
  - p12_wf_admin_orchestration
  - p01_kc_orchestration
  - bld_instruction_supervisor
  - bld_tools_signal
  - p03_sp_director_builder
  - bld_tools_runtime_rule
  - bld_tools_workflow
  - p11_qg_director
---

# Tools: supervisor-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| cex_mission_runner.py | Autonomous orchestration: waves -> grid -> poll -> stop -> consolidate | Runtime execution of supervisor plan | ACTIVE |
| cex_coordinator.py | Synthesis gates between mission waves + workflow orchestration | Wave gate enforcement | ACTIVE |
| cex_signal_watch.py | Blocking signal poll: waits for builder completion, detects crashes | Signal monitoring | ACTIVE |
| _spawn/dispatch.sh | Solo and grid dispatch to nuclei (solo/grid/status/stop) | Builder dispatch | ACTIVE |
| signal_writer.py | Inter-nucleus signal emission (complete, error, retry) | Signal protocol | ACTIVE |
| cex_agent_spawn.py | Agent config validation + spawn pre-flight checks | Pre-dispatch validation | ACTIVE |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P08_architecture/_schema.yaml | Field definitions, supervisor constraints |
| Supervisor KC | P01_knowledge/library/kind/kc_supervisor.md | Domain knowledge, patterns, anti-patterns |
| Runtime Handoffs | .cex/runtime/handoffs/ | Per-builder mission context files |
| Runtime Signals | .cex/runtime/signals/ | Builder completion/error signals |
| Decision Manifest | .cex/runtime/decisions/decision_manifest.yaml | GDP decisions for subjective choices |
| Nucleus Models | .cex/config/nucleus_models.yaml | Model assignments per nucleus |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated supervisor validator exists yet. Check each QUALITY_GATES.md gate manually.
Key checks: YAML parses, id pattern match, kind == supervisor, quality == null,
builders list >= 2 entries, dispatch_mode in enum, llm_function == ORCHESTRATE,
no task execution logic in body, wave_topology documented, fallback_per_builder complete.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_supervisor]] | downstream | 0.41 |
| [[bld_architecture_supervisor]] | downstream | 0.39 |
| [[p12_wf_admin_orchestration]] | downstream | 0.38 |
| [[p01_kc_orchestration]] | upstream | 0.36 |
| [[bld_instruction_supervisor]] | upstream | 0.36 |
| [[bld_tools_signal]] | sibling | 0.35 |
| [[p03_sp_director_builder]] | upstream | 0.35 |
| [[bld_tools_runtime_rule]] | sibling | 0.34 |
| [[bld_tools_workflow]] | sibling | 0.34 |
| [[p11_qg_director]] | downstream | 0.34 |
