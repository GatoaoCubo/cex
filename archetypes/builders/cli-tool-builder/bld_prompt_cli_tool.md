---
kind: instruction
id: bld_instruction_cli_tool
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for cli_tool
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.1
title: "Instruction Cli Tool"
version: "1.0.0"
author: n03_builder
tags: [cli_tool, builder, examples]
tldr: "Golden and anti-examples for cli tool construction, demonstrating ideal structure and common pitfalls."
domain: "cli tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_output_validator
  - bld_instruction_retriever_config
  - bld_instruction_memory_scope
  - bld_instruction_chunk_strategy
  - bld_instruction_prompt_version
  - bld_instruction_handoff_protocol
  - bld_instruction_constraint_spec
  - bld_instruction_hook_config
  - bld_instruction_search_tool
  - bld_instruction_client
---

# Instructions: How to Produce a cli_tool
## Phase 1: RESEARCH
1. Identify the task the tool performs (build, lint, convert, generate, upload, etc.)
2. Define every command and subcommand the tool exposes (concrete verb names)
3. List flags and args for each command with types and defaults
4. Determine output format: text, json, table, or yaml
5. Define exit codes with semantic meaning (0=success, 1=user error, 2=system error, etc.)
6. Map config file path and format (if any) and env var overrides with precedence order
7. Check for existing cli_tool artifacts to avoid duplicates
8. Confirm tool slug for id: snake_case, lowercase, no hyphens
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Write Commands section: for each command, list name, description, args, and flags with types
5. Write Output Format section: selected format with concrete examples of success and error output
6. Write Exit Codes section: numeric code plus meaning for every defined code
7. Write Config section: file format, env var overrides, and precedence order
8. Write Dependencies section: runtime requirements (language version, system binaries, etc.)
9. Verify body <= 1024 bytes
10. Verify id matches `^p04_ct_[a-z][a-z0-9_]+$`
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p04_ct_`
4. Confirm kind == cli_tool
5. Confirm commands are listed and each has exit codes defined
6. Confirm output format is specified with examples
7. HARD gates: frontmatter valid, id pattern matches, commands listed, exit codes defined, output format specified
8. SOFT gates: score against QUALITY_GATES.md
9. Cross-check: one-shot execution (not a daemon that runs persistently)? Not a phased process (skill)? Not pluggable into another system (plugin)?
10. Revise if score < 8.0 before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify cli
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | cli tool construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_output_validator]] | sibling | 0.47 |
| [[bld_instruction_retriever_config]] | sibling | 0.46 |
| [[bld_instruction_memory_scope]] | sibling | 0.46 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.44 |
| [[bld_instruction_prompt_version]] | sibling | 0.44 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.43 |
| [[bld_instruction_constraint_spec]] | sibling | 0.43 |
| [[bld_instruction_hook_config]] | sibling | 0.42 |
| [[bld_instruction_search_tool]] | sibling | 0.42 |
| [[bld_instruction_client]] | sibling | 0.42 |
