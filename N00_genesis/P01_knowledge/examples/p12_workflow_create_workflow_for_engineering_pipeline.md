---
id: p12_wf_engineering_pipeline
kind: workflow
pillar: P12
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "workflow-builder"
title: "Engineering Pipeline"
steps_count: 4
execution: mixed
agent_groups: [edison, tesla, reviewer, deployer]
timeout: 3600
retry_policy: per_step
depends_on: []
signals: [complete, error]
spawn_configs: [p12_spawn_edison_solo_build, p12_spawn_tesla_solo_test, p12_spawn_reviewer_solo_review, p12_spawn_deployer_solo_deploy]
domain: "engineering"
quality: 9.0
tags: [workflow, engineering, pipeline, ci-cd]
tldr: "4-step mixed workflow: edison builds and tesla tests in parallel (wave 1), reviewer gates quality (wave 2), deployer ships to production (wave 3)"
density_score: 0.89
related:
  - p12_wf_builder_8f_pipeline
  - p12_wf_creation_pipeline
  - p12_wf_create_orchestration_agent
  - p12_wf_brand_pipeline
  - p12_wf_orchestration_pipeline
  - p12_wf_knowledge_pipeline
  - bld_architecture_chain
  - tpl_instruction
  - bld_memory_workflow
  - bld_examples_workflow
---
## Purpose
Orchestrates the full software engineering pipeline from code compilation through production deployment. Wave 1 runs code build and test suite in parallel to minimize cycle time. Wave 2 gates on both completing before code review begins. Wave 3 deploys only after review passes. Per-step retry isolates transient failures without aborting healthy parallel steps.

## Steps

### Step 1: Code Build [edison]
- **Agent**: edison (opus)
- **Wave**: 1
- **Action**: Compile source code, resolve dependencies, and package build artifacts
- **Input**: Source code at git HEAD, `build.yaml` config
- **Output**: Compiled artifacts and build manifest in `build/dist/`
- **Signal**: `edison_build_complete` with build status and artifact paths
- **Depends on**: none (parallel with Step 2)
- **On failure**: retry (max 2), then abort

### Step 2: Test Suite [tesla]
- **Agent**: tesla (sonnet)
- **Wave**: 1
- **Action**: Execute unit and integration tests; produce coverage report
- **Input**: Source code at git HEAD, test configuration
- **Output**: Test results JSON and coverage report in `build/test-results/`
- **Signal**: `tesla_test_complete` with pass/fail counts and coverage percentage
- **Depends on**: none (parallel with Step 1)
- **On failure**: retry (max 1), then abort

### Step 3: Code Review [reviewer]
- **Agent**: reviewer (opus)
- **Wave**: 2
- **Action**: Evaluate diff against quality gates — security, style, complexity, and coverage threshold
- **Input**: Build artifacts (Step 1), test results (Step 2), git diff
- **Output**: Review report with approved/rejected verdict in `build/reviews/`
- **Signal**: `reviewer_review_complete` with verdict and findings list
- **Depends on**: Step 1, Step 2
- **On failure**: abort (review failure is a hard block)

### Step 4: Deploy [deployer]
- **Agent**: deployer (sonnet)
- **Wave**: 3
- **Action**: Push artifacts to production, verify health checks, record rollback checkpoint
- **Input**: Build artifacts (Step 1), approved review (Step 3)
- **Output**: Deployed release tag and checkpoint entry in `deploy/log/`
- **Signal**: `deployer_deploy_complete` with release tag and health check status
- **Depends on**: Step 3
- **On failure**: retry (max 1), then rollback to previous release and abort

## Dependencies
- git HEAD must be on a releasable branch (`main` or `release/*`)
- `build.yaml` must exist in repository root
- spawn_configs for all four agents must be registered and valid
- Production credentials must be present in `secret_config` before workflow starts

## Signals
- **Wave 1 complete**: `edison_build_complete` AND `tesla_test_complete` both emitted; Step 3 unblocked
- **Wave 2 complete**: `reviewer_review_complete` with `verdict: approved`; Step 4 unblocked
- **Workflow complete**: `engineering_pipeline_complete` with release tag and aggregate quality score
- **On error**: `{agent}_error` emitted; per-step retry attempted (max defined per step); escalate to orchestrator after exhaustion

## References
- signal-builder: completion signal naming conventions (`{agent}_complete`, `{agent}_error`)
- spawn-config-builder: agent launch parameters per step
- quality_gate: review threshold enforcement in Step 3

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_builder_8f_pipeline]] | sibling | 0.45 |
| [[p12_wf_creation_pipeline]] | sibling | 0.43 |
| [[p12_wf_create_orchestration_agent]] | sibling | 0.40 |
| [[p12_wf_brand_pipeline]] | sibling | 0.38 |
| [[p12_wf_orchestration_pipeline]] | sibling | 0.37 |
| [[p12_wf_knowledge_pipeline]] | sibling | 0.36 |
| [[bld_architecture_chain]] | upstream | 0.36 |
| [[tpl_instruction]] | upstream | 0.35 |
| [[bld_memory_workflow]] | upstream | 0.35 |
| [[bld_examples_workflow]] | upstream | 0.35 |
