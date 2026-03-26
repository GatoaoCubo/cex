---
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for few-shot example construction
---

# Knowledge: few-shot-example-builder

## Foundational Theory
Brown et al. 2020 "Language Models are Few-Shot Learners" (GPT-3 paper):
- 1-3 examples in context dramatically improve task performance
- Example quality > example quantity
- Format demonstration is the core mechanism — LLM pattern-matches structure

## Industry Patterns
- OpenAI few-shot guides: representative input covers the typical case; edge_case input covers the boundary
- Anthropic prompt engineering: show don't tell — concrete examples outperform instructions alone
- LangChain ExampleSelector: diversity sampling (MMR) + semantic similarity for dynamic selection

## CEX Extensions
- quality field: always null — scored externally by evaluator, never by builder
- domain binding: tie example to a specific artifact kind (knowledge_card, validator, etc.)
- difficulty enum: easy (canonical), medium (realistic variation), hard (edge case / ambiguous)

## Key Construction Patterns
1. Representative: input covers the typical use case for the domain
2. Edge case: input tests boundary conditions (empty values, max length, unusual chars)
3. Difficulty graduation: easy -> medium -> hard progression teaches the LLM range
4. Format-first: output demonstrates the target format structure, not just correct content

## Boundary Knowledge
| Kind | Function | Has scoring? | Has assertions? | Has input/output? |
|------|----------|-------------|-----------------|-------------------|
| few_shot_example | Format teaching | NO | NO | YES |
| golden_test (P07) | Quality evaluation | YES (rubric) | NO | YES |
| unit_eval (P07) | Assertion testing | NO | YES | YES |
| prompt_template (P03) | Reusable prompt | NO | NO | partial |

## Common Pitfalls
- Output too abstract: "good response" instead of concrete formatted output
- Input too vague: "write something" — no task context for LLM to learn from
- quality self-scored: breaks evaluation pipeline
- Scoring rubric included: golden_test drift — remove immediately
- Over 1024 bytes: fails H-gate, trim body sections
