---
id: revision_loop_policy_n03
kind: revision_loop_policy
nucleus: n03
pillar: P11
mirrors: N00_genesis/P11_feedback/tpl_revision_loop_policy.md
overrides:
  tone: precise, principled, no-magic
  sin_lens: SOBERBA INVENTIVA
  quality_threshold: 9.3
  density_target: 0.90
max_iterations: 3
iteration_on_quality_floor: 8.5
priority_order: [quality, tests, implementation]
escalation_target: user
per_scenario_overrides:
  security_critical: 5
  documentation: 2
  schema_breaking_change: 4
version: 1.0.0
quality: 8.4
tags: [mirror, n03, engineering, hermes_assimilation, revision_loop_policy]
tldr: "N03 revision policy: max 3 cycles, quality>tests>implementation priority. Schema breaks get 4 cycles."
created: "2026-04-18"
related:
  - agent_card_engineering_nucleus
  - p12_dr_software_project
  - p02_agent_creation_nucleus
  - p03_sp_n03_creation_nucleus
  - agent_card_n03
  - p12_dr_builder_nucleus
  - p01_kc_quality_gates
  - p01_kc_self_healing_skill
  - bld_sp_collaboration_software_project
  - p01_kc_n03_software_engineering
density_score: 1.0
updated: "2026-04-22"
---

## Axioms

1. **Revision is not retry** -- each cycle must change the approach, not repeat it.
2. **Quality before tests** -- a well-structured artifact that fails tests is better than passing tests on bad structure.
3. **Three cycles is discipline** -- if you need more than 3 cycles, the spec is wrong; escalate.

## Policy Table (N03 Overrides)

| Parameter | N00 Default | N03 Override | Reason |
|-----------|-------------|-------------|--------|
| max_iterations | 3 | 3 | HERMES proven; no override needed |
| quality_floor | 8.5 | 8.5 | N03 floor; quality gate raises to 9.3 |
| priority_order | security>quality>impl | quality>tests>impl | N03 rarely handles security kinds directly |
| escalation_target | user | user | N07 dispatch issues escalate to user, not N07 |

## Scenario Overrides (N03-Specific)

| Scenario | Max Cycles | Rationale |
|----------|-----------|-----------|
| security_critical | 5 | Security kinds (guardrail, secret_config) need extra review |
| documentation | 2 | KC / context_file rarely need more than 2 passes |
| schema_breaking_change | 4 | Breaking change to type_def / input_schema warrants extra care |
| standard_build | 3 | Default for all other kinds |

## Anti-Patterns

| Anti-Pattern | Risk | Fix |
|-------------|------|-----|
| Same approach on retry | Zero progress, wastes cycles | Change strategy: template-first -> hybrid -> fresh |
| Ignoring gate failure reason | F7 fails again | Read gate output before retry |
| Silent escalation | User unaware of failure | Write escalation message with failing_gates list |
| Increasing max_iterations ad hoc | Infinite loop risk | Only override via scenario_overrides, never inline |

## Integration in pipeline_template

```yaml
revision_loop:
  policy_ref: revision_loop_policy_n03
  max_iterations: 3
  escalation_target: user
  priority_order: [quality, tests, implementation]
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent_card_engineering_nucleus]] | upstream | 0.21 |
| [[p12_dr_software_project]] | downstream | 0.21 |
| [[p02_agent_creation_nucleus]] | upstream | 0.19 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.18 |
| [[agent_card_n03]] | upstream | 0.18 |
| [[p12_dr_builder_nucleus]] | downstream | 0.18 |
| [[p01_kc_quality_gates]] | upstream | 0.17 |
| [[p01_kc_self_healing_skill]] | upstream | 0.17 |
| [[bld_sp_collaboration_software_project]] | related | 0.17 |
| [[p01_kc_n03_software_engineering]] | upstream | 0.16 |
