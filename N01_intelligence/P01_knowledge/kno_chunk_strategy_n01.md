---
id: kno_chunk_strategy_n01
kind: chunk_strategy
8f: F3_inject
pillar: P01
nucleus: N01
title: "N01 Chunk Strategy"
version: "1.0.0"
quality: 9.0
tags: [chunk_strategy, n01, p01, analytical_envy, retrieval]
density_score: 0.97
related:
  - chunk-strategy-builder
  - bld_collaboration_chunk_strategy
  - n01_emb_text_embedding_4
  - p01_kc_chunk_strategy
  - p10_lr_chunk_strategy_builder
  - p01_chunk_strategy
  - bld_knowledge_card_chunk_strategy
  - bld_examples_chunk_strategy
  - p01_kc_rag_chunking_strategies
  - p01_cs_recursive_1000
---
<!-- 8F: F1=chunk_strategy/P01 F2=kc_chunk_strategy+tpl_chunk_strategy F3=nucleus_def_n01+kc_chunk_strategy+ex_chunk_strategy_recursive_1000+source_quality_contract F4=hybrid comparative ingestion spec
     F5=rg+Get-Content+apply_patch F6=target dense markdown artifact F7=self-check properties+8F+ascii+80lines F8=N01_intelligence/P01_knowledge/kno_chunk_strategy_n01.md -->

# N01 Chunk Strategy

## Purpose
N01 does not chunk to merely fit context.
N01 chunks to outperform weaker evidence packs.
The strategy is designed for research artifacts, competitor dossiers, paper notes, and citation-heavy intelligence briefs.
Analytical Envy means every split must preserve comparative signal, not just semantic continuity.
If a chunk hides the delta between two sources, the chunk is wrong even when retrieval still works.

## Properties

| Property | Value |
|----------|-------|
| Kind | `chunk_strategy` |
| Pillar | `P01` |
| Nucleus | `N01` |
| Lens | `Analytical Envy` |
| Primary corpus | research briefs, competitor pages, papers, source notes |
| Default method | hierarchical recursive with comparison anchors |
| Default chunk_size | 900 tokens |
| Default chunk_overlap | 180 tokens |
| Quality target | preserve claims, counters, and provenance together |
| Failure mode to avoid | chunks that separate a claim from its evidence or rival benchmark |

## Why N01 Needs A Different Splitter
Generic RAG chunking optimizes for topical coherence.
N01 needs comparative coherence.
That means the unit of retrieval is often:
- claim plus benchmark
- feature plus competitor contrast
- source quote plus reliability note
- trend statement plus freshness qualifier
- pricing claim plus region and date

The chunker must keep those paired facts together.
If a citation is detached from the sentence it grounds, N01 loses proof pressure.
If competitor A and competitor B land in unrelated chunks, synthesis drifts into vague summary.

## Strategy Profile

| Field | Setting | N01 reason |
|-------|---------|------------|
| method | `hierarchical_recursive` | Respects headings, tables, and evidence blocks |
| token_counter | `cl100k_base_compatible` | Aligns with modern long-context models |
| chunk_size | `900` | Large enough for comparison sets, small enough for precise recall |
| chunk_overlap | `180` | Keeps adjacent evidence windows connected |
| heading_priority | `h2 > h3 > paragraph > sentence` | Preserves report structure before raw length |
| table_policy | `keep_table_with_intro_or_footer` | Matrices are meaningless without labels |
| quote_policy | `bind_quote_to_source_line` | Citation must travel with excerpt |
| metadata_policy | `inherit_and_extend` | Each chunk carries source, date, entity, topic, and confidence |

## Boundary Rules
1. Split first on report sections that imply analytical mode: market, pricing, strengths, weaknesses, evidence, appendix.
2. Keep comparative statements and the contrasted entities in the same chunk whenever possible.
3. Keep a source excerpt with its provenance line, access date, and reliability marker.
4. Never split a table header from the first data row.
5. Never split a bullet list of competitor dimensions across more than two chunks.
6. Merge orphan headings into the following body block.
7. Extend the chunk if a sentence contains date, region, or unit qualifiers needed for interpretation.
8. Cap extension when the chunk would exceed 1200 tokens.

