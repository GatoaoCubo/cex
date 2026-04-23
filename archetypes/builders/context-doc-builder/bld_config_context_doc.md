---
kind: config
id: bld_config_context_doc
pillar: P09
llm_function: CONSTRAIN
purpose: Runtime configuration constraints for context_doc production
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Context Doc"
version: "1.0.0"
author: n03_builder
tags: [context_doc, builder, examples]
tldr: "Golden and anti-examples for context doc construction, demonstrating ideal structure and common pitfalls."
domain: "context doc construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_context_doc
  - bld_output_template_context_doc
  - bld_schema_context_doc
  - p11_qg_context_doc
  - bld_instruction_context_doc
  - bld_config_rag_source
  - bld_config_few_shot_example
  - p03_sp_context_doc_builder
  - bld_config_component_map
  - bld_config_knowledge_card
---
# Config: context_doc
## Naming Rules
| Rule | Pattern | Example |
|------|---------|---------|
| Markdown file | `p01_ctx_{topic_slug}.md` | `p01_ctx_br_import_regs.md` |
| YAML companion | `p01_ctx_{topic_slug}.yaml` | `p01_ctx_br_import_regs.yaml` |
| id field | `p01_ctx_{topic_slug}` | `p01_ctx_br_import_regs` |
| topic_slug | `[a-z][a-z0-9_]+` (snake_case, no hyphens) | `br_import_regs` |
**Critical**: id MUST equal filename stem. Brain search depends on this invariant.
## File Paths
| Artifact | Canonical Path |
|----------|---------------|
| Produced context_docs | `cex/P01_knowledge/examples/` |
| Schema reference | `cex/P01_knowledge/_schema.yaml` |
| Seed bank | `cex/P01_knowledge/SEED_BANK.yaml` |
| Builder files | `cex/archetypes/builders/context-doc-builder/` |
## Size Constraints
| Constraint | Value | Scope |
|------------|-------|-------|
| max_bytes | 2048 | Body only (all sections after frontmatter) |
| tldr max | 160 chars | frontmatter.tldr field |
| tags min | 3 items | frontmatter.tags list |
| keywords min | 3 items | frontmatter.keywords list |
| scope min | 1 sentence | frontmatter.scope field |
| density_score min | 0.80 | if provided (recommended) |
## Trim Priority (if body exceeds 2048 bytes)
1. Trim `## References` section first (least dense)
2. Trim `## Background` narrative prose (keep facts, remove transitions)
3. Trim `## Stakeholders` to bullet list only
4. Never trim `## Scope` or `## Constraints & Assumptions`
## Invariants (never override)
- `quality: null` — never self-assign score
- `kind: context_doc` — literal, no variation
- `pillar: P01` — pillar assignment fixed
- id == filename stem — enforced by gate H03

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_context_doc]] | upstream | 0.33 |
| [[bld_output_template_context_doc]] | upstream | 0.32 |
| [[bld_schema_context_doc]] | upstream | 0.32 |
| [[p11_qg_context_doc]] | downstream | 0.24 |
| [[bld_instruction_context_doc]] | upstream | 0.24 |
| [[bld_config_rag_source]] | sibling | 0.23 |
| [[bld_config_few_shot_example]] | sibling | 0.23 |
| [[p03_sp_context_doc_builder]] | upstream | 0.23 |
| [[bld_config_component_map]] | sibling | 0.22 |
| [[bld_config_knowledge_card]] | sibling | 0.20 |
