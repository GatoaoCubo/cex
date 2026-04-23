---
id: bld_memory_revision_loop_policy
kind: procedural_memory
pillar: P10
llm_function: INJECT
purpose: P10 memory hooks for revision_loop_policy builder
quality: 8.3
title: "Memory: Revision Loop Policy Builder"
version: "1.0.0"
author: n03_hermes_w1_6
tags: [memory, revision_loop_policy, builder, p10, patterns, learnings]
domain: "revision_loop_policy construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.87
related:
  - p11_qg_pattern
  - p11_qg_router
  - p03_sp_hitl_config_builder
  - p08_pat_construction_triad
  - p03_sp_kind_builder
  - bld_examples_quality_gate
---

## Learned Patterns

### Pattern 1: Always default to max_iterations: 3
The HERMES spec proved 3 iterations as the optimal balance: enough for content-quality
convergence, not so many that the pipeline stalls. Override only when scenario demands it.

### Pattern 2: escalation_target selection heuristic
| Pipeline Mode | Target | Rationale |
|--------------|--------|-----------|
| Interactive (user present) | `user` | Human review is feasible |
| Automated with N07 available | `senior_nucleus` | N07 can re-plan |
| Overnight/headless | `freeze` | No human to route to; log for morning review |

### Pattern 3: Quality floor vs publish minimum
- Quality floor (8.5): triggers a new revision cycle -- not the same as the publish gate
- Publish minimum (8.0): CEX system floor -- an artifact can publish at 8.0 without triggering revision
- Target (9.0): N03 inventive pride standard -- aim for this on all production artifacts

### Pattern 4: Per-scenario override table is NOT optional
Always include at minimum `security_critical: 5` and `documentation: 2`.
These are the canonical HERMES overrides. Omitting them makes the policy incomplete
for security audits.

### Pattern 5: escalation_message_template is a contract
Recipients of the escalation message (user, senior_nucleus) use the message to understand
WHAT failed (the failing_gates list) and HOW MANY times (the max_iterations count) the pipeline tried.
Never use a generic message like "too many retries" -- it provides no actionable context.

## Anti-Pattern Registry

| Anti-Pattern | Consequence | Fix |
|-------------|-------------|-----|
| priority_order with only 2 items | H03 gate fails | Always include all 3: [security, quality, implementation] |
| Swapping security and quality positions | Wrong conflict resolution | security MUST be index 0 |
| max_iterations: 0 | No revisions attempted | Minimum is 1; for no revisions use quality_gate directly |
| Generic escalation_message_template | Unactionable escalation | Must contain the max_iterations and failing_gates placeholder tokens |
| Using revision_loop_policy for network retries | Wrong kind | Route to retry_policy (P09) |

## Build History Context
- W1.6 HERMES Assimilation (2026-04-18): initial kind creation from opencode-hermes-multiagent spec
- Designed to work with pipeline_template (W1.5) which references revision loops

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_pattern]] | downstream | 0.17 |
| [[p11_qg_router]] | downstream | 0.16 |
| [[p03_sp_hitl_config_builder]] | upstream | 0.16 |
| [[p08_pat_construction_triad]] | upstream | 0.16 |
| [[p03_sp_kind_builder]] | upstream | 0.16 |
| [[bld_examples_quality_gate]] | upstream | 0.15 |
