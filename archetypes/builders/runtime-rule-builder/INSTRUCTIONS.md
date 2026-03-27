---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for runtime_rule
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a runtime_rule

## Phase 1: RESEARCH
1. Identify the operation or component that needs runtime rules
2. Classify the rule type: timeout, retry, rate_limit, circuit_breaker, or concurrency
3. Determine scope: which component, endpoint, or operation
4. Research appropriate numeric values for the domain
5. Define fallback behavior when the rule triggers
6. Assess severity: what happens if this rule is misconfigured
7. Check for existing runtime_rule artifacts via brain_query [IF MCP] (avoid duplicates)
8. Confirm rule slug for id: snake_case, lowercase, no hyphens

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill {{vars}} following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Set rule_type to concrete value from enum
5. Set scope to specific component or operation
6. Write ## Rule Specification: parameter table with values and units
7. Write ## Trigger Behavior: what happens when rule activates
8. Write ## Tuning Guide: how to adjust, safe ranges, metrics
9. Verify all numeric values have units (ms, s, req/s, etc.)
10. Verify body <= 3072 bytes
11. Verify id matches `^p09_rr_[a-z][a-z0-9_]+$`

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm rule_type is valid enum value
4. Confirm all numeric values include units
5. Confirm quality == null
6. Confirm body has all 3 required sections
7. Confirm no vague terms (no "fast", "many", "some")
8. Confirm body <= 3072 bytes
9. Score SOFT gates against QUALITY_GATES.md
10. Revise if score < 8.0 before outputting
