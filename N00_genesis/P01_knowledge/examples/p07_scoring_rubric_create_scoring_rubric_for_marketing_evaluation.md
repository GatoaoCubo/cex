---
id: p07_sr_5d_marketing
kind: scoring_rubric
pillar: P07
title: "Rubric: 5D Marketing"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "scoring-rubric-builder"
framework: "5D"
target_kinds: [system_prompt, prompt_template, agent, agent_card, knowledge_card]
dimensions_count: 5
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: "semi-automated"
domain: "marketing"
quality: 9.2
tags: [scoring-rubric, 5d, marketing, evaluation, copywriting, brand-voice]
tldr: "5D rubric for marketing artifacts: persuasion 30%, brand alignment 20%, audience fit 20%, CTA clarity 15%, message density 15%"
density_score: 0.91
inter_rater_agreement: 0.82
appeals_process: "Submit contested artifact to N02 lead with scored dimension and alternative evidence; re-scored within 24h"
linked_artifacts:
  primary: "quality-gate-builder"
  related: [p11_qg_marketing_artifacts, p03_system_prompt_create_system_prompt_for_marketing_nucleus]
---
## Framework Overview

5D Marketing evaluates marketing artifacts (system_prompt, prompt_template, agent, agent_card, knowledge_card) produced by N02 and N06 nuclei. It measures whether an artifact converts a reader by moving them through the clarity → desire → action arc, using on-brand language targeted at a specific persona.

This rubric complements the P11 marketing quality gate (binary pass/fail) by providing weighted scoring for nuanced quality assessment. Gate pass ≠ high rubric score: the gate enforces minimum structural presence; this rubric measures execution quality and conversion power.

**Not covered**: YAML syntax validity (→ H01 quality gate), pricing strategy soundness (→ N06 monetization rubric), technical code correctness (→ N05 operations rubric), factual accuracy of knowledge claims (→ N04 knowledge rubric).

## Dimensions

| Dimension | Weight | Scale | Criteria | Example (10) | Example (5) |
|-----------|--------|-------|----------|-------------|-------------|
| Persuasion | 30% | 0–10 | Clarity→desire→action arc fully present; emotional hook in first sentence; every sentence advances toward conversion | Perfect 3-phase arc, hooks in line 1, zero passive constructions, reader compelled to act | Copy is informational; two of three arc phases weak; reads as feature list without emotional engagement |
| Brand Alignment | 20% | 0–10 | Voice, tone, and archetype match brand_config; do/don't rules followed; no phrase sounds off-brand | Indistinguishable from brand's best content; archetype integrated throughout; zero off-brand phrases | Brand tone occasionally present; copy could belong to any company in the category; archetype named but not expressed |
| Audience Fit | 20% | 0–10 | Named persona referenced; specific pain points, vocabulary, and buying stage addressed; no generic language | Written for exact persona; pain points verbatim from audience research; vocabulary mirrors target's register | Audience implied by category; no persona differentiation; broad-appeal language; could target any market participant |
| CTA Clarity | 15% | 0–10 | Single unambiguous next step; action verb + benefit + urgency signal; no competing CTAs | One CTA, action verb + quantified benefit + deadline signal; zero competing links | CTA present but vague ("learn more" without benefit); urgency absent; reader must infer the value of clicking |
| Message Density | 15% | 0–10 | Every sentence removes an objection, adds proof, or advances desire; density ≥ 0.88; zero filler phrases | Density 0.90+; zero transitional filler; every sentence tests positive for persuasive function | Density 0.70–0.75; noticeable padding; key points buried in qualifying prose; 4–6 filler phrases |

## Score Anchors (per dimension)

### Persuasion
| Score | Criterion |
|-------|-----------|
| 10 | Three-phase arc complete; emotional hook occupies sentence 1; desire phase references reader's specific goal; CTA flows from desire without friction; zero passive voice |
| 9 | Arc fully present; hook present; at most one weak transition between phases |
| 7 | Arc identifiable; one phase underdeveloped but conversion logic followable |
| 5 | Two phases weak; copy informs but does not persuade; no emotional engagement |
| 3 | No arc; feature list or description; reader not moved toward any action |
| 1 | Random statements; no connection to reader's needs, desires, or context |

### Brand Alignment
| Score | Criterion |
|-------|-----------|
| 10 | Every sentence consistent with brand archetype, voice score, and do/don't vocabulary; impossible to confuse with competitor |
| 9 | Brand voice throughout; at most one phrase that sounds generically corporate |
| 7 | Brand tone identifiable; 2–3 phrases generic or slightly misaligned |
| 5 | Brand present in sections but absent elsewhere; category-generic language dominates |
| 3 | Archetype named in frontmatter but absent in body; generic corporate language |
| 1 | Copy contradicts brand voice definition; wrong archetype expressed |

