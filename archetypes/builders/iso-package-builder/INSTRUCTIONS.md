---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for iso_package
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce an iso_package

## Phase 1: DISCOVER
1. Identify the target agent by name and domain
2. Locate the source agent definition (P02 agent artifact or existing iso_vectorstore)
3. Determine the target tier (minimal, standard, complete, or whitelabel)
4. List all files required for the selected tier
5. Search for existing iso_packages via brain_query [IF MCP] (avoid duplicates)
6. Collect system_instruction content from agent's system prompt or PRIME file
7. Measure system_instruction token count (must be <= 4096)
8. Verify no hardcoded paths exist in source materials

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Generate agent_slug in snake_case from agent name
4. Fill manifest.yaml frontmatter: all 14 required fields (quality: null)
5. Set tier to match the target completeness level
6. Write Agent Identity section: one paragraph on who the agent is
7. Write File Inventory table: list every file with pillar, tier requirement, status
8. Write Tier Compliance section: declared tier vs actual files
9. Write Portability Notes: platform dependencies, hardcoded path check
10. Write References section: source agent, builder version
11. Generate system_instruction.md from agent's system prompt
12. Generate instructions.md from agent's execution protocol
13. Generate remaining tier files (architecture.md, examples.md, etc.)
14. Set files_count to match actual files in directory
15. Build lp_mapping object with all included files
16. Check each file is <= 4096 bytes

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually against produced package
2. Verify all 10 HARD gates pass
3. Confirm manifest.yaml YAML parses correctly
4. Confirm id matches p02_iso_ pattern
5. Confirm kind == iso_package
6. Confirm quality == null
7. Confirm 3 required files exist (manifest, system_instruction, instructions)
8. Confirm files_count matches actual directory contents
9. Confirm system_instruction.md <= 4096 tokens
10. Scan all files for hardcoded paths (H10)
11. Score each SOFT gate
12. If score < 8.0: revise files before outputting
