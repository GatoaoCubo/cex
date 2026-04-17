---
id: kc_intelligence_vocabulary
kind: knowledge_card
pillar: P01
nucleus: n01
title: "N01 Intelligence Domain Controlled Vocabulary"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: null
tags: [controlled_vocabulary, ubiquitous_language, n01, intelligence_terms, analytical_envy, canonical]
tldr: "Canonical vocabulary for N01 Intelligence domain: 20 seed terms mapped to industry definitions, N01 application, and anti-patterns. This KC makes N01 think in correct intelligence tradecraft terminology automatically."
density_score: 0.93
---

<!-- 8F: F1 constrain=P01/knowledge_card F2 become=knowledge-card-builder F3 inject=ubiquitous-language-rule+spec_metaphor_dictionary+reasoning_strategy_n01+bias_audit_n01+all new artifacts built in W1 F4 reason=vocabulary KC is built LAST so it reflects everything N01 built, not a guess at what it needs F5 call=cex_compile F6 produce=kc_intelligence_vocabulary.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P01_knowledge/ -->

## Purpose

This KC implements the Ubiquitous Language Protocol (`.claude/rules/ubiquitous-language.md`)
for the N01 Intelligence domain.

Loading this KC at F2b SPEAK ensures that:
- All N01 outputs use canonical intelligence tradecraft terms
- CEX metaphors are transmuted to industry terms automatically
- Cross-nucleus communication is unambiguous (LLM-to-LLM interoperability)
- Vocabulary drift is prevented over time

## Canonical Vocabulary (20 Terms)

| Term | Industry Definition | N01 Domain Application | Anti-Pattern (Never Use) |
|------|-------------------|----------------------|--------------------------|
| intent_resolution | mapping user input to structured action (kind, pillar, nucleus, verb) | F1 CONSTRAIN step -- map research request to task type | "understanding what the user wants" |
| query_rewriting | rephrasing a search query to improve retrieval quality | generating 3 query variants (direct, comparative, signal) in DSTCS Step 1 | "changing the search words" |
| retrieval_augmented_generation | grounding LLM generation with retrieved documents to reduce hallucination | search_strategy -> document_loader -> synthesis pipeline | "RAG" (abbreviation only, define on first use) |
| eval_harness | infrastructure for running evaluations consistently across models/prompts | eval_framework_n01 + golden_test_n01 + benchmark_suite_n01 combined | "the testing system" |
| ground_truth | verified, authoritative correct answer for evaluation | manually verified data for golden_test calibration | "the right answer" |
| precision | fraction of retrieved results that are relevant (P = TP / (TP + FP)) | retriever_n01 performance metric at P@5, P@10 | "how accurate the results are" |
| recall | fraction of all relevant items that are retrieved (R = TP / (TP + FN)) | retriever_n01 coverage metric at R@10, R@20 | "how many results we got" |
| NDCG | Normalized Discounted Cumulative Gain -- rank-weighted relevance metric | primary ranking metric for retriever_n01 evaluation | "the ranking score" |
| knowledge_graph | directed graph where nodes=entities, edges=typed relationships | entity network in entity_memory_n01 (company -> acquires -> company) | "the connections between things" |
| citation_network | directed graph of academic papers connected by citations | citation_tracker_n01 maps this for academic research | "how papers reference each other" |
| competitive_moat | durable structural advantage that prevents competitors from competing on equal terms | D3 Comparative Coverage key signal -- what makes the lead entity hard to catch | "what makes X better" |
| market_sizing | systematic estimation of TAM/SAM/SOM using top-down and bottom-up methods | action_prompt AP-02 + kc_market_sizing_methodology.md | "how big the market is" |
| TAM_SAM_SOM | Total Addressable Market / Serviceable Addressable Market / Serviceable Obtainable Market | three-tier market sizing hierarchy in kc_market_sizing_methodology.md | "the full market / our market / our share" |
| benchmark_suite | collection of standardized tests measuring system performance against ground truth | benchmark_suite_n01.md -- 5 categories, 20 cases each | "the test set" |
| bias_detection | systematic identification of cognitive or methodological biases in research process | bias_audit_n01.md B1-B5 checks + kc_research_bias_taxonomy.md taxonomy | "checking for mistakes" |
| hallucination_rate | fraction of LLM-generated claims not supported by cited sources | llm_judge_n01 metric -- target < 5% for N01 outputs | "making things up rate" |
| information_retrieval | field of study focused on finding relevant information from large collections | core discipline behind retriever_n01 (BM25 + dense + RRF) | "searching for stuff" |
| structured_extraction | transforming unstructured text into typed data conforming to a schema | data_extractor_n01 -- text -> CompetitorProfile / PricingData / MarketSignal | "pulling data from text" |
| corpus_analysis | systematic analysis of a document collection to identify patterns and insights | retriever_n01 querying the N01 corpus (167+ artifacts) | "looking at all the documents" |
| source_triangulation | confirming a claim by finding >= 3 independent sources that agree | N01 hard gate H01 -- mandatory for all major claims | "checking multiple sources" |
| evidence_grading | assigning quality scores to sources based on reliability and credibility | N01 source scoring system (A1-F6 from IC standard) in kc_competitive_intelligence_methods.md | "judging source quality" |

## Cross-Nucleus Shared Terms (DO NOT REDEFINE HERE)

These terms are defined in N00_genesis and are imported, not redefined:

| Term | Definition Source | N01 Application |
|------|-----------------|----------------|
| 8F pipeline | `.claude/rules/8f-reasoning.md` | N01 follows F1-F8 for every research task |
| kind | `.cex/kinds_meta.json` | N01 produces kinds: knowledge_card, research_pipeline, etc. |
| pillar | N00_genesis P01-P12 | N01 primary: P01, P07, P04, P10, P03 |
| quality_gate | P07 definition | N01 quality_gate_intelligence.md implements for research domain |
| signal | F8 COLLABORATE convention | N01 signals: `write_signal('n01', 'complete', score)` |

## Trigger Phrases -> Combo Activation

| User Phrase | Activates Combo | Action |
|-------------|----------------|--------|
| "research", "analyze", "investigate" | COMBO A (Intelligence Pipeline) | load research_pipeline + search_strategy + document_loader |
| "find in corpus", "search knowledge base", "what do we know" | COMBO B (RAG Stack) | load retriever + knowledge_index + embedding_config |
| "evaluate", "score", "how good is", "benchmark" | COMBO C (Eval Intelligence) | load eval_framework + llm_judge + scoring_rubric + benchmark_suite |
| "schema", "API spec", "data contract" | COMBO D (Schema) | load input_schema + api_reference + type_def |
| "remember", "persist", "track over time", "what did we know before" | COMBO E (Persistent Memory) | load entity_memory + knowledge_index + memory_architecture |

## Vocabulary Load Protocol

At F2b SPEAK:
```
load: N01_intelligence/P01_knowledge/kc_intelligence_vocabulary.md
load: _docs/specs/spec_metaphor_dictionary.md (Industry term column)
activate: drift_prevention = True
```

All subsequent F3-F8 output must use terms from this KC.
Violation detection: F7 GOVERN H07 checks for vocabulary compliance.