### Audience Fit
| Score | Criterion |
|-------|-----------|
| 10 | Named persona; specific pain points referenced verbatim from audience research; vocabulary mirrors target's register; stage-appropriate (awareness/consideration/decision) |
| 9 | Clear persona match; pain points addressed; at most one generic phrase |
| 7 | Target audience inferable from copy; pain points implied but not explicit |
| 5 | Audience implied by category; no stage differentiation; could target anyone in market |
| 3 | No persona signal; broad-appeal language dilutes targeting |
| 1 | Wrong audience; mismatched vocabulary, wrong pain points, wrong buying stage |

### CTA Clarity
| Score | Criterion |
|-------|-----------|
| 10 | Single CTA; action verb + quantified benefit + urgency signal (deadline or scarcity); zero competing links |
| 9 | CTA clear; action verb and benefit present; urgency implied; at most one secondary reference |
| 7 | CTA specific but lacks urgency or benefit articulation |
| 5 | CTA present but vague ("learn more", "click here") without stated benefit |
| 3 | CTA buried or requires inference; no action verb |
| 1 | No CTA, or 3+ competing CTAs of equal visual weight causing decision paralysis |

### Message Density
| Score | Criterion |
|-------|-----------|
| 10 | Density ≥ 0.88; every sentence scores positive on persuasive function test (objection removal, proof, desire advancement) |
| 9 | Density ≥ 0.85; at most one transitional sentence without conversion value |
| 7 | Density ≥ 0.78; 2–3 filler phrases; core message remains strong |
| 5 | Density ≥ 0.70; noticeable padding; key points require extraction from prose |
| 3 | Density < 0.65; significant padding; message obscured |
| 1 | Density < 0.50; copy is filler with embedded message fragments |

## Thresholds

| Tier | Score | Range | Action |
|------|-------|-------|--------|
| GOLDEN | ≥ 9.5 | 9.5–10.0 | Promote to calibration set; use as reference example for future evaluation |
| PUBLISH | ≥ 8.0 | 8.0–9.4 | Merge to active pool; no revision required |
| REVIEW | ≥ 7.0 | 7.0–7.9 | Return with dimension-specific feedback; one revision cycle |
| REJECT | < 7.0 | 0.0–6.9 | Redo from scratch; attach scored rubric with failure dimensions |

## Calibration

Reference examples anchoring the four tiers:

- **GOLDEN (9.7)** — N02 launch email for SaaS product: 3-phase arc complete in 4 sentences; archetype ("Sage-Challenger") present in every paragraph; pain point "you're losing 3h/week to manual reporting" verbatim from ICP research; CTA "Start free — save your first hour today" with action verb + quantified benefit + urgency; density 0.91
- **PUBLISH (8.4)** — N06 pricing page copy: persuasion arc present; brand voice consistent; pain points implied; CTA clear but urgency absent; density 0.83; one generic transition phrase
- **REVIEW (7.2)** — N02 social ad variant: hook present but desire phase generic; brand tone identifiable in 60% of copy; CTA has action verb but no benefit; density 0.76; 4 filler phrases
- **REJECT (5.8)** — N06 landing page draft: feature list masquerading as copy; no arc; brand absent; CTA "Contact us" with no benefit; density 0.62; 40% padding

## Automation

| Dimension | Status | Tool / Check |
|-----------|--------|-------------|
| Persuasion | manual | Human review: verify 3-phase arc and emotional hook position |
| Brand Alignment | semi-automated | `brand_audit.py` checks voice score + archetype tags; manual for phrase-level alignment |
| Audience Fit | manual | Human review: verify persona match and pain point specificity |
| CTA Clarity | semi-automated | Grep for action verbs + benefit patterns; manual for urgency signal quality |
| Message Density | automated | `cex_token_budget.py` char ratio calculation; threshold flag at < 0.80 |

**Automation gap**: `automation_target` is semi-automated; Persuasion and Audience Fit require manual review until an LLM-judge profile for marketing copy is implemented.

## Inter-Rater Guidance

When two reviewers diverge by > 1.0 on any dimension:
1. Both reviewers annotate the specific sentence(s) driving the score difference
2. Apply the score anchor table above to the annotated sentences
3. If still divergent: escalate to N02 lead with both scored artifacts within 24h
4. N02 lead ruling is final; update calibration set if ruling reveals anchor gap

Target inter-rater agreement: ≥ 0.82 (current baseline).

## References

- AAC&U VALUE Rubrics — scoring methodology baseline: https://www.aacu.org/initiatives/value-initiative
- N06 Brand + Monetization Rubric — dual scoring model for mixed artifacts
- `brand_audit.py` v1.0 — automated brand voice dimension check
- `cex_token_budget.py` — message density calculation reference