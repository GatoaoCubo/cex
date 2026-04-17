---
kind: instruction
id: bld_instruction_search_tool
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for search_tool
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.1
title: "Instruction Search Tool"
version: "1.0.0"
author: n03_builder
tags: [search_tool, builder, examples]
tldr: "Golden and anti-examples for search tool construction, demonstrating ideal structure and common pitfalls."
domain: "search tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Instructions: How to Produce a search_tool
## Phase 1: RESEARCH
1. Identify the search use case (general web, news, academic, semantic similarity, etc.)
2. Select provider based on use case (Tavily for AI, Serper for Google SERP, Exa for neural)
3. Determine search type: web, semantic, hybrid, news, images
4. Define max results per query (typical: 5-20)
5. Identify result fields available from provider (title, url, snippet, content, score)
6. Determine filtering needs: date range, domain filter, language, region
7. Check for existing search_tool artifacts to avoid duplicates
8. Confirm provider slug for id: snake_case, lowercase, no hyphens
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Write Overview section: what this search does and primary use case
5. Write Query section: parameters, syntax, filtering options
6. Write Results section: result structure with fields and types
7. Write Provider section: API details, rate limits, cost per query
8. Verify body <= 2048 bytes
9. Verify id matches `^p04_search_[a-z][a-z0-9_]+$`
10. Verify NO API keys in artifact — env vars only
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p04_search_`
4. Confirm kind == search_tool
5. Confirm provider is specified
6. Confirm max_results >= 1
7. Confirm result_fields documented
8. HARD gates: frontmatter valid, id pattern, provider defined, max_results set
9. SOFT gates: score against QUALITY_GATES.md
10. Cross-check: is this external search (not local vector store)? Not file ingestion? Not navigation?

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify search
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | search tool construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
