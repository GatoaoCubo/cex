---
id: n00_smoke_eval_manifest
kind: knowledge_card
8f: F3_inject
pillar: P07
nucleus: n00
title: "Smoke Eval -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, smoke_eval, p07, n00, archetype, template]
density_score: 0.99
related:
  - smoke-eval-builder
  - bld_schema_smoke_eval
  - bld_collaboration_smoke_eval
  - bld_memory_smoke_eval
  - p03_sp_smoke_eval_builder
  - bld_config_smoke_eval
  - bld_schema_reranker_config
  - bld_schema_eval_metric
  - bld_schema_integration_guide
  - bld_schema_unit_eval
---

<!-- 8F: F1=knowledge_card P07 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Smoke eval defines a quick sanity test (target: under 30 seconds) that validates the most critical system paths are operational after a deployment or configuration change. It does not test comprehensiveness; it tests that the system is alive and the critical happy path works. Smoke evals are run on every deploy, every nucleus boot, and as the first check before a full e2e eval.

## Pillar
P07 -- Evals

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `smoke_eval` |
| pillar | string | yes | Always `P07` |
| title | string | yes | System name + "Smoke Eval" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| target_system | string | yes | System or nucleus being smoke-tested |
| max_duration_seconds | int | yes | Hard timeout (must be <= 30) |
| critical_paths | list | yes | Named paths that MUST pass for smoke eval to pass |
| on_fail | enum | yes | alert / block_deploy / rollback |
| run_trigger | enum | yes | pre_deploy / post_deploy / on_boot / on_demand |

## When to use
- Verifying a nucleus is responsive immediately after boot
- Checking that a deployment did not break the critical happy path
- Running a fast gate before committing resources to a full e2e eval run

## Builder
`archetypes/builders/smoke_eval-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind smoke_eval --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N05 operations defines and runs smoke evals
- `{{SIN_LENS}}` -- Gating Wrath: if the smoke test fails, nothing else runs
- `{{TARGET_AUDIENCE}}` -- CI/CD pipeline and nucleus boot sequence
- `{{DOMAIN_CONTEXT}}` -- nucleus type, critical paths, deploy frequency

## Example (minimal)
```yaml
---
id: smoke_eval_cex_n01_boot
kind: smoke_eval
pillar: P07
nucleus: n05
title: "N01 Intelligence -- Boot Smoke Eval"
version: 1.0
quality: null
---
target_system: n01_intelligence
max_duration_seconds: 30
run_trigger: on_boot
on_fail: alert
critical_paths:
  - "8F intent resolution responds in < 5s"
  - "cex_doctor.py exits 0"
```

## Related kinds
- `e2e_eval` (P07) -- comprehensive test that follows successful smoke eval
- `unit_eval` (P07) -- component-level test; smoke_eval tests the integrated system
- `regression_check` (P07) -- continuous monitoring after smoke eval passes

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[smoke-eval-builder]] | related | 0.49 |
| [[bld_schema_smoke_eval]] | upstream | 0.48 |
| [[bld_collaboration_smoke_eval]] | related | 0.48 |
| [[bld_memory_smoke_eval]] | downstream | 0.47 |
| [[p03_sp_smoke_eval_builder]] | upstream | 0.42 |
| [[bld_config_smoke_eval]] | downstream | 0.38 |
| [[bld_schema_reranker_config]] | upstream | 0.38 |
| [[bld_schema_eval_metric]] | upstream | 0.38 |
| [[bld_schema_integration_guide]] | upstream | 0.37 |
| [[bld_schema_unit_eval]] | upstream | 0.37 |
