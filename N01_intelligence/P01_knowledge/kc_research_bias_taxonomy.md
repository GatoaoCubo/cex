---
id: kc_research_bias_taxonomy
kind: knowledge_card
pillar: P01
nucleus: n01
title: "Research Bias Taxonomy for Intelligence Analysis"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: 9.1
tags: [research_bias, cognitive_bias, selection_bias, confirmation_bias, n01, analytical_envy]
tldr: "Complete taxonomy of cognitive and research biases affecting intelligence analysis: 12 bias types with detection signatures, impact severity, and mitigation strategies. Grounds the bias_audit_n01 detection protocol."
density_score: 0.92
updated: "2026-04-17"
---

<!-- 8F: F1 constrain=P01/knowledge_card F2 become=knowledge-card-builder F3 inject=bias_audit_n01+reasoning_strategy_n01+eval_framework_n01 F4 reason=Analytical Envy demands we know ALL the ways we can be wrong, not just the obvious ones -- this taxonomy makes bias detection comprehensive F5 call=cex_compile F6 produce=kc_research_bias_taxonomy.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P01_knowledge/ -->

## Definition

Research bias = systematic error in how information is sought, collected, analyzed, or presented.
Distinct from random error (noise) because it consistently skews in one direction.

Analytical Envy means KNOWING our blind spots so we can compensate for them.

## Bias Taxonomy (12 Types)

### Category 1: Source Biases

| Bias | Definition | Detection Signature | Impact | Mitigation |
|------|-----------|--------------------|---------|----|
| Selection bias | systematically choosing sources that support a view | 80%+ sources are same type/origin | H | diversify source categories |
| Availability bias | using easy-to-find data over best data | only first-page search results | M | run L2/L3 search layers |
| Publication bias | peer-reviewed literature over-represents positive results | no null results in literature review | M | include preprints, grey literature |
| Geographic bias | over-representing US/Western sources | < 5% non-English sources for global topic | M | explicitly search non-English sources |

### Category 2: Cognitive Biases

| Bias | Definition | Detection Signature | Impact | Mitigation |
|------|-----------|--------------------|---------|----|
| Confirmation bias | seeking evidence that confirms hypothesis | > 80% evidence supports initial hypothesis | H | require counter-evidence in AP-06 |
| Anchoring bias | over-relying on first piece of information | conclusion tracks closely with first source | M | read multiple sources before concluding |
| Representativeness | judging by pattern-match to prototype | "X is like Y therefore X has Y's properties" | M | demand independent evidence |
| Recency bias | over-weighting recent information | > 70% sources from past 30 days | M | include historical baseline |

### Category 3: Analytical Biases

| Bias | Definition | Detection Signature | Impact | Mitigation |
|------|-----------|--------------------|---------|----|
| Survivorship bias | analyzing only successful cases | no failure cases in sample | H | explicitly include failed cases |
| Base rate neglect | ignoring prior probability | "X does Y, therefore X will win" without market priors | H | always state base rate |
| Narrative bias | fitting data to a compelling story | data cherry-picked to fit narrative arc | H | challenge narrative with contradictory data |
| Overconfidence | assigning too-high confidence to estimates | uncertainty not acknowledged | M | apply confidence calibration |

## Bias Severity Definitions

| Severity | Definition | P-value Analogy | N01 Action |
|----------|-----------|----------------|-----------|
| H (High) | bias likely changes the conclusion | < 0.05 | reject and redo |
| M (Medium) | bias affects specific claims but not conclusion | 0.05-0.20 | add caveats |
| L (Low) | bias affects peripheral details | > 0.20 | note and proceed |

## Bias Detection Heuristics

Applied by bias_audit_n01.md (B1-B5 checks are a subset of this taxonomy):

| Heuristic | Question | Positive = bias risk |
|-----------|---------|---------------------|
| Single category | "Are all sources the same type?" | yes |
| Directional evidence | "Does evidence only support one direction?" | yes |
| Temporal cluster | "Are all sources from the same time period?" | yes |
| First-hit dependence | "Does the conclusion match the first search result?" | yes |
| Missing competitor | "Is the obvious alternative not mentioned?" | yes |
| Confidence mismatch | "Is confidence > 0.85 with < 3 sources?" | yes |
| Prototype matching | "Is the reasoning 'X is like Y, therefore...'?" | yes |
| Missing base rate | "Is a comparison made without establishing the baseline?" | yes |

## Intelligence Community Bias Mitigations

| Technique | Origin | Application |
|-----------|--------|------------|
| ACH (Analysis of Competing Hypotheses) | CIA | test all hypotheses against evidence |
| Devil's Advocate | IC standard | assign analyst to argue against conclusion |
| Red Teaming | military | outsider challenges assumption set |
| Team A / Team B | NSA | parallel teams with different instructions |
| Structured Debate | DIA | formal pro/con argumentation |

N01 automated approximation: AP-06 bias check + counter-argument requirement in AP-08.

## Comparison: Bias Mitigation Approaches

| Approach | Bias Types Covered | Automation | N01 Fit |
|----------|------------------|-----------|---------|
| None (naive research) | 0/12 | N/A | fail |
| Self-review | 3-5/12 | 0% | partial (blind spots) |
| bias_audit_n01 (B1-B5) | 5/12 | 80% | good (covers highest impact) |
| This taxonomy + audit | 12/12 | 60% | optimal |
| Human red team | 12/12 | 0% | use for highest-stakes decisions |
