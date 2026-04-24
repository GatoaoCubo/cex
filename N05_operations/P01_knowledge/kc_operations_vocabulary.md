---
id: p01_kc_operations_vocabulary
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "N05 Operations Controlled Vocabulary"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "n05_operations"
domain: controlled_vocabulary
quality: 9.1
tags: [operations, vocabulary, terminology, devops, sre, knowledge]
tldr: "22 canonical operations terms with N05 enforcement rules. Load at F2b SPEAK. Prevents semantic drift in all N05 artifacts."
when_to_use: "Load at F2b SPEAK before generating any N05 artifact. Required for all infrastructure, deployment, and reliability work."
keywords: [vocabulary, operations, devops, sre, terminology]
long_tails:
  - What terms must N05 use for deployment patterns and reliability?
  - How does N05 enforce industry-standard operations terminology?
axioms:
  - ALWAYS load this KC at F2b SPEAK before producing any N05 artifact
  - NEVER invent synonyms for terms defined in this vocabulary
  - ALWAYS use the enforcement column to constrain tool calls and artifact choices
  - NEVER skip F7 GOVERN -- zero_trust applies to all artifact outputs
linked_artifacts:
  primary: null
  related: [p01_kc_railway_superintendent, p01_kc_pre_commit_hooks_for_ai]
density_score: 0.91
data_source: "archetypes/builders/knowledge-card-builder/bld_schema_knowledge_card.md"
related:
  - p12_wf_create_orchestration_agent
  - p03_sp_n03_creation_nucleus
  - grid_test_n05_20260407
  - p12_wf_orchestration_pipeline
  - leverage_map_v2_n05_verify
  - p12_sig_builder_nucleus
  - p02_agent_test_ops
  - p12_wf_auto_review
  - report_intent_resolution_value_prop
  - p12_wf_auto_ship
---

# N05 Operations Controlled Vocabulary

## Quick Reference
```yaml
topic: controlled_vocabulary_n05
scope: N05 Operations nucleus -- all artifact generation and tool calls
owner: n05_operations
criticality: high
type: meta_kc
```

## Canonical Terms

| Term | Definition | N05 Enforcement |
|------|-----------|-----------------|
| `infrastructure_as_code` | Infra managed via version-controlled config files | CEX config = `.yaml`/`.md` only; no manual edits |
| `idempotent_deployment` | Same result on repeated runs | `compile`+`signal` must re-run safely; no state mutation |
| `blue_green_deployment` | Two identical envs; atomic traffic switch | N/A locally; document in `workflow_deploy_pipeline.md` |
| `canary_release` | Gradual rollout to subset before full promote | `/evolve` heuristic pass = canary; agent = full rollout |
| `circuit_breaker` | Halt downstream calls after threshold failures | Max 3 retries per tool call, then fail-fast |
| `retry_budget` | Max retries before accepting failure | 2 retries in F7 GOVERN; exceeded = surface error |
| `rate_limiting` | Request frequency cap to protect downstream | `rate_limit_config` per nucleus/provider; no ad-hoc sleep |
| `observability_triad` | Logs + metrics + traces for system understanding | `audit_log` + quality scores + `trace_config` (all 3 required) |
| `MTTR_MTTF` | Mean time to recovery / mean time to failure | Target MTTR < 5 min; track in `.cex/experiments/results.tsv` |
| `SLO_SLA_SLI` | Objective / agreement / indicator service levels | SLO: quality >= 8.0; SLI: signal within 30 min |
| `zero_trust` | Never trust implicitly; verify every artifact | All artifacts through F7 GOVERN; no `--skip-validate` |
| `principle_of_least_privilege` | Minimum permissions for the task | Nucleus writes only to own directory |
| `OWASP_top10` | Top 10 web application security risk classes | ASCII-only = no injection (A03); no secrets in code (A02) |
| `shift_left_testing` | Test earlier in lifecycle to reduce fix cost | Pre-commit hooks (`cex_hooks.py`); not post-deploy |
| `test_pyramid` | Unit > integration > e2e distribution | `cex_system_test.py`: unit -> integration -> e2e |
| `contract_testing` | Verify API consumer/provider honor shared schema | P06 `input_schema`+`validation_schema` = contracts |
| `chaos_engineering` | Deliberate failure injection for resilience | `/grid` multi-runtime dispatch; `fallback_chain` = harness |
| `mean_time_to_recovery` | Elapsed time from failure detection to restoration | Target < 5 min nucleus restart |
| `error_budget` | Allowed failure margin before blocking action | Quality >= 8.0 floor; below triggers bugloop |
| `toil_reduction` | Automate repetitive manual operational work | `cex_evolve.py` heuristic pass; manual sweeps = toil |
| `runbook` | Step-by-step procedure for operational tasks | `workflow` artifacts are the runbooks |
| `deployment_pipeline` | Automated stages: commit -> production | `workflow_deploy_pipeline.md`: lint->compile->test->signal |

