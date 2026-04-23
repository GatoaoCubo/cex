---
id: context_file_n05
kind: context_file
nucleus: n05
pillar: P03
mirrors: N00_genesis/P03_prompt/tpl_context_file.md
overrides:
  tone: strict, deterministic, gate-heavy
  voice: imperative, risk-averse
  sin_lens: IRA
  required_fields:
    - sla_target
    - failure_mode
    - rollback_procedure
  quality_threshold: 9.3
  density_target: 0.90
  example_corpus: 3+ examples with failure modes section
title: "N05 Operations -- Context File (Ops Playbooks)"
scope: nucleus
injection_point: session_start
inheritance_chain: [N00_genesis/P03_prompt/tpl_context_file.md]
max_bytes: 8192
priority: 5
applies_to_nuclei: [n05]
version: 1.0.0
quality: 8.4
tags: [mirror, n05, operations, hermes_assimilation, context_file]
tldr: "N05 runtime context: ops playbooks, oncall runbooks, incident escalation, deploy gates -- injected at session start."
related:
  - p03_sp_n03_creation_nucleus
  - p01_kc_git_hooks_ci
  - p03_sp_quality_gate_builder
  - p12_wf_auto_ship
  - p03_sp_handoff_builder
  - p04_hook_pre_commit_qa
  - p11_qg_admin_orchestration
  - p03_sp_kind_builder
  - p03_sp_system-prompt-builder
  - p02_agent_deploy_ops
density_score: 1.0
updated: "2026-04-22"
---

## Build Rules (Operations)

1. ALWAYS validate deployments via quality gate before merge
2. NEVER skip pre-commit hooks or CI gates (--no-verify is forbidden)
3. ALWAYS run `python _tools/cex_doctor.py` before signaling complete
4. NEVER force-push to main or shared branches
5. ALWAYS include rollback procedure in deploy artifacts

## Quality Rules (IRA Enforcement)

1. ALWAYS set `quality: null` -- never self-score
2. ALWAYS compile after saving: `python _tools/cex_compile.py {path}`
3. NEVER commit without doctor check passing
4. ALWAYS include SLA target in operational artifacts
5. ALWAYS document failure modes for any runtime component

## Oncall Context

| Field | Value |
|-------|-------|
| Escalation path | N05 oncall -> N07 orchestrator -> user |
| Alert channels | .cex/runtime/signals/ + gateway audit log |
| Runbook location | N05_operations/P04_tools/ |
| Incident log | .cex/runtime/audit/n05_incidents.jsonl |

## Deploy Gates (Mandatory)

| Gate | Tool | Failure Action |
|------|------|----------------|
| Pre-commit | cex_hooks.py | Block commit |
| ASCII check | cex_sanitize.py --check | Block commit |
| Doctor | cex_doctor.py | Block signal |
| Compile | cex_compile.py | Block commit |
| System test | cex_system_test.py | Block deploy |

## Active Runbooks

| Runbook | Trigger | SLA |
|---------|---------|-----|
| Process cleanup | orphan detected | 5min |
| Credential rotation | token age >75d | 24h |
| Disk space alert | >80% usage | 1h |
| Failed deploy rollback | CI gate fail | 15min |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_n03_creation_nucleus]] | related | 0.29 |
| [[p01_kc_git_hooks_ci]] | upstream | 0.29 |
| [[p03_sp_quality_gate_builder]] | related | 0.26 |
| [[p12_wf_auto_ship]] | downstream | 0.26 |
| [[p03_sp_handoff_builder]] | related | 0.25 |
| [[p04_hook_pre_commit_qa]] | downstream | 0.24 |
| [[p11_qg_admin_orchestration]] | downstream | 0.23 |
| [[p03_sp_kind_builder]] | related | 0.23 |
| [[p03_sp_system-prompt-builder]] | related | 0.23 |
| [[p02_agent_deploy_ops]] | upstream | 0.22 |
