---
id: n00_revision_loop_policy_manifest
kind: knowledge_card
8f: F3_inject
pillar: P11
nucleus: n00
title: "Revision Loop Policy -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, revision_loop_policy, p11, n00, archetype, hermes, escalation]
density_score: 1.0
upstream_source: "1ilkhamov/opencode-hermes-multiagent"
related:
  - bld_schema_safety_policy
  - bld_schema_bugloop
  - bld_schema_reranker_config
  - bld_schema_rbac_policy
  - bld_schema_usage_report
  - bld_schema_kind
  - bld_schema_integration_guide
  - bld_schema_benchmark_suite
  - bld_schema_search_strategy
  - bld_schema_dataset_card
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A revision_loop_policy governs how many iterative revision cycles are permitted on an artifact
before the pipeline escalates to a human or senior nucleus. It encodes the OpenCode-Hermes rule
"Up to 3 iterations permitted before escalation" as a declarative, reusable policy artifact.

Distinct from quality_gate (single pass/fail check) and retry_policy (transient-failure retries):
revision_loop_policy orchestrates N consecutive quality gates in a content-improvement cycle.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier (`rlp_{{name}}`) |
| kind | string | yes | Always `revision_loop_policy` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable policy name |
| max_iterations | integer | yes | Max revision cycles (default: 3, HERMES proven) |
| iteration_on_quality_floor | float | yes | Score below which revision triggers (default: 8.5) |
| priority_order | array | yes | Resolution order for conflicting gates |
| escalation_target | enum | yes | `user`, `senior_nucleus`, or `freeze` |
| escalation_message_template | string | yes | Template with `{{max_iterations}}` and `{{failing_gates}}` |
| per_scenario_overrides | map | no | Kind- or scenario-specific iteration overrides |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |

## When to use
- When configuring revision cycles inside a pipeline_template stage sequence
- When enforcing quality improvement loops before escalation in 8F F7 GOVERN
- When setting per-scenario iteration budgets (e.g., security_critical gets 5, docs get 2)

## Builder
`archetypes/builders/revision-loop-policy-builder/`

Run: `python _tools/cex_8f_runner.py "revision policy for X" --kind revision_loop_policy --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: rlp_standard
kind: revision_loop_policy
pillar: P11
title: "Revision Policy: Standard"
max_iterations: 3
iteration_on_quality_floor: 8.5
priority_order: [security, quality, implementation]
escalation_target: user
escalation_message_template: "Reached {{max_iterations}} revisions without passing gates: {{failing_gates}}"
per_scenario_overrides:
  security_critical: 5
  documentation: 2
version: 1.0.0
quality: null
tags: [hermes_origin, revision, escalation, policy]
---
```

## Related kinds
- `quality_gate` (P11) -- the gate evaluated on each revision iteration
- `bugloop` (P11) -- correction loop for code bugs (narrower scope)
- `pipeline_template` (P12) -- the pipeline that embeds the revision_loop_policy
- `retry_policy` (P09) -- transient-failure retries (network, timeout) -- NOT this kind
- `regression_check` (P11) -- diff vs baseline -- NOT this kind

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_safety_policy]] | upstream | 0.42 |
| [[bld_schema_bugloop]] | related | 0.41 |
| [[bld_schema_reranker_config]] | upstream | 0.40 |
| [[bld_schema_rbac_policy]] | upstream | 0.40 |
| [[bld_schema_usage_report]] | upstream | 0.39 |
| [[bld_schema_kind]] | upstream | 0.39 |
| [[bld_schema_integration_guide]] | upstream | 0.39 |
| [[bld_schema_benchmark_suite]] | upstream | 0.39 |
| [[bld_schema_search_strategy]] | upstream | 0.38 |
| [[bld_schema_dataset_card]] | upstream | 0.38 |
