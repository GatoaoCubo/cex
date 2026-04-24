---
id: revision_loop_policy_n05
kind: revision_loop_policy
8f: F7_govern
nucleus: n05
pillar: P11
mirrors: N00_genesis/P11_feedback/tpl_revision_loop_policy.md
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
title: "N05 Operations -- Revision Loop Policy (Deploy Revision)"
max_iterations: 3
iteration_on_quality_floor: 9.0
priority_order: [security, quality, implementation]
escalation_target: n07
version: 1.0.0
quality: 8.5
tags: [mirror, n05, operations, hermes_assimilation, revision_loop_policy]
tldr: "N05-owned deploy revision policy: max 3 rollback cycles, security-first priority, IRA-enforced escalation to N07."
related:
  - p12_wf_create_orchestration_agent
  - n07_output_orchestration_audit
  - p02_agent_creation_nucleus
  - bld_collaboration_kind
  - agent_card_engineering_nucleus
  - p03_sp_bugloop_builder
  - bld_output_template_team_charter
  - p01_kc_cex_project_overview
  - p11_qg_admin_orchestration
  - self_audit_n05_codex_2026_04_15
---

## Ownership

N05 OWNS this kind. Operations controls revision loop behavior for all
deploy and runtime artifacts. IRA lens: no infinite loops, no silent failures.

## Policy: N05 Operations Deploy Revision

### Revision Loop Behavior

| Parameter | Value | Notes |
|-----------|-------|-------|
| Max iterations | 3 | Hard limit, no override without N07 approval |
| Quality floor | 9.0 | N05 demands higher than generic 8.5 |
| Priority | security > quality > implementation | Non-negotiable order |
| Escalation | n07 | Orchestrator decides after exhaustion |
| SLA target | resolution <30min per cycle | Alert at 25min |

### Scenario Overrides (IRA-Enforced)

| Scenario | Max Iterations | Quality Floor | Escalation | Rationale |
|----------|---------------|---------------|------------|-----------|
| security_critical | 5 | 9.5 | user (immediate) | Security incidents get extra cycles + direct user escalation |
| deploy_rollback | 2 | 9.0 | n07 | Fast rollback: 2 attempts then escalate |
| documentation | 2 | 8.5 | n05 oncall | Docs rarely need >2 cycles |
| ci_gate_failure | 3 | 9.0 | n07 | Standard: 3 attempts at fixing gate |
| incident_response | 1 | 8.0 | user (immediate) | Incidents: one shot then human takes over |

### Failure Modes

| Failure | Detection | Response | Escalation |
|---------|-----------|----------|------------|
| Max iterations reached | counter == max | freeze artifact, emit signal | n07 + audit log |
| Quality floor never met | score < floor after all cycles | mark as blocked | n07 review queue |
| Escalation target unreachable | signal timeout >5min | fallback to user | direct user alert |
| Infinite loop detected | same score 3x consecutive | force-stop | n05 oncall + audit |

### Escalation Protocol

When `max_iterations` is reached without all gates passing:

1. Emit escalation signal: `write_signal('n05', 'revision_exhausted', {score}, details={failing_gates})`
2. Freeze the artifact (set `status: revision_blocked` in frontmatter)
3. Route to `escalation_target`:
   - `n07`: orchestrator reviews and re-dispatches or accepts
   - `user`: direct notification with full revision trace
   - `n05_oncall`: internal ops review (runtime issues only)
4. Log full revision trace to `.cex/runtime/audit/n05_revision_trace.jsonl`
5. SLA: escalation acknowledged within 15min

### Rollback Procedure

| Step | Action | Gate |
|------|--------|------|
| 1 | Identify last-known-good version via git log | version exists |
| 2 | Revert artifact to last-good | diff is clean |
| 3 | Re-run quality gate on reverted version | score >= floor |
| 4 | Signal revert complete | signal acknowledged |

### Boundaries

- NOT `retry_policy` (P09): retry handles transient failures; this handles content quality cycles
- NOT `quality_gate` (P11): quality_gate is a single pass/fail; this orchestrates N of them
- NOT `regression_check` (P11): regression diffs against baseline; this iterates toward a floor

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_create_orchestration_agent]] | downstream | 0.27 |
| [[n07_output_orchestration_audit]] | downstream | 0.22 |
| [[p02_agent_creation_nucleus]] | upstream | 0.21 |
| [[bld_collaboration_kind]] | downstream | 0.20 |
| [[agent_card_engineering_nucleus]] | upstream | 0.20 |
| [[p03_sp_bugloop_builder]] | related | 0.19 |
| [[bld_output_template_team_charter]] | upstream | 0.19 |
| [[p01_kc_cex_project_overview]] | upstream | 0.19 |
| [[p11_qg_admin_orchestration]] | related | 0.19 |
| [[self_audit_n05_codex_2026_04_15]] | upstream | 0.19 |
