---
id: p11_qg_output_validator
kind: quality_gate
pillar: P11
title: "Gate: output_validator"
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
domain: "post-LLM output validation and correction"
quality: 9.0
tags: [quality-gate, output-validator, P05]
tldr: "Pass/fail gate for output_validator artifacts: required fields, id pattern, body sections, parameter completeness."
density_score: 0.90
llm_function: GOVERN
---
# Gate: output_validator
## Definition
| Field | Value |
|---|---|
| metric | output_validator artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: output_validator` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p05_oval_[a-z][a-z0-9_]+$` | ID contains uppercase, spaces, or invalid chars |
| H03 | ID equals filename stem | id field != filename without extension |
| H04 | Kind equals literal `output_validator` | Any other kind value |
| H05 | Quality field is null | Any non-null value |
| H06 | All required fields present | Missing quality, tags, tldr or other required fields |
| H07 | All required body sections present | Missing ## Overview or ## Checks or ## Failure Actions or ## Integration |
| H08 | Body <= 2048 bytes | Body exceeds size limit |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Parameter completeness | 1.0 | All parameters have concrete values (no placeholders) |
| Rationale quality | 1.0 | Each parameter value has clear rationale |
| Pattern selection | 1.0 | Correct pattern chosen for the use case |
| Boundary clarity | 1.0 | Explicitly states what this IS and IS NOT |
| Integration mapping | 0.5 | Upstream and downstream connections documented |
| Density | 1.0 | Information density >= 0.85, no filler content |
| Tags quality | 0.5 | Tags >= 3, includes "output_validator", relevant to content |
| Tldr quality | 0.5 | Tldr <= 160 chars, dense, accurate summary |
| Domain specificity | 1.0 | Parameters and values specific to declared domain |
| Testability | 0.5 | Configuration can be validated with known inputs |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
