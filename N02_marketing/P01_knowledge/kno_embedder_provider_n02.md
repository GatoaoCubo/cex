---
id: kno_embedder_provider_n02
kind: embedder_provider
8f: F3_inject
pillar: P02
nucleus: N02
title: "N02 Marketing Embedder Provider"
version: "1.0.0"
quality: 9.1
tags: [embedder_provider, marketing, embeddings, retrieval, creative_lust, n02]
density_score: 1.0
related:
  - p01_emb_openai_text_embedding_3_small
  - p01_kc_embedder_provider
  - p06_schema_embedding
  - bld_examples_embedder_provider
  - p01_kc_vector_embedding_model_selection
  - bld_knowledge_card_embedding_config
  - p01_kc_embedding_config
  - p03_ins_embedder_provider
  - p03_sp_embedder_provider_builder
  - embedder-provider-builder
---
<!-- 8F: F1=embedder_provider/P01 F2=embedder-provider-builder F3=nucleus_def_n02+kc_campaign+ab_testing_framework+P01_schema+N02_memory F4=provider_choice_for_conversion_copy_similarity F5=shell_command,apply_patch F6=approx_6kb F7=frontmatter+8F+80_lines+dense_tables+self_check_pass F8=N02_marketing/P01_knowledge/kno_embedder_provider_n02.md -->

# Purpose

| Property | Value |
|----------|-------|
| Kind | embedder_provider |
| Pillar | P01 |
| Nucleus | N02 |
| Role | encode marketing artifacts for semantic recall |
| Creative Lust lens | similarity must capture desire pattern, not just topic overlap |
| Selection intent | retrieve copy that feels behaviorally relevant at campaign time |

## Provider Decision

N02 should use an embedding stack optimized for nuanced text retrieval across short and mid-length marketing assets.
The recommended provider profile is OpenAI `text-embedding-3-large` for primary indexing.
The fallback profile is OpenAI `text-embedding-3-small` for lower-cost rebuilds and batch experimentation.

## Why This Provider Fits N02

| Requirement | Need | Provider fit |
|-------------|------|--------------|
| short-form ad recall | hooks and CTA language must remain distinguishable | strong |
| long-form landing sections | proof and objection clusters need stable vectors | strong |
| cross-channel retrieval | email, ads, LPs, and brand docs share one semantic field | strong |
| dimension flexibility | cost tiering for experiments matters | available |
| operational simplicity | N02 already rate-limits around OpenAI | aligned |

## Recommended Configuration Matrix

| Parameter | Primary value | Fallback value | Why |
|-----------|---------------|----------------|-----|
| provider | openai | openai | matches N02 runtime config |
| model | text-embedding-3-large | text-embedding-3-small | quality vs cost split |
| dimensions | 3072 | 1536 | richer semantic separation for persuasive nuance |
| dimensions_override | null | null | keep default dimensions for stable comparisons |
| distance_metric | cosine | cosine | aligns with normalized semantic ranking |
| normalize | yes at query service | yes at query service | stable hybrid ranking |
| batch_size | 64 texts | 96 texts | medium corpus, bounded concurrency |
| max_input_role | 320 token chunks | 320 token chunks | matches chunk strategy |

## Semantic Goals

| Goal | Encoding behavior |
|------|-------------------|
| audience match | map similar pains and aspirations close together |
| funnel match | separate awareness hooks from decision-stage closers |
| proof match | keep outcome-led evidence near related claims |
| tone match | distinguish authoritative, playful, urgent, and premium voice modes |
| CTA match | preserve action intent without overpowering topical meaning |

## What Must Be Embedded

1. chunk text
2. funnel stage
3. channel
4. audience segment
5. CTA type
6. proof type
7. offer family

The embed payload should not be raw text only.
It should be a structured serialization that exposes persuasion metadata.

## Canonical Embed Payload

