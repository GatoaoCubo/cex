---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for pattern
pattern: 3-phase pipeline (discover -> compose -> validate)
---

# Instructions: How to Produce a pattern

## Phase 1: DISCOVER
1. Identify the recurring problem to formalize as pattern
2. Verify recurrence: confirm this happens repeatedly (not a one-off fix)
3. Identify forces: list competing tensions that make the problem hard
4. Identify at least 2 concrete examples where this solution was applied
5. Check brain_query [IF MCP] for existing patterns (avoid duplicates)
6. Determine related patterns: complementary, alternative, or prerequisite
7. Identify anti-patterns: common wrong approaches to the same problem

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Fill frontmatter: all 14 required + 7 extended fields (null OK for optional)
4. Set quality: null (NEVER self-score)
5. Write Problem: the recurring situation in concrete terms
6. Write Context: environment, frequency, severity
7. Write Forces: competing tensions (at least 2)
8. Write Solution: concrete reusable approach with optional diagram
9. Write Consequences: benefits AND costs (never benefits-only)
10. Write Examples: 2+ concrete applications
11. Write Anti-Patterns: wrong approaches with explanation
12. Write Related Patterns: navigation to complementary solutions

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually (no automated validator yet)
2. HARD gates (all must pass): YAML parses, id pattern, kind literal, quality null, required fields, name present, problem describes recurrence
3. SOFT gates: check each against QUALITY_GATES.md
4. Cross-check: is it truly a pattern (recurring)? Not drifting into law or workflow?
5. If score < 8.0: revise in same pass before outputting
