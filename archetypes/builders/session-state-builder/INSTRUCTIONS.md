---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for session_state
pattern: capture -> compose -> validate
---

# Instructions: How to Produce a session_state

## Phase 1: CAPTURE
1. Identify the agent or satellite whose session is being captured
2. Determine the session identifier (unique per execution context)
3. Record current session status: active, paused, completed, or aborted
4. Note the session start timestamp in ISO 8601 format
5. Collect optional runtime data: tasks, tokens, tools, errors
6. brain_query [IF MCP] for existing session snapshots to avoid duplicates

## Phase 2: COMPOSE
1. Read SCHEMA.md first
2. Use OUTPUT_TEMPLATE.md as a direct derivative of SCHEMA.md
3. Set filename as `p10_ss_{session_slug}.yaml`
4. Fill all required fields exactly once
5. Set quality: null (NEVER self-score)
6. Write Active Context section with current tasks and execution state
7. Write Resource Usage section with tokens, tools, time data
8. Write Checkpoints section with recovery points if available
9. Add optional fields only if they are compact and relevant
10. Omit absent optional fields instead of using placeholders

## Phase 3: VALIDATE
1. Check HARD gates in QUALITY_GATES.md
2. Verify YAML parses correctly
3. Cross-check filename matches id pattern `p10_ss_*`
4. Confirm the artifact is ephemeral and not drifting into runtime_state scope
5. Confirm the snapshot remains under 3072 bytes
6. If validation fails, revise in the same pass before output
