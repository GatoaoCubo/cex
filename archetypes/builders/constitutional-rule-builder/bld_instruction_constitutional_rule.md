---
id: bld_instruction_constitutional_rule
kind: instruction
pillar: P11
title: "Constitutional Rule Builder -- Instruction"
version: 1.0.0
quality: null
tags: [builder, constitutional_rule, instruction]
llm_function: REASON
---
# Instructions: How to Produce a constitutional_rule
## Phase 1: RESEARCH
1. Identify the absolute prohibition: what behavior must NEVER occur under ANY circumstances?
2. Classify the constitutional basis: harm_prevention, honesty, autonomy_preservation, legality
3. Verify it is truly absolute: is there ANY legitimate scenario where this should be bypassed? If yes -> it is a guardrail, not a constitutional rule.
4. Define the violation test: how would a reviewer recognize that this rule was broken?
5. Write the rationale: why can this never have an exception?
6. Check existing constitutional_rules for overlap -- each rule should cover a distinct prohibition.
## Phase 2: COMPOSE
1. Read bld_schema_constitutional_rule.md -- source of truth for required fields
2. Fill frontmatter: id pattern p11_cr_{slug}, kind: constitutional_rule, quality: null
3. Write Principle section: one clear, concrete statement of the absolute prohibition
4. Write Basis section: which constitutional value this protects (harm/honesty/autonomy/legality)
5. Write Rationale section: why this has zero exceptions
6. Write Violation section: concrete examples of what breaking this rule looks like
7. Write Detection section: how a violation is identified
8. CONFIRM: bypass_policy must be "none" -- if you find yourself writing any bypass, downgrade to guardrail
## Phase 3: VALIDATE
1. HARD gates: id matches `p11_cr_[a-z][a-z0-9_]+`, kind == constitutional_rule, quality == null
2. bypass_policy == "none" (absolute)
3. Principle is a single clear prohibition, not a collection
4. At least 2 concrete violation examples
5. constitutional_basis is one of the valid enum values
