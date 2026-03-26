---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for spawn_config
pattern: 3-phase pipeline (classify -> compose -> validate)
---

# Instructions: How to Produce a spawn_config

## Phase 1: CLASSIFY
1. Identify the spawn scenario: how many satellites? How many tasks?
2. Select mode: solo (1 sat, 1 task), grid (N sats, N tasks), continuous (>6 tasks, auto-refill)
3. Check existing spawn_configs via brain_query (avoid duplicates)
4. Determine satellite-model pairing from STELLA routing table
5. Identify required MCP servers for the satellite

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Fill frontmatter: all 19 fields (null OK for optional)
4. Set quality: null (NEVER self-score)
5. Write Spawn Command section: exact PowerShell command ready to execute
6. Write Parameters section: table with value and rationale for each parameter
7. Write Constraints section: safety notes, RAM limits, concurrent satellite limits
8. Verify flags include baseline (--dangerously-skip-permissions, --no-chrome)
9. Check body <= 3072 bytes

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually (no automated validator yet)
2. HARD gates (all must pass): YAML parses, id matches p12_spawn_ pattern, kind == spawn_config, quality == null, required fields present, body has all 3 sections, mode is valid enum
3. SOFT gates: check each against QUALITY_GATES.md
4. Cross-check: flags include baseline? timeout is reasonable? model matches satellite routing?
5. If score < 8.0: revise in same pass before outputting
