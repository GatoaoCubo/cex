---
kind: instruction
id: bld_instruction_knowledge_card
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for knowledge_card
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction Knowledge Card"
version: "1.0.0"
author: n03_builder
tags: [knowledge_card, builder, examples]
tldr: "Golden and anti-examples for knowledge card construction, demonstrating ideal structure and common pitfalls."
domain: "knowledge card construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_knowledge_card_builder
  - bld_knowledge_card_knowledge_card
  - p01_kc_knowledge_best_practices
  - bld_instruction_input_schema
  - bld_instruction_instruction
  - bld_instruction_kind
  - bld_instruction_output_validator
  - p01_kc_creation_best_practices
  - bld_instruction_context_doc
  - bld_instruction_memory_scope
---

# Instructions: How to Produce a knowledge_card
## Phase 1: RESEARCH
1. Identify the topic: what single atomic fact or pattern needs capturing?
2. Gather sources: official documentation, URLs, code references, or established expert knowledge
3. Extract key facts — concrete data points (numbers, dates, names, measurements), not opinions or vague claims
4. Determine the KC type:
   - domain_kc: external knowledge about a tool, API, protocol, or domain
   - meta_kc: internal pattern or lesson learned from operating this system
5. Check existing knowledge_cards via brain_query [IF MCP] for the same topic — avoid duplicates
6. Assess information density: can you reach >= 0.80 density (tables, code, concrete bullets over filler prose)?
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all frontmatter fields and body constraints
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints exactly
3. Fill frontmatter: 14 required fields + 5 CEX extended fields (null is acceptable for recommended fields)
4. Set quality: null — never self-score
5. Write the body following the structure for the KC type:
   - domain_kc: Quick Reference, Key Concepts, Strategy Phases, Golden Rules, Flow, Comparativo, References
   - meta_kc: Executive Summary, Spec Table, Patterns, Anti-Patterns, Application, References
6. Prefer high-density formats: tables and code blocks over paragraphs
7. Keep every bullet at or below 80 characters
8. Include at least one external URL in the References section
9. Write axioms in frontmatter as ALWAYS / NEVER / IF-THEN rules — at least one required
10. Keep body between 200 and 5120 bytes
## Phase 3: VALIDATE
1. Run `python _tools/validate_kc.py <file>` if available — this is an active automated tool
2. HARD gates (all must pass):
   - YAML frontmatter parses without errors
   - id matches pattern `p01_kc_[a-z][a-z0-9_]+`
   - kind == knowledge_card
   - quality == null
   - density >= 0.80
   - at least 3 concrete facts present (numbers, dates, named entities)
   - body is between 200 and 5120 bytes
   - no internal paths in body (records/, .claude/, /home/)
   - no filler sentences ("this document covers", "as mentioned above")
3. SOFT gates (score each against QUALITY_GATES.md):
   - tldr contains concrete data, not generic description
   - axioms are in ALWAYS / NEVER / IF-THEN form
   - at least 4 sections with at least 3 non-empty lines each
   - keywords and long_tails present for search
4. Cross-check scope boundaries:
   - atomic searchable fact, not a broad domain overview (context_doc)?
   - not a term definition (glossary_entry)?
   - not an embedding configuration file?
   - are the facts concrete (numbers, dates, names) rather than vague claims?
5. If a HARD gate fails: fix immediately and re-run the validator
6. If score < 8.0: expand thin sections, replace prose with tables or code blocks, remove filler


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_knowledge_card_builder]] | related | 0.39 |
| [[bld_knowledge_card_knowledge_card]] | upstream | 0.38 |
| [[p01_kc_knowledge_best_practices]] | upstream | 0.34 |
| [[bld_instruction_input_schema]] | sibling | 0.34 |
| [[bld_instruction_instruction]] | sibling | 0.31 |
| [[bld_instruction_kind]] | sibling | 0.30 |
| [[bld_instruction_output_validator]] | sibling | 0.29 |
| [[p01_kc_creation_best_practices]] | upstream | 0.29 |
| [[bld_instruction_context_doc]] | sibling | 0.29 |
| [[bld_instruction_memory_scope]] | sibling | 0.28 |
