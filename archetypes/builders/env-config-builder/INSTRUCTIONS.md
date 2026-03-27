---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for env_config
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce an env_config

## Phase 1: RESEARCH
1. Identify the scope: global, satellite name, or service name
2. List every environment variable the scope needs
3. Classify each variable: type (string, integer, boolean, url, secret)
4. Determine which variables are required vs optional (with defaults)
5. Mark sensitive variables (API keys, tokens, passwords, secrets)
6. Define validation rule for each variable (regex, range, enum, format)
7. Check for existing env_config artifacts via brain_query [IF MCP] (avoid duplicates)
8. Confirm scope slug for id: snake_case, lowercase, no hyphens

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill {{vars}} following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Set scope to concrete value (global, satellite name, service name)
5. Write variables list with exact names matching ## Variable Catalog
6. Write ## Overview: 1-2 sentences on scope, purpose, consumers
7. Write ## Variable Catalog: table with name, type, required, default, sensitive, validation
8. Write ## Override Precedence: env > file > default (or custom order)
9. Write ## Sensitive Variables: list sensitive vars with masking and storage rules
10. Verify body <= 4096 bytes
11. Verify id matches `^p09_env_[a-z][a-z0-9_]+$`

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm variables list matches variable names in ## Variable Catalog (zero drift)
4. Confirm quality == null
5. Confirm body has all 4 required sections
6. Confirm no actual secret values appear anywhere in artifact
7. Confirm body <= 4096 bytes
8. Score SOFT gates against QUALITY_GATES.md
9. Revise if score < 8.0 before outputting
