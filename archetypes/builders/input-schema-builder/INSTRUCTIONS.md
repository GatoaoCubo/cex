---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for input_schema
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce an input_schema

## Phase 1: DISCOVER
1. Identify the target: what agent/operation needs this input contract?
2. Check brain_query for existing input_schemas on this scope (avoid duplicates)
3. List the fields needed: what data must the caller provide?
4. For each field, determine type, required/optional, and default
5. Identify coercion needs: will data arrive in mixed formats?
6. Draft error messages for required fields

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Fill frontmatter: all 20+ fields (null OK for optional)
4. Set quality: null (NEVER self-score)
5. Write Contract Definition section: what operation this input serves
6. Write Fields section: table of name/type/required/default/description
7. Write Coercion Rules section: type conversion rules
8. Write Examples section: at least one valid payload

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually (no automated validator yet)
2. HARD gates (all must pass): YAML parses, id matches p06_is_ pattern, kind == input_schema, fields list non-empty, quality == null
3. SOFT gates: check each against QUALITY_GATES.md
4. Cross-check: still unilateral? Not drifting into bilateral interface? Not drifting into abstract type_def?
5. If score < 8.0: revise in same pass before outputting
