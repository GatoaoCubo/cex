---
kind: examples
id: bld_examples_prompt_version
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of prompt_version artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.1
title: "Examples Prompt Version"
version: "1.0.0"
author: n03_builder
tags: [prompt_version, builder, examples]
tldr: "Golden and anti-examples for prompt version construction, demonstrating ideal structure and common pitfalls."
domain: "prompt version construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

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
