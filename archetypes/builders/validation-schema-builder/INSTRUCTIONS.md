---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for validation_schema
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a validation_schema

## Phase 1: DISCOVER
1. Identify the target_kind: which artifact type needs post-generation validation?
2. Read the target kind's _schema.yaml for field definitions
3. Check brain_query [IF MCP] for existing validation_schemas (avoid duplicates)
4. Determine which fields are critical (must be validated vs nice-to-have)
5. Determine on_failure strategy: reject (strict), warn (lenient), auto_fix (resilient)
6. Identify constraint types needed: type check, regex, enum, range, required

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill following SCHEMA constraints
3. Fill frontmatter: all 17 required fields (quality: null)
4. Define fields list with name, type, required, constraints per field
5. Write Schema Overview section: what is validated and why
6. Write Fields section: table with all field definitions
7. Write Failure Handling section: on_failure behavior, error messages
8. Write Integration section: where in the pipeline this schema is applied

## Phase 3: VALIDATE
1. Check against QUALITY_GATES.md (this builder's own gates)
2. HARD: id format, kind, pillar, quality==null, fields_count >= 1
3. HARD: on_failure in enum, format in enum, target_kind non-empty
4. SOFT: constraints are specific (not vague), field types are JSON-compatible
5. Verify: still a SYSTEM-SIDE contract? Not drifting into prompt instructions (response_format)?
6. Verify: still a structural schema? Not an individual rule (validator)?
7. If score < 8.0: revise before outputting
