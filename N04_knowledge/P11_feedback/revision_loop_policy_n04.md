---
id: revision_loop_policy_n04
kind: revision_loop_policy
nucleus: n04
pillar: P11
mirrors: N00_genesis/compiled/tpl_revision_loop_policy.yaml
mirror_version: 1.0.0
promoted_from: null
overrides:
  tone: archival, dense, citation-thick
  voice: third-person encyclopedic
  sin_lens: GULA DO CONHECIMENTO
  required_fields:
    - sources
    - retrieval_method
    - freshness
  quality_threshold: 9.2
  density_target: 0.92
  example_corpus: 3+ examples with source manifest
max_iterations: 3
iteration_on_quality_floor: 8.5
priority_order:
  - citation_completeness   # N04 extension: no claim without source
  - factual_accuracy        # N04 extension: verify against corpus before passing
  - security
  - quality
  - implementation
version: 1.0.0
quality: 8.1
tags: [mirror, n04, knowledge, revision_loop_policy, hermes_assimilation, fact_check]
related:
  - p02_nd_n00.md
  - self_audit_n04_codex_2026_04_15
  - p09_feedback_iteration_history
  - bld_architecture_supabase_data_layer
  - p11_qg_intelligence
  - n04_dr_knowledge
  - p01_kc_supabase_data_layer_n04
  - bld_collaboration_supabase_data_layer
  - spec_n01_n04_verticalization
  - agent_card_n04
updated: "2026-04-22"
---

## Override Rationale

N04's fact-check loop mirrors the N00 revision policy but raises the priority of
**citation completeness** above all else -- Knowledge Gluttony demands that every
revised claim carries a traceable source. Factual accuracy is verified against the
active knowledge corpus before the iteration is counted.

## Revision Policy (N04 flavor)

| Parameter | Value | N04 Notes |
|-----------|-------|-----------|
| Max iterations | 3 | HERMES proven default; see upstream_source |
| Quality floor | 8.5 | Trigger revision if score below |
| Priority 1 | citation_completeness | No fact without source -- N04 canonical |
| Priority 2 | factual_accuracy | Cross-check against corpus before accepting |
| Priority 3 | security | Inherited from N00 |
| Priority 4 | quality | Density >= 0.92 required |
| Priority 5 | implementation | Structural completeness |
| Escalation | user | After max_iterations exhausted without convergence |

## Scenario Overrides

| Scenario | Max Iterations | Rationale |
|----------|---------------|-----------|
| `citation_missing` | 4 | Extra cycle to locate source before accepting claim |
| `corpus_conflict` | 5 | Two sources disagree -- extra rounds for reconciliation |
| `security_critical` | 5 | Inherited from N00 |
| `documentation` | 2 | Quick documentation tasks need less cycling |

## Iteration Gate Checklist

Before counting an iteration as passing, N04 verifies:

1. **Source count**: >= 3 sources cited in body
2. **Freshness**: each source has a `last_verified` date <= 90 days old
3. **Retrieval method**: explicit (`dense | sparse | hybrid | graph`)
4. **Factual consistency**: no contradiction between cited sources
5. **Density**: body density_score >= 0.92

If any gate fails, the iteration is rejected and the loop retries.

## Links

- N00 archetype: [[N00_genesis/compiled/tpl_revision_loop_policy.yaml]]
- N00 KC: [[N00_genesis/P01_knowledge/library/compiled/kc_revision_loop_policy.yaml]]
- Related: [[N04_knowledge/P11_feedback/quality_gate_knowledge.md]]
- Upstream: HERMES opencode-hermes-multiagent (1ilkhamov)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_nd_n00.md]] | upstream | 0.25 |
| [[self_audit_n04_codex_2026_04_15]] | upstream | 0.19 |
| [[p09_feedback_iteration_history]] | upstream | 0.19 |
| [[bld_architecture_supabase_data_layer]] | upstream | 0.19 |
| [[p11_qg_intelligence]] | related | 0.18 |
| [[n04_dr_knowledge]] | related | 0.18 |
| [[p01_kc_supabase_data_layer_n04]] | upstream | 0.17 |
| [[bld_collaboration_supabase_data_layer]] | downstream | 0.17 |
| [[spec_n01_n04_verticalization]] | upstream | 0.17 |
| [[agent_card_n04]] | upstream | 0.17 |
