---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for instruction
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce an instruction

## Phase 1: RESEARCH
1. Identify the task: what needs to be done, by whom, in what context
2. Determine prerequisites: what must be true before starting
3. Analyze existing instructions via brain_query (avoid duplicates)
4. Identify dependencies: tools, files, services, permissions needed
5. Determine idempotency: can this be safely re-run?
6. Plan rollback: what happens if execution fails midway?

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Fill frontmatter: all 20 fields (null OK for optional)
4. Set quality: null (NEVER self-score)
5. Write Prerequisites section: verifiable conditions, not vague assumptions
6. Write Steps section: numbered, one action per step, concrete commands/actions
7. Write Validation section: how to verify each step and final outcome
8. Write Rollback section: undo procedure (or "N/A — instruction is idempotent")
9. Verify steps_count matches actual numbered steps in body
10. Check body <= 4096 bytes

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually (no automated validator yet)
2. HARD gates (all must pass): YAML parses, id matches p03_ins_ pattern, kind == instruction, quality == null, required fields present, body has all 4 sections, steps_count matches
3. SOFT gates: check each against QUALITY_GATES.md
4. Cross-check: each step has one action? Prerequisites verifiable? No identity/persona leaked?
5. If score < 8.0: revise in same pass before outputting