## Anti-Patterns

| Wrong Term | Use Instead | Reason |
|------------|------------|--------|
| "restart the service" | `mean_time_to_recovery` remediation | Hides detection-vs-restore distinction |
| "test it manually" | `shift_left_testing` via hook | Manual = toil; needs automated pre-commit |
| "try again" | `retry_budget` check first | Unbounded retry = denial-of-service |
| "run the deploy script" | `deployment_pipeline` execution | Ad-hoc scripts bypass gates |
| "check the logs" | `observability_triad` | Logs alone miss metrics + traces |
| "give it access" | `principle_of_least_privilege` | Never broad; scope to nucleus dir |
| "a/b test this" | `canary_release` | A/B = UX experiment; canary = deploy safety |

## Cross-Nucleus Shared Terms (DO NOT REDEFINE)

Defined in N00_genesis. N05 uses verbatim -- no synonyms, no redefinitions.

| Term | Source | N05 Usage |
|------|--------|-----------|
| `8F pipeline` | 8f-reasoning.md | F7=zero_trust gate; F8=signal emit |
| `kind` | kinds_meta.json (257) | N05 primary: `workflow`, `bugloop`, `env_config` |
| `pillar` | N00_genesis P01-P12 | N05 primary: P04, P09, P11 |
| `nucleus` | nucleus_def files | N05 = operations; dispatched by N07 |
| `quality_gate` | P07 schema | floor 8.0, target 9.0 |
| `signal` | F8 COLLABORATE | N05 emits on complete; N07 polls |
| `handoff` | dispatch protocol | Read from `.cex/runtime/handoffs/` at boot |

## Application Flow

```
[task] -> [F2b: load KC] -> [map verbs -> terms] -> [select kind] -> [F7 gate]
```

- `"deploy"` -> `deployment_pipeline` -> `workflow`
- `"retry"` -> `retry_budget` check -> `circuit_breaker` if exhausted
- `"check logs"` -> `observability_triad` -> `trace_config`

## References

- Ubiquitous language: `.claude/rules/ubiquitous-language.md`
- Metaphor dictionary: `_docs/specs/spec_metaphor_dictionary.md`
- Rate limits: `.cex/P09_config/rate_limits.yaml`
- Prompt compiler: `N00_genesis/P03_prompt/layers/p03_pc_cex_universal.md`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_create_orchestration_agent]] | downstream | 0.27 |
| [[p03_sp_n03_creation_nucleus]] | downstream | 0.24 |
| [[grid_test_n05_20260407]] | downstream | 0.23 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.23 |
| [[leverage_map_v2_n05_verify]] | downstream | 0.22 |
| [[p12_sig_builder_nucleus]] | downstream | 0.22 |
| [[p02_agent_test_ops]] | downstream | 0.21 |
| [[p12_wf_auto_review]] | downstream | 0.21 |
| [[report_intent_resolution_value_prop]] | related | 0.21 |
| [[p12_wf_auto_ship]] | downstream | 0.21 |
