---
pillar: P10
llm_function: INJECT
purpose: Persistent patterns and anti-patterns for few-shot-example-builder
---

# Memory: few-shot-example-builder

## Common Mistakes (ranked by frequency)

| Mistake | Gate | Fix |
|---------|------|-----|
| quality not null (self-scored) | H05 | Set quality: null always |
| Missing output field | H07 | output is required — show the format |
| Scoring rubric included | S07 | Remove rubric — that is golden_test (P07) |
| Wrong id prefix (kc_ instead of p01_fse_) | H02 | Prefix MUST be p01_fse_ |
| Body exceeds 1024 bytes | S06 | Trim Variations/Edge Cases sections |
| Input too vague ("write something") | S04 | Make input a specific, realistic task |
| Output is description not demonstration | S05 | Show format, not "a good response would have..." |
| id != filename stem | H03 | Always check: id value == file name without extension |
| Tags as string not list | S02 | tags: [few-shot, domain, format] — list syntax |
| Missing Explanation section | S03 | Always explain WHY this pair teaches the format |

## Difficulty Calibration Table

| Difficulty | Input characteristic | Output characteristic | Typical count per domain |
|------------|---------------------|----------------------|--------------------------|
| easy | Simple canonical request, single domain | Complete format, no ambiguity | 1 (start here) |
| medium | Realistic variation, different domain | Format with domain-specific choices | 1-2 |
| hard | Edge case, ambiguous, boundary condition | Format handling the tricky case | 1 (per edge case) |

## Domain Patterns
- knowledge_card: always include quality: null in output; tldr <= 160ch
- validator: conditions must be list of objects, not string
- rag_source: chunk_size and overlap are numeric, not string
- few_shot_example: recursive — this builder produces its own kind

## Boundary Reinforcement
Encountered golden_test drift 3 times during early builds.
Trigger: user asks "show a good example with quality score".
Response: "quality scoring is golden_test (P07). I produce input/output pairs for format teaching only."

## Session Counter
Artifacts produced: 0
Last updated: 2026-03-26
