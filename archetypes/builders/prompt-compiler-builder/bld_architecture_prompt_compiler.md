---
kind: architecture
id: bld_architecture_prompt_compiler
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of prompt_compiler -- inventory, dependencies, and position
quality: 9.1
title: "Architecture Prompt Compiler"
version: "1.0.0"
author: n03_builder
tags: [prompt_compiler, builder, architecture, P03]
tldr: "Architectural position of prompt_compiler in CEX: first in 8F pipeline, between user input and kind resolution."
domain: "prompt_compiler construction"
created: "2026-04-12"
updated: "2026-04-12"
density_score: 0.90
related:
  - prompt-compiler-builder
  - p03_sp_prompt_compiler_builder
  - p03_ins_prompt_compiler
  - p01_kc_prompt_compiler
  - bld_output_template_prompt_compiler
  - bld_knowledge_card_prompt_compiler
  - p11_qg_prompt_compiler
  - bld_examples_prompt_compiler
  - bld_collaboration_prompt_compiler
  - bld_schema_prompt_compiler
---

# Architecture: prompt_compiler in CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, coverage, languages) | prompt-compiler-builder | active |
| kind_resolution_table | All 300 kinds mapped to user patterns | author | active |
| verb_resolution_table | User verbs mapped to canonical actions | author | active |
| ambiguity_resolver | Protocol for multi-kind matches | author | active |
| fallback_heuristics | Handling unrecognized input | author | active |
| nucleus_routing_matrix | Kind-to-nucleus mapping | author | active |
| behavioral_instructions | Rules for LLM as prompt compiler | author | active |
## Dependency Graph
```
user_input   --resolved_by-->  prompt_compiler  --produces-->  {kind, pillar, nucleus, verb}
                                     |
                                     +--reads-->  kinds_meta.json
                                     +--reads-->  _schema.yaml (per pillar)
                                     +--feeds-->  router (P02), dispatcher (P12), builder (N03)
```
| From | To | Type | Data |
|------|----|------|------|
| user_input | prompt_compiler | data_flow | natural language text (PT or EN) |
| kinds_meta.json | prompt_compiler | dependency | 124 kind definitions |
| prompt_compiler | 8F pipeline (F1) | produces | resolved {kind, pillar, nucleus, verb} |
| prompt_compiler | router (P02) | feeds | resolved kind for provider routing |
| prompt_compiler | dispatch_rule (P12) | feeds | resolved nucleus for task dispatch |
## Boundary Table
| prompt_compiler IS | prompt_compiler IS NOT |
|-------------------|----------------------|
| Intent resolution from user input to {kind, pillar, nucleus} | Provider routing with confidence thresholds (router P02) |
| Bilingual pattern matching (PT-BR + EN) | Task-to-agent keyword mapping (dispatch_rule P12) |
| First function in 8F pipeline (F1 CONSTRAIN) | Template with `{{variables}}` (prompt_template P03) |
| Loaded as prompt layer by cex_prompt_layers.py | A runtime agent with capabilities (agent P02) |
| Covers all 124 registered kinds | A subset of kinds for one domain |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Input | user_input, language detection | Raw natural language from user |
| Resolution | kind_resolution_table, verb_resolution_table | Pattern match to {kind, pillar, nucleus, verb} |
| Disambiguation | ambiguity_resolver | Handle multi-kind matches |
| Fallback | fallback_heuristics | Handle unrecognized input |
| Output | {kind, pillar, nucleus, verb} tuple | Feed to 8F F1 CONSTRAIN |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[prompt-compiler-builder]] | upstream | 0.52 |
| [[p03_sp_prompt_compiler_builder]] | upstream | 0.48 |
| [[p03_ins_prompt_compiler]] | upstream | 0.47 |
| [[p01_kc_prompt_compiler]] | upstream | 0.45 |
| [[bld_output_template_prompt_compiler]] | upstream | 0.44 |
| [[bld_knowledge_card_prompt_compiler]] | upstream | 0.42 |
| [[p11_qg_prompt_compiler]] | downstream | 0.41 |
| [[bld_examples_prompt_compiler]] | upstream | 0.39 |
| [[bld_collaboration_prompt_compiler]] | upstream | 0.37 |
| [[bld_schema_prompt_compiler]] | upstream | 0.35 |
