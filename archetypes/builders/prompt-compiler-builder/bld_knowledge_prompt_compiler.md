---
kind: knowledge_card
id: bld_knowledge_card_prompt_compiler
pillar: P03
llm_function: INJECT
purpose: Domain knowledge for prompt_compiler production -- atomic searchable facts
sources: prompt-compiler-builder MANIFEST.md + SCHEMA.md
quality: 9.0
title: "Knowledge Card Prompt Compiler"
version: "1.0.0"
author: n03_builder
tags: [prompt_compiler, builder, knowledge_card, P03]
tldr: "Domain knowledge for prompt_compiler: intent resolution, DSPy compilation, multilingual NLU, 8F integration."
domain: "prompt_compiler construction"
created: "2026-04-12"
updated: "2026-04-12"
density_score: 0.90
related:
  - p01_kc_prompt_compiler
  - p03_ins_prompt_compiler
  - p03_sp_prompt_compiler_builder
  - prompt-compiler-builder
  - p11_qg_prompt_compiler
  - bld_memory_prompt_compiler
  - bld_architecture_prompt_compiler
  - bld_output_template_prompt_compiler
  - bld_examples_prompt_compiler
  - bld_schema_prompt_compiler
---

# Domain Knowledge: prompt_compiler
## Executive Summary
A prompt_compiler is a dense intent resolution artifact that maps natural language user input to structured {kind, pillar, nucleus, verb} tuples. Unlike router (provider-to-provider with confidence thresholds), dispatch_rule (task-to-agent keyword map), or prompt_template (template with `{{variables}}`), a prompt_compiler handles the FIRST resolution step -- determining WHAT the user wants before any routing, dispatching, or template-filling occurs.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P03 (prompt) |
| ID pattern | `^p03_pc_[a-z][a-z0-9_]+$` |
| Required frontmatter fields | 14 (includes `coverage`, `languages`) |
| Default `coverage` | 124 (all registered kinds) |
| Max body | 16384 bytes |
| Body sections | 7 (Preamble, Kind Resolution, Verb Resolution, Ambiguity, Fallback, Routing Matrix, Behavioral) |
| Naming | `p03_pc_{slug}.md` |
| llm_function | CONSTRAIN (F1 in 8F pipeline) |
## Patterns
| Pattern | Rule |
|---------|------|
| Kind Resolution entry | kind, pillar, nucleus, patterns_en, patterns_pt, verb, 8f_emphasis, boundary |
| Coverage integrity | `coverage` field MUST equal actual kinds in table |
| Multilingual requirement | >= 80% of EN patterns should have community language equivalents |
| Verb canonicalization | User verbs map to one of: create, improve, rebuild, analyze, validate, document, integrate, test, deploy, configure, optimize, audit, schedule, monitor |
| Fallback confidence | Unrecognized input must report confidence level |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Partial kind coverage | Unmapped kinds mean lost user intents |
| Machine-translated patterns | PT-BR users phrase differently than EN literal translations |
| Missing boundary notes | Similar kinds get confused (router vs dispatch_rule) |
| Prose instead of tables | 3x lower density; harder for LLM to parse |
| Silent fallback | User must know when confidence is low |
## Industry References
| System | Term | Relationship to prompt_compiler |
|--------|------|--------------------------------|
| DSPy | prompt compilation | Direct inspiration -- "compile signatures into optimized prompts" |
| Rasa / Dialogflow / Lex | intent resolution | Same function -- map text to structured intent |
| LlamaIndex / Elasticsearch | query rewriting | Related -- rewrite vague input for better retrieval |
| CEX 8F | F1 CONSTRAIN | This IS F1 -- first function in every pipeline |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_prompt_compiler]] | sibling | 0.66 |
| [[p03_ins_prompt_compiler]] | related | 0.58 |
| [[p03_sp_prompt_compiler_builder]] | related | 0.55 |
| [[prompt-compiler-builder]] | related | 0.54 |
| [[p11_qg_prompt_compiler]] | downstream | 0.49 |
| [[bld_memory_prompt_compiler]] | downstream | 0.48 |
| [[bld_architecture_prompt_compiler]] | downstream | 0.43 |
| [[bld_output_template_prompt_compiler]] | downstream | 0.43 |
| [[bld_examples_prompt_compiler]] | downstream | 0.42 |
| [[bld_schema_prompt_compiler]] | downstream | 0.42 |
