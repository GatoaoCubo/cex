---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for scoring_rubric
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a scoring_rubric

## Phase 1: RESEARCH
1. Identify the target_kinds: which artifact types this rubric evaluates
2. Find existing rubrics for the same domain (search P07_evals/examples/)
3. Identify quality dimensions from the target_kind's schema and gates
4. Research industry evaluation frameworks for the domain
5. Locate golden_tests that can serve as calibration anchors
6. Check brain_query [IF MCP] for duplicate rubrics
7. Determine automation feasibility per dimension

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill following SCHEMA constraints
3. Fill frontmatter: all 19 required + 4 recommended fields (quality: null)
4. Set framework name (descriptive, unique)
5. Write Framework Overview section: what it measures and why
6. Write Dimensions table: name, weight (summing to 100%), scale, criteria
7. Write Thresholds section: GOLDEN/PUBLISH/REVIEW/REJECT with actions
8. Write Calibration section: examples at each tier with rationale
9. Write Automation section: status per dimension (manual/semi/automated)

## Phase 3: VALIDATE
1. Check against QUALITY_GATES.md (this builder's own gates)
2. HARD: id format, kind, pillar, quality==null, weights sum to 100%
3. HARD: all 4 tiers defined, dimensions >= 3
4. SOFT: criteria are concrete (no vague language), calibration present
5. Verify: no dimension overlap (each measures ONE thing)
6. Verify: scales are consistent across dimensions
7. If score < 8.0: revise before outputting
