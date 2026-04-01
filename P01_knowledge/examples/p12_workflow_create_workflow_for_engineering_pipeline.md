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
agent_nodes: [builder_agent, test_agent, security_agent, deploy_agent, monitor_agent]
timeout: 3600
retry_policy: per_step
depends_on: []
signals: [build_complete, test_complete, security_complete, deploy_complete, pipeline_complete, pipeline_error]
spawn_configs: [p12_spawn_builder_solo, p12_spawn_test_solo, p12_spawn_security_solo, p12_spawn_deploy_solo, p12_spawn_monitor_solo]
domain: "engineering"
quality: 8.7
tags: [workflow, engineering, pipeline, ci-cd, sequential]
tldr: "5-step sequential engineering pipeline: build → test → security scan → deploy → monitor with per-step retry and comprehensive error handling"
density_score: 0.92
---
## Purpose
Orchestrates a complete engineering pipeline from code build through production monitoring. Each step must complete successfully before the next begins, ensuring quality gates are enforced and failures are isolated. Supports rapid development cycles while maintaining production stability through comprehensive testing and monitoring.

## Steps

### Step 1: Code Build [builder_agent]
- **Agent**: builder_agent
- **Action**: Compile source code, resolve dependencies, and generate build artifacts
- **Input**: Source code changes from git repository
- **Output**: Compiled binaries and build artifacts in dist/ directory
- **Signal**: build_complete with build_id and artifact_paths
- **Depends on**: none

### Step 2: Test Suite [test_agent]
- **Agent**: test_agent
- **Action**: Execute unit tests, integration tests, and generate coverage report
- **Input**: Build artifacts from Step 1
- **Output**: Test results with coverage metrics and junit reports
- **Signal**: test_complete with coverage_percentage and test_status
- **Depends on**: Step 1

### Step 3: Security Scan [security_agent]
- **Agent**: security_agent
- **Action**: Run SAST/DAST scans, dependency vulnerability checks, and compliance validation
- **Input**: Build artifacts and test results from Steps 1-2
- **Output**: Security report with vulnerability assessment and compliance status
- **Signal**: security_complete with security_score and vulnerability_count
- **Depends on**: Step 2

### Step 4: Deploy [deploy_agent]
- **Agent**: deploy_agent
- **Action**: Deploy to staging environment, run smoke tests, promote to production
- **Input**: Validated artifacts from Steps 1-3
- **Output**: Deployed application with health checks passing
- **Signal**: deploy_complete with deployment_url and health_status
- **Depends on**: Step 3

### Step 5: Monitor [monitor_agent]
- **Agent**: monitor_agent
- **Action**: Initialize monitoring dashboards, set up alerts, verify metrics collection
- **Input**: Deployed application from Step 4
- **Output**: Active monitoring configuration with baseline metrics
- **Signal**: pipeline_complete with monitoring_dashboard_url
- **Depends on**: Step 4

## Dependencies
- Git repository with latest source code changes
- Build environment with required compilers and tools
- Test databases and mock services for integration testing
- Security scanning tools (SonarQube, OWASP ZAP, Snyk)
- Staging and production deployment environments
- Monitoring infrastructure (Prometheus, Grafana, alerting)

## Signals
- **On step complete**: {agent}_complete signal emitted with step-specific metrics and outputs
- **On pipeline complete**: pipeline_complete signal with aggregate quality score and deployment details
- **On error**: pipeline_error signal with failure details, automatic retry per step (max 1), escalate to operations team if retry fails