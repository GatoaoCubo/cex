---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for guardrail
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a guardrail

## Phase 1: RESEARCH
1. Identify the scope: what agent, pipeline, or output needs protection
2. Find existing guardrails for the same scope (search P11_feedback/examples/)
3. Determine severity: what is the worst case if this guardrail is violated
4. Research industry safety patterns for the domain
5. Check brain_query [IF MCP] for duplicate guardrails

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill following SCHEMA constraints
3. Fill frontmatter: all 17 required + 4 recommended fields (quality: null)
4. Set severity and enforcement mode based on risk assessment
5. Write Definition section: what it protects and why
6. Write Rules section: concrete, numbered, measurable restrictions
7. Write Violations section: specific examples of what breaks this guardrail
8. Write Enforcement section: how violations are detected and handled
9. Write Bypass section: conditions, approver, audit trail

## Phase 3: VALIDATE
1. Check against QUALITY_GATES.md (this builder's own gates)
2. HARD: id format, kind, pillar, quality==null, severity valid, enforcement valid
3. SOFT: rules are concrete, violations are specific, bypass defined
4. Verify: every rule is enforceable (no subjective judgment required)
5. If score < 8.0: revise before outputting
