---
id: scoring_rubric_research
kind: scoring_rubric
pillar: P11
nucleus: n01
title: "N01 Research Output Scoring Rubric"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: null
tags: [scoring_rubric, research_quality, n01, peer_review, analytical_envy]
tldr: "Peer-review scoring rubric for N01 research outputs: 5 dimensions with behavioral anchors at 1, 4, 7, 10. Used by llm_judge_n01 and human reviewers to assign quality scores consistently."
density_score: 0.90
---

<!-- 8F: F1 constrain=P11/scoring_rubric F2 become=scoring-rubric-builder F3 inject=eval_framework_n01+llm_judge_n01+quality_gate_intelligence+scoring_rubric_intelligence F4 reason=eval_framework defines dimensions; scoring rubric makes them operationalizable with behavioral anchors that any reviewer can apply consistently F5 call=cex_compile F6 produce=scoring_rubric_research.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P11_feedback/ -->

## Purpose

The eval_framework_n01 defines WHAT to measure.
This rubric defines HOW to score each dimension consistently:
- Behavioral anchors at 4 levels (1, 4, 7, 10)
- Common pitfalls that inflate or deflate scores
- Calibration examples for each dimension

Used by llm_judge_n01 (automated) and human peer reviewers.

## D1: Source Quality (Weight 25%)

| Score | Behavioral Anchor |
|-------|-----------------|
| 10 | All sources are primary (SEC filings, official docs, peer-reviewed papers). Every source has URL + date. Zero paywalled-but-unverified sources. |
| 7 | Majority (> 60%) primary or peer-reviewed. Some secondary (analyst reports, Tier-1 news). All sources cited. |
| 4 | Mix of secondary (blogs, press releases). Some sources without dates. 1-2 unverified. |
| 1 | Primarily forums, social media, or a single unverifiable source. |

**Common inflate pitfalls:** counting quantity over quality (10 blog links != 2 papers).
**Common deflate pitfalls:** penalizing news sources -- Tier-1 news (Reuters, WSJ) = valid secondary source.

## D2: Analytical Depth (Weight 25%)

| Score | Behavioral Anchor |
|-------|-----------------|
| 10 | First-principles analysis. Identifies root cause and mechanism. Models system dynamics. Explores counterfactual ("what if X changed"). Synthesizes across sources into novel insight. |
| 7 | Multi-factor analysis. SWOT or equivalent. Identifies causes, not just symptoms. Original interpretation of evidence. |
| 4 | Summary with some interpretation. Identifies obvious causes. Mostly paraphrases sources. |
| 1 | Pure verbatim extraction from sources. Zero original analysis. |

**Common inflate pitfalls:** mistaking jargon-heavy prose for analysis.
**Common deflate pitfalls:** penalizing conciseness -- a 200-word deep analysis outscores a 2000-word shallow one.

## D3: Comparative Coverage (Weight 25%)

| Score | Behavioral Anchor |
|-------|-----------------|
| 10 | All major market participants covered. Quantified deltas on every metric. Year-over-year comparison. Category benchmark (market average). Explicit ranking. |
| 7 | 3+ competitors compared. Quantified on 2+ metrics. Some relative ranking. |
| 4 | 1-2 competitors mentioned. Qualitative comparison only. |
| 1 | Single entity focused. No competitive context whatsoever. |

**Analytical Envy override:** D3 < 5 = automatic quality floor of 7.0 regardless of other dimensions.
This is the N01 non-negotiable: no research without comparison.

**Common inflate pitfalls:** listing competitors by name without actually comparing.
**Common deflate pitfalls:** penalizing for missing competitors who are genuinely not relevant.

## D4: Claim Confidence (Weight 15%)

| Score | Behavioral Anchor |
|-------|-----------------|
| 10 | Every key claim has explicit confidence score (0.0-1.0). Uncertainty sources named. Limitations section present. Contested claims flagged. |
| 7 | Major claims have confidence indicators (high/medium/low). Some uncertainty acknowledged. |
| 4 | Claims hedged with "likely", "probably" without evidence basis. |
| 1 | Overconfident assertions. "X is the leader" without evidence. No uncertainty acknowledgment. |

## D5: Actionability (Weight 10%)

| Score | Behavioral Anchor |
|-------|-----------------|
| 10 | 3+ specific recommendations with: who should act, what specifically, by when, and how to measure success. |
| 7 | 2+ recommendations with rationale. Somewhat specific. |
| 4 | Implications noted but vague ("should consider X"). |
| 1 | Pure description. Reader left to derive all implications. |

## Calibration Examples

### Score 9.5 Example Pattern

```
Topic: "Anthropic vs. OpenAI pricing analysis Q1 2026"
D1: Primary sources (Anthropic.com/pricing + OpenAI.com/pricing + SEC indirect)
    + Tier-1 news (FT, The Information) -- score 9
D2: Token economics model, competitive response analysis, trajectory -- score 9
D3: vs. OpenAI + Google + Mistral + Cohere, 4 metrics each -- score 10
D4: Confidence scores on every finding, contested data flagged -- score 9
D5: 3 specific recommendations for enterprise buyers -- score 9
Result: (9+9+10+9+9) weighted = 9.4, no bias penalty = 9.4
```

### Score 6.0 Example Pattern

```
Topic: "AI market analysis"
D1: Mostly TechCrunch + Twitter -- score 4
D2: List of facts, no synthesis -- score 4
D3: Mentions 2 companies without comparison -- score 4
D4: "AI is growing fast" -- score 3
D5: "Consider investing in AI" -- score 3
Result: (4+4+4+3+3) weighted = 3.8, but floor at 6 with warning
```

## Related Artifacts

| Artifact | Relationship |
|----------|-------------|
| `P07_evals/eval_framework_n01.md` | defines the dimensions this rubric scores |
| `P07_evals/llm_judge_n01.md` | uses this rubric in judge prompt |
| `P11_feedback/quality_gate_intelligence.md` | complementary hard gates |
| `P07_evals/scoring_rubric_intelligence.md` | general-purpose predecessor |
