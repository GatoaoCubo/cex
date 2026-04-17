---
id: p07_sr_5d_brand_evaluation
kind: scoring_rubric
pillar: P07
title: "Rubric: 5D Brand Evaluation"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "scoring-rubric-builder"
framework: "5D"
target_kinds: [brand_config, agent, system_prompt, agent_card]
dimensions_count: 5
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: "semi-automated"
domain: "brand"
quality: 9.1
tags: [scoring-rubric, 5d, brand, evaluation, brand-identity]
tldr: "5D brand rubric: consistency 25%, clarity 25%, differentiation 20%, authenticity 15%, memorability 15%"
density_score: 0.91
calibration_set: [p07_gt_brand_nucleus_config, p07_gt_brand_voice_calibration]
inter_rater_agreement: 0.83
appeals_process: "Submit to N06 chief reviewer with dimension-level rationale; re-evaluation within 24h"
linked_artifacts:
  primary: "p11_qg_brand_artifacts"
  related: [p03_system_prompt_brand_nucleus, p01_bld_sp_manifest_software_project_create_agent_card_for_engineering_nucleus]
---
## Framework Overview

5D Brand Evaluation measures the quality of brand-carrying artifacts across five orthogonal dimensions that determine whether an artifact strengthens or dilutes brand identity. Applies to brand_config files, agent personas (system_prompt, agent), and agent_card artifacts that express brand voice.

This rubric complements the P11 brand quality gate (pass/fail barrier) by providing nuanced weighted scoring for brand strength. A gate pass does not guarantee a high rubric score — the gate enforces minimum presence, the rubric measures quality of execution.

**Not covered**: technical correctness of YAML syntax (→ quality_gate H01), pricing or funnel effectiveness (→ N06 monetization rubric), code quality (→ N05 operations rubric).

## Dimensions

| Dimension | Weight | Scale | Criteria | Example (10) | Example (5) |
|-----------|--------|-------|----------|-------------|-------------|
| Consistency | 25% | 0-10 | Verbal/visual elements align across all artifact sections; zero contradictions in tone, naming, or values | Single voice throughout; values, tone, and naming conventions identical in every section; no term used in two different senses | Tone shifts between sections; one value named differently in two places; formatting inconsistent |
| Clarity | 25% | 0-10 | Brand positioning, value proposition, and target audience are explicit and unambiguous; a reader unfamiliar with the brand understands who it is for and why | One-sentence UVP present, specific audience demographic named, differentiator named with concrete comparison; no jargon without definition | Positioning implied but not stated; audience described as "professionals" without specifics; value prop buried in paragraph 3 |
| Differentiation | 20% | 0-10 | Artifact makes brand's unique position legible vs. at least one named alternative; avoids commodity language | Names 2+ specific differentiators; contrasts with named alternatives; avoids "best quality" / "trusted" / "innovative" as standalone claims | States one differentiator without comparison; uses 3+ commodity phrases like "industry-leading" without evidence |
| Authenticity | 15% | 0-10 | Brand values are traceable to specific behaviors, not stated as ideals; voice matches the declared personality profile | Values demonstrated through concrete examples or behaviors; personality profile referenced and embodied in tone choices; no aspirational-only claims | Values listed but no behavioral evidence; tone described as "friendly" but copy is formal; mission statement not reflected in artifact body |
| Memorability | 15% | 0-10 | Artifact contains at least one distinctive phrase, metaphor, or device that anchors the brand in memory; avoids generic phrasing | 1+ coined phrase or memorable metaphor; brand name conceptually linked to a unique idea; someone reading once could recall the brand concept | Generic phrasing throughout; brand name could be swapped for a competitor; no distinctive voice fingerprint |

## Thresholds

| Tier | Score | Range | Action |
|------|-------|-------|--------|
| GOLDEN | >= 9.5 | 9.5 – 10.0 | Promote to calibration_set; use as reference example for future brand artifacts |
| PUBLISH | >= 8.0 | 8.0 – 9.4 | Merge to brand pool; cleared for nucleus consumption |
| REVIEW | >= 7.0 | 7.0 – 7.9 | Return to author with dimension-level feedback; specify lowest-scoring dimension first |
| REJECT | < 7.0 | 0 – 6.9 | Redo from brand_config source; do not patch — structural brand signal is missing |

## Calibration

**GOLDEN (9.7)**: brand_config with 6 core values each tied to one concrete behavior, single coined phrase ("X in CEX is a variable"), UVP in first sentence, audience named as "early-stage SaaS founders with 2+ engineers", two named competitors with specific differentiation claims, tone profile with 5 do/don't examples. All sections use same vocabulary for core concepts.

**PUBLISH (8.2)**: brand_config with 4 values, UVP present but in paragraph 2, audience named broadly ("tech startups"), one differentiator with vague comparison ("unlike most tools"), consistent tone, one memorable tagline. Differentiation score 7 drags overall below GOLDEN.

**REVIEW (7.3)**: system_prompt with correct tone but no explicit UVP, audience unstated, two values named without behavioral evidence, no distinctive phrases, minor tone shift in the examples section. Clarity (5) and Memorability (6) pull score below PUBLISH.

**REJECT (5.8)**: agent_card with generic "helpful assistant" framing, no brand values present, interchangeable with any vendor, commodity phrasing throughout ("reliable", "professional", "high quality"), no UVP, no audience. All five dimensions below 7.

## Automation

| Dimension | Status | Tool |
|-----------|--------|------|
| Consistency | semi-automated | brand_validate.py — detects term collisions and tone markers across sections |
| Clarity | semi-automated | brand_audit.py — checks for UVP and audience keyword presence; human verifies specificity |
| Differentiation | manual | Human review required; commodity-phrase detector flags candidates but cannot score comparison quality |
| Authenticity | manual | Human review required; values-behavior linkage requires semantic judgment |
| Memorability | manual | Human review required; distinctiveness cannot be reliably automated |

## References

- brand_validate.py v1.0 — term collision and tone consistency checker
- brand_audit.py v1.0 — brand signal presence audit (6 dimensions)
- AAC&U VALUE Rubrics (2009): https://www.aacu.org/initiatives/value-initiative
- N06 Scoring Rubric (brand + monetization dual model) — `P07_evals/examples/`