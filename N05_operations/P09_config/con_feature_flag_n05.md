---
id: con_feature_flag_n05
kind: feature_flag
pillar: P09
nucleus: n05
title: Ops Feature Flags
version: 1.0
quality: 9.0
tags: [config, flags, operations, rollout, safety]
density_score: 1.0
related:
  - bld_knowledge_card_feature_flag
  - p03_sp_feature_flag_builder
  - bld_collaboration_feature_flag
  - feature-flag-builder
  - p10_lr_feature_flag_builder
  - p01_kc_feature_flag
  - bld_instruction_feature_flag
  - bld_examples_feature_flag
  - bld_config_feature_flag
  - bld_architecture_feature_flag
---
<!-- 8F: F1 constrain=P09/feature_flag F2 become=feature-flag-builder F3 inject=nucleus_def_n05+n05-operations+kc_feature_flag+P09_config+N05 rollout patterns
     F4 reason=feature gates for risky operational pathways with immediate kill switches F5 call=apply_patch F6 produce=4640 bytes
     F7 govern=self-check headings+tables+gating_wrath+ascii+80_lines F8 collaborate=N05_operations/P09_config/con_feature_flag_n05.md -->

# Ops Feature Flags

## Purpose

| Field | Value |
|---|---|
| Intent | Define the operational feature flags that gate risky rollout and recovery behaviors in N05. |
| Scope | Canary release automation, auto rollback, verbose tracing, expedited approvals, shadow traffic. |
| Gating Wrath Lens | Every flag must have an owner, kill switch, rollback expectation, and expiry discipline. |
| Default Posture | New flags start off unless required to preserve safety. |
| Lifecycle Rule | Add, ramp, audit, remove. Permanent flags are a control failure. |

## Values

| Flag | Category | Default | Rollout | Owner | Kill Switch | Expiry Rule |
|---|---|---|---|---|---|---|
| ops_canary_auto_promote | release | off | 0% | release_manager_n05 | instant off | Remove after rollout system stabilizes. |
| ops_auto_rollback | ops | on | 100% | incident_commander_n05 | manual override only | Keep permanent because it reduces blast radius. |
| ops_shadow_traffic | experiment | off | 10% -> 50% -> 100% | perf_audit_n05 | instant off | Remove after traffic profile is validated. |
| ops_fast_approval_lane | permission | off | named cohort only | qa_lead_n05 | instant off | Expire after incident or launch window. |
| ops_verbose_deploy_trace | ops | off | environment scoped | sre_n05 | instant off | Disable when incident closes. |
| ops_freeze_manual_override | ops | on | 100% | release_manager_n05 | ticketed off | Permanent during freeze windows only. |

## Targeting Rules

| Flag | Eligible Scope | Blocked Scope | Reason |
|---|---|---|---|
| ops_canary_auto_promote | staging, prod canary | full prod direct | Broad rollout must stay human-gated. |
| ops_auto_rollback | staging, prod | none | Safety control should remain available everywhere. |
| ops_shadow_traffic | staging, low-risk prod cohort | incident state | Shadowing during instability distorts telemetry. |
| ops_fast_approval_lane | named emergency roster | general operators | Prevent privilege drift. |
| ops_verbose_deploy_trace | on-call sessions | normal flow | High log volume can leak signal-to-noise. |
| ops_freeze_manual_override | freeze windows | non-freeze periods | Restrict discretionary movement during risk spikes. |

## Rationale

| Design Choice | Why It Exists | Gating Wrath Effect |
|---|---|---|
| Most flags default off | Untested behavior should not self-activate. | Reduces surprise pathways. |
| Auto rollback defaults on | Safety automation deserves fail-safe treatment. | Containment beats convenience. |
| Owner field is mandatory | Someone must retire or defend each flag. | Prevents orphaned toggles. |
| Expiry rule on every temporary flag | Old flags become hidden branches. | Forces cleanup and re-review. |
| Cohort-limited fast lane | Emergency acceleration must be narrow and named. | Stops broad privilege spread. |

## Example

| Scenario | Flag State | Result |
|---|---|---|
| New canary controller release | `ops_canary_auto_promote=off` | Human promotion still required. |
| Critical error spike in prod | `ops_auto_rollback=on` | Automatic rollback path remains armed. |
| Incident war room active | `ops_verbose_deploy_trace=on` | Extra deployment trace collected for short interval. |

```yaml
flags:
  ops_canary_auto_promote:
    enabled: false
    rollout_pct: 0
    owner: release_manager_n05
    category: release
  ops_auto_rollback:
    enabled: true
    rollout_pct: 100
    owner: incident_commander_n05
    category: ops
  ops_fast_approval_lane:
    enabled: false
    rollout_pct: 0
    owner: qa_lead_n05
    category: permission
```

## Properties

| Property | Value |
|---|---|
| Kind | `feature_flag` |
| Pillar | `P09` |
| Nucleus | `n05` |
| Evaluation Point | Pre-deploy and runtime gate controllers |
| Kill Switch Standard | All flags must support immediate disable. |
| Audit Rule | Owner and expiry reviewed every release cycle. |
| Failure Mode | Unknown flag state resolves to disabled except `ops_auto_rollback`. |
| Sin Lens | Gating Wrath: flags exist to shrink risk, not to bypass controls. |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_feature_flag]] | upstream | 0.50 |
| [[p03_sp_feature_flag_builder]] | upstream | 0.45 |
| [[bld_collaboration_feature_flag]] | downstream | 0.42 |
| [[feature-flag-builder]] | related | 0.41 |
| [[p10_lr_feature_flag_builder]] | downstream | 0.41 |
| [[p01_kc_feature_flag]] | related | 0.39 |
| [[bld_instruction_feature_flag]] | upstream | 0.36 |
| [[bld_examples_feature_flag]] | upstream | 0.32 |
| [[bld_config_feature_flag]] | related | 0.29 |
| [[bld_architecture_feature_flag]] | upstream | 0.29 |
