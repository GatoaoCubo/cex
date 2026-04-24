---
id: kno_chunk_strategy_n02
kind: chunk_strategy
8f: F3_inject
pillar: P01
nucleus: N02
title: "N02 Marketing Chunk Strategy"
version: "1.0.0"
quality: 9.1
tags: [chunk_strategy, marketing, retrieval, campaigns, creative_lust, n02]
density_score: 1.0
related:
  - p01_cs_recursive_1000
  - p10_lr_chunk_strategy_builder
  - bld_knowledge_card_chunk_strategy
  - p01_kc_chunk_strategy
  - p07_sr_5d_marketing
  - p01_kc_rag_chunking_strategies
  - chunk-strategy-builder
  - bld_examples_chunk_strategy
  - bld_collaboration_chunk_strategy
  - p08_ac_n02
---
<!-- 8F: F1=chunk_strategy/P01 F2=chunk-strategy-builder F3=nucleus_def_n02+kc_campaign+ab_testing_framework+P01_schema+P10_schema F4=hybrid_chunking_for_marketing_copy_and_proof F5=shell_command,apply_patch F6=approx_6kb F7=frontmatter+8F+80_lines+dense_tables+self_check_pass F8=N02_marketing/P01_knowledge/kno_chunk_strategy_n02.md -->

# Purpose

| Property | Value |
|----------|-------|
| Kind | chunk_strategy |
| Pillar | P01 |
| Nucleus | N02 |
| Domain | campaign copy, ads, landing pages, brand voice |
| Primary objective | preserve persuasion arcs without smearing proof across chunks |
| Creative Lust lens | desire must stay attached to proof, CTA, and audience tension |

## Operating Thesis

N02 does not chunk generic text.
N02 chunks persuasion systems.
Each chunk must preserve the emotional hook, the proof signal, the stage of the funnel, and the intended next action.
If desire is separated from evidence, retrieval returns seductive nonsense.
If evidence is separated from the CTA, retrieval returns sterile notes that do not convert.

## Retrieval Unit Design

| Unit | Why it exists | Default target |
|------|---------------|----------------|
| hook block | stores the attention pattern and audience pain | 80-140 tokens |
| proof block | keeps stats, testimonials, and outcome claims together | 90-160 tokens |
| CTA block | captures action language and offer timing | 50-110 tokens |
| objection block | preserves friction and resolution logic | 80-150 tokens |
| full section block | used when a landing page section carries a complete argument | 180-320 tokens |

## Chunking Method

| Setting | Value | Rationale |
|---------|-------|-----------|
| method | hierarchical_semantic_marketing | start with structure, then tighten by semantic boundary |
| primary splitter | markdown heading plus campaign field labels | most N02 artifacts are structured markdown |
| secondary splitter | sentence cluster by hook-proof-CTA role | keeps persuasive rhythm intact |
| chunk_size | 260 tokens target | large enough for a full micro-argument |
| chunk_overlap | 45 tokens | keeps tone and offer continuity |
| min_chunk_size | 90 tokens | avoids fragments with no tactical value |
| max_chunk_size | 340 tokens | prevents mixed stages in one retrieval hit |
| tokenizer | cl100k style budget assumption | aligned with current N02 provider profile |
| keep_separator | yes | headings and labels matter for funnel stage |
| strip_whitespace | yes | reduces noisy vectors |

## Boundary Rules

| Rule | Decision |
|------|----------|
| split on stage change | yes |
| split on audience segment change | yes |
| split on CTA change | yes |
| split on proof source change | yes |
| split on visual description only | no, unless visual changes the claim |
| split inside testimonial quote | no |

## Marketing-Aware Separators

| Separator | Priority | Meaning |
|-----------|----------|---------|
| `##` | 1 | major persuasion block |
| `###` | 2 | sub-argument or channel slice |
| `Audience:` | 3 | persona boundary |
| `Offer:` | 3 | value exchange boundary |
| `Proof:` | 3 | evidence boundary |
| `CTA:` | 3 | action boundary |
| paragraph break | 4 | fallback logical pause |
| sentence break | 5 | last-resort precision split |

