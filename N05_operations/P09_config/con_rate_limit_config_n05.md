---
id: con_rate_limit_config_n05
kind: rate_limit_config
8f: F1_constrain
pillar: P09
nucleus: n05
title: Ops Rate Limits
version: 1.0
quality: 9.0
tags: [config, rate-limit, operations, budget, provider]
density_score: 1.0
updated: "2026-04-17"
related:
  - p01_kc_rate_limit_config
  - bld_collaboration_cost_budget
  - bld_knowledge_card_rate_limit_config
  - rate-limit-config-builder
  - p11_qg_rate_limit_config
  - p01_kc_api_rate_limiting_retry_patterns
  - p03_sp_rate_limit_config_builder
  - bld_collaboration_rate_limit_config
  - cost-budget-builder
  - bld_examples_rate_limit_config
---
<!-- 8F: F1 constrain=P09/rate_limit_config F2 become=rate-limit-config-builder F3 inject=nucleus_def_n05+n05-operations+kc_rate_limit_config+P09_config+N05 provider control
     F4 reason=cost and throughput ceilings for ops tooling with rollback-safe throttling F5 call=apply_patch F6 produce=4320 bytes
     F7 govern=self-check headings+tables+gating_wrath+ascii+80_lines F8 collaborate=N05_operations/P09_config/con_rate_limit_config_n05.md -->

# Ops Rate Limits

## Purpose

| Field | Value |
|---|---|
| Intent | Define hard throughput and spend ceilings for N05 operational automation and provider calls. |
| Scope | CI diagnostics, deploy checks, review summarization, telemetry analysis, incident bursts. |
| Gating Wrath Lens | Limits exist to stop runaway spend and provider saturation before they become incidents. |
| Default Posture | Conservative ceilings with explicit burst allowances only for incident response. |
| Budget Rule | Production automation must have a declared budget cap. |

## Values

| Profile | Provider | RPM | TPM | Daily Budget USD | Concurrency | Backoff | Use Case |
|---|---|---|---|---|---|---|---|
| steady_review | shared_llm | 30 | 120000 | 12 | 2 | exponential_jitter | Normal code review and document checks. |
| release_gate | shared_llm | 20 | 90000 | 8 | 1 | exponential_jitter | Pre-release critical path work. |
| incident_burst | shared_llm | 45 | 180000 | 20 | 3 | exponential_jitter | Short-lived emergency analysis window. |
| telemetry_digest | analytics_api | 60 | 0 | 5 | 4 | fixed_30s | Metrics and log summarization. |
| secret_backend | vault_api | 15 | 0 | 2 | 1 | linear_5s | Secret lookup should be narrow and deliberate. |

## Guard Conditions

| Condition | Rule | Result |
|---|---|---|
| Budget >= 80% consumed | Drop to `steady_review` regardless of requested profile. | Preserve remaining budget for incident triage. |
| Repeated 429 within 5 min | Reduce RPM by 50% and open operator alert. | Avoid thundering herd escalation. |
| Incident declared | Permit `incident_burst` for max 60 minutes. | Time-box emergency throughput. |
| Provider degraded | Force concurrency to 1. | Favor correctness over speed. |
| Unrecognized profile | Deny execution. | No ad hoc rate class creation during runtime. |

## Rationale

| Design Choice | Why It Exists | Gating Wrath Effect |
|---|---|---|
| Named profiles | Operators choose from bounded, reviewed envelopes. | Prevents custom unsafe overrides. |
| Daily budget per profile | Spend control is part of runtime governance. | Stops invisible cost incidents. |
| Incident burst time limit | Emergencies justify more capacity, not unlimited capacity. | Contains blast radius. |
| Exponential jitter default | Smooths retries under provider pressure. | Reduces retry storms. |
| Deny unknown profiles | Runtime creativity is dangerous in controls. | Keeps limits predictable. |

## Example

| Scenario | Applied Profile | Result |
|---|---|---|
| Regular release evidence aggregation | `release_gate` | 20 RPM, 90k TPM, single concurrency |
| Major outage triage for 30 minutes | `incident_burst` | Higher ceiling, still budgeted and time-boxed |
| Budget exhausted to 82% | fallback | System drops to `steady_review` |

```yaml
provider: shared_llm
profiles:
  steady_review:
    rpm: 30
    tpm: 120000
    daily_budget_usd: 12
    concurrency: 2
    backoff_strategy: exponential_jitter
  release_gate:
    rpm: 20
    tpm: 90000
    daily_budget_usd: 8
    concurrency: 1
    backoff_strategy: exponential_jitter
  incident_burst:
    rpm: 45
    tpm: 180000
    daily_budget_usd: 20
    concurrency: 3
    max_duration_minutes: 60
```

## Properties

| Property | Value |
|---|---|
| Kind | `rate_limit_config` |
| Pillar | `P09` |
| Nucleus | `n05` |
| Control Surface | RPM, TPM, budget, concurrency, backoff |
| Safety Default | Conservative profiles only |
| Failure Mode | Unknown profile or exhausted budget results in deny or downgrade |
| Alerting | Trigger alert on repeated 429 or budget threshold crossing |
| Sin Lens | Gating Wrath: throughput is governed like a hazardous tool, not an entitlement. |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_rate_limit_config]] | related | 0.44 |
| [[bld_collaboration_cost_budget]] | downstream | 0.38 |
| [[bld_knowledge_card_rate_limit_config]] | upstream | 0.36 |
| [[rate-limit-config-builder]] | related | 0.35 |
| [[p11_qg_rate_limit_config]] | downstream | 0.35 |
| [[p01_kc_api_rate_limiting_retry_patterns]] | upstream | 0.34 |
| [[p03_sp_rate_limit_config_builder]] | related | 0.34 |
| [[bld_collaboration_rate_limit_config]] | downstream | 0.33 |
| [[cost-budget-builder]] | related | 0.31 |
| [[bld_examples_rate_limit_config]] | upstream | 0.31 |
