---
id: audit_intent_resolution
kind: knowledge_card
pillar: P01
title: Audit Report -- Intent Resolution Artifacts
version: 1.0.0
created: 2026-04-08
author: n03_builder
domain: meta-construction/intent-resolution
quality: 9.0
tags: [audit, intent-resolution, canonicalization, motor, query, transmutation]
tldr: "Audit of 6 artifacts that participate in intent resolution. 21 kinds unreachable, 2 stale refs, verb coverage at 54%."
density_score: 0.92
---

# Audit Report: Intent Resolution Artifacts

## Executive Summary

| Metric | Value | Status |
|--------|-------|--------|
| Total kinds in taxonomy | 123 | Baseline |
| Kinds reachable via OBJECT_TO_KINDS | 102 | 83% |
| Kinds unreachable from natural language | 21 | [FAIL] 17% gap |
| Stale kind references in motor | 2 | [FAIL] |
| PT verb coverage | 7 actions (12 conjugations) | [WARN] 54% of common actions |
| EN verb coverage | 0 | [FAIL] |
| Intent resolution rule examples | 8 | [WARN] covers 6% of use cases |
| Metaphor dictionary entries | 64 | [OK] but no kind-level mapping |
| TF-IDF fallback (cex_query.py) | Functional | [WARN] only searches bld_manifest |

## Artifact 1: n07-input-transmutation.md

**Role in intent resolution:** Defines the 5-step intent resolution protocol (capture > map > resolve > restate > execute). Contains the primary mapping table and 12-pillar mastery reference.

**Strengths:**
- Clear 5-step protocol
- 8F pipeline mastery table maps functions to N07 roles
- 12-pillar table provides pillar > domain > example kinds

**Gaps found:**

| Gap | Severity | Impact |
|-----|----------|--------|
| Only 8 mapping examples | High | Covers 6% of real user intent patterns |
| No Portuguese trigger phrases | High | User is PT-native, most input in Portuguese |
| Missing P06/P09/P10/P11 in mapping table | Medium | 4 pillars have zero direct mapping examples |
| Pillar table shows only 3 kinds each (36/123) | Low | Not exhaustive but gives direction |
| No mention of industry terms (intent resolution, query rewriting, prompt optimization) | Medium | Transmutation is the internal metaphor -- industry uses 3 terms depending on pipeline stage |

**Recommendation:** Expand mapping table to cover all 12 pillars with at least 3 examples each. Add Portuguese trigger phrases. Reference intent resolution map artifact for exhaustive coverage.

## Artifact 2: n07-technical-authority.md

**Role in intent resolution:** Teaching protocol for metaphor-to-industry-term translation. Defines the TRANSMUTE > STRESS > TEACH behaviors.

**Strengths:**
- Clear 10-entry translation table for game metaphors
- Teaching protocol (state correct > source > why > mapping > move on)
- Self-correction acknowledgment protocol

**Gaps found:**

| Gap | Severity | Impact |
|-----|----------|--------|
| Translation table limited to game metaphors (10 entries) | Medium | 54 other metaphors in dictionary not covered |
| No kind-specific mappings | Medium | Cannot help with "I want a validator" > kind:validator |
| No PT variant tracking | Low | Only teaches EN industry terms |
| Memory-based tracking not automated | Low | Relies on N07 manually updating memory |

**Recommendation:** Add kind-resolution as a first-class behavior. Reference the intent resolution map for exhaustive kind mappings.

## Artifact 3: spec_metaphor_dictionary.md

**Role in intent resolution:** Master translation table from user metaphors to industry terms. 64 entries across 6 categories (game, architecture, process, quality, brand, and a general catch-all).

**Strengths:**
- Comprehensive metaphor coverage (64 entries)
- 4-column structure: user says > system means > industry term > CEX implementation
- Clear rules for usage (artifacts use industry terms, accept user metaphors)
- Llama-7B readability test

**Gaps found:**

| Gap | Severity | Impact |
|-----|----------|--------|
| No kind-level intent mapping | High | Metaphors describe concepts, not target kinds |
| No verb-to-action mapping | Medium | Only covers nouns/concepts, not "criar", "testar" |
| No pillar routing hints | Medium | Reader cannot derive pillar from metaphor alone |
| No examples of compound intent | Low | "build me an agent that validates" needs decomposition |

**Recommendation:** This artifact covers concept-level translation well. Kind-level and verb-level resolution belong in separate artifacts (intent resolution map and motor VERB_TABLE respectively).

## Artifact 4: kinds_meta.json

**Role in intent resolution:** The canonical registry of all 123 kinds. Every intent ultimately resolves to one or more kind entries here. Contains descriptions, boundaries, pillars, naming patterns, and llm_function.

**Strengths:**
- Complete (123 kinds registered)
- Boundary field disambiguates similar kinds
- llm_function field maps kind to 8F pipeline stage
- Description field supports TF-IDF search

**Gaps found:**

| Gap | Severity | Impact |
|-----|----------|--------|
| 21 kinds not in OBJECT_TO_KINDS | High | 17% unreachable via direct keyword |
| Descriptions in PT only | Medium | EN queries may miss matches |
| No `trigger_phrases` field | Medium | Natural language triggers not stored with kind |
| No `nucleus` routing field | Low | Nucleus must be inferred from pillar |

**21 unreachable kinds:**

