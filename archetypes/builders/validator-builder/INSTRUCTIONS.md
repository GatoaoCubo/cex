---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for validator
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a validator

## Phase 1: DISCOVER
1. Identify the target: what artifact kind needs this validation rule?
2. Check brain_query for existing validators on this domain (avoid duplicates)
3. Determine scope: pre-commit, post-generation, or on-demand?
4. List the specific fields/properties that need checking
5. Classify severity: does failure block (error), warn (warning), or inform (info)?
6. Determine if auto-fix is feasible (formatting, casing = yes; logic = no)

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Fill frontmatter: all 22 fields (null OK for optional)
4. Set quality: null (NEVER self-score)
5. Write Rule Definition section: plain-language description of what is checked
6. Write Conditions section: structured table with field/operator/value triples
7. Write Error Handling section: actionable error_message + remediation steps
8. Write Bypass Policy section: conditions, approver, audit requirement

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually (no automated validator yet)
2. HARD gates (all must pass): YAML parses, id matches p06_val_ pattern, kind == validator, severity in enum, conditions non-empty, quality == null
3. SOFT gates: check each against QUALITY_GATES.md
4. Cross-check: still binary pass/fail? Not drifting into scoring (quality_gate)? Not drifting into schema definition (input_schema)?
5. If score < 8.0: revise in same pass before outputting
