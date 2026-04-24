---
id: p01_kc_source_triangulation
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Source Triangulation"
version: 2.0.0
created: 2026-03-31
updated: 2026-04-07
author: n01_research
domain: patterns
quality: 9.1
tags: [pattern, skill, llm, triangulation, verification, cross-reference, multi-source]
tldr: "Cross-reference 3+ sources of different origin and type. 3/3 agree = high confidence. 2/3 = use majority + flag. 0/3 = halt and ask user."
when_to_use: "When a claim is critical (published content, architecture decisions) or when a single source has unknown reliability."
keywords: [triangulation, verification, cross-reference, multi-source, fact-check]
density_score: 0.95
related:
  - p11_qg_intelligence
  - p01_kc_confidence_scoring
  - p10_out_source_dossier
  - p03_ins_rag_source
  - bld_memory_rag_source
  - p01_kc_intelligence_best_practices
  - p06_schema_source_quality
  - bld_knowledge_card_citation
  - p01_kc_market_research_data_triangulation
  - n01_rs_intelligence_sources
---

# Source Triangulation

## Quick Reference

| Aspect | Detail |
|--------|--------|
| Core idea | Verify claims across 3+ independent sources of different types |
| Trigger | Critical claims, unknown source reliability, conflicting data |
| Benefit | Reduces hallucination risk from ~15% to <3% |
| Risk if skipped | Propagating single-source errors into published artifacts |

## Rule of Three

Find claim in **Source A** (primary), verify in **Source B** (different origin), confirm in **Source C** (different type).

| Source Diversity | Example | Strength |
|-----------------|---------|----------|
| Same author, same format | Two blog posts by same person | Weak (echo chamber) |
| Different author, same format | Two independent articles | Medium |
| Different author, different format | Article + API docs + code | **Strong** |
| Different author, different domain | Academic paper + industry report + code | **Strongest** |

## Confidence Matrix

| Agreement | Confidence | Action |
|-----------|-----------|--------|
| 3/3 sources agree | High (0.95+) | Use directly, cite all three |
| 2/3 agree | Medium (0.75) | Use majority, flag disagreement |
| 1/3 agree | Low (0.40) | Investigate further, do not publish |
| 0/3 agree | None | Halt — escalate to user |

## Verification Protocol

| Step | Action | Output |
|------|--------|--------|
| 1. Identify claim | Extract atomic assertion | Claim statement |
| 2. Source A (primary) | Find in original/official source | Evidence A |
| 3. Source B (lateral) | Find in independent source, different origin | Evidence B |
| 4. Source C (orthogonal) | Find in different format (code, data, API) | Evidence C |
| 5. Compare | Align evidence, note agreements and conflicts | Confidence score |
| 6. Decide | Apply confidence matrix above | Use / flag / halt |

## Source Type Taxonomy

| Type | Examples | Reliability Tier |
|------|----------|-----------------|
| Official docs | API reference, SDK docs, spec | Tier 1 |
| Codebase | Source code, tests, configs | Tier 1 |
| Academic/peer-reviewed | Papers, standards (RFC, W3C) | Tier 1 |
| Industry report | Gartner, analyst reports | Tier 2 |
| Blog/tutorial | Developer blogs, Medium posts | Tier 3 |
| Forum/social | Stack Overflow, Reddit, Twitter | Tier 4 |
| LLM-generated | ChatGPT, Claude (uncited) | Tier 5 (verify always) |

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|-------------|--------------|
| Echo chamber | 3 sources that all cite the same original = 1 source |
| Recency bias | Only checking newest sources, ignoring authoritative older ones |
| Confirmation bias | Stopping search once 1 source confirms your assumption |
| Format homogeneity | 3 blog posts ≠ triangulation (same type, different authors) |
| Skipping for speed | "I'm pretty sure" → publish → wrong |

## Linked Artifacts

- `p01_kc_confidence_scoring` — threshold actions after triangulation
- `p01_kc_query_decomposition` — split complex claims into atomic sub-queries
- `p01_kc_web_scraping_ethics` — ethical sourcing constraints

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_intelligence]] | downstream | 0.27 |
| [[p01_kc_confidence_scoring]] | sibling | 0.27 |
| [[p10_out_source_dossier]] | downstream | 0.22 |
| [[p03_ins_rag_source]] | related | 0.21 |
| [[bld_memory_rag_source]] | downstream | 0.21 |
| [[p01_kc_intelligence_best_practices]] | sibling | 0.20 |
| [[p06_schema_source_quality]] | downstream | 0.19 |
| [[bld_knowledge_card_citation]] | sibling | 0.19 |
| [[p01_kc_market_research_data_triangulation]] | sibling | 0.19 |
| [[n01_rs_intelligence_sources]] | related | 0.19 |