| Kind | Pillar | Added |
|------|--------|-------|
| citation | P01 | -- |
| compression_config | P10 | 10.0.0 |
| content_monetization | P11 | -- |
| context_window_config | P03 | -- |
| landing_page | P05 | -- |
| memory_type | P10 | -- |
| model_provider | P02 | 10.0.0 |
| multi_modal_config | P04 | -- |
| prompt_cache | P10 | -- |
| reasoning_trace | P03 | 10.0.0 |
| research_pipeline | P04 | -- |
| session_backend | P10 | 10.0.0 |
| skill | P04 | -- |
| social_publisher | P04 | -- |
| software_project | P02 | -- |
| supabase_data_layer | P04 | -- |
| tagline | P03 | -- |
| toolkit | P04 | 10.0.0 |
| trace_config | P07 | 10.0.0 |
| vector_store | P01 | 10.0.0 |
| workflow_primitive | P12 | 10.0.0 |

**Recommendation:** Add all 21 missing kinds to OBJECT_TO_KINDS in cex_8f_motor.py. Consider adding a `trigger_phrases` field to kinds_meta.json for future intent resolution.

## Artifact 5: cex_8f_motor.py

**Role in intent resolution:** The primary intent parser. Receives natural language, produces execution plan. Pipeline: parse_intent() > classify_objects() > fan_out_builders() > compose_plan().

**Strengths:**
- VERB_TABLE covers 7 actions (create, improve, rebuild, analyze, validate, document, integrate) with 12 PT conjugations
- OBJECT_TO_KINDS has ~160 keyword > kind mappings including PT aliases
- Multi-object detection via trigram/bigram/unigram priority
- TF-IDF fallback via cex_query.py when direct lookup fails
- Effort-aware dispatch (low/medium/high/max)
- Permission scope enforcement per builder

**Gaps found:**

| Gap | Severity | Impact |
|-----|----------|--------|
| 21 kinds missing from OBJECT_TO_KINDS | High | 17% of taxonomy unreachable |
| 2 stale kind references | High | `law` should be `invariant`, `director` should be `supervisor` |
| VERB_TABLE has no EN verbs | Medium | "create", "test", "deploy" not recognized |
| Missing PT verbs: testar, implantar, configurar, otimizar, auditar, agendar, monitorar | Medium | Common user actions not parsed |
| Domain extraction misses compound domains | Low | "agente de vendas para e-commerce" loses structure |
| No synonym expansion for keywords | Low | "database" maps but "banco de dados" does not |

**Stale references (bugs):**

| Motor keyword | Maps to | Should map to | Fix |
|---------------|---------|---------------|-----|
| `law` | `("law", "P08", "CONSTRAIN")` | `("invariant", "P08", "CONSTRAIN")` | Rename kind to `invariant` |
| `regra` | `("law", "P08", "CONSTRAIN")` | `("invariant", "P08", "CONSTRAIN")` | Same fix |
| `director` | `("director", "P08", "COLLABORATE")` | `("supervisor", "P08", "COLLABORATE")` | Rename kind to `supervisor` |

**Recommendation:** Fix stale references immediately. Add 21 missing kinds. Expand VERB_TABLE with EN verbs and missing PT verbs. Add compound PT keywords ("banco de dados", "chave de api", etc.).

## Artifact 6: cex_query.py

**Role in intent resolution:** TF-IDF fallback when OBJECT_TO_KINDS has no match. Searches bld_manifest keywords in index.db.

**Strengths:**
- Bilingual tokenization (PT/EN stop words)
- Simple stemmer handles both languages
- Weighted scoring: keyword 0.6, substring 0.3, domain 0.3, kind 0.1
- Suggest-crew feature for collaboration discovery
- Intent fallback flag (`--intent`) that queries OBJECT_TO_KINDS as secondary

**Gaps found:**

| Gap | Severity | Impact |
|-----|----------|--------|
| Only searches bld_manifest rows | Medium | kinds_meta descriptions/boundaries not indexed |
| Depends on index.db existence | Medium | Fails silently without index |
| No synonym expansion | Low | "pricing" won't match "monetizacao" |
| Score normalization penalizes long queries | Low | 5-word queries get lower scores than 2-word |
| No integration with metaphor dictionary | Low | Metaphors not expanded to industry terms |

**Recommendation:** Index kinds_meta.json descriptions alongside bld_manifest keywords for broader coverage. Consider adding metaphor-to-term expansion as a pre-processing step.

## Cross-Artifact Gap Analysis

| Gap Category | Affected Artifacts | Priority |
|--------------|-------------------|----------|
| 21 unreachable kinds | motor, kinds_meta | P0 -- blocks intent resolution |
| 2 stale kind names | motor | P0 -- produces wrong builder |
| No EN verb parsing | motor | P1 -- EN users get no verb match |
| 7 missing PT verbs | motor | P1 -- common actions ignored |
| 8 examples in intent resolution rule | intent resolution | P2 -- insufficient guidance |
| No kind-level metaphor mapping | dictionary, authority | P2 -- concept translation only |
| TF-IDF only on bld_manifest | query | P3 -- fallback misses kinds |

## Deliverables from This Audit

1. **Intent Resolution Map** (kc_intent_resolution_map.md) -- maps all 123 kinds to natural language phrases
2. **Enhanced Intent Resolution Rule** -- expanded with missing mappings and PT triggers
3. **Intent Resolution Quality Gate** -- 20 test cases (10 EN, 10 PT)
