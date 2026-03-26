---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for signal
pattern: classify -> compose -> validate
---

# Instructions: How to Produce a signal

## Phase 1: CLASSIFY
1. Confirm the request is a runtime event, not an instruction or routing rule
2. Identify the event slug for naming: `satellite_complete`, `build_error`, `batch_progress`
3. Determine emitter satellite and target consumer context
4. Select status: `complete`, `error`, or `progress`
5. Gather optional metadata only if it helps automation

## Phase 2: COMPOSE
1. Read SCHEMA.md first
2. Use OUTPUT_TEMPLATE.md as a direct derivative of SCHEMA.md
3. Emit filename as `p12_sig_{event}.json`
4. Fill minimum payload fields exactly once
5. Keep values machine-friendly: lowercase enums, numeric quality, ISO timestamp
6. Add optional fields only if they are compact and relevant

## Phase 3: VALIDATE
1. Check HARD gates in QUALITY_GATES.md
2. Cross-check filename, payload shape, and CONFIG.md restrictions
3. Confirm the artifact is still atomic and not drifting into handoff scope
4. Confirm the signal remains under 4096 bytes
5. If validation fails, revise in the same pass before output
