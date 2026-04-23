---
kind: config
id: bld_config_knowledge_card
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: fork
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Knowledge Card"
version: "1.0.0"
author: n03_builder
tags: [knowledge_card, builder, examples]
tldr: "Golden and anti-examples for knowledge card construction, demonstrating ideal structure and common pitfalls."
domain: "knowledge card construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_output_validator
  - p01_kc_knowledge_best_practices
  - p03_sp_knowledge_card_builder
  - output-validator-builder
  - bld_collaboration_output_validator
  - bld_schema_knowledge_card
  - bld_instruction_knowledge_card
  - bld_knowledge_card_knowledge_card
  - bld_config_retriever_config
  - bld_tools_validator
---
# Config: knowledge_card Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p01_kc_{topic_slug}.md` | `p01_kc_prompt_caching.md` |
| Builder directory | kebab-case | `knowledge-card-builder/` |
| Frontmatter fields | snake_case | `density_score`, `when_to_use` |
| Topic slug | lowercase, underscores | `rag_fundamentals`, `prompt_caching` |
Rule: id MUST equal filename stem (validator H02 checks this).
## File Paths
- Output: `cex/P01_knowledge/examples/p01_kc_{topic}.md`
- Compiled: `cex/P01_knowledge/compiled/p01_kc_{topic}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: 200-5120 bytes (validator H08)
- Total (frontmatter + body): max ~6500 bytes
- Density: >= 0.80
- Bullet max: 80 chars (validator S10)
- Title: 5-100 chars (validator S03)
- tldr: <= 160 chars, no self-references (S01, S02)
## Body Requirements
- >= 4 sections (validator S06)
- Each section >= 3 non-empty lines (validator S08)
- Largest section >= 30% of body (validator S07)
- >= 1 table (S11), >= 1 code block (S12), >= 1 URL (S13)
## KC Type Selection
| Content | Type | Body Structure |
|---------|------|---------------|
| External tech (APIs, patterns) | domain_kc | Quick Ref + Concepts + Phases + Rules + Flow + Compare + Refs |
| CEX-internal (architecture) | meta_kc | Summary + Spec + Patterns + Anti + Application + Refs |
Default: domain_kc. Use meta_kc only for CEX system documentation.
## Freshness
- updated field should reflect last meaningful edit
- Knowledge degrades slower than model_cards (no 90-day hard gate)
- Stale KCs identified by brain_query freshness ranking

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_output_validator]] | sibling | 0.39 |
| [[p01_kc_knowledge_best_practices]] | upstream | 0.33 |
| [[p03_sp_knowledge_card_builder]] | upstream | 0.31 |
| [[output-validator-builder]] | upstream | 0.31 |
| [[bld_collaboration_output_validator]] | downstream | 0.31 |
| [[bld_schema_knowledge_card]] | upstream | 0.29 |
| [[bld_instruction_knowledge_card]] | upstream | 0.28 |
| [[bld_knowledge_card_knowledge_card]] | upstream | 0.28 |
| [[bld_config_retriever_config]] | sibling | 0.27 |
| [[bld_tools_validator]] | upstream | 0.26 |
