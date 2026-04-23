---
kind: knowledge_card
id: bld_knowledge_card_knowledge_card
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for knowledge_card production — atomic searchable facts
sources: validate_kc.py v2.0, _schema.yaml v4.0, 721 real knowledge cards
quality: 9.1
title: "Knowledge Card Knowledge Card"
version: "1.0.0"
author: n03_builder
tags: [knowledge_card, builder, examples]
tldr: "Golden and anti-examples for knowledge card construction, demonstrating ideal structure and common pitfalls."
domain: "knowledge card construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p01_kc_knowledge_best_practices
  - bld_instruction_knowledge_card
  - p01_kc_creation_best_practices
  - p03_sp_knowledge_card_builder
  - knowledge-card-builder
  - bld_collaboration_knowledge_card
  - p01_kc_knowledge_card
  - p01_kc_artifact_quality_evaluation_methods
  - knowledge-index-builder
  - bld_knowledge_card_retriever_config
---

# Domain Knowledge: knowledge_card
## Executive Summary
Knowledge cards are atomic searchable facts — the smallest retrieval unit in a knowledge system. Each card answers ONE question about ONE topic with density >= 0.80 (>80% concrete data, no filler). Cards are retrieved via hybrid search (BM25 + vector) using frontmatter fields. They differ from model cards (LLM specs), learning records (internal experience), and context docs (domain background).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P01 (knowledge) |
| Frontmatter fields | 14 required + 5 extended |
| Quality gates | 10 HARD + 20 SOFT |
| Max body | 5120 bytes |
| Min body | 200 bytes |
| Density minimum | >= 0.80 |
| Size sweet spot | 50-80 lines (single concept), 80-120 (multi-pattern) |
| Scoring dimensions | D1 Frontmatter, D2 Density, D3 Axioms, D4 Structure, D5 Format |
## Patterns
- **Retrieval surface**: frontmatter fields drive search discovery
| Field | Retrieval role | Pattern |
|-------|---------------|---------|
| tldr | Primary match (BM25 + embedding) | Specific: "Execute CLI via subprocess, retry 3x" |
| tags | Faceted filtering, clustering | 3-7 tags, mix domain + technique |
| keywords | BM25 exact match boost | 2-5 terms user would literally type |
| long_tails | Semantic/vector search | Full phrases: "how to handle concurrent token refresh" |
| when_to_use | Agent activation trigger | Specific context, not "when needed" |
- **Density hierarchy** (most to least info/token): tables > code blocks > bullets > ASCII diagrams > paragraphs
- **Two body structures**: domain_kc (external knowledge: Quick Ref, Key Concepts, Strategy, Golden Rules, Flow, References) and meta_kc (system-internal: Exec Summary, Spec Table, Patterns, Anti-Patterns, Application, References)
- **Density gate**: density = data_lines / total_non_empty_lines; < 0.80 = card fails regardless of other quality
- **Axiom form**: ALWAYS/NEVER/IF-THEN with condition + action + consequence
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Vague tldr ("How to use CLI") | No search signal; returns wrong in BM25 |
| Prose body | Low density; convert to tables, bullets, code |
| Template residue (`{{placeholder}}`) | Unfilled fields; looks incomplete |
| Frontmatter echo in body | Body repeats title/tldr; adds zero depth |
| Giant monolith (300+ lines) | Split into 2+ focused atomic cards |
| density < 0.80 | Card fails regardless of other quality scores |
## Application
1. Define ONE topic: what single question does this card answer?
2. Write frontmatter: all 14 required fields with specific, search-optimized values
3. Select body structure: domain_kc (external) or meta_kc (internal)
4. Write dense body: tables first, bullets second, paragraphs only when necessary
5. Check density: data_lines / total >= 0.80
6. Validate: <= 5120 bytes, >= 200 bytes, axioms in ALWAYS/NEVER/IF-THEN form
## References
- validate_kc.py v2.0: 10 HARD + 20 SOFT gate validator
- _schema.yaml v4.0: canonical field definitions for knowledge_card
- 721 real knowledge cards: empirical patterns (p95 body = 4274 bytes)
- Information retrieval: BM25 + vector hybrid search for dense retrieval

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_knowledge_best_practices]] | sibling | 0.44 |
| [[bld_instruction_knowledge_card]] | downstream | 0.41 |
| [[p01_kc_creation_best_practices]] | sibling | 0.39 |
| [[p03_sp_knowledge_card_builder]] | downstream | 0.38 |
| [[knowledge-card-builder]] | downstream | 0.30 |
| [[bld_collaboration_knowledge_card]] | downstream | 0.28 |
| [[p01_kc_knowledge_card]] | sibling | 0.26 |
| [[p01_kc_artifact_quality_evaluation_methods]] | sibling | 0.26 |
| [[knowledge-index-builder]] | downstream | 0.26 |
| [[bld_knowledge_card_retriever_config]] | sibling | 0.26 |
