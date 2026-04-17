---
id: con_permission_n05
kind: permission
pillar: P09
nucleus: n05
title: Ops Permission Matrix
version: 1.0
quality: null
tags: [config, permission, operations, access, governance]
---
<!-- 8F: F1 constrain=P09/permission F2 become=permission-builder F3 inject=nucleus_def_n05+n05-operations+kc_permission+P09_config+N05 workflow boundaries
     F4 reason=minimum necessary access for review deploy rollback flows F5 call=apply_patch F6 produce=4710 bytes
     F7 govern=self-check headings+tables+gating_wrath+ascii+80_lines F8 collaborate=N05_operations/config/con_permission_n05.md -->

# Ops Permission Matrix

## Purpose

| Field | Value |
|---|---|
| Intent | Define who can read, write, execute, and approve within N05 operational workflows. |
| Scope | Review agents, deploy automation, incident response, compile steps, and signal emission. |
| Gating Wrath Lens | Access is earned by role and narrowed by resource; deny rules outrank convenience. |
| Default Posture | Deny by default, allow by need, audit every override. |
| Enforcement Model | RBAC with explicit deny exceptions for high-risk actions. |

## Values

| Subject | Resources | Allowed Actions | Denied Actions | Reason |
|---|---|---|---|---|
| release_manager_n05 | `N05_operations/config/*`, `N05_operations/schemas/*`, `.cex_signals/*` | read, write, approve | delete on source roots | Can author and signal, but not destructively rewrite history. |
| qa_reviewer_n05 | `N05_operations/*`, `_reports/*` | read, comment, approve | deploy, delete | Reviews quality without mutating runtime state. |
| deployer_n05 | `compiled/*`, `.cex_signals/*`, deploy endpoints | read, execute, write | source delete, permission override | Executes approved rollout only. |
| incident_commander_n05 | `_reports/*`, `.cex_signals/*`, rollback controls | read, execute, write, rollback | source authoring | Can contain incidents fast without broad author rights. |
| automation_worker_n05 | declared deliverable paths only | read, write | wildcard write, delete, spawn | Keeps automated edits in bounded scope. |
| observer_n05 | logs, reports, compiled outputs | read | write, execute, approve | Monitoring role stays read-only. |

## Deny-First Overrides

| Deny Rule | Applies To | Why | Release Consequence |
|---|---|---|---|
| No wildcard delete on source trees | all subjects | Protect authored artifacts and rules. | Manual escalation required. |
| No approval without named role | automation_worker_n05, observer_n05 | Approval must stay human-accountable. | Gate remains blocked. |
| No deploy from reviewer role | qa_reviewer_n05 | Separation of duties prevents self-approval deploys. | Hand-off required. |
| No permission mutation during incident | deployer_n05, incident_commander_n05 | Containment should not expand privilege surface. | Use admin escalation outside this scope. |

## Rationale

| Design Choice | Why It Exists | Gating Wrath Effect |
|---|---|---|
| Deny by default | Permission sprawl is the fast path to operational mistakes. | Shrinks attack and error surface. |
| Role separation | Review, deploy, and incident response should not collapse into one actor by habit. | Forces explicit hand-off. |
| Delete restrictions | Destructive power should be rare and explicit. | Preserves recoverability. |
| Bounded automation | Workers may write only intended outputs. | Prevents broad accidental edits. |
| No live privilege expansion | Incidents create pressure to bypass process. | Keeps crisis actions auditable. |

## Example

| Scenario | Decision |
|---|---|
| `qa_reviewer_n05` tries to trigger deploy | denied |
| `deployer_n05` writes compiled artifacts after approval | allowed |
| `automation_worker_n05` attempts to edit unrelated config file | denied |
| `incident_commander_n05` triggers rollback path | allowed |

```yaml
scope: n05_operations
default_effect: deny
subjects:
  release_manager_n05:
    allow: [read, write, approve]
    resources:
      - N05_operations/config/*
      - N05_operations/schemas/*
      - .cex_signals/*
    deny: [delete]
  deployer_n05:
    allow: [read, execute, write]
    resources:
      - compiled/*
      - .cex_signals/*
      - deploy_endpoint/*
    deny:
      - delete
      - permission_override
```

## Properties

| Property | Value |
|---|---|
| Kind | `permission` |
| Pillar | `P09` |
| Nucleus | `n05` |
| Access Model | RBAC with explicit denies |
| Review Cadence | Every release process update or incident postmortem |
| Failure Mode | Unmatched subject-resource pair resolves to deny |
| Audit Signal | Approval, deploy, rollback, and override attempts logged |
| Sin Lens | Gating Wrath: access exists to enforce discipline, not to erase friction. |
