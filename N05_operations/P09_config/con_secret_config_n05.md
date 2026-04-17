---
id: con_secret_config_n05
kind: secret_config
pillar: P09
nucleus: n05
title: Ops Secret Registry
version: 1.0
quality: null
tags: [config, secret, operations, vault, rotation]
---
<!-- 8F: F1 constrain=P09/secret_config F2 become=secret-config-builder F3 inject=nucleus_def_n05+n05-operations+kc_secret_config+P09_config+N05 secret patterns
     F4 reason=secret registry with rotation and retrieval discipline for ops workflows F5 call=apply_patch F6 produce=4521 bytes
     F7 govern=self-check headings+tables+gating_wrath+ascii+80_lines F8 collaborate=N05_operations/config/con_secret_config_n05.md -->

# Ops Secret Registry

## Purpose

| Field | Value |
|---|---|
| Intent | Define how N05 stores, references, rotates, and retrieves operational secrets without exposing values. |
| Scope | CI credentials, deploy tokens, alert webhooks, provider API keys, rollback control secrets. |
| Gating Wrath Lens | A secret without owner, backend, or rotation policy is treated as a latent incident. |
| Default Posture | Store references only; never persist raw secret material in this artifact. |
| Backend Rule | Approved backends are `vault`, `railway`, or short-lived env injection. |

## Values

| Secret ID | Provider | Runtime Env Var | Rotation Policy | Retrieval Pattern | Owner | Failure Action |
|---|---|---|---|---|---|---|
| ops_deploy_token | vault | CEX_DEPLOY_TOKEN | 30_days | just_in_time_read | release_manager_n05 | Abort deploy and alert owner. |
| ops_alert_webhook | railway | CEX_ALERT_WEBHOOK | 90_days | deploy_time_injection | sre_n05 | Disable non-critical notifications and log exception. |
| ops_provider_key | vault | CEX_PROVIDER_API_KEY | 45_days | just_in_time_read | platform_ops_n05 | Block provider calls. |
| ops_rollback_token | vault | CEX_ROLLBACK_TOKEN | 30_days | just_in_time_read | incident_commander_n05 | Block rollback automation and escalate immediately. |
| ops_ci_signing_key | vault | CEX_CI_SIGNING_KEY | 60_days | runner_session_injection | qa_lead_n05 | Fail artifact verification. |

## Secret Handling Rules

| Rule | Description | Gating Effect |
|---|---|---|
| No raw values | This file stores only identifiers, env var names, and policies. | Prevents credential leakage by design. |
| Rotation mandatory | Every secret has a bounded rotation window. | Shrinks breach duration. |
| Owner mandatory | Each secret has a named operator or team. | No orphaned credentials. |
| Short-lived retrieval preferred | Read secret near execution time, not during idle setup. | Limits exposure window. |
| Breach path predefined | Failure action must be explicit. | Reduces panic and delay during incidents. |

## Rationale

| Design Choice | Why It Exists | Gating Wrath Effect |
|---|---|---|
| Vault-first posture | Centralized, audited retrieval beats local sprawl. | Improves revocation speed. |
| Distinct rollback token | Recovery authority should be separable from deploy authority. | Protects emergency control channel. |
| 30-90 day windows | Rotation cadence is strict enough for ops risk and manageable for humans. | Balances discipline and feasibility. |
| Per-secret failure action | Different secrets fail differently and need tailored containment. | Speeds correct operator response. |
| Session injection for signing key | Build integrity material should live briefly in runner memory. | Minimizes residue. |

## Example

| Scenario | Secret Outcome |
|---|---|
| Deploy token expired | Release job fails before rollout and pages release owner. |
| Provider key unavailable | Review automation halts rather than issuing partial results. |
| Rollback token missing during incident | Escalation is immediate because recovery path is impaired. |

```yaml
name: n05_ops_secrets
provider: vault
rotation_policy: strict
secrets:
  ops_deploy_token:
    env_var: CEX_DEPLOY_TOKEN
    rotation_days: 30
    retrieval: just_in_time_read
    owner: release_manager_n05
  ops_rollback_token:
    env_var: CEX_ROLLBACK_TOKEN
    rotation_days: 30
    retrieval: just_in_time_read
    owner: incident_commander_n05
```

## Properties

| Property | Value |
|---|---|
| Kind | `secret_config` |
| Pillar | `P09` |
| Nucleus | `n05` |
| Storage Style | Reference registry only |
| Approved Backends | `vault`, `railway`, `env` |
| Review Cadence | Monthly or after any credential incident |
| Failure Mode | Missing secret blocks the dependent action and opens escalation |
| Sin Lens | Gating Wrath: secret hygiene is enforced before action, not audited after damage. |
