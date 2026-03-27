---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for feature_flag
pattern: 3-phase pipeline (classify -> compose -> validate)
---

# Instructions: How to Produce a feature_flag

## Phase 1: CLASSIFY
1. Identify the feature to be flagged
2. Classify the flag category: release, experiment, ops, or permission
3. Determine default state (on or off)
4. Define rollout percentage target (0-100)
5. Identify targeting strategy (all users, cohort, percentage)
6. Set expiration date for stale flag cleanup
7. Check for existing feature_flag artifacts via brain_query [IF MCP] (avoid duplicates)
8. Confirm feature slug for id: snake_case, lowercase, no hyphens

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill {{vars}} following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Set default_state to concrete value (on or off)
5. Set rollout_percentage to integer 0-100
6. Write ## Flag Specification: feature description, current state, kill switch info
7. Write ## Rollout Strategy: stages with percentages and timeline
8. Write ## Lifecycle: create, test, ramp, full, retire stages
9. Verify body <= 1536 bytes
10. Verify id matches `^p09_ff_[a-z][a-z0-9_]+$`

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm default_state is "on" or "off" (not other values)
4. Confirm rollout_percentage is integer 0-100
5. Confirm quality == null
6. Confirm body has all 3 required sections
7. Confirm body <= 1536 bytes
8. Score SOFT gates against QUALITY_GATES.md
9. Revise if score < 8.0 before outputting
