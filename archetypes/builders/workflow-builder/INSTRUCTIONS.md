---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for workflow
pattern: 3-phase pipeline (plan -> compose -> validate)
---

# Instructions: How to Produce a workflow

## Phase 1: PLAN
1. Identify the mission: what end-to-end outcome is needed?
2. Decompose into steps with clear agent assignments (which satellite does what)
3. Analyze existing workflows via brain_query [IF MCP] (avoid duplicates)
4. Map dependencies: which steps must complete before others start?
5. Determine execution mode: sequential (safe), parallel (fast), mixed (optimized)
6. Identify signals needed per step (reference signal-builder conventions)
7. Check spawn_configs exist for each satellite involved

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Fill frontmatter: all 20 fields (null OK for optional)
4. Set quality: null (NEVER self-score)
5. Write Purpose section: 2-4 sentences on what mission this workflow accomplishes
6. Write Steps section: numbered steps with Agent/Action/Input/Output/Signal/Depends
7. Write Dependencies section: prerequisites that must exist before workflow starts
8. Write Signals section: what signals are emitted and when
9. Verify steps_count matches actual steps in body
10. Check body <= 3072 bytes

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually (no automated validator yet)
2. HARD gates (all must pass): YAML parses, id matches p12_wf_ pattern, kind == workflow, quality == null, required fields present, body has all 4 sections, steps_count matches, execution is valid enum
3. SOFT gates: check each against QUALITY_GATES.md
4. Cross-check: steps have agent assignments? Dependencies form valid order? Signals reference signal conventions? No prompt chaining leaked?
5. If score < 8.0: revise in same pass before outputting
