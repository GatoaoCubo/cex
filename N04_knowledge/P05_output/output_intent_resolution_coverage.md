---
id: n04_output_intent_resolution_coverage
kind: context_doc
pillar: P01
title: "Kind KC Coverage Audit: Natural Language Discovery Paths"
version: 1.0.0
created: 2026-04-08
author: N04_knowledge
mission: CANONICALIZATION
wave: 1
quality: 8.9
tags: [audit, coverage, intent-resolution, discovery, kind-kc]
related:
  - p01_kc_prompt_compiler
  - output_kc_quality_audit_20260408
  - audit_intent_resolution
  - bld_instruction_kind
  - p03_ins_prompt_compiler
  - p10_out_taxonomy_map
  - p10_out_sql_migration
  - output-validator-builder
  - bld_collaboration_kind
  - bld_knowledge_card_prompt_compiler
---

# Kind KC Coverage Audit: Natural Language Discovery

## Executive Summary

**123 kinds exist. 123 KCs exist. 0 have explicit natural language discovery paths.**

Every kind has a KC file, but none are optimized for intent resolution. A user saying "I need a test" has no structured path to discover `unit_eval` vs `e2e_eval` vs `smoke_eval` vs `golden_test` vs `benchmark`. The system relies entirely on exact kind names or short keyword lists.

## Coverage Matrix

| Field | KCs with field | KCs without | Coverage | Role in Discovery |
|-------|---------------|-------------|----------|-------------------|
| File exists | 123/123 | 0 | 100% | Base existence |
| `keywords` | 121/123 | 2 | 98.4% | Short-form discovery (3-5 terms) |
| `when_to_use` | 122/123 | 1 | 99.2% | Situational trigger (1 sentence) |
| `tldr` | 122/123 | 1 | 99.2% | Quick summary for retrieval ranking |
| Cross-Framework Map | 110/123 | 13 | 89.4% | Provider vocabulary mapping |
| `long_tails` | 18/123 | 105 | **14.6%** | Natural language query matching |
| `aliases` | 18/123 | 105 | **14.6%** | Alternative names for kind |
| `also_known_as` | 0/123 | 123 | **0%** | Cross-provider synonyms (superseded by cross_provider) |
| `user_says` | 18/123 | 105 | **14.6%** | Common user phrasings |
| `cross_provider` | 18/123 | 105 | **14.6%** | Framework-specific equivalent mapping |

## Missing Fields Detail

### KCs missing `keywords` (2)
- `kc_landing_page.md` -- newer kind, non-standard frontmatter
- `kc_tagline.md` -- newer kind, non-standard frontmatter

### KCs missing `tldr` (1)
- `kc_landing_page.md`

### KCs missing Cross-Framework Map (13)
These 13 KCs lack the cross-provider mapping table that connects kind names to LangChain, LlamaIndex, DSPy, and provider equivalents. This table is critical for intent resolution because users often use framework-specific terms.

## The Discovery Gap

### Current state: keyword-only discovery

```
User: "I need something to validate my output"
  |
  cex_query.py TF-IDF search over keywords:
  |-- output_validator: keywords=[output, validation, post-llm]
  |-- validator: keywords=[validation, pre-commit, quality-gate]
  |-- validation_schema: keywords=[schema, contract, validation]
  |-- quality_gate: keywords=[quality, score, pass-fail]
  |
  Result: 4 candidates, no disambiguation signal
```

### Desired state: long-tail + alias discovery

```
User: "I need something to validate my output"
  |
  Semantic search over long_tails + aliases + user_says:
  |-- output_validator:
  |     long_tails: ["check if LLM output matches expected format",
  |                   "validate generated text before returning to user"]
  |     user_says: ["check the output", "validate what it produced"]
  |     aliases: ["post-generation validator", "output checker"]
  |
  |-- validator:
  |     long_tails: ["run pre-commit checks on artifact quality",
  |                   "validate YAML frontmatter before saving"]
  |     user_says: ["check the file", "validate this artifact"]
  |
  Result: output_validator wins (long_tail match on "output" + "validate")
```

## Recommendation: Add `long_tails` and `user_says` to All Kind KCs

### Proposed frontmatter additions

```yaml
# Add to every kind KC:
long_tails:
  - "natural language query 1 that should resolve to this kind"
  - "natural language query 2 that should resolve to this kind"
  - "natural language query 3 that should resolve to this kind"
user_says:
  - "common user phrasing 1"
  - "common user phrasing 2"
aliases:
  - "alternative name from LangChain"
  - "alternative name from OpenAI"
  - "alternative name from Google"
```