## Corpus-Specific Policies

| Corpus type | Strategy |
|-------------|----------|
| landing pages | chunk by section first, then by hook-proof-CTA trio |
| ad variants | one variant per chunk unless proof spills over two lines |
| email sequences | one email block per chunk, plus sub-chunk for CTA if reused |
| A/B reports | keep hypothesis, metric, result, and insight together |
| brand voice docs | chunk by principle, anti-pattern, and approved example |

## Why This Fits Creative Lust

The Lust lens is not decoration.
It is the rule that makes chunking respect desire flow.
Desire in N02 is built from tension, aspiration, proof, and invitation.
Chunks must preserve that seduction loop:

```yaml
seduction_loop:
  trigger: audience_pain_or_desire
  intensifier: contrast_or_specific_outcome
  proof: stat_testimonial_or_case
  invitation: cta_or_offer
```

## Retrieval Consequences

| If chunking is too small | Result |
|--------------------------|--------|
| hook isolated | empty hype returned |
| proof isolated | cold evidence with no narrative |
| CTA isolated | generic action language |

| If chunking is too large | Result |
|--------------------------|--------|
| multiple funnel stages mixed | routing confusion |
| variant families fused | weak A/B contrast |
| audience segments blended | wrong tone at generation time |

## Assembly Rules

1. Prefer chunks containing one complete persuasion move.
2. Attach metadata for `funnel_stage`, `channel`, `audience_segment`, and `cta_type`.
3. Promote chunks with explicit metrics, outcomes, or objection handling.
4. Down-rank chunks that are purely visual polish without conversion logic.
5. Never merge two different offers into the same chunk.

## Example

```yaml
example_chunk:
  funnel_stage: mofu
  channel: landing_page
  audience_segment: b2b_saas
  chunk_role: proof_block
  token_count: 214
  overlap_from_previous: 41
  preserved_fields:
    - hook
    - proof
    - objection
    - cta
```

## Anti-Patterns

| Anti-pattern | Why it fails |
|--------------|--------------|
| fixed 500-token chunks everywhere | ignores persuasion boundaries |
| paragraph-only splitting | loses stage labels and offer transitions |
| no overlap | breaks tonal continuity |
| aggressive dedupe before chunking | removes repeated CTA context needed for ranking |
| merging brand rules with campaign metrics | retrieval returns mismatched guidance |

## Governance Checklist

| Check | Pass condition |
|-------|----------------|
| stage integrity | one dominant funnel stage per chunk |
| proof integrity | proof stays attached to its claim |
| CTA integrity | action language stays with local promise |
| audience integrity | one audience assumption per chunk |
| density | chunk is useful without surrounding file |

## Properties

| Property | Value |
|----------|-------|
| Chunk target | 260 tokens |
| Overlap target | 45 tokens |
| Primary split mode | heading plus persuasion role |
| Metadata anchors | stage, channel, audience, CTA |
| Best suited for | campaign docs, ads, emails, landing pages |
| Main risk prevented | seductive but contextless retrieval |
| Save path | N02_marketing/P01_knowledge/kno_chunk_strategy_n02.md |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_cs_recursive_1000]] | sibling | 0.27 |
| [[p10_lr_chunk_strategy_builder]] | downstream | 0.27 |
| [[bld_knowledge_card_chunk_strategy]] | related | 0.26 |
| [[p01_kc_chunk_strategy]] | related | 0.26 |
| [[p07_sr_5d_marketing]] | downstream | 0.25 |
| [[p01_kc_rag_chunking_strategies]] | related | 0.24 |
| [[chunk-strategy-builder]] | related | 0.24 |
| [[bld_examples_chunk_strategy]] | downstream | 0.24 |
| [[bld_collaboration_chunk_strategy]] | downstream | 0.24 |
| [[p08_ac_n02]] | downstream | 0.23 |
