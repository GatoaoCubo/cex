---
kind: schema
id: bld_schema_rag_source
pillar: P06
llm_function: CONSTRAIN
role: source_of_truth
version: 1.0.0
quality: 9.1
title: "Schema Rag Source"
author: n03_builder
tags: [rag_source, builder, examples]
tldr: "Golden and anti-examples for rag source construction, demonstrating ideal structure and common pitfalls."
domain: "rag source construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_ins_rag_source
  - bld_knowledge_card_rag_source
  - bld_schema_model_registry
  - bld_examples_rag_source
  - bld_schema_experiment_tracker
  - bld_schema_benchmark_suite
  - bld_schema_multimodal_prompt
  - bld_schema_app_directory_entry
  - bld_schema_training_method
  - bld_schema_eval_metric
---

# Schema: rag_source
SOURCE OF TRUTH. OUTPUT_TEMPLATE.md derives from this file. If conflict exists, this file wins.
## Required Fields (must be present — H06 HARD gate)
| Field | Type | Constraint | Example |
|-------|------|-----------|---------|
| id | string | ^p01_rs_[a-z][a-z0-9_]+$ | p01_rs_anthropic_claude_docs |
| kind | string | exactly "rag_source" | rag_source |
| pillar | string | exactly "P01" | P01 |
| version | string | semver "X.Y.Z" | "1.0.0" |
| created | string | YYYY-MM-DD | "2026-03-26" |
| updated | string | YYYY-MM-DD | "2026-03-26" |
| author | string | agent id or user handle | builder_agent |
| url | string | valid URL, https:// preferred | "https://docs.anthropic.com" |
| domain | string | CEX domain taxonomy value | llm_providers |
| last_checked | string | YYYY-MM-DD | "2026-03-26" |
| quality | null | MUST be null — never self-score | null |
| tags | list | >= 3 items, includes "rag-source" | [rag-source, llm_providers, html] |
| tldr | string | <= 160 chars, non-empty | "Official Anthropic API reference..." |
## Recommended Fields
| Field | Type | Enum / Constraint |
|-------|------|------------------|
| keywords | list | 3-8 domain keywords |
| reliability | string | high / medium / low |
| format | string | html / json / api / pdf / csv |
| extraction_method | string | crawl / api_call / scrape / download |
## ID Pattern
```
^p01_rs_[a-z][a-z0-9_]+$
```
- Prefix: p01_rs_ (pillar + kind abbreviation)
- Body: lowercase alphanumeric + underscores
- Must equal filename stem exactly (H03)
## File Naming
```
p01_rs_{source_slug}.md    # human-readable artifact
p01_rs_{source_slug}.yaml  # machine-readable twin
```
Both files must exist and have matching id.
## Body Structure (3 mandatory sections)
1. `## Source Description` — what, who, why
2. `## Freshness Policy` — re-check schedule, staleness threshold
3. `## Extraction Notes` — method, format, auth, quirks
## Hard Constraints
| Constraint | Value |
|-----------|-------|
| max_bytes | 1024 (body only) |
| quality | null always |
| kind | rag_source always |
| pillar | P01 always |
| url | must be present and valid format |
| POINTER ONLY | body must NOT contain extracted content |
## Boundary Rule (critical)
rag_source IS: a pointer to external indexable source.
rag_source IS NOT: the content itself, a knowledge_card, a context_doc.
If the body contains paragraphs of extracted text — it is a knowledge_card, not a rag_source.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_rag_source]] | upstream | 0.46 |
| [[bld_knowledge_card_rag_source]] | upstream | 0.45 |
| [[bld_schema_model_registry]] | sibling | 0.43 |
| [[bld_examples_rag_source]] | downstream | 0.40 |
| [[bld_schema_experiment_tracker]] | sibling | 0.39 |
| [[bld_schema_benchmark_suite]] | sibling | 0.38 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.38 |
| [[bld_schema_app_directory_entry]] | sibling | 0.37 |
| [[bld_schema_training_method]] | sibling | 0.37 |
| [[bld_schema_eval_metric]] | sibling | 0.37 |
