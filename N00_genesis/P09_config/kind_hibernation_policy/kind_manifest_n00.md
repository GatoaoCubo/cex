---
id: n00_hibernation_policy_manifest
kind: knowledge_card
pillar: P09
nucleus: n00
title: "Hibernation Policy -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, hibernation_policy, p09, n00, archetype, hermes]
density_score: 1.0
related:
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - bld_schema_sandbox_spec
  - bld_schema_usage_report
  - bld_schema_benchmark_suite
  - bld_schema_bugloop
  - bld_schema_rbac_policy
  - bld_schema_search_strategy
  - bld_schema_dataset_card
  - bld_schema_thinking_config
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A hibernation_policy defines the rules under which an idle serverless workload (Daytona, Modal, Singularity) suspends itself to eliminate idle-time cost. It declares the idle trigger (no activity or no requests for N seconds), the wake-on conditions (incoming request, scheduled cron, explicit signal), state persistence settings (memory/disk snapshot), and the SLA for cold-start wake latency. Owned by N05 Operations; configured in the `environments/` directory alongside `terminal_backend`.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier (p09_hp_{{backend}}) |
| kind | string | yes | Always `hibernation_policy` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable policy name |
| target_backend | enum | yes | daytona \| modal \| singularity \| generic |
| idle_trigger.type | enum | yes | no_activity_seconds \| no_requests_seconds \| explicit_signal |
| idle_trigger.threshold_seconds | integer | yes | Seconds of idle before hibernation fires (min 60) |
| wake_on | list | yes | Conditions that wake the workload (incoming_request, scheduled_cron, explicit_signal) |
| state_persistence.keep_memory | bool | yes | Whether in-process memory is snapshotted before sleep |
| state_persistence.snapshot_disk | bool | yes | Whether filesystem is checkpointed |
| state_persistence.checkpoint_cadence_seconds | integer | no | How often to write checkpoints while active (null = on-hibernate only) |
| wake_latency_sla_seconds | integer | yes | Maximum acceptable cold-start latency in seconds |
| cost_savings_estimate_pct | integer | no | Estimated idle-cost reduction percentage (0-100) |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |

## When to use
- Configuring serverless backends (Modal, Daytona) to hibernate after idle periods
- Reducing idle-time cost on GPU workloads (singularity HPC clusters)
- Declaring cold-start SLA requirements so orchestrators route time-sensitive tasks to warm instances
- Pairing with `terminal_backend` to fully describe both WHERE code runs and WHEN it sleeps

## Boundary
- NOT `cost_budget` -- cost_budget is a spend CAP (max USD); hibernation_policy is a cost REDUCTION strategy via sleep
- NOT `rate_limit_config` -- rate_limit_config governs throughput (RPM/TPM); hibernation_policy governs idle-state
- NOT `terminal_backend` -- terminal_backend declares WHAT execution environment; hibernation_policy declares WHEN it sleeps
- NOT `runtime_rule` -- runtime_rule handles timeouts and retries during active execution; hibernation_policy handles inactivity

## Builder
`archetypes/builders/hibernation-policy-builder/`

Run: `python _tools/cex_8f_runner.py "configure hibernation for modal backend" --kind hibernation_policy --execute`

## Template variables (open for instantiation)
- `{{backend}}` -- backend type slug (daytona, modal, singularity, generic)
- `{{idle_seconds}}` -- idle threshold before hibernation (default 900)
- `{{wake_latency}}` -- max wake latency SLA in seconds (default 10)

## Example (minimal -- modal with 15-min idle threshold)
```yaml
---
id: p09_hp_modal
kind: hibernation_policy
pillar: P09
title: "Hibernation Policy: modal"
target_backend: modal
idle_trigger:
  type: no_requests_seconds
  threshold_seconds: 900
wake_on:
  - incoming_request
  - scheduled_cron
state_persistence:
  keep_memory: true
  snapshot_disk: false
  checkpoint_cadence_seconds: null
wake_latency_sla_seconds: 10
cost_savings_estimate_pct: 70
version: 1.0.0
quality: null
tags: [hermes_origin, hibernation, serverless, cost]
---
```

## Related kinds
- `terminal_backend` (P09) -- declares the execution environment this policy governs
- `cost_budget` (P09) -- spend cap that works alongside hibernation cost reduction
- `runtime_rule` (P09) -- active-execution timeouts; hibernation_policy handles inactivity
- `secret_config` (P09) -- credentials for backend API that issues hibernate/wake calls

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | upstream | 0.40 |
| [[bld_schema_integration_guide]] | upstream | 0.40 |
| [[bld_schema_sandbox_spec]] | upstream | 0.39 |
| [[bld_schema_usage_report]] | upstream | 0.39 |
| [[bld_schema_benchmark_suite]] | upstream | 0.38 |
| [[bld_schema_bugloop]] | downstream | 0.38 |
| [[bld_schema_rbac_policy]] | upstream | 0.38 |
| [[bld_schema_search_strategy]] | upstream | 0.37 |
| [[bld_schema_dataset_card]] | upstream | 0.37 |
| [[bld_schema_thinking_config]] | upstream | 0.37 |
