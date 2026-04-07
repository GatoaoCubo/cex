---
kind: examples
id: bld_examples_few_shot_example
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of few_shot_example artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: few-shot-example-builder
## Golden Example
INPUT: "Create um few_shot_example mostrando the format de frontmatter YAML de um knowledge_card"
OUTPUT:
```yaml
id: p01_fse_kc_frontmatter
kind: few_shot_example
pillar: P01
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
input: "Create a knowledge card about Docker networking basics"
output: |
  id: kc_docker_networking
  kind: knowledge_card
  pillar: P01
  version: "1.0.0"
  created: "2026-03-26"
  updated: "2026-03-26"
  author: "knowledge-engine"
  quality: null
  tags: [docker, networking, devops]
  tldr: "Docker networking: bridge, host, overlay modes and use cases."
domain: knowledge_card
difficulty: easy
edge_case: false
format: "knowledge_card YAML frontmatter"
quality: null
tags: [few-shot, knowledge-card, frontmatter, yaml]
tldr: "Input/output pair teaching knowledge_card YAML frontmatter format."
keywords: [knowledge-card, frontmatter, yaml, format]
```
## Explanation
Teaches the exact YAML frontmatter structure for knowledge_card.
LLM learns: required fields, field order, quality: null rule, tags as list.
## Variations
- **Variation 1**: "Create a KC about Python async/await" — same format, different domain
- **Variation 2**: "Create a KC about React hooks best forctices" — tests tag selection
## Edge Cases
- **Edge**: input requests a KC with quality: 9.0
  **Expected**: output shows quality: null — self-scoring is forbidden
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p01_fse_ pattern (H02 pass)
- id == filename stem p01_fse_kc_frontmatter (H03 pass)
- kind: few_shot_example (H04 pass)
- input field non-empty, realistic task (H06 pass)
- output field non-empty, shows complete format (H07 pass)
- YAML parses cleanly (H01 pass)
- tldr <= 160 chars (S01 pass)
- tags list has 4 items >= 3 (S02 pass)
- Explanation section present (S03 pass)
- No scoring rubric (S07 pass)
## Anti-Example
INPUT: "Faz um example de knowledge card"
BAD OUTPUT:
```yaml
id: kc_example
kind: example
pillar: knowledge
input: write a knowledge card
output: a good knowledge card with all fields
quality: 8.5
scoring:
  criteria: completeness
  weight: 0.5
tags: example
This document shows how to make knowledge cards. Basically you fill in the fields.
```
FAILURES:
1. id: no `p01_fse_` prefix -> H02 FAIL
2. kind: "example" not "few_shot_example" -> H04 FAIL
3. quality: 8.5 (not null) -> H05 FAIL
4. input: "write a knowledge card" — not a realistic task request -> S04 FAIL
5. output: abstract description, not format demonstration -> S05 FAIL
6. scoring rubric included: golden_test drift -> S07 FAIL
7. tags: string not list, len < 3 -> S02 FAIL
8. body: filler prose ("basically you fill in the fields") -> S07 FAIL
9. pillar: "knowledge" not "P01" -> H01 schema violation
10. Explanation section missing -> S03 FAIL
