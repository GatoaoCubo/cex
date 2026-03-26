---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for golden_test
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a golden_test

## Phase 1: RESEARCH
1. Identify the target_kind: which artifact type needs a golden reference
2. Find existing golden_tests for the same target_kind (search P07_evals/examples/)
3. Locate the QUALITY_GATES.md of the target_kind's builder
4. Select a candidate artifact scoring >= 9.5 (or craft one from scratch)
5. Check brain_query [IF MCP] for duplicate golden_tests

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill following SCHEMA constraints
3. Fill frontmatter: all 17 required + 5 recommended fields (quality: null)
4. Set quality_threshold to 9.5 or higher
5. Write Input Scenario section: the complete request verbatim
6. Write Golden Output section: the complete artifact with no abbreviation
7. Write Rationale section: map each quality dimension to gate IDs
8. Write Evaluation Criteria section: specific checks this golden validates

## Phase 3: VALIDATE
1. Check against QUALITY_GATES.md (this builder's own gates)
2. HARD: id format, kind, pillar, quality==null, quality_threshold >= 9.5
3. SOFT: rationale maps to gates, output is complete, reviewer assigned
4. Verify: golden_output passes ALL HARD gates of target_kind's builder
5. If score < 8.0: revise before outputting
