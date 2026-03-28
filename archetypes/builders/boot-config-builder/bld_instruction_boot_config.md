---
kind: instruction
id: bld_instruction_boot_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for boot_config
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a boot_config
## Phase 1: RESEARCH
1. Identify the target agent this config initializes
2. Determine the provider: claude, cursor, or codex — these are the valid enum values
3. Map provider capabilities: available tools, MCP servers supported, context window size
4. Define identity block requirements: what name, role, and satellite assignment this agent carries
5. Establish constraint parameters: max tokens, context window, timeout in seconds, max retries, temperature appropriate for the agent's domain
6. Search for existing boot_configs for this agent-provider combination (avoid duplicates)
7. Identify MCP configuration needs: which servers must be available, which params each server requires
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — template to fill
3. Fill frontmatter: all 15 required fields plus 7 recommended fields (quality: null, never self-score)
4. Write Identity Block section: name, role, satellite — these three fields are mandatory
5. Write Constraints section: tokens, context window, timeout, retries, and temperature — all numeric
6. Write Tools section: enable/disable flags for each tool available on this provider
7. Write MCP Configuration section: list each server with its params
8. Write CLI Flags section: provider-specific flags with purpose of each
9. Write Permissions section: scoped permissions required for this agent on this provider
10. Keep body <= 2048 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually
2. HARD gate: id matches `p02_bc_` pattern
3. HARD gate: kind == boot_config
4. HARD gate: quality == null
5. HARD gate: provider is one of the valid enum values (claude, cursor, codex)
6. HARD gate: identity block contains name, role, and satellite
7. HARD gate: all constraint values are numeric (not strings)
8. Cross-check: is this config provider-specific rather than generic? A generic config is not a boot_config
9. Cross-check: is this a boot_config and not an env_config (environment variables) or spawn_config (process launch)?
10. If score < 8.0: revise before outputting
