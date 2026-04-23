---
kind: output_template
id: bld_output_template_context_doc
pillar: P05
llm_function: PRODUCE
purpose: Structural template for context_doc artifacts — derives from SCHEMA.md
quality: 9.0
title: "Output Template Context Doc"
version: "1.0.0"
author: n03_builder
tags: [context_doc, builder, examples]
tldr: "Golden and anti-examples for context doc construction, demonstrating ideal structure and common pitfalls."
domain: "context doc construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_knowledge_card_context_doc
  - bld_schema_context_doc
  - bld_instruction_context_doc
  - p03_sp_context_doc_builder
  - bld_examples_context_doc
  - bld_config_context_doc
  - context-doc-builder
  - bld_collaboration_context_doc
  - p11_qg_context_doc
  - p01_kc_context_doc
---

# Output Template: context_doc
## Frontmatter (copy and fill all fields)
```yaml
id: p01_ctx_{{topic_slug}}
kind: context_doc
pillar: P01
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
domain: "{{domain_value}}"
scope: "{{scope_description_one_sentence}}"
quality: null
tags: [context-doc, {{domain_tag}}, {{scope_tag}}]
tldr: "{{dense_summary_max_160ch}}"
keywords: [{{kw1}}, {{kw2}}, {{kw3}}]
density_score: {{0.80_to_1.00}}
```
## Field Fill Guide
| Field | Format | Example |
|-------|--------|---------|
| id | `p01_ctx_` + snake_case topic | `p01_ctx_br_import_regs` |
| domain | snake_case domain label | `ecommerce_imports` |
| scope | one sentence, specific | `Brazilian import regs 2025-2026 for marketplace sellers` |
| tldr | <= 160 chars, dense | `BR import rules: ICMS 17%, NCM codes required, Receita Federal enforcement 2025` |
| keywords | 3-7 relevant terms | `[icms, ncm, receita_federal, import, brazil]` |
| density_score | float 0.80-1.00 | `0.85` |
## Body Structure
```markdown
## Scope
[Restate scope boundary. List what is in scope and what is explicitly out of scope.
Minimum 3 lines. No filler.]
## Background
[Domain background: history, current state, key facts. No filler prose.
Dense, informative. This is the context agents will INJECT before acting.]
## Stakeholders
[Who uses this context? Agents, roles, teams. What decisions does this inform?]
## Constraints & Assumptions
[Hard constraints: what cannot change.
Working assumptions: what is taken as given.
Format as bullet list.]
## Dependencies
[Other artifacts, systems, APIs, or knowledge this context references.
Format: artifact_id or URL + one-line description.]
## References
[Source links, related context_docs, version history notes.]
```
## Notes
- Body (all sections combined) MUST be <= 2048 bytes
- id MUST equal filename stem (e.g., id: p01_ctx_foo -> file: p01_ctx_foo.md)
- Produce companion .yaml with same frontmatter fields

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_context_doc]] | upstream | 0.38 |
| [[bld_schema_context_doc]] | downstream | 0.37 |
| [[bld_instruction_context_doc]] | upstream | 0.34 |
| [[p03_sp_context_doc_builder]] | upstream | 0.34 |
| [[bld_examples_context_doc]] | downstream | 0.33 |
| [[bld_config_context_doc]] | downstream | 0.31 |
| [[context-doc-builder]] | upstream | 0.27 |
| [[bld_collaboration_context_doc]] | downstream | 0.27 |
| [[p11_qg_context_doc]] | downstream | 0.26 |
| [[p01_kc_context_doc]] | upstream | 0.24 |
