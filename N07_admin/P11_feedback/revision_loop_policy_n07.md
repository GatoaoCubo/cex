---
id: revision_loop_policy_n07
kind: revision_loop_policy
8f: F7_govern
nucleus: n07
pillar: P11
mirrors: N00_genesis/P11_feedback/tpl_revision_loop_policy.md
overrides:
  tone: terse, dispatch-oriented, meta
  voice: imperative orchestrator
  sin_lens: PREGUICA ORQUESTRADORA
  required_fields:
    - target_nucleus
    - expected_deliverables
    - do_not_list
  quality_threshold: 9.2
  density_target: 0.90
  example_corpus: 3+ examples with full do-not lists
max_iterations: 3
iteration_on_quality_floor: 8.0
priority_order: [deliverables, signals, quality]
escalation_target: user
per_scenario_overrides:
  mission_dispatch: 2
  overnight_grid: 1
  hotfix: 3
version: 1.0.0
quality: 8.3
tags: [mirror, n07, orchestration, revision_loop_policy, hermes_assimilation]
tldr: "N07 dispatch revision: max 3 nucleus retries before user escalation. Overnight gets 1 shot."
created: "2026-04-18"
related:
  - n07_output_orchestration_audit
  - p12_wf_create_orchestration_agent
  - p01_kc_orchestration_best_practices
  - p02_agent_creation_nucleus
  - p12_wf_admin_orchestration
  - p12_wf_orchestration_pipeline
  - agent_card_engineering_nucleus
  - p08_ac_orchestrator
  - bld_knowledge_card_nucleus_def
  - p12_ho_admin_template
density_score: 1.0
updated: "2026-04-22"
---

## Override Rationale

N07's revision loop governs **dispatch retries**, not artifact revisions.
When a nucleus fails (bad signal, missing deliverables, quality < 8.0),
N07 re-dispatches with an enriched handoff. After max_iterations, escalate to user.

## Policy Table (N07 Overrides)

| Parameter | N00 Default | N07 Override | Reason |
|-----------|-------------|-------------|--------|
| max_iterations | 3 | 3 | Match HERMES default; 3 dispatch retries |
| quality_floor | 8.5 | 8.0 | N07 accepts lower floor; nuclei self-gate at 8.5 |
| priority_order | security>quality>impl | deliverables>signals>quality | N07 cares about existence first, quality second |
| escalation_target | user | user | Never escalate to another nucleus |

## Scenario Overrides (N07-Specific)

| Scenario | Max Retries | Rationale |
|----------|------------|-----------|
| mission_dispatch | 2 | Mission waves have downstream dependencies; fail fast |
| overnight_grid | 1 | Unattended; no point retrying without human oversight |
| hotfix | 3 | Hotfix is critical; worth 3 attempts with different approaches |
| standard_dispatch | 3 | Default: 3 retries covers most transient failures |

## Retry Enrichment Protocol

On each retry, N07 enriches the handoff:

| Retry # | Enrichment |
|---------|------------|
| 1 | Add artifact references the nucleus missed |
| 2 | Simplify scope (split into smaller deliverables) |
| 3 | Escalate to user with failure report |

## Failure Modes N07 Detects

| Failure | Detection | Response |
|---------|-----------|----------|
| No signal after 45 min | PID alive but no git commits | Kill + re-dispatch |
| Signal with quality < 8.0 | Signal file score field | Re-dispatch with quality emphasis |
| Missing deliverables | File existence check | Re-dispatch with explicit file paths |
| Process crash | PID dead, no signal | Log + re-dispatch |
| Repeated same failure | 2 identical failure modes | Escalate to user |

## Links

- N00 archetype: [[N00_genesis/P11_feedback/tpl_revision_loop_policy.md]]
- N03 sibling: [[N03_engineering/P11_feedback/revision_loop_policy_n03.md]]
- N04 sibling: [[N04_knowledge/P11_feedback/revision_loop_policy_n04.md]]
- Autonomous lifecycle: [[.claude/rules/n07-autonomous-lifecycle.md]]

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n07_output_orchestration_audit]] | downstream | 0.36 |
| [[p12_wf_create_orchestration_agent]] | downstream | 0.33 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.32 |
| [[p02_agent_creation_nucleus]] | upstream | 0.31 |
| [[p12_wf_admin_orchestration]] | downstream | 0.30 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.30 |
| [[agent_card_engineering_nucleus]] | upstream | 0.30 |
| [[p08_ac_orchestrator]] | upstream | 0.29 |
| [[bld_knowledge_card_nucleus_def]] | upstream | 0.28 |
| [[p12_ho_admin_template]] | downstream | 0.28 |
