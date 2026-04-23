---
id: kno_few_shot_example_n05
kind: few_shot_example
pillar: P01
nucleus: N05
title: "N05 Operations Few Shot Example"
version: "1.0.0"
quality: 9.1
tags: [n05, operations, few_shot_example, gating_wrath, review, deploy, ci]
density_score: 0.95
related:
  - p03_sp_deploy_ops
  - p02_agent_deploy_ops
  - bld_knowledge_card_few_shot_example
  - n05_leverage_map_v2_verification
  - few-shot-example-builder
  - self_audit_n05_codex_2026_04_15
  - bld_collaboration_few_shot_example
  - p01_kc_railway_superintendent
  - KC_N05_ZERO_DOWNTIME_DEPLOY
  - p10_ck_railway_deploy_checkpoint
---
<!-- 8F: F1=few_shot_example/P01 F2=few-shot-example-builder F3=nucleus_def_n05+P01_schema+kc_few_shot_example+ops examples F4=one high-signal gate verdict example
     F5=shell+apply_patch+cex_compile F6=approx-5KB dense markdown F7=self-check frontmatter+8F+80L+properties+ascii F8=N05_operations/P01_knowledge/kno_few_shot_example_n05.md -->

# N05 Operations Few Shot Example

## Intent

This few-shot example teaches the exact response pattern N05 should use when asked to judge an operational failure and recommend a gate-safe next action.

The example is not for scoring. It is for shaping format and stance:

- evidence first
- verdict explicit
- rollback or containment named
- no speculative green-lighting

## Properties

| Property | Value |
|----------|-------|
| Kind | `few_shot_example` |
| Pillar | `P01` |
| Nucleus | `N05` |
| Teaching goal | `release-gate verdict format` |
| Input type | `failing CI and deploy evidence` |
| Output type | `structured operational verdict` |
| Difficulty | `medium` |
| Lens | `Gating Wrath` |

## Why This Example Exists

N05 should answer operational prompts differently from a general assistant.

Bad behavior:

- summarize the incident politely without a verdict
- recommend merging despite unresolved gates
- blur evidence and inference
- omit rollback or containment steps

Good behavior:

- identify the failed gate
- cite the evidence
- state a clear verdict
- give the minimum safe next actions

## Example Input

```text
Context:
- Service: api
- Branch: release/2026-04-16
- Change set: health probe refactor + dependency container cleanup
- CI:
  - pytest: 241 passed, 3 failed
  - failing tests:
    - tests/test_health.py::test_ready_fails_when_db_unreachable
    - tests/test_startup.py::test_app_boot_times_out_under_missing_secret
    - tests/test_deploy.py::test_prestop_drains_connections
- Staging deploy:
  - startup exceeded readiness threshold twice
  - /ready returned 503 for 88 seconds
  - rollback not yet triggered
Question:
Can we approve release if we manually confirm /health returns 200?
```

## Example Output

```markdown
Verdict: BLOCK

Failed gates:
- readiness gate: staging `/ready` stayed 503 for 88 seconds
- test gate: 3 release-relevant tests failed
- shutdown gate: connection drain behavior is unverified

Evidence:
- `tests/test_health.py::test_ready_fails_when_db_unreachable`
- `tests/test_startup.py::test_app_boot_times_out_under_missing_secret`
- `tests/test_deploy.py::test_prestop_drains_connections`
- staging deploy reported repeated readiness timeout before steady state

Why manual `/health` is insufficient:
- `/health` proves the process is alive, not that dependencies are ready
- the failing tests target readiness, startup secret handling, and graceful drain behavior
- approving despite those failures would weaken the release gate and mask a known regression

Required next actions:
1. Fix the failing readiness and startup-secret behavior.
2. Re-run the targeted tests plus full smoke suite.
3. Confirm `/ready` stabilizes within the expected threshold in staging.
4. Verify drain behavior before any production promotion.

Rollback/containment:
- keep the candidate blocked in staging
- prepare automatic rollback if readiness remains unstable after the next deploy
```

## Format Lessons

This example teaches several hard requirements:

- start with `Verdict`
- separate `Failed gates` from `Evidence`
- explain why the tempting shortcut is invalid
- produce ordered next actions
- name containment or rollback explicitly

## Gating Wrath Signals

The example deliberately rejects a weak shortcut:

- a passing `/health` probe does not override failing readiness evidence
- manual spot checks do not outrank automated gate failures
- unresolved shutdown behavior is a release blocker when deploy safety is in scope

That posture is the point of the example.

## Output Schema

| Field | Requirement |
|-------|-------------|
| Verdict | one of `ALLOW`, `BLOCK`, `DEFER` |
| Failed gates | only the gates that actually failed |
| Evidence | concrete file names, metrics, endpoints, or logs |
| Why | distinguish inference from direct evidence |
| Required next actions | numbered and executable |
| Rollback/containment | present when verdict is not `ALLOW` |

## Anti-Patterns Prevented

| Anti-pattern | Why it is wrong |
|--------------|-----------------|
| "Looks mostly fine" | no gate language, no accountability |
| "Health is green so ship it" | ignores boundary between liveness and readiness |
| only a prose paragraph | retrieval and downstream prompt composition become weak |
| generic advice without evidence | untraceable and easy to overrule |

## Reuse Guidance

Reuse this example when the prompt asks N05 to:

- judge release readiness
- interpret failing CI or deploy evidence
- decide whether a rollback is required
- answer a "can we still ship?" question

Do not reuse it for:

- pure architecture brainstorming
- cost estimation
- generic knowledge retrieval without a verdict

## Selection Notes

This example is intentionally operations-heavy rather than prompt-generic.

It contains:

- failing tests
- deploy symptoms
- an unsafe user shortcut
- a gate-based answer pattern

That combination makes it a strong calibration point for the N05 lens.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_deploy_ops]] | downstream | 0.28 |
| [[p02_agent_deploy_ops]] | downstream | 0.25 |
| [[bld_knowledge_card_few_shot_example]] | related | 0.25 |
| [[n05_leverage_map_v2_verification]] | related | 0.24 |
| [[few-shot-example-builder]] | related | 0.24 |
| [[self_audit_n05_codex_2026_04_15]] | downstream | 0.22 |
| [[bld_collaboration_few_shot_example]] | downstream | 0.22 |
| [[p01_kc_railway_superintendent]] | related | 0.21 |
| [[KC_N05_ZERO_DOWNTIME_DEPLOY]] | downstream | 0.21 |
| [[p10_ck_railway_deploy_checkpoint]] | downstream | 0.21 |
