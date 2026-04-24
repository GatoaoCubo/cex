---
id: p07_trace_config_operations
kind: trace_config
8f: F8_collaborate
pillar: P07
title: Operations Observability Trace Configuration
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n05_operations
domain: observability-operations
quality: 9.1
tags: [trace_config, observability, operations, N05, telemetry, monitoring]
tldr: "Trace configuration for N05 operations covering deploy telemetry, test execution traces, health check monitoring, and signal flow observability."
density_score: 0.96
related:
  - p01_kc_trace_config
  - bld_collaboration_reasoning_trace
  - bld_config_reasoning_trace
  - p02_agent_deploy_ops
  - p01_kc_reasoning_trace
  - bld_collaboration_trace_config
  - bld_tools_reasoning_trace
  - p03_sp_deploy_ops
  - bld_memory_reasoning_trace
  - agent_card_n05
---

# Operations Trace Configuration

## Overview

This trace configuration defines observability instrumentation for all N05 operations. Every deploy, test execution, health check, and inter-nucleus signal is traceable. No operation runs in the dark.

## Boundary

This artifact defines the trace configuration for N05 operations, specifying how to instrument and monitor deploy, test, health, and signal activities. It is not a technical implementation of the tracing system, but rather the policy and structure for what should be traced, how data is captured, and how traces are stored and used.

## Related Kinds

- **observability_policies**: Defines the rules and criteria for when and how traces are used in decision-making processes.
- **telemetry_data_models**: Structures the format and content of the data captured in each trace, ensuring consistency across systems.
- **deployment_workflows**: Integrates trace configurations to monitor and log the execution of deployment steps.
- **signal_orchestration**: Relies on signal traces to ensure proper coordination and debugging of inter-nucleus communication.

## Trace Points

### Deploy Traces

| trace_id | trigger | data_captured | retention |
|------|---------|------|-------|
| DEPLOY_PRE | Pre-flight check start | env_vars_count, railway_toml_hash, migration_status | 90d |
| DEPLOY_EXEC | `railway up` invocation | build_duration_ms, nixpacks_cache_hit, service_name | 90d |
| DEPLOY_HEALTH | Health check poll | response_code, response_time_ms, health_json_hash | 90d |
| DEPLOY_POST | Post-deploy verification | middleware_order_valid, startup_steps_passed, rollback_ready | 90d |
| DEPLOY_ROLLBACK | Rollback triggered | trigger_reason, services_affected, rollback_duration_ms | 365d |

### Test Traces

| trace_id | trigger | data_captured | retention |
|------|---------|------|-------|
| TEST_UNIT | Unit eval start/end | test_count, pass_count, fail_count, duration_ms | 30d |
| TEST_E2E | E2E eval start/end | scenario_count, service_topology, fixture_setup_ms | 30d |
| TEST_SMOKE | Smoke eval execution | critical_path_count, pass_rate, deploy_context | 30d |
| TEST_BENCH | Benchmark execution | p50_ms, p95_ms, p99_ms, samples_count, baseline_delta | 90d |
| TEST_REGRESS | Regression check | baseline_version, current_version, delta_metrics | 90d |

### Signal Traces

| trace_id | trigger | data_captured | retention |
|------|---------|------|-------|
| SIG_EMIT | Signal written | source_nucleus, signal_type, quality_score, timestamp | 30d |
| SIG_RECV | Signal consumed | consumer_nucleus, signal_id, latency_ms | 30d |
| SIG_TIMEOUT | Signal poll timeout | expected_source, wait_duration_s, retry_count | 90d |

### Health Traces

| trace_id | trigger | data_captured | retention |
|------|---------|------|-------|
| HEALTH_POLL | Periodic health check | endpoint, response_ms, status_code, body_hash | 7d |
| HEALTH_DEGRADE | Health degradation | endpoint, previous_status, current_status, delta_ms | 90d |
| HEALTH_RECOVER | Health recovery | endpoint, downtime_ms, recovery_trigger | 90d |

## Sampling Configuration

| trace_category | sample_rate | reason |
|------|------|-------|
| DEPLOY_* | 100% | Every deploy is traced — no exceptions |
| TEST_* | 100% | Every test run is traced for regression detection |
| SIG_* | 100% | Signal flow is critical for orchestration debugging |
| HEALTH_POLL | 10% | High frequency, sample to control storage |
| HEALTH_DEGRADE | 100% | Always trace degradation events |

## Storage

| field | value |
|-------|-----|
| format | JSON lines (.jsonl) |
| location | `.cex/runtime/traces/` |
| rotation | Daily, compressed after 7 days |
| max_size | 100MB per trace category |
| cleanup | Auto-purge beyond retention period |

## Alert Rules

| rule | condition | action |
|------|-----------|--------|
| DEPLOY_SLOW | DEPLOY_EXEC duration > 120s | Signal N07 warning |
| HEALTH_DOWN | HEALTH_POLL 3 consecutive failures | Signal N07 + trigger rollback assessment |
| TEST_REGRESS | TEST_REGRESS delta > 10% degradation | Block deploy, flag for review |
| SIG_LOST | SIG_TIMEOUT retry_count > 3 | Signal N07 crash detection |

## 8F Pipeline Function

Primary function: **GOVERN**

The GOVERN function ensures trace configurations are enforced across all operations, including:
- Enforcing sampling rates (e.g., 100% for critical traces)
- Validating data capture completeness (e.g., ensuring all deploy phases are logged)
- Maintaining storage policies (e.g., 90d retention for deploy traces)
- Applying alert rules (e.g., triggering rollback assessments on health failures)
- Integrating with observability policies to align trace usage with operational goals

| Responsibility | Impact | Example |
|--------------|--------|--------|
| Sampling control | Reduces storage overhead | 10% sampling for HEALTH_POLL |
| Data validation | Ensures trace completeness | All deploy phases must be logged |
| Alert activation | Enables proactive remediation | Triggers rollback on health degradation |
| Policy alignment | Ensures trace usage consistency | Aligns with observability_policies |
| Storage management | Prevents data sprawl | Auto-purge beyond retention |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_trace_config]] | related | 0.32 |
| [[bld_collaboration_reasoning_trace]] | upstream | 0.29 |
| [[bld_config_reasoning_trace]] | downstream | 0.27 |
| [[p02_agent_deploy_ops]] | upstream | 0.27 |
| [[p01_kc_reasoning_trace]] | upstream | 0.27 |
| [[bld_collaboration_trace_config]] | downstream | 0.26 |
| [[bld_tools_reasoning_trace]] | upstream | 0.26 |
| [[p03_sp_deploy_ops]] | upstream | 0.26 |
| [[bld_memory_reasoning_trace]] | downstream | 0.26 |
| [[agent_card_n05]] | upstream | 0.25 |
