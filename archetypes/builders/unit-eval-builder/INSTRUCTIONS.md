---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for unit_eval
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a unit_eval

## Phase 1: RESEARCH
1. Identify the target agent or prompt to test
2. Find existing unit_evals for the same target (search P07_evals/)
3. Locate the target's expected behavior specification
4. Identify edge cases that need separate test coverage
5. Check brain_query [IF MCP] for duplicate unit_evals

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill following SCHEMA constraints
3. Fill frontmatter: all required + recommended fields (quality: null)
4. Write Input section: the exact input/prompt to feed the target
5. Write Expected Output section: the correct output for this input
6. Write Assertions section: each assertion maps to a gate_ref
7. Write Setup section: preconditions and state initialization
8. Write Teardown section: cleanup after test execution
9. Set timeout appropriate to unit scope (default 60s)

## Phase 3: VALIDATE
1. Check against QUALITY_GATES.md (this builder's own gates)
2. HARD: id format, kind, pillar, quality==null, assertions non-empty
3. SOFT: coverage scope defined, edge_case flagged, setup/teardown present
4. Verify: each assertion has a concrete expected value (no vague checks)
5. If score < 8.0: revise before outputting
