---
id: pipeline_template_n05
kind: pipeline_template
8f: F8_collaborate
nucleus: n05
pillar: P12
mirrors: N00_genesis/P12_orchestration/templates/tpl_pipeline_template.md
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
title: "N05 Operations -- Pipeline Template (CI/CD)"
scenario: ci_cd_deploy
version: 1.0.0
quality: 8.4
tags: [mirror, n05, operations, hermes_assimilation, pipeline_template, ci_cd]
tldr: "N05 CI/CD pipelines: build, test, deploy, rollback -- IRA-enforced gates at every stage, zero tolerance for skipped validation."
related:
  - bld_schema_bugloop
  - p12_wf_auto_rollback
  - p03_sp_deploy_ops
  - bld_schema_e2e_eval
  - bld_schema_agents_md
  - p02_agent_deploy_ops
  - bld_schema_smoke_eval
  - p02_agent_test_ops
  - bld_schema_voice_pipeline
  - p12_wf_railway_superintendent
---

## Scenario: CI/CD Operations Pipeline

N05 owns the operational pipeline scenarios: build, test, deploy, rollback.
Every stage has a mandatory gate. No stage can be skipped. IRA lens: if a gate
fails, the pipeline stops. No mercy.

## Stage Sequence

| Order | Role | Model Tier | Optional | Gate | Failure Mode | Rollback |
|-------|------|-----------|----------|------|--------------|----------|
| 1 | linter | low | No | syntax clean | block pipeline | n/a |
| 2 | tester | medium | No | all tests pass | block pipeline | n/a |
| 3 | security_scanner | medium | No | no critical CVEs | block pipeline | n/a |
| 4 | builder | medium | No | artifact compiles | block pipeline | n/a |
| 5 | deployer | high | No | health check pass | auto-rollback | revert to last-good |
| 6 | verifier | medium | No | smoke test pass | auto-rollback | revert to last-good |
| 7 | monitor | low | No | no error spike 5min | alert oncall | manual decision |

## Revision Loop

| Parameter | Value | Notes |
|-----------|-------|-------|
| Max iterations | 3 | HERMES proven default |
| Quality floor | 9.0 | N05 demands higher than generic 8.5 |
| Priority | security > quality > implementation | Non-negotiable |
| Escalation | n07 | Orchestrator decides after 3 failures |
| SLA target | pipeline complete <15min | Alert at 12min |

## Quality Gates (IRA-Enforced)

| Gate | Stage | Mandatory | Failure Action |
|------|-------|-----------|----------------|
| Lint pass | linter | Yes | Block |
| Test pass | tester | Yes | Block |
| CVE scan clean | security_scanner | Yes | Block |
| Compile success | builder | Yes | Block |
| Health check | deployer | Yes | Auto-rollback |
| Smoke test | verifier | Yes | Auto-rollback |
| Error rate stable | monitor | Yes | Alert + manual |

## Failure Modes

| Failure | Detection | Auto-Response | Escalation |
|---------|-----------|--------------|------------|
| Test flake | >2 flaky runs in 24h | quarantine test | N05 oncall |
| Build timeout | >5min | kill + retry 1x | alert |
| Deploy health fail | HTTP 5xx from health endpoint | instant rollback | page oncall |
| Smoke test fail | assertion error | rollback + DLQ | N07 |
| Post-deploy error spike | error rate >2x baseline | rollback | page oncall |

## Instantiation

```yaml
pipeline:
  template_ref: pipeline_template_n05
  scenario: ci_cd_deploy
  revision_loop:
    policy_ref: revision_loop_policy_n05
    max_iterations: 3
    escalation_target: n07
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_bugloop]] | upstream | 0.27 |
| [[p12_wf_auto_rollback]] | related | 0.25 |
| [[p03_sp_deploy_ops]] | upstream | 0.24 |
| [[bld_schema_e2e_eval]] | upstream | 0.23 |
| [[bld_schema_agents_md]] | upstream | 0.23 |
| [[p02_agent_deploy_ops]] | upstream | 0.22 |
| [[bld_schema_smoke_eval]] | upstream | 0.22 |
| [[p02_agent_test_ops]] | upstream | 0.21 |
| [[bld_schema_voice_pipeline]] | upstream | 0.21 |
| [[p12_wf_railway_superintendent]] | related | 0.20 |
