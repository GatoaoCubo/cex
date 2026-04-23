---
kind: quality_gate
id: p11_qg_output_validator
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of output_validator artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: output_validator"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, output-validator, P05]
tldr: "Pass/fail gate for output_validator artifacts: required fields, id pattern, body sections, parameter completeness."
domain: "post-LLM output validation and correction"
created: "2026-03-29"
updated: "2026-03-29"
density_score: 0.90
related:
  - bld_examples_output_validator
  - p11_qg_retriever_config
  - p11_qg_memory_scope
  - p11_qg_chunk_strategy
  - p11_qg_handoff_protocol
  - p11_qg_constraint_spec
  - p11_qg_prompt_version
  - p11_qg_effort_profile
  - bld_instruction_output_validator
  - p11_qg_hook_config
---

## Quality Gate

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

## Examples

# Examples: output-validator-builder
## Golden Example
INPUT: "Create output validator for product listing JSON"
OUTPUT:
```yaml
id: p05_oval_product_listing
kind: output_validator
pillar: P05
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
name: "Product Listing JSON Validator"
quality: null
tags: [output_validator, P05, output]
tldr: "Product Listing JSON Validator — production-ready output_validator configuration"
```
## Overview
Post-generation validator for product listing JSON output.
Runs 4 checks in sequence; on failure, injects error context and retries up to 2 times.

## Checks
| ID | Check | Type | Severity | Description |
|----|-------|------|----------|-------------|
| C01 | schema_valid | json_schema | HARD | Output matches product listing Pydantic model |
| C02 | price_positive | assertion | HARD | price > 0 and price < 999999 |
| C03 | title_length | range | SOFT | 10 <= len(title) <= 200 characters |
| C04 | no_prohibited_claims | regex_deny | HARD | No health claims, no superlatives without evidence |
Execution order: C01 -> C02 -> C04 -> C03 (HARD gates first, SOFT last).
Short-circuit: first HARD failure triggers on_fail immediately.

## Failure Actions
| Action | When | Behavior |
|--------|------|----------|
| fix_and_retry | HARD gate fails, retries < 2 | Inject error + failed check into prompt, regenerate |
| warn | SOFT gate fails | Log warning, pass output with quality penalty |
| reject | HARD gate fails after 2 retries | Return error object with failure details |
Fix prompt template: "Previous output failed validation: {error}. Fix the {field} field to satisfy: {check_description}. Output ONLY the corrected JSON."
Max retries: 2. Backoff: none (immediate retry).

## Integration
- Input: raw LLM output string (expected JSON)
- Output: validated object or error report
- Upstream: p03_constraint_json_product (decode-time constraint)
- Downstream: p11_qg_product_listing (quality scoring)
- Applies to: any pipeline producing product listing JSON
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p05_oval_ pattern (H02 pass)
- kind: output_validator (H04 pass)
- All required fields present (H06 pass)
- Body has all 4 sections: Overview, Checks, Failure Actions, Integration (H07 pass)
- Parameters table with value and rationale (S03 pass)
- tldr under 160 chars (S01 pass)
- tags >= 3 items, includes "output_validator" (S02 pass)
## Anti-Example
INPUT: "Create validator for chat responses"
BAD OUTPUT:
```yaml
id: chat-validator
kind: validator
quality: 9.0
tags: [validator]
```
FAILURES:
1. id has hyphens and no p05_oval_ prefix -> H02 FAIL
2. kind: 'validator' not 'output_validator' -> H04 FAIL
3. Missing fields: checks, on_fail -> H06 FAIL
4. quality: 9.5 (not null) -> H05 FAIL
5. No ## Checks section with table -> H07 FAIL
6. No failure actions table -> S04 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
