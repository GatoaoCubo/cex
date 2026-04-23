---
kind: instruction
id: bld_instruction_context_window_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for context_window_config
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.1
title: "Instruction Context Window Config"
version: "1.0.0"
author: n03_builder
tags: [context_window_config, builder, examples]
tldr: "Golden and anti-examples for context window config construction, demonstrating ideal structure and common pitfalls."
domain: "context window config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_examples_context_window_config
  - bld_config_context_window_config
  - p01_kc_context_window_config
  - bld_instruction_retriever_config
  - bld_instruction_output_validator
  - bld_output_template_context_window_config
  - bld_instruction_memory_scope
  - bld_instruction_handoff_protocol
  - bld_instruction_prompt_cache
  - bld_instruction_prompt_version
---

# Instructions: How to Produce a context_window_config
## Phase 1: RESEARCH
1. Identify target model(s): what model's context window are we configuring?
2. Determine total_tokens: model's hard ceiling (200K for Claude, 128K for GPT-4, etc.)
3. Assess workload: how much RAG context? How many few-shot examples? System prompt size?
4. Profile the use case: RAG-heavy? Few-shot-heavy? Long-form generation?
5. Check existing configs to avoid duplicates
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill the template
3. Allocate budgets: system (10%), examples (15%), context (40%), query (5%), output (30%)
4. Adjust for workload: RAG-heavy → more context, few-shot-heavy → more examples
5. Define priority_tiers: system > query > context > examples (protect identity first)
6. Define overflow_strategy: truncate_lowest, compress, or drop_section
7. Set quality: null
8. Keep file under 2048 bytes
## Phase 3: VALIDATE
1. Verify sum(budgets) + output_reserve <= total_tokens
2. Check output_reserve >= 2000 tokens
3. Verify priority_tiers is ordered list
4. Verify overflow_strategy is valid enum
5. Check id matches `p03_cwc_[a-z][a-z0-9_]+`
6. Verify total file under 2048 bytes
7. If any gate fails: fix and re-validate

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify context
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | context window config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_context_window_config]] | downstream | 0.41 |
| [[bld_config_context_window_config]] | downstream | 0.40 |
| [[p01_kc_context_window_config]] | related | 0.33 |
| [[bld_instruction_retriever_config]] | sibling | 0.31 |
| [[bld_instruction_output_validator]] | sibling | 0.31 |
| [[bld_output_template_context_window_config]] | downstream | 0.30 |
| [[bld_instruction_memory_scope]] | sibling | 0.30 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.30 |
| [[bld_instruction_prompt_cache]] | sibling | 0.30 |
| [[bld_instruction_prompt_version]] | sibling | 0.30 |
