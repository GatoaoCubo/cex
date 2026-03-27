---
pillar: P01
llm_function: INJECT
purpose: Distilled patterns for constructing few-shot examples that reliably teach LLMs format and quality
sources: [Brown et al. 2020, Anthropic prompt engineering, real golden/anti examples from production]
---

# Domain Knowledge: few_shot_example

## Why Few-Shot Examples Work

Brown et al. 2020 demonstrated that 1-3 in-context examples dramatically improve task performance. The mechanism is pattern-matching: the LLM reads the example's structure and replicates it. This makes example quality the single highest-leverage factor in output quality. A mediocre prompt with a golden example outperforms an excellent prompt with no example.

## Anatomy of a Golden Example

A golden example has three layers:

### Layer 1: Complete Frontmatter
Every field from the schema appears with a realistic, non-placeholder value. The frontmatter IS the format specification — if a field is missing, the LLM learns to omit it.

```yaml
---
id: p03_sp_knowledge_card_builder    # correct prefix pattern
kind: system_prompt                   # exact literal
quality: null                         # never self-score
tags: [system_prompt, knowledge, distillation, P01]  # >= 3, includes kind
tldr: "System prompt defining knowledge-card-builder identity, 8 ALWAYS/NEVER rules, YAML output format"
# ... all remaining required fields present
---
```

### Layer 2: Dense Body
The body demonstrates the target structure with concrete, domain-specific content. No filler phrases ("this document describes", "in summary"). Every sentence carries information. Every section matches a required section from the schema.

### Layer 3: Explanation Block
After the example output, a "WHY THIS IS GOLDEN" block maps every quality gate to the example:

```
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p03_sp_ pattern (H02 pass)
- 19 required fields present (H06 pass)
- Rules use ALWAYS/NEVER pattern (S04 pass)
- tldr: 89 chars <= 160 (S01 pass)
- No filler phrases (S12 pass)
```

This is the bridge between example and schema. It teaches the LLM not just WHAT to produce but WHY each element matters. Every gate code (H01-H08, S01-S12) should appear at least once across the golden explanation.

## Anatomy of an Anti-Example

An anti-example is equally structured but demonstrates failure:

### Minimal/Wrong Frontmatter
Deliberately violates the schema — wrong prefix, missing fields, self-assigned quality score, wrong kind literal.

### Generic Body
Uses filler language ("You are a helpful assistant"), lacks required sections, contains no domain-specific content.

### Failure Catalog
After the bad output, a "FAILURES" block lists every violated gate:

```
FAILURES:
1. id: no `p03_sp_` prefix -> H02 FAIL
2. kind: "prompt" not "system_prompt" -> H04 FAIL
3. quality: 8.5 (not null) -> H05 FAIL
4. tldr: 103 chars but is filler -> S12 FAIL
```

Number each failure. Reference the specific gate code. State what's wrong AND what the correct value would be. This teaches the LLM to self-check against gates.

## How Many Examples?

The proven pattern from production is **1 golden + 1 anti per builder**. This is sufficient because:

- 1 golden teaches the complete format (all fields, all sections, correct values)
- 1 anti teaches the failure modes (what breaks, which gates catch it)
- More examples add diminishing returns but consume context tokens
- Difficulty variation (easy golden vs hard edge case) is handled by the Variations section, not by adding full examples

If the artifact kind has genuinely distinct modes (e.g., different output formats), add 1 golden per mode. Never exceed 3 golden + 3 anti — context budget is finite.

## The Bridge Pattern: Example Demonstrates Schema

Every field in the schema should appear in the golden example. Every gate in the quality gates should be referenced in either the golden explanation or the anti-example failures. This creates a three-way alignment:

```
SCHEMA defines fields → EXAMPLE demonstrates them → GATES validate them
```

If a schema field has no representation in the example, the LLM may ignore it. If a gate has no reference in the example explanations, the builder can't learn to avoid that failure mode.

### Verification Checklist
1. List all required fields from SCHEMA.md
2. Confirm each appears in golden example frontmatter
3. List all HARD gates from QUALITY_GATES.md
4. Confirm each is referenced in golden (pass) or anti (fail) explanation
5. List all SOFT gates
6. Confirm >= 80% are referenced across both examples

## Density in Examples

Examples must be denser than typical content because they serve as format templates. Specific density rules:

| Element | Good | Bad |
|---------|------|-----|
| tldr | "8 ALWAYS/NEVER rules for KB identity, YAML output" | "This is a system prompt for a helpful assistant" |
| Rules | "ALWAYS read SCHEMA.md first" | "Be helpful" |
| Identity | "specialist in knowledge distillation: atomic facts, density scoring" | "a helpful assistant that helps users" |
| Sections | 4+ body sections with 3+ lines each | 1 paragraph with generic advice |

The test: if you can replace a sentence with "blah blah blah" and the example still seems complete, that sentence is filler. Remove it.

## Input Design

The INPUT prompt in an example should be realistic and specific:

- Golden input: names a concrete artifact and domain ("Create system prompt for the knowledge-card-builder agent")
- Anti input: is vague or generic ("Create system prompt for a helper agent")

This contrast teaches the LLM that specific inputs produce specific outputs — and that vague inputs are a warning sign.

## Edge Cases Section

The body's `## Edge Cases` section covers boundary inputs with expected outputs:

- Empty/null input fields
- Maximum-length values
- Special characters in strings
- Conflicting constraints (e.g., required field with null default)

Each edge case is a mini-example: input + expected output + why this is the correct handling.

## Boundary Knowledge

| Kind | Function | Has scoring? | Has input/output pair? |
|------|----------|-------------|----------------------|
| few_shot_example | Format teaching via demonstration | NO | YES (core purpose) |
| golden_test | Quality evaluation with rubric | YES | YES |
| unit_eval | Assertion-based testing | NO (assertions) | YES |
| scoring_rubric | Defines evaluation dimensions | YES (defines them) | NO |

If your artifact has a scoring rubric, it is NOT a few_shot_example — redirect to golden_test builder. If it has assertions, redirect to unit_eval builder.

## Anti-Patterns

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| Abstract output ("good response") | LLM can't pattern-match structure | Concrete formatted output with real values |
| Vague input ("write something") | No task context for learning | Specific domain task with named artifacts |
| Self-scored quality | Breaks evaluation pipeline | quality: null always |
| Scoring rubric in example | golden_test drift | Remove rubric, redirect to correct builder |
| Body > 1024 bytes | Fails size HARD gate | Trim sections, compress bullets |
| Missing gate references | Builder can't learn what to avoid | Map all gates in WHY/FAILURES blocks |
| Too many examples (>3 golden) | Context bloat, diminishing returns | 1 golden + 1 anti is sufficient |

## References

- Brown, T. et al. (2020). Language Models are Few-Shot Learners. NeurIPS.
- Anthropic Prompt Engineering: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering
- LangChain ExampleSelector: https://python.langchain.com/docs/how_to/#example-selectors