## Comparative Anchors
Analytical Envy requires explicit anchors that ordinary chunkers ignore.

| Anchor type | Example | Handling rule |
|-------------|---------|---------------|
| benchmark pair | "Company A latency vs Company B latency" | keep in one chunk |
| freshness clause | "as of 2026-04-16" | attach to the claim sentence |
| reliability note | "tier_2 official docs" | store in metadata and local text |
| counterclaim | "vendor says X, reviews say Y" | do not split between sides |
| unit qualifier | USD, region, monthly, annual | preserve with metric |
| confidence tag | high, medium, low | preserve in metadata |

## Metadata Schema
Each chunk should emit metadata that sharpens downstream retrieval instead of adding noise.

| Metadata key | Example value | Why N01 cares |
|--------------|---------------|---------------|
| source_id | `cit_openai_pricing_2026q2` | trace to citation card |
| source_type | `official_doc` | reliability weighting |
| entity_primary | `OpenAI` | main retrieval handle |
| entity_secondary | `Anthropic` | comparison handle |
| topic | `pricing` | battle card routing |
| comparison_axis | `cost_per_1m_tokens` | matrix synthesis |
| region | `global` | avoids false comparisons |
| date_claim | `2026-04-16` | freshness audit |
| reliability_tier | `tier_2` | trust weighting |
| contradiction_flag | `false` | reranker can prioritize conflicts |

## Recommended Flow
1. Parse headings and tables.
2. Detect entity mentions and comparative phrases.
3. Build candidate chunks around structural boundaries.
4. Expand candidates when a claim lacks provenance or rival context.
5. Attach metadata before embedding.
6. Reject chunks that do not contain a usable analytical unit.

## Good And Bad Examples

| Case | Result | Verdict |
|------|--------|---------|
| Pricing section with vendor quote and date intact | retrieval can answer how much and when | good |
| Feature list split away from competitor names | synthesis loses comparison | fail |
| Table plus notes plus footnote source retained | procurement evaluation stays grounded | good |
| Benchmark sentence split before units | metric becomes ambiguous | fail |

## Operational Defaults
- Use this strategy for competitor landing pages, public docs, pricing pages, PDFs converted to markdown, and structured research notes.
- Downgrade to sentence mode only for short review snippets under 250 tokens.
- Use larger 1100 token windows for academic papers with dense method sections.
- Use smaller 600 token windows for forum or review corpora with high topical drift.

## Governance Checks
1. Does each chunk answer a research question, not just hold text.
2. Can a reviewer tell what source and date a claim came from.
3. Does the chunk preserve the opposing benchmark when one exists.
4. Are units, currencies, and regions still attached.
5. Would a reranker see enough signal to prefer the chunk for a comparative query.

## N01 Decision
The default N01 splitter is not recursive markdown.
It is a comparison-preserving recursive splitter.
That distinction matters because N01 exists to rank, challenge, and surpass competing evidence.
Chunking is therefore the first analytical act in the pipeline, not a preprocessing footnote.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[chunk-strategy-builder]] | related | 0.31 |
| [[bld_collaboration_chunk_strategy]] | downstream | 0.29 |
| [[n01_emb_text_embedding_4]] | related | 0.28 |
| [[p01_kc_chunk_strategy]] | related | 0.28 |
| [[p10_lr_chunk_strategy_builder]] | downstream | 0.28 |
| [[p01_chunk_strategy]] | sibling | 0.28 |
| [[bld_knowledge_card_chunk_strategy]] | related | 0.27 |
| [[bld_examples_chunk_strategy]] | downstream | 0.27 |
| [[p01_kc_rag_chunking_strategies]] | related | 0.26 |
| [[p01_cs_recursive_1000]] | sibling | 0.25 |
