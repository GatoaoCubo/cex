---
id: p12_wf_engineering_pipeline
kind: workflow
pillar: P12
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "workflow-builder"
title: "Engineering Pipeline Workflow"
steps_count: 5
execution: sequential
agent_nodes: [reviewer, tester, builder, deployer, monitor]
timeout: 3600
retry_policy: per_step
depends_on: []
signals: [complete, error, pipeline_complete]
spawn_configs: [p12_spawn_reviewer_solo, p12_spawn_tester_solo, p12_spawn_builder_solo, p12_spawn_deployer_solo, p12_spawn_monitor_solo]
domain: "engineering"
quality: 8.7
tags: [workflow, engineering, pipeline, sequential, ci-cd]
tldr: "5-step sequential engineering pipeline: code review → testing → build → deploy → monitor with per-step retry and completion signals"
density_score: 0.88
---
## Purpose
Orchestrates a complete engineering pipeline from code review through production deployment and monitoring. Each step must complete successfully before the next begins, ensuring quality gates are met at every stage. Failed steps trigger per-step retry with escalation to orchestrator on repeated failure.

## Steps

### Step 1: Code Review [reviewer]
- **Agent**: reviewer (sonnet)
- **Action**: Review code changes for quality, security, and engineering best practices
- **Input**: git diff from feature branch, coding standards checklist
- **Output**: review report with pass/fail decision, feedback comments
- **Signal**: review_complete with quality score
- **Depends on**: none (first step)

### Step 2: Unit Testing [tester]
- **Agent**: tester (opus)
- **Action**: Execute unit test suite and generate coverage report
- **Input**: reviewed code from Step 1, existing test suite
- **Output**: test results with pass/fail status, coverage metrics
- **Signal**: tests_complete with coverage percentage
- **Depends on**: Step 1

### Step 3: Build [builder]
- **Agent**: builder (opus)
- **Action**: Compile code, generate artifacts, run static analysis
- **Input**: tested code from Step 2, build configuration
- **Output**: compiled artifacts, build logs, static analysis report
- **Signal**: build_complete with artifact checksums
- **Depends on**: Step 2

### Step 4: Deploy [deployer]
- **Agent**: deployer (codex)
- **Action**: Deploy artifacts to target environment with rollback capability
- **Input**: built artifacts from Step 3, deployment configuration
- **Output**: deployment status, environment health check results
- **Signal**: deploy_complete with deployment URL
- **Depends on**: Step 3

### Step 5: Monitor [monitor]
- **Agent**: monitor (sonnet)
- **Action**: Verify deployment health and establish monitoring baselines
- **Input**: deployed application from Step 4, monitoring configuration
- **Output**: health dashboard, alert configuration, baseline metrics
- **Signal**: pipeline_complete with monitoring URLs
- **Depends on**: Step 4

## Dependencies
- Feature branch must exist with committed changes ready for review
- Target deployment environment must be accessible and configured
- Test suite must exist with minimum coverage thresholds defined
- Build configuration and deployment scripts must be present in repository

## Signals
- **On step complete**: {agent}_complete signal emitted with step-specific metrics (see signal-builder)
- **On workflow complete**: pipeline_complete signal with aggregate quality score and deployment URLs
- **On error**: {agent}_error signal with failure details, per-step retry (max 1), escalate to orchestrator on repeated failure