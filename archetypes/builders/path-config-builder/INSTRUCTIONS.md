---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for path_config
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a path_config

## Phase 1: RESEARCH
1. Identify the scope: global, satellite name, or service name
2. List every filesystem path the scope needs
3. Classify each path: type (dir or file)
4. Determine platform compatibility (windows, unix, all)
5. Define default value for each path
6. Determine which paths are required vs optional
7. Check for existing path_config artifacts via brain_query [IF MCP] (avoid duplicates)
8. Confirm scope slug for id: snake_case, lowercase, no hyphens

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill {{vars}} following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Set scope to concrete value (global, satellite, service)
5. Write paths list with exact names matching ## Path Catalog
6. Write ## Overview: 1-2 sentences on scope, purpose, consumers
7. Write ## Path Catalog: table with name, type, platform, default, required, notes
8. Write ## Directory Hierarchy: ASCII tree showing path relationships
9. Write ## Platform Notes: platform differences and resolution rules
10. Verify body <= 3072 bytes
11. Verify id matches `^p09_path_[a-z][a-z0-9_]+$`

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm paths list matches path names in ## Path Catalog (zero drift)
4. Confirm quality == null
5. Confirm body has all 4 required sections
6. Confirm no user-specific absolute paths (use expandable vars)
7. Confirm body <= 3072 bytes
8. Score SOFT gates against QUALITY_GATES.md
9. Revise if score < 8.0 before outputting
