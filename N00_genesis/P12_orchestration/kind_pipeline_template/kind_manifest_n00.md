---
quality: null
id: n00_pipeline_template_manifest
kind: knowledge_card
pillar: P12
nucleus: n00
title: "Pipeline Template -- Canonical Manifest"
version: 1.0
tags: [manifest, pipeline_template, p12, n00, archetype, hermes]
density_score: 1.0
related:
  - bld_schema_e2e_eval
  - bld_schema_reranker_config
  - bld_schema_dataset_card
  - bld_schema_quickstart_guide
  - bld_schema_usage_report
  - bld_schema_voice_pipeline
  - bld_schema_roi_calculator
  - bld_schema_crew_template
  - bld_schema_multimodal_prompt
  - bld_schema_integration_guide
updated: "2026-04-22"
---

<!-- 8F: F1=knowledge_card P12 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose

A pipeline_template is a scenario-indexed agent pipeline recipe for software engineering tasks.
It encodes the OpenCode-Hermes 7-scenario catalog: for each scenario (new_feature, bug_fix,
refactoring, etc.) the template defines the ordered stage sequence, model tier per stage,
revision loop policy, and mandatory quality gates (reviewer + tester). Pipeline templates are
instantiated with a team_charter for a specific codebase task, enabling N07 to dispatch the
correct stage sequence without rebuilding it from scratch.

## Pillar

P12 -- orchestration

## Schema (key fields)

| Field          | Type       | Required | Description |
|----------------|------------|----------|-------------|
| id             | string     | yes      | Unique artifact identifier, pattern: `p12_pt_{scenario_slug}` |
| kind           | string     | yes      | Always `pipeline_template` |
| pillar         | string     | yes      | Always `P12` |
| title          | string     | yes      | Human-readable name, pattern: "Pipeline: {Scenario Human}" |
| scenario       | enum       | yes      | One of 7 canonical values (see below) |
| stages         | array      | yes      | Ordered stage objects (role + model_tier + optional) |
| revision_loop  | object     | yes      | `max_iterations` (1-5) + `escalation_target` (user/nucleus/n07) |
| quality_gates  | object     | yes      | `mandatory`: [reviewer, tester] + `priority_order` |
| version        | semver     | yes      | Artifact version, follows semver |
| quality        | float/null | yes      | Peer-review score (null until reviewed) |
| tags           | array      | yes      | Must include `hermes_origin`, `pipeline`, scenario slug |
| upstream_source| string     | no       | Origin attribution (e.g., "1ilkhamov/opencode-hermes-multiagent") |

### Stage Object Schema

Each entry in the `stages` array follows this structure:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `role` | enum | yes | One of 15 canonical roles (finder, analyst, architect, etc.) |
| `model_tier` | enum | yes | `low` / `medium` / `high` / `xhigh` |
| `optional` | boolean | yes | If true, stage can be skipped without breaking the pipeline |

### Revision Loop Object Schema

| Field | Type | Range | Default | Description |
|-------|------|-------|---------|-------------|
| `max_iterations` | integer | 1-5 | 3 | Maximum revision attempts before escalation |
| `escalation_target` | enum | user/nucleus/n07 | user | Who receives unresolved failures |

### Quality Gates Object Schema

| Field | Type | Description |
|-------|------|-------------|
| `mandatory` | array | Stages that MUST pass; default `[reviewer, tester]` |
| `priority_order` | array | Gate evaluation priority; `[security, quality, implementation]` |

## When to use

- When a codebase task maps to one of the 7 canonical engineering scenarios
- When N07 dispatches a coding task and needs a deterministic stage sequence
- When integrating OpenCode-Hermes-style pipelines into CEX multi-agent orchestration
- When composing a `crew_template` that wraps a pipeline for team-based execution

## When NOT to use

- For non-engineering tasks (marketing, knowledge, commercial) -- use `crew_template` or `workflow`
- For arbitrary DAG workflows -- use `workflow` kind instead
- For single-step tasks -- use solo builder dispatch, no pipeline needed
- For ad-hoc experimentation -- pipelines are for repeatable, scenario-indexed recipes

## Builder

`archetypes/builders/pipeline-template-builder/`

```bash
# Build a pipeline template via 8F
python _tools/cex_8f_runner.py "your intent" --kind pipeline_template --execute

# Compile after creation
python _tools/cex_compile.py N0X_{domain}/P12_orchestration/p12_pt_{slug}.md
```

## 7 Canonical Scenarios

| Scenario | Key Stages | Stage count | Typical duration |
|----------|-----------|-------------|-----------------|
| new_feature | finder->analyst->architect->planner->coder->reviewer->tester->documenter | 8 | Long |
| new_feature_security | all new_feature + researcher + security gate | 10 | Longest |
| bug_fix_unknown | finder->debugger->fixer->reviewer->tester | 5 | Medium |
| bug_fix_known | finder->fixer->reviewer->tester | 4 | Short |
| refactoring | finder->analyst->refactorer->reviewer->tester | 5 | Medium |
| perf_opt | finder->analyst->optimizer->reviewer->tester | 5 | Medium |
| infra | finder->devops->reviewer->tester | 4 | Short |

### Scenario Selection Decision Tree

```
Is this a bug fix?
  |-- YES: Do you know the root cause?
  |     |-- YES -> bug_fix_known (4 stages)
  |     |-- NO  -> bug_fix_unknown (5 stages)
  |-- NO: Is this infrastructure/DevOps?
        |-- YES -> infra (4 stages)
        |-- NO: Is this restructuring existing code?
              |-- YES: Performance-related?
              |     |-- YES -> perf_opt (5 stages)
              |     |-- NO  -> refactoring (5 stages)
              |-- NO: New feature?
                    |-- YES: Security-sensitive?
                    |     |-- YES -> new_feature_security (10 stages)
                    |     |-- NO  -> new_feature (8 stages)
```

## Related kinds

- `crew_template` (P12) -- fixed multi-role team blueprint; pipeline_template is scenario recipe
- `team_charter` (P12) -- mission contract that instantiates this template for a specific task
- `workflow` (P12) -- arbitrary DAG; pipeline_template is a predefined linear recipe
- `workflow_node` (P12) -- single step; pipeline_template is the whole flow
- `revision_loop_policy` (P11) -- externalizes the revision_loop config
- `quality_gate` (P11) -- defines gate criteria referenced by pipeline quality_gates

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_e2e_eval]] | upstream | 0.37 |
| [[bld_schema_reranker_config]] | upstream | 0.37 |
| [[bld_schema_dataset_card]] | upstream | 0.37 |
| [[bld_schema_quickstart_guide]] | upstream | 0.37 |
| [[bld_schema_usage_report]] | upstream | 0.36 |
| [[bld_schema_voice_pipeline]] | upstream | 0.36 |
| [[bld_schema_roi_calculator]] | upstream | 0.36 |
| [[bld_schema_crew_template]] | upstream | 0.36 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.36 |
| [[bld_schema_integration_guide]] | upstream | 0.36 |
