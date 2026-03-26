---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for boot_config
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a boot_config

## Phase 1: RESEARCH
1. Identify the target provider runtime (claude, cursor, codex, etc.)
2. Determine the agent identity (name, role, satellite)
3. Research provider-specific limits (context window, max output, rate limits)
4. List tools/MCPs available on this provider
5. Identify required CLI flags for the provider
6. Search for existing boot_configs via brain_query [IF MCP] (avoid duplicates)
7. Collect provider documentation URLs for reference
8. Note any provider-specific constraints (timeout limits, permission model)

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Generate provider_slug in snake_case from provider name
4. Fill frontmatter: all 15 required fields (quality: null)
5. Build identity object (name, role, satellite)
6. Build constraints object (max_tokens, context_window, timeout_seconds, max_retries)
7. List tools available on this provider
8. Set model to provider's default or recommended model
9. Set temperature appropriate for agent's domain
10. Write Provider Overview section: provider name, runtime type
11. Write Identity Block section: name, role, satellite
12. Write Constraints table: each parameter with value and rationale
13. Write Tools Configuration table: each tool with type and purpose
14. Write Flags section: each flag with purpose
15. Write References section: provider docs, related configs
16. Check body <= 2048 bytes

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually
2. Verify all 9 HARD gates pass
3. Confirm id matches p02_boot_ pattern
4. Confirm kind == boot_config
5. Confirm quality == null
6. Confirm identity has name, role, satellite
7. Confirm constraints has max_tokens, context_window, timeout_seconds
8. Confirm tools is non-empty list
9. Score each SOFT gate
10. If score < 8.0: revise before outputting
