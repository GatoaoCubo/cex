---
id: bld_instruction_domain_vocabulary
kind: instruction
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for domain_vocabulary
version: 1.0.0
quality: null
tags: [domain_vocabulary, builder, instruction]
title: "Instruction Domain Vocabulary Builder"
---
# Instructions: How to Produce a domain_vocabulary
## Phase 1: SCOPE
1. Identify the bounded context this vocabulary governs (e.g., sales, billing, identity)
2. List the agents/nuclei that share this context and need consistent terms
3. Collect candidate terms from existing artifacts (KCs, handoffs, events)
4. Prioritize: terms used in >= 2 artifacts or causing > 1 ambiguity incident
5. Check: does a domain_vocabulary already exist for this BC?
## Phase 2: COMPOSE
1. Read bld_schema_domain_vocabulary.md for required fields
2. Set id: dv_{bounded_context}_vocabulary (snake_case)
3. Set bounded_context field and governed_agents list
4. For each term: name, definition, industry_standard, anti_patterns, status
5. Status lifecycle: proposed -> active -> deprecated
6. Set quality: null -- never self-score
## Phase 3: VALIDATE
1. HARD gates:
   - id follows pattern dv_{context}_vocabulary
   - kind == domain_vocabulary
   - quality == null
   - bounded_context present
   - >= 3 canonical terms in terms section
   - each term has definition and status
2. SOFT gates:
   - each term maps to an industry standard (or "CEX-internal" if novel)
   - anti_patterns list per term (what NOT to say)
   - governed_agents list non-empty
   - deprecated terms have replacement noted
