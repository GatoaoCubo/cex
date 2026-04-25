---
id: p01_kc_cex_function_constrain
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Function CONSTRAIN — Formatting and Restricting Output to Standards"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, llm-function, constrain, grammar, schema, template, formatting]
tldr: "CONSTRAIN restricts output via 11 types in 3 levels (hard/medium/soft) — delivers to required standard"
when_to_use: "Understand how LLMs format output and the boundary between CONSTRAIN (format) and GOVERN (quality)"
keywords: [constrain, grammar, schema, template, response_format, validation, formatting]
long_tails:
  - "What is the difference between CONSTRAIN and GOVERN in CEX"
  - "What are the 11 constraint types in the CEX taxonomy"
axioms:
  - "ALWAYS prefer grammar (hard) over response_format (soft) when conformance is critical"
  - "NEVER confuse CONSTRAIN (output format) with GOVERN (output quality)"
linked_artifacts:
  primary: p01_kc_cex_function_produce
  related: [p01_kc_cex_function_govern, p01_kc_cex_function_call]
density_score: null
data_source: "https://github.com/guidance-ai/guidance"
related:
  - p06_gram_json_object
  - p01_kc_cex_lp06_schema
  - bld_architecture_response_format
  - p01_kc_validation_schema
  - p01_kc_cex_lp05_output
  - bld_knowledge_card_constraint_spec
  - response-format-builder
  - p03_ins_response_format
  - p01_kc_response_format
  - bld_knowledge_card_response_format
---

## Summary

CONSTRAIN formats, structures, and restricts output to conform with schemas, templates, and formal grammars. With 11 types (14% of CEX), it operates at 3 rigidity levels: HARD (grammar — impossible to violate at decoder), MEDIUM (law, axiom, guardrail — inviolable rules), SOFT (response_format, template — instructions the LLM may fail to follow). Critical insight: response_format (LLM sees in prompt) vs grammar (LLM does not see, decoder applies). Same function, radically different guarantees. Frameworks like Guidance (Microsoft) and Outlines (dottxt) confirm that CONSTRAIN intervenes in the generation process, not just post-processes.

## Spec

| Type | LP | Rigidity | Function | Detail |
|------|-----|----------|----------|--------|
| grammar | P06 | Hard | Formal grammar | BNF/EBNF/FSM at decoder |
| law | P08 | Medium | Inviolable rule | Constitutional principle |
| axiom | P10 | Medium | Assumed truth | Domain constraint |
| guardrail | P11 | Medium | Safety barrier | Prevents inadequate output |
| response_format | P05 | Soft | Expected format | JSON, Markdown, XML |
| prompt_template | P03 | Soft | Parameterized template | Prompt reuse |
| input_schema | P06 | Soft | Input validation | Boundary between systems |
| output_schema | P06 | Soft | Output validation | Downstream format |
| validation_schema | P06 | Soft | Intermediate validation | Multi-step pipeline |
| template | P05 | Soft | Output template | Emails, reports |
| style_guide | P05 | Soft | Writing conventions | Tone, terminology |

HARD: grammar operates DURING generation (token-level). Impossible to violate.
SOFT: response_format operates via prompt. LLM may ignore.
MEDIUM: rules applied by external system. Hard to violate but not
impossible. Guidance (MS) and Outlines (dottxt) use FSMs and CFGs for
constrained generation — altering the space of possible tokens.
LMQL (ETH Zurich) offers SQL-like WHERE clauses for constraint.

## Patterns

| Trigger | Action |
|---------|--------|
| Mathematically guaranteed conformance | grammar (BNF/EBNF at decoder) |
| JSON output for downstream API | output_schema + response_format |
| Same prompt for varied inputs | parameterized prompt_template |
| Consistency across multiple outputs | shared style_guide |
| Multi-step pipeline with validation | validation_schema per stage |
| Output for standardized human consumption | template (email, report) |
| Boundary between systems | input_schema at entry |

## Code

<!-- lang: python | purpose: constrained generation patterns -->
```python
# grammar (HARD): decoder-level constraint via Outlines
import outlines
generator = outlines.generate.json(model, ProductSchema)
result = generator("Extract product data")  # IMPOSSIVEL violar schema

# response_format (SOFT): prompt-level instruction
response = llm.complete(
    prompt=f"Return JSON:\n{input_text}",
    response_format={"type": "json_object"}  # LLM PODE ignorar
)

# prompt_template (SOFT): parametrized reuse
template = "Analyze {product} for {market}. Output: {format}"
prompt = template.format(product="LED", market="BR", format="table")
```

## Anti-Patterns

- response_format for critical data (LLM may ignore, use grammar)
- grammar for free/creative output (over-constrains generation)
- Confusing schema (validation) with format (expectation)
- Rigid template for output that needs adaptation
- style_guide without concrete examples (interpretive ambiguity)
- Validation only on final output (error cascades through pipeline)

## References

- source: https://github.com/guidance-ai/guidance
- source: https://github.com/dottxt-ai/outlines
- related: p01_kc_cex_function_produce
- related: p01_kc_cex_function_govern

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p06_gram_json_object]] | downstream | 0.37 |
| [[p01_kc_cex_lp06_schema]] | sibling | 0.36 |
| [[bld_architecture_response_format]] | downstream | 0.30 |
| [[p01_kc_validation_schema]] | sibling | 0.29 |
| [[p01_kc_cex_lp05_output]] | sibling | 0.29 |
| [[bld_knowledge_card_constraint_spec]] | sibling | 0.28 |
| [[response-format-builder]] | downstream | 0.27 |
| [[p03_ins_response_format]] | downstream | 0.25 |
| [[p01_kc_response_format]] | sibling | 0.24 |
| [[bld_knowledge_card_response_format]] | sibling | 0.24 |
