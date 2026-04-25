---
quality: 8.7
quality: 7.9
id: bld_kc_revision_loop_policy
kind: knowledge_card
pillar: P01
llm_function: INJECT
purpose: Linked KC for revision_loop_policy builder (F3 INJECT context)
title: "Knowledge Card: revision_loop_policy (Builder Link)"
version: "1.0.0"
author: n03_hermes_w1_6
tags: [knowledge_card, revision_loop_policy, builder, p11, hermes, escalation]
domain: "revision_loop_policy construction"
created: "2026-04-18"
updated: "2026-04-18"
tldr: "Linked KC for revision_loop_policy builder (F3 INJECT context)"
density_score: 0.88
related:
  - bld_collaboration_quality_gate
  - p08_ac_verification
  - p03_sp_quality_gate_builder
  - p03_sp_bugloop_builder
  - p03_sp_hitl_config_builder
  - bugloop-builder
  - bld_norms
  - p03_sp_n03_creation_nucleus
  - quality-gate-builder
  - bld_instruction_bugloop
---

## Builder Knowledge Injection

This file is loaded at **F3 INJECT** by the revision-loop-policy-builder to prime the LLM
with domain context before producing an artifact.

## Key Facts (inject verbatim)

1. **HERMES origin**: OpenCode-Hermes multiagent spec defines "Up to 3 iterations before escalation" as the canonical revision budget.
2. **Priority order**: Always `[security, quality, implementation]`. Security gates evaluated first, regardless of score.
3. **Default max**: 3 iterations. Security-critical gets 5. Documentation gets 2.
4. **Quality floor**: 8.5 triggers a revision cycle. Artifacts scoring >= 8.5 do NOT get revised.
5. **Escalation targets**: `user` (human review), `senior_nucleus` (N07 or domain lead), `freeze` (block pipeline, log for async review).
6. **Naming**: `p11_rlp_{{name}}.yaml`. Always lowercase slug.
7. **max_bytes**: 2048 (compact policy format, no prose bloat).

## Boundary Map (memorize before producing)

```
revision_loop_policy (THIS)
  = iterative content-quality improvement cycles
  = "how many times can we try to improve this before escalating"

quality_gate (P11)
  = single pass/fail check at one pipeline stage
  = "does this artifact pass THIS check right now"
  (revision_loop_policy ORCHESTRATES N quality_gates)

retry_policy (P09)
  = transient-failure retries (network timeout, rate limit)
  = infrastructure retries, NOT content quality
  (different pillar, different problem domain)

bugloop (P11)
  = code bug auto-correction: detect > fix > verify
  = narrower scope: code bugs only, not general artifact quality
  (sibling kind, narrower domain)

regression_check (P11)
  = diff artifact output against a known baseline
  = backward-looking comparison, NOT iterative improvement
  (sibling kind, different semantic)
```

## Canonical Template Reference

```
N00_genesis/P11_feedback/tpl_revision_loop_policy.md
```

## Full KC Reference

```
N00_genesis/P01_knowledge/library/kind/kc_revision_loop_policy.md
```

## Implementation Checklist (enforce at F7 GOVERN)

- `max_iterations` MUST be a positive integer; default 3 unless scenario override applies
- `priority_order` MUST contain exactly [security, quality, implementation] in that order
- `escalation_target` MUST be one of: user, senior_nucleus, freeze
- `escalation_message_template` MUST reference `{{max_iterations}}` and `{{failing_gates}}`
- `iteration_on_quality_floor` MUST be a float between 0.0 and 10.0 (default 8.5)
- Per-scenario overrides MUST be a mapping; at minimum include security_critical and documentation
- Tag `hermes_origin` required on all revision_loop_policy artifacts for OpenCode-Hermes provenance
- `freeze` escalation target blocks the pipeline synchronously; use only when human review is mandatory
- `senior_nucleus` escalation routes to N07 by default; override with explicit nucleus ID if needed
- When `max_iterations = 1`, the policy is single-attempt; first failure immediately escalates
- `freeze` escalation suspends the pipeline synchronously until a human or N07 releases it
- Revision context (failing gates from previous attempt) MUST be passed to next iteration prompt

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_quality_gate]] | downstream | 0.22 |
| [[p08_ac_verification]] | downstream | 0.21 |
| [[p03_sp_quality_gate_builder]] | downstream | 0.20 |
| [[p03_sp_bugloop_builder]] | downstream | 0.20 |
| [[p03_sp_hitl_config_builder]] | downstream | 0.20 |
| [[bugloop-builder]] | downstream | 0.19 |
| [[bld_norms]] | downstream | 0.18 |
| [[p03_sp_n03_creation_nucleus]] | downstream | 0.18 |
| [[quality-gate-builder]] | downstream | 0.18 |
| [[bld_instruction_bugloop]] | downstream | 0.18 |
