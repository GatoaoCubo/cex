---
id: p11_arch_revision_loop_policy
kind: component_map
pillar: P11
llm_function: CONSTRAIN
purpose: F1 CONSTRAIN structural architecture for revision_loop_policy
quality: 8.5
title: "Architecture: Revision Loop Policy"
version: "1.0.0"
author: n03_hermes_w1_6
tags: [architecture, revision_loop_policy, builder, p11, governance, hermes]
domain: "revision_loop_policy construction"
created: "2026-04-18"
updated: "2026-04-18"
tldr: "F1 CONSTRAIN structural architecture for revision_loop_policy"
density_score: 0.89
related:
  - bld_architecture_compliance_checklist
  - bld_architecture_subscription_tier
  - bld_architecture_self_improvement_loop
  - bld_architecture_ab_test_config
  - bld_architecture_audit_log
  - bld_architecture_enterprise_sla
  - quality-gate-builder
  - bugloop-builder
  - p01_kc_cex_lp11_feedback
  - bld_architecture_quality_gate
---

## Position in CEX Architecture

```
P12 Orchestration
  pipeline_template
    stages[]
      revision_loop:           <-- embeds revision_loop_policy by ref
        policy_ref: rlp_*

P11 Feedback
  revision_loop_policy         <-- THIS KIND
    governs -> quality_gate    <-- evaluated each iteration
    escalates -> user | senior_nucleus | freeze
    peer -> bugloop            <-- code-specific correction loop
    peer -> retry_policy (P09) <-- transient-failure retries (different pillar)
```

## Component Relationships

| Component | Relationship | Direction |
|-----------|-------------|-----------|
| `pipeline_template` (P12) | embeds `revision_loop_policy` as `revision_loop` block | P12 -> P11 |
| `quality_gate` (P11) | evaluated on each revision iteration | P11 internal |
| `bugloop` (P11) | sibling for code-bug correction (narrower scope) | P11 sibling |
| `retry_policy` (P09) | sibling for transient-failure retries (different pillar) | P09 sibling |
| `regression_check` (P11) | sibling for baseline-diff comparison | P11 sibling |
| `reward_signal` (P11) | emitted on escalation to signal quality failure | P11 internal |

## Lifecycle in 8F Pipeline

```
F7 GOVERN (in any builder):
  1. Evaluate quality gates
  2. IF score >= iteration_on_quality_floor: PASS, continue to F8
  3. IF score < floor AND attempt < max_iterations:
     a. Inject gate failure context
     b. Return to F6 PRODUCE for regeneration
     c. Increment attempt counter
  4. IF attempt == max_iterations:
     a. Emit escalation_message_template
     b. Route to escalation_target
     c. Log revision trace
```

## Data Flow

```
Input: artifact draft + quality gate results
          |
          v
revision_loop_policy evaluates:
  - current_score vs iteration_on_quality_floor
  - attempt_count vs max_iterations
  - priority_order for gate conflict resolution
          |
          v
Decision: ACCEPT | REVISE | ESCALATE
          |
    REVISE: return to F6 with gate context
    ACCEPT: proceed to F8
    ESCALATE: emit message, route to target
```

## Pillar Placement
- **Pillar**: P11 (Feedback) -- governance layer, quality enforcement
- **Layer**: governance (not runtime, not content)
- **Owner nucleus**: N05 (operations/gating)
- **LLM function**: GOVERN -- evaluates and gates artifact acceptance

## Naming Pattern
```
p11_rlp_{{name}}.yaml
```
Lives in nucleus P11 directories or shared `.cex/policies/` for cross-nucleus use.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_compliance_checklist]] | upstream | 0.37 |
| [[bld_architecture_subscription_tier]] | upstream | 0.35 |
| [[bld_architecture_self_improvement_loop]] | upstream | 0.35 |
| [[bld_architecture_ab_test_config]] | upstream | 0.35 |
| [[bld_architecture_audit_log]] | upstream | 0.34 |
| [[bld_architecture_enterprise_sla]] | upstream | 0.31 |
| [[quality-gate-builder]] | related | 0.30 |
| [[bugloop-builder]] | related | 0.25 |
| [[p01_kc_cex_lp11_feedback]] | upstream | 0.22 |
| [[bld_architecture_quality_gate]] | upstream | 0.22 |
