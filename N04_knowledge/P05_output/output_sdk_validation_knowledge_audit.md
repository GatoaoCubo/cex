---
id: output_sdk_validation_knowledge_audit
name: SDK Validation — Knowledge Audit
kind: output
pillar: P01
nucleus: N04
mission: SDK_VALIDATION
created: 2026-04-06
quality: 9.1
density_score: 1.0
title: "Output Sdk Validation Knowledge Audit"
version: 1.0.0
author: N04
tags: [output, knowledge, output]
tldr: "**Verdict**: PASS. Full coverage. 2 extra KCs exist for specialized domains not in kinds_meta."
domain: knowledge
updated: 2026-04-07
related:
  - n01_sdk_validation_self_audit
  - p07_gt_stripe_pipeline
  - p01_kc_iterative_refinement_skill
  - self_audit_newpc
  - hybrid_review7_n05
  - output_sdk_validation_audit
  - p01_kc_refinement
  - bld_examples_invariant
  - self_audit_newpc_2026_04_12
  - n01_hybrid_review_wave1
---

# N04 SDK Validation — Knowledge Audit Report

## T1. KC Coverage

| Metric | Value |
|--------|-------|
| Kinds in registry | 115 |
| KC files | 117 |
| Kinds WITHOUT KC | 0 |
| KCs WITHOUT kind | 2 (`software_project`, `supabase_data_layer`) |

**Verdict**: PASS. Full coverage. 2 extra KCs exist for specialized domains not in kinds_meta.

## T2. Retriever Stats

| Metric | Value |
|--------|-------|
| Documents indexed | 2,450 |
| Vocabulary size | 14,698 |
| Index built | 2026-04-02 |
| Top kind | knowledge_card (504 docs) |

**Verdict**: PASS. Index is 4 days old, covers 2,450 docs with 14.7K vocab.

## T3. Compile All

| Metric | Value |
|--------|-------|
| Compiled | 367/367 |
| Errors | 0 |
| Rate | 100% |

**Verdict**: PASS. Zero compile failures.

## T4. Reverse Compiler

| Target | Status | Output |
|--------|--------|--------|
| claude-md | OK | 86 artifacts -> CLAUDE_GENERATED.md (12,741 bytes) |
| cursorrules | OK | 28 artifacts -> .cursorrules |

**Verdict**: PASS. Both targets produce valid output, no crashes.

## T5. Memory Types + Age

| Component | Status |
|-----------|--------|
| MemoryType enum | 4 types: `user`, `feedback`, `project`, `reference` |
| Freshness caveat (30d) | Returns `[STALE]` label with verification warning |

**Verdict**: PASS. 4-type taxonomy + age decay functional.

## T6. Knowledge Library Audit

### Artifact Count by Directory

| Directory | Count |
|-----------|-------|
| P01_knowledge/examples | 191 |
| P01_knowledge/templates | 9 |
| P01_knowledge/library/kind | 117 |
| P01_knowledge/library/platform | 40 |
| P01_knowledge/library/frontend | 10 |
| P01_knowledge/library/infrastructure | 10 |
| P01_knowledge/library/sources | 3 |
| P01_knowledge/library/specs | 1 |
| **TOTAL** | **381** |

### Quality Distribution

| Metric | Value |
|--------|-------|
| Total scanned | 458 |
| quality: null | 2 |
| quality >= 8.0 | 456 |
| quality < 8.0 | 0 |

### Top 5 by Quality

| Score | Artifact |
|-------|----------|
| 9.5 | ex_knowledge_card_format_benchmark_cex_types |
| 9.2 | kc_artifact_quality_evaluation_methods |
| 9.2 | kc_ab_testing_content_optimization |
| 9.2 | kc_brand_best_practices |
| 9.2 | kc_competitive_intelligence_osint |

### Bottom 5 by Quality

| Score | Artifact |
|-------|----------|
| 8.3 | kc_prompt_evolution |
| 8.3 | kc_query_decomposition |
| 8.3 | kc_self_healing_skill |
| 8.3 | kc_source_triangulation |
| 8.0 | kc_rag_chunking_strategies |

**Verdict**: PASS. Zero artifacts below 8.0. Floor is 8.0, ceiling is 9.5.

## T7. Model Upgrade Verification

| Field | Expected | Actual |
|-------|----------|--------|
| cli | claude | claude |
| model | claude-opus-4-6 | claude-opus-4-6 |
| context | 1000000 | 1000000 |

**Verdict**: PASS. N04 upgraded to Opus 1M.

## Summary

| Task | Status |
|------|--------|
| T1 KC Coverage | PASS |
| T2 Retriever Stats | PASS |
| T3 Compile All | PASS |
| T4 Reverse Compiler | PASS |
| T5 Memory Types/Age | PASS |
| T6 Library Audit | PASS |
| T7 Model Upgrade | PASS |

**Overall: 7/7 PASS. Knowledge layer fully validated.**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n01_sdk_validation_self_audit]] | sibling | 0.39 |
| [[p07_gt_stripe_pipeline]] | downstream | 0.29 |
| [[p01_kc_iterative_refinement_skill]] | related | 0.29 |
| [[self_audit_newpc]] | related | 0.29 |
| [[hybrid_review7_n05]] | related | 0.27 |
| [[output_sdk_validation_audit]] | sibling | 0.27 |
| [[p01_kc_refinement]] | related | 0.26 |
| [[bld_examples_invariant]] | downstream | 0.25 |
| [[self_audit_newpc_2026_04_12]] | related | 0.25 |
| [[n01_hybrid_review_wave1]] | related | 0.25 |
