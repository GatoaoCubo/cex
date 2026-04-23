---
kind: architecture
id: bld_architecture_smoke_eval
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of smoke_eval — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Smoke Eval"
version: "1.0.0"
author: n03_builder
tags: [smoke_eval, builder, examples]
tldr: "Golden and anti-examples for smoke eval construction, demonstrating ideal structure and common pitfalls."
domain: "smoke eval construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Architecture: smoke_eval in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, target, timeout, etc.) | smoke-eval-builder | active |
| critical_path | Minimal sequence of operations that must succeed for basic health | author | active |
| assertions | Fast boolean checks verifying each critical path step | author | active |
| timeout_limit | Maximum execution time (< 30 seconds) for fast-fail behavior | author | active |
| health_checks | Component-level liveness and readiness verifications | author | active |
| failure_action | What happens on smoke failure (block deploy, alert, rollback) | author | active |
## Dependency Graph
```
target_component  --tested_by-->  smoke_eval  --produces-->    pass_fail_result
smoke_eval        --consumed_by-->  CI_pipeline  --signals-->  smoke_event
smoke_eval        --depends-->      health_endpoint
```
| From | To | Type | Data |
|------|----|------|------|
| target_component | smoke_eval | data_flow | component under test provides health endpoints |
| smoke_eval | pass_fail_result | produces | boolean pass/fail with failure details |
| smoke_eval | CI_pipeline | consumes | pipeline runs smoke eval as pre-deploy gate |
| smoke_eval | smoke_event (P12) | signals | emitted on pass or fail with timing data |
| health_endpoint | smoke_eval | dependency | health checks require accessible endpoints |
| quality_gate (P11) | smoke_eval | dependency | gate may require smoke eval pass before promotion |
## Boundary Table
| smoke_eval IS | smoke_eval IS NOT |
|---------------|-------------------|
| A fast sanity check (< 30 seconds) for basic component health | A deep correctness test with full coverage (unit_eval P07) |
| Tests the critical path — minimal viable functionality | A full pipeline test across multiple components (e2e_eval P07) |
| Fast-fail: stops on first assertion failure | A performance measurement with benchmarks (benchmark P07) |
| Run before every deploy as a safety gate | A periodic quality review or calibration |
| Produces boolean pass/fail with failure details | A scored evaluation with weighted dimensions (scoring_rubric P07) |
| Scoped to one component or service | A system-wide health assessment |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Target | target_component, health_endpoint | Identify what is being tested and its health interface |
| Test | frontmatter, critical_path, assertions | Define the minimal checks and their pass criteria |
| Constraint | timeout_limit | Enforce fast execution for quick feedback |
| Response | failure_action, pass_fail_result | Define what happens on success or failure |
| Integration | CI_pipeline, quality_gate, smoke_event | Connect to deploy pipeline and signal results |
