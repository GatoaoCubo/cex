---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for mental_model (P02)
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a mental_model

## Phase 1: ANALYZE
1. Identify the target agent by name and domain
2. Determine the agent's primary routing patterns (what triggers what)
3. List the key decisions the agent makes during operation
4. Identify priority ordering (what takes precedence)
5. Collect heuristics from agent's operational history
6. Map domain boundaries (what agent covers vs delegates)
7. Search for existing mental_models via brain_query [IF MCP] (avoid duplicates)
8. Confirm this is P02 (design-time), not P10 (runtime state)

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Generate agent_slug in snake_case from agent name
4. Fill frontmatter: all 14 required fields (quality: null)
5. Build routing_rules: >= 3 rules with keywords, action, confidence
6. Build decision_tree: >= 2 conditions with if/then/else
7. Set priorities list ordered highest-first
8. Write heuristics as actionable rules of thumb
9. Build domain_map with covers and routes_to
10. Set personality (tone, verbosity, risk_tolerance)
11. List constraints as hard behavioral limits
12. Define fallback with action and escalate_to
13. Write Agent Reference section: one-line identity
14. Write Routing Rules table in body
15. Write Decision Tree as numbered if/then list
16. Write Priorities, Heuristics, Domain Map sections
17. Check body <= 2048 bytes

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually
2. Verify all 9 HARD gates pass
3. Confirm id matches p02_mm_ pattern
4. Confirm kind == mental_model
5. Confirm pillar == P02 (NOT P10)
6. Confirm quality == null
7. Confirm routing_rules has >= 3 rules with keywords + action
8. Confirm decision_tree has >= 2 conditions with condition + then
9. Verify keywords are specific (not "general" or "anything")
10. Score each SOFT gate
11. If score < 8.0: revise before outputting
