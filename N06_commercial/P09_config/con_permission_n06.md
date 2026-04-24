---
id: con_permission_n06
kind: permission
8f: F1_constrain
pillar: P09
nucleus: n06
title: Commercial Permission Model
version: 1.0
quality: 9.0
tags: [config, permission, access, premium, governance]
density_score: 1.0
related:
  - bld_schema_permission
  - bld_schema_bugloop
  - bld_schema_rbac_policy
  - bld_schema_quickstart_guide
  - bld_schema_reranker_config
  - bld_schema_safety_policy
  - bld_schema_usage_report
  - bld_schema_context_window_config
  - bld_schema_sandbox_config
  - bld_schema_pitch_deck
---

<!-- 8F: F1 constrain=P09/permission F2 become=permission-builder F3 inject=nucleus_def_n06.md,n06-commercial.md,bld_manifest_permission.md,kc_permission.md,P09_config/_schema.yaml F4 reason=least_privilege_access_for_high_value_commercial_resources F5 call=apply_patch;python _tools/cex_compile.py F6 produce=5152_bytes F7 govern=frontmatter_sections_ascii_density_review F8 collaborate=N06_commercial/P09_config/con_permission_n06.md -->

# Commercial Permission Model

## Purpose

| Field | Value |
|-------|-------|
| Goal | Define who can read, write, and execute against N06 commercial resources |
| Business Lens | Strategic Greed wants fast monetization moves, but premium assets, pricing logic, and revenue evidence need tighter control than generic content |
| Primary Use | Protect pricing strategy, compiled outputs, and secret-linked operations from careless mutation |
| Failure Prevented | accidental margin erosion, broken offers, leaked premium logic, and noisy low-value edits |
| Access Model | deny by default, allow by role |
| Priority | premium revenue surfaces receive strongest protection |

## Values

| Role | Resource | Read | Write | Execute | Rationale |
|------|----------|------|-------|---------|-----------|
| n06_owner | `N06_commercial/**` | yes | yes | yes | core commercial operator |
| n07_orchestrator | `N06_commercial/**` | yes | limited | yes | coordination and validation authority |
| revenue_analyst | `N06_commercial/P05_output/**` | yes | yes | no | can refine business artifacts, not runtime behavior |
| pricing_reviewer | `N06_commercial/P06_schema/**` | yes | propose_only | no | review contracts without direct mutation |
| runtime_compiler | `N06_commercial/compiled/**` | yes | yes | yes | compile path requires write and run |
| market_reader | `N06_commercial/P01_knowledge/**` | yes | no | no | reference access only |
| generic_agent | `N06_commercial/P09_config/**` | no | no | no | config is too sensitive for blanket access |
| audit_process | `_reports/**` | yes | yes | yes | can produce revenue diagnostics |

## Deny Rules

| Deny ID | Subject | Resource | Deny | Why |
|---------|---------|----------|------|-----|
| DP01 | all_non_n06 | `N06_commercial/P09_config/con_secret_config_n06.md` | read_write_execute | secret policy must stay tightly bounded |
| DP02 | all_non_n06_owner | `N06_commercial/P09_config/con_rate_limit_config_n06.md` | write | spend policy changes alter monetization economics |
| DP03 | all_non_n06_owner | `N06_commercial/P06_schema/sch_type_def_n06.md` | write | type drift breaks pricing telemetry |
| DP04 | generic_agent | `N06_commercial/P05_output/**` | write | low-context edits can weaken offers |
| DP05 | all_roles | `.git/**` | execute_delete | this config does not grant repo-destructive power |

## Escalation Rules

| Case | Escalation Path | Reason |
|------|-----------------|--------|
| emergency pricing fix | n06_owner plus n07_orchestrator | trade speed against revenue risk |
| secret policy update | n06_owner only, documented review after | credential exposure is asymmetric damage |
| enterprise offer change | n06_owner plus pricing_reviewer | premium motion needs dual scrutiny |

## Rationale

| Design Choice | Why It Exists | Strategic Greed Impact |
|---------------|---------------|------------------------|
| Deny by default | unscoped access always expands risk | keeps premium logic scarce and valuable |
| Separate reviewer from owner | review should not equal mutation | increases price-discipline without slowing analysis |
| Tight control on rate limits and secrets | cost and trust are revenue foundations | protects both spend and reputation |
| Read-only market access | insight can be shared safely | research informs greed without corrupting source memory |
| Audit process can write reports | evidence compounds advantage | makes commercial learning durable |

## Example

| Request | Result | Reason |
|---------|--------|--------|
| `generic_agent` tries to edit `con_rate_limit_config_n06.md` | deny | spend policy too sensitive |
| `runtime_compiler` writes compiled YAML | allow | required for artifact pipeline |
| `pricing_reviewer` proposes changes to `sch_enum_def_n06.md` | read and comment only | contract safety over speed |

```yaml
default_policy: deny
roles:
  - n06_owner
  - n07_orchestrator
  - revenue_analyst
  - pricing_reviewer
denies:
  - subject: all_non_n06
    resource: N06_commercial/P09_config/con_secret_config_n06.md
    actions: [read, write, execute]
```

## Properties

| Property | Value |
|----------|-------|
| Owner | N06 Commercial |
| Model | RBAC with explicit denies |
| Default | deny |
| Role Count | 8 |
| Deny Count | 5 |
| Premium Defense | strongest around secrets, types, and rate limits |
| Escalation Mode | explicit dual approval for high-risk changes |
| Auditability | required for all exceptions |
| Commercial Bias | protect scarce revenue logic from broad mutation |
| Related Pillars | P09, P06, P11 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_permission]] | upstream | 0.42 |
| [[bld_schema_bugloop]] | downstream | 0.36 |
| [[bld_schema_rbac_policy]] | upstream | 0.36 |
| [[bld_schema_quickstart_guide]] | upstream | 0.33 |
| [[bld_schema_reranker_config]] | upstream | 0.33 |
| [[bld_schema_safety_policy]] | upstream | 0.33 |
| [[bld_schema_usage_report]] | upstream | 0.32 |
| [[bld_schema_context_window_config]] | upstream | 0.32 |
| [[bld_schema_sandbox_config]] | upstream | 0.32 |
| [[bld_schema_pitch_deck]] | upstream | 0.32 |
