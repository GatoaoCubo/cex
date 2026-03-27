---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for axiom
pattern: 3-phase pipeline (classify -> compose -> validate)
---

# Instructions: How to Produce an axiom

## Phase 1: CLASSIFY
1. Identify the candidate rule: write out the proposed truth in plain language
2. Test immutability: ask "can this rule change under any circumstance without breaking the system?" — if yes, it is not an axiom
3. Test universality: confirm the rule applies across all contexts in its scope, not just specific cases
4. Distinguish type: is this a law (enforced policy), a guardrail (safety boundary), a lifecycle rule (process step), or a fundamental truth? Only fundamental truths qualify as axioms
5. Check for existing axioms that already express the same truth (avoid duplicates)
6. Formulate as a single declarative statement: no conditionals, no conjunctions, one complete thought

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — template to fill
3. Fill frontmatter: all 20 required fields (quality: null, never self-score)
4. Set quality: null
5. Write Statement section: one declarative sentence expressing the immutable truth
6. Write Rationale section: evidence or first-principles reasoning for why this truth is permanent
7. Write Enforcement section: how violations are detected and what response is triggered
8. Write Scope section: declare whether this axiom is universal or bounded, and if bounded, define the boundary
9. Keep total body size <= 3072 bytes
10. Verify information density >= 0.80 (no filler sentences)

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually
2. HARD gate: id matches `p10_ax_` pattern
3. HARD gate: kind == axiom
4. HARD gate: quality == null
5. HARD gate: Statement is a single declarative sentence
6. HARD gate: Statement contains no conditionals ("if", "when", "unless")
7. HARD gate: required fields all present
8. Cross-check: is this truly immutable, or does it drift into law/guardrail territory?
9. Cross-check: does any existing axiom already cover this truth?
10. If score < 8.0: revise before outputting
