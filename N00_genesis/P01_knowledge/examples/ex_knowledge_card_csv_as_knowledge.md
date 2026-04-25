---
id: p01_kc_csv_as_knowledge
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CSV as Knowledge — Structured Data as Searchable Runtime Knowledge Base"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: cex_taxonomy
quality: 9.2
tags: [csv, knowledge-base, bm25, structured-data, runtime-search]
tldr: "CSVs as searchable knowledge base via BM25 — no database, no embeddings, no server, ~50ms per query"
when_to_use: "When you need contextual recommendations based on structured data without external infrastructure"
keywords: [csv-knowledge, structured-search, data-driven-decisions, bm25-csv]
long_tails:
  - "How to use CSVs as knowledge base for LLM agents"
  - "When to use CSV with BM25 instead of a database"
axioms:
  - "ALWAYS one CSV per domain — never a giant multi-purpose CSV"
  - "NEVER hardcode recommendations in code — use CSV as source"
linked_artifacts:
  primary: null
  related: [p01_kc_bm25_search, p01_kc_agentskills_spec]
density_score: null
data_source: "https://github.com/kepano/obsidian-skills"
related:
  - p01_kc_bm25_search
  - p06_schema_export_format
  - p01_kc_multi_stack
  - bld_collaboration_agentic_rag
  - bld_collaboration_eval_metric
  - p01_kc_slide_generation
  - p02_agent_data_validator
  - p01_kc_brand_skill
  - p01_kc_brand_tokens_pipeline
  - bld_collaboration_ecommerce_vertical
---

## TL;DR

CSVs work as queryable knowledge bases at runtime via BM25. No database, no embeddings, no server. Each CSV is a specialized domain (products, styles, colors, typography) with search in ~50ms. Proven pattern with 55+ CSVs in production covering design, UX and recommendations.

## Core Concept

The premise is that structured data with well-defined keywords does not need embeddings for effective retrieval. A CSV with separate search columns (search_cols) and output columns (output_cols) creates a queryable decision table: each row is a rule encoded as data, not code.

The pattern works because CSVs are: human-editable (Excel, Google Sheets), versionable (readable git diff), portable (no runtime dependency) and composable (multiple CSVs queried in parallel). BM25 search on search_cols returns the most relevant rows, and the system extracts only the needed output_cols.

Domain separation is critical: one CSV per knowledge type (products, styles, guidelines) ensures BM25 operates in a focused lexical space. Large multi-purpose CSVs degrade precision because terms common to multiple domains dilute ranking.

## Architecture/Patterns

| Component | File | Content |
|-----------|------|---------|
| Catalog | products.csv | 161 product types + recommendations |
| Styles | styles.csv | 67 UI styles + CSS keywords |
| Colors | colors.csv | 161 palettes per product type |
| Typography | typography.csv | 57 font pairings + Google Fonts |
| Landing | landing.csv | 24 patterns + CTA strategies |
| UX Rules | ux-guidelines.csv | 99 rules + anti-patterns |

Standard schema for each CSV:
```
search_cols: columns indexed by BM25 (keywords, desc)
output_cols: columns returned in results (complete)
Row 1: header with column names
```

Multi-domain search (5 parallel CSVs):
```
Request -> detect domain (regex)
  -> products.csv  (category?)
  -> styles.csv    (UI style?)
  -> colors.csv    (palette?)
  -> landing.csv   (pattern?)
  -> typography.csv (fonts?)
-> merge results -> unified output
```

Replicable structure for any domain:
```
domain/
  data/entities.csv    # entity catalog
  data/rules.csv       # recommendation rules
  data/guidelines.csv  # anti-patterns + best practices
  scripts/core.py      # BM25 engine (reusable)
```

## Practical Examples

| Request | CSV queried | Result |
|---------|------------|--------|
| Landing page for spa | products.csv | Style, palette, pattern |
| Font for e-commerce | typography.csv | Pairs with Google Fonts URL |
| UX rule for forms | ux-guidelines.csv | ARIA rules + anti-patterns |
| Chart for data | charts.csv | Recommended type + when not to use |

Complete flow:
1. User request arrives at the system
2. Regex detects domain automatically
3. BM25 searches in the domain CSV's search_cols
4. Top 3-5 results extracted with output_cols
5. Result injected as context for LLM generation

CSV as decision table:
```csv
Product Type,Primary Style,Anti-Pattern
Banking,Trust & Authority,"AI purple gradients"
Gaming,3D & Hyperrealism,"Flat design"
Healthcare,Accessible & Ethical,"Low contrast"
```

## Anti-Patterns

- Giant multi-domain CSV (degrades BM25 precision)
- Recommendations hardcoded in code instead of CSV
- Embeddings for simple structured data (overkill)
- Duplicated data across CSVs from different domains
- Search_cols with long texts (BM25 prefers keywords)
- Missing separate output_cols (returns everything)

## Referencias

- source: https://github.com/kepano/obsidian-skills
- source: https://en.wikipedia.org/wiki/Okapi_BM25
- related: p01_kc_bm25_search
- related: p01_kc_agentskills_spec

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_bm25_search]] | sibling | 0.34 |
| [[p06_schema_export_format]] | downstream | 0.28 |
| [[p01_kc_multi_stack]] | sibling | 0.22 |
| [[bld_collaboration_agentic_rag]] | downstream | 0.19 |
| [[bld_collaboration_eval_metric]] | downstream | 0.18 |
| [[p01_kc_slide_generation]] | sibling | 0.17 |
| [[p02_agent_data_validator]] | downstream | 0.17 |
| [[p01_kc_brand_skill]] | sibling | 0.16 |
| [[p01_kc_brand_tokens_pipeline]] | sibling | 0.16 |
| [[bld_collaboration_ecommerce_vertical]] | downstream | 0.16 |