### Priority tiers for remediation

| Priority | Kinds | Count | Rationale |
|----------|-------|-------|-----------|
| P0 (critical) | Core kinds that users ask for most: `agent`, `prompt_template`, `knowledge_card`, `system_prompt`, `guardrail`, `workflow`, `function_def` | 7 | Highest user-facing frequency |
| P1 (high) | Evaluation kinds with overlapping names: `unit_eval`, `e2e_eval`, `smoke_eval`, `golden_test`, `benchmark`, `scoring_rubric` | 6 | Most disambiguation-critical |
| P2 (medium) | Memory/state kinds: `entity_memory`, `memory_summary`, `session_state`, `runtime_state`, `memory_scope` | 5 | Users say "memory" for all of these |
| P3 (normal) | All remaining kinds | 105 | Batch via overnight evolve |

### Estimated effort

- P0 (7 kinds): Manual curation, 30 min -- requires understanding of common user phrasings
- P1 (6 kinds): Manual curation, 20 min -- requires disambiguation analysis
- P2 (5 kinds): Manual curation, 15 min
- P3 (105 kinds): Automated via `cex_evolve.py` with prompt to add long_tails

### Existing infrastructure that supports this

| Tool | How it helps |
|------|-------------|
| `cex_retriever.py` | Already does TF-IDF -- adding long_tails to corpus would improve recall |
| `cex_query.py` | Builder discovery via TF-IDF -- long_tails would expand vocabulary |
| `cex_8f_motor.py` | Intent parser -- could match against long_tails for kind resolution |
| `kinds_meta.json` | Could add `long_tails` field per kind for fast lookup |

## Metaphor Dictionary Audit Results

### Verified entries (existing dictionary)

All 40 existing entries in `spec_metaphor_dictionary.md` were verified:

| Section | Entries | Industry terms verified? | Issues found |
|---------|---------|------------------------|--------------|
| Game Architecture | 16 | All correct | None |
| Architecture | 8 | All correct | None |
| Process | 9 | All correct | "handoff" noted as CEX convention (not pure industry) |
| Quality | 6 | All correct | None |
| Brand | 4 | All correct | None |

### New entries added (this session)

| Section | New entries | Focus |
|---------|-----------|-------|
| Intent Resolution Metaphors | 6 | translate, understand, fill in blanks, figure out, rewrite, assemble |
| Input/Output Pipeline Metaphors | 6 | feed, spit out, cook, filter, mix, stamp |
| **Total new** | **12** | Input/output/pipeline coverage |

### Missing metaphors identified (future work)

Users may also say:

| User might say | Should map to | Industry term |
|---------------|---------------|---------------|
| "teach it" | fine-tune / few-shot injection | **in-context learning** |
| "remember this" | persist to memory | **entity memory** / knowledge persistence |
| "forget this" | prune memory | **memory eviction** |
| "connect to X" | integrate API/MCP | **tool registration** / MCP server |
| "speed it up" | optimize latency | **inference optimization** |
| "make it cheaper" | reduce cost | **token budget optimization** |
| "make it smarter" | improve quality | **prompt optimization** / model upgrade |
| "test it" | run evaluation | **evaluation** (unit/e2e/smoke) |

These 8 entries are candidates for the next metaphor dictionary update.

## Rosetta Stone Expansion Summary

Added Section 8: "Intent Resolution & Input Processing Concepts" with 8 rows mapping across:
- 4 providers (Anthropic, OpenAI, Google, MCP)
- 2 frameworks (LangChain, DSPy)
- CEX implementation

Concepts covered: intent classification, query rewriting, context assembly, slot filling, input normalization, intent-to-kind mapping, prompt composition, disambiguation.

## Boundary

Contexto de dominio para hidratar prompts. NAO eh knowledge_card (sem density gate) nem glossary_entry (nao define termo).


## 8F Pipeline Function

Primary function: **INJECT**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_prompt_compiler]] | downstream | 0.25 |
| [[output_kc_quality_audit_20260408]] | related | 0.22 |
| [[audit_intent_resolution]] | related | 0.22 |
| [[bld_instruction_kind]] | downstream | 0.22 |
| [[p03_ins_prompt_compiler]] | downstream | 0.20 |
| [[p10_out_taxonomy_map]] | downstream | 0.20 |
| [[p10_out_sql_migration]] | downstream | 0.19 |
| [[output-validator-builder]] | downstream | 0.19 |
| [[bld_collaboration_kind]] | downstream | 0.19 |
| [[bld_knowledge_card_prompt_compiler]] | downstream | 0.19 |
