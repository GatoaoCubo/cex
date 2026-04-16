---
kind: examples
id: bld_examples_scoring_rubric
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of scoring_rubric artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.1
title: "Examples Scoring Rubric"
version: "1.0.0"
author: n03_builder
tags: [scoring_rubric, builder, examples]
tldr: "Golden and anti-examples for scoring rubric construction, demonstrating ideal structure and common pitfalls."
domain: "scoring rubric construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: scoring-rubric-builder
## Golden Example
INPUT: "Create rubric de evaluation 5D para knowledge_cards"
OUTPUT:
```yaml
id: p07_sr_5d_knowledge_card
kind: scoring_rubric
pillar: P07
title: "Rubric: 5D Knowledge Card"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
framework: "5D"
target_kinds: [knowledge_card]
dimensions_count: 5
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: "semi-automated"
domain: "knowledge"
quality: null
tags: [scoring-rubric, 5d, knowledge-card, evaluation]
tldr: "5-dimension rubric for KCs: density 25%, completeness 25%, actionability 20%, boundary 15%, references 15%"
density_score: 0.92
calibration_set: [p07_gt_kc_prompt_caching]
inter_rater_agreement: 0.85
appeals_process: "Submit to p01-chief with rationale for re-evaluation"
linked_artifacts:
  primary: "quality-gate-builder"
  related: [p11_qg_kc_publish, p07_gt_kc_prompt_caching]
## Framework Overview
5D evaluates knowledge_cards across 5 orthogonal dimensions.
Designed to complement the KC quality_gate (P11) which enforces HARD pass/fail.
This rubric provides the SOFT scoring framework for nuanced quality assessment.
## Dimensions
| Dimension | Weight | Scale | Criteria | Example (10) | Example (5) |
|-----------|--------|-------|----------|-------------|-------------|
| Density | 25% | 0-10 | Ratio of concrete data to total text >= 0.80 | 0.93 density, zero filler phrases | 0.65 density, has "this document describes" |
| Completeness | 25% | 0-10 | All required sections present, >= 3 bullets each | 7 sections, 4+ bullets, all fields filled | 4 sections, some empty, missing tags |
| Actionability | 20% | 0-10 | Contains commands, code, or specific steps | 3 CLI commands, 2 code snippets, concrete steps | General advice, no specific commands |
| Boundary | 15% | 0-10 | Clear IS/IS NOT, no drift to other types | Explicit boundary table, 3+ IS NOT rows | Vague scope, overlaps with other kinds |
| References | 15% | 0-10 | >= 1 source URL, dates, verifiable claims | 3 URLs, all accessible, dated 2026 | No URLs, unverifiable claims |
## Thresholds
| Tier | Score | Action |
|------|-------|--------|
| GOLDEN | >= 9.5 | Promote to calibration set, mark as reference |
| PUBLISH | >= 8.0 | Merge to pool |
| REVIEW | >= 7.0 | Return with specific dimension feedback |
| REJECT | < 7.0 | Redo from scratch with new research |
## Calibration
- GOLDEN (9.8): p07_gt_kc_prompt_caching — density 0.93, 7 sections, 3 URLs, explicit boundary
- PUBLISH (8.3): typical KC with all sections, density 0.82, 1 URL, adequate boundary
- REVIEW (7.2): KC with 5 sections, density 0.75, no URLs, vague boundary
- REJECT (5.0): KC with 3 sections, density 0.50, filler prose, no boundary section
## Automation
| Dimension | Status | Tool |
|-----------|--------|------|
| Density | automated | validate_kc.py (char ratio calculation) |
| Completeness | automated | validate_kc.py (section/field counting) |
| Actionability | manual | Human review for command quality |
| Boundary | semi-automated | Grep for IS/IS NOT patterns |
| References | semi-automated | URL presence check + manual accessibility |
## References
- AAC&U VALUE Rubrics: https://www.aacu.org/initiatives/value-initiative
- validate_kc.py v2.0 (CEX 5D implementation reference)
```
WHY THIS IS GOLDEN:
- quality: null (H06 pass)
- id matches p07_sr_ pattern (H02 pass)
- kind: scoring_rubric (H04 pass)
- 25 frontmatter fields present (H08 pass)
- 5 dimensions with weights 25+25+20+15+15 = 100% (H07 pass)
- All 4 tiers defined with score ranges and actions (H09 pass)
- Criteria are concrete per dimension with examples at 10 and 5 (S03 pass)
- Calibration section has examples at all 4 tiers (S05 pass)
- Automation status per dimension with tool refs (S06 pass)
