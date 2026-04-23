---
kind: instruction
id: bld_instruction_action_prompt
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for action_prompt
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.1
title: "Instruction Action Prompt"
version: "1.0.0"
author: n03_builder
tags: [action_prompt, builder, examples]
tldr: "Golden and anti-examples for action prompt construction, demonstrating ideal structure and common pitfalls."
domain: "action prompt construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_golden_test
  - bld_instruction_instruction
  - bld_instruction_input_schema
  - bld_instruction_output_validator
  - bld_instruction_prompt_version
  - action-prompt-builder
  - bld_instruction_memory_scope
  - bld_instruction_retriever_config
  - p03_sp_action_prompt_builder
  - bld_instruction_handoff_protocol
---

# Instructions: How to Produce an action_prompt
## Phase 1: RESEARCH
1. Identify the action: what task needs a prompt, expressed as a verb phrase
2. Define input contract: what data types and formats are provided to the prompt
3. Define output contract: what the result should look like (structure, format, constraints)
4. Analyze existing action_prompts via brain_query [IF MCP] to avoid duplicates
5. Enumerate edge cases: at least 2 scenarios where input is ambiguous or malformed
6. Determine constraints: what the prompt must NOT do (no identity, no multi-step recipes)
7. Identify purpose: WHY this action prompt exists (business value, not just mechanics)
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Fill frontmatter: all 21 fields (null OK for optional)
4. Set quality: null (NEVER self-score)
5. Write Context section: 2-3 sentences on background and purpose of the action
6. Write Input section: specific data items with types, required/optional, and defaults
7. Write Execution section: concise steps to transform input into output (no sub-steps)
8. Write Output section: expected structure, format, and one inline example
9. Write Validation section: criteria to verify output correctness and completeness
10. Check body <= 3072 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually (no automated validator yet)
2. HARD gates: YAML parses, id matches `p03_ap_` pattern, kind == action_prompt, quality == null, required fields present, body has all 5 sections, edge_cases >= 2
3. SOFT gates: check each against QUALITY_GATES.md
4. Cross-check: action is verb phrase? Input has types? No identity/persona leaking? No detailed multi-step recipe (that would be instruction)?
5. If score < 8.0: revise in same pass before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify action
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | action prompt construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_golden_test]] | sibling | 0.44 |
| [[bld_instruction_instruction]] | sibling | 0.42 |
| [[bld_instruction_input_schema]] | sibling | 0.41 |
| [[bld_instruction_output_validator]] | sibling | 0.40 |
| [[bld_instruction_prompt_version]] | sibling | 0.40 |
| [[action-prompt-builder]] | related | 0.40 |
| [[bld_instruction_memory_scope]] | sibling | 0.39 |
| [[bld_instruction_retriever_config]] | sibling | 0.38 |
| [[p03_sp_action_prompt_builder]] | related | 0.38 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.37 |
