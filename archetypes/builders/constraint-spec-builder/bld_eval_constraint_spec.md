---
kind: quality_gate
id: p11_qg_constraint_spec
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of constraint_spec artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: constraint_spec"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, constraint-spec, P03]
tldr: "Pass/fail gate for constraint_spec artifacts: required fields, id pattern, body sections, parameter completeness."
domain: "constrained LLM generation rules"
created: "2026-03-29"
updated: "2026-03-29"
density_score: 1.0
related:
  - bld_examples_constraint_spec
  - p11_qg_chunk_strategy
  - p11_qg_retriever_config
  - p11_qg_memory_scope
  - p11_qg_output_validator
  - p11_qg_handoff_protocol
  - p11_qg_effort_profile
  - p11_qg_prompt_version
  - bld_instruction_constraint_spec
  - p10_lr_constraint_spec_builder
---

## Quality Gate

# Gate: constraint_spec
## Definition
| Field | Value |
|---|---|
| metric | constraint_spec artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: constraint_spec` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p03_constraint_[a-z][a-z0-9_]+$` | ID contains uppercase, spaces, or invalid chars |
| H03 | ID equals filename stem | id field != filename without extension |
| H04 | Kind equals literal `constraint_spec` | Any other kind value |
| H05 | Quality field is null | Any non-null value |
| H06 | All required fields present | Missing quality, tags, tldr or other required fields |
| H07 | All required body sections present | Missing ## Overview or ## Constraint Definition or ## Provider Compatibility or ## Integration |
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
| Tags quality | 0.5 | Tags >= 3, includes "constraint_spec", relevant to content |
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

## Bypass
| Field | Value |
|-------|-------|
| conditions | Experimental constrained LLM generation rules artifact under active A/B testing |
| approver | Nucleus lead (written approval required) |
| audit_trail | Log in records/audits/ with bypass reason and timestamp |
| expiry | 48h — must pass all gates before expiry |
| never_bypass | H01 (YAML parse), H05 (quality null) |

## Examples

# Examples: constraint-spec-builder
## Golden Example
INPUT: "Create constraint spec for JSON output with specific schema"
OUTPUT:
```yaml
id: p03_constraint_json_product
kind: constraint_spec
pillar: P03
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
name: "Product Data JSON Constraint"
quality: null
tags: [constraint_spec, P03, constraint]
tldr: "Product Data JSON Constraint — production-ready constraint_spec configuration"
```
## Overview
JSON schema constraint ensuring LLM outputs valid product data objects.
Applied at decode time where supported; falls back to output_validator post-generation.

## Constraint Definition
Type: json_schema
```json
{
  "type": "object",
  "required": ["name", "price", "category"],
  "properties": {
    "name": {"type": "string", "maxLength": 200},
    "price": {"type": "number", "minimum": 0},
    "category": {"type": "string", "enum": ["electronics", "home", "fashion", "food"]}
  },
  "additionalProperties": false
}
```
Temperature override: 0.3 (lower for structured output reliability).
Max tokens: 500 (bounded to prevent runaway generation).

## Provider Compatibility
| Provider | Support | Method |
|----------|---------|--------|
| OpenAI | native | response_format: json_schema |
| Anthropic | partial | tool_use with schema |
| Outlines | native | JSON guide from schema |
| LMQL | partial | where clause + type hint |
Fallback: inject schema in prompt + output_validator post-check.

## Integration
- Injected into: prompt_template as generation constraint
- Validated by: p05_oval_product_schema (post-generation safety net)
- Used by: product listing pipeline, data extraction workflows
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p03_constraint_ pattern (H02 pass)
- kind: constraint_spec (H04 pass)
- All required fields present (H06 pass)
- Body has all 4 sections: Overview, Constraint Definition, Provider Compatibility, Integration (H07 pass)
- Parameters table with value and rationale (S03 pass)
- tldr under 160 chars (S01 pass)
- tags >= 3 items, includes "constraint_spec" (S02 pass)
## Anti-Example
INPUT: "Create constraint for structured output"
BAD OUTPUT:
```yaml
id: structured-output
kind: constraint
quality: 9.0
tags: [constraint]
```
FAILURES:
1. id has hyphens and no p03_constraint_ prefix -> H02 FAIL
2. kind: 'constraint' not 'constraint_spec' -> H04 FAIL
3. Missing fields: constraint_type, pattern -> H06 FAIL
4. quality: 9.0 (not null) -> H05 FAIL
5. No ## Constraint Definition section -> H07 FAIL
6. No provider compatibility table -> S04 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
