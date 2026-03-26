---
lp: P03
llm_function: REASON
purpose: Step-by-step production process for quality_gate
pattern: 3-phase pipeline (research → compose → validate)
---

# Instructions: How to Produce a quality_gate

## Phase 1: RESEARCH
1. Identify the domain: what type of artifact does this gate protect?
2. Find existing gates for similar domains (search P11_feedback/examples/)
3. Determine HARD gates: what failures are UNACCEPTABLE? (block publish)
4. Determine SOFT gates: what qualities VARY? (contribute to score)
5. Research industry thresholds for the domain

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill following SCHEMA constraints
3. Fill frontmatter: id, type, lp, title, version, quality: null
4. Write Definition table: metric, threshold, operator, scope
5. Write Checklist: concrete checks (HARD gates)
6. Write Scoring table: dimensions with weights summing to 100%
7. Write Actions table: pass/fail consequences
8. Write Bypass policy: conditions, approver, audit

## Phase 3: VALIDATE
1. Check against QUALITY_GATES.md (this builder's own gates)
2. HARD: id format, type, lp, quality==null, threshold is numeric
3. SOFT: weights sum to 100%, bypass defined, actions concrete
4. Verify: every check is automatable (no subjective judgment)
5. If score < 8.0: revise before outputting
