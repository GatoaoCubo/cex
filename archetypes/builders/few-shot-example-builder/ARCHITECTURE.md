---
pillar: P08
llm_function: CONSTRAIN
purpose: Architectural position and boundary of few_shot_example in CEX
---

# Architecture: few_shot_example

## What few_shot_example IS
An input/output pair that teaches an LLM a format by demonstration.
- Input: realistic task request
- Output: ideal response showing the target format
- Purpose: inject into prompt context so LLM pattern-matches the structure

## What few_shot_example is NOT

| Confused With | Difference | Correct Kind |
|---------------|-----------|--------------|
| golden_test (P07) | Has scoring rubric, evaluates quality | P07 golden_test |
| unit_eval (P07) | Has assertions (assert x == y) | P07 unit_eval |
| prompt_template (P03) | Reusable prompt with {{variables}} | P03 prompt_template |
| context_doc (P01) | Background knowledge, no input/output pair | P01 context_doc |

## Pipeline Position

```
Domain Knowledge (P01)
       |
       v
few_shot_example  <-- this artifact (format teaching)
       |
       v
Prompt Hydration (P03)
       |
       v
LLM Context Window
       |
       v
Better-Formatted Output
       |
       v
golden_test (P07)  <-- evaluates the output quality (separate step)
```

## Taxonomy Position
- Layer: content (taxonomy) / prompt (schema layer field) — both correct
- Pillar: P01 (knowledge pillar owns it)
- Core 24: YES — content tier: knowledge_card, rag_source, glossary_entry, context_doc, few_shot_example
- Fractal: L0 content, INJECT llm_function, machine_format yaml

## Dependency Graph
- few_shot_example DEPENDS ON: none (standalone artifact)
- few_shot_example IS USED BY: prompt_template (P03), system_prompt (P03), LLM context injection
- few_shot_example IS EVALUATED BY: golden_test (P07) — separate artifact, not embedded

## Constraints from Architecture
- max_bytes 1024: keeps context injection cost low
- quality: null: evaluated externally, not by producer
- input+output both required: incomplete pair has zero learning value
