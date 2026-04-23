---
kind: schema
id: bld_schema_context_doc
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for context_doc
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.0
title: "Schema Context Doc"
version: "1.0.0"
author: n03_builder
tags: [context_doc, builder, examples]
tldr: "Golden and anti-examples for context doc construction, demonstrating ideal structure and common pitfalls."
domain: "context doc construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_action_prompt
  - bld_schema_usage_report
  - bld_schema_golden_test
  - bld_schema_retriever_config
  - bld_schema_search_strategy
  - bld_schema_input_schema
  - bld_schema_memory_scope
  - bld_schema_reranker_config
  - bld_schema_smoke_eval
  - bld_schema_integration_guide
---

# Schema: context_doc
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p01_ctx_{topic}) | YES | - | Namespace compliance |
| kind | literal "context_doc" | YES | - | Type integrity |
| pillar | literal "P01" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| domain | string (snake_case) | YES | - | Machine-readable domain label |
| scope | string (one sentence) | YES | - | Scope boundary statement |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "context-doc" |
| tldr | string <= 160ch | YES | - | Dense summary |
| keywords | list[string], len >= 3 | REC | - | Domain search terms |
| density_score | float 0.80-1.00 | REC | - | Content density |
## ID Pattern
Regex: `^p01_ctx_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
Examples: `p01_ctx_br_import_regs`, `p01_ctx_api_auth_jwt`, `p01_ctx_marketplace_fees`
## Body Structure (required sections)
1. `## Scope` — in-scope and out-of-scope boundary, minimum 3 lines
2. `## Background` — domain history, current state, key facts
3. `## Stakeholders` — who consumes this context, what decisions it informs
4. `## Constraints & Assumptions` — hard constraints + working assumptions
5. `## Dependencies` — referenced artifacts, systems, external sources
6. `## References` — source links, related artifacts (optional but recommended)
## Constraints
- max_bytes: 2048 (body only, all sections combined)
- naming: p01_ctx_{topic}.md + p01_ctx_{topic}.yaml
- machine_format: yaml
- id == filename stem (enforced by H03)
- quality: null always (enforced by H05)
- llm_function: INJECT (context_doc is injected into prompts)
- layer: content (P01 knowledge layer)
## Boundary Rules
- context_doc is NOT knowledge_card: no single-atomic-fact constraint, no mandatory density gate
- context_doc is NOT glossary_entry: does not define a single term
- context_doc is NOT instruction: no step-by-step execution protocol
- context_doc DOES allow narrative prose (unlike knowledge_card)
- context_doc DOES allow multiple facts (unlike glossary_entry)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_action_prompt]] | sibling | 0.56 |
| [[bld_schema_usage_report]] | sibling | 0.55 |
| [[bld_schema_golden_test]] | sibling | 0.55 |
| [[bld_schema_retriever_config]] | sibling | 0.55 |
| [[bld_schema_search_strategy]] | sibling | 0.55 |
| [[bld_schema_input_schema]] | sibling | 0.55 |
| [[bld_schema_memory_scope]] | sibling | 0.55 |
| [[bld_schema_reranker_config]] | sibling | 0.54 |
| [[bld_schema_smoke_eval]] | sibling | 0.54 |
| [[bld_schema_integration_guide]] | sibling | 0.54 |
