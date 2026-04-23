---
id: n00_p12_kind_index
kind: knowledge_card
pillar: P12
nucleus: n00
title: "P12 Orchestration -- Kind Index"
version: 1.0
quality: 8.9
tags: [index, p12, archetype, n00]
density_score: 1.0
related:
  - bld_collaboration_kind
  - bld_collaboration_workflow
  - p12_wf_create_orchestration_agent
  - bld_architecture_kind
  - workflow-builder
  - p02_agent_creation_nucleus
  - p12_wf_admin_orchestration
  - bld_collaboration_crew_template
  - kind-builder
  - bld_collaboration_checkpoint
---

<!-- 8F: F1=knowledge_card P12 F2=knowledge-card-builder F3=kinds_meta+schema F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Master index of all 16 kinds in pillar P12. Reference for /mentor, nucleus builders, and the 8F pipeline.

## Pillar: P12 Orchestration
Workflow coordination and dispatch: DAGs, crew templates, handoffs, signals, schedules, and dispatch rules. The coordination layer that composes individual agents into coherent multi-agent systems.

## Kinds in P12

| Kind | Purpose | Primary Nucleus | Builder |
|------|---------|-----------------|---------|
| `checkpoint` | Workflow state snapshot | N07 | `checkpoint-builder` |
| `collaboration_pattern` | Multi-agent coordination topology | N07 | `collaboration_pattern-builder` |
| `crew_template` | CrewAI/AutoGen-style reusable crew blueprint (roles, process, memory,  | N07 | `crew_template-builder` |
| `dag` | Acyclic dependency graph | N07 | `dag-builder` |
| `dispatch_rule` | Dispatch rule (keyword > agent_group) | N07 | `dispatch_rule-builder` |
| `handoff` | Handoff instruction (task + context + commit) | N07 | `handoff-builder` |
| `renewal_workflow` | Renewal workflow with stages, owners, automation, escalation, contract | N07 | `renewal_workflow-builder` |
| `schedule` | Trigger temporal que inicia workflow | N07 | `schedule-builder` |
| `signal` | Inter-agent signal (complete, error, progress) | N07 | `signal-builder` |
| `spawn_config` | Spawn configuration (solo, grid, continuous) | N07 | `spawn_config-builder` |
| `team_charter` | Mission contract for a specific crew instance. Bridges GDP decisions ( | N07 | `team_charter-builder` |
| `visual_workflow` | GUI-based workflow editor configuration | N07 | `visual_workflow-builder` |
| `workflow` | Workflow (sequential/parallel steps) | N07 | `workflow-builder` |
| `pipeline_template` | Scenario-indexed agent pipeline recipe (new-feature, bug-fix, refactor, perf, infra) | N07 | `pipeline-template-builder` |
| `workflow_node` | Typed node in visual/programmatic workflow | N07 | `workflow_node-builder` |
| `workflow_primitive` | Workflow execution primitive (Step, Parallel, Loop, Condition, Router) | N07 | `workflow_primitive-builder` |

## Usage
```python
# Build any of these via 8F:
python _tools/cex_8f_runner.py "your intent" --kind {kind} --execute
```

## CoC Hierarchy Note
These 16 kinds follow the convention-over-configuration hierarchy: each instance
(N01-N07) inherits this schema and fills the variables for its sin lens.
N00_genesis holds the canonical archetype; nuclei hold the instantiated versions.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_kind]] | related | 0.46 |
| [[bld_collaboration_workflow]] | related | 0.39 |
| [[p12_wf_create_orchestration_agent]] | related | 0.38 |
| [[bld_architecture_kind]] | upstream | 0.37 |
| [[workflow-builder]] | related | 0.36 |
| [[p02_agent_creation_nucleus]] | upstream | 0.34 |
| [[p12_wf_admin_orchestration]] | related | 0.33 |
| [[bld_collaboration_crew_template]] | related | 0.33 |
| [[kind-builder]] | upstream | 0.32 |
| [[bld_collaboration_checkpoint]] | related | 0.31 |
