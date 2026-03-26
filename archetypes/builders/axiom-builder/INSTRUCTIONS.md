---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for axiom
pattern: 3-phase pipeline (classify -> compose -> validate)
---

# Instructions: How to Produce an axiom

## Phase 1: CLASSIFY
1. Identify the candidate rule to formalize as axiom
2. Verify immutability: ask "can this rule EVER change without breaking the system?"
3. Verify atomicity: confirm the rule states ONE truth (no conjunctions)
4. Check brain_query [IF MCP] for existing axioms (avoid duplicates)
5. Determine scope: identify WHERE this axiom applies (domain, layer, system)

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Fill frontmatter: all 13 required + 7 extended fields (null OK for optional)
4. Set quality: null (NEVER self-score)
5. Write Rule Statement: one sentence expressing the immutable truth
6. Write Rationale: 2-3 concrete reasons WHY this truth is permanent
7. Write Scope: domain, system, layer where it applies
8. Write Enforcement: HOW violations are detected and responded to
9. Write Examples: 2+ cases where the axiom holds in practice
10. Write Violations: 1+ known or hypothetical breach with impact

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually (no automated validator yet)
2. HARD gates (all must pass): YAML parses, id pattern, kind literal, quality null, required fields, rule is atomic, scope defined
3. SOFT gates: check each against QUALITY_GATES.md
4. Cross-check: is it truly immutable? Not drifting into law or guardrail?
5. If score < 8.0: revise in same pass before outputting
