---
id: con_env_config_n05
kind: env_config
pillar: P09
nucleus: n05
title: Ops Env Contract
version: 1.0
quality: 9.0
tags: [config, env, operations, ci, deploy]
density_score: 1.0
related:
  - bld_schema_env_config
  - bld_examples_kind
  - bld_schema_sandbox_config
  - bld_schema_usage_report
  - bld_schema_safety_policy
  - bld_schema_dataset_card
  - bld_schema_quickstart_guide
  - bld_schema_reranker_config
  - bld_schema_pitch_deck
  - bld_schema_benchmark_suite
---
<!-- 8F: F1 constrain=P09/env_config F2 become=env-config-builder F3 inject=nucleus_def_n05+n05-operations+kc_env_config+P09_config+N05 env examples
     F4 reason=environment contract with strict precedence and fail-closed validation F5 call=apply_patch F6 produce=5202 bytes
     F7 govern=self-check headings+tables+gating_wrath+ascii+80_lines F8 collaborate=N05_operations/P09_config/con_env_config_n05.md -->

# Ops Env Contract

## Purpose

| Field | Value |
|---|---|
| Intent | Define the environment variables required for N05 review, CI, deploy, and rollback operations. |
| Scope | Local validation, CI runners, staging deploy jobs, production release workflows. |
| Gating Wrath Lens | Missing or malformed variables halt execution before risky actions begin. |
| Default Posture | Fail closed and mask sensitive values in all logs. |
| Precedence | runtime env -> secure injection -> checked defaults; no silent fallback to unsafe values. |

## Values

| Variable | Type | Required | Sensitive | Default | Validation | Action On Failure |
|---|---|---|---|---|---|---|
| CEX_ENV | string | yes | no | none | `dev|staging|prod` | Abort run on unknown environment. |
| CEX_RELEASE_CHANNEL | string | yes | no | `manual` | `manual|canary|full` | Block deploy on invalid channel. |
| CEX_GATE_STRICT | boolean | yes | no | `true` | boolean | Treat invalid value as hard stop. |
| CEX_CI_SHA | string | yes | no | none | non-empty digest or commit | Refuse unverifiable artifact. |
| CEX_DEPLOY_WINDOW_UTC | string | yes | no | none | `HH:MM-HH:MM` | Deny out-of-window release. |
| CEX_SMOKE_TIMEOUT_SEC | integer | yes | no | `300` | 60..900 | Avoid endless hangs. |
| CEX_ROLLBACK_PLAN_REF | string | yes | no | none | non-empty URI-like ref | No plan, no deploy. |
| CEX_ALERT_WEBHOOK | string | no | yes | none | https URL | Disable notifications only with documented exception. |
| CEX_PROVIDER_PROFILE | string | yes | no | `balanced` | `balanced|cost_guarded|latency_guarded` | Reject unknown provider policy. |
| CEX_SECRET_BACKEND | string | yes | no | `vault` | `vault|railway|env` | Force supported secret retrieval path. |

## Groups

| Group | Variables | Why |
|---|---|---|
| Identity | `CEX_ENV`, `CEX_CI_SHA` | Tie every run to an environment and immutable artifact. |
| Gate Control | `CEX_GATE_STRICT`, `CEX_DEPLOY_WINDOW_UTC`, `CEX_RELEASE_CHANNEL` | Prevent accidental fast paths. |
| Recovery | `CEX_ROLLBACK_PLAN_REF`, `CEX_SMOKE_TIMEOUT_SEC` | Limit blast radius and define escape route. |
| Integrations | `CEX_ALERT_WEBHOOK`, `CEX_SECRET_BACKEND`, `CEX_PROVIDER_PROFILE` | Keep operator notifications and provider choice explicit. |

## Resolution Rules

| Rule | Description | Gating Effect |
|---|---|---|
| Required first | Validate required vars before any network or deploy action. | Cuts unsafe partial startup. |
| Secret masking | Any variable marked sensitive is redacted in logs and summaries. | Prevents accidental leakage under pressure. |
| No implicit prod | If `CEX_ENV` is absent, do not infer production or staging. | Stops mistaken targeting. |
| Window enforcement | Deploys outside `CEX_DEPLOY_WINDOW_UTC` must terminate before rollout. | Protects support coverage. |
| Immutable artifact binding | `CEX_CI_SHA` must match artifact metadata. | Blocks drift between review and release. |

## Rationale

| Design Choice | Why It Exists | Gating Wrath Effect |
|---|---|---|
| Strict boolean gate | `CEX_GATE_STRICT=true` by default keeps policy enforcement on. | Safe by default. |
| Explicit release channel | Operators must state manual, canary, or full. | Eliminates accidental broad rollout. |
| Rollback ref in env | The run cannot start if recovery is undefined. | Recovery becomes mandatory input. |
| Secret backend enum | Only approved paths are allowed. | Removes ad hoc secret access. |
| Webhook optional but validated | Notification can be disabled only knowingly. | Makes observability gaps visible. |

## Example

| Scenario | Effective Outcome |
|---|---|
| `CEX_ENV=prod` and missing rollback ref | Deployment aborted before image promotion. |
| `CEX_RELEASE_CHANNEL=canary` with valid window | Deploy job may continue to staged rollout logic. |
| `CEX_GATE_STRICT=false` in prod | Denied unless exception ticket exists outside this config. |

```env
CEX_ENV=prod
CEX_RELEASE_CHANNEL=canary
CEX_GATE_STRICT=true
CEX_CI_SHA=9f31b4d2
CEX_DEPLOY_WINDOW_UTC=13:00-17:00
CEX_SMOKE_TIMEOUT_SEC=300
CEX_ROLLBACK_PLAN_REF=runbook://ops/rollback/api-blue-green
CEX_PROVIDER_PROFILE=balanced
CEX_SECRET_BACKEND=vault
```

## Properties

| Property | Value |
|---|---|
| Kind | `env_config` |
| Pillar | `P09` |
| Nucleus | `n05` |
| Scope | CI, deploy, rollback, smoke validation |
| Secret Handling | Mask sensitive values, store only refs here. |
| Enforcement Point | Pre-flight bootstrap before any mutable action. |
| Failure Mode | Hard stop with operator-readable error and owner action. |
| Sin Lens | Gating Wrath: no missing variable gets a soft warning in production. |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_env_config]] | upstream | 0.44 |
| [[bld_examples_kind]] | upstream | 0.41 |
| [[bld_schema_sandbox_config]] | upstream | 0.38 |
| [[bld_schema_usage_report]] | upstream | 0.38 |
| [[bld_schema_safety_policy]] | upstream | 0.38 |
| [[bld_schema_dataset_card]] | upstream | 0.37 |
| [[bld_schema_quickstart_guide]] | upstream | 0.37 |
| [[bld_schema_reranker_config]] | upstream | 0.37 |
| [[bld_schema_pitch_deck]] | upstream | 0.37 |
| [[bld_schema_benchmark_suite]] | upstream | 0.36 |
