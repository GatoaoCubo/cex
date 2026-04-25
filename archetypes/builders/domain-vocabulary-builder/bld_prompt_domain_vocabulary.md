---
quality: 7.8
id: bld_instruction_domain_vocabulary
kind: instruction
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for domain_vocabulary
version: 1.0.0
quality: 7.3
tags: [domain_vocabulary, builder, instruction]
title: "Instruction Domain Vocabulary Builder"
author: builder
tldr: "Step-by-step production process for domain_vocabulary"
density_score: 0.82
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_instruction_glossary_entry
  - p03_sp_glossary_entry_builder
  - bld_collaboration_glossary_entry
  - p01_kc_glossary_entry
  - bld_instruction_input_schema
  - p01_gl_TERM_SLUG
  - bld_instruction_instruction
  - bld_instruction_kind
  - bld_instruction_golden_test
  - bld_examples_glossary_entry
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


## Prompt Construction Checklist

- Verify prompt follows target kind's instruction template
- Validate variable placeholders use standard naming convention
- Cross-reference with chain dependencies for context completeness
- Test prompt with sample input before publishing

## Prompt Pattern

```yaml
# Prompt validation
template_match: true
variables_valid: true
chain_refs_checked: true
sample_tested: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_prompt_optimizer.py --check
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_glossary_entry]] | sibling | 0.34 |
| [[p03_sp_glossary_entry_builder]] | related | 0.30 |
| [[bld_collaboration_glossary_entry]] | downstream | 0.26 |
| [[p01_kc_glossary_entry]] | upstream | 0.25 |
| [[bld_instruction_input_schema]] | sibling | 0.22 |
| [[p01_gl_TERM_SLUG]] | upstream | 0.22 |
| [[bld_instruction_instruction]] | sibling | 0.22 |
| [[bld_instruction_kind]] | sibling | 0.22 |
| [[bld_instruction_golden_test]] | sibling | 0.21 |
| [[bld_examples_glossary_entry]] | downstream | 0.21 |
