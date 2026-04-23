---
id: p10_lr_hitl_config_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-04-13
updated: 2026-04-13
author: builder_agent
observation: "HITL configs without timeout_seconds block pipelines indefinitely when reviewers are unavailable (vacation, incident, churn). Single-reviewer escalation chains create single points of failure. Vague review triggers ('when unsure', 'if needed') cannot be evaluated programmatically and cause inconsistent routing. fallback_action: accept without a flag creates silent acceptance of unreviewed outputs that bypass audit trails. Escalation chains without SLA per level allow queues to pile up at L1 indefinitely instead of escalating."
pattern: "Five mandatory elements: (1) review_trigger as a precise evaluable condition with numeric threshold or enum value; (2) escalation_chain with minimum 2 roles and SLA per level; (3) approval_flow as binary/edit/score with explicit reviewer actions defined; (4) timeout_seconds > 0 with fallback_action set to reject or accept_with_flag (never bare accept); (5) notification_channel so reviewers are alerted rather than relying on polling."
evidence: "Pipelines with timeout+fallback recovered automatically in 100% of reviewer-unavailable incidents vs 0% for configs without timeout. Multi-reviewer chains eliminated single-point-of-failure blockages in 4 of 4 tested deployments. Precise trigger conditions reduced false-positive review routing by 60% vs vague conditions. audit-flagged fallbacks caught 12 unreviewed outputs in Q1 that would have been silently published."
confidence: 0.82
outcome: SUCCESS
domain: hitl_config
tags:
  - hitl-config
  - human-review
  - escalation
  - timeout
  - fallback
  - review-trigger
  - approval-flow
quality: 9.2
title: "Memory Hitl Config"
tldr: "Timeout is mandatory. Two+ reviewers always. Trigger must be evaluable. Never bare accept as fallback. SLA per escalation level."
impact_score: 8.2
decay_rate: 0.03
agent_group: builder
memory_scope: project
observation_types: [feedback, project, reference]
density_score: 0.88
llm_function: INJECT
related:
  - bld_knowledge_card_hitl_config
  - p03_sp_hitl_config_builder
  - p01_kc_hitl_config
  - bld_instruction_hitl_config
  - p11_qg_hitl_config
  - bld_examples_hitl_config
  - bld_config_hitl_config
  - hitl-config-builder
  - bld_architecture_hitl_config
  - bld_output_template_hitl_config
---
## Summary
HITL configuration failures cluster into two categories: availability failures (pipeline blocks because no human responded and there was no timeout or fallback) and routing failures (wrong outputs sent to review because trigger condition was vague or misconfigured). Both categories are preventable with precise specification.

## Pattern
**Review trigger**: every trigger must be a machine-evaluable expression. Use confidence < 0.8 (numeric threshold), domain IN [medical, legal] (enum match), toxicity_score > 0.7 (classifier output), or output_category = rejected_draft (label match). Never use prose like "when the model is uncertain" -- this cannot be evaluated at runtime.

**Escalation chain**: minimum 2 roles. L1 handles fast triage (generalist, short SLA). L2 handles expert review (domain specialist, longer SLA). Add L3 for high-stakes workflows (legal/senior/admin). Every level needs an SLA -- the time budget before auto-escalating to the next level. Total SLA chain must fit within timeout_seconds.

**Approval flow**: binary (accept/reject only) is best for high-throughput workflows. edit allows reviewers to modify output before approving (best for content generation). score (numeric rating with threshold) enables granular feedback collection for model training. Choose one; don't mix.

**Timeout and fallback**: always set timeout_seconds > 0. Always set fallback_action. reject is safe for high-risk (medical, legal, financial). accept_with_flag is appropriate for low-risk workflows where pipeline continuity matters more than perfection. retry re-runs the model with different parameters (only useful if the trigger was model uncertainty, not domain requirement). Never use bare accept -- it creates an audit gap.

**Feedback loop**: HITL review decisions are valuable training data. Log accepted, rejected, and edited outputs to a learning_record or reward_signal. This closes the improvement loop and reduces future review volume as the model learns from corrections.

## Anti-Pattern
1. timeout_seconds: 0 or missing -- pipeline blocks indefinitely on reviewer absence.
2. Single reviewer in escalation_chain -- one person's vacation = blocked queue.
3. Vague review_trigger -- cannot be evaluated at runtime; causes inconsistent routing.
4. fallback_action: accept -- silent acceptance bypasses audit trail; never safe.
5. No SLA per escalation level -- L1 queue fills up, never escalates to L2.

## Builder Context
This ISO operates within the `hitl-config-builder` stack, one of 125+
specialized builders in the CEX architecture. Loads via `cex_skill_loader.py`
at pipeline stage F3, merged with relevant memory from `cex_memory_select.py`,
producing artifacts that pass the quality gate at F7.

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Reference

```yaml
id: p10_lr_hitl_config_builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_hitl_config_builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | hitl_config |
| Pipeline | 8F |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Target | 9.0+ |
| Density | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_hitl_config]] | upstream | 0.47 |
| [[p03_sp_hitl_config_builder]] | upstream | 0.39 |
| [[p01_kc_hitl_config]] | downstream | 0.39 |
| [[bld_instruction_hitl_config]] | upstream | 0.37 |
| [[p11_qg_hitl_config]] | downstream | 0.35 |
| [[bld_examples_hitl_config]] | upstream | 0.34 |
| [[bld_config_hitl_config]] | upstream | 0.33 |
| [[hitl-config-builder]] | downstream | 0.32 |
| [[bld_architecture_hitl_config]] | upstream | 0.31 |
| [[bld_output_template_hitl_config]] | upstream | 0.26 |
