---
pillar: P01
llm_function: INJECT
purpose: Distilled patterns for constructing few-shot examples that reliably teach LLMs format and quality
sources: [Brown et al. 2020, Anthropic prompt engineering, real golden/anti examples from production]
---

# Domain Knowledge: few_shot_example

## Core Insight

1-3 in-context examples dramatically improve task performance (Brown et al. 2020). LLM pattern-matches example structure. A mediocre prompt + golden example outperforms excellent prompt + no example.

## Golden Example: 3 Layers

| Layer | Content | Key Rule |
|-------|---------|----------|
| Frontmatter | Every schema field with realistic value | Missing field = LLM learns to omit it |
| Dense Body | Concrete domain content, no filler | Every sentence carries information |
| WHY GOLDEN | Maps each quality gate to example | Bridge between example and schema |

WHY block format: `- quality: null (H05 pass)` — gate code + pass/fail for every gate.

## Anti-Example: 3 Layers

| Layer | Content | Key Rule |
|-------|---------|----------|
| Wrong Frontmatter | Deliberately violates schema | Wrong prefix, missing fields, self-scored quality |
| Generic Body | Filler language, no domain content | "You are a helpful assistant" |
| FAILURES | Numbered list of violated gates | `1. id: no p03_sp_ prefix -> H02 FAIL` |

## Quantity Rule

**1 golden + 1 anti per builder** is sufficient and proven.
- Golden teaches complete format; anti teaches failure modes
- If distinct output modes exist: 1 golden per mode
- Never exceed 3 golden + 3 anti (context budget)

## Bridge Pattern

```
SCHEMA defines fields -> EXAMPLE demonstrates them -> GATES validate them
```

- Every schema field must appear in golden example
- Every HARD gate referenced in golden (pass) or anti (fail)
- >= 80% of SOFT gates referenced across both examples

## Density Rules

| Element | Good | Bad |
|---------|------|-----|
| tldr | "8 ALWAYS/NEVER rules, YAML output" | "A system prompt for a helper" |
| Rules | "ALWAYS read SCHEMA.md first" | "Be helpful" |
| Identity | "specialist in knowledge distillation" | "a helpful assistant" |
| Sections | 4+ sections, 3+ lines each | 1 generic paragraph |

Test: if replacing a sentence with "blah blah" and example seems complete, it's filler.

## Input Design

- Golden: specific, names concrete artifact ("Create system prompt for knowledge-card-builder")
- Anti: vague, generic ("Create system prompt for a helper agent")

## Edge Cases Section

Cover boundary inputs with expected outputs:
- Empty/null fields, max-length values, special characters, conflicting constraints
- Each: input + expected output + why correct

## Boundary Knowledge

| Kind | Function | Scoring? | I/O pair? |
|------|----------|----------|-----------|
| few_shot_example | Format teaching | NO | YES (core) |
| golden_test | Quality eval with rubric | YES | YES |
| unit_eval | Assertion-based testing | NO | YES |
| scoring_rubric | Defines eval dimensions | YES | NO |

Has rubric? -> golden_test. Has assertions? -> unit_eval.

## Anti-Patterns

| Anti-Pattern | Fix |
|-------------|-----|
| Abstract output ("good response") | Concrete formatted output with real values |
| Vague input ("write something") | Specific domain task with named artifacts |
| Self-scored quality | `quality: null` always |
| Body > 1024 bytes | Trim, compress bullets |
| Missing gate references | Map all gates in WHY/FAILURES |
| >3 golden examples | 1 golden + 1 anti is sufficient |
