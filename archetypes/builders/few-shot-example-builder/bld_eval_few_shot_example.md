---
kind: quality_gate
id: p11_qg_few_shot_example
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of few_shot_example artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: few_shot_example"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, few-shot-example, prompt-engineering, format-teaching, P11]
tldr: "Validates few_shot_example artifacts: input/output completeness, format demonstration clarity, and byte-size constraint."
domain: "few_shot_example — input/output pairs that teach format to LLMs via in-context prompt engineering"
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.90
related:
  - bld_examples_few_shot_example
  - p11_qg_golden_test
  - bld_instruction_few_shot_example
  - bld_schema_few_shot_example
  - p11_qg_formatter
  - p11_qg_glossary_entry
  - bld_knowledge_card_few_shot_example
  - p03_sp_few_shot_example_builder
  - p10_lr_few_shot_example_builder
  - bld_output_template_few_shot_example
---

## Quality Gate

# Gate: few_shot_example
## Definition
| Field     | Value |
|-----------|-------|
| metric    | composite score across SOFT dimensions |
| threshold | >= 7.0 to publish; >= 9.5 for golden |
| operator  | weighted average after all HARD gates pass |
| scope     | all artifacts where `kind: few_shot_example` |
All HARD gates are AND-logic: one failure rejects the artifact regardless of SOFT score.
## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Any YAML syntax error |
| H02 | ID matches `^p01_fse_[a-z][a-z0-9_]+$` | Wrong format or namespace |
| H03 | ID equals filename stem (no extension) | Mismatch between id field and file name |
| H04 | Kind equals literal `few_shot_example` | Any other value |
| H05 | `quality` field is null | Any non-null value |
| H06 | `input` field present and non-empty string | Missing or empty input |
| H07 | `output` field present and non-empty string | Missing or empty output |
| H08 | Artifact body size <= 1024 bytes | Exceeds byte limit (bloats prompt context) |
| H09 | No scoring rubric present anywhere in the artifact | Rubric found (conflates with golden_test) |
## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| S01 | `tldr` <= 160 chars, names the format being taught | 0.10 | Accurate=1.0, vague=0.4, absent=0.0 |
| S02 | Tags list len >= 3, includes `few-shot` | 0.05 | Met=1.0, partial=0.5 |
| S03 | Output demonstrates FORMAT visibly (structure present, not just content) | 0.18 | Clear structure=1.0, content-only=0.2 |
| S04 | Input is a realistic task request (not abstract or contrived) | 0.14 | Realistic=1.0, contrived=0.3 |
| S05 | Explanation section present and explains why the output format is correct | 0.12 | Present+explains=1.0, missing=0.0 |
| S06 | Example is self-contained (no external reference required to understand it) | 0.10 | Self-contained=1.0, requires context=0.2 |
| S07 | Example covers a non-trivial pattern (edge case or formatting nuance) | 0.10 | Non-trivial=1.0, trivial happy-path=0.4 |
| S08 | `density_score` >= 0.80 | 0.08 | Met=1.0, below=0.0 |
| S09 | No filler in output ("as you can see", "this example shows") | 0.07 | Clean=1.0, filler present=0.0 |
| S10 | Difficulty level (`easy`/`medium`/`hard`) matches actual complexity | 0.06 | Accurate=1.0, mislabeled=0.2 |
**Weight sum: 1.00**
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — reference artifact for few_shot_example calibration |
| >= 8.0 | PUBLISH — pool-eligible; format clearly demonstrated in output |
| >= 7.0 | REVIEW — usable but output may be content-heavy, not format-focused |
| < 7.0  | REJECT — redo; likely missing format structure or oversized body |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Domain so narrow that no realistic input exists; synthetic input approved in writing |
| approver | Prompt engineer who owns the target prompt template |
| audit trail | Required: target prompt ID, justification for synthetic input, approver name |
| expiry | Permanent until a realistic example is available to replace it |
| never bypass | H01 (corrupt YAML), H05 (self-scored quality is invalid), H08 (byte limit protects prompt context budgets — non-negotiable) |

## Examples

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
quality: 8.8
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
