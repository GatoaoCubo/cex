---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for hook artifact
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a hook

## Phase 1: RESEARCH
1. Identify the target event (pre_tool_use, post_tool_use, session_start, etc.)
2. Determine execution timing (pre, post, or both)
3. Define the script to execute (path, language, arguments)
4. Determine blocking behavior (blocking hooks must be fast)
5. Define conditions that gate hook execution
6. Determine error handling strategy (ignore, log, fail, retry)
7. Search for existing hooks via brain_query [IF MCP] (avoid duplicates)
8. Identify environment variables needed by the script

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — template to fill
3. Generate hook_slug in snake_case (e.g., post_tool_law12_tracker)
4. Fill frontmatter: all 16 required fields (quality: null, never self-score)
5. Set trigger_event from enum
6. Set script_path to valid script location
7. Set timeout (blocking hooks: <= 10000ms, async hooks: <= 30000ms)
8. Write Trigger Configuration section: event, conditions, timing
9. Write Script section: path, language, content or description
10. Write Input/Output section: what hook receives and returns
11. Write Error Handling section: per-strategy behavior
12. Check body <= 1024 bytes

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually
2. Verify all 9 HARD gates pass
3. Score each SOFT gate against QUALITY_GATES.md
4. Confirm id matches p04_hook_ pattern
5. Confirm kind == hook
6. Confirm quality == null
7. Confirm trigger_event is valid enum value
8. Confirm timeout > 0 and <= 30000
9. Confirm blocking hooks have timeout <= 10000
10. If score < 8.0: revise before outputting
