---
kind: examples
id: bld_examples_output_validator
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of output_validator artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.2
title: "Examples Output Validator"
version: "1.0.0"
author: n03_builder
tags: [output_validator, builder, examples]
tldr: "Golden and anti-examples for output validator construction, demonstrating ideal structure and common pitfalls."
domain: "output validator construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

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
