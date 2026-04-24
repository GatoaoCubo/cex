---
id: con_secret_config_n06
kind: secret_config
8f: F1_constrain
pillar: P09
nucleus: n06
title: Commercial Secret Config
version: 1.0
quality: 9.0
tags: [config, secret, payments, rotation, security]
density_score: 1.0
updated: "2026-04-17"
related:
  - bld_collaboration_secret_config
  - bld_knowledge_card_secret_config
  - secret-config-builder
  - bld_config_secret_config
  - bld_examples_secret_config
  - p01_kc_secret_config
  - p09_secret_openai_key
  - p09_secret_config
  - p10_lr_secret_config_builder
  - bld_instruction_secret_config
---

<!-- 8F: F1 constrain=P09/secret_config F2 become=secret-config-builder F3 inject=nucleus_def_n06.md,n06-commercial.md,bld_manifest_secret_config.md,kc_secret_config.md,P09_config/_schema.yaml F4 reason=secret_registry_for_payment_alert_and_revenue_control_credentials F5 call=apply_patch;python _tools/cex_compile.py F6 produce=4811_bytes F7 govern=frontmatter_sections_ascii_density_review F8 collaborate=N06_commercial/P09_config/con_secret_config_n06.md -->

# Commercial Secret Config

## Purpose

| Field | Value |
|-------|-------|
| Goal | Define how N06 stores, references, rotates, and audits commercial secrets |
| Business Lens | Strategic Greed knows revenue depends on trust; payment, webhook, and alert credentials must be scarce, rotated, and never committed |
| Primary Use | document secret ids, providers, access patterns, and rotation cadence without exposing values |
| Failure Prevented | payment outage, leaked billing tokens, forged alerts, and long-lived credential drift |
| Storage Principle | pointer registry only, never actual secret value |
| Recovery Principle | rotate fast, restore revenue paths first |

## Values

| Secret ID | Provider | Runtime Env Var | Rotation Policy | Access Pattern | Commercial Use |
|-----------|----------|-----------------|-----------------|----------------|----------------|
| sec_payment_primary | vault | `N06_PAYMENT_API_KEY` | 30_day_or_incident | injected at runtime | primary checkout processing |
| sec_payment_webhook | vault | `N06_PAYMENT_WEBHOOK_SECRET` | 30_day_or_incident | verifier only | settlement and fraud callbacks |
| sec_alert_webhook | vault | `N06_ALERT_WEBHOOK` | 45_day_or_incident | injected at runtime | revenue-risk and churn alerts |
| sec_crm_sync | vault | `N06_CRM_SYNC_TOKEN` | 60_day_or_incident | service token | move high-value leads into follow-up |
| sec_experiment_store | vault | `N06_EXPERIMENT_TOKEN` | 60_day_or_incident | service token | track pricing test winners safely |

## Storage Rules

| Rule ID | Rule | Reason |
|---------|------|--------|
| SC01 | all N06 commercial secrets live in managed vault storage | removes file-based sprawl |
| SC02 | local development uses short-lived injected values only | avoids persistent desktop leakage |
| SC03 | secret ids may appear in docs, secret values may not | supports audit without exposure |
| SC04 | rotation after incident overrides scheduled cadence | breach window must collapse fast |
| SC05 | access logs retained for every secret read | high-value credentials demand traceability |

## Rotation Playbook

| Step | Action | Priority |
|------|--------|----------|
| 1 | rotate payment primary and webhook pair | highest, revenue path depends on both |
| 2 | verify checkout and settlement callbacks | highest, cash flow validation |
| 3 | rotate alert and CRM sync tokens | medium, preserves response loops |
| 4 | rotate experiment token | medium, protects pricing telemetry |
| 5 | close incident note with affected revenue estimate | required for learning and finance visibility |

## Rationale

| Design Choice | Why It Exists | Strategic Greed Impact |
|---------------|---------------|------------------------|
| Short rotation for payment secrets | payment loss hurts instantly | maximizes uptime and fraud defense |
| Vault-only provider | scattered storage invites leaks | protects monetization rails |
| Separate webhook secret | verification should be isolated from active payment credential | limits blast radius |
| Access logs mandatory | secrecy without audit is theater | lets N06 trace suspicious use |
| Incident-first rotation | schedule is secondary to exposure risk | keeps cash path recoverable |

## Example

| Scenario | Result |
|----------|--------|
| suspected webhook leak after settlement mismatch | rotate `sec_payment_webhook`, verify callbacks, preserve checkout continuity |

```yaml
name: n06_commercial_secrets
provider: vault
rotation_policy: incident_or_scheduled
secrets:
  - secret_id: sec_payment_primary
    env_var: N06_PAYMENT_API_KEY
    rotation_days: 30
  - secret_id: sec_alert_webhook
    env_var: N06_ALERT_WEBHOOK
    rotation_days: 45
```

## Properties

| Property | Value |
|----------|-------|
| Owner | N06 Commercial |
| Provider | vault |
| Secret Count | 5 |
| Fastest Rotation | 30 days |
| Logging Requirement | every read audited |
| Exposure Rule | values never stored in artifact files |
| Highest Priority Secret | payment primary and webhook pair |
| Local Dev Rule | short-lived injection only |
| Commercial Bias | trust and uptime protect revenue |
| Related Pillars | P09, P06, P11 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_secret_config]] | downstream | 0.42 |
| [[bld_knowledge_card_secret_config]] | upstream | 0.39 |
| [[secret-config-builder]] | related | 0.37 |
| [[bld_config_secret_config]] | related | 0.36 |
| [[bld_examples_secret_config]] | upstream | 0.34 |
| [[p01_kc_secret_config]] | related | 0.34 |
| [[p09_secret_openai_key]] | sibling | 0.34 |
| [[p09_secret_config]] | sibling | 0.33 |
| [[p10_lr_secret_config_builder]] | downstream | 0.31 |
| [[bld_instruction_secret_config]] | upstream | 0.29 |
