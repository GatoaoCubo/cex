---
kind: instruction
id: bld_instruction_env_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for env_config
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction Env Config"
version: "1.0.0"
author: n03_builder
tags: [env_config, builder, examples]
tldr: "Golden and anti-examples for env config construction, demonstrating ideal structure and common pitfalls."
domain: "env config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_env_config_builder
  - bld_instruction_input_schema
  - p11_qg_env_config
  - bld_instruction_context_doc
  - bld_instruction_secret_config
  - env-config-builder
  - bld_instruction_enum_def
  - bld_instruction_instruction
  - bld_instruction_feature_flag
  - bld_instruction_output_validator
---

# Instructions: How to Produce an env_config
## Phase 1: RESEARCH
1. Identify the scope: global (applies to all services), a named agent_group, or a specific service
2. Catalog all environment variables needed within that scope — include name, current or example value, and purpose
3. Classify the type of each variable: string, integer, boolean, URL, or secret
4. Classify the sensitivity of each variable: public (safe to log), internal (omit from logs), or secret (mask in all output)
5. Determine validation rules per variable: regex pattern for strings, numeric range for integers, allowed values enum for controlled sets
6. Define default values and whether each variable is required or optional — optional variables must have a usable default
7. Define override precedence: environment variable wins over config file, which wins over default
8. Check existing env_configs via brain_query [IF MCP] for the same scope — do not duplicate a config that already covers this service
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints
3. Fill all required frontmatter fields; set `quality: null` — never self-score
4. Write **Variable Catalog** section: table with columns name, type, scope, default, required/optional, sensitive flag
5. Write **Validation Rules** section: per variable — pattern or range, allowed values, error message on failure
6. Write **Override Precedence** section: explicit ordering (env > file > default) with scope inheritance rules
7. Write **Secrets Handling** section: masking rules for each secret variable, rotation policy, storage location (vault, platform secrets manager)
8. Write **Groups** section: logical groupings such as database, API keys, feature toggles, file paths
9. Confirm body <= 4096 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm `id` matches `^p09_ev_[a-z][a-z0-9_]+$`
4. Confirm at least one variable is defined
5. Confirm all sensitive variables have masking rules in the Secrets Handling section
6. Confirm validation rules are present for at least the required variables
7. Confirm no actual secret values appear anywhere in the artifact — only placeholders or descriptions
8. Confirm `quality` is null
9. Confirm body <= 4096 bytes
10. Cross-check: are these generic runtime variables? If this is a startup script it belongs in `boot_config`. If these are on/off toggles they belong in `feature_flag`. If this is access control it belongs in `permission`. This artifact catalogs variables, it does not toggle features or control access.
11. If score < 8.0: revise in the same pass before outputting


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_env_config_builder]] | related | 0.44 |
| [[bld_instruction_input_schema]] | sibling | 0.42 |
| [[p11_qg_env_config]] | downstream | 0.39 |
| [[bld_instruction_context_doc]] | sibling | 0.37 |
| [[bld_instruction_secret_config]] | sibling | 0.37 |
| [[env-config-builder]] | downstream | 0.36 |
| [[bld_instruction_enum_def]] | sibling | 0.36 |
| [[bld_instruction_instruction]] | sibling | 0.36 |
| [[bld_instruction_feature_flag]] | sibling | 0.36 |
| [[bld_instruction_output_validator]] | sibling | 0.36 |
