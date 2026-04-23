---
kind: instruction
id: bld_instruction_code_executor
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for code_executor
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.1
title: "Instruction Code Executor"
version: "1.0.0"
author: n03_builder
tags: [code_executor, builder, examples]
tldr: "Golden and anti-examples for code executor construction, demonstrating ideal structure and common pitfalls."
domain: "code executor construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_memory_scope
  - bld_instruction_output_validator
  - bld_instruction_retriever_config
  - bld_instruction_prompt_version
  - bld_instruction_search_tool
  - bld_instruction_chunk_strategy
  - bld_instruction_constraint_spec
  - bld_instruction_handoff_protocol
  - bld_instruction_hook_config
  - bld_instruction_function_def
---

# Instructions: How to Produce a code_executor
## Phase 1: RESEARCH
1. Identify the execution use case (data analysis, code testing, file processing, etc.)
2. Determine which languages the executor must support (python, node, bash, etc.)
3. Select sandbox type based on isolation requirements (docker, e2b, wasm, vm, process)
4. Define resource limits: timeout, max CPU, max memory, max disk
5. Determine network access policy (isolated vs connected)
6. Determine file I/O needs (read-only, read-write, none)
7. Check for existing code_executor artifacts to avoid duplicates
8. Confirm runtime slug for id: snake_case, lowercase, no hyphens
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Write Overview section: what this executor does and primary use case
5. Write Sandbox section: isolation mechanism, security boundary details
6. Write Languages section: each language with version constraint
7. Write Limits section: timeout, CPU, memory, disk, network policy
8. Verify body <= 2048 bytes
9. Verify id matches `^p04_exec_[a-z][a-z0-9_]+$`
10. Verify timeout > 0
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p04_exec_`
4. Confirm kind == code_executor
5. Confirm sandbox_type is valid enum value
6. Confirm languages list is non-empty with version constraints
7. Confirm timeout > 0
8. HARD gates: frontmatter valid, id pattern, sandbox defined, languages listed, timeout set
9. SOFT gates: score against QUALITY_GATES.md
10. Cross-check: is this sandboxed (not bare metal)? Not a CLI tool? Not a daemon?

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify code
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | code executor construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_memory_scope]] | sibling | 0.53 |
| [[bld_instruction_output_validator]] | sibling | 0.52 |
| [[bld_instruction_retriever_config]] | sibling | 0.52 |
| [[bld_instruction_prompt_version]] | sibling | 0.50 |
| [[bld_instruction_search_tool]] | sibling | 0.49 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.49 |
| [[bld_instruction_constraint_spec]] | sibling | 0.49 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.49 |
| [[bld_instruction_hook_config]] | sibling | 0.46 |
| [[bld_instruction_function_def]] | sibling | 0.46 |
