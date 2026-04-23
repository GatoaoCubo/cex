---
kind: quality_gate
id: p11_qg_prompt_version
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of prompt_version artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: prompt_version"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, prompt-version, P03]
tldr: "Pass/fail gate for prompt_version artifacts: required fields, id pattern, body sections, parameter completeness."
domain: "versioned prompt snapshots for tracking and rollback"
created: "2026-03-29"
updated: "2026-03-29"
density_score: 0.90
related:
  - bld_examples_prompt_version
  - p11_qg_retriever_config
  - p11_qg_chunk_strategy
  - p11_qg_memory_scope
  - p11_qg_handoff_protocol
  - p11_qg_output_validator
  - p11_qg_constraint_spec
  - bld_instruction_prompt_version
  - p11_qg_effort_profile
  - p03_sp_prompt_version_builder
---

## Quality Gate

# Gate: prompt_version
## Definition
| Field | Value |
|---|---|
| metric | prompt_version artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: prompt_version` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p03_pv_[a-z][a-z0-9_]+$` | ID contains uppercase, spaces, or invalid chars |
| H03 | ID equals filename stem | id field != filename without extension |
| H04 | Kind equals literal `prompt_version` | Any other kind value |
| H05 | Quality field is null | Any non-null value |
| H06 | All required fields present | Missing quality, tags, tldr or other required fields |
| H07 | All required body sections present | Missing ## Overview or ## Prompt Snapshot or ## Metrics or ## Lineage |
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
| Density | 1.0 | Information density >= 0.8, no filler content |
| Tags quality | 0.5 | Tags >= 3, includes "prompt_version", relevant to content |
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

# Examples: prompt-version-builder
## Golden Example
INPUT: "Create prompt version for product description generator v2"
OUTPUT:
```yaml
id: p03_pv_product_desc_v2
kind: prompt_version
pillar: P03
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
name: "Product Description Generator v2"
quality: null
tags: [prompt_version, P03, prompt]
tldr: "Product Description Generator v2 — production-ready prompt_version configuration"
```
## Overview
Immutable snapshot of product description prompt after optimization pass.
Improved conversion rate by 12% over v1 through shorter, benefit-focused copy.

## Prompt Snapshot
```
Template: p03_pt_product_description
Version: 2.0.0
Hash: sha256:a1b2c3d4e5f6...
Variables: [product_name, features, target_audience, tone, max_words]
Token count: 847
Model tested: claude-sonnet-4-5-20250514
```

## Metrics
| Metric | v1.0.0 | v2.0.0 | Delta |
|--------|--------|--------|-------|
| Conversion rate | 3.2% | 3.6% | +12.5% |
| Avg length (words) | 185 | 142 | -23.2% |
| Readability (Flesch) | 62 | 71 | +14.5% |
| Eval score (P07) | 7.8 | 8.5 | +9.0% |
| Hallucination rate | 2.1% | 0.8% | -61.9% |
Status: promoted (active in production)
AB group: winner (was variant_a, beat control by 12.5%)

## Lineage
- v1.0.0 (2026-02-15): Initial version, verbose style
- v1.1.0 (2026-02-28): Minor tone adjustment
- v2.0.0 (2026-03-15): DSPy-optimized, benefit-focused rewrite <- THIS VERSION
Parent: p03_pv_product_desc_v1_1
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p03_pv_ pattern (H02 pass)
- kind: prompt_version (H04 pass)
- All required fields present (H06 pass)
- Body has all 4 sections: Overview, Prompt Snapshot, Metrics, Lineage (H07 pass)
- Parameters table with value and rationale (S03 pass)
- tldr under 160 chars (S01 pass)
- tags >= 3 items, includes "prompt_version" (S02 pass)
## Anti-Example
INPUT: "Create prompt version for email template"
BAD OUTPUT:
```yaml
id: email-v2
kind: prompt
quality: 9.0
tags: [prompt]
```
FAILURES:
1. id has hyphens and no p03_pv_ prefix -> H02 FAIL
2. kind: 'prompt' not 'prompt_version' -> H04 FAIL
3. Missing fields: prompt_ref, version, author -> H06 FAIL
4. quality: 8.0 (not null) -> H05 FAIL
5. No ## Prompt Snapshot section -> H07 FAIL
6. No metrics comparison table -> S03 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