```yaml
embed_payload:
  channel: linkedin_ad
  funnel_stage: tofu
  audience_segment: b2b_saas_founder
  proof_type: metric
  cta_type: soft_demo
  offer_family: audit
  body: "Stop paying for clicks that never turn into pipeline..."
```

## Retrieval Tradeoffs

| Choice | Benefit | Cost |
|--------|---------|------|
| large model | better nuance across adjacent copy variants | higher storage and rebuild cost |
| small model | cheaper experiments and rebuilds | weaker discrimination on subtle tone shifts |
| payload metadata included | better stage and offer recall | slightly more index size |
| raw body only | simpler pipeline | weaker behavioral match |

## Creative Lust Implications

N02 content wins when the system remembers not only what was said, but how the desire was staged.
Embedding must therefore preserve:

| Signal | Example |
|--------|---------|
| aspiration | become the team that ships faster |
| tension | still paying for traffic that leaks |
| proof | 23 percent lift in qualified demos |
| invitation | book the audit now |

If embeddings compress these into one vague "marketing" neighborhood, retrieval becomes generic.
Generic retrieval is the enemy of seduction.

## Cost Governance

| Mode | When to use | Rule |
|------|-------------|------|
| primary_high_fidelity | production retrieval | use large model |
| experiment_fast | A/B bulk ingest or draft corpora | use small model |
| rebuild_conservation | 80 percent daily spend reached | pause full large-model rebuild |
| fallback_recovery | provider pressure or quota hit | switch to small model temporarily |

## Integration Pattern

```yaml
embedding_flow:
  source: marketing_chunk
  serializer: chunk_plus_metadata
  provider: openai
  model: text-embedding-3-large
  write_to: qdrant_marketing_collection
  read_by: hybrid_retriever_n02
```

## Operational Rules

1. Rebuild large embeddings after major corpus changes in campaign history or brand voice.
2. Use identical serialization for documents and queries.
3. Keep brand style rules indexed, but lower their ranking weight than live performance evidence.
4. Never mix unrelated nuclei embeddings inside the same N02 collection namespace.
5. Log model version on each rebuild for auditability.

## Anti-Patterns

| Anti-pattern | Failure mode |
|--------------|--------------|
| mixing large and small vectors in one collection | retrieval instability |
| embedding unstructured markdown noise | metadata gets buried |
| excluding CTA metadata | action intent retrieval weakens |
| excluding proof markers | hype rises above evidence |
| reusing product-search embeddings for copy retrieval | commercial nuance is lost |

## Decision Summary

| Decision area | Choice |
|---------------|--------|
| primary provider | OpenAI |
| primary model | text-embedding-3-large |
| fallback model | text-embedding-3-small |
| metric | cosine |
| strategy | metadata-enriched embeddings |
| north star | behavioral similarity for conversion work |

## Properties

| Property | Value |
|----------|-------|
| Primary model | text-embedding-3-large |
| Fallback model | text-embedding-3-small |
| Main retrieval gain | better tone, stage, and proof matching |
| Main operational guard | spend-aware rebuild tiers |
| Main risk prevented | semantically similar but tactically wrong recalls |
| Save path | N02_marketing/P01_knowledge/kno_embedder_provider_n02.md |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_emb_openai_text_embedding_3_small]] | sibling | 0.41 |
| [[p01_kc_embedder_provider]] | upstream | 0.34 |
| [[p06_schema_embedding]] | downstream | 0.34 |
| [[bld_examples_embedder_provider]] | downstream | 0.33 |
| [[p01_kc_vector_embedding_model_selection]] | upstream | 0.32 |
| [[bld_knowledge_card_embedding_config]] | upstream | 0.32 |
| [[p01_kc_embedding_config]] | upstream | 0.28 |
| [[p03_ins_embedder_provider]] | downstream | 0.27 |
| [[p03_sp_embedder_provider_builder]] | downstream | 0.27 |
| [[embedder-provider-builder]] | related | 0.26 |
