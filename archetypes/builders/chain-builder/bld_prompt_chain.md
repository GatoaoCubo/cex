---
kind: instruction
id: bld_instruction_chain
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for chain
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction Chain"
version: "1.0.0"
author: n03_builder
tags: [chain, builder, examples]
tldr: "Golden and anti-examples for chain construction, demonstrating ideal structure and common pitfalls."
domain: "chain construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p10_lr_chain_builder
  - p11_qg_chain
  - bld_knowledge_card_chain
  - p03_sp_chain_builder
  - bld_instruction_fallback_chain
  - bld_architecture_chain
  - p11_qg_workflow
  - p01_kc_chain
  - tpl_instruction
  - bld_knowledge_card_workflow
---

# Instructions: How to Produce a chain
## Phase 1: RESEARCH
1. Identify the complex task to decompose: state the input and the final output in concrete terms
2. List atomic steps: each step must be exactly one LLM call with one purpose — split any step that requires two decisions into two steps
3. Define data flow between steps: for each connection, specify the exact type (string, list, JSON object, markdown block) of data passed from one step to the next
4. Determine error handling strategy per step: fail_fast for steps where downstream steps cannot proceed without the output, skip for enrichment steps, retry for transient failures, fallback for steps with an acceptable degraded alternative
5. Map branching logic: if any step produces a conditional output, define the condition and both paths explicitly
6. Search for existing chains that perform the same transformation (avoid duplicates)
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — template to fill
3. Fill frontmatter: all 19 fields (quality: null, never self-score)
4. Set quality: null
5. Write Steps section: for each step, provide name, the prompt reference it uses, input type, and output type — all four fields required per step
6. Write Data Flow section: connections between steps with typed inputs and outputs shown explicitly
7. Write Error Handling section: strategy for each step and the global fallback policy
8. Write Branching section: conditions for each path selection, or state "no branching" if the chain is strictly linear
9. Write Context Passing section: specify which data accumulates across steps and which resets at each step boundary
10. Verify steps_count in frontmatter matches the actual number of steps written
11. Keep body <= 8192 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually
2. HARD gate: id matches `p03_ch_` pattern
3. HARD gate: kind == chain
4. HARD gate: quality == null
5. HARD gate: every step has input type and output type specified
6. HARD gate: error handling strategy is specified (at minimum at the global level)
7. HARD gate: each step represents exactly one LLM call — reject any step that describes multiple calls or includes routing logic
8. Cross-check: do the steps reference prompts (not workflows)? Chains belong to P03, workflows belong to P12
9. Cross-check: is there any runtime orchestration logic embedded in the steps? Runtime orchestration is not part of a chain definition
10. Cross-check: are all data types between steps explicit, not implied?
11. If score < 8.0: revise before outputting


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_chain_builder]] | downstream | 0.49 |
| [[p11_qg_chain]] | downstream | 0.47 |
| [[bld_knowledge_card_chain]] | upstream | 0.44 |
| [[p03_sp_chain_builder]] | related | 0.42 |
| [[bld_instruction_fallback_chain]] | sibling | 0.39 |
| [[bld_architecture_chain]] | downstream | 0.39 |
| [[p11_qg_workflow]] | downstream | 0.39 |
| [[p01_kc_chain]] | related | 0.38 |
| [[tpl_instruction]] | sibling | 0.38 |
| [[bld_knowledge_card_workflow]] | upstream | 0.38 |
