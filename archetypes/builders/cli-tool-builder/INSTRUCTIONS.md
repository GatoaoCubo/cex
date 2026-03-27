---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for cli_tool
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a cli_tool

## Phase 1: RESEARCH
1. Identify the tool name and primary purpose (build, lint, convert, generate, etc.)
2. List every command the tool exposes (concrete verb names)
3. List flags and args for each command (with types and defaults)
4. Determine output_format: text, json, table, or yaml
5. Define exit_codes with semantic meaning (0=success, 1=error, etc.)
6. Identify config_file path and format (if any)
7. Check for existing cli_tool artifacts via brain_query [IF MCP] (avoid duplicates)
8. Confirm tool slug for id: snake_case, lowercase, no hyphens

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill {{vars}} following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Write commands list with exact names matching ## Commands body section
5. Write ## Overview: 1-2 sentences on what tool does and who uses it
6. Write ## Commands: for each command, define syntax, flags, args, behavior
7. Write ## Output: output format, exit codes, stderr vs stdout
8. Write ## Configuration: config file, env vars, defaults
9. Verify body <= 1024 bytes
10. Verify id matches `^p04_cli_[a-z][a-z0-9_]+$`

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm commands list matches command names in ## Commands section (zero drift)
4. Confirm quality == null
5. Confirm body has all 4 required sections
6. Confirm body <= 1024 bytes
7. Score SOFT gates against QUALITY_GATES.md
8. Revise if score < 8.0 before outputting
