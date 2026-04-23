---
kind: knowledge_card
id: bld_knowledge_card_response_format
pillar: P05
llm_function: INJECT
purpose: Domain knowledge for response_format production — atomic searchable facts
sources: response-format-builder MANIFEST.md + SCHEMA.md
quality: 9.1
title: "Knowledge Card Response Format"
version: "1.0.0"
author: n03_builder
tags: [response_format, builder, examples]
tldr: "Golden and anti-examples for response format construction, demonstrating ideal structure and common pitfalls."
domain: "response format construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_response_format
  - p03_ins_response_format
  - bld_architecture_response_format
  - response-format-builder
  - p03_sp_response_format_builder
  - bld_collaboration_response_format
  - bld_examples_response_format
  - bld_knowledge_card_prompt_template
  - p11_qg_response_format
  - bld_memory_response_format
---

# Domain Knowledge: response_format
## Executive Summary
A response_format is a template injected into the LLM prompt that specifies how the model must structure its output during generation — it is a pre-generation contract the LLM sees. Post-generation validation belongs to validation_schema (P06). Data extraction belongs to parser (P05). Format transformation belongs to formatter (P05). The response_format is guidance, not enforcement; clarity and a concrete example output are what drive compliance.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P05 (IO) |
| ID pattern | `^p05_rf_[a-z][a-z0-9_]+$` |
| Required frontmatter fields | 12 (includes `format_type` and `domain`) |
| Recommended fields | 4 (target_kind, example_output, variable_syntax, sections) |
| Max body | 4096 bytes |
| Body sections | 4 (Format Specification, Variables Table, Template Body, Example Output) |
| Section count constraint | 4–7 sections; consolidate if > 7 |
| Naming | `p05_rf_{format_slug}.yaml` |
## Patterns
| Pattern | Rule |
|---------|------|
| Format compliance hierarchy | JSON (95%) > YAML (90%) > Markdown tables (88%) > Numbered lists (85%) > Prose (70%) |
| Consumer-driven format_type | Machine consumer = `json`; config = `yaml`; human = `markdown` |
| Variable syntax tier 1 | `{{VARIABLE_NAME}}` — mustache, required; must have type + example in variables table |
| Variable syntax tier 2 | `[VARIABLE_NAME]` — bracket, optional; clearly marked as optional |
| Variables table completeness | Every variable requires: name, type, constraints, required/optional, example |
| Example Output section | Must be fully filled — no placeholders remaining in the example |
| Injection point selection | `system_prompt` for persistent structure; `user_message` for per-request context |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Untyped `{{value}}` variable | Forbidden — schema rejects variables without type + example |
| > 7 sections | Exceeds section limit; must consolidate |
| Prose-only template body | 70% LLM compliance — lowest tier; use structured format |
| `quality` non-null | Self-scoring forbidden; always `null` |
| Example Output section missing | LLM cannot verify output shape without a filled reference |
| Mixing mustache and bracket for same tier | Ambiguous variable precedence |
| response_format containing validation rules | Wrong artifact — post-generation validation belongs in validation_schema (P06) |
| Vague section names (`## Details`) | Use action-oriented names: `## Remediation Steps`, `## Score Breakdown` |
## Application
1. Identify the target artifact kind and consumer type (machine / config / human)
2. Select `format_type` based on consumer: machine = `json`, config = `yaml`, human = `markdown`
3. Write frontmatter: 12 required fields; `quality: null`; add `target_kind` and `sections` list
4. Write `## Format Specification` — output structure, format_type rationale, compliance notes
5. Write `## Variables Table` — every variable with type, constraints, required/optional, example
6. Write `## Template Body` — actual template using `{{REQUIRED}}` and `[OPTIONAL]` placeholders
7. Write `## Example Output` — fully filled; zero remaining placeholders
8. Verify body <= 4096 bytes; sections count 4–7; `id` matches filename stem
## References
- response-format-builder MANIFEST.md v1.0.0
- response_format SCHEMA.md v2.0.0
- Boundary: response_format (LLM sees, pre-gen) vs validation_schema (P06, system applies post-gen) vs parser (P05, extracts data) vs formatter (P05, transforms format)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_response_format]] | downstream | 0.51 |
| [[p03_ins_response_format]] | related | 0.46 |
| [[bld_architecture_response_format]] | downstream | 0.41 |
| [[response-format-builder]] | related | 0.39 |
| [[p03_sp_response_format_builder]] | upstream | 0.37 |
| [[bld_collaboration_response_format]] | related | 0.36 |
| [[bld_examples_response_format]] | downstream | 0.36 |
| [[bld_knowledge_card_prompt_template]] | sibling | 0.34 |
| [[p11_qg_response_format]] | downstream | 0.32 |
| [[bld_memory_response_format]] | downstream | 0.31 |
