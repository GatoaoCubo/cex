---
kind: instruction
id: bld_instruction_dispatch_rule
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for dispatch_rule
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.2
title: "Instruction Dispatch Rule"
version: "1.0.0"
author: n03_builder
tags: [dispatch_rule, builder, examples]
tldr: "Golden and anti-examples for dispatch rule construction, demonstrating ideal structure and common pitfalls."
domain: "dispatch rule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_context_doc
  - p03_sp_dispatch_rule_builder
  - bld_instruction_output_validator
  - bld_instruction_memory_scope
  - bld_instruction_handoff_protocol
  - bld_instruction_retriever_config
  - bld_instruction_chunk_strategy
  - bld_instruction_prompt_version
  - bld_instruction_hook_config
  - bld_instruction_constraint_spec
---

# Instructions: How to Produce a dispatch_rule
## Phase 1: CLASSIFY
1. Identify the domain scope for this routing rule (research, build, marketing, orchestration, execute, knowledge, monetize)
2. List 3–8 keywords that trigger this rule, covering both Portuguese and English variants of the domain terms
3. Determine the target agent_group and the model it runs (opus for build/execute, sonnet for research/marketing/knowledge)
4. Define the confidence threshold for a keyword match to be considered authoritative (minimum 0.65)
5. Specify fallback behavior when confidence falls below threshold: pass to next rule, route to a default agent_group, or reject with an error
6. Assign priority level: 7–8 for core domain rules, 5–6 for supporting or overlapping domains
7. Check existing dispatch_rules in P12 for scope overlap — two rules must not claim the same keywords without explicit priority separation
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints
3. Fill all required frontmatter fields; set `quality: null` — never self-score
4. Write **Keywords** section: full list of PT and EN terms that trigger routing, one per line, lowercase
5. Write **Target** section: agent_group name, model, priority level
6. Write **Confidence** section: threshold value and fuzzy matching behavior (exact, stemmed, semantic)
7. Write **Fallback** section: what happens below threshold — next rule name, default agent_group, or rejection reason
8. Write **Scope Fence** section: which domains this rule covers and which adjacent domains it explicitly excludes
9. Verify body <= 3072 bytes
## Phase 3: VALIDATE
1. Check all HARD gates in QUALITY_GATES.md
2. Confirm `id` matches `^p12_dr_[a-z][a-z0-9_]+$`
3. Confirm `fallback` agent_group differs from the primary `agent_group`
4. Confirm `quality` is the literal null, not a number
5. Confirm no runtime status fields are present (`status`, `timestamp`, `quality_score`)
6. Confirm no execution instruction fields are present (`tasks`, `scope_fence`, `commit`)
7. Confirm body <= 3072 bytes
8. Cross-check: is this a routing policy? If it contains execution steps it is a handoff, not a dispatch_rule. If it records events it is a signal. If it sequences workflow stages it belongs in a workflow artifact.
9. If validation fails, revise in the same pass before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify dispatch
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | dispatch rule construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_context_doc]] | sibling | 0.42 |
| [[p03_sp_dispatch_rule_builder]] | related | 0.42 |
| [[bld_instruction_output_validator]] | sibling | 0.42 |
| [[bld_instruction_memory_scope]] | sibling | 0.42 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.42 |
| [[bld_instruction_retriever_config]] | sibling | 0.42 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.40 |
| [[bld_instruction_prompt_version]] | sibling | 0.40 |
| [[bld_instruction_hook_config]] | sibling | 0.39 |
| [[bld_instruction_constraint_spec]] | sibling | 0.38 |
