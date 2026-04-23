---
id: kno_chunk_strategy_n06
kind: chunk_strategy
pillar: P01
nucleus: n06
title: Commercial Chunk Strategy
version: 1.0
quality: 9.0
tags: [knowledge, chunk_strategy, rag, pricing, funnels, monetization]
density_score: 1.0
related:
  - bld_collaboration_chunk_strategy
  - chunk-strategy-builder
  - p10_lr_chunk_strategy_builder
  - p01_kc_chunk_strategy
  - bld_knowledge_card_chunk_strategy
  - p08_pat_pricing_framework
  - p01_kc_rag_chunking_strategies
  - bld_config_chunk_strategy
  - n06_commercial
  - bld_examples_chunk_strategy
---
<!-- 8F: F1=P01/chunk_strategy F2=chunk-strategy-builder F3=nucleus_def_n06.md,kc_chunk_strategy.md,P01_knowledge/_schema.yaml,N06 W1 config/schema F4=revenue_weighted_recursive_chunking_for_commercial_retrieval F5=apply_patch;python _tools/cex_compile.py F6=author_dense_markdown_artifact F7=frontmatter_ascii_density_linecount_review F8=N06_commercial/P01_knowledge/kno_chunk_strategy_n06.md -->

# Commercial Chunk Strategy

## Purpose

| Field | Value |
|-------|-------|
| Goal | Split commercial knowledge into retrieval units that preserve buying context, pricing logic, and conversion leverage |
| Business Lens | Strategic Greed values chunks by revenue yield, not by document symmetry |
| Primary Use | retrieval for pricing pages, offer design, checkout friction diagnosis, renewal rescue, and upsell prompts |
| Failure Prevented | high-value evidence buried inside oversized docs or diluted inside generic marketing chunks |
| Default Method | recursive_segment_priority |
| Retrieval Bias | premium offers, objections, margin rules, and segment-specific proof stay intact |

## Method

| Setting | Value | Rationale |
|---------|-------|-----------|
| method | `recursive_segment_priority` | respects doc structure while forcing monetization boundaries |
| chunk_size | `540` tokens | enough room for one offer block plus proof and objection |
| chunk_overlap | `90` tokens | keeps CTA, pricing anchor, and proof transitions connected |
| separators | `["## ","### ","\\n\\n","\\n","; ",". "]` | commercial docs usually turn on headers, paragraph breaks, and list punctuation |
| min_chunk_size | `180` tokens | rejects thin fragments that cannot support a business decision |
| max_tables_per_chunk | `1` | pricing tables become noisy when merged with unrelated copy |
| hard_boundary_labels | `pricing`, `offer`, `segment`, `objection`, `renewal`, `upsell` | protects revenue-critical sections from accidental merge |

## Revenue Priority Rules

| Rule ID | Chunk Trigger | Action | Why N06 Wants It |
|---------|---------------|--------|------------------|
| CS01 | premium tier table detected | isolate as standalone chunk | premium anchors should retrieve cleanly |
| CS02 | objection plus counter-objection pair | keep in same chunk | sales resistance only matters with the answer attached |
| CS03 | renewal risk playbook section | preserve surrounding thresholds and scripts | retention logic fails when timing rules split away |
| CS04 | free-tier limits described | bind limits with upgrade CTA | prevents retrieval of generosity without monetization path |
| CS05 | case study contains revenue metrics | keep proof with segment label | proof converts best when segment match survives retrieval |
| CS06 | bundle description spans many bullets | compress into one bounded chunk if same offer | fragmented bundles lower recommendation confidence |

## Source-Type Handling

| Source Type | Strategy | Boundary Rule | Commercial Intent |
|-------------|----------|---------------|-------------------|
| pricing frameworks | recursive by header | one pricing model per chunk | keeps monetization logic atomic |
| funnel teardown | stage-based chunking | each funnel stage gets its own unit | diagnose leakage precisely |
| offer docs | offer-block chunking | one offer per chunk unless nested upsell | preserve conversion package integrity |
| battlecards | objection-led chunking | one objection cluster per chunk | fast rebuttal retrieval for sales prompts |
| retention playbooks | trigger-led chunking | one save motion per chunk | save tactics should be callable by risk state |
| competitor notes | plan-anchor chunking | one competitor plus one pricing axis | enables clean side-by-side retrieval |

