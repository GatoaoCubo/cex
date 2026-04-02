---
id: p07_sr_knowledge_eval
kind: scoring_rubric
pillar: P07
title: "Rubric: Knowledge Evaluation"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "scoring-rubric-builder"
framework: "knowledge_eval"
target_kinds: [knowledge_card, context_doc, glossary_entry]
dimensions_count: 5
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: "semi-automated"
domain: "knowledge"
quality: 9.1
tags: [scoring-rubric, knowledge-eval, knowledge-card, evaluation, P07]
tldr: "5D rubric for knowledge artifacts: density 25%, completeness 25%, actionability 20%, accuracy 20%, boundary 10%."
density_score: 0.91
calibration_set: [p07_gt_kc_prompt_caching]
inter_rater_agreement: 0.85
appeals_process: "Submit re-evaluation request to N04 with annotated objections per dimension; chief reviewer adjudicates within 48h"
linked_artifacts:
  primary: "knowledge-card-builder"
  related: [p11_qg_kc_publish, p07_gt_kc_prompt_caching, p07_sr_5d_knowledge_card]
---
## Framework Overview

knowledge_eval measures quality of artifacts that encode factual domain knowledge for LLM nucleus injection: knowledge_card (P01), context_doc (P03), glossary_entry (P04). Poor knowledge artifacts cascade into poor downstream generation — this rubric provides SOFT scoring to discriminate between surface-complete and genuinely useful knowledge. Use alongside quality_gate (P11), which enforces HARD pass/fail barriers; this rubric drives the PUBLISH / REVIEW / REJECT tier decision and coaching feedback.

## Dimensions

| Dimension | Weight | Scale | Criteria | Example (10) | Example (5) |
|-----------|--------|-------|----------|-------------|-------------|
| Density | 25% | 0-10 | Concrete data ratio (facts/tables/code/values) >= 0.80 of total token count | density=0.93; every sentence carries a fact or threshold; zero filler phrases | density=0.65; has "this section describes"; some tables but padding present |
| Completeness | 25% | 0-10 | All schema-required sections present; >= 3 substantive items per section; frontmatter fully populated | 7 sections, 5+ bullets each, all frontmatter fields filled, spec table present | 4 sections, two with < 3 bullets, missing `tldr` or `tags` |
| Actionability | 20% | 0-10 | Contains commands, code snippets, or decision-ready anti-patterns with explicit when / when-not guidance | 3 CLI commands, 2 code blocks, anti-pattern table >= 4 rows, explicit "when NOT to use" | Pattern names listed; no usage examples or commands |
| Accuracy | 20% | 0-10 | Claims verifiable; >= 1 source URL with date; zero contradictions with schema or kind spec | 3 accessible URLs, dated 2024-2026, zero schema contradictions, cross-refs verified | 1 URL, 2 unverifiable claims, one field description contradicts schema |
| Boundary Clarity | 10% | 0-10 | Explicit IS / IS NOT table; no scope drift into adjacent kinds; >= 3 IS NOT rows | 5-row IS/IS NOT table, adjacent kinds named explicitly, zero prose drift | Scope paragraph only; no explicit IS NOT rows; overlaps with quality_gate description |

## Score Anchors

| Score | Density | Completeness | Actionability | Accuracy | Boundary |
|-------|---------|--------------|---------------|----------|----------|
| 10 | >= 0.90; no filler; tables dominate prose | All required + recommended; every field populated | Commands + code + anti-patterns + when-not table | All claims sourced; all URLs accessible | IS/IS NOT >= 5 rows; adjacent kinds named |
| 9 | 0.85–0.89; max 1 filler sentence | All required sections; 1 recommended missing | Commands + code + anti-patterns present | >= 2 URLs; max 1 minor unverifiable claim | IS/IS NOT >= 3 rows; adjacent kinds named |
| 7 | 0.75–0.84; readable but some padding | All required; some sections < 3 bullets | 1–2 commands or code snippets; no anti-patterns | 1 URL; claims internally consistent | IS/IS NOT section present but prose-only |
| 5 | 0.60–0.74; noticeable padding; still usable | 1 required section missing or empty | Pattern names listed; no examples or commands | No URLs; claims plausible but unverified | Scope paragraph; no explicit IS NOT |
| 3 | 0.40–0.59; more filler than content | 2+ required sections missing | Theory only; requires inference to act | 1+ contradiction with schema or adjacent KC | No boundary section; overlaps with other kinds |
| 1 | < 0.40; no actionable content | < 50% required sections present | Abstract description only | Multiple factual errors or schema violations | No scope; content could belong to any kind |

## Thresholds

| Tier | Score | Action |
|------|-------|--------|
| GOLDEN | >= 9.5 | Promote to `calibration_set`; mark as reference example in builder ISOs |
| PUBLISH | >= 8.0 | Merge to knowledge pool; available for nucleus injection |
| REVIEW | >= 7.0 | Return with per-dimension breakdown and specific improvement targets |
| REJECT | < 7.0 | Redo from scratch; attach this rubric score sheet as failure report |

Score formula: `final = density×0.25 + completeness×0.25 + actionability×0.20 + accuracy×0.20 + boundary×0.10`

## Calibration

| Tier | Example | Score | Key Signals |
|------|---------|-------|-------------|
| GOLDEN | p07_gt_kc_prompt_caching | 9.8 | density=0.93, 7 sections, 3 verified URLs, IS/IS NOT table, 4 code snippets |
| PUBLISH | typical KC with all sections | 8.3 | density=0.82, 1 URL, adequate boundary, 1 code example |
| REVIEW | KC with weak actionability | 7.2 | density=0.75, no URLs, vague boundary, no commands |
| REJECT | stub KC, 3 sections | 5.0 | density=0.50, no URLs, no boundary, no commands |

Inter-rater calibration: two reviewers must agree within ±0.5 per dimension. Disagreement >= 1.0 on any dimension → escalate to N04 chief reviewer with annotated example. Target inter-rater agreement >= 0.85.

## Automation

| Dimension | Status | Tool |
|-----------|--------|------|
| Density | automated | `validate_kc.py` — char-ratio calculation |
| Completeness | automated | `cex_doctor.py` — section + field counting |
| Actionability | semi-automated | Grep for code block + command patterns; human review for quality |
| Accuracy | semi-automated | `link_check.py` — URL presence; manual claim verification |
| Boundary Clarity | semi-automated | Grep for IS/IS NOT patterns; human review for overlap |

## References
- AAC&U VALUE Rubrics: https://www.aacu.org/initiatives/value-initiative
- Bloom Taxonomy (Anderson & Krathwohl, 2001 revision)
- CEX `validate_kc.py` v2.0 — 5D density implementation
- LLM-as-Judge (Zheng et al., 2023): https://arxiv.org/abs/2306.05685