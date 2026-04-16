---
kind: examples
id: bld_examples_judge_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of judge_config artifacts
quality: 8.8
title: "Examples Judge Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [judge_config, builder, examples]
tldr: "Golden and anti-examples of judge_config artifacts"
domain: "judge_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```markdown
---
kind: judge_config
name: llm_judge_automated_eval
---
model: "gpt-4o"
criteria:
  - relevance
  - coherence
  - factual_accuracy
scoring:
  threshold: 0.75
  scale: 1-5
api:
  endpoint: "https://api.openai.com/v1/engines/gpt-4o/completions"
  auth: "Bearer <API_KEY>"
  timeout: 30
```

## Anti-Example 1: Missing Essential Parameters
```markdown
---
kind: judge_config
name: incomplete_judge
---
model: "gpt-4o"
criteria: []
scoring:
  threshold: 0.75
```
## Why it fails
Lacks required evaluation criteria and API configuration, making the judge non-functional. Empty criteria list prevents any meaningful evaluation.

## Anti-Example 2: Human Rubric Contamination
```markdown
---
kind: judge_config
name: hybrid_judge
---
model: "gpt-4o"
criteria:
  - "Use 3-point rubric for grammar"
  - "Apply human-style feedback"
scoring:
  threshold: 0.5
  scale: "A-F"
```
## Why it fails
Mixes automated judge config with human rubric elements (letter grades, explicit feedback instructions). Contradicts boundary requirement to exclude scoring_rubric content.