## Metadata to Attach

| Metadata Key | Example | Why It Matters |
|--------------|---------|----------------|
| revenue_stage | `acquire`, `convert`, `expand`, `retain` | supports stage-aware retrieval |
| segment_value | `starter`, `growth`, `scale`, `enterprise` | high-LTV routes can ask for premium evidence first |
| offer_type | `trial`, `core_plan`, `annual`, `bundle`, `enterprise` | offer-specific retrieval lowers prompt waste |
| margin_sensitivity | `high`, `medium`, `low` | margin protection can outrank raw conversion |
| intent_signal | `cold`, `warm`, `active_checkout`, `renewal_risk` | retrieval should follow proximity to cash |
| proof_present | `true`, `false` | proof-rich chunks rerank better for persuasion tasks |

## Assembly Logic

| Step | Action | Output |
|------|--------|--------|
| 1 | detect commercial document type | source profile |
| 2 | map headers to revenue stages | stage-tagged sections |
| 3 | split recursively using hard boundaries first | candidate chunks |
| 4 | merge only adjacent chunks with same stage and segment | revenue-coherent units |
| 5 | attach metadata and rank class | index-ready chunks |
| 6 | reject thin or mixed-intent chunks | higher signal corpus |

## Rationale

| Design Choice | Why It Exists | Strategic Greed Impact |
|---------------|---------------|------------------------|
| Larger-than-default chunk size | commercial persuasion needs claim plus proof plus CTA | higher retrieval usefulness per hit |
| Strong overlap | pricing anchors often reference adjacent objections | avoids losing conversion logic at boundaries |
| Hard boundary labels | revenue sections are more valuable than generic prose | keeps premium context pure |
| Metadata per chunk | retrieval quality depends on buying stage, not only semantics | routes cash-near questions to cash-near evidence |
| Thin chunk rejection | small fragments sound clever but convert poorly | protects generation quality |

## Example

| Scenario | Result |
|----------|--------|
| A pricing doc contains Free, Pro, and Enterprise sections with proof blocks and upgrade CTAs | each plan becomes a separate chunk set with linked proof and intent metadata |

```yaml
name: commercial_recursive_segment_priority
method: recursive_segment_priority
chunk_size: 540
chunk_overlap: 90
separators:
  - "## "
  - "### "
  - "\n\n"
  - "\n"
metadata_keys:
  - revenue_stage
  - segment_value
  - offer_type
  - margin_sensitivity
```

## Governance

| Check | Pass Condition |
|-------|----------------|
| boundary purity | chunk contains one dominant revenue stage |
| plan integrity | no tier table split across chunks |
| proof linkage | claim and commercial proof remain together |
| ascii safety | identifiers and config keys remain unaccented |
| density | every chunk can answer a revenue question without outside rescue |

## Properties

| Property | Value |
|----------|-------|
| Owner | N06 Commercial |
| Kind | `chunk_strategy` |
| Method | `recursive_segment_priority` |
| Default Chunk Size | 540 tokens |
| Default Overlap | 90 tokens |
| Index Bias | revenue-stage aware |
| Main Tradeoff | slight storage growth for better conversion-context recall |
| Related Artifacts | `kno_retriever_config_n06`, `kno_vector_store_n06`, `mem_knowledge_index_n06` |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_chunk_strategy]] | downstream | 0.31 |
| [[chunk-strategy-builder]] | related | 0.31 |
| [[p10_lr_chunk_strategy_builder]] | downstream | 0.28 |
| [[p01_kc_chunk_strategy]] | related | 0.26 |
| [[bld_knowledge_card_chunk_strategy]] | related | 0.25 |
| [[p08_pat_pricing_framework]] | downstream | 0.24 |
| [[p01_kc_rag_chunking_strategies]] | related | 0.23 |
| [[bld_config_chunk_strategy]] | downstream | 0.23 |
| [[n06_commercial]] | downstream | 0.22 |
| [[bld_examples_chunk_strategy]] | downstream | 0.22 |
