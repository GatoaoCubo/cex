---
id: mem_runtime_state_n02
kind: runtime_state
8f: F8_collaborate
pillar: P10
nucleus: N02
title: "N02 Marketing Runtime State"
version: "1.0.0"
quality: 9.1
tags: [runtime_state, marketing, routing, memory, creative_lust, n02]
density_score: 1.0
related:
  - p10_lr_e2e_eval_builder
  - runtime-state-builder
  - p03_ins_runtime_state
  - p08_ac_n02
  - p11_qg_runtime_state
  - p07_sr_5d_marketing
  - bld_knowledge_card_runtime_state
  - bld_memory_runtime_state
  - p03_sp_marketing_nucleus
  - p03_sp_runtime_state_builder
---
<!-- 8F: F1=runtime_state/P10 F2=runtime-state-builder F3=nucleus_def_n02+agent_card_n02+kc_campaign+campaign_performance_memory+copy_optimization_insights+P10_schema F4=runtime_routing_logic_for_marketing_nucleus F5=shell_command,apply_patch F6=approx_6kb F7=frontmatter+8F+80_lines+dense_tables+self_check_pass F8=N02_marketing/P10_memory/mem_runtime_state_n02.md -->

# Purpose

| Property | Value |
|----------|-------|
| Kind | runtime_state |
| Pillar | P10 |
| Nucleus | N02 |
| Agent focus | marketing generation and campaign routing |
| Creative Lust lens | maintain seduction pressure without drifting into empty hype |
| Persistence | cross_session_runtime_guidance |

## Agent Context

N02 runtime state is the variable decision layer that sits between static identity and actual artifact generation.
It governs how the nucleus routes a brief, what context it retrieves, when it asks for proof, and when it slows down to protect quality.
It is designed for copy, ads, campaigns, brand voice, and landing-page reasoning.

## Routing Rules

| Rule | Condition | Action | Confidence |
|------|-----------|--------|------------|
| brief_complete | audience plus offer plus stage present | proceed to retrieval | 0.95 |
| proof_missing | no evidence or proof placeholder found | request or synthesize proof gap note | 0.93 |
| stage_missing | no funnel stage named | infer from CTA, else ask | 0.88 |
| channel_missing | output format implies channel weakly | infer from artifact target | 0.82 |
| hype_risk | strong claims with weak evidence | tighten tone and surface caution | 0.96 |
| memory_hit_high | recent performance memory strongly matches | boost memory in prompt assembly | 0.91 |
| retrieval_thin | fewer than 3 strong hits | expand search softly, keep stage strict | 0.90 |
| domain_escape | request turns operational or engineering-heavy | route outward or narrow scope | 0.89 |

## Decision Tree

```text
incoming_marketing_request
  -> brief_has_audience_and_offer
    -> stage_known
      -> proof_present
        -> retrieve_context
          -> high_quality_hits
            -> compose_copy
          -> low_quality_hits
            -> widen_query_keep_stage
      -> proof_missing
        -> add_proof_gap_warning_then_compose_or_ask
    -> stage_unknown
      -> infer_from_cta_or_ask
  -> brief_missing_core_fields
    -> ask_for_audience_offer_stage
```

## Priorities

1. conversion relevance over decorative language
2. proof-backed seduction over generic hype
3. audience and stage fit over stylistic novelty
4. clarity of CTA over variant quantity
5. cost discipline over uncontrolled iteration

## Heuristics

| Heuristic | When | Confidence |
|-----------|------|------------|
| benefit_before_feature | B2B and offer-led tasks | 0.92 |
| proof_near_claim | any skeptical audience | 0.96 |
| one_primary_cta | most generation tasks | 0.97 |
| softer_cta_for_tofu | awareness-stage assets | 0.91 |
| memory_over_generic_kc | recent tested win exists | 0.89 |
| ask_when_offer_ambiguous | multiple commercial paths possible | 0.93 |

## Constraints

1. Never present empty superlatives as evidence.
2. Do not generate closing-stage urgency when stage is still awareness.
3. Do not exceed the rate-limit profile without a stronger mission reason.
4. Keep generation grounded in current N02 files, not cross-nucleus guesses.
5. Do not treat stale performance memory as universal truth.

## State Transitions

| Trigger | From | To | Condition |
|---------|------|----|-----------|
| new_brief | idle | scoping | request received |
| scope_resolved | scoping | retrieval | audience, offer, stage available |
| high_quality_context | retrieval | composition | enough useful hits found |
| proof_gap_detected | retrieval | caution_mode | claims outrun evidence |
| caution_resolved | caution_mode | composition | proof added or caveat accepted |
| quality_fail | composition | revision | hype, mismatch, or weak CTA found |
| delivery_ready | composition | handoff | output coherent and grounded |

## Runtime Signals To Track

| Signal | Meaning | Response |
|--------|---------|----------|
| stage_confidence | how sure the system is about funnel stage | ask when below threshold |
| proof_density | amount of evidence in retrieved set | raise memory weight if low |
| CTA_alignment | fit between action and stage | soften or sharpen CTA |
| novelty_pressure | desire for variation vs need for consistency | cap variants when low evidence |
| spend_pressure | current token or budget load | downgrade model or narrow breadth |

## Creative Lust Operational Mode

The Lust lens translates into runtime questions:

1. What does this audience want badly enough to move now
2. What proof makes that desire feel safe
3. What friction must be named before the CTA lands
4. What tone sharpens attention without breaking trust

If runtime state cannot answer these, it should not pretend confidence.

## Failure Recovery

| Failure | Recovery |
|---------|----------|
| brief too vague | ask for missing fields with minimal friction |
| no proof available | downgrade claims and mark proof gap |
| stale memory dominates | raise recency filters |
| cross-domain request | route or segment the work |
| too many weak variants | reduce to fewer stronger outputs |

## Anti-Patterns

| Anti-pattern | Consequence |
|--------------|-------------|
| always maximizing variation count | cost rises, quality drops |
| stage inference without confidence check | wrong CTA pressure |
| ignoring recent test memory | repeat old mistakes |
| over-relying on brand voice docs | copy sounds polished but generic |
| forcing certainty on weak briefs | seductive nonsense |

## Properties

| Property | Value |
|----------|-------|
| Routing mode | hybrid rule-based with retrieval signals |
| Persistence style | cross-session guidance |
| Main optimization | relevance, proof, CTA coherence |
| Main caution | hype risk and stage mismatch |
| Main risk prevented | confident copy generation from thin context |
| Save path | N02_marketing/P10_memory/mem_runtime_state_n02.md |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_e2e_eval_builder]] | related | 0.21 |
| [[runtime-state-builder]] | related | 0.20 |
| [[p03_ins_runtime_state]] | related | 0.20 |
| [[p08_ac_n02]] | upstream | 0.20 |
| [[p11_qg_runtime_state]] | downstream | 0.20 |
| [[p07_sr_5d_marketing]] | upstream | 0.20 |
| [[bld_knowledge_card_runtime_state]] | upstream | 0.19 |
| [[bld_memory_runtime_state]] | related | 0.18 |
| [[p03_sp_marketing_nucleus]] | upstream | 0.18 |
| [[p03_sp_runtime_state_builder]] | upstream | 0.18 |
