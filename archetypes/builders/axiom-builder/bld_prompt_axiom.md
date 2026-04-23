---
kind: instruction
id: bld_instruction_axiom
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for axiom
pattern: 3-phase pipeline (classify -> compose -> validate)
quality: 9.1
title: "Instruction Axiom"
version: "1.0.0"
author: n03_builder
tags: [axiom, builder, examples]
tldr: "Golden and anti-examples for axiom construction, demonstrating ideal structure and common pitfalls."
domain: "axiom construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_golden_test
  - p03_sp_axiom_builder
  - bld_instruction_memory_scope
  - bld_instruction_output_validator
  - bld_instruction_retriever_config
  - bld_instruction_agent
  - p11_qg_axiom
  - axiom-builder
  - bld_instruction_chunk_strategy
  - bld_instruction_action_prompt
---

# Instructions: How to Produce an axiom
## Phase 1: CLASSIFY
1. Identify the candidate rule: write out the proposed truth in plain language
2. Test immutability: ask "can this rule change under any circumstance without breaking the system?" — if yes, it is not an axiom
3. Test universality: confirm the rule applies across all contexts in its scope, not just specific cases
4. Distinguish type: is this a law (enforced policy), a guardrail (safety boundary), a lifecycle rule (process step), or a fundamental truth? Only fundamental truths qualify as axioms
5. Check for existing axioms that already express the same truth (avoid duplicates)
6. Formulate as a single declarative statement: no conditionals, no conjunctions, one complete thought
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — template to fill
3. Fill frontmatter: all 20 required fields (quality: null, never self-score)
4. Set quality: null
5. Write Statement section: one declarative sentence expressing the immutable truth
6. Write Rationale section: evidence or first-principles reasoning for why this truth is permanent
7. Write Enforcement section: how violations are detected and what response is triggered
8. Write Scope section: declare whether this axiom is universal or bounded, and if bounded, define the boundary
9. Keep total body size <= 3072 bytes
10. Verify information density >= 0.80 (no filler sentences)
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually
2. HARD gate: id matches `p10_ax_` pattern
3. HARD gate: kind == axiom
4. HARD gate: quality == null
5. HARD gate: Statement is a single declarative sentence
6. HARD gate: Statement contains no conditionals ("if", "when", "unless")
7. HARD gate: required fields all present
8. Cross-check: is this truly immutable, or does it drift into law/guardrail territory?
9. Cross-check: does any existing axiom already cover this truth?
10. If score < 8.0: revise before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify axiom
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | axiom construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_golden_test]] | sibling | 0.43 |
| [[p03_sp_axiom_builder]] | related | 0.40 |
| [[bld_instruction_memory_scope]] | sibling | 0.38 |
| [[bld_instruction_output_validator]] | sibling | 0.38 |
| [[bld_instruction_retriever_config]] | sibling | 0.38 |
| [[bld_instruction_agent]] | sibling | 0.38 |
| [[p11_qg_axiom]] | downstream | 0.37 |
| [[axiom-builder]] | downstream | 0.37 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.36 |
| [[bld_instruction_action_prompt]] | sibling | 0.36 |
