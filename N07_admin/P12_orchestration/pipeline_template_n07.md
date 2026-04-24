---
id: pipeline_template_n07
kind: pipeline_template
8f: F8_collaborate
nucleus: n07
pillar: P12
mirrors: N00_genesis/P12_orchestration/templates/tpl_pipeline_template.md
ownership: canonical
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
  scenarios: [mission, hotfix, evolve, overnight, audit]
scenario: mission
stages:
  - role: planner
    model_tier: high
    optional: false
  - role: guide
    model_tier: high
    optional: true
  - role: spec_writer
    model_tier: high
    optional: false
  - role: dispatcher
    model_tier: high
    optional: false
  - role: monitor
    model_tier: high
    optional: false
  - role: consolidator
    model_tier: high
    optional: false
revision_loop:
  max_iterations: 2
  escalation_target: user
quality_gates:
  mandatory: [consolidator]
  priority_order: [deliverables, signals, quality]
version: 1.0.0
quality: 8.4
tags: [mirror, n07, orchestration, pipeline_template, hermes_assimilation, canonical_owner]
tldr: "N07 dispatch pipelines: mission/hotfix/evolve/overnight/audit. Plan->guide->spec->grid->consolidate."
created: "2026-04-18"
related:
  - p01_kc_orchestration_best_practices
  - ctx_cex_new_dev_guide
  - n07_output_orchestration_audit
  - p08_ac_orchestrator
  - p03_sp_orchestration_nucleus
  - p12_wf_orchestration_pipeline
  - spec_n07_operational_intelligence
  - p02_agent_admin_orchestrator
  - p01_kc_cex_project_overview
  - p03_sp_admin_orchestrator
---

## Override Rationale

N07 **owns** the `pipeline_template` kind. Orchestrating Sloth means every pipeline
is optimized for delegation: plan the work, guide decisions, spec the blueprint,
dispatch to nuclei, monitor signals, consolidate results. N07 never touches artifacts.

## Canonical Stage Sequences

| Scenario | Stages | Notes |
|----------|--------|-------|
| mission | planner -> guide -> spec_writer -> dispatcher -> monitor -> consolidator | Full lifecycle: /plan -> /guide -> /spec -> /grid -> /consolidate |
| hotfix | dispatcher -> monitor -> consolidator | Skip planning; direct dispatch to affected nucleus |
| evolve | planner -> dispatcher -> monitor -> consolidator | Autonomous improvement; no guide needed |
| overnight | planner -> spec_writer -> dispatcher -> monitor -> consolidator | Unattended; spec locks all decisions upfront |
| audit | planner -> monitor -> consolidator | Read-only; no dispatch, just verification |

## Stage Definitions (N07)

| Stage | Role | Input | Output | 8F Map |
|-------|------|-------|--------|--------|
| planner | Decompose goal into tasks | User intent | plan.md with waves + dependencies | F1 + F4 |
| guide | GDP: collect subjective decisions | plan.md | decision_manifest.yaml | F4 (GDP) |
| spec_writer | Blueprint exact artifacts | plan + decisions | spec.md with file paths + kinds | F4 + F6 |
| dispatcher | Write handoffs + spawn nuclei | spec.md | handoff files + PID tracking | F5 + F8 |
| monitor | Poll signals + git log | PID file | wave completion status | F5 |
| consolidator | Verify + stop + commit + archive | signals | consolidation report | F7 + F8 |

## Quality Gates (N07)

| Gate | Role | Pass Criteria |
|------|------|--------------|
| Deliverables exist | consolidator | All files listed in spec exist on disk |
| Signals received | consolidator | All dispatched nuclei signaled complete |
| Quality floor | consolidator | Average quality across wave >= 8.5 |
| Clean processes | consolidator | No orphan claude/node processes after stop |

## Anti-Patterns

| Anti-Pattern | Risk | Fix |
|-------------|------|-----|
| Skipping guide for subjective work | Nuclei guess wrong, waste tokens | Always run GDP before mission dispatch |
| Dispatching without spec | No verification target | Spec defines exact deliverables to check |
| Monitor as blocking poll | N07 idles, wastes 1M context | Interleave own work with periodic checks |
| Skipping consolidation | Orphan processes + uncommitted work | Consolidate is mandatory after every wave |

## Wave Composition

```
Mission "BUILD_CRM":
  W1: [N01_research, N04_knowledge]     # independent research
  W2: [N03_build, N02_copy]             # depends on W1 output
  W3: [N05_test, N06_pricing]           # depends on W2 artifacts
  W4: [N07_consolidate]                 # final gate
```

## Links

- N00 archetype: [[N00_genesis/P12_orchestration/templates/tpl_pipeline_template.md]]
- N03 engineering sibling: [[N03_engineering/P12_orchestration/pipeline_template_n03.md]]
- N05 operations sibling: [[N05_operations/P12_orchestration/pipeline_template_n05.md]]
- Mission runner: [[_tools/cex_mission_runner.py]]
- Dispatch script: [[_spawn/dispatch.sh]]

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_orchestration_best_practices]] | upstream | 0.38 |
| [[ctx_cex_new_dev_guide]] | related | 0.36 |
| [[n07_output_orchestration_audit]] | related | 0.35 |
| [[p08_ac_orchestrator]] | upstream | 0.34 |
| [[p03_sp_orchestration_nucleus]] | upstream | 0.34 |
| [[p12_wf_orchestration_pipeline]] | related | 0.31 |
| [[spec_n07_operational_intelligence]] | upstream | 0.30 |
| [[p02_agent_admin_orchestrator]] | upstream | 0.30 |
| [[p01_kc_cex_project_overview]] | upstream | 0.30 |
| [[p03_sp_admin_orchestrator]] | upstream | 0.29 |
